# Ata de Reunião — Kickoff e Aprovação do Plano · Pacote Final 24 — SuperApp Fruki

| Campo | Valor |
|---|---|
| **Documento** | ATA-FRUKI01-008 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 09/10/2025 |
| **Local / meio** | Videoconferência (Microsoft Teams) |
| **Responsável pela ata** | Abraão Oliveira |
| **Sessões do dia** | "Parceria Fruki ↔ Timeware" (Fireflies: HWwWGbMe3glWfXgl) + "Entendimento Demanda Caixa Preta" (Fireflies: gOI5CeLpUr7VPiyf) |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão Oliveira | Timeware | Gerente de Projeto / Product Owner |
| Tiago Nascimento | Timeware | COO / Apoio Comercial |
| Brenda Chrystie | Timeware | UX/UI Designer / Analista de Negócio |
| Luca Watson | Timeware | Desenvolvedor Front-End (React Native) |
| Thiago Gomes | Timeware | Desenvolvedor Front-End (React Native) |
| Leandro Lottermann | Fruki Bebidas | Coordenador de Sistemas / Gestor do Contrato |
| Cecília Ribeiro | Fruki Bebidas | Analista Digital / Product Owner do cliente |
| Jardel Dargas Silva | Fruki Bebidas | Desenvolvedor Jr / Responsável pelas APIs |

---

## 2. Pauta

1. Apresentação e aprovação formal da proposta "Pacote Final 24"
2. Apresentação do macroplanejamento: sprints mensais, entregas incrementais, marcos e prazo final
3. Alinhamento dos módulos do escopo: Pedidos Não Alocados, Regra de Ouro (Caixa Preta) e PDV
4. Definição de equipe, papéis e canais de comunicação
5. Próximos passos e agenda das próximas atividades

---

## 3. Discussões e definições

### 3.1 Contexto e continuidade

O Pacote Final 24 é a continuidade do Pacote 1 (Módulo Metas/RV, entregue em set/2025). A mesma equipe Timeware e os mesmos interlocutores da Fruki continuam no projeto, o que elimina o tempo de onboarding. A base de código do SuperApp está madura e o padrão de integração com as APIs Fruki já foi estabelecido.

### 3.2 Escopo aprovado

Leandro Lottermann confirmou a aprovação da proposta "Pacote Final 24 v1.1" para desenvolvimento dos três módulos abaixo:

| Módulo | Descrição | Sprint prevista |
|---|---|---|
| Pedidos Não Alocados | Painel de pedidos sem entrega para o representante em campo | Sprint 1 — out/2025 |
| Regra de Ouro (Caixa Preta) | Visualização detalhada da composição da RV por indicador/SKU/família | Sprint 2 — nov/2025 |
| PDV / Rota PDV | Formulário digital de pesquisa de execução de PDV com geolocalização | Sprint 3 — dez/2025–jan/2026 |

Também foram incluídos no escopo ajustes pontuais no Módulo Metas/RV (Pacote 1) e entrega do build AAB v2.0 para a Play Store.

### 3.3 Inclusão do módulo Regra de Ouro

Na sessão "Entendimento Demanda Caixa Preta" (Fireflies: gOI5CeLpUr7VPiyf), Leandro Lottermann solicitou a inclusão do módulo de composição da remuneração variável ("Caixa Preta") no escopo do Pacote Final 24. O módulo não constava da proposta original de 26/09/2025, que previa apenas Pedidos Não Alocados e PDV. Tiago Nascimento e Abraão Oliveira aprovaram a inclusão sem custo adicional, alocando Sprint 2 (novembro) para o módulo. Esta mudança foi formalizada como CR-FRUKI01-001.

### 3.4 Premissas acordadas

- Fruki disponibiliza as APIs de cada módulo com pelo menos 1 semana de antecedência antes de cada sprint
- Cecília Ribeiro valida os protótipos de UX antes do desenvolvimento de cada módulo
- Leandro Lottermann é a autoridade de aprovação e aceite formal das entregas
- Reuniões quinzenais de acompanhamento: toda quarta às 15h (Timeware e Fruki)

### 3.5 Aprovação do Plano de Projeto

O Plano de Projeto PLA-FRUKI01-002 foi apresentado por Abraão Oliveira com escopo, estimativas (75 SP / 3 sprints mensais), marcos e prazo final de 15/01/2026. Leandro Lottermann aprovou o plano, estabelecendo-o como baseline do Pacote Final 24. A partir deste ponto, mudanças de escopo seguem o fluxo de change request.

---

## 4. Decisões e aceites

| Decisão | Responsável | Data |
|---|---|---|
| Aprovação da proposta Pacote Final 24 v1.1 | Leandro Lottermann | 09/10/2025 |
| Aprovação do PLA-FRUKI01-002 como baseline | Leandro Lottermann / Abraão Oliveira | 09/10/2025 |
| Inclusão do módulo Regra de Ouro sem custo adicional (CR-FRUKI01-001) | Leandro Lottermann / Tiago Nascimento / Abraão Oliveira | 09/10/2025 |
| Sprint 2 (nov/2025) alocada para o módulo Regra de Ouro | Abraão Oliveira | 09/10/2025 |
| Reuniões quinzenais de acompanhamento: quarta 15h | Timeware + Fruki | 09/10/2025 |

---

## 5. Ações (follow-up)

| Ação | Responsável | Prazo |
|---|---|---|
| Início do desenvolvimento do Módulo Pedidos Não Alocados (Sprint 1) | Luca Watson / Thiago Gomes | Out/2025 |
| Protótipo do Módulo Pedidos Não Alocados para validação por Cecília | Brenda Chrystie | Out/2025 |
| Envio da API de Pedidos Não Alocados | Jardel Dargas Silva | Antes do início da sprint 1 |
| Agendamento de reunião de levantamento detalhado dos requisitos da Regra de Ouro | Abraão Oliveira | Out/2025 |
| Formalizar CR-FRUKI01-001 (inclusão do módulo Regra de Ouro) | Abraão Oliveira | Out/2025 |

---

## 6. Próximos passos

- Sprint 1 — Pedidos Não Alocados: desenvolvimento e integração em out/2025; entrega PR #57 prevista para 25/10/2025
- Levantamento de regras do módulo Regra de Ouro com Cecília antes do início da Sprint 2
- Protótipo do módulo PDV com Alexsandro de Vargas Braga: nov/2025
- Aceite final via Microsoft Teams: 15/01/2026

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 09/10/2025 | Abraão Oliveira | Versão inicial — registro retroativo (reuniões realizadas em 09/10/2025) |
