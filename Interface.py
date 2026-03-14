# Funções para gerar a interface do Streamlit
import streamlit as st
from Perguntas import DIAGNOSTICO_CONFIG, ACOLHIMENTO_CONFIG, LISTA_DIRECIONAMENTO, LISTA_DOR_PRINCIPAL, LISTA_SOLUCAO_OFERTADA
from Formatacoes import formatar_moeda

def renderizar_pergunta(pergunta, key_prefix=""):
    """
    Renderiza uma pergunta (Radio ou Texto) no Streamlit.
    """
    unique_key = f"{key_prefix}_{pergunta['id']}"
    
    if pergunta.get("tipo") == "texto":
        resposta_selecionada = st.text_area(
            label=pergunta["pergunta"],
            key=unique_key,
            placeholder="Escreva a resposta aqui..."
        )
    elif pergunta.get("tipo") == "radio":
        resposta_selecionada = st.radio(
            label=pergunta["pergunta"],
            options=pergunta["opcoes"],
            key=unique_key,
            index=None # <-- ADICIONADO AQUI
        )
    else:
        opcoes_texto = [op["texto"] for op in pergunta["opcoes"]]
        resposta_selecionada = st.radio(
            label=pergunta["pergunta"],
            options=opcoes_texto,
            key=unique_key,
            index=None # <-- ADICIONADO AQUI
        )
    return resposta_selecionada

def renderizar_area_diagnostico(nome_area):
    """
    Renderiza uma aba e calcula a nota média automaticamente para o Diagnóstico Inicial.
    """
    area_config = DIAGNOSTICO_CONFIG[nome_area]
    st.subheader(f"Análise de {nome_area}")
    respostas = {}
    detalhes_perguntas = []
    
    for pergunta in area_config["perguntas"]:
        resposta = renderizar_pergunta(pergunta, "diag")
        respostas[pergunta["id"]] = resposta
        detalhes_perguntas.append({
            "pergunta": pergunta["pergunta"],
            "resposta": resposta if resposta else "Não respondida"
        })
    
    nota_automatica = calcular_nota_area(respostas, area_config)
    st.info(f"Maturidade Calculada para {nome_area}: **{nota_automatica:.2f} / 4.00**")
    st.divider()
    
    observacoes = st.text_area(
        f"Notas Internas do Consultor ({nome_area})",
        key=f"obs_diag_{nome_area}"
    )
    
    return {
        "respostas": respostas,
        "detalhes_perguntas": detalhes_perguntas,
        "nota_calculada": nota_automatica,
        "observacoes": observacoes
    }

def calcular_nota_area(respostas_area, area_config):
    """
    Calcula a nota de uma área com base nas respostas.
    """
    if not respostas_area:
        return 0
    total_pontos = 0
    max_pontos = 0
    
    for pergunta in area_config["perguntas"]:
        if pergunta.get("tipo") == "texto":
            continue
            
        resposta_usuario = respostas_area.get(pergunta["id"])
        max_pontos += max([op["valor"] for op in pergunta["opcoes"]])
        
        for opcao in pergunta["opcoes"]:
            if opcao["texto"] == resposta_usuario:
                total_pontos += opcao["valor"]
                break
    
    if max_pontos == 0: return 0
    return (total_pontos / max_pontos) * 4.0

def renderizar_acolhimento():
    """
    Renderiza o formulário de Acolhimento completo conforme novas solicitações.
    """
    st.header("Fase de Acolhimento")
    
    respostas_acolhimento = {}
    
    # 2. Mapeamento Inicial
    st.subheader("2. Mapeamento Inicial")
    
    disponibilidade = st.selectbox(
        "Qual a sua disponibilidade de tempo para se dedicar a ações de inovação e melhoria no seu negócio ou conhecimento?",
        options=ACOLHIMENTO_CONFIG["Mapeamento Inicial"]["disponibilidade"],
        key="acolh_disponibilidade",
        index=None,
        placeholder="Selecione uma opção..."
    )
    respostas_acolhimento["disponibilidade"] = disponibilidade
    
    canal = st.selectbox(
        "Qual é o principal canal que você usa para se comunicar com seus clientes e realizar atendimentos?",
        options=ACOLHIMENTO_CONFIG["Mapeamento Inicial"]["canais"],
        key="acolh_canal",
        index=None,
        placeholder="Selecione uma opção..."
    )
    respostas_acolhimento["canal_comunicacao"] = canal
    
    st.divider()
    
    # 4. Radar de Demandas
    st.subheader("4. Radar de Demandas")
    st.write(f"**Introdução ao Diagnóstico:** {ACOLHIMENTO_CONFIG['Radar de Demandas']['intro']}")
    
    radar_data = {}
    areas = ACOLHIMENTO_CONFIG["Radar de Demandas"]["areas"]
    escala_demanda = ACOLHIMENTO_CONFIG["Radar de Demandas"]["escala_demanda"]
    escala_interesse = ACOLHIMENTO_CONFIG["Radar de Demandas"]["escala_interesse"]
    
    for area in areas:
        nome_area = area["nome"]
        with st.expander(f"Área: {nome_area}"):
            st.write(f"**Pergunta de Reflexão:** {area['reflexao']}")
            
            # Resposta do cliente (Aberta)
            resp_cliente = st.text_area(f"Resposta do cliente - {nome_area}", key=f"resp_cli_{nome_area}")
            
            # Observações do agente (Aberta)
            obs_agente = st.text_area(f"Observações do agente - {nome_area}", key=f"obs_age_{nome_area}")
            
            col1, col2 = st.columns(2)
            with col1:
                # Escala de Demanda (para empresas)
                opcoes_demanda = [op["texto"] for op in escala_demanda]
                demanda_sel = st.selectbox(
                    f"Escala de Demanda (para empresas) - {nome_area}", 
                    options=opcoes_demanda, 
                    key=f"dem_{nome_area}",
                    index=None,
                    placeholder="Selecione..."
                )
                # Valor interno seguro (evita erro se não selecionar nada)
                val_demanda = next((op["valor"] for op in escala_demanda if op["texto"] == demanda_sel), 0) if demanda_sel else 0
                
            with col2:
                # Escala de Interesse (para pessoas)
                opcoes_interesse = [op["texto"] for op in escala_interesse]
                interesse_sel = st.selectbox(
                    f"Escala de Interesse (para pessoas) - {nome_area}", 
                    options=opcoes_interesse, 
                    key=f"int_{nome_area}",
                    index=None,
                    placeholder="Selecione..."
                )
                # Valor interno seguro
                val_interesse = next((op["valor"] for op in escala_interesse if op["texto"] == interesse_sel), 0) if interesse_sel else 0
            
            radar_data[nome_area] = {
                "abreviacao": area["abreviacao"],
                "resposta_cliente": resp_cliente,
                "observacoes_agente": obs_agente,
                "demanda": val_demanda,
                "interesse": val_interesse
            }
    
    respostas_acolhimento["radar"] = radar_data
    
    st.divider()
    
    # 5. Alinhamento sobre Investimento
    st.subheader("5. Alinhamento sobre Investimento")
    disposto_investir = st.radio(
        "Você estaria disposto(a) a fazer investimentos em ferramentas e soluções pagas?",
        options=["Sim", "Não"],
        horizontal=True,
        key="acolh_investir",
        index=None
    )
    respostas_acolhimento["disposto_investir"] = disposto_investir
    
    orcamento = ""
    if disposto_investir == "Sim":
        orcamento_raw = st.text_input(
            "Qual seria a faixa de orçamento que você estaria disposto(a) a considerar?",
            placeholder="Ex: 500,00",
            key="acolh_orcamento"
        )
        orcamento = formatar_moeda(orcamento_raw)
        st.write(f"Valor formatado: **{orcamento}**")
    
    respostas_acolhimento["orcamento"] = orcamento
    
    st.divider()
    
    # 6. Fechamento e próximos passos
    st.subheader("6. Fechamento e próximos passos")
    
    st.write("**Resumo e Validação:**")
    st.info("\"Agradeço muito pela sua abertura em compartilhar essas informações. Pelo que percebi, suas principais demandas estão em [Resumir as áreas identificadas]. Isso está alinhado com o que você sente?\"")
    
    direcionamento = st.selectbox(
        "Direcionamento:",
        options=LISTA_DIRECIONAMENTO,
        key="acolh_direcionamento",
        index=None,
        placeholder="Selecione uma opção..."
    )
    respostas_acolhimento["direcionamento"] = direcionamento
    
    # Instruções baseadas no direcionamento
    st.write("**Instruções:**")
    if direcionamento in ["Eventos", "Programas"]:
        st.success("Eventos e Programas - Direcione para as inscrições e instrua sobre as principais informações")
    elif direcionamento == "Trilha do Conhecimento":
        st.success("Trilha do Conhecimento - Apresente a plataforma e instrua sobre seu acesso e funcionamento")
    elif direcionamento == "Mandala de Soluções":
        st.success("Mandala de Soluções - Conecte com o parceiro, agendando uma reunião de match para conhecer mais sobre o serviço")
    elif direcionamento == "Diagnóstico Completo":
        st.success("Diagnóstico Completo - Direcione/agende com o Consultor do Núcleo de Operações do Horizonte")
        st.write("**Apresentação da Jornada e Diagnóstico:**")
        st.info("\"A partir de agora, a sua jornada em nosso projeto será a seguinte: agendaremos um Diagnóstico de Demandas completo, que leva em torno de 60 minutos para ser realizado. Com esse diagnóstico, será possível entender de forma mais clara os principais gargalos na sua operação, para que as soluções do plano de ação se enquadrem à sua realidade. As soluções que iremos propor podem ser da CDL/BH, SEBRAE MG ou de outros parceiros participantes do projeto. Parte dessas soluções são gratuitas, mas algumas podem ter custo adicionado. A partir do plano de ação, vamos te encaminhar para algumas dessas instituições para mais detalhes sobre a solução.\"")
    elif direcionamento == "Negociação de Nova Parceria":
        st.success("Novas Parcerias - Direcione para o formulário de manifestação de interesse em ser parceiro e agende uma reunião")

    col_dor, col_sol = st.columns(2)
    with col_dor:
        dor = st.selectbox("Principal Dor identificada:", options=LISTA_DOR_PRINCIPAL, key="acolh_dor_principal", index=None, placeholder="Selecione...")
        respostas_acolhimento["dor_principal_acolh"] = dor
    with col_sol:
        solucao = st.selectbox("Solução Ofertada:", options=LISTA_SOLUCAO_OFERTADA, key="acolh_solucao_ofertada", index=None, placeholder="Selecione...")
        respostas_acolhimento["solucao_ofertada"] = solucao

    st.write("**Agendamento (se for o caso):**")
    agendamento = st.text_input("\"Vamos agendar o próximo encontro? Tenho a seguinte disponibilidade: [Oferecer opções de data e horário].\"", placeholder="Ex: 20/03 às 14h", key="acolh_agendamento")
    respostas_acolhimento["agendamento"] = agendamento

    st.write("**Despedida:**")
    st.info("\"Muito obrigado(a) mais uma vez pela conversa! Estamos aqui para te ajudar. Até breve.\"")

    st.divider()
    
    # 7. Relatório Final
    st.subheader("7. Relatório Final: Principais pontos observados no acolhimento")
    relatorio_final = st.text_area("Principais pontos observados no acolhimento (Campo Aberto)", key="acolh_relatorio_final")
    respostas_acolhimento["relatorio_final"] = relatorio_final
        
    return respostas_acolhimento