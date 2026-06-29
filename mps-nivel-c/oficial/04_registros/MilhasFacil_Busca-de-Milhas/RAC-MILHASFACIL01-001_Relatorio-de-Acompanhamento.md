# Relatório de Acompanhamento — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | RAC-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.2 |
| **Data** | 26/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Tech Lead / Arquiteto / DevOps** | Cézar Velazquez |
| **Processo MPS-SW** | GPR |

---

## 1. Situação geral

Projeto **em andamento e sob controle**: Sprint 10 de 12 dentro da janela do cronograma (09/02–26/07/2026), com a release v0.9.0 promovida a `main` (RF13/RF14/MF-64 entregues) e o único change request do período (CR-MF-001) absorvido sem atraso macro.

| Dimensão | Status | Comentário (1 linha) |
|---|---|---|
| **Prazo** | 🟢 No prazo | Sprint 10 de 12 dentro da janela 09/02–26/07/2026; sem atraso macro |
| **Escopo** | 🟡 Em mudança | CR-MF-001 absorvido na S9 (+10 h, antecipação de RF13 de S10→S9), sem atraso macro |
| **Risco** | 🟢 Sob controle | R-01 e R-02 materializados e tratados (encerrados); R-03 (Z-API) mantido como best-effort com fallback por e-mail |
| **Qualidade** | 🟢 Dentro do esperado | Cobertura JaCoCo 82%+ desde a S5, com gate de CI ≥80% ativo desde a S4; NC-001 encerrada |

> *Convenção de cores:* 🟢 sem ação necessária · 🟡 sob acompanhamento, ação em curso · 🔴 exige decisão/atenção do cliente.

## 2. Objetivo

Monitorar o progresso do projeto MilhasFacil em relação ao plano estabelecido (`PLA-MILHASFACIL01-001`), identificar desvios de prazo, escopo, esforço e qualidade por sprint, e registrar a situação atual. Este relatório consolida os snapshots de acompanhamento das Sprints S1 a S9 e serve como evidência do processo GPR (Gerência de Projeto). A fonte da verdade de gestão é a planilha `GEST-MILHASFACIL01-001`.

---

## 3. Acompanhamento por sprint (S1–S9)

| Sprint | Período | SP plan | SP real | Aderência | Carry | h_est | h_real | Desvio h | Situação |
|---|---|---|---|---|---|---|---|---|---|
| S1 | 09–22/02/2026 | 23 | 20 | 87% | 3 | 40 | 45 | +12% | Concluída |
| S2 | 23/02–08/03/2026 | 40 | 35 | 88% | 5 | 80 | 88 | +10% | Concluída |
| S3 | 09–22/03/2026 | 38 | 34 | 89% | 4 | 76 | 82 | +8% | Concluída |
| S4 | 23/03–05/04/2026 | 45 | 41 | 91% | 4 | 88 | 93 | +6% | Concluída |
| S5 | 06–19/04/2026 | 35 | 33 | 94% | 2 | 76 | 80 | +5% | Concluída |
| S6 | 20/04–03/05/2026 | 33 | 30 | 91% | 3 | 72 | 78 | +9% | Concluída |
| S7 | 04–17/05/2026 | 37 | 30 | 81% | 7 | 70 | 76 | +9% | Concluída |
| S8 | 18–31/05/2026 | 58 | 48 | 83% | 10 | 112 | 124 | +11% | Concluída |
| S9 | 01–14/06/2026 | 69 | 63 | 91% | 6 | 138 | 148 | +7% | Concluída |
| **Total S1–S9** | | **378** | **334** | | **44** | **752** | **814** | **+8,2%** | |

O board do GitLab (board 614) e os burndowns por sprint evidenciam a execução planejada vs. real.

![IMG-JIRA-01 — board 614 e burndown das Sprints S1–S9](evidencias/IMG-JIRA-01_board-burndown.png)

## 4. Medição por sprint (S1–S8)

| Sprint | Velocity | JaCoCo | Karma | pytest | Bugs | NCs |
|---|---|---|---|---|---|---|
| S1 | 20 | 78% | 76% | 80% | 0 | 0 |
| S2 | 35 | 74% | 72% | 78% | 2 | 1 (NC-001 aberta) |
| S3 | 34 | 76% | 75% | 79% | 0 | 1 |
| S4 | 41 | 80% | 78% | 81% | 0 | 1 |
| S5 | 33 | 82% | 80% | 82% | 3 | 0 (NC-001 encerrada) |
| S6 | 30 | 84% | 83% | 83% | 0 | 0 |
| S7 | 30 | 85% | 84% | 83% | 2 | 0 |
| S8 | 48 | 84% | 81% | 83% | 2 | 0 |

Metas: Velocity ≥ 30, Cobertura ≥ 80%, NCs = 0, MRs sem revisor = 0.

## 5. Velocity

A velocity média no ciclo S1–S9 foi de **37,1 SP por sprint**, acima da meta de ≥30 SP. A aderência de SP variou de **81% (S7) a 94% (S5)**, com carry controlado — máximo de **10 SP na S8**. A S9 encerrou com 63 SP reais (91% de aderência), entregando RF13, RF14 e MF-64 na release v0.9.0. A cobertura de testes superou o limiar de 80% de forma sustentada a partir da S4 (gate de CI ativado), com JaCoCo entre 80% e 85% nas Sprints S4–S8. Os pipelines GitLab CI (runner-vm-docker, online) executam nos três repositórios com `.gitlab-ci.yml` presente em `main`/`develop`/`homolog`.

