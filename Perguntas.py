
# Perguntas do diagnósticos e configurações
DIAGNOSTICO_CONFIG = {
    "Recursos Humanos": {
        "abreviacao": "RH",
        "perguntas": [
            {
                "id": "rh_q1",
                "pergunta": "Existe um processo estruturado para recrutamento e seleção?",
                "opcoes": [
                    {"texto": "Não existe processo definido", "valor": 1},
                    {"texto": "Processo informal e sem critérios claros", "valor": 2},
                    {"texto": "Processo definido, mas sem padrão documentado", "valor": 3},
                    {"texto": "Processo estruturado com critérios técnicos e comportamentais", "valor": 4}
                ]
            },
            {
                "id": "rh_q2",
                "pergunta": "Nos últimos 12 meses, houve dificuldade em contratar pessoas adequadas para as funções?",
                "opcoes": [
                    {"texto": "Sim, frequentemente", "valor": 1},
                    {"texto": "Sim, algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não houve dificuldade", "valor": 4}
                ]
            },
            {
                "id": "rh_q3",
                "pergunta": "Já ocorreram desligamentos por erro de contratação ou desalinhamento com a cultura?",
                "opcoes": [
                    {"texto": "Sim, com frequência", "valor": 1},
                    {"texto": "Sim, ocasionalmente", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "rh_q4",
                "pergunta": "A empresa possui definição clara de perfil comportamental e técnico para cada função?",
                "tipo": "texto",
                "opcoes": [{"texto": "Resposta Aberta", "valor": 0}]
            },
            {
                "id": "rh_q5",
                "pergunta": "Existe processo estruturado de integração (onboarding) para novos colaboradores?",
                "opcoes": [
                    {"texto": "Não existe", "valor": 1},
                    {"texto": "Existe informalmente", "valor": 2},
                    {"texto": "Existe parcialmente estruturado", "valor": 3},
                    {"texto": "Existe estruturado e padronizado", "valor": 4}
                ]
            },
            {
                "id": "rh_q6",
                "pergunta": "A falta de treinamento já impactou a qualidade do serviço ou produtividade?",
                "opcoes": [
                    {"texto": "Sim, com frequência", "valor": 1},
                    {"texto": "Sim, algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "rh_q7",
                "pergunta": "Os líderes da empresa receberam algum tipo de capacitação em liderança ou gestão de pessoas?",
                "opcoes": [
                    {"texto": "Nunca", "valor": 1},
                    {"texto": "Já participaram pontualmente", "valor": 2},
                    {"texto": "Participam ocasionalmente", "valor": 3},
                    {"texto": "Existe desenvolvimento contínuo", "valor": 4}
                ]
            },
            {
                "id": "rh_q8",
                "pergunta": "Quando um funcionário sai, há perda significativa de conhecimento ou processos?",
                "opcoes": [
                    {"texto": "Sim, sempre", "valor": 1},
                    {"texto": "Sim, parcialmente", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não, tudo é documentado", "valor": 4}
                ]
            },
            {
                "id": "rh_q9",
                "pergunta": "Existe processo estruturado de avaliação de desempenho e feedback?",
                "opcoes": [
                    {"texto": "Não existe", "valor": 1},
                    {"texto": "Existe apenas quando há problema", "valor": 2},
                    {"texto": "Existe de forma informal", "valor": 3},
                    {"texto": "Existe estruturado e periódico", "valor": 4}
                ]
            },
            {
                "id": "rh_q10",
                "pergunta": "A equipe costuma cumprir prazos e metas estabelecidas?",
                "opcoes": [
                    {"texto": "Frequentemente não cumprem", "valor": 1},
                    {"texto": "Cumprimento irregular", "valor": 2},
                    {"texto": "Cumpre na maioria das vezes", "valor": 3},
                    {"texto": "Cumpre consistentemente", "valor": 4}
                ]
            },
            {
                "id": "rh_q11",
                "pergunta": "Você percebe baixo engajamento ou desmotivação na equipe?",
                "opcoes": [
                    {"texto": "Sim, frequentemente", "valor": 1},
                    {"texto": "Às vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "rh_q12",
                "pergunta": "Existem metas claras individuais ou por equipe?",
                "opcoes": [
                    {"texto": "Não existem metas", "valor": 1},
                    {"texto": "Existem metas informais", "valor": 2},
                    {"texto": "Existem metas definidas, mas pouco acompanhadas", "valor": 3},
                    {"texto": "Existem metas acompanhadas com indicadores", "valor": 4}
                ]
            },
            {
                "id": "rh_q13",
                "pergunta": "Existe política de incentivos, reconhecimento ou benefícios vinculados a desempenho?",
                "opcoes": [
                    {"texto": "Não existe", "valor": 1},
                    {"texto": "Existe informalmente", "valor": 2},
                    {"texto": "Existe parcialmente estruturada", "valor": 3},
                    {"texto": "Existe estruturada e vinculada a metas", "valor": 4}
                ]
            }
        ]
    },
    "Atendimento ao Cliente": {
        "abreviacao": "Atendimento",
        "perguntas": [
            {
                "id": "atend_q1",
                "pergunta": "Como você avalia a experiência e o relacionamento que oferece aos seus clientes?",
                "opcoes": [
                    {"texto": "Crítico - Muitas reclamações e perda de vendas", "valor": 1},
                    {"texto": "Baixo - Pouca organização e demora no retorno", "valor": 2},
                    {"texto": "Médio - Atendimento funcional, mas sem diferenciais", "valor": 3},
                    {"texto": "Alto - Atendimento ágil e clientes satisfeitos", "valor": 4}
                ]
            }
        ]
    },
    "Operação, Estoque e Logística": {
        "abreviacao": "Operação",
        "perguntas": [
            {
                "id": "oper_q1",
                "pergunta": "Como você avalia a organização e eficiência da sua rotina, processos ou operação?",
                "opcoes": [
                    {"texto": "Crítico - Muitos gargalos e retrabalho", "valor": 1},
                    {"texto": "Baixo - Processos manuais e pouco controle", "valor": 2},
                    {"texto": "Médio - Organizado, mas com pontos de melhoria", "valor": 3},
                    {"texto": "Alto - Processos fluidos e eficientes", "valor": 4}
                ]
            }
        ]
    },
    "Sustentabilidade Financeira": {
        "abreviacao": "Financeiro",
        "perguntas": [
            {
                "id": "finan_q1",
                "pergunta": "Como você avalia sua organização financeira atualmente (pessoal ou do negócio)?",
                "opcoes": [
                    {"texto": "Crítico - Sem clareza de custos e margens", "valor": 1},
                    {"texto": "Baixo - Controle básico, mas com insegurança", "valor": 2},
                    {"texto": "Médio - Boa clareza, mas falta planejamento", "valor": 3},
                    {"texto": "Alto - Controle total e planejamento futuro", "valor": 4}
                ]
            }
        ]
    },
    "Concorrência e Diferenciais": {
        "abreviacao": "Estratégia",
        "perguntas": [
            {
                "id": "concor_q1",
                "pergunta": "Como você avalia seu posicionamento no mercado frente à concorrência?",
                "opcoes": [
                    {"texto": "Crítico - Sem diferenciais claros", "valor": 1},
                    {"texto": "Baixo - Conhece concorrentes, mas não se destaca", "valor": 2},
                    {"texto": "Médio - Diferenciais percebidos por alguns clientes", "valor": 3},
                    {"texto": "Alto - Posicionamento forte e metas claras", "valor": 4}
                ]
            }
        ]
    },
    "Tecnologia e Inovação": {
        "abreviacao": "Tecnologia",
        "perguntas": [
            {
                "id": "tecno_q1",
                "pergunta": "Como você avalia o nível de digitalização e uso de tecnologia no seu negócio?",
                "opcoes": [
                    {"texto": "Crítico - Processos totalmente analógicos", "valor": 1},
                    {"texto": "Baixo - Uso básico de ferramentas digitais", "valor": 2},
                    {"texto": "Médio - Tecnologia presente em partes do negócio", "valor": 3},
                    {"texto": "Alto - Uso avançado de automação e dados", "valor": 4}
                ]
            }
        ]
    },
    "Comercial e Marketing": {
        "abreviacao": "Marketing",
        "perguntas": [
            {
                "id": "mkt_q1",
                "pergunta": "Como você avalia sua capacidade de gerar oportunidades e converter vendas?",
                "opcoes": [
                    {"texto": "Crítico - Dificuldade extrema em atrair clientes", "valor": 1},
                    {"texto": "Baixo - Presença digital fraca e pouca conversão", "valor": 2},
                    {"texto": "Médio - Estratégia funcional, mas inconstante", "valor": 3},
                    {"texto": "Alto - Estratégia estruturada e bons resultados", "valor": 4}
                ]
            }
        ]
    }
}

# Configurações específicas para o Formulário de Acolhimento
ACOLHIMENTO_CONFIG = {
    "Mapeamento Inicial": {
        "disponibilidade": [
            "Dias de semana — manhã ou tarde",
            "Dias de semana — noite",
            "Apenas finais de semana",
            "Dias de semana e finais de semana"
        ],
        "canais": [
            "WhatsApp",
            "Redes Sociais",
            "Telefone",
            "E-mail",
            "Atendimento presencial",
            "Site",
            "Plataformas digitais / marketplaces",
            "Outro",
            "Não se aplica"
        ]
    },
    "Radar de Demandas": {
        "intro": "Agora, vamos passar por algumas áreas/temas importantes para você, ou para o seu negócio, para identificar onde você sente a maior necessidade de apoio. Não se preocupe em dar muitos detalhes agora, apenas a sua percepção inicial.",
        "areas": [
            {
                "nome": "Tecnologia e Inovação",
                "abreviacao": "TEC",
                "reflexao": "Como você avalia o nível de organização, digitalização e uso de tecnologia na sua rotina profissional ou no seu negócio? Você acredita que poderia ganhar mais eficiência, produtividade ou competitividade com melhor uso de ferramentas digitais, automação, análise de dados ou soluções inovadoras?"
            },
            {
                "nome": "Marketing e Vendas",
                "abreviacao": "MKT",
                "reflexao": "Como está a sua presença digital e a captação de novos clientes? Você sente que seus processos de venda e divulgação são eficazes?"
            },
            {
                "nome": "Processos e Operações",
                "abreviacao": "PROC",
                "reflexao": "Sua rotina de trabalho é organizada? Os processos do seu negócio são claros e padronizados para evitar erros e retrabalho?"
            },
            {
                "nome": "Gestão Financeira",
                "abreviacao": "FIN",
                "reflexao": "Como você lida com as finanças? Existe clareza sobre lucros, despesas e investimentos necessários para o crescimento?"
            },
            {
                "nome": "Pessoas e Liderança",
                "abreviacao": "PES",
                "reflexao": "Como está o engajamento da equipe (se houver) ou a sua própria gestão de tempo e liderança frente aos desafios?"
            },
            {
                "nome": "Estratégia e Mercado",
                "abreviacao": "EST",
                "reflexao": "Você tem clareza de onde quer chegar e como se diferenciar da concorrência no mercado atual?"
            },
            {
                "nome": "Experiência do Cliente",
                "abreviacao": "CLI",
                "reflexao": "Como você avalia a satisfação dos seus clientes e a jornada deles desde o primeiro contato até o pós-venda?"
            }
        ],
        "escala_demanda": [
            {"texto": "Demanda Muito Baixa", "valor": 5},
            {"texto": "Demanda Baixa", "valor": 4},
            {"texto": "Demanda Média", "valor": 3},
            {"texto": "Demanda Alta", "valor": 2},
            {"texto": "Demanda Crítica", "valor": 1}
        ],
        "escala_interesse": [
            {"texto": "Nenhum Interesse", "valor": 5},
            {"texto": "Baixo Interesse", "valor": 4},
            {"texto": "Interesse Moderado", "valor": 3},
            {"texto": "Alto Interesse", "valor": 2},
            {"texto": "Interesse Muito Alto", "valor": 1}
        ]
    }
}

# Configurações do Google Drive
GDRIVE_CONFIG = {
    "ID_DIAGNOSTICO": "1ttG1OxbuROj4zWCqIq0KPaFObbLTyltV",
    "ID_ACOLHIMENTO": "10XrquN7q2x8rOok7GnR3tOQgjAXdUNPA",
    "client_secret.json": "client_secret.json",
    "https://www.googleapis.com/auth/drive": ["https://www.googleapis.com/auth/drive"]
}

# Listas Auxiliares
LISTA_DIRECIONAMENTO = ["Eventos", "Programas", "Mandala de Soluções", "Trilha do Conhecimento", "Diagnóstico Completo", "Negociação de Nova Parceria"]
LISTA_DOR_PRINCIPAL = ["Marketing", "Atendimento ao cliente", "Financeiro"]
LISTA_SOLUCAO_OFERTADA = ["Evento x", "Evento y", "Solução 1 da mandala", "Solução 2 da mandala"]
LISTA_ESTADOS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
LISTA_SETORES = ["Comércio", "Serviços", "Indústria", "Agronegócio", "Outro"]
LOGO_URL = "https://exemplo.com/logo.png"

# Catálogo automatizado de Soluções
CATALOGO_SOLUCOES = {
    "Nenhuma": {
        "descricao": "", 
        "parceiro": "", 
        "custo": ""
    },
    "CDL Negócios": {"descricao": "Descrição XXXXXXXX", "parceiro": "CDL", "custo": "R$ 2,00"},
    "Cemig Sim": {"descricao": "Descrição XXXXXXXX", "parceiro": "Parceiro a definir", "custo": "R$ 2,00"},
    "Centro de Convenções": {"descricao": "Descrição XXXXXXXX", "parceiro": "Parceiro a definir", "custo": "R$ 2,00"},
    "Instagram Day + Facebook Day + Whatsapp Day": {"descricao": "Descrição XXXXXXXX", "parceiro": "Parceiro a definir", "custo": "R$ 2,00"},
    "Como vender em Marketplaces: Mercado Livre, Shopee e Amazon": {"descricao": "Descrição XXXXXXXX", "parceiro": "Parceiro a definir", "custo": "R$ 2,00"},
    "Curso Iniciantes Digital - Sebrae Play": {"descricao": "Descrição XXXXXXXX", "parceiro": "Sebrae", "custo": "R$ 2,00"},
    "Curso Aprendiz Digital - Sebrae Play": {"descricao": "Descrição XXXXXXXX", "parceiro": "Sebrae", "custo": "R$ 2,00"},
    "Curso Empreendedor Digital - Sebrae Play": {"descricao": "Descrição XXXXXXXX", "parceiro": "Sebrae", "custo": "R$ 2,00"},
    "Curso Inovador Digital - Sebrae Play": {"descricao": "Descrição XXXXXXXX", "parceiro": "Sebrae", "custo": "R$ 2,00"},
    "Luz, Câmera, Conversão - Sebrae Play": {"descricao": "Descrição XXXXXXXX", "parceiro": "Sebrae", "custo": "R$ 2,00"},
    "SPC Registros": {"descricao": "Descrição XXXXXXXX", "parceiro": "SPC", "custo": "R$ 2,00"},
    "CDL Cobrança": {"descricao": "Descrição XXXXXXXX", "parceiro": "CDL", "custo": "R$ 2,00"},
    "Garantia de Cheques": {"descricao": "Descrição XXXXXXXX", "parceiro": "Parceiro a definir", "custo": "R$ 2,00"},
    "BDMG para acesso ao crédito": {"descricao": "Descrição XXXXXXXX", "parceiro": "BDMG", "custo": "R$ 2,00"},
    "Marketing de Relacionamento - Sebrae Play": {"descricao": "Descrição XXXXXXXX", "parceiro": "Sebrae", "custo": "R$ 2,00"},
    "Plano de Saúde (Unimed e Hapvida)": {"descricao": "Descrição XXXXXXXX", "parceiro": "Unimed/Hapvida", "custo": "R$ 2,00"},
    "Cartão Saúde": {"descricao": "Descrição XXXXXXXX", "parceiro": "Parceiro a definir", "custo": "R$ 2,00"},
    "SPC AVISA": {"descricao": "Descrição XXXXXXXX", "parceiro": "SPC", "custo": "R$ 2,00"},
    "Maxbot - Integração de chatbot": {"descricao": "Descrição XXXXXXXX", "parceiro": "Maxbot", "custo": "R$ 2,00"},
    "Maxbot - Treinamentos de Ferramentas de IA para Atendimento": {"descricao": "Descrição XXXXXXXX", "parceiro": "Maxbot", "custo": "R$ 2,00"},
    "Maxbot - Treinamentos de Boas Práticas de Atendimento no WhatsApp": {"descricao": "Descrição XXXXXXXX", "parceiro": "Maxbot", "custo": "R$ 2,00"},
    "GeoUAI - Geolocalização de Ponto Comercial": {
        "descricao": "Atendimento no ponto físico > É elaborado um relatório de análise sobre o ponto comercial, apontando possibilidades de melhorias. Indicam também questões de precificação e portfólio de produtos.", 
        "parceiro": "GeoUAI", 
        "custo": "R$ 2,00"
    },
    "GeoUAI - Geolocalização de Tráfego Pago": {
        "descricao": "Atendimento online > Normalmente, eles fazem contratos de 3 meses para o acompanhamento de Tráfego Pago.", 
        "parceiro": "GeoUAI", 
        "custo": "R$ 2,00"
    },
    "Inup": {
        "descricao": "Ecossistema de soluções contábeis e financeiras para empreendedores, startups e empresas em crescimento. Com abordagem consultiva e foco em tecnologia.", 
        "parceiro": "Inup", 
        "custo": "R$ 2,00"
    },
    "PaperUP": {
        "descricao": "Sistemas de gestão personalizados para as empresas (controle financeiro, estoque, caixa, PDV, orçamentos, sites, delivery, cupons e notas fiscais, etc.).", 
        "parceiro": "PaperUP", 
        "custo": "R$ 2,00"
    },
    "Oficina Inteligência Financeira - Sebrae Play": {"descricao": "Descrição XXXXXXXX", "parceiro": "Sebrae", "custo": "R$ 2,00"}
}