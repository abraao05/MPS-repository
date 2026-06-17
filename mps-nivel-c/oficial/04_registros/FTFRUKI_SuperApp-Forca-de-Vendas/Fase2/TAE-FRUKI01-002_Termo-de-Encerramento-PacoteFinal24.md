# Termo de Encerramento e Aceite do Projeto — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | TAE-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Cliente** | Fruki Bebidas S.A. |
| **Versão** | 1.1 |
| **Data de encerramento** | 15/01/2026 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Resumo do projeto

O Pacote Final 24 do SuperApp Fruki entregou três módulos que fecharam o roadmap 2025 da Fruki Bebidas: Pedidos Não Alocados (rastreabilidade de pedidos sem entrega para o vendedor em campo), Regra de Ouro (visualização detalhada da composição da remuneração variável, anteriormente denominada "caixa preta") e PDV / Rota PDV (formulário digital de pesquisa de execução de ponto de venda com geolocalização e integração à API de Rota PDV).

O projeto foi executado de outubro de 2025 a janeiro de 2026, com kickoff em 09/10/2025, entregas incrementais mensais (Pedidos Não Alocados em out/2025, Regra de Ouro em nov/2025, PDV em dez/2025–jan/2026) e aceite formal via Microsoft Teams em 15/01/2026. O aplicativo foi publicado na Play Store na versão 2.0.

---

## 2. Entregas realizadas

| Entrega | Situação | Referência |
|---|---|---|
| Módulo Pedidos Não Alocados (RF-05 a RF-08) — painel, cards, filtros, mensageria, normalização front-end | Concluída | PR #57 — Azure DevOps Fruki — 25/10/2025 |
| Módulo Regra de Ouro (RF-09 a RF-11) — indicadores, gráficos circulares, pesquisa de SKU | Concluída | PR Regra de Ouro — Azure DevOps Fruki — Nov/2025 |
| Módulo PDV / Rota PDV (RF-12 a RF-14) — formulário digital, geolocalização, API Rota PDV | Concluída | PR PDV — Azure DevOps Fruki — Jan/2026 |
| Build APK de homologação por módulo (distribuído via Expo) | Concluída | Compartilhado com Cecília antes de cada sprint |
| Build AAB v2.0 para publicação na Play Store | Concluída | Entregue em Jan/2026; publicação sob responsabilidade da Fruki |
| Ajustes no Módulo Metas/RV (normalização, correções pós-piloto Pacote 1) | Concluída | Incluído no escopo do Pacote Final 24 |

---

## 3. Escopo: planejado × realizado

Todos os itens previstos no PLA-FRUKI01-002 foram entregues. Houve uma solicitação de mudança de escopo (`CR-FRUKI01-001`) aprovada em 09/10/2025 — antes do início da execução — para inclusão do Módulo Regra de Ouro, que estava fora do escopo original da proposta de 26/09/2025. A mudança foi aprovada sem custo adicional e formalizada no TAP-FRUKI01-002. Não houve novas change requests durante a execução dos sprints.

| Item de escopo | Planejado | Realizado | Observação |
|---|---|---|---|
| RF-05 a RF-14 — três módulos completos | Sim | Sim | |
| Ajustes no Módulo Metas/RV | Sim | Sim | |
| Build APK por módulo (homologação) | Sim | Sim | |
| Build AAB v2.0 (Play Store) | Sim | Sim | |
| APIs (responsabilidade Fruki) | Não incluído | Não aplicável | API Rota PDV recebida com atraso (08/01/2026); gerenciada sem impacto no prazo final |
| Versão iOS | Não incluído | Não aplicável | |

---

## 4. Aceite do cliente

| Cliente / responsável | Aceite | Data | Ref. da ata |
|---|---|---|---|
| Leandro Lottermann (Coordenador de Sistemas — Fruki) | Aprovado | 15/01/2026 | ATA-FRUKI01-003 — reunião Microsoft Teams |
| Cecília Ribeiro (Analista Digital — Fruki) | Validado | 15/01/2026 | ATA-FRUKI01-003 — reunião Microsoft Teams |

---

## 5. Transição / sustentação

O código dos três módulos foi entregue via Pull Requests revisadas e mergeadas por Jardel Dargas Silva no repositório Azure DevOps da Fruki. O build AAB v2.0 foi entregue para publicação na Play Store pelo time Fruki. Toda a infraestrutura (repositório, APIs, Play Store) permanece sob custódia da Fruki. A Timeware não mantém ambiente de sustentação ativo — novas demandas seguem nova proposta comercial.

---

## 6. Lições aprendidas

| Tema | O que ocorreu | Lição / recomendação |
|---|---|---|
| Atraso na disponibilização de API | A API de Rota PDV foi disponibilizada por Jardel apenas em 08/01/2026 (Sprint 3), com ~1 semana de atraso em relação ao prazo acordado | Incluir no plano de projeto uma cláusula formal de pré-requisito de API com data de comprometimento assinada pelo cliente; desenvolver a interface (tela) antes da integração real para minimizar impacto de atraso |
| Entrega incremental funciona bem | A cadência de um módulo por mês permitiu validação antecipada com o cliente e redução do risco de retrabalho | Manter o modelo de entrega incremental mensal para projetos mobile de múltiplos módulos; validar protótipo com cliente pelo menos 1 sprint antes do desenvolvimento |
| Renomeação de "Caixa Preta" para "Regra de Ouro" | A nomenclatura interna da Fruki foi substituída por uma mais positiva durante a revisão de protótipos com Cecília (22/10/2025) | Incluir na reunião de levantamento de requisitos uma seção explícita sobre nomenclatura de UI — evitar assumir que nomes internos são adequados para a interface do usuário |
| Formulário PDV com perguntas confirmadas tardiamente | A lista completa de perguntas do formulário de PDV foi recebida de Alexsandro apenas em 04/12/2025, no início da Sprint 3 | Obter a lista completa de perguntas antes do kickoff da sprint de desenvolvimento; incluir como pré-requisito formal no plano de projeto |
| Piloto de Rota PDV com dados reais funcionou sem defeitos | Após integração com a API recebida em 08/01/2026, os testes com dados reais não revelaram defeitos | A decisão de desenvolver a interface antes da integração real (usando mock) foi acertada — permitiu validar UX antecipadamente e acelerar a integração |

---

## Registro de encerramento

| Evento | Data | Ref. |
|---|---|---|
| Kickoff e aprovação da proposta | 09/10/2025 | ATA-FRUKI01-001 (Kickoff) — Fireflies ID: HWwWGbMe3glWfXgl |
| PR #57 — entrega Módulo Pedidos Não Alocados | 25/10/2025 | Azure DevOps Fruki |
| Entrega Módulo Regra de Ouro | Nov/2025 | Azure DevOps Fruki |
| Recebimento API Rota PDV de Jardel | 08/01/2026 | E-mail / WhatsApp Jardel |
| Aceite formal via Microsoft Teams | 15/01/2026 | ATA-FRUKI01-003 |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/01/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado out/2025–jan/2026) |
| 1.1 | 05/06/2026 | Abraão Oliveira | §3 corrigido: referência à CR-FRUKI01-001 (mudança de escopo aprovada em 09/10/2025 antes do início da execução) |
