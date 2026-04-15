from fpdf import FPDF
from datetime import datetime
import os

def limpar_texto(texto):
    """Substitui caracteres especiais e garante que a string nunca seja vazia para o FPDF."""
    if texto is None or str(texto).strip() == "":
        return "N/A"
    
    t = str(texto)
    # Substituições comuns de caracteres que causam erro na fonte padrão
    t = t.replace("—", "-").replace("–", "-").replace("…", "...")
    t = t.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    t = t.replace("\u2022", "*") # bullet point
    t = t.replace("\xa0", " ") # espaços inquebráveis (principal causador do erro de renderização)
    
    # Tenta converter para latin-1 (padrão do FPDF Arial) e ignora o que não conseguir
    try:
        return t.encode('latin-1', 'replace').decode('latin-1')
    except:
        # Se falhar radicalmente, remove caracteres não-latin-1
        return "".join([c if ord(c) < 256 else "?" for c in t])

class PDF_Horizonte(FPDF):
    def __init__(self):
        # Configuração de margens padrão ABNT (Superior: 30, Esquerda: 30, Direita: 20, Inferior: 20)
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(left=30, top=30, right=20)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        try:
            # Tenta carregar a logo se existir
            if os.path.exists("LogoHorizonte1.png"):
                self.image("LogoHorizonte1.png", 30, 8, 32)
            elif os.path.exists("LogoHorizonte1.jpg"):
                self.image("LogoHorizonte1.jpg", 30, 8, 32)
        except:
            pass
        self.set_font("Arial", "B", 10)
        self.set_y(15)
        # OBRIGATÓRIO USAR CELL: multi_cell no header causa quebra do layout se a página virar
        self.ln(13)
        self.line(30, 32, 190, 32) # Linha horizontal de separação
        self.ln(5)

    def footer(self):
        self.set_y(-20) # Margem inferior de 20mm
        self.set_font("Arial", "I", 8)
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        # OBRIGATÓRIO USAR CELL: multi_cell no footer corrompe a renderização ao mudar de página
        self.cell(0, 10, limpar_texto(f"Página {self.page_no()}/{{nb}} | Gerado em: {data_hora}"), border=0, align="C")

    def secao(self, titulo):
        self.ln(4)
        self.set_font("Arial", "B", 10)
        self.set_fill_color(240, 240, 240)
        # Textos curtos de 1 linha: usar cell
        self.cell(0, 8, limpar_texto(f" {titulo}"), border=0, ln=True, align="L", fill=True)
        self.ln(2)

    def item_duas_colunas(self, label1, valor1, label2, valor2):
        """Imprime duas colunas curtas na mesma linha para os Dados do Negócio."""
        y_atual = self.get_y()
        
        # Coluna 1
        self.set_font("Arial", "B", 10)
        lbl1 = f"{limpar_texto(label1)}: "
        self.cell(self.get_string_width(lbl1), 6, lbl1)
        self.set_font("Arial", "", 10)
        val1 = limpar_texto(valor1)[:35] # Trunca suavemente para não invadir col 2
        self.cell(110 - self.get_x(), 6, val1)
        
        # Coluna 2
        self.set_xy(110, y_atual)
        self.set_font("Arial", "B", 10)
        lbl2 = f"{limpar_texto(label2)}: "
        self.cell(self.get_string_width(lbl2), 6, lbl2)
        self.set_font("Arial", "", 10)
        self.cell(0, 6, limpar_texto(valor2), ln=True)

    def item(self, label, valor):
        """Cria um item com rótulo e valor em linhas separadas (Abordagem Vertical Segura)."""
        self.set_font("Arial", "B", 10)
        # Rótulo usa cell para evitar bugs
        self.cell(0, 6, limpar_texto(f"{label}:"), ln=True)
        self.set_font("Arial", "", 10)
        # multi_cell seguro apenas no valor, pois ele pode ter múltiplas linhas
        self.multi_cell(0, 6, limpar_texto(valor))
        self.ln(2)
    
    def item_horizontal(self, label, valor):
        """Imprime o rótulo e o valor na mesma linha para economizar espaço."""
        self.set_font("Arial", "B", 10)
        lbl = f"{limpar_texto(label)}: "
        self.cell(self.get_string_width(lbl), 6, lbl)
        self.set_font("Arial", "", 10)
        self.cell(0, 6, limpar_texto(str(valor)), ln=True)
        self.ln(1)

