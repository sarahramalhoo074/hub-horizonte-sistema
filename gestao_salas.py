import streamlit as st
import gspread
import pickle
import pandas as pd
from datetime import datetime
from googleapiclient.discovery import build
from gdrive_utils import get_gdrive_service

def conectar_planilha():
    """Conecta o sistema à sua planilha do Google Sheets."""
    get_gdrive_service() # Garante que a janela de login do Google abra
    
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    
    gc = gspread.authorize(creds)
    return gc.open("Gestao_Salas_Horizonte"), creds

def criar_evento_agenda(creds, resumo, descricao, data_str, horario_str):
    """Cria o evento automaticamente no Google Agenda"""
    try:
        service = build('calendar', 'v3', credentials=creds)
        
        # VERIFICAÇÃO INTELIGENTE: Tem tracinho ou não?
        if " - " in horario_str:
            hora_inicio, hora_fim = horario_str.split(" - ")
        else:
            # Se for do formato antigo, assume 1 hora de duração padrão
            hora_inicio = horario_str
            h = int(hora_inicio.split(":")[0])
            m = hora_inicio.split(":")[1]
            hora_fim = f"{h+1:02d}:{m}"
        
        start_dt = datetime.strptime(f"{data_str} {hora_inicio}", "%d/%m/%Y %H:%M").isoformat()
        end_dt = datetime.strptime(f"{data_str} {hora_fim}", "%d/%m/%Y %H:%M").isoformat()
        
        event = {
          'summary': resumo,
          'description': descricao,
          'start': {
            'dateTime': start_dt,
            'timeZone': 'America/Sao_Paulo',
          },
          'end': {
            'dateTime': end_dt,
            'timeZone': 'America/Sao_Paulo',
          },
        }
        
        service.events().insert(calendarId='primary', body=event).execute()
        return True
    except Exception as e:
        st.error(f"Erro ao criar evento na agenda: {e}")
        return False

def renderizar_gestao_salas():
    st.header("Reserva de Salas")
    st.write("Controle a disponibilidade dos espaços do Hub Horizonte.")
    
    try:
        planilha, creds = conectar_planilha()
        aba_horarios = planilha.worksheet("Horarios")
        aba_pedidos = planilha.worksheet("Pedidos")
        
        tab_cadastro, tab_pedidos = st.tabs(["Cadastrar Horários Disponíveis", "Aprovar Reservas"])
        
        # --- ABA 1: CADASTRAR HORÁRIOS ---
        with tab_cadastro:
            st.subheader("Adicionar horários em lote")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                nova_sala = st.selectbox("Sala", ["Sala de Reuniões 1", "Sala de Reuniões 2", "Estúdio", "Auditório"])
            with col2:
                nova_data = st.date_input("Data")
            with col3:
                # Cria blocos de 1 hora inteira
                opcoes_horas = [f"{h:02d}:00 - {h+1:02d}:00" for h in range(8, 20)]
                novos_horarios = st.multiselect("Horários Disponíveis", opcoes_horas, placeholder="Escolha vários...")
            
            if st.button("Cadastrar Horários Selecionados", use_container_width=False):
                if not novos_horarios:
                    st.warning("Selecione pelo menos um horário na lista!")
                else:
                    data_str = nova_data.strftime("%d/%m/%Y")
                    novas_linhas = []
                    
                    for hora in novos_horarios:
                        novas_linhas.append([nova_sala, data_str, hora, "Disponível"])
                    
                    aba_horarios.append_rows(novas_linhas)
                    st.success(f"Show! {len(novos_horarios)} horários cadastrados para o dia {data_str}.")
                
            st.divider()
            st.subheader("Seus Horários Cadastrados")
            try:
                dados_horarios = aba_horarios.get_all_records()
                if dados_horarios:
                    st.dataframe(pd.DataFrame(dados_horarios), use_container_width=True, hide_index=True)
                else:
                    st.info("Nenhum horário cadastrado ainda.")
            except:
                st.warning("Planilha sem dados ou sem cabeçalho.")

        # --- ABA 2: APROVAR PEDIDOS (A MÁGICA) ---
        with tab_pedidos:
            st.subheader("Pedidos Pendentes de Aprovação")
            try:
                todos_pedidos = aba_pedidos.get_all_records()
                
                # Filtra apenas os pedidos com status "Pendente"
                pendentes = []
                for idx, pedido in enumerate(todos_pedidos):
                    if pedido.get("Status") == "Pendente":
                        pedido["linha_planilha"] = idx + 2
                        pendentes.append(pedido)
                
                if not pendentes:
                    st.success("Tudo tranquilo por aqui! Nenhum pedido pendente.")
                else:
                    for ped in pendentes:
                        with st.expander(f" {ped['Data']} às {ped['Horario']} | {ped['Sala']} | Solicitante: {ped['Nome']}", expanded=True):
                            st.write(f"**E-mail de contato:** {ped['Email']}")
                            
                            col_btn1, col_btn2 = st.columns(2)
                            
                            with col_btn1:
                                if st.button(f"Aprovar", key=f"btn_aprovar_{ped['linha_planilha']}"):
                                    with st.spinner("Criando evento na agenda..."):
                                        resumo = f"Reserva {ped['Sala']} - {ped['Nome']}"
                                        descricao = f"Reserva solicitada via Sistema Hub Horizonte.\nContato: {ped['Email']}"
                                        
                                        sucesso = criar_evento_agenda(creds, resumo, descricao, ped['Data'], ped['Horario'])
                                        
                                        if sucesso:
                                            # 1. Muda status do pedido
                                            aba_pedidos.update_cell(ped['linha_planilha'], 6, "Aprovado")
                                            
                                            # 2. Muda status do horário na aba Horarios para "Reservado" (NOVIDADE AQUI!)
                                            celulas_sala = aba_horarios.col_values(1)
                                            celulas_data = aba_horarios.col_values(2)
                                            celulas_hora = aba_horarios.col_values(3)
                                            
                                            for i in range(1, len(celulas_sala)):
                                                if celulas_sala[i] == ped['Sala'] and celulas_data[i] == ped['Data'] and celulas_hora[i] == ped['Horario']:
                                                    aba_horarios.update_cell(i + 1, 4, "Reservado")
                                                    break
                                            
                                            st.success("Reserva aprovada!")
                                            st.rerun() 
                                            
                            with col_btn2:
                                if st.button(f"Reprovar", key=f"btn_reprovar_{ped['linha_planilha']}"):
                                    with st.spinner("Cancelando reserva e liberando a sala..."):
                                        # 1. Reprova na aba de pedidos
                                        aba_pedidos.update_cell(ped['linha_planilha'], 6, "Reprovado")
                                        
                                        # 2. Devolve a sala pro público
                                        celulas_sala = aba_horarios.col_values(1)
                                        celulas_data = aba_horarios.col_values(2)
                                        celulas_hora = aba_horarios.col_values(3)
                                        
                                        for i in range(1, len(celulas_sala)):
                                            if celulas_sala[i] == ped['Sala'] and celulas_data[i] == ped['Data'] and celulas_hora[i] == ped['Horario']:
                                                aba_horarios.update_cell(i + 1, 4, "Disponível")
                                                break
                                                
                                        st.warning("Reserva reprovada e horário liberado novamente!")
                                        st.rerun()

            except Exception as e:
                st.warning(f"Erro ao processar pedidos: {e}")

    except Exception as e:
        st.error(f"Erro ao conectar com a planilha: {e}")