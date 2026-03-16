import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import base64
import os
from Perguntas import DIAGNOSTICO_CONFIG, GDRIVE_CONFIG, LOGO_URL, LISTA_ESTADOS, LISTA_SETORES, ACOLHIMENTO_CONFIG, CATALOGO_MANDALA, CATALOGO_TRILHA, LISTA_DOR_PRINCIPAL
from Interface import renderizar_area_diagnostico, renderizar_acolhimento
from Formatacoes import formatar_cnpj, formatar_cpf, formatar_telefone, formatar_moeda
from gdrive_utils import gerir_pasta_empresa, upload_arquivo
from pdf_generator import gerar_ata_interna, gerar_plano_cliente
from gestao_salas import renderizar_gestao_salas

# NUVEM: Recria as senhas a partir do cofre ---
if not os.path.exists('token.pickle') and "google" in st.secrets:
    with open('token.pickle', 'wb') as f:
        f.write(base64.b64decode(st.secrets["google"]["token_pickle"]))

if not os.path.exists('client_secret.json') and "client_secret" in st.secrets:
    with open('client_secret.json', 'w') as f:
        f.write(st.secrets["client_secret"])
# -------------------------------------------------------------------

# --- FUNÇÃO PARA LOGO LOCAL ---
def get_base64_logo():
    for ext in ["png", "jpg", "jpeg"]:
        path = f"LogoHorizonte1.{ext}"
        if os.path.exists(path):
            try:
                with open(path, "rb") as f:
                    data = base64.b64encode(f.read()).decode("utf-8")
                    return f"data:image/{ext if ext != 'jpg' else 'jpeg'};base64,{data.replace('\n', '')}"
            except Exception:
                continue
    return LOGO_URL

logo_src = get_base64_logo()

# --- INICIALIZAÇÃO DO ESTADO ---
def inicializar_estado():
    if 'dados_empresa' not in st.session_state:
        st.session_state['dados_empresa'] = {}

st.set_page_config(page_title="Hub Horizonte", layout="wide")
inicializar_estado()