def gerar_ata_interna(dados, resultados, caminho_radar, nome_arquivo, modo="Diagnóstico Inicial"):
    pdf = PDF_Horizonte()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    empresa = str(dados.get("empresa", "Empresa"))
    titulo_doc = "ATA DE DIAGNÓSTICO" if modo == "Diagnóstico Inicial" else "ATA DE ACOLHIMENTO"
    
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 10, limpar_texto(f"{titulo_doc} - {empresa.upper()}"), border=0, ln=True, align="C")
    pdf.ln(2)

    # É PJ OU PF?
    documento = dados.get('cnpj', '')
    is_pj = '/' in documento

    # ======================
    # 1 DADOS DO NEGÓCIO / CLIENTE
    # ======================
    titulo_secao_1 = "1. DADOS DO NEGÓCIO" if is_pj else "1. DADOS DO CLIENTE"
    pdf.secao(titulo_secao_1)
    
    label_nome = "Empresa" if is_pj else "Nome Responsável"
    label_doc = "CNPJ" if is_pj else "CPF"
    
    pdf.item_duas_colunas("Data", dados.get('data',''), "Consultor", dados.get('consultor',''))
    pdf.item_duas_colunas(label_nome, dados.get('empresa',''), label_doc, documento)
    pdf.item_duas_colunas("Setor", dados.get('setor',''), "Contato", dados.get('contato',''))
    pdf.item_duas_colunas("Município", dados.get('municipio',''), "Estado", dados.get('estado',''))
    
    if is_pj:
        pdf.item_duas_colunas("Colaboradores", dados.get('n_colaboradores',''), "Fundação", dados.get('ano_fundacao',''))
    else:
        pdf.item_horizontal("Nascimento", dados.get('ano_fundacao',''))
    
    pdf.item_horizontal("Endereço", f"{dados.get('endereco','')} ({dados.get('tipo_endereco','')})")
    pdf.item_horizontal("Associado CDL/BH", f"{dados.get('cdl_bh','')} (Nº: {dados.get('num_associado','')})")
    pdf.item_horizontal("Estrutura", f"Loja Física: {dados.get('loja_fisica','')} | Loja Virtual: {dados.get('loja_virtual','')}")

    pdf.secao("ESCOPO ESTRATÉGICO")
    lbl_vende = "O que vende / Serviços" if is_pj else "Atuação / Serviços"
    pdf.item(lbl_vende, dados.get('o_que_vende',''))
    pdf.item("Objetivo", dados.get('objetivo',''))
    pdf.item("Principais desafios", dados.get('desafios',''))
    pdf.item("Interesse em expansão", dados.get('interesse_expansao',''))

    # ======================
    # 2 REPRESENTANTES / PARTICIPANTES
    # ======================
    titulo_secao_2 = "2. REPRESENTANTES" if is_pj else "2. PARTICIPANTES"
    pdf.secao(titulo_secao_2)
    participantes = dados.get("participantes", [])
    if participantes:
        for i, p in enumerate(participantes):
            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 7, limpar_texto(f"Participante {i+1}:"), border=0, ln=True, align="L")
            pdf.set_font("Arial", "", 10)
            
            if is_pj:
                info_p = f"Nome: {p.get('nome','')} | Cargo: {p.get('cargo','')} | CPF: {p.get('cpf','')}\n"
            else:
                info_p = f"Nome: {p.get('nome','')} | CPF: {p.get('cpf','')}\n"
                
            info_p += f"Telefone: {p.get('celular','')} | E-mail: {p.get('email','')}"
            pdf.multi_cell(0, 6, limpar_texto(info_p))
            pdf.ln(2)
    else:
        pdf.item("Participantes", "Nenhum participante registrado.")

    # ======================
    # 3 CONTEÚDO (DIAGNÓSTICO OU ACOLHIMENTO)
    # ======================
    if modo == "Diagnóstico Inicial":
        pdf.secao("3. DIAGNÓSTICO INICIAL")
        for area, res in resultados.items():
            pdf.set_font("Arial", "B", 11)
            pdf.set_fill_color(245, 245, 245)
            pdf.cell(0, 8, limpar_texto(f" Área: {area} (Nota: {res.get('nota_calculada', 0):.2f})"), border=0, ln=True, align="L", fill=True)
            pdf.ln(1)
            perguntas = res.get("detalhes_perguntas", [])
            for p in perguntas:
                pdf.item(p['pergunta'], p['resposta'])
            pdf.item("Notas Internas do Consultor", res.get("observacoes", "Sem observações."))
            pdf.ln(2)
    else:
        pdf.secao("3. MAPEAMENTO DE ACOLHIMENTO")
        pdf.item("Disponibilidade de Tempo", resultados.get("disponibilidade", "N/A"))
        pdf.item("Canais de Atendimento", resultados.get("canal_comunicacao", "N/A"))
        
        pdf.secao("ANÁLISE DE ÁREAS CRÍTICAS (RADAR)")
        radar_data = resultados.get("radar", {})
        for area_nome, vals in radar_data.items():
            if not isinstance(vals, dict):
                vals = {}
                
            pdf.set_font("Arial", "B", 11)
            pdf.set_fill_color(245, 245, 245)
            pdf.cell(0, 8, limpar_texto(f" Área: {area_nome}"), border=0, ln=True, align="L", fill=True)
            pdf.ln(1)
            
            pdf.item("Resposta | Observações do Consultor", vals.get('notas_consultor', 'N/A'))
            nota = vals.get('demanda', 0) if is_pj else vals.get('interesse', 0) # 1. Pega a nota certa dependendo se é PJ ou PF
            # 2. Transforma em número inteiro 
            try:
                nota = int(nota)
            except:
                nota = 0

            # 3. Dicionários tradutores
            dic_demanda = {1: "Demanda Muito Baixa", 2: "Demanda Baixa", 3: "Demanda Média", 4: "Demanda Alta", 5: "Demanda Crítica"}
            dic_interesse = {1: "Nenhum Interesse", 2: "Baixo Interesse", 3: "Interesse Moderado", 4: "Alto Interesse", 5: "Interesse Muito Alto"}
            
            # 4. Escolhe a frase certa e monta o texto final
            if is_pj:
                texto_nivel = dic_demanda.get(nota, "Não avaliado")
            else:
                texto_nivel = dic_interesse.get(nota, "Não avaliado")
                
            pdf.item("Nível", f"{texto_nivel} ({nota})")
            pdf.ln(2)
            
        pdf.secao("4. ALINHAMENTO FINANCEIRO")
        pdf.item("Disposição para Investimento", resultados.get("disposto_investir", "N/A"))
        pdf.item("Faixa de Orçamento", resultados.get("orcamento", "N/A"))
          
        pdf.secao("5. CONCLUSÃO DO ACOLHIMENTO")
        pdf.item("Principal Dor", resultados.get("dor_principal_acolh", "N/A")) 
        pdf.item("Direcionamento", resultados.get("direcionamento", "N/A"))     
        sol_of = resultados.get("solucao_ofertada", "N/A")
        detalhe_sol = resultados.get("solucao_detalhe", {})
        
        if detalhe_sol:
            texto_sol = f"{sol_of}\n"
            texto_sol += f"Descrição: {detalhe_sol.get('descricao', 'Não informada')}\n"
            texto_sol += f"Instituição: {detalhe_sol.get('instituicao', 'Não informada')}"
            if detalhe_sol.get('carga_horaria'):
                texto_sol += f"\nCarga Horária: {detalhe_sol.get('carga_horaria', '')}"
            if detalhe_sol.get('custo'):
                texto_sol += f"\nCusto: {detalhe_sol.get('custo', '')}"
            if detalhe_sol.get('link'):
                texto_sol += f"\nLink de Acesso: {detalhe_sol.get('link', '')}"
                
            pdf.item("Solução Ofertada", texto_sol)
        else:
            pdf.item("Solução Ofertada", str(sol_of))
            
        pdf.item("Agendamento", resultados.get("agendamento", "N/A"))
        
        pdf.secao("6. RELATÓRIO FINAL")
        pdf.item("Pontos Observados", resultados.get("relatorio_final", "N/A"))

    # ======================
    # 4 RADAR
    # ======================
    if caminho_radar and os.path.exists(caminho_radar):
        pdf.add_page()
        pdf.secao("RADAR DE MATURIDADE / DEMANDAS")
        pdf.ln(5)
        try:
            largura_util = pdf.w - pdf.l_margin - pdf.r_margin
            largura_img = largura_util * 0.90
            x = pdf.l_margin + (largura_util - largura_img) / 2
            pdf.image(caminho_radar, x=x, w=largura_img)
        except:
            pdf.cell(0, 10, "Erro ao carregar imagem do radar.", ln=True)

    # ======================
    # 5 PLANO DE AÇÃO (Apenas para Diagnóstico)
    # ======================
    if modo == "Diagnóstico Inicial":
        pdf.secao("5. PLANO DE AÇÃO ESTRATÉGICO")
        pdf.item("Principal Dor Identificada", dados.get('dor_principal',''))
        solucoes = dados.get("solucoes", [])
        if solucoes:
            for i, s in enumerate(solucoes):
                pdf.set_font("Arial", "B", 11)
                pdf.cell(0, 8, limpar_texto(f"Indicação de Solução {i+1}"), border=0, ln=True, align="L")
                
                # Textos longos usam o item normal (título em cima, texto embaixo)
                pdf.item("Solução", s.get('solucao',''))
                pdf.item("Descrição", s.get('descricao',''))
                pdf.item("Motivo da Indicação", s.get('motivo',''))
                pdf.item_horizontal("Parceiro / Fornecedor", s.get('parceiro',''))
                
                if s.get('carga_horaria'):
                    pdf.item_horizontal("Carga Horária", s.get('carga_horaria'))
                    
                if s.get('custo'):
                    pdf.item_horizontal("Custo Estimado", s.get('custo'))
                    
                if s.get('link'):
                    pdf.item_horizontal("Link de Acesso", s.get('link'))
                    
                pdf.ln(2)
        
        # Prazos gerais no final (agora sim!)
        pdf.item("Checkpoints e Prazos Gerais", dados.get('prazos_gerais', 'Nenhum prazo definido.'))

    pdf.output(nome_arquivo)
    return nome_arquivo


