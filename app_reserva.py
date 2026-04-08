import streamlit as st
import gspread
import pickle
import pandas as pd
import os
import base64

# --- MÁGICA DA NUVEM: Recria as senhas a partir do cofre secreto ---
if not os.path.exists('token.pickle') and "google" in st.secrets:
    with open('token.pickle', 'wb') as f:
        f.write(base64.b64decode(st.secrets["google"]["token_pickle"]))

if not os.path.exists('client_secret.json') and "client_secret" in st.secrets:
    with open('client_secret.json', 'w') as f:
        f.write(st.secrets["client_secret"])
# -------------------------------------------------------------------

# --- CONFIGURAÇÃO DA PÁGINA E ESTILO ---
st.set_page_config(page_title="Reserva de Salas -Horizonte", layout="centered")

def get_base64_logo():
    for ext in ["png", "jpg", "jpeg"]:
        path = f"LogoHorizonte1.{ext}"
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
                return f"data:image/{ext if ext != 'jpg' else 'jpeg'};base64,{data.replace('\n', '')}"
    return ""

logo_src = get_base64_logo()

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
.stApp {{ background: #F8FAFC; }}
.custom-header {{
    background: #FFFFFF; padding: 2rem; border-radius: 20px; text-align: center;
    margin-bottom: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-bottom: 3px solid #00B4D8;
}}
.logo-img {{ max-height: 280px; width: auto; }}
h1, h2, h3, p {{ font-family: 'Montserrat', sans-serif; color: #0F172A; }}
.stButton > button {{
    background: linear-gradient(90deg, #0A1128 0%, #006699 100%) !important;
    color: #FFFFFF !important; 
    font-weight: 700 !important; 
    border-radius: 8px !important;
    width: 100% !important; 
    padding: 15px !important; 
    text-transform: uppercase; 
    letter-spacing: 1px;
    border: none !important; /* Tira qualquer bordinha cinza que o Streamlit coloque */
}}

/* Essa é a linha mágica que obriga o texto de dentro a ficar branco! */
.stButton > button * {{
    color: #FFFFFF !important;
}}
div[data-baseweb="select"] > div, input {{ background-color: #FFFFFF !important; }}
</style>
<div class="custom-header">
    <img src="{logo_src}" class="logo-img">
    <h2 style="margin-top: -45px; color: #121A3B; font-weight: 600;">Solicitação de Espaços</h2>
    <p style="color: #64748b; font-weight: 600;">Selecione os horários disponíveis abaixo</p>
</div>
""", unsafe_allow_html=True)

# --- CONEXÃO COM O GOOGLE SHEETS ---
@st.cache_resource(ttl=30) # Atualiza a leitura a cada 30 segundos
def conectar_planilha():
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    gc = gspread.authorize(creds)
    return gc.open("Gestao_Salas_Horizonte")

try:
    planilha = conectar_planilha()
    aba_horarios = planilha.worksheet("Horarios")
    aba_pedidos = planilha.worksheet("Pedidos")
    
    # Lendo os dados
    dados_horarios = aba_horarios.get_all_records()
    df = pd.DataFrame(dados_horarios)
    
    # Filtra apenas os que estão "Disponível"
    if not df.empty and "Status" in df.columns:
        df_disponivel = df[df["Status"] == "Disponível"]
    else:
        df_disponivel = pd.DataFrame()

    if df_disponivel.empty:
        st.warning("Poxa! No momento não temos nenhum horário disponível para reserva. Volte novamente mais tarde.")
    else:
        # --- FORMULÁRIO DE RESERVA ---
        st.markdown("### 1️- O que você precisa?")
        
        # Cascateamento inteligente
        salas_disponiveis = df_disponivel["Sala"].unique().tolist()
        sala_escolhida = st.selectbox("Escolha o espaço:", salas_disponiveis, index=None, placeholder="Selecione uma sala...")
        
        if sala_escolhida:
            df_sala = df_disponivel[df_disponivel["Sala"] == sala_escolhida]
            datas_disponiveis = df_sala["Data"].unique().tolist()
            
            data_escolhida = st.selectbox("Escolha a data:", datas_disponiveis, index=None, placeholder="Selecione um dia...")
            
            if data_escolhida:
                df_final = df_sala[df_sala["Data"] == data_escolhida]
                horarios_disponiveis = df_final["Horario"].tolist()
                
                horarios_escolhidos = st.multiselect("Escolha os blocos de horário (você pode selecionar vários):", horarios_disponiveis, placeholder="Selecione os horários...")
                
                if horarios_escolhidos:
                    st.divider()
                    st.markdown("### 2️- Seus Dados")
                    col1, col2 = st.columns(2)
                    with col1:
                        nome_solicitante = st.text_input("Nome Completo")
                    with col2:
                        email_solicitante = st.text_input("E-mail para receber confirmação")
                    
                    st.write("") # Espaço
                    if st.button("Confirmar Solicitação"):
                        if not nome_solicitante or not email_solicitante:
                            st.error("Por favor, preencha seu nome e e-mail para continuarmos!")
                        else:
                            with st.spinner("Reservando horários"):
                                # Puxa todas as colunas para a gente achar a linha certa
                                celulas_sala = aba_horarios.col_values(1)
                                celulas_data = aba_horarios.col_values(2)
                                celulas_hora = aba_horarios.col_values(3)
                                
                                linhas_pedidos = []
                                
                                for horario in horarios_escolhidos:
                                    for i in range(1, len(celulas_sala)):
                                        if celulas_sala[i] == sala_escolhida and celulas_data[i] == data_escolhida and celulas_hora[i] == horario:
                                            linha_planilha = i + 1 # +1 porque o índice do python começa em 0
                                            
                                            # Atualiza o status na aba Horarios
                                            aba_horarios.update_cell(linha_planilha, 4, "Aguardando Aprovação")
                                            
                                            # Prepara o pedido para a aba Pedidos
                                            linhas_pedidos.append([nome_solicitante, email_solicitante, sala_escolhida, data_escolhida, horario, "Pendente"])
                                            break
                                
                                if linhas_pedidos:
                                    aba_pedidos.append_rows(linhas_pedidos)
                                    st.success(f" Ótimo, {nome_solicitante.split()[0]}! Sua solicitação foi enviada para o Horizonte. Você receberá a confirmação no e-mail {email_solicitante} em breve.")
                                    # Limpa a tela após 3 segundos (opcional, ele avisa que deu certo e para)
                                    
except Exception as e:
    st.error(f"Sistema em manutenção rápida. Tente novamente em alguns minutos. Erro: {e}")
