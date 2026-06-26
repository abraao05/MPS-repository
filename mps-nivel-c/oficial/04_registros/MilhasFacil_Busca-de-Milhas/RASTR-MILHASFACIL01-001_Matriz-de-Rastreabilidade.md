# Matriz de Rastreabilidade — Hub de Milhas · MilhasFacil (Busca de Milhas)

| Campo | Valor |
|---|---|
| **Documento** | RASTR-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.2 |
| **Data** | 26/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | REQ (evidência de projeto — rastreabilidade) |

---

## 1. Objetivo

Registrar a rastreabilidade bidirecional entre requisitos funcionais, issues do GitLab, branches de desenvolvimento, merge requests do GitLab e builds de CI, garantindo que cada requisito pode ser localizado da especificação à entrega (forward) e que cada artefato de implementação remonta a um requisito (backward). As evidências refletem o estado real dos repositórios em 26/06/2026.

Os três repositórios do projeto (branch padrão `main`) são: **MilhasFacil_api**, **MilhasFacil_web** e **MilhasFacil_crawler**, hospedados no GitLab (http://191.234.192.153). Na **release v0.9.0** (15/06/2026), o ramo `develop` foi promovido `develop → homolog → main` (tag v0.9.0): os requisitos RF13, RF14 e a melhoria MF-64 estão **Entregues (released em `main`)**, como os demais RF. O cartão MF-73 (padronização de nomenclatura de banco, migration V10) permanece no **MR !15 ativo** (MilhasFacil_api), ainda não mergeado.

---

## 2. Rastreabilidade forward — Requisito → Jira → Branch → MR → Build

| Requisito | Cartão Jira | Branch | MR(s) GitLab | Build | Sprint | Status |
|---|---|---|---|---|---|---|
| RF01 | MF-2 | feat/MF-2-auth-register | api !1 / web !1 | success | S1 | Entregue (main) |
| RF02 | MF-3 | feat/MF-3-auth-login | api !2 | success | S1 | Entregue (main) |
| RF03 | MF-8 / MF-9 / MF-10 | feat/MF-8-search-module · feat/MF-8-crawler-setup | api !4 / crawler !1 | success | S2–S3 | Entregue (main) |
| RF04 | MF-11 | feat/MF-8-search-page | web !2 | success | S2 | Entregue (main) |
| RF05 | MF-13 | feat/MF-13-flight-history | api !5 / web !3 | success | S3 | Entregue (main) |
| RF06 | MF-21 | feat/MF-21-route-preferences | api !6 | success | S3–S4 | Entregue (main) |
| RF07 | MF-23 | feat/MF-29-alerts-profile | api !7 / web !4 | success | S4 | Entregue (main) |
| RF08 | MF-29 | feat/MF-29-alerts-profile | api !7 | success | S4 | Entregue (main) |
| RF09 | MF-44 / MF-49 | feat/MF-49-whatsapp-notifications | api !10 | success | S7 | Entregue (main) |
| RF10 | MF-30 / MF-35 | feat/MF-35-subscriptions | api !8 | success | S5 | Entregue (main) |
| RF11 | MF-31 | feat/MF-35-subscriptions | api !8 / web !5 | success | S5 | Entregue (main) |
| RF12 | MF-51 / MF-53 / MF-60 | feat/MF-60-redis-blacklist | api !11 | success | S8 | Entregue (main) |
| RF13 | MF-62 / MF-65 / MF-66 | feat/MF-65-search-filters · feat/MF-65-cabin-type-filter | api !13 / web !9 / crawler !4 | success | S9 | **Entregue (released v0.9.0)** |
| RF14 | MF-57 / MF-69 | feat/MF-69-csv-export · feat/MF-69-csv-ui | api !14 / web !10 | success | S8–S9 | **Entregue (released v0.9.0)** |
| MF-64 | MF-64 | feat/MF-64-airport-ilike | api !12 | success | S9 | **Entregue (released v0.9.0)** |
| RF15 | — | — | — | — | S10 | Não iniciado |

> A estabilização de parsers da Sprint 8 (correção do redesenho de portais, MF-59) foi entregue pela branch `fix/MF-42-estabilizacao` e pelas branches de crawler `fix/crawler-maintenance-sp2-sp6` e `fix/crawler-sp7-sp8`. A busca de aeroportos por `ILIKE`/`unaccent` (MF-64) foi entregue pela branch `feat/MF-64-airport-ilike` (api !12). A padronização de nomenclatura de banco (MF-73, migration V10) está na branch `fix/MF-73-db-naming-conventions` associada ao **api !15 ativo**.

---

## 3. Rastreabilidade backward — Branch/MR → Requisito

| Branch | MR(s) GitLab | Requisito de origem |
|---|---|---|
| feat/MF-2-auth-register | api !1 / web !1 | RF01 |
| feat/MF-3-auth-login | api !2 | RF02 |
| feat/MF-8-search-module | api !4 | RF03 |
| feat/MF-8-crawler-setup | crawler !1 | RF03 |
| feat/MF-8-search-page | web !2 | RF04 |
| feat/MF-13-flight-history | api !5 / web !3 | RF05 |
| feat/MF-21-route-preferences | api !6 | RF06 |
| feat/MF-29-alerts-profile | api !7 / web !4 | RF07, RF08 |
| feat/MF-35-subscriptions | api !8 / web !5 | RF10, RF11 |
| feat/MF-49-whatsapp-notifications | api !10 | RF09 |
| feat/MF-60-redis-blacklist | api !11 | RF12 |
| feat/MF-65-search-filters / feat/MF-65-cabin-type-filter | api !13 / web !9 / crawler !4 | RF13 |
| feat/MF-69-csv-export / feat/MF-69-csv-ui | api !14 / web !10 | RF14 |
| feat/MF-64-airport-ilike | api !12 | MF-64 (busca de aeroportos) |
| fix/MF-73-db-naming-conventions | api !15 (ativo) | Chore — migration V10 (`is_active` + índices), GUIA-GCO-001 |
| fix/MF-42-estabilizacao | api !9 | RF03 (estabilização de busca) |

---

## 4. Merge requests e revisão (estado em 26/06/2026)

São **37 MRs** ao todo: **36 concluídos** + **1 ativo (api !15 — MF-73, fix/MF-73-db-naming-conventions)**.

| Conjunto | MRs GitLab | Revisores registrados |
|---|---|---|
| 6 MRs funcionais S9 (concluídos em 15/06/2026) | api !12 (MF-64), api !13 (RF13), api !14 (RF14), web !9 (RF13), web !10 (RF14), crawler !4 (RF13) | cezar.velazquez + lucas.batista / abraao.oliveira / felipe.siqueira (2 por MR — Approved), mergeados em `develop` e promovidos a `main` na release v0.9.0 |
| MR de release S9: develop → homolog | api !17 | lucas.batista + abraao.oliveira (Approved) |
| MR de documentação/GQA | api !16 | cezar.velazquez + lucas.batista (Approved) |
| 22 MRs funcionais S1–S8 (concluídos) | api !1–!11, web !1–!8, crawler !1–!3 | 2 revisores por MR — cezar.velazquez + lucas.batista / felipe.siqueira / abraao.oliveira (Approved) |
| 6 MRs de configuração CI S10 | api !18/!19, web !11/!12, crawler !5/!6 | lucas.batista (ou felipe.siqueira) + abraao.oliveira (Approved) |
| MR ativo (MF-73) | api !15 fix/MF-73-db-naming-conventions → develop | cezar.velazquez + lucas.batista (Approved) — aguardando merge (padronização de nomenclatura de BD, migration V10) |

> Nota de identidade (time atual): os registros de projeto adotam os nomes reais da equipe vigente — Gerente de Projeto **Abraão** (gestão; aprovador de escopo/CR), Tech Lead / Arquiteto / DevOps e **aprovador de MR Cézar Velazquez**, QA **Jonathan Alves**, GQA independente **Carol (Caroline)** e devs **Felipe Santos / Lucas Batista / Henry Oliveira**. Todos os **37 MRs possuem exatamente 2 revisores aprovados** registrados no GitLab (verificado em 26/06/2026 via SQL em `merge_request_reviewers` — 0 linhas com contagem ≠ 2). O MR api !15 (MF-73) segue **ativo**, aprovado por cezar.velazquez + lucas.batista, aguardando merge.

Distribuição por repositório: api !1–!14 + !16–!19 (concluídos; inclui CI setup, release, docs e CI config) + api !15 (MF-73, ativo); web !1–!12 (todos concluídos); crawler !1–!6 (todos concluídos). Pipelines GitLab CI (runner-vm-docker, online; triggers `develop`/`homolog`/`main`): `.gitlab-ci.yml` presente em todos os repositórios. Gate JaCoCo de 80% no api (stage `test`). Baselines: v0.1.0 (S1) … v0.8.0 (S8), **v0.9.0 (release de 15/06/2026)**.

---

## 5. Rastreabilidade — Casos de teste por requisito

| Caso de teste | Cenário | Requisito | Sprint | Tipo | Resultado |
|---|---|---|---|---|---|
| CT-01 | register + login | RF01, RF02 | S1 | Happy | Aprovado |
| CT-02 | credenciais inválidas → 401 | RF02 | S1 | Sad | Aprovado |
| CT-03 | busca 3 companhias < 30s | RF03 | S2/S3 | Happy | Aprovado |
| CT-04 | histórico paginado (MF-38) | RF05 | S3 | Happy | Aprovado |
| CT-05 | refresh token rotation | RF11 | S5 | Happy | Aprovado |
| CT-06 | logout blacklist → 401 | RF12 | S8 | Happy | Aprovado |
| CT-07 | WhatsApp sem duplicata | RF08, RF09 | S7 | Happy | Aprovado |
| CT-08 | LatamParser regressão (MF-59) | RF03 | S8 | Regressão | Aprovado |
| CT-09 | Smiles 6 dígitos (MF-58) | RF03 | S8 | Happy | Aprovado |
| CT-10 | coverage gate ≥ 80% | RNF02 | S6+ | CI/CD | Aprovado |
| CT-11 | filtros maxMiles + cabinType | RF13 | S9 | Happy | **Aprovado** (testes do `FilteredSearchService` integrados; build verde) |
| CT-12 | airport ILIKE (MF-64) | MF-64 | S9 | Sad | **Aprovado** (teste de integração `AirportRepository` `q=gru` → GRU Guarulhos; build verde) |

---

## 6. Cobertura de requisitos

| Faixa | Requisitos | Situação |
|---|---|---|
| Entregues em produção (main) | RF01–RF14 | 14 requisitos concluídos e verificados (PRs concluídos / builds `succeeded`); RF13/RF14 promovidos na release v0.9.0 |
| Não iniciado | RF15 | Planejado para a Sprint 10 (push PWA) |

**Cobertura de RF: 14/15 entregues em produção (main) (RF01–RF14); RF15 (1/15) não iniciado.** A melhoria MF-64 está **Entregue (released na v0.9.0)** em `main`.

A padronização de nomenclatura de banco (MF-73, migration V10 — `route_preferences.is_active` + índices) está no **api !15 ativo** (fix/MF-73-db-naming-conventions), ainda não promovida a `main`.

Os requisitos não funcionais RNF01–RNF05 são rastreados às suas evidências no Documento de Design (PCP-MILHASFACIL01-001 §8) e à medição de cobertura do CI (RNF02, gate JaCoCo/Karma/pytest a partir da S4).

---

### Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-GITLAB-01 | Lista dos 37 MRs (36 concluídos + 1 ativo, api !15/MF-73); todos com 2 revisores aprovados | GitLab — http://191.234.192.153 → MilhasFacil_api/web/crawler → Merge Requests |
| IMG-JIRA-01 | Board 614 com os cartões MF-2..MF-72 distribuídos pelas sprints S1–S9 (MF-64/MF-65/MF-69 = Concluído) | Jira — board 614 |
| IMG-CI-01 | Pipelines GitLab CI com status `success`; gate JaCoCo 80% no api (stage `test`); tag de release v0.9.0 | GitLab — http://191.234.192.153 → MilhasFacil_api → CI/CD → Pipelines |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Preenchimento do MR da branch `fix/MF-42-estabilizacao` (RF03) na rastreabilidade backward com api !9 (conforme ITP-MILHASFACIL01-001 §5, Ordem 9 — estabilização da S6). |
| 1.2 | 26/06/2026 | Time de Melhoria Contínua | Reconciliação MPS.BR Nível C — substituição de todas as referências Azure DevOps por GitLab (MR !iids por repositório); contagem 29 → 37 MRs (inclui release api !17, docs api !16, 6 MRs de CI config S10); remoção da ressalva "sem revisor" (todos os 37 MRs com 2 revisores verificados via SQL em `merge_request_reviewers`); seções 2, 3 e 4 atualizadas com !iids reais do GitLab. |