![IMG-CI-01 — pipelines GitLab CI MilhasFacil API/Web/Crawler](evidencias/IMG-CI-01_builds-pipelines.png)

## 6. Marcos e baselines

| Baseline | Sprint | Situação |
|---|---|---|
| v0.1.0 … v0.8.0 | S1 … S8 | Liberadas |
| v0.9.0 | S9 | Released em main (tag nos três repositórios, 15/06/2026) |

Na S9, a baseline foi promovida de develop para main na release **v0.9.0** (develop→homolog→main nos três repositórios, com tag v0.9.0) em 15/06/2026, entregando RF13, RF14 e MF-64 em main.

## 7. Desvios identificados e riscos materializados

| Sprint | Desvio / evento | Referência |
|---|---|---|
| S2 | Cobertura abaixo de 80% (JaCoCo 74%) — NC-001 aberta (risco R-02 materializado) | GQA / NC-001 |
| S2–S4 | Desvio de esforço acima de +6% por sprint; carry acumulado | Planilha §7 |
| S5 | NC-001 encerrada com JaCoCo 82% após priorização de testes e gate de CI (S4+) | GQA / NC-001 |
| S6 | Indisponibilidade de serviços (downtime 3h registrado) — RNF05 | Planilha §6 |
| S8 | Redesign de companhia quebrou o LatamParser (MF-59); corrigido (risco R-01 materializado) | CT-08 |
| S8 | Maior desvio de esforço do ciclo (+11%, h_real 124 vs. h_est 112) | Planilha §7 |

## 8. Situação atual

A Sprint 9 (01–14/06/2026) está **Concluída** — 63 SP reais, 91% de aderência, 6 SP de carry. Os **6 MRs funcionais** (api !12/!13/!14, web !9/!10, crawler !4) foram **concluídos em 15/06/2026 com 2 revisores aprovados por MR e mergeados em develop**, integrando os filtros avançados (RF13 — api !13/web !9/crawler !4), a exportação CSV UTF-8 BOM (RF14 — api !14/web !10) e a busca de aeroportos por ILIKE (MF-64, api !12). A release **v0.9.0** foi promovida de develop para main (develop→homolog→main via api !17, tag v0.9.0 nos três repositórios) em 15/06/2026, com **RF13, RF14 e MF-64 Entregues (released em main)**. Os cards **MF-64, MF-65 e MF-69 estão "Concluído"** no Jira; o card **MF-73** (padronização de nomenclatura de BD) está no **api !15 ativo**, aprovado por cezar.velazquez + lucas.batista, aguardando merge.

Na medição de qualidade: **39 MRs** ao total — **38 concluídos + 1 ativo** (api !15, MF-73). **Todos os 39 MRs possuem exatamente 2 revisores aprovados** (verificado em 26/06/2026 via SQL — 0 linhas com contagem ≠ 2). A meta "MRs sem revisor = 0" está **plenamente cumprida**. A proteção de branch com push=No one está ativa em `main`/`homolog`/`develop` nos três repositórios, com reset de aprovação em push. A auditoria de GQA da S9 concluída — NC-001 encerrada. O consolidado S1–S9 é **CONFORME**.

## 9. Mudanças (change requests)

| ID | Descrição | Abertura | Dias em aberto | Status | Aceite final |
|---|---|---|---|---|---|
| CR-MF-001 | Antecipação dos filtros avançados de busca (`maxMiles`/`cabinType`, RF13) da Sprint 10 para a Sprint 9 (+10 h; 0 dia de atraso macro) | 28/05/2026 | — | Aprovada (implementada na S9) | RF13 entregue na release v0.9.0 (released em `main`) |

> Detalhamento em `CR-MILHASFACIL01-001`. A absorção do CR na S9 (api !13, web !9, crawler !4 — issue #65 "Concluído") está refletida no escopo (painel §1) e nas baselines (§6).

## 10. Decisões necessárias

Nenhuma decisão pendente no período de referência.

---

### Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-JIRA-01 | Board 614 com as colunas e o burndown das Sprints S1–S9 (S9 com MF-64/MF-65/MF-69 "Concluído"; MF-73 em andamento) | Jira — board 614 |
| IMG-CI-01 | Pipelines GitLab CI dos três repositórios com status `success`; gate JaCoCo 80% no api | GitLab — http://191.234.192.153 → CI/CD → Pipelines |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 25/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 25/06/2026 | Time de Melhoria Contínua | Aderência ao TPL-GPR-005: inclusão do painel de situação RAG de 4 dimensões (§1), CR-MF-001 (§9) e decisões necessárias (§10). |
| 1.2 | 26/06/2026 | Time de Melhoria Contínua | Reconciliação MPS.BR Nível C — S9 marcada como "Concluída" (63 SP real, 91%); total S1-S9 adicionado; remoção de "Mateus Veloso" e "WIP"; referências a PR #numbers trocadas por !iids GitLab; meta "MRs sem revisor = 0" — Cumprida (37 MRs, 2 revisores cada, verificado via SQL). |
| 1.3 | 29/06/2026 | Auditoria MPS.BR Nível C | Contagem de MRs atualizada 37 → 39 (inclusão de api !20/!21 — correção de build develop/homolog) em §8. |
