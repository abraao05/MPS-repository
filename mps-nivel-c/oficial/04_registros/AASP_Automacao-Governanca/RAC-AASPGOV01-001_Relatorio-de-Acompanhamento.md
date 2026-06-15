# Relatório de Acompanhamento (Status Report) — AASP_GOV · SensrJiraSync

| Campo | Valor |
|---|---|
| **Projeto** | AASP_GOV — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Período de referência** | Sprints 1 e 2 · 27/04/2026 – 22/05/2026 |
| **Data do relatório** | 25/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Destinatários** | Marcos Correa Fernandez Turnes (Sponsor — AASP); Patrocinador interno (Timeware) |

---

## 1. Situação geral

Desenvolvimento dos serviços concluído (Sprint 1 + Sprint 2). Projeto entra na Sprint 3 — Homologação e Hardening — com encerramento previsto para 02/06/2026, dentro do prazo do TAP.

| Dimensão | Status | Comentário |
|---|---|---|
| **Prazo** | 🟢 No prazo | Sprints 1 e 2 entregues nas datas planejadas; Sprint 3 inicia em 25/05 conforme cronograma |
| **Escopo** | 🟢 Estável | 11 RF + 6 RNF mantidos desde o Kickoff; sem CR aprovado até o momento |
| **Risco** | 🟢 Sob controle | 6 riscos identificados, todos mitigados (R-04 e R-06 com mitigações já implementadas no design) |
| **Qualidade** | 🟢 Dentro do esperado | Testes unitários do StatusMapper, HtmlHelper e SanitizeLabel aprovados; homologação E2E inicia na Sprint 3 |

> *Convenção de cores:* 🟢 sem ação necessária · 🟡 sob acompanhamento, ação em curso · 🔴 exige decisão/atenção do cliente.

## 2. Resumo do período

Nas Sprints 1 e 2 (27/04 a 22/05), o time entregou o núcleo do serviço SensrJiraSync: criação automática de Epics, Tasks e Subtasks no Jira (Sprint 1), sincronização incremental de status, conversão HTML→ADF, sanitização de labels, mapeamento de status (Sprint 1) e fluxo completo de atualização com idempotência (Sprint 2). O serviço já é executável e produz cards válidos no workspace de teste da AASP. A Sprint 3 entra agora com foco em homologação contra ambiente real e hardening final.

**Indicadores do período (destaque):**

| Indicador | Valor |
|---|---|
| Horas trabalhadas no período | 128 h (Sprint 1: 64 h + Sprint 2: 64 h) |
| SP entregues no período | 32 SP (Sprint 1: 16 SP + Sprint 2: 16 SP) |
| Avanço do projeto (acumulado) | 47 SP de 59 SP — **80%** concluído |
| Sprints concluídas | 3 de 4 (Sprint 0, 1, 2) |

## 3. Entregas realizadas no período

| Entrega | Resultado / valor para o cliente | Situação |
|---|---|---|
| Criação automática de Epics no Jira (RF-02) | Hierarquia de projetos preservada na migração | ✅ Concluído |
| Criação de Tasks com summary `#ID Nome` (RF-03) | Identificação única por atividade migrada | ✅ Concluído |
| Criação de Subtasks vinculadas à Task pai (RF-04) | Sub-hierarquia preservada | ✅ Concluído |
| Conversão HTML → ADF via HtmlHelper + BuildAdfDocument (RF-07) | Conteúdo legível no Jira sem tags visíveis | ✅ Concluído |
| Mapeamento dos 5 status Sensr → Jira (RF-08) | Status consistente entre as plataformas | ✅ Concluído |
| Sanitização de labels (RF-09) | Labels válidos no Jira sem erro de criação | ✅ Concluído |
| Sincronização incremental de status (RF-05) | Status alterado no Sensr reflete no Jira | ✅ Concluído |
| Migração de histórico como comentários (RF-06) | Rastreabilidade temporal preservada | ✅ Concluído |
| Executável Azure Scheduled Job (RF-11) | Pronto para implantação | ✅ Concluído |
| Idempotência via verificação por `#ID` (RNF-01) | Sem duplicatas em execuções repetidas | ✅ Concluído |
| Resiliência por desenvolvedor (RNF-02) | Falha em 1 dev não interrompe demais | ✅ Concluído |
| Log estruturado (RNF-03) | Auditoria de execução habilitada | ✅ Concluído |

## 4. Planejado para o próximo período