# --- ESTILO CSS ---
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Inter:wght@300;400;600&display=swap');
.stApp {{ background: #FFFFFF; }}
.custom-header {{
    background: #FFFFFF; padding: 1.5rem 1rem; border-radius: 0 0 20px 20px; text-align: center;
    margin-bottom: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03); border-bottom: 1px solid #E2E8F0;
}}
.logo-img {{ max-height: 320px; width: auto; }}
[data-testid="stSidebar"] {{ background-color: #0A1128; }}
[data-testid="stSidebar"] * {{ color: #E2E8F0 !important; }}
.stButton > button {{
    background: linear-gradient(90deg, #121A3B 0%, #0077B6 100%) !important;
    color: white !important; font-weight: 700 !important; border-radius: 12px !important;
    width: 100% !important; height: 4.8em !important; text-transform: uppercase;
}}
</style>
<div class="custom-header">
    <img src="{logo_src}" class="logo-img">
    <p style="font-size: 1rem; color: #64748b; letter-spacing: 4px; margin-top: -60px; text-transform: uppercase;">SISTEMA DE GESTÃO</p>
</div>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO PRINCIPAL ---
escolha = st.sidebar.radio("Navegação Principal", ["Acolhimento", "Diagnóstico Inicial", "Reserva de Salas"], key="nav_main")

# Inicialização de variáveis para evitar erros
res_acolhimento = {}
res_diagnostico = {}
dor_principal = "N/A"
sols_detalhadas = []
lista_participantes = []
empresa = ""
cnpj_input = ""
consultor_responsavel = ""
cdl_bh = "Não"
num_associado = ""
outra_cdl = "Não"
nome_municipio_cdl = ""
loja_fisica = "Não"
tempo_fisica = ""
loja_virtual = "Não"
tempo_virtual = ""
interesse_em_ter = "N/A"

# --- LÓGICA DE EXIBIÇÃO POR PÁGINA ---

if escolha in ["Acolhimento", "Diagnóstico Inicial"]:
    
    # A CHAVE SELETORA (Fica centralizada e sozinha no início) - SEM EMOJIS PRA NÃO DAR BUG!
    st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Qual é o perfil do cliente atendido?</h3>", unsafe_allow_html=True)
    col_vazia1, col_radio, col_vazia2 = st.columns([1, 2, 1])
    with col_radio:
        tipo_cliente = st.radio(
            label="Perfil",
            options=["Pessoa Jurídica (PJ)", "Pessoa Física (PF)"],
            horizontal=True,
            index=None, # Mantém tudo invisível até clicar
            label_visibility="collapsed"
        )
    
    st.divider()

    # Só mostra o resto se ele tiver clicado em algo
    if tipo_cliente:
        # Variável para saber fácil quem é quem
        is_pj = (tipo_cliente == "Pessoa Jurídica (PJ)")
        
        # --- SEÇÃO 1: DADOS INICIAIS ---
        st.header("Dados Principais")
        col_topo1, col_topo2, col_topo3 = st.columns([1, 1, 1])
        with col_topo1:
            data_atendimento = st.date_input("Data do Atendimento", datetime.now(), format="DD/MM/YYYY", key="input_data")
        with col_topo2:
            consultor_responsavel = st.text_input("Consultor Responsável", key="input_consultor")
        with col_topo3:
            lbl_nome = "Nome da Empresa" if is_pj else "Nome Completo"
            empresa = st.text_input(lbl_nome, key="input_empresa")

        col_a, col_b = st.columns(2)
        with col_a:
            lbl_doc = "CNPJ" if is_pj else "CPF"
            cnpj_input = st.text_input(lbl_doc, placeholder="00.000.000/0000-00" if is_pj else "000.000.000-00", key="input_cnpj")
            
            lbl_ano = "Ano de Fundação" if is_pj else "Data de Nascimento"
            ano_fundacao = st.text_input(lbl_ano, key="input_ano")
            
            setor = st.selectbox("Setor de Atuação", LISTA_SETORES, key="input_setor", index=None, placeholder="Selecione o setor...")
            
            lbl_vende = "O que vende? Quais os serviços prestados?" if is_pj else "O que faz? Quais serviços presta?"
            o_que_vende = st.text_area(lbl_vende, key="input_vende")
        with col_b:
            lbl_end = "Endereço do Negócio" if is_pj else "Endereço"
            endereco_negocio = st.text_input(lbl_end, key="input_endereco")
            
            tipo_endereco = st.radio("Tipo de Endereço", ["Comercial", "Residencial"], horizontal=True, key="input_tipo_end", index=None)
            
            col_estado, col_municipio = st.columns([1, 2])
            with col_estado:
                estado = st.selectbox("Estado", [""] + LISTA_ESTADOS, key="input_uf", index=None, placeholder="UF")
            with col_municipio:
                municipio = st.text_input("Município", key="input_municipio")
            
            lbl_contato = "Contato Institucional" if is_pj else "Telefone / WhatsApp "
            contato_negocio_input = st.text_input(lbl_contato, placeholder="(00) 00000-0000", key="input_tel")

        col_desc1, col_desc2 = st.columns(2)
        with col_desc1:
            lbl_obj = "Qual o maior objetivo com o negócio? Onde quer chegar?" if is_pj else "Qual o seu maior objetivo profissional? Onde quer chegar?"
            objetivo_negocio = st.text_area(lbl_obj, key="input_objetivo")
        with col_desc2:
            desafios_negocio = st.text_area("Quais os principais desafios identificados?", key="input_desafios")

        st.markdown("<hr style='border-top: 1px dashed #cbd5e1; margin: 30px 0;'>", unsafe_allow_html=True)
        col_c, col_d = st.columns(2)
        with col_c:
            col_cdl_bh1, col_cdl_bh2 = st.columns([1, 1])
            with col_cdl_bh1:
                cdl_bh = st.radio("É associado da CDL/BH?", ["Não", "Sim"], horizontal=True, key="input_cdlbh", index=None)
            with col_cdl_bh2:
                if cdl_bh == "Sim":
                    num_associado = st.text_input("Nº de Associado", key="input_num_assoc")
            
            if cdl_bh == "Não": 
                col_cdl_outra1, col_cdl_outra2 = st.columns([1, 1])
                with col_cdl_outra1:
                    outra_cdl = st.radio("É associado de outra CDL?", ["Não", "Sim"], horizontal=True, key="input_outra_cdl", index=None)
                with col_cdl_outra2:
                    if outra_cdl == "Sim":
                        nome_municipio_cdl = st.text_input("Estado / Município da CDL", key="input_mun_cdl")

            if is_pj:
                num_funcionarios = st.number_input("Número de colaboradores da empresa atualmente", min_value=0, step=1, key="input_colaboradores")
            else:
                num_funcionarios = 0 

        with col_d:
            col_lf1, col_lf2 = st.columns([1, 1])
            with col_lf1:
                loja_fisica = st.radio("Possui espaço físico para atendimento?", ["Não", "Sim"], horizontal=True, key="input_lf", index=None)
            with col_lf2:
                if loja_fisica == "Sim":
                    tempo_fisica = st.text_input("Há quanto tempo?", key="input_tempo_lf")

            col_lv1, col_lv2 = st.columns([1, 1])
            with col_lv1:
                loja_virtual = st.radio("Vende pela internet (Loja Virtual/Redes)?", ["Não", "Sim"], horizontal=True, key="input_lv", index=None)
            with col_lv2:
                if loja_virtual == "Sim":
                    tempo_virtual = st.text_input("Há quanto tempo?", key="input_tempo_lv")
                    interesse_em_ter = "Não se aplica"
            if loja_fisica == "Não" or loja_virtual == "Não":
                interesse_em_ter = st.radio("Tem interesse em expandir para onde ainda não atua?", ["Não", "Sim", "Talvez"], horizontal=True, key="input_interesse", index=None)

        st.divider()

        # --- SEÇÃO 2: REPRESENTANTES ---
        
        # MÁGICA DO AUTO-PREENCHIMENTO: Injetando os dados direto no "cérebro" do Streamlit
        if not is_pj:
            st.session_state["p_nome_0"] = st.session_state.get("input_empresa", "")
            st.session_state["p_cpf_0"] = st.session_state.get("input_cnpj", "")
            st.session_state["p_cel_0"] = st.session_state.get("input_tel", "")

        st.header("Representantes e Participantes")
        num_participantes = st.number_input("Número de pessoas presentes", 1, 10, 1, key="count_part")
        for i in range(num_participantes):
            st.markdown(f"**Pessoa {i+1}**")
            col_p1, col_p2, col_p3 = st.columns([2, 1, 1])
            with col_p1:
                p_nome = st.text_input(f"Nome", key=f"p_nome_{i}")
            with col_p2:
                p_cargo = st.text_input(f"Cargo", key=f"p_cargo_{i}")
            with col_p3:
                p_fundador = st.selectbox(f"É fundador(a)?", ["Sim", "Não"], key=f"p_fun_{i}")
            
            col_p4, col_p5, col_p6 = st.columns([1, 1, 1])
            with col_p4:
                p_cpf = st.text_input(f"CPF", key=f"p_cpf_{i}", placeholder="000.000.000-00")
            with col_p5:
                p_tempo_empresa = st.text_input(f"Tempo na Empresa/Negócio", key=f"p_tempo_{i}")
            with col_p6:
                p_celular = st.text_input(f"Celular para contato", key=f"p_cel_{i}", placeholder="(00) 00000-0000")
            
            p_email = st.text_input(f"E-mail", key=f"p_email_{i}")
            
            if p_nome:
                lista_participantes.append({
                    "nome": p_nome, "cargo": p_cargo, "email": p_email,
                    "celular": formatar_telefone(p_celular), "fundador": p_fundador,
                    "cpf": formatar_cpf(p_cpf), "tempo": p_tempo_empresa
                })
        st.divider()

        # --- CONTEÚDO ESPECÍFICO ---
        if escolha == "Diagnóstico Inicial":
            st.header("Diagnóstico Inicial")
            for nome_area in list(DIAGNOSTICO_CONFIG.keys()):
                with st.expander(f"Área: {nome_area}"):
                    res_diagnostico[nome_area] = renderizar_area_diagnostico(nome_area)
            st.markdown("#### Visão Geral do Diagnóstico - Gráfico de Radar")
            
            # Puxa os nomes curtinhos e as notas automáticas que o sistema calculou
            labels_diag = [DIAGNOSTICO_CONFIG[area]["abreviacao"] for area in res_diagnostico]
            valores_diag = [float(res_diagnostico[area]["nota_calculada"]) for area in res_diagnostico]
            
            # Desenha o gráfico se tiver algum valor
            if valores_diag:
                fig_diag = go.Figure(data=go.Scatterpolar(
                    r=valores_diag + [valores_diag[0]], 
                    theta=labels_diag + [labels_diag[0]], 
                    fill='toself', 
                    fillcolor='rgba(0, 180, 216, 0.25)', 
                    line=dict(color='#121A3B', width=3)
                ))
                # Nota: Diagnóstico vai de 0 a 4!
                fig_diag.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 4], tickvals=[0, 1, 2, 3, 4])), showlegend=False)
                st.plotly_chart(fig_diag, use_container_width=True)

            st.divider()

            st.header("Plano de Ação Estratégico")
            dor_principal = st.selectbox("Principal Dor Identificada", LISTA_DOR_PRINCIPAL, key="dor_main", index=None, placeholder="Selecione a dor principal...")
            
            st.write("Você pode indicar até 4 soluções para este plano de ação:")
            
            for i in range(4):
                st.markdown(f"**Indicação de Solução {i+1}**")
                
                # A chave seletora inteligente para cada solução!
                direcionamento_diag = st.selectbox(
                    "Direcionamento", 
                    ["Nenhuma", "Eventos e Programas", "Mandala de Soluções", "Trilha do Conhecimento", "Negociação de Nova Parceria"],
                    key=f"dir_diag_{i}",
                    index=0 # Começa no "Nenhuma" para esconder as perguntas
                )
                
                if direcionamento_diag != "Nenhuma":
                    s_nome = None
                    info = {}
                    
                    # 1. EVENTOS E PROGRAMAS
                    if direcionamento_diag == "Eventos e Programas":
                        s_nome = st.text_input("Solução Ofertada (Campo Aberto):", key=f"s_nome_ev_{i}", placeholder="Ex: Inscrição no Bootcamp")
                        info = {"descricao": "Participação em evento ou programa parceiro.", "parceiro": "Hub Horizonte / Parceiros", "custo": "A consultar"}
                        
                    # 2. MANDALA DE SOLUÇÕES
                    elif direcionamento_diag == "Mandala de Soluções":
                        s_nome = st.selectbox("Solução Ofertada:", list(CATALOGO_MANDALA.keys()), key=f"s_nome_man_{i}", index=None)
                        if s_nome:
                            info_raw = CATALOGO_MANDALA[s_nome]
                            info = {"descricao": info_raw["descricao"], "parceiro": info_raw["instituicao"], "custo": info_raw["custo"]}
                            st.info(f"**Descrição:** {info['descricao']}\n\n**Instituição:** {info['parceiro']} | **Custo:** {info['custo']}")
                            
                    # 3. TRILHA DO CONHECIMENTO
                    elif direcionamento_diag == "Trilha do Conhecimento":
                        s_nome = st.selectbox("Solução Ofertada:", list(CATALOGO_TRILHA.keys()), key=f"s_nome_tri_{i}", index=None)
                        if s_nome:
                            info_raw = CATALOGO_TRILHA[s_nome]
                            info = {"descricao": info_raw["descricao"], "parceiro": info_raw["instituicao"], "custo": info_raw["custo"]}
                            st.info(f"**Descrição:** {info['descricao']}\n\n**Instituição:** {info['parceiro']} | **Carga Horária:** {info_raw['carga_horaria']} | **Custo:** {info['custo']}\n\n**Link:** {info_raw['link']}")
                            
                    # 4. NEGOCIAÇÃO DE NOVA PARCERIA
                    elif direcionamento_diag == "Negociação de Nova Parceria":
                        s_nome = st.text_input("Foco da Parceria (Campo Aberto):", key=f"s_nome_parc_{i}", placeholder="Ex: Buscar startup de logística")
                        info = {"descricao": "Prospecção e negociação de nova parceria estratégica para suprir gargalo.", "parceiro": "A definir", "custo": "A consultar"}

                    # Se o consultor escolheu/digitou uma solução, abre as caixas finais
                    # Se o consultor escolheu/digitou uma solução, abre as caixas finais
                    if s_nome:
                        s_motivo = st.text_area(f"Motivo da indicação", key=f"s_mot_{i}")
                        
                        # Resgatando o Link e a Carga Horária se for Trilha!
                        link_extra = ""
                        carga_extra = ""
                        if direcionamento_diag == "Trilha do Conhecimento":
                            link_extra = CATALOGO_TRILHA[s_nome].get("link", "")
                            carga_extra = CATALOGO_TRILHA[s_nome].get("carga_horaria", "")
                        
                        # Salva empacotadinho com TUDO dentro!
                        sols_detalhadas.append({
                            "solucao": s_nome, 
                            "parceiro": info['parceiro'], 
                            "custo": info['custo'], 
                            "descricao": info['descricao'], 
                            "motivo": s_motivo, 
                            "prazos": "", # <-- Vazio pra não quebrar
                            "link": link_extra,
                            "carga_horaria": carga_extra
                        })
                        
            # --- CAMPO GERAL DE PRAZOS (FORA DO LOOP DAS 4 SOLUÇÕES) ---
            st.divider()
            st.markdown("**Prazos, observações e próximos passos**")
            prazos_gerais = st.text_area("Quais são os checkpoints, prazos ou observações gerais para a execução deste plano de ação?", key="prazos_gerais_diag")

        elif escolha == "Acolhimento":
            res_acolhimento = renderizar_acolhimento(is_pj)
            dor_principal = res_acolhimento.get("acolh_dor_principal", "N/A")

        # --- BOTÃO FINALIZAR ---
        st.divider()
        if st.button("FINALIZAR E GERAR DOCUMENTOS", key="btn_final_oficial"):
            if not empresa or not cnpj_input or not consultor_responsavel:
                st.error("Campos obrigatórios: Nome, Documento (CNPJ/CPF) e Consultor.")
            else:
                id_raiz = GDRIVE_CONFIG['ID_DIAGNOSTICO'] if escolha == "Diagnóstico Inicial" else GDRIVE_CONFIG['ID_ACOLHIMENTO']
                id_pasta_cliente = gerir_pasta_empresa(empresa, cnpj_input, id_raiz)
                
                if id_pasta_cliente:
                    with st.spinner("Processando arquivos e enviando para o Drive..."):
                        try:
                            if escolha == "Diagnóstico Inicial":
                                labels = [DIAGNOSTICO_CONFIG[area]["abreviacao"] for area in res_diagnostico]
                                valores = [float(res_diagnostico[area]["nota_calculada"]) for area in res_diagnostico]
                            else:
                                radar_data = res_acolhimento.get('radar', {})
                                labels = [radar_data[area]['abreviacao'] for area in radar_data]
                                valores = [radar_data[area]['nota_radar'] for area in radar_data]

                            fig = go.Figure(data=go.Scatterpolar(
                                r=valores + [valores[0]], theta=labels + [labels[0]], 
                                fill='toself', fillcolor='rgba(0, 180, 216, 0.25)', line=dict(color='#121A3B', width=3)
                            ))

                            tick_exato = [0, 1, 2, 3, 4, 5] if escolha != "Diagnóstico Inicial" else [0, 1, 2, 3, 4]
                            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5 if escolha != "Diagnóstico Inicial" else 4], tickvals=tick_exato)), showlegend=False)
                            caminho_radar = "radar_temp.png"
                            fig.write_image(caminho_radar, engine="kaleido")

                            doc_formatado = formatar_cnpj(cnpj_input) if is_pj else formatar_cpf(cnpj_input)

                            dados_pdf = {
                                'empresa': empresa, 'cnpj': doc_formatado, 'consultor': consultor_responsavel,
                                'data': data_atendimento.strftime("%d/%m/%Y"), 'contato': formatar_telefone(contato_negocio_input),
                                'endereco': endereco_negocio, 'tipo_endereco': tipo_endereco, 'municipio': municipio, 'estado': estado,
                                'setor': setor, 'o_que_vende': o_que_vende, 'objetivo': objetivo_negocio, 'desafios': desafios_negocio,
                                'cdl_bh': cdl_bh, 'num_associado': num_associado, 'n_colaboradores': str(num_funcionarios),
                                'ano_fundacao': ano_fundacao, 'loja_fisica': loja_fisica, 'loja_virtual': loja_virtual,
                                'interesse_expansao': interesse_em_ter, 'participantes': lista_participantes,
                                'dor_principal': dor_principal, 'solucoes': sols_detalhadas,
                                'prazos_gerais': st.session_state.get("prazos_gerais_diag", "")
                            }

                            nome_pdf_ata = f"Ata_{empresa.replace(' ', '_')}.pdf"
                            nome_pdf_plano = f"Plano_de_ação_{empresa.replace(' ', '_')}.pdf"
                            
                            gerar_ata_interna(dados_pdf, res_diagnostico if escolha == "Diagnóstico Inicial" else res_acolhimento, caminho_radar, nome_pdf_ata, escolha)
                            gerar_plano_cliente(dados_pdf, res_diagnostico if escolha == "Diagnóstico Inicial" else res_acolhimento, caminho_radar, nome_pdf_plano, escolha)
                            
                            if upload_arquivo(nome_pdf_ata, id_pasta_cliente) and upload_arquivo(nome_pdf_plano, id_pasta_cliente):
                                st.success("Documentos enviados com sucesso para o Drive!")
                                #st.plotly_chart(fig)
                                col_d1, col_d2 = st.columns(2)
                                with col_d1: st.download_button("Baixar Ata Interna", open(nome_pdf_ata, "rb"), nome_pdf_ata)
                                with col_d2: st.download_button("Baixar Plano de Ação", open(nome_pdf_plano, "rb"), nome_pdf_plano)
                            else:
                                st.error("Erro no upload para o Drive. Verifique a conexão.")
                        except Exception as e:
                            st.error(f"Erro no processamento: {e}")

# --- SEÇÃO RESERVA DE SALAS ---
elif escolha == "Reserva de Salas":
    renderizar_gestao_salas()