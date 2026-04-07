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
                "pergunta": "O tempo de resposta ao cliente já gerou perda de venda ou reclamação?",
                "opcoes": [
                    {"texto": "Sim, com frequência", "valor": 1},
                    {"texto": "Sim, algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "atend_q2",
                "pergunta": "Existe padrão definido de atendimento (roteiro, abordagem, linguagem)?",
                "opcoes": [
                    {"texto": "Não existe padrão", "valor": 1},
                    {"texto": "Existe informalmente", "valor": 2},
                    {"texto": "Existe parcialmente estruturado", "valor": 3},
                    {"texto": "Existe estruturado e aplicado por toda equipe", "valor": 4}
                ]
            },
            {
                "id": "atend_q3",
                "pergunta": "Os canais de atendimento (WhatsApp, redes sociais, presencial) são integrados ou organizados em um único sistema?",
                "opcoes": [
                    {"texto": "Não há organização", "valor": 1},
                    {"texto": "São separados e pouco controlados", "valor": 2},
                    {"texto": "Há alguma organização", "valor": 3},
                    {"texto": "São integrados e monitorados", "valor": 4}
                ]
            },
            {
                "id": "atend_q4",
                "pergunta": "A empresa utiliza ferramentas de automação (respostas automáticas, chatbot, CRM integrado)?",
                "opcoes": [
                    {"texto": "Não utiliza", "valor": 1},
                    {"texto": "Utiliza muito pouco", "valor": 2},
                    {"texto": "Utiliza parcialmente", "valor": 3},
                    {"texto": "Utiliza de forma estruturada", "valor": 4}
                ]
            },
            {
                "id": "atend_q5",
                "pergunta": "A empresa monitora a taxa de retorno ou recompra dos clientes?",
                "opcoes": [
                    {"texto": "Não monitora", "valor": 1},
                    {"texto": "Tem percepção informal", "valor": 2},
                    {"texto": "Monitora parcialmente", "valor": 3},
                    {"texto": "Monitora com indicadores claros", "valor": 4}
                ]
            },
            {
                "id": "atend_q6",
                "pergunta": "Existe sistema ou base estruturada para gestão de contatos (CRM)?",
                "opcoes": [
                    {"texto": "Não existe", "valor": 1},
                    {"texto": "Existe informalmente (planilhas/contatos soltos)", "valor": 2},
                    {"texto": "Existe parcialmente estruturado", "valor": 3},
                    {"texto": "Existe CRM organizado e utilizado estrategicamente", "valor": 4}
                ]
            },
            {
                "id": "atend_q7",
                "pergunta": "Existe processo ativo de acompanhamento pós-venda?",
                "opcoes": [
                    {"texto": "Não existe", "valor": 1},
                    {"texto": "Só ocorre quando há problema", "valor": 2},
                    {"texto": "Ocorre ocasionalmente", "valor": 3},
                    {"texto": "Existe processo estruturado (agradecimento, suporte, novas ofertas)", "valor": 4}
                ]
            },
            {
                "id": "atend_q8",
                "pergunta": "A empresa realiza pesquisa de satisfação e utiliza os dados para melhoria?",
                "opcoes": [
                    {"texto": "Nunca realizou", "valor": 1},
                    {"texto": "Realiza informalmente", "valor": 2},
                    {"texto": "Realiza com alguma análise", "valor": 3},
                    {"texto": "Realiza sistematicamente e aplica melhorias", "valor": 4}
                ]
            },
            {
                "id": "atend_q9",
                "pergunta": "Existe canal estruturado para reclamações e resolução de problemas?",
                "opcoes": [
                    {"texto": "Não existe", "valor": 1},
                    {"texto": "É informal", "valor": 2},
                    {"texto": "Existe parcialmente", "valor": 3},
                    {"texto": "Existe processo claro e acompanhado", "valor": 4}
                ]
            },
            {
                "id": "atend_q10",
                "pergunta": "A empresa possui definição clara de público-alvo ou persona?",
                "opcoes": [
                    {"texto": "Não sabe definir", "valor": 1},
                    {"texto": "Tem ideia genérica", "valor": 2},
                    {"texto": "Tem definição razoável", "valor": 3},
                    {"texto": "Tem persona clara e documentada", "valor": 4}
                ]
            },
            {
                "id": "atend_q11",
                "pergunta": "A empresa coleta e analisa dados sobre comportamento de compra (frequência, ticket médio, preferências)?",
                "opcoes": [
                    {"texto": "Não coleta dados", "valor": 1},
                    {"texto": "Coleta parcialmente", "valor": 2},
                    {"texto": "Analisa ocasionalmente", "valor": 3},
                    {"texto": "Analisa e usa para decisões estratégicas", "valor": 4}
                ]
            },
            {
                "id": "atend_q12",
                "pergunta": "As informações dos clientes são utilizadas para campanhas personalizadas ou ações direcionadas?",
                "opcoes": [
                    {"texto": "Não utiliza", "valor": 1},
                    {"texto": "Utiliza raramente", "valor": 2},
                    {"texto": "Utiliza parcialmente", "valor": 3},
                    {"texto": "Utiliza de forma estratégica", "valor": 4}
                ]
            },
            {
                "id": "atend_q13",
                "pergunta": "Você acredita que deixa de vender por não conhecer melhor seu cliente?",
                "opcoes": [
                    {"texto": "Sim, com frequência", "valor": 1},
                    {"texto": "Às vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            }
        ]
    },
    "Operação, Estoque e Logística": {
        "abreviacao": "Operação, Estoque<br>e Logística",
        "perguntas": [
            {
                "id": "oper_q1",
                "pergunta": "Existe controle estruturado e atualizado de estoque?",
                "opcoes": [
                    {"texto": "Não existe controle", "valor": 1},
                    {"texto": "Controle informal e desatualizado", "valor": 2},
                    {"texto": "Controle manual organizado", "valor": 3},
                    {"texto": "Sistema informatizado integrado", "valor": 4}
                ]
            },
            {
                "id": "oper_q2",
                "pergunta": "A empresa tem precisão sobre quantidades disponíveis em estoque?",
                "opcoes": [
                    {"texto": "Não tem controle real", "valor": 1},
                    {"texto": "Tem apenas estimativa", "valor": 2},
                    {"texto": "Controle razoável", "valor": 3},
                    {"texto": "Controle exato e atualizado", "valor": 4}
                ]
            },
            {
                "id": "oper_q3",
                "pergunta": "Já ocorreu perda de venda por falta de produto disponível?",
                "opcoes": [
                    {"texto": "Frequentemente", "valor": 1},
                    {"texto": "Algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "oper_q4",
                "pergunta": "Existem produtos parados ou com giro muito baixo no estoque?",
                "opcoes": [
                    {"texto": "Sim, em grande volume", "valor": 1},
                    {"texto": "Sim, em volume moderado", "valor": 2},
                    {"texto": "Pequeno volume", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "oper_q5",
                "pergunta": "A empresa realiza inventários periódicos para conferência de estoque?",
                "opcoes": [
                    {"texto": "Nunca realiza", "valor": 1},
                    {"texto": "Realiza apenas quando há problema", "valor": 2},
                    {"texto": "Realiza ocasionalmente", "valor": 3},
                    {"texto": "Realiza periodicamente com controle formal", "valor": 4}
                ]
            },
            {
                "id": "oper_q6",
                "pergunta": "A organização ou disposição dos produtos já gerou dificuldade para o cliente encontrar o que procurava?",
                "opcoes": [
                    {"texto": "Sim, frequentemente", "valor": 1},
                    {"texto": "Algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "oper_q7",
                "pergunta": "A vitrine é utilizada como ferramenta estratégica para atrair clientes e promover produtos específicos?",
                "opcoes": [
                    {"texto": "Não há estratégia de vitrine", "valor": 1},
                    {"texto": "Montagem improvisada", "valor": 2},
                    {"texto": "Existe planejamento ocasional", "valor": 3},
                    {"texto": "Existe estratégia definida com foco comercial", "valor": 4}
                ]
            },
            {
                "id": "oper_q8",
                "pergunta": "Existe controle estruturado sobre prazos e entregas?",
                "opcoes": [
                    {"texto": "N/A - Não se aplica", "valor": 0},
                    {"texto": "Não existe controle", "valor": 1},
                    {"texto": "Controle informal", "valor": 2},
                    {"texto": "Controle parcial", "valor": 3},
                    {"texto": "Controle estruturado com acompanhamento", "valor": 4}
                ]
            },
            {
                "id": "oper_q9",
                "pergunta": "As rotas de entrega são planejadas para otimizar tempo e custo?",
                "opcoes": [
                    {"texto": "N/A - Não se aplica", "valor": 0},
                    {"texto": "Não há planejamento", "valor": 1},
                    {"texto": "Planejamento improvisado", "valor": 2},
                    {"texto": "Planejamento básico", "valor": 3},
                    {"texto": "Planejamento estruturado", "valor": 4}
                ]
            },
            {
                "id": "oper_q10",
                "pergunta": "Já houve reclamações ou perda de cliente por atraso na entrega?",
                "opcoes": [
                    {"texto": "N/A - Não se aplica", "valor": 0},
                    {"texto": "Sim, frequentemente", "valor": 1},
                    {"texto": "Algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "oper_q11",
                "pergunta": "Os fornecedores cumprem prazos e condições acordadas?",
                "opcoes": [
                    {"texto": "Frequentemente falham", "valor": 1},
                    {"texto": "Às vezes falham", "valor": 2},
                    {"texto": "Raramente falham", "valor": 3},
                    {"texto": "Cumprimento consistente", "valor": 4}
                ]
            },
            {
                "id": "oper_q12",
                "pergunta": "Existe planejamento prévio de compras baseado em giro e demanda?",
                "opcoes": [
                    {"texto": "Não existe", "valor": 1},
                    {"texto": "É feito de forma improvisada", "valor": 2},
                    {"texto": "Existe parcialmente", "valor": 3},
                    {"texto": "Existe planejamento estruturado", "valor": 4}
                ]
            },
            {
                "id": "oper_q13",
                "pergunta": "A empresa depende excessivamente de um único fornecedor?",
                "opcoes": [
                    {"texto": "Sim, totalmente dependente", "valor": 1},
                    {"texto": "Alta dependência", "valor": 2},
                    {"texto": "Dependência moderada", "valor": 3},
                    {"texto": "Fornecedores diversificados", "valor": 4}
                ]
            },
            {
                "id": "oper_q14",
                "pergunta": "A escolha de fornecedores considera critérios além do preço (qualidade, prazo, confiabilidade)?",
                "opcoes": [
                    {"texto": "Considera apenas preço", "valor": 1},
                    {"texto": "Considera preço e prazo", "valor": 2},
                    {"texto": "Considera múltiplos fatores", "valor": 3},
                    {"texto": "Possui critérios técnicos definidos", "valor": 4}
                ]
            },
            {
                "id": "oper_q15",
                "pergunta": "A empresa oferece treinamento de segurança adequado à atividade?",
                "opcoes": [
                    {"texto": "Não oferece", "valor": 1},
                    {"texto": "Oferece parcialmente", "valor": 2},
                    {"texto": "Oferece no início, sem reciclagem", "valor": 3},
                    {"texto": "Oferece e realiza reciclagens", "valor": 4}
                ]
            },
            {
                "id": "oper_q16",
                "pergunta": "A empresa monitora e registra ocorrências ou acidentes de trabalho?",
                "opcoes": [
                    {"texto": "Não monitora", "valor": 1},
                    {"texto": "Monitora informalmente", "valor": 2},
                    {"texto": "Registra parcialmente", "valor": 3},
                    {"texto": "Registra e acompanha indicadores", "valor": 4}
                ]
            },
            {
                "id": "oper_q17",
                "pergunta": "Acidentes ou falhas de segurança já impactaram a operação?",
                "opcoes": [
                    {"texto": "Sim, frequentemente", "valor": 1},
                    {"texto": "Algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Nunca", "valor": 4}
                ]
            },
            {
                "id": "oper_q18",
                "pergunta": "A empresa possui documentação e adequações obrigatórias de segurança atualizadas?",
                "opcoes": [
                    {"texto": "Não possui", "valor": 1},
                    {"texto": "Possui parcialmente", "valor": 2},
                    {"texto": "Possui, mas sem controle de atualização", "valor": 3},
                    {"texto": "Possui e mantém regularizadas", "valor": 4}
                ]
            }
        ]
    },
    "Sustentabilidade Financeira": {
        "abreviacao": "Sustentabilidade Financeira",
        "perguntas": [
            {
                "id": "finan_q1",
                "pergunta": "As finanças da empresa estão separadas das finanças pessoais?",
                "opcoes": [
                    {"texto": "Não há separação; todas as movimentações são misturadas", "valor": 1},
                    {"texto": "Há tentativa de separação, mas ainda ocorre mistura frequente", "valor": 2},
                    {"texto": "A maior parte está separada, com pequenos ajustes ou retiradas informais", "valor": 3},
                    {"texto": "As finanças são totalmente separadas, com pró-labore definido", "valor": 4}
                ]
            },
            {
                "id": "finan_q2",
                "pergunta": "A empresa possui controle estruturado de fluxo de caixa e acompanhamento financeiro periódico?",
                "opcoes": [
                    {"texto": "Não possui controle", "valor": 1},
                    {"texto": "Controle informal", "valor": 2},
                    {"texto": "Controle organizado, mas pouco analisado", "valor": 3},
                    {"texto": "Controle estruturado com análise frequente", "valor": 4}
                ]
            },
            {
                "id": "finan_q3",
                "pergunta": "O gestor conhece com clareza os principais números do negócio (faturamento, despesas, lucro, ponto de equilíbrio)?",
                "opcoes": [
                    {"texto": "Não conhece", "valor": 1},
                    {"texto": "Conhece superficialmente", "valor": 2},
                    {"texto": "Conhece parcialmente", "valor": 3},
                    {"texto": "Conhece com clareza e acompanha", "valor": 4}
                ]
            },
            {
                "id": "finan_q4",
                "pergunta": "As decisões financeiras são tomadas com base em dados ou percepção?",
                "opcoes": [
                    {"texto": "Apenas percepção", "valor": 1},
                    {"texto": "Mais percepção do que dados", "valor": 2},
                    {"texto": "Combinação de dados e percepção", "valor": 3},
                    {"texto": "Baseadas em indicadores claros", "valor": 4}
                ]
            },
            {
                "id": "finan_q5",
                "pergunta": "A contabilidade realiza apenas obrigações fiscais ou também oferece acompanhamento e orientação estratégica?",
                "opcoes": [
                    {"texto": "Apenas obrigações básicas", "valor": 1},
                    {"texto": "Orientação pontual", "valor": 2},
                    {"texto": "Algum acompanhamento", "valor": 3},
                    {"texto": "Acompanhamento consultivo", "valor": 4}
                ]
            },
            {
                "id": "finan_q6",
                "pergunta": "A empresa possui assessoria jurídica preventiva?",
                "opcoes": [
                    {"texto": "Não possui", "valor": 1},
                    {"texto": "Só busca advogado quando há problema", "valor": 2},
                    {"texto": "Possui contato eventual", "valor": 3},
                    {"texto": "Possui acompanhamento preventivo", "valor": 4}
                ]
            },
            {
                "id": "finan_q7",
                "pergunta": "A empresa já enfrentou demandas jurídicas com clientes ou colaboradores?",
                "opcoes": [
                    {"texto": "Sim, com frequência", "valor": 1},
                    {"texto": "Sim, algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Nunca", "valor": 4}
                ]
            },
            {
                "id": "finan_q8",
                "pergunta": "Existem pendências tributárias, trabalhistas ou documentais em aberto?",
                "opcoes": [
                    {"texto": "Sim, relevantes", "valor": 1},
                    {"texto": "Sim, pequenas pendências", "valor": 2},
                    {"texto": "Poucas pendências", "valor": 3},
                    {"texto": "Totalmente regularizada", "valor": 4}
                ]
            },
            {
                "id": "finan_q9",
                "pergunta": "A empresa possui capital de giro suficiente para manter a operação com segurança?",
                "opcoes": [
                    {"texto": "Não possui", "valor": 1},
                    {"texto": "Possui insuficiente", "valor": 2},
                    {"texto": "Possui razoável", "valor": 3},
                    {"texto": "Possui adequado", "valor": 4}
                ]
            },
            {
                "id": "finan_q10",
                "pergunta": "A empresa reinveste parte do lucro no próprio negócio (estrutura, estoque, marketing, tecnologia, equipe)?",
                "opcoes": [
                    {"texto": "Não reinveste; todo lucro é retirado", "valor": 1},
                    {"texto": "Reinveste raramente ou apenas quando sobra recurso", "valor": 2},
                    {"texto": "Reinveste parte do lucro de forma ocasional", "valor": 3},
                    {"texto": "Possui política ou prática consistente de reinvestimento", "valor": 4}
                ]
            },
            {
                "id": "finan_q11",
                "pergunta": "A falta de recursos financeiros já limitou investimentos ou crescimento?",
                "opcoes": [
                    {"texto": "Sim, frequentemente", "valor": 1},
                    {"texto": "Algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "finan_q12",
                "pergunta": "A empresa tem acesso estruturado a crédito quando necessário?",
                "opcoes": [
                    {"texto": "Não tem acesso", "valor": 1},
                    {"texto": "Tem com muita dificuldade", "valor": 2},
                    {"texto": "Tem com alguma burocracia", "valor": 3},
                    {"texto": "Tem acesso facilitado", "valor": 4}
                ]
            },
            {
                "id": "finan_q13",
                "pergunta": "A precificação é baseada em cálculo real de custos e margem?",
                "opcoes": [
                    {"texto": "É intuitiva", "valor": 1},
                    {"texto": "Baseada apenas na concorrência", "valor": 2},
                    {"texto": "Considera custos parcialmente", "valor": 3},
                    {"texto": "Baseada em custos + margem + estratégia", "valor": 4}
                ]
            },
            {
                "id": "finan_q14",
                "pergunta": "A empresa sabe a margem de lucro real por produto ou serviço?",
                "opcoes": [
                    {"texto": "Não sabe", "valor": 1},
                    {"texto": "Tem estimativa", "valor": 2},
                    {"texto": "Sabe parcialmente", "valor": 3},
                    {"texto": "Sabe com precisão", "valor": 4}
                ]
            },
            {
                "id": "finan_q15",
                "pergunta": "Já houve percepção de que o preço pode estar comprometendo a lucratividade?",
                "opcoes": [
                    {"texto": "Sim, claramente", "valor": 1},
                    {"texto": "Possivelmente", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            }
        ]
    },
    "Concorrência e Diferenciais": {
        "abreviacao": "Concorrência e Diferenciais",
        "perguntas": [
            {
                "id": "concor_q1",
                "pergunta": "A empresa possui direcionamento estratégico claro (missão, visão, metas definidas)?",
                "opcoes": [
                    {"texto": "Não possui definição", "valor": 1},
                    {"texto": "Possui ideias informais", "valor": 2},
                    {"texto": "Possui definição parcial", "valor": 3},
                    {"texto": "Possui direcionamento formalizado", "valor": 4}
                ]
            },
            {
                "id": "concor_q2",
                "pergunta": "Existem metas claras de faturamento, crescimento ou desempenho?",
                "opcoes": [
                    {"texto": "Não existem metas", "valor": 1},
                    {"texto": "Existem metas informais", "valor": 2},
                    {"texto": "Existem metas definidas, mas pouco acompanhadas", "valor": 3},
                    {"texto": "Existem metas acompanhadas por indicadores", "valor": 4}
                ]
            },
            {
                "id": "concor_q3",
                "pergunta": "Os resultados são acompanhados de forma estruturada e periódica?",
                "opcoes": [
                    {"texto": "Não há acompanhamento", "valor": 1},
                    {"texto": "Acompanhamento esporádico", "valor": 2},
                    {"texto": "Acompanhamento regular, mas sem análise aprofundada", "valor": 3},
                    {"texto": "Acompanhamento com indicadores e planos de ação", "valor": 4}
                ]
            },
            {
                "id": "concor_q4",
                "pergunta": "A empresa já realizou planejamento estratégico formal nos últimos 12 meses?",
                "opcoes": [
                    {"texto": "Nunca realizou", "valor": 1},
                    {"texto": "Realizou há muito tempo", "valor": 2},
                    {"texto": "Realizou, mas não executou completamente", "valor": 3},
                    {"texto": "Realiza e executa periodicamente", "valor": 4}
                ]
            },
            {
                "id": "concor_q5",
                "pergunta": "A empresa tem clareza sobre o que a diferencia dos concorrentes?",
                "opcoes": [
                    {"texto": "Não sabe diferenciar", "valor": 1},
                    {"texto": "Diferencial pouco claro", "valor": 2},
                    {"texto": "Diferencial razoavelmente definido", "valor": 3},
                    {"texto": "Diferencial claro e comunicado", "valor": 4}
                ]
            },
            {
                "id": "concor_q6",
                "pergunta": "A empresa desenvolve novos produtos/serviços com base em oportunidades de mercado?",
                "opcoes": [
                    {"texto": "Nunca desenvolve", "valor": 1},
                    {"texto": "Desenvolve raramente", "valor": 2},
                    {"texto": "Desenvolve ocasionalmente", "valor": 3},
                    {"texto": "Possui processo contínuo de inovação", "valor": 4}
                ]
            },
            {
                "id": "concor_q7",
                "pergunta": "Antes de lançar novidades, a empresa testa ou valida a aceitação do mercado?",
                "opcoes": [
                    {"texto": "Não testa", "valor": 1},
                    {"texto": "Testa informalmente", "valor": 2},
                    {"texto": "Testa parcialmente", "valor": 3},
                    {"texto": "Testa de forma estruturada", "valor": 4}
                ]
            },
            {
                "id": "concor_q8",
                "pergunta": "A ampliação do portfólio é baseada em análise de demanda e oportunidade?",
                "opcoes": [
                    {"texto": "Não há critério", "valor": 1},
                    {"texto": "Baseada apenas em percepção", "valor": 2},
                    {"texto": "Baseada parcialmente em análise", "valor": 3},
                    {"texto": "Baseada em dados e estratégia", "valor": 4}
                ]
            },
            {
                "id": "concor_q9",
                "pergunta": "A empresa acompanha sistematicamente as ações e estratégias dos concorrentes?",
                "opcoes": [
                    {"texto": "Não acompanha", "valor": 1},
                    {"texto": "Observa informalmente", "valor": 2},
                    {"texto": "Acompanha ocasionalmente", "valor": 3},
                    {"texto": "Analisa de forma estruturada", "valor": 4}
                ]
            },
            {
                "id": "concor_q10",
                "pergunta": "A empresa possui posicionamento claro no mercado (preço, qualidade, nicho, especialização)?",
                "opcoes": [
                    {"texto": "Não possui posicionamento claro", "valor": 1},
                    {"texto": "Posicionamento confuso", "valor": 2},
                    {"texto": "Posicionamento razoavelmente definido", "valor": 3},
                    {"texto": "Posicionamento claro e consistente", "valor": 4}
                ]
            },
            {
                "id": "concor_q11",
                "pergunta": "Existe plano estruturado para crescimento, fortalecimento ou expansão?",
                "opcoes": [
                    {"texto": "Não existe plano", "valor": 1},
                    {"texto": "Existe intenção, mas sem estrutura", "valor": 2},
                    {"texto": "Existe plano parcial", "valor": 3},
                    {"texto": "Existe plano estruturado", "valor": 4}
                ]
            },
            {
                "id": "concor_q12",
                "pergunta": "A empresa já percebeu perda de clientes ou mercado para concorrentes?",
                "opcoes": [
                    {"texto": "Sim, frequentemente", "valor": 1},
                    {"texto": "Algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            }
        ]
    },
    "Tecnologia e Inovação": {
        "abreviacao": "Tecnologia e Inovação",
        "perguntas": [
            {
                "id": "tecno_q1",
                "pergunta": "Existem processos importantes que ainda são realizados manualmente e poderiam ser digitalizados?",
                "opcoes": [
                    {"texto": "A maioria é manual", "valor": 1},
                    {"texto": "Muitos processos são manuais", "valor": 2},
                    {"texto": "Alguns processos ainda são manuais", "valor": 3},
                    {"texto": "A maior parte já está digitalizada", "valor": 4}
                ]
            },
            {
                "id": "tecno_q2",
                "pergunta": "A empresa utiliza ferramentas ou softwares para automatizar tarefas operacionais?",
                "opcoes": [
                    {"texto": "Não utiliza", "valor": 1},
                    {"texto": "Utiliza muito pouco", "valor": 2},
                    {"texto": "Utiliza parcialmente", "valor": 3},
                    {"texto": "Utiliza de forma estruturada", "valor": 4}
                ]
            },
            {
                "id": "tecno_q3",
                "pergunta": "Os sistemas utilizados (vendas, estoque, financeiro, atendimento) são integrados?",
                "opcoes": [
                    {"texto": "Não existem sistemas ou são totalmente separados", "valor": 1},
                    {"texto": "Existem sistemas, mas sem integração", "valor": 2},
                    {"texto": "Integração parcial", "valor": 3},
                    {"texto": "Sistemas integrados", "valor": 4}
                ]
            },
            {
                "id": "tecno_q4",
                "pergunta": "A operação depende excessivamente de conhecimento individual (se alguém sair, o processo para)?",
                "opcoes": [
                    {"texto": "Sim, totalmente dependente", "valor": 1},
                    {"texto": "Alta dependência", "valor": 2},
                    {"texto": "Dependência moderada", "valor": 3},
                    {"texto": "Processos estruturados e documentados", "valor": 4}
                ]
            },
            {
                "id": "tecno_q5",
                "pergunta": "A falta de tecnologia já gerou retrabalho, erros ou atrasos na operação?",
                "opcoes": [
                    {"texto": "Sim, frequentemente", "valor": 1},
                    {"texto": "Algumas vezes", "valor": 2},
                    {"texto": "Raramente", "valor": 3},
                    {"texto": "Não", "valor": 4}
                ]
            },
            {
                "id": "tecno_q6",
                "pergunta": "A empresa utiliza indicadores (KPIs) para acompanhar desempenho?",
                "opcoes": [
                    {"texto": "Não utiliza indicadores", "valor": 1},
                    {"texto": "Utiliza poucos indicadores", "valor": 2},
                    {"texto": "Utiliza alguns indicadores regularmente", "valor": 3},
                    {"texto": "Utiliza indicadores estratégicos para decisões", "valor": 4}
                ]
            },
            {
                "id": "tecno_q7",
                "pergunta": "As decisões estratégicas são baseadas em análise de dados?",
                "opcoes": [
                    {"texto": "Baseadas apenas em percepção", "valor": 1},
                    {"texto": "Mais percepção do que dados", "valor": 2},
                    {"texto": "Combinação de dados e percepção", "valor": 3},
                    {"texto": "Baseadas majoritariamente em dados", "valor": 4}
                ]
            },
            {
                "id": "tecno_q8",
                "pergunta": "Os dados da empresa estão organizados e acessíveis para análise?",
                "opcoes": [
                    {"texto": "Não estão organizados", "valor": 1},
                    {"texto": "Organização limitada", "valor": 2},
                    {"texto": "Organização razoável", "valor": 3},
                    {"texto": "Organizados e facilmente acessíveis", "valor": 4}
                ]
            },
            {
                "id": "tecno_q9",
                "pergunta": "A empresa gera relatórios periódicos para avaliar desempenho?",
                "opcoes": [
                    {"texto": "Não gera relatórios", "valor": 1},
                    {"texto": "Gera esporadicamente", "valor": 2},
                    {"texto": "Gera regularmente, mas pouco analisa", "valor": 3},
                    {"texto": "Gera e utiliza para planos de ação", "valor": 4}
                ]
            },
            {
                "id": "tecno_q10",
                "pergunta": "A empresa utiliza ou testa ferramentas de Inteligência Artificial para melhorar processos ou decisões?",
                "opcoes": [
                    {"texto": "Não conhece nem utiliza", "valor": 1},
                    {"texto": "Conhece, mas não utiliza", "valor": 2},
                    {"texto": "Utiliza de forma experimental", "valor": 3},
                    {"texto": "Utiliza de forma estratégica", "valor": 4}
                ]
            },
            {
                "id": "tecno_q11",
                "pergunta": "A empresa já avaliou sua vulnerabilidade a vazamentos ou ataques digitais?",
                "opcoes": [
                    {"texto": "Nunca avaliou", "valor": 1},
                    {"texto": "Já considerou, mas não tomou medidas", "valor": 2},
                    {"texto": "Possui medidas básicas", "valor": 3},
                    {"texto": "Possui estratégia estruturada de segurança digital", "valor": 4}
                ]
            }
        ]
    },
    "Comercial e Marketing": {
        "abreviacao": "Comercial e Marketing",
        "perguntas": [
            {
                "id": "mkt_q1",
                "pergunta": "A empresa possui processo estruturado de vendas (captação, abordagem, negociação e fechamento)?",
                "opcoes": [
                    {"texto": "Não possui processo definido", "valor": 1},
                    {"texto": "Processo informal", "valor": 2},
                    {"texto": "Processo parcialmente estruturado", "valor": 3},
                    {"texto": "Processo estruturado e acompanhado", "valor": 4}
                ]
            },
            {
                "id": "mkt_q2",
                "pergunta": "A empresa acompanha a taxa de conversão de vendas e considera o resultado satisfatório?",
                "opcoes": [
                    {"texto": "Não acompanha e a conversão é baixa", "valor": 1},
                    {"texto": "Não acompanha com clareza ou a conversão está abaixo do esperado", "valor": 2},
                    {"texto": "Acompanha e a conversão é razoável", "valor": 3},
                    {"texto": "Acompanha com indicadores claros e a conversão é considerada boa", "valor": 4}
                ]
            },
            {
                "id": "mkt_q3",
                "pergunta": "Existe estratégia estruturada de geração de leads (campanhas, formulários, landing pages, parcerias)?",
                "opcoes": [
                    {"texto": "Não existe estratégia", "valor": 1},
                    {"texto": "Existe informalmente", "valor": 2},
                    {"texto": "Existe parcialmente estruturada", "valor": 3},
                    {"texto": "Existe estratégia clara e contínua", "valor": 4}
                ]
            },
            {
                "id": "mkt_q4",
                "pergunta": "As ações de captação de leads têm gerado volume suficiente de oportunidades para sustentar as metas de vendas?",
                "opcoes": [
                    {"texto": "Não geram leads suficientes", "valor": 1},
                    {"texto": "Geram abaixo do necessário", "valor": 2},
                    {"texto": "Geram volume razoável", "valor": 3},
                    {"texto": "Geram volume consistente e previsível", "valor": 4}
                ]
            },
            {
                "id": "mkt_q5",
                "pergunta": "Existe critério para qualificar clientes antes da abordagem comercial?",
                "opcoes": [
                    {"texto": "Não existe critério", "valor": 1},
                    {"texto": "Existe informalmente", "valor": 2},
                    {"texto": "Existe parcialmente estruturado", "valor": 3},
                    {"texto": "Existe processo claro de qualificação", "valor": 4}
                ]
            },
            {
                "id": "mkt_q6",
                "pergunta": "A empresa possui canais digitais estruturados para venda (site, e-commerce ou marketplace)?",
                "opcoes": [
                    {"texto": "N/A - Não se aplica", "valor": 0},
                    {"texto": "Não possui", "valor": 1},
                    {"texto": "Possui, mas sem estratégia", "valor": 2},
                    {"texto": "Possui com alguma organização", "valor": 3},
                    {"texto": "Possui estrutura organizada e estratégica", "valor": 4}
                ]
            },
            {
                "id": "mkt_q7",
                "pergunta": "A empresa acompanha o retorno e desempenho das vendas online?",
                "opcoes": [
                    {"texto": "N/A - Não se aplica", "valor": 0},
                    {"texto": "Não acompanha", "valor": 1},
                    {"texto": "Acompanha informalmente", "valor": 2},
                    {"texto": "Acompanha parcialmente", "valor": 3},
                    {"texto": "Acompanha com indicadores claros", "valor": 4}
                ]
            },
            {
                "id": "mkt_q8",
                "pergunta": "A experiência de compra online é simples, rápida e intuitiva?",
                "opcoes": [
                    {"texto": "N/A - Não se aplica", "valor": 0},
                    {"texto": "Processo confuso e com barreiras", "valor": 1},
                    {"texto": "Apresenta dificuldades", "valor": 2},
                    {"texto": "Funciona razoavelmente bem", "valor": 3},
                    {"texto": "É otimizada e facilita conversão", "valor": 4}
                ]
            },
            {
                "id": "mkt_q9",
                "pergunta": "A empresa depende excessivamente de um único canal de vendas?",
                "opcoes": [
                    {"texto": "N/A - Não se aplica", "valor": 0},
                    {"texto": "Sim, totalmente dependente", "valor": 1},
                    {"texto": "Alta dependência", "valor": 2},
                    {"texto": "Dependência moderada", "valor": 3},
                    {"texto": "Canais diversificados e equilibrados", "valor": 4}
                ]
            },
            {
                "id": "mkt_q10",
                "pergunta": "Existe planejamento estruturado de marketing com metas e calendário?",
                "opcoes": [
                    {"texto": "Não existe planejamento", "valor": 1},
                    {"texto": "Planejamento informal", "valor": 2},
                    {"texto": "Planejamento parcial", "valor": 3},
                    {"texto": "Planejamento estruturado", "valor": 4}
                ]
            },
            {
                "id": "mkt_q11",
                "pergunta": "O conteúdo nas redes sociais é produzido com objetivo estratégico (atração, relacionamento ou venda)?",
                "opcoes": [
                    {"texto": "Conteúdo sem estratégia", "valor": 1},
                    {"texto": "Conteúdo esporádico", "valor": 2},
                    {"texto": "Conteúdo com algum planejamento", "valor": 3},
                    {"texto": "Conteúdo estratégico com objetivo definido", "valor": 4}
                ]
            },
            {
                "id": "mkt_q12",
                "pergunta": "A empresa analisa métricas de engajamento e ajusta estratégias com base nos resultados?",
                "opcoes": [
                    {"texto": "Não analisa métricas", "valor": 1},
                    {"texto": "Analisa raramente", "valor": 2},
                    {"texto": "Analisa parcialmente", "valor": 3},
                    {"texto": "Analisa e ajusta continuamente", "valor": 4}
                ]
            },
            {
                "id": "mkt_q13",
                "pergunta": "A empresa utiliza campanhas pagas (Google Ads, Meta Ads) com estratégia definida?",
                "opcoes": [
                    {"texto": "Não utiliza", "valor": 1},
                    {"texto": "Utiliza sem estratégia clara", "valor": 2},
                    {"texto": "Utiliza parcialmente estruturado", "valor": 3},
                    {"texto": "Utiliza com estratégia e acompanhamento", "valor": 4}
                ]
            },
            {
                "id": "mkt_q14",
                "pergunta": "A empresa trabalha posicionamento digital (SEO, presença no Google, reputação online)?",
                "opcoes": [
                    {"texto": "Não trabalha", "valor": 1},
                    {"texto": "Trabalha informalmente", "valor": 2},
                    {"texto": "Trabalha parcialmente", "valor": 3},
                    {"texto": "Trabalha de forma estratégica", "valor": 4}
                ]
            },
            {
                "id": "mkt_q15",
                "pergunta": "O cliente entende claramente a proposta de valor da marca nos canais digitais?",
                "opcoes": [
                    {"texto": "Não entende", "valor": 1},
                    {"texto": "Entende parcialmente", "valor": 2},
                    {"texto": "Entende na maioria dos casos", "valor": 3},
                    {"texto": "Entende claramente e de forma consistente", "valor": 4}
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
LISTA_DIRECIONAMENTO = ["Eventos e Programas", "Portifólio de Soluções", "Trilha do Conhecimento", "Diagnóstico Completo", "Negociação de Nova Parceria", "Atendimento de construção personalizada]
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
