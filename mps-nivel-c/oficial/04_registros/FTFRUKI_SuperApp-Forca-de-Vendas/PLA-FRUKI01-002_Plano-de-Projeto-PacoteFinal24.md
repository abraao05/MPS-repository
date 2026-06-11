# Plano de Projeto — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | PLA-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Cliente** | Fruki Bebidas S.A. |
| **Contrato** | Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Desenvolver três novos módulos no SuperApp Fruki (React Native / Expo) como continuação do Pacote 1: Pedidos Não Alocados, Regra de Ouro (Caixa Preta) e PDV / Rota PDV. O resultado fecha o roadmap 2025 da Fruki com entregas incrementais mensais e encerramento formal em janeiro de 2026.

Detalhamento de escopo: ver `REQ-FRUKI01-002_Documento-de-Requisitos.md`.

## 2. Escopo (GPR 1)

- **Incluído:** RF-05 a RF-14 conforme REQ-FRUKI01-002 — Módulo Pedidos Não Alocados (painel, cards, filtros, mensageria); Módulo Regra de Ouro (gráficos, indicadores por SKU/família, pesquisa); Módulo PDV (formulário digital, geolocalização, integração API Rota PDV); ajustes no módulo Metas/RV; builds APK/AAB versão 2.0.
- **Não incluído:** Desenvolvimento de APIs (responsabilidade Fruki); módulos fora do roadmap do Pacote Final 24; versão iOS.

## 3. Adaptação do processo (GPR 2)

Detalhamento completo em `ADAP-FRUKI01-002_Registro-de-Adaptacao.md`. Resumo:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Design UX/UI | Aplicável — com UX/UI | Três novos módulos com interface mobile; protótipos validados por Cecília antes de cada sprint |
| Origem dos requisitos e design | Timeware elabora, cliente valida | Brenda conduz design; Cecília e Alexsandro validam regras de negócio de cada módulo |
| Porte do projeto | Médio | Três módulos em ~3 meses; equipe de 5 pessoas |
| Combinação de papéis | Abraão: GP + PO; Brenda: UX + analista | Mesma configuração do Pacote 1; equipe enxuta |
| Cadência de entrega | Por módulo — entrega incremental mensal | Pedidos Não Alocados (out); Regra de Ouro (nov); PDV (dez/jan) |
| Ambiente de stage | Expo APK + branch feature no Azure DevOps | Builds de teste antes de cada merge; link Expo compartilhado com cliente para validação |

## 4. Estimativas (GPR 3, 4)

- **Tamanho estimado:** ~75 story points

| Módulo / Feature | Complexidade | Story Points |
|---|---|---|
| RF-05 a RF-08 — Pedidos Não Alocados (painel, cards, filtros, mensageria) | Alta | 21 |
| RF-09 a RF-11 — Regra de Ouro (gráficos, indicadores, pesquisa de SKU) | Alta | 21 |
| RF-12 a RF-14 — PDV (formulário, geolocalização, API Rota PDV) | Alta | 21 |
| Ajustes Metas/RV (normalização front-end, correções) | Baixa | 5 |
| Builds APK/AAB, versionamento 2.0, pull requests | Baixa | 5 |
| Documentação e aceite | — | 2 |
| **Total** | | **~75 SP** |

- **Velocity de referência:** ~25 SP/sprint (equipe de 2 devs front-end + 1 UX; sprints de 2 semanas; velocidade observada no Pacote 1)
- **Esforço/prazo estimado:** ~3 sprints / 3 meses (out/2025 – jan/2026)
- **Base histórica:** Velocity observada no Pacote 1 (Metas/RV) do próprio SuperApp Fruki

## 5. Cronograma e marcos (GPR 5)

| Marco | Data prevista / realizada |
|---|---|
| Apresentação da proposta ao cliente | 26/09/2025 |
| Kickoff formal / aprovação da proposta | 09/10/2025 |
| Sprint 1 — Pedidos Não Alocados | Out/2025 |
| Entrega PR #57 — Módulo Pedidos Não Alocados | 25/10/2025 |
| Sprint 2 — Regra de Ouro (Caixa Preta) | Nov/2025 |
| Alinhamento técnico e PDV | 02/12/2025 e 04/12/2025 |
| Sprint 3 — PDV / Rota PDV | Dez/2025 |
| Status report parcial | 27/12/2025 |
| Entrega final e aceite via Microsoft Teams | 15/01/2026 |

**Detalhamento por sprint:**

*Sprint 1 (out/2025) — Pedidos Não Alocados:*
- Levantamento de requisitos com Cecília (regras de não alocação, filtros, mensageria)
- Protótipo e validação com cliente
- Desenvolvimento: painel, cards (nome fantasia, localização, número do pedido), filtros por data e cliente
- Normalização de dados de pedidos não alocados no front-end
- Entrega via PR #57 no Azure DevOps

*Sprint 2 (nov/2025) — Regra de Ouro:*
- Levantamento das regras de composição de RV por perfil (Cecília)
- Prototipagem e validação (reuniões 22/10 e 13/11)
- Desenvolvimento: tela da Regra de Ouro com gráficos circulares, indicadores por SKU/família, pesquisa de SKU
- Integração com API da Regra de Ouro (Jardel)

*Sprint 3 (dez/2025 – jan/2026) — PDV / Rota PDV:*
- Levantamento do formulário de PDV com Alexsandro (Alinhamento PDV 04/12/2025)
- Desenvolvimento: formulário digital de pesquisa de PDV com geolocalização
- Integração com API Rota PDV (recebida de Jardel em 08/01/2026)
- Geração de AAB para Play Store; versionamento 2.0
- Aceite final via Microsoft Teams — 15/01/2026

## 6. Recursos (GPR 6, 7)

**Equipe:**

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto / Product Owner | Abraão Oliveira | Parcial (gestão, alinhamentos com cliente) |
| COO / Apoio Comercial | Tiago Nascimento | Parcial (reuniões e financeiro) |
| UX/UI Designer / Analista de Negócio | Brenda Chrystie | Parcial (protótipos, levantamento de regras) |
| Desenvolvedor Front-End React Native | Luca Watson | Integral (desenvolvimento) |
| Desenvolvedor Front-End React Native | Thiago Gomes | Integral (desenvolvimento) |
| GQA | COO (Operações) | Parcial (auditorias de processo) |

**Ambiente e ferramentas:**

| Ferramenta / Ambiente | Uso |
|---|---|
| React Native / Expo | Framework do aplicativo mobile |
| Azure DevOps (Fruki) | Repositório — `https://dev.azure.com/fruki/superapp/_git/fruki-app.git` |
| APIs REST Fruki (`https://api.fruki.com.br/comercial/v1/`) | Pedidos não alocados, Rota PDV |
| Expo APK / AAB | Builds de teste e publicação Play Store |
| Google Meet | Reuniões quinzenais de alinhamento de negócio e backlog |
| Microsoft Teams | Reunião de aceite final (15/01/2026) |
| WhatsApp (grupo do projeto) | Comunicação ágil de alinhamentos técnicos |
| E-mail corporativo | Comunicações formais, status reports |

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Leandro Lottermann (Fruki) | Aprovação e aceite formal de entregas | E-mail formal de status; presença no aceite final (Teams 15/01/2026) |
| Cecília Ribeiro (Fruki) | Validação de negócio, protótipos e regras de RV | Reuniões quinzenais recorrentes (quarta 15h) |
| Jardel Dargas Silva (Fruki) | Integração técnica das APIs | Reuniões técnicas ad hoc; e-mail e WhatsApp |
| Alexsandro de Vargas Braga (Fruki) | Requisitos do formulário de PDV | Reunião específica para levantamento (ago/2025) e alinhamento PDV (dez/2025) |
| Brenda Chrystie (Timeware) | Design e validação de UX | Daily interno; revisão de protótipos |
| Luca Watson / Thiago Gomes (Timeware) | Desenvolvimento | Daily interno; alinhamento técnico com Jardel |

## 8. Transição (GPR 8)

Código entregue via Pull Request ao repositório Azure DevOps da Fruki, revisado e mergeado por Jardel. AAB entregue para publicação na Play Store (versão 2.0). Toda a infraestrutura permanece no Azure da Fruki. Pós-encerramento do Pacote Final 24, novas demandas seguem nova proposta comercial.

## 9. Riscos (GPR 10)

| # | Risco | Prob. | Impacto | Resposta |
|---|---|---|---|---|
| R-01 | APIs da Fruki não disponibilizadas no prazo, bloqueando o desenvolvimento | 3 | 3 | Trabalhar com mock de dados; solicitar prazo formal no início de cada sprint; escalar via Leandro |
| R-02 | Atraso na validação de protótipos por Cecília | 2 | 2 | Enviar protótipos com 1 semana de antecedência; reuniões quinzenais mantidas |
| R-03 | Mudança de escopo durante a sprint | 2 | 2 | Registrar via e-mail; avaliar impacto no prazo antes de aceitar |
| R-04 | Problema de agenda para aceite final (Teams 15/01/2026) | 2 | 2 | Agendar sessão de aceite com antecedência mínima de 2 semanas |

## 10. Viabilidade (GPR 11)

Viável dentro do escopo e prazo: equipe com familiaridade na base de código do SuperApp Fruki (Pacote 1); APIs a serem fornecidas pela Fruki com interlocutores identificados e engajados; três módulos bem delimitados com entregas mensais. Principal risco é a dependência da disponibilização das APIs pelo time Fruki.

## 11. Aprovação do Plano (GPR 13)

Plano apresentado e aprovado na reunião de Kickoff do Pacote Final 24 em 09/10/2025. O aceite foi registrado na ata da reunião (ATA-FRUKI01-008). A partir deste ponto, o plano constitui a baseline do Pacote Final 24 e mudanças de escopo seguem o fluxo de change request.

| Envolvido | Papel | Aceite | Data | Ref. da ata |
|---|---|---|---|---|
| Leandro Lottermann | Coordenador de Sistemas / Gestor — Fruki | Aprovado | 09/10/2025 | ATA-FRUKI01-008 — Ata de Kickoff e Aprovação do Plano (09/10/2025) |
| Abraão Oliveira | Gerente de Projeto — Timeware | Confirmado | 09/10/2025 | ATA-FRUKI01-008 — Ata de Kickoff e Aprovação do Plano (09/10/2025) |

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado out/2025–jan/2026) |
| 1.1 | 05/06/2026 | Abraão Oliveira | §11 corrigido: aprovação do plano referenciada em ATA-FRUKI01-008 (ata de kickoff e aprovação do plano) em vez de e-mail |
