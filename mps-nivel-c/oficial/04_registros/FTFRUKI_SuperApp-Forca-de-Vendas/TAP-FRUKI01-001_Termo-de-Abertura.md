# Termo de Abertura do Projeto — SuperApp Fruki · Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | TAP-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Novas Features Força de Vendas |
| **Cliente** | Fruki Bebidas S.A. |
| **Contrato** | Pacote Final 24 |
| **Versão** | 1.0 |
| **Data de abertura** | 05/06/2024 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Objetivo do projeto

Desenvolver novas funcionalidades no SuperApp Fruki — aplicativo mobile de força de vendas da Fruki Bebidas, utilizado pela equipe comercial de campo. O projeto compreende a evolução incremental do aplicativo com módulos de Metas e Remuneração Variável (RV), Pedidos Não Alocados, Regra de Ouro (Caixa Preta), PDV (Ponto de Venda) e Rota PDV, entregando ao time de vendas maior visibilidade de indicadores, melhoria no acompanhamento de performance e rastreabilidade de pedidos em campo.

## 2. Escopo macro

Conforme proposta comercial "Pacote Final 24" aprovada pelo cliente em setembro/outubro de 2024, complementada pelo levantamento de demandas realizado entre junho e setembro de 2024.

- **Incluído:**
  - Módulo de Metas e Remuneração Variável (RV): indicadores de volume, cobertura, drop size, positivação e regra de ouro por perfil de vendedor
  - Módulo de Pedidos Não Alocados: painel de acompanhamento com cards por cliente, filtros por data e geolocalização, mensageria de não alocados
  - Módulo Regra de Ouro (Caixa Preta): visualização dos indicadores de composição de meta de RV por perfil de vendedor
  - Módulo PDV (Ponto de Venda): pesquisa de execução de PDV com geolocalização, formulário de perguntas e integração com API Rota PDV
  - Integração com APIs fornecidas pela equipe de desenvolvimento da Fruki (Azure DevOps)
  - Entrega de APKs para testes e produção via Expo/Play Store

- **Não incluído:**
  - Desenvolvimento de APIs de negócio (responsabilidade da equipe Fruki — Jardel e Renan)
  - Gestão de infraestrutura Azure do cliente
  - Módulos fora do roadmap acordado no Pacote Final 24
  - Desenvolvimento de versão iOS (foco em Android para o piloto)

## 3. Partes interessadas

| Parte interessada | Papel | Contato |
|---|---|---|
| Leandro Lottermann | Coordenador de Sistemas / Gestor do Contrato — Fruki | leandro_lottermann@fruki.com.br |
| Cecília Ribeiro | Analista Digital / Product Owner do cliente — Fruki | cecilia_ribeiro@fruki.com.br |
| Jardel Dargas Silva | Desenvolvedor Jr / Responsável pelas APIs — Fruki | jardel_silva@fruki.com.br |
| Renan Gustavo da Silva | Desenvolvedor / Suporte às APIs — Fruki | renan_silva@fruki.com.br |
| Alexsandro de Vargas Braga | Responsável comercial pelo módulo PDV — Fruki | alexsandro_braga@fruki.com.br |

## 4. Equipe do projeto

| Papel | Responsável |
|---|---|
| Gerente de Projeto / Product Owner | Abraão Oliveira |
| COO / Gestão Comercial | Tiago Nascimento |
| UX/UI Designer / Product Designer | Brenda Chrystie |
| Desenvolvedor Front-End (React Native) | Luca Watson |
| Desenvolvedor Front-End (React Native) | Thiago Gomes |
| Responsável por Medição | Abraão Oliveira |

## 5. Macroplanejamento (datas-alvo)

| Marco | Data-alvo |
|---|---|
| Proposta comercial inicial / Kickoff | 05/06/2024 |
| Levantamento demanda Metas (1ª reunião formal) | 25/06/2024 |
| Início do desenvolvimento — Módulo Metas/RV | Jul/2024 |
| Acompanhamento e piloto — Módulo Metas/RV | 05/08/2024 |
| Entendimento novas demandas (Não Alocados) | 19/09/2024 |
| Apresentação e aprovação Proposta Pacote Final 24 | 26/09/2024 |
| Kickoff Pacote Final 24 / Entendimento Caixa Preta | 09/10/2024 |
| Entrega Módulo Pedidos Não Alocados | 25/10/2024 |
| Desenvolvimento Módulo Regra de Ouro / PDV | Nov–Dez/2024 |
| Entrega final e aceite | 15/01/2025 |

## 6. Agenda das próximas atividades

- Reuniões quinzenais de alinhamento de negócio e backlog (Timeware e Fruki — recorrentes)
- Reuniões técnicas de alinhamento com Jardel (desenvolvimento e integração de APIs)
- Entregas incrementais a cada mês conforme roadmap do Pacote Final 24
- Validação de protótipos de UX com Cecília Ribeiro antes de cada sprint de desenvolvimento
- Emissão de Nota Fiscal conforme marcos de entrega (1/3 por entrega)
- Visita técnica presencial ao cliente (RS) para aceite final — prevista 15/01/2025

## 7. Premissas e restrições iniciais

**Premissas:**
- A Fruki disponibiliza acesso ao repositório Azure DevOps (https://dev.azure.com/fruki/superapp/_git/fruki-app.git) e às APIs documentadas (Swagger)
- As APIs são desenvolvidas e mantidas pelo time de TI da Fruki (Jardel e Renan), com prazos alinhados ao cronograma de entrega da Timeware
- Cecília Ribeiro atua como ponto focal de negócio, validando protótipos e regras de RV antes do desenvolvimento
- O Leandro Lottermann é a autoridade de aprovação contratual e de aceite formal das entregas
- O orçamento disponível para o Pacote Final 24 é de R$55.000 até o final de 2024

**Restrições:**
- Prazo máximo para entrega do Pacote Final 24: 15/01/2025
- Dependência crítica das APIs da Fruki: atrasos na disponibilização das APIs impactam diretamente o cronograma de desenvolvimento front-end
- O desenvolvimento é restrito ao ambiente React Native / Expo conforme arquitetura existente do SuperApp
- Mudanças de escopo fora do Pacote Final 24 requerem nova proposta comercial

---

## Registro de abertura

| Reunião de kickoff realizada em | Ref. da autorização |
|---|---|
| 05/06/2024 | Reunião "Proposta Comercial - Fruki <> Timeware" — Fireflies ID: IhH8wQEDaiMe4o4b |
| 25/06/2024 | Reunião "Levantamento demanda Metas" — Fireflies ID: mo3xiqhyv46qvkkb |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — abertura retroativa do projeto (projeto executado jun/2024–jan/2025) |