def gerar_plano_cliente(dados, resultados, caminho_radar, nome_arquivo, modo="Diagnóstico Inicial"):
    pdf = PDF_Horizonte()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    empresa = str(dados.get("empresa", "Empresa"))
    titulo_doc = "PLANO DE AÇÃO DIAGNÓSTICO" if modo == "Diagnóstico Inicial" else "PLANO DE AÇÃO - ACOLHIMENTO"
    
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 10, limpar_texto(f"{titulo_doc} - {empresa.upper()}"), border=0, ln=True, align="C")
    pdf.ln(2)

    documento = dados.get('cnpj', '')
    is_pj = '/' in documento

    # ======================
    # 1 DADOS DO NEGÓCIO E PARTICIPANTES
    # ======================
    titulo_secao_1 = "1. DADOS DO NEGÓCIO" if is_pj else "1. DADOS DO CLIENTE"
    pdf.secao(titulo_secao_1)
    
    label_nome = "Empresa" if is_pj else "Nome Responsável"
    label_doc = "CNPJ" if is_pj else "CPF"
    
    pdf.item_duas_colunas("Data", dados.get('data',''), "Consultor", dados.get('consultor',''))
    pdf.item_duas_colunas(label_nome, dados.get('empresa',''), label_doc, documento)
    pdf.item_duas_colunas("Setor", dados.get('setor',''), "Contato", dados.get('contato',''))
    pdf.item_duas_colunas("Município", dados.get('municipio',''), "Estado", dados.get('estado',''))
    pdf.ln(2)

    titulo_secao_2 = "2. REPRESENTANTES" if is_pj else "2. PARTICIPANTES"
    pdf.secao(titulo_secao_2)
    participantes = dados.get("participantes", [])
    if participantes:
        for i, p in enumerate(participantes):
            pdf.set_font("Arial", "B", 10)
            pdf.cell(0, 7, limpar_texto(f"Participante {i+1}:"), border=0, ln=True, align="L")
            pdf.set_font("Arial", "", 10)
            
            if is_pj:
                info_p = f"Nome: {p.get('nome','')} | Cargo: {p.get('cargo','')} | Telefone: {p.get('celular','')}\n"
            else:
                info_p = f"Nome: {p.get('nome','')} | Telefone: {p.get('celular','')}\n"
                
            info_p += f"E-mail: {p.get('email','')}"
            pdf.multi_cell(0, 6, limpar_texto(info_p))
            pdf.ln(2)
    else:
        pdf.item("Participantes", "Nenhum participante registrado.")

    # CONTEÚDO ESPECÍFICO POR MODO
    if modo == "Diagnóstico Inicial":
        
        # RADAR (O lindo automático do App.py!)
        if caminho_radar and os.path.exists(caminho_radar):
            pdf.secao("3. RADAR DE MATURIDADE")
            pdf.ln(2)
            try:
                largura_util = pdf.w - pdf.l_margin - pdf.r_margin
                largura_img = largura_util * 0.85
                x = pdf.l_margin + (largura_util - largura_img) / 2
                pdf.image(caminho_radar, x=x, w=largura_img)
                pdf.ln(5)
            except:
                pdf.cell(0, 10, "Erro ao carregar imagem do radar.", ln=True)
                
        # PLANO DE AÇÃO
        pdf.secao("4. PLANO DE AÇÃO ESTRATÉGICO")
        pdf.item("Principal Dor Identificada", dados.get('dor_principal',''))
        solucoes = dados.get("solucoes", [])
        if solucoes:
            for i, s in enumerate(solucoes):
                pdf.set_font("Arial", "B", 11)
                pdf.cell(0, 8, limpar_texto(f"Indicação de Solução {i+1}"), border=0, ln=True, align="L")
                
                # Textos longos usam o item normal (título em cima, texto embaixo)
                pdf.item("Solução", s.get('solucao',''))
                pdf.item("Descrição", s.get('descricao',''))
                pdf.item("Motivo da Indicação", s.get('motivo',''))
                
                # Textos curtos usam o horizontal para ficar elegante e economizar papel!
                pdf.item_horizontal("Parceiro / Fornecedor", s.get('parceiro',''))
                
                if s.get('carga_horaria'):
                    pdf.item_horizontal("Carga Horária", s.get('carga_horaria'))
                    
                if s.get('custo'):
                    pdf.item_horizontal("Custo Estimado", s.get('custo'))
                    
                if s.get('link'):
                    pdf.item_horizontal("Link de Acesso", s.get('link'))
                    
                pdf.ln(2)
        
        # Prazos gerais no final do Plano de Ação
        pdf.item("Checkpoints e Prazos Gerais", dados.get('prazos_gerais', 'Nenhum prazo definido.'))

    else: # Modo Acolhimento
        pdf.secao("3. MAPEAMENTO DE ACOLHIMENTO")
        pdf.item("Disponibilidade de Tempo", resultados.get("disponibilidade", "N/A"))
        pdf.item("Canais de Atendimento", resultados.get("canal_comunicacao", "N/A"))
        
        # RADAR
        if caminho_radar and os.path.exists(caminho_radar):
            pdf.secao("4. RADAR DE ACOLHIMENTO")
            pdf.ln(2)
            try:
                largura_util = pdf.w - pdf.l_margin - pdf.r_margin
                largura_img = largura_util * 0.85
                x = pdf.l_margin + (largura_util - largura_img) / 2
                pdf.image(caminho_radar, x=x, w=largura_img)
                pdf.ln(5)
            except:
                pass
                
        pdf.secao("5. CONCLUSÃO DO ACOLHIMENTO")
        pdf.item("Principal Dor", resultados.get("dor_principal_acolh", "N/A")) 
        pdf.item("Direcionamento", resultados.get("direcionamento", "N/A"))    
        
        # Pega a solução ofertada e os detalhes (como Link e Carga horária)
        sol_of = resultados.get("solucao_ofertada", "N/A")
        detalhe_sol = resultados.get("solucao_detalhe", {})
        if detalhe_sol:
            texto_sol = f"{sol_of}\nDescrição: {detalhe_sol.get('descricao', '')}\nInstituição: {detalhe_sol.get('instituicao', '')}"
            if detalhe_sol.get('carga_horaria'):
                texto_sol += f"\nCarga Horária: {detalhe_sol.get('carga_horaria', '')}"
            if detalhe_sol.get('link'):
                texto_sol += f"\nLink de Acesso: {detalhe_sol.get('link', '')}"
            pdf.item("Solução Ofertada", texto_sol)
        else:
            pdf.item("Solução Ofertada", str(sol_of))
            
        pdf.item("Agendamento", resultados.get("agendamento", "N/A"))

    pdf.output(nome_arquivo)
    return nome_arquivo