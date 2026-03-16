# Perguntas do diagnósticos e configurações
DIAGNOSTICO_CONFIG = {
    "Recursos Humanos": {
        "abreviacao": "Recursos Humanos",
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
                    {"texto": "Existe estruturado e periodicamente", "valor": 4}
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
        "abreviacao": "Atendimento ao Cliente",
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
        "abreviacao": "Operação, Estoque<br>e Logística",
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
        "abreviacao": "Sustentabilidade Financeira",
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
        "abreviacao": "Concorrência e Diferenciais",
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
        "abreviacao": "Tecnologia e Inovação",
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
        "abreviacao": "Comercial e Marketing",
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

ACOLHIMENTO_CONFIG = {
    "Mapeamento Inicial": {
        "disponibilidade": [
            "Dias de semana - manhã ou tarde",
            "Dias de semana - noite",
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
                "abreviacao": "Tecnologia e Inovação",
                "reflexao": "Como você avalia o uso de tecnologia e inovação na sua rotina profissional ou no seu negócio? Você sente necessidade de aprender ou utilizar melhor ferramentas digitais, automatizar processos, atuar no ambiente online ou explorar soluções como inteligência artificial?"
            },
            {
                "nome": "Comercial e Marketing",
                "abreviacao": "Comercial e Marketing",
                "reflexao": "Em relação à divulgação, vendas ou posicionamento, como você avalia a forma como você (ou seu negócio) se apresenta e se comunica com o público? Você sente que poderia melhorar sua presença digital, estratégias de venda, redes sociais ou a forma de atrair clientes e oportunidades?"
            },
            {
                "nome": "Operação e Logística",
                "abreviacao": "Operação e Logística",
                "reflexao": "Sobre a organização do dia a dia, processos internos ou rotinas de trabalho, você identifica pontos que poderiam ser mais eficientes? Por exemplo, gestão do tempo, organização de atividades, controle de recursos, entregas ou fluxo de trabalho."
            },
            {
                "nome": "Sustentabilidade Financeira",
                "abreviacao": "Sustentabilidade Financeira",
                "reflexao": "Pensando na parte financeira, como você avalia hoje sua organização e segurança financeira, pessoal ou do negócio? Existem desafios como falta de controle, dificuldade de planejamento, gestão de custos, acesso a crédito ou geração de renda sustentável?"
            },
            {
                "nome": "Recursos Humanos",
                "abreviacao": "Recursos Humanos",
                "reflexao": "Quando falamos de pessoas, equipes ou parcerias, você enfrenta desafios relacionados à comunicação, liderança, divisão de tarefas, engajamento, contratação ou desenvolvimento de pessoas?"
            },
            {
                "nome": "Concorrência e Diferenciais:",
                "abreviacao": "Concorrência e Diferenciais:",
                "reflexao": "Em relação ao mercado em que você atua (ou à sua área profissional), como você avalia o seu posicionamento estratégico frente à concorrência? Você possui clareza sobre seus objetivos de posicionamento, público-alvo e diferenciais competitivos, e utiliza algum tipo de planejamento, metas ou ferramentas para acompanhar se você (ou seu negócio) está se destacando e sendo escolhido em relação a outras opções do mercado?"
            },
            {
                "nome": "Atendimento ao Cliente",
                "abreviacao": "Atendimento ao Cliente",
                "reflexao": "Por fim, como você avalia a experiência de atendimento e relacionamento que você (ou seu negócio) oferece às pessoas com quem se relaciona - clientes, parceiros ou público em geral? Você considera esse um ponto que poderia ser aprimorado?"
            }
        ],
        "escala_demanda": [
            {"texto": "Demanda Muito Baixa", "valor": 1},
            {"texto": "Demanda Baixa", "valor": 2},
            {"texto": "Demanda Média", "valor": 3},
            {"texto": "Demanda Alta", "valor": 4},
            {"texto": "Demanda Crítica", "valor": 5}
        ],
        "escala_interesse": [
            {"texto": "Nenhum Interesse", "valor": 1},
            {"texto": "Baixo Interesse", "valor": 2},
            {"texto": "Interesse Moderado", "valor": 3},
            {"texto": "Alto Interesse", "valor": 4},
            {"texto": "Interesse Muito Alto", "valor": 5}
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
LISTA_DIRECIONAMENTO = ["Eventos e Programas", "Mandala de Soluções", "Trilha do Conhecimento", "Diagnóstico Completo", "Negociação de Nova Parceria"]
LISTA_DOR_PRINCIPAL = [
    "Atendimento ao Cliente: Agilidade e Estrutura de Atendimento",
    "Atendimento ao Cliente: Relacionamento, Fidelização e Pós-venda",
    "Atendimento ao Cliente: Perfil e Inteligência sobre o Cliente",
    "Comercial e Marketing: Melhoria de Vendas",
    "Comercial e Marketing: Estruturação de Canais Digitais e Vendas Online",
    "Comercial e Marketing: Estratégia de Marketing e Posicionamento Digital",
    "Operação, Logística e Estoque: Gerenciamento e Controle de Estoque",
    "Operação, Logística e Estoque: Logística e Rotas",
    "Operação, Logística e Estoque: Compras e Fornecedores",
    "Operação, Logística e Estoque: Segurança do Trabalho",
    "Recursos Humanos: Recrutamento e Seleção",
    "Recursos Humanos: Qualificação e Capacitação",
    "Recursos Humanos: Gestão e Produtividade da Equipe",
    "Sustentabilidade Financeira: Gestão Financeira",
    "Sustentabilidade Financeira: Gestão Jurídica e Contábil",
    "Sustentabilidade Financeira: Recursos Financeiros e Capital",
    "Sustentabilidade Financeira: Precificação",
    "Tecnologia e Inovação: Gestão e Automação de Processos",
    "Tecnologia e Inovação: Análise e Uso de Dados",
    "Concorrência e Diferenciais: Planejamento Estratégico",
    "Concorrência e Diferenciais: Diferenciais Competitivos e Inovação",
    "Concorrência e Diferenciais: Análise e Posicionamento de Mercado"
]
LISTA_ESTADOS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
LISTA_SETORES = ["Comércio", "Serviços", "Indústria", "Agronegócio", "Outro"]
LOGO_URL = "https://exemplo.com/logo.png"


# --- NOVOS CATÁLOGOS PARA O ACOLHIMENTO E DIAGNÓSTICO ---

CATALOGO_MANDALA = {
    "Centro de Convenções": {"descricao": "Acesso ao Centro de Convenções da CDL/BH.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "Plano de Saúde (Unimed e Hapvida)": {"descricao": "Condições especiais em planos de saúde Unimed e Hapvida.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "Cartão Saúde": {"descricao": "Acesso a benefícios e descontos na área da saúde.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "Cemig Sim (Desconto na conta)": {"descricao": "Desconto na conta de luz através da parceria com a Cemig Sim.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "SPC Registros": {"descricao": "Registro de clientes inadimplentes no SPC Brasil e envio de carta de notificação para regularização.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "CDL Cobrança": {"descricao": "Gestão completa da carteira de inadimplência da sua empresa feita pela CDL/BH.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "Garantia de Cheques": {"descricao": "Consulta e garantia de recebimento de cheques. Reembolso em caso de devolução pelos bancos.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "BDMG": {"descricao": "Acesso facilitado a linhas de crédito através do BDMG.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "SPC AVISA": {"descricao": "Monitoramento de inclusão/exclusão de informações negativas e consultas realizadas no seu CPF ou CNPJ.", "instituicao": "CDL/BH", "custo": "Não informado"},
    "CDL Negócios (Grupos Temáticos)": {"descricao": "Participação em grupos temáticos (Moda, Pet, Gastronomia, etc.) para networking, viagens e eventos focados no seu setor.", "instituicao": "CDL/BH", "custo": "Não informado"}
}

CATALOGO_TRILHA = {
    "WhatsApp Day": {
        "descricao": "Aprenda a usar o WhatsApp Business como ferramenta de atendimento, relacionamento e vendas, incluindo automação e catálogo.",
        "instituicao": "SEBRAE MG", "carga_horaria": "13 horas", "link": "https://sebraeplay.com.br/cursos/whatsapp-day", "custo": "Gratuito"
    },
    "Comportamento do Consumidor Digital": {
        "descricao": "Entenda as tendências do consumidor online e como transformar leads em clientes fiéis criando conexões de valor.",
        "instituicao": "SEBRAE MG", "carga_horaria": "2 horas", "link": "https://sebraeplay.com.br/cursos/comportamento-do-consumidor-digital", "custo": "Gratuito"
    },
    "Apresentações de Impacto": {
        "descricao": "Aprenda a criar apresentações envolventes usando narrativa, design e técnicas de persuasão para encantar seu público.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/apresentacoes-de-impacto", "custo": "Gratuito"
    },
    "Fundamentos sobre Marketing": {
        "descricao": "Fortaleça sua marca aprendendo desde proposta de valor e público-alvo até marketing digital e fidelização.",
        "instituicao": "IEBT", "carga_horaria": "1 hora", "link": "https://www.skininnovation.com.br/course/horizonte", "custo": "Gratuito"
    },
    "E-mail marketing para a sua empresa": {
        "descricao": "Crie campanhas de e-mail marketing com foco em engajamento e conversão, abordando conteúdo e análise de resultados.",
        "instituicao": "SEBRAE MG", "carga_horaria": "4 horas", "link": "https://sebraeplay.com.br/cursos/e-mail-marketing-para-a-sua-empresa", "custo": "Gratuito"
    },
    "Luz, Câmera e Conversão": {
        "descricao": "Use vídeos como ferramenta de vendas. Aprenda sobre planejamento, gravação, edição e análise de desempenho.",
        "instituicao": "SEBRAE MG", "carga_horaria": "2 horas", "link": "https://sebraeplay.com.br/cursos/luz-camera-e-conversao", "custo": "Gratuito"
    },
    "Planejamento de Marketing Digital": {
        "descricao": "Estruture um planejamento estratégico digital alinhado às tendências para gerar resultados no ambiente online.",
        "instituicao": "SEBRAE MG", "carga_horaria": "4 horas", "link": "https://sebraeplay.com.br/cursos/planejamento-de-marketing-digital", "custo": "Gratuito"
    },
    "Novo Marketing de Relacionamento": {
        "descricao": "Fortaleça a relação com clientes mapeando a jornada de compra e criando experiências marcantes e duradouras.",
        "instituicao": "SEBRAE MG", "carga_horaria": "4 horas", "link": "https://sebraeplay.com.br/cursos/novo-marketing-relacionamento", "custo": "Gratuito"
    },
    "Impulsionamento de Vendas Digitais": {
        "descricao": "Escale resultados impulsionando vendas em canais digitais e marketplaces. Entenda o consumidor e estratégias de conversão.",
        "instituicao": "IEBT", "carga_horaria": "40 minutos", "link": "https://www.skininnovation.com.br/course/horizonte", "custo": "Gratuito"
    },
    "Instagram Day": {
        "descricao": "Utilize o Instagram de forma estratégica abordando criação de conteúdo, anúncios, métricas e funcionalidades da plataforma.",
        "instituicao": "SEBRAE MG", "carga_horaria": "13 horas", "link": "https://sebraeplay.com.br/cursos/instagram-day", "custo": "Gratuito"
    },
    "Facebook Day": {
        "descricao": "Explore Grupos, Marketplace, Stories e anúncios do Facebook para gerar engajamento e vendas.",
        "instituicao": "SEBRAE MG", "carga_horaria": "13 horas", "link": "https://sebraeplay.com.br/cursos/facebook-day", "custo": "Gratuito"
    },
    "Empreenda: Vendas Automatizadas": {
        "descricao": "Crie sistemas automáticos de captação e conversão usando ferramentas digitais para vender com menos esforço manual.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/empreenda-vendas-automatizadas", "custo": "Gratuito"
    },
    "Empreenda: Vendas Pontuais": {
        "descricao": "Estruture interações eficientes com clientes, combinando automação e toque humano para gerar experiências positivas.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/empreenda-vendas-pontuais", "custo": "Gratuito"
    },
    "Empreenda: Vendas Personalizadas": {
        "descricao": "Ofereça um atendimento mais humano e estratégico, adaptando soluções às necessidades do cliente para fidelização.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/empreenda-vendas-personalizadas", "custo": "Gratuito"
    },
    "Empreenda: Vendas Dedicadas": {
        "descricao": "Desenvolva relações contínuas com clientes focando na identificação de necessidades e aumento do valor percebido.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/empreenda-vendas-dedicadas", "custo": "Gratuito"
    },
    "Mais lucro e menos custo no setor de Alimentação": {
        "descricao": "Aplique práticas de ESG em negócios de alimentação para reduzir custos e aumentar a lucratividade de forma sustentável.",
        "instituicao": "SEBRAE MG", "carga_horaria": "4 horas", "link": "https://sebraeplay.com.br/cursos/mais-lucro-menos-custo-setor-de-alimentacao", "custo": "Gratuito"
    },
    "Gestão Inteligente na Moda com mais resultados": {
        "descricao": "Alinhe sustentabilidade, organização interna e aumento de lucro aplicando práticas de ESG em negócios de moda.",
        "instituicao": "SEBRAE MG", "carga_horaria": "4 horas", "link": "https://sebraeplay.com.br/cursos/gestao-inteligente-na-moda-com-mais-resultados", "custo": "Gratuito"
    },
    "Turismo Gastronômico": {
        "descricao": "Transforme a gastronomia em diferencial competitivo criando experiências, valorizando produtos locais e parcerias.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas e 30 minutos", "link": "https://sebraeplay.com.br/cursos/turismo-gastronomico", "custo": "Gratuito"
    },
    "Oficina Adaptabilidade, in book": {
        "descricao": "Reflita sobre propósito e transformação conhecendo conceitos de adaptabilidade e novos modelos econômicos.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/oficina-adaptabilidade-in-book", "custo": "Gratuito"
    },
    "Planejamento e Gestão Estratégica": {
        "descricao": "Construa um planejamento eficiente com ferramentas como FOFA, metas SMART, 5W2H e KPIs para organizar o crescimento.",
        "instituicao": "IEBT", "carga_horaria": "45 minutos", "link": "https://www.skininnovation.com.br/course/horizonte", "custo": "Gratuito"
    },
    "Gestão de Pessoas e Liderança": {
        "descricao": "Forme equipes de alta performance aprendendo sobre segurança psicológica, propósito e ferramentas como OKRs, Kanban e RACI.",
        "instituicao": "IEBT", "carga_horaria": "45 minutos", "link": "https://www.skininnovation.com.br/course/horizonte", "custo": "Gratuito"
    },
    "Inteligência Emocional": {
        "descricao": "Fortaleça sua saúde mental desenvolvendo habilidades para lidar com emoções, estresse e desafios profissionais.",
        "instituicao": "SEBRAE MG", "carga_horaria": "14 horas", "link": "https://sebraeplay.com.br/cursos/inteligencia-emocional", "custo": "Gratuito"
    },
    "Oficina Produtividade, in book": {
        "descricao": "Aumente resultados com equilíbrio usando técnicas de priorização, gestão do tempo e foco baseadas no essencialismo.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/oficina-produtividade-in-book", "custo": "Gratuito"
    },
    "Oficina Relacionamento, in book": {
        "descricao": "Desenvolva relacionamentos profissionais estratégicos usando conceitos de influência e networking.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/oficina-relacionamento-in-book", "custo": "Gratuito"
    },
    "In book Pocket Inteligência Financeira": {
        "descricao": "Mude sua mentalidade financeira unindo organização e autoconhecimento para tomar decisões mais conscientes.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/in-book-pocket-inteligencia-financeira", "custo": "Gratuito"
    },
    "MEI: Já tem seu CNPJ, e agora?": {
        "descricao": "Tome decisões com segurança conhecendo as obrigações, rotinas e gestão do MEI para manter seu CNPJ em ordem.",
        "instituicao": "SEBRAE MG", "carga_horaria": "4 horas", "link": "https://sebraeplay.com.br/cursos/mei-ja-tem-seu-cnpj", "custo": "Gratuito"
    },
    "MEI: Como iniciar o seu negócio": {
        "descricao": "Transforme uma ideia em negócio formalizado como MEI aprendendo sobre planejamento e aspectos jurídicos e tributários.",
        "instituicao": "SEBRAE MG", "carga_horaria": "4 horas", "link": "https://sebraeplay.com.br/cursos/mei-como-iniciar-o-seu-negocio", "custo": "Gratuito"
    },
    "ALVO Sebrae: gestão inteligente de resultados": {
        "descricao": "Use a plataforma ALVO para planejar metas, acompanhar indicadores e tomar decisões baseadas em dados.",
        "instituicao": "SEBRAE MG", "carga_horaria": "Não informado", "link": "https://sebraeplay.com.br/cursos/alvo-gestao-inteligente-de-resultados", "custo": "Gratuito"
    },
    "ChatGPT para pequenos negócios": {
        "descricao": "Otimize tarefas, crie conteúdos e melhore a comunicação usando o ChatGPT de forma prática no dia a dia do negócio.",
        "instituicao": "SEBRAE MG", "carga_horaria": "35 minutos", "link": "https://sebraeplay.com.br/cursos/chatgpt-para-pequenos-negocios", "custo": "Gratuito"
    },
    "Iniciante Digital: despertando para o digital": {
        "descricao": "Inicie o desenvolvimento de habilidades digitais conhecendo conceitos básicos e navegação segura.",
        "instituicao": "SEBRAE MG", "carga_horaria": "2 horas", "link": "https://sebraeplay.com.br/cursos/iniciante-digital-despertando-para-o-digital", "custo": "Gratuito"
    },
    "Inovador Digital: automatizando e escalando": {
        "descricao": "Escale seu negócio implantando uma cultura de inovação, explorando automação, IA e análise de dados.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/inovador-digital-automatizando-escalando", "custo": "Gratuito"
    },
    "Aprendiz Digital: Experimentando as Primeiras Ferramentas": {
        "descricao": "Prepare-se para o mercado digital aprendendo fundamentos de tecnologia, ferramentas, marketing e programação.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/aprendiz-digital", "custo": "Gratuito"
    },
    "Empreendedor Digital: integrando e otimizando": {
        "descricao": "Melhore a operação digital e a expansão de vendas aprendendo a integrar canais e automatizar processos.",
        "instituicao": "SEBRAE MG", "carga_horaria": "3 horas", "link": "https://sebraeplay.com.br/cursos/empreendedor-digital", "custo": "Gratuito"
    }
}