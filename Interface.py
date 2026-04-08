# Funções para gerar a interface do Streamlit
import streamlit as st
from Perguntas import DIAGNOSTICO_CONFIG, ACOLHIMENTO_CONFIG, LISTA_DIRECIONAMENTO, LISTA_DOR_PRINCIPAL, CATALOGO_MANDALA, CATALOGO_TRILHA
from Formatacoes import formatar_moeda
import plotly.graph_objects as go

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
            index=None 
        )
    else:
        opcoes_texto = [op["texto"] for op in pergunta["opcoes"]]
        resposta_selecionada = st.radio(
            label=pergunta["pergunta"],
            options=opcoes_texto,
            key=unique_key,
            index=None 
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

def renderizar_acolhimento(is_pj=True):
    """
    Renderiza o formulário de Acolhimento completo conforme novas solicitações.
    """
    st.header("Acolhimento")
    
    respostas_acolhimento = {}
    
    # Mapeamento Inicial
    st.subheader("1. Mapeamento Inicial")
    
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
    st.subheader("2. Diagnóstico de Demandas")
    st.write(f"**Introdução ao Diagnóstico:** {ACOLHIMENTO_CONFIG['Radar de Demandas']['intro']}")
    
    # Mostra a escala de PJ se is_pj for True, senão mostra a de PF.
    if is_pj:
        st.markdown("""
        <details style="background-color: #ebebff; border: 2px solid #b7b5f5; border-radius: 5px; padding: 10px; margin-bottom: 15px;">
            <summary style="font-weight: bold; cursor: pointer; color: #080808;">Escala de Avaliação (PJ - Demanda)</summary>
            <ul style="margin-top: 10px; color: #080808;">
                <li><b>1 - Muito Baixa:</b> Confiança na área. Situação controlada e sem urgência.</li>
                <li><b>2 - Baixa:</b> Oportunidade de melhoria, mas não é um impeditivo no momento.</li>
                <li><b>3 - Média:</b> Desafios claros que já impactam o dia a dia. Merece atenção.</li>
                <li><b>4 - Alta:</b> Problema recorrente com impactos negativos (tempo/dinheiro). Gargalo evidente.</li>
                <li><b>5 - Crítica:</b> Obstáculo severo à sobrevivência do negócio. Exige solução imediata.</li>
            </ul>
        </details>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <details style="background-color: #ebebff; border: 2px solid #b7b5f5; border-radius: 5px; padding: 10px; margin-bottom: 15px;">
            <summary style="font-weight: bold; cursor: pointer; color: #080808;">Escala de Avaliação (PF - Interesse)</summary>
            <ul style="margin-top: 10px; color: #080808;">
                <li><b>1 - Nenhum:</b> Tema não possui relação ou relevância para a realidade atual.</li>
                <li><b>2 - Baixo:</b> Reconhece a importância, mas sem motivação para aprofundamento a curto prazo.</li>
                <li><b>3 - Moderado:</b> Curiosidade e abertura para aprender, embora ainda não seja prioridade.</li>
                <li><b>4 - Alto:</b> Entusiasmo e motivação. Vontade clara de aprender e aplicar.</li>
                <li><b>5 - Muito Alto:</b> Tema estratégico e essencial. Busca ativa, engajamento imediato.</li>
            </ul>
        </details>
        """, unsafe_allow_html=True)

    radar_data = {}
    areas = ACOLHIMENTO_CONFIG["Radar de Demandas"]["areas"]
    escala_demanda = ACOLHIMENTO_CONFIG["Radar de Demandas"]["escala_demanda"]
    escala_interesse = ACOLHIMENTO_CONFIG["Radar de Demandas"]["escala_interesse"]
    
    for area in areas:
        nome_area = area["nome"]
        with st.expander(f"Área: {nome_area}"):
            st.write(f"**Pergunta de Reflexão:** {area['reflexao']}")
            
            notas_consultor = st.text_area(f"Notas Internas do Consultor - {nome_area}", key=f"notas_cons_{nome_area}")
            
            # --- A MÁGICA DA SEPARAÇÃO ACONTECE AQUI ---
            if is_pj:
                opcoes_demanda = [op["texto"] for op in escala_demanda]
                demanda_sel = st.selectbox(
                    f"Escala de Demanda - {nome_area}", 
                    options=opcoes_demanda, 
                    key=f"dem_{nome_area}",
                    index=None,
                    placeholder="Selecione..."
                )
                valor_radar = next((op["valor"] for op in escala_demanda if op["texto"] == demanda_sel), 0) if demanda_sel else 0
            else:
                opcoes_interesse = [op["texto"] for op in escala_interesse]
                interesse_sel = st.selectbox(
                    f"Escala de Interesse - {nome_area}", 
                    options=opcoes_interesse, 
                    key=f"int_{nome_area}",
                    index=None,
                    placeholder="Selecione..."
                )
                valor_radar = next((op["valor"] for op in escala_interesse if op["texto"] == interesse_sel), 0) if interesse_sel else 0
            
            radar_data[nome_area] = {
                "abreviacao": area["abreviacao"],
                "resposta_cliente": resp_cliente,
                "observacoes_agente": obs_agente,
                "nota_radar": valor_radar, # <--  montar o gráfico!
                "demanda": valor_radar if is_pj else 0,
                "interesse": valor_radar if not is_pj else 0
            }
    respostas_acolhimento["radar"] = radar_data
    
    #   GRÁFICO AO VIVO (Visão do Consultor)
    st.markdown("#### 3.Visão Geral - Gráfico de Radar ")
    
    labels = [radar_data[area]['abreviacao'] for area in radar_data]
    valores = [radar_data[area]['nota_radar'] for area in radar_data]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=valores + [valores[0]], 
        theta=labels + [labels[0]], 
        fill='toself', 
        fillcolor='rgba(0, 180, 216, 0.25)', 
        line=dict(color='#121A3B', width=3)
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False)
    
    # Desenha o gráfico na tela!
    st.plotly_chart(fig, use_container_width=True)
    st.divider()
    
    # 5. Alinhamento sobre Investimento
    st.subheader("4. Alinhamento sobre Investimento")
    # ... o código continua normal pra baixo
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
    st.subheader("5. Fechamento e próximos passos")
    
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
    
    if direcionamento:
        st.write("**Instruções:**")

        # 1. EVENTOS E PROGRAMAS
        if direcionamento == "Eventos e Programas":
            st.success("Eventos e Programas - Direcione para as inscrições e instrua sobre as principais informações")
            col_dor, col_sol = st.columns(2)
            with col_dor:
                dor = st.selectbox("Principal Dor identificada:", options=LISTA_DOR_PRINCIPAL, key="acolh_dor_principal", index=None)
            with col_sol:
                solucao = st.text_input("Solução Ofertada:", key="acolh_solucao_ofertada", placeholder="Ex: Inscrição no evento X")
            respostas_acolhimento["dor_principal_acolh"] = dor
            respostas_acolhimento["solucao_ofertada"] = solucao

        # 2. PORTIFÓLIO DE SOLUÇÕES
        elif direcionamento == "Portifólio de Soluções":
            st.success("Portifólio de Soluções - Conecte com o parceiro, agendando uma reunião de match para conhecer mais sobre o serviço")
            col_dor, col_sol = st.columns(2)
            with col_dor:
                dor = st.selectbox("Principal Dor identificada:", options=LISTA_DOR_PRINCIPAL, key="acolh_dor_principal", index=None)
            with col_sol:
                solucao = st.selectbox("Solução Ofertada:", options=list(CATALOGO_MANDALA.keys()), key="acolh_solucao_ofertada", index=None)
            respostas_acolhimento["dor_principal_acolh"] = dor
            respostas_acolhimento["solucao_ofertada"] = solucao

            if solucao:
                info = CATALOGO_MANDALA[solucao]
                st.info(f"**Descrição:** {info['descricao']}\n\n**Instituição:** {info['instituicao']} | **Custo:** {info['custo']}")
                respostas_acolhimento["solucao_detalhe"] = info

        # 3. TRILHA DO CONHECIMENTO
        elif direcionamento == "Trilha do Conhecimento":
            st.success("Trilha do Conhecimento - Apresente a plataforma e instrua sobre seu acesso e funcionamento")
            col_dor, col_sol = st.columns(2)
            with col_dor:
                dor = st.selectbox("Principal Dor identificada:", options=LISTA_DOR_PRINCIPAL, key="acolh_dor_principal", index=None)
            with col_sol:
                solucao = st.selectbox("Solução Ofertada:", options=list(CATALOGO_TRILHA.keys()), key="acolh_solucao_ofertada", index=None)
            respostas_acolhimento["dor_principal_acolh"] = dor
            respostas_acolhimento["solucao_ofertada"] = solucao

            if solucao:
                info = CATALOGO_TRILHA[solucao]
                st.info(f"**Descrição:** {info['descricao']}\n\n**Instituição:** {info['instituicao']} | **Carga Horária:** {info['carga_horaria']} | **Custo:** {info['custo']}\n\n**Link de Acesso:** {info['link']}")
                respostas_acolhimento["solucao_detalhe"] = info

        # 4. DIAGNÓSTICO COMPLETO
        elif direcionamento == "Diagnóstico Completo":
            st.success("Diagnóstico Completo - Direcione/agende com o Consultor do Núcleo de Operações do Horizonte")
            dor = st.selectbox("Principal Dor identificada:", options=LISTA_DOR_PRINCIPAL, key="acolh_dor_principal", index=None)
            respostas_acolhimento["dor_principal_acolh"] = dor
            respostas_acolhimento["solucao_ofertada"] = "Agendado Diagnóstico Completo"

        # 5. NEGOCIAÇÃO DE NOVA PARCERIA
        elif direcionamento == "Negociação de Nova Parceria":
            st.success("Novas Parcerias - Direcione para o formulário de manifestação de interesse em ser parceiro e agende uma reunião")
            dor = st.selectbox("Principal Dor identificada:", options=LISTA_DOR_PRINCIPAL, key="acolh_dor_principal", index=None)
            respostas_acolhimento["dor_principal_acolh"] = dor
            respostas_acolhimento["solucao_ofertada"] = "Negociação de Parceria"

        # 6. ATENDIMENTO | CONSTRUÇÃO PERSONALIZADA  
        if direcionamento == "Atendimento | Construção Personalizada":
            st.success("Atendimento | Construção Personalizada - Direcione/agende com o Consultor do Núcleo de Operações do Horizonte")
            col_dor, col_sol = st.columns(2)
            with col_dor:
                dor = st.selectbox("Principal Dor identificada:", options=LISTA_DOR_PRINCIPAL, key="acolh_dor_principal", index=None)
            with col_sol:
                solucao = st.text_input("Solução Ofertada:", key="acolh_solucao_ofertada", placeholder="Ex: Atendimento agendado para xxxx na sala de Imersão Criativa")
            respostas_acolhimento["dor_principal_acolh"] = dor
            respostas_acolhimento["solucao_ofertada"] = solucao

        st.write("**Observação / Agendamento:**")
        agendamento = st.text_input("\" Oferecer opções de data e horário ou fazer anotações sobre os próximos passos.\"", placeholder="Ex: Diagnóstico marcado para 20/03 às 14h", key="acolh_agendamento")
        respostas_acolhimento["agendamento"] = agendamento

    st.write("**Despedida:**")
    st.info("\"Muito obrigado(a) mais uma vez pela conversa! Estamos aqui para te ajudar. Até breve.\"")

    st.divider()
    
    # 7. Relatório Final
    st.subheader("6. Relatório Final: Principais pontos observados no acolhimento")
    relatorio_final = st.text_area("Principais pontos observados no acolhimento", key="acolh_relatorio_final")
    respostas_acolhimento["relatorio_final"] = relatorio_final
        
    return respostas_acolhimento