| Item / marco | Data prevista | Observação |
|---|---|---|
| Início da Sprint 3 — Homologação | 25/05/2026 | Foco: validação E2E em ambiente real Sensr/Jira |
| Validação dos critérios CA01–CA07 | 25/05 – 29/05/2026 | Caroline Sousa (QA) entra a partir de 21/05 |
| Reunião de validação de homologação | 29/05/2026 | Sponsor + QA + Tech Lead — ATA-AASPGOV01-003 prevista |
| Aceite formal e encerramento | 02/06/2026 | TAE-AASPGOV01-001 + ATA-AASPGOV01-004 |

## 5. Indicadores do projeto (acompanhamento)

| Indicador | Meta / referência | Período atual | Tendência |
|---|---|---|---|
| Aderência ao prazo (M1) | ≤ 5% desvio | 0% (todas as sprints no prazo) | ➡️ |
| Esforço estimado × realizado (M2) | ≤ 10% desvio | +6,7% acumulado (Sprints 0–2: 188 h vs 176 h) | ➡️ |
| Velocity (M3) | ≥ 12 SP/sprint | 15,7 SP/sprint (média das 3 sprints concluídas) | ⬆️ |
| Itens entregues × planejados (M4) | ≥ 95% | 100% (47/47 SP) | ⬆️ |
| Densidade de defeitos (M5) | ≤ 1 def / 4 SP | 0 (homologação ainda não iniciou) | ➡️ |

## 6. Diário de bordo (eventos e impactos)

| Data | Evento / motivo | Origem | Impacto (dias) | Situação |
|---|---|---|---|---|
| 23/04/2026 | Mapeamento da API Jira v3 exigiu investigação adicional sobre o formato ADF | Externo (Atlassian) | +4 h (Sprint 0) | Resolvido — decisão D04 registrada |
| 06/05/2026 | Decisão D04 formalizada — uso de ADF para campos de texto rico | Timeware | 0 | Resolvido (GDE-AASPGOV01-001 / RAD detalhado) |
| 15/05/2026 | Implementação do HtmlHelper concluída — necessária para D05 (conversão HTML) | Timeware | 0 | Resolvido |

## 7. Pontos de atenção, riscos e plano de ação

**Início da homologação em ambiente real** — 🟡 Médio
- **Ponto:** Sprint 3 vai testar pela primeira vez o fluxo completo contra APIs reais do Sensr e do Jira.
- **Risco:** identificação de incompatibilidades não previstas (campos opcionais, status indisponíveis no workspace, paginação em projetos grandes).
- **Ação:** Caroline Sousa (QA) iniciou em 21/05 com foco em rodadas de homologação em workspace de teste; Tech Lead em standby para correções rápidas; janela de 1 semana até a validação formal em 29/05.

**Identificação dos cards por `#ID` no summary** — 🟢 Baixo
- **Ponto:** estratégia depende do summary começar com `#ID` — cards criados manualmente no Jira não terão esse prefixo.
- **Risco:** cards criados fora do serviço não são reconhecidos como migrados (R-01).
- **Ação:** mitigado pela decisão D03 e pelos testes de idempotência (CT-02); orientação aos usuários para não criar cards manualmente nos projetos migrados durante o período de transição.

## 8. Mudanças (change requests)

| ID | Descrição | Abertura | Dias em aberto | Status | Aceite final |
|---|---|---|---|---|---|
| — | Nenhum CR aberto até o momento | — | — | — | — |

## 9. Decisões necessárias

| Decisão necessária | Responsável pela decisão | Prazo desejado |
|---|---|---|
| Confirmação da janela de homologação em ambiente real (workspace de teste AASP) | Marcos Correa Fernandez Turnes (Sponsor — AASP) | 26/05/2026 |
| Aprovação da publicação no Azure Scheduled Job após validação de homologação | Marcos Correa Fernandez Turnes (Sponsor — AASP) | 01/06/2026 |

---

## Cadência de reporte

| Item | Definição |
|---|---|
| **Periodicidade** | Por marco / fase do cronograma (Kickoff, fim de Sprint 2, validação de homologação, aceite final) |
| **Participantes obrigatórios** | Gerente de Projeto (Timeware) + Sponsor (AASP) |
| **Participantes opcionais** | Tech Lead (Timeware); QA (Timeware) na fase de homologação |
| **Canal** | Reunião de alinhamento (videoconferência) + ata registrada (ATA-AASPGOV01-XXX) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 25/05/2026 | Time de Melhoria Contínua | Relatório de acompanhamento do ponto de controle Sprints 1+2 do projeto AASP_GOV, seguindo TPL-GPR-005 v2.1. |
