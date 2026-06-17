# Matriz de Rastreabilidade — Hub de Milhas · MilhasFacil (Busca de Milhas)

| Campo | Valor |
|---|---|
| **Documento** | RASTR-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.1 |
| **Data** | 15/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | REQ (evidência de projeto — rastreabilidade) |

---

## 1. Objetivo

Registrar a rastreabilidade bidirecional entre requisitos funcionais, cartões do Jira, branches de desenvolvimento, pull requests do Azure DevOps e builds de CI, garantindo que cada requisito pode ser localizado da especificação à entrega (forward) e que cada artefato de implementação remonta a um requisito (backward). As evidências refletem o estado real dos repositórios em 15/06/2026.

Os três repositórios do projeto (branch padrão `main`) são: **MilhasFacil_api**, **MilhasFacil_web** e **MilhasFacil_crawler**. As datas de PR e build concentram-se em 13–15/06/2026 (histórico inicializado retroativamente). Na **release v0.9.0** (15/06/2026), o ramo `develop` foi promovido `develop → homolog → main` (tag v0.9.0): os requisitos RF13, RF14 e a melhoria MF-64 estão **Entregues (released em `main`)**, como os demais RF. O cartão MF-73 (padronização de nomenclatura de banco, migration V10) permanece no **PR #29 ativo**, ainda não mergeado.

---

## 2. Rastreabilidade forward — Requisito → Jira → Branch → PR → Build

| Requisito | Cartão Jira | Branch | PR(s) Azure DevOps | Build | Sprint | Status |
|---|---|---|---|---|---|---|
| RF01 | MF-2 | feat/MF-2-auth-register | API #1 / Web #13 | succeeded (#41–#60) | S1 | Entregue (main) |
| RF02 | MF-3 | feat/MF-3-auth-login | API #2 | succeeded | S1 | Entregue (main) |
| RF03 | MF-8 / MF-9 / MF-10 | feat/MF-8-search-module · feat/MF-8-crawler-setup | API #3 / Craw #23 | succeeded | S2–S3 | Entregue (main) |
| RF04 | MF-11 | feat/MF-8-search-page | Web #14 | succeeded | S2 | Entregue (main) |
| RF05 | MF-13 | feat/MF-13-flight-history | API #4 / Web #15 | succeeded | S3 | Entregue (main) |
| RF06 | MF-21 | feat/MF-21-route-preferences | API #5 | succeeded | S3–S4 | Entregue (main) |
| RF07 | MF-23 | feat/MF-29-alerts-profile | API #6 / Web #16 | succeeded | S4 | Entregue (main) |
| RF08 | MF-29 | feat/MF-29-alerts-profile | API #6 | succeeded | S4 | Entregue (main) |
| RF09 | MF-44 / MF-49 | feat/MF-49-whatsapp-notifications | API #9 | succeeded | S7 | Entregue (main) |
| RF10 | MF-30 / MF-35 | feat/MF-35-subscriptions | API #7 | succeeded | S5 | Entregue (main) |
| RF11 | MF-31 | feat/MF-35-subscriptions | API #7 / Web #17 | succeeded | S5 | Entregue (main) |
| RF12 | MF-51 / MF-53 / MF-60 | feat/MF-60-redis-blacklist | API #10 | succeeded | S8 | Entregue (main) |
| RF13 | MF-62 / MF-65 / MF-66 | feat/MF-65-search-filters · feat/MF-65-cabin-type-filter | API #11 / Web #21 / Craw #27 | succeeded | S9 | **Entregue (released v0.9.0)** |
| RF14 | MF-57 / MF-69 | feat/MF-69-csv-export · feat/MF-69-csv-ui | API #12 / Web #22 | succeeded | S8–S9 | **Entregue (released v0.9.0)** |
| MF-64 | MF-64 | feat/MF-64-airport-ilike | API #28 | succeeded | S9 | **Entregue (released v0.9.0)** |
| RF15 | — | — | — | — | S10 | Não iniciado |

> A estabilização de parsers da Sprint 8 (correção do redesenho de portais, MF-59) foi entregue pela branch `fix/MF-42-estabilizacao` e pelas branches de crawler `fix/MF-8-smiles-fixes`, `feat/MF-crawler-refactor` e `fix/MF-crawler-regex-smiles-redesign`. A busca de aeroportos por `ILIKE`/`unaccent` (MF-64) foi entregue pela branch `feat/MF-64-airport-ilike` (PR API #28). A padronização de nomenclatura de banco (MF-73, migration V10) está na branch de chore associada ao **PR #29 ativo**.

---

## 3. Rastreabilidade backward — Branch/PR → Requisito

| Branch | PR(s) | Requisito de origem |
|---|---|---|
| feat/MF-2-auth-register | API #1 / Web #13 | RF01 |
| feat/MF-3-auth-login | API #2 | RF02 |
| feat/MF-8-search-module | API #3 | RF03 |
| feat/MF-8-crawler-setup | Craw #23 | RF03 |
| feat/MF-8-search-page | Web #14 | RF04 |
| feat/MF-13-flight-history | API #4 / Web #15 | RF05 |
| feat/MF-21-route-preferences | API #5 | RF06 |
| feat/MF-29-alerts-profile | API #6 / Web #16 | RF07, RF08 |
| feat/MF-35-subscriptions | API #7 / Web #17 | RF10, RF11 |
| feat/MF-49-whatsapp-notifications | API #9 | RF09 |
| feat/MF-60-redis-blacklist | API #10 | RF12 |
| feat/MF-65-search-filters / feat/MF-65-cabin-type-filter | API #11 / Web #21 / Craw #27 | RF13 |
| feat/MF-69-csv-export / feat/MF-69-csv-ui | API #12 / Web #22 | RF14 |
| feat/MF-64-airport-ilike | API #28 | MF-64 (busca de aeroportos) |
| MF-73 (padronização de nomenclatura de BD) | API #29 (ativo) | Chore — migration V10 (`is_active` + índices), GUIA-GCO-001 |
| fix/MF-42-estabilizacao | API #8 | RF03 (estabilização de busca) |

---

## 4. Pull requests e revisão (estado em 15/06/2026)

São 29 PRs ao todo: **28 concluídos** + **1 ativo (PR #29 — MF-73)**.

| Conjunto | PRs | Revisor registrado |
|---|---|---|
| 6 PRs da Sprint 9 (concluídos em 15/06/2026) | API #11, API #12, API #28, Web #21, Web #22, Craw #27 | **`Mateus Veloso` — Approved (vote 10)** (= Cézar Velazquez, Tech Lead), mergeados em `develop` e promovidos a `main` na release v0.9.0 |
| 22 PRs históricos S1–S8 (concluídos) | API #1–#10, Web #13–#20, Craw #23–#26 | Sem revisor registrado (integração retroativa do histórico) |
| PR ativo (MF-73) | API #29 | **Cézar Velazquez** (conta própria no Azure — Approved, vote 10) — aguardando merge (padronização de nomenclatura de BD, migration V10) |

> Nota de identidade (time atual): os registros de projeto adotam os nomes reais da equipe vigente — Gerente de Projeto **Abraão** (gestão; aprovador de escopo/CR), Tech Lead / Arquiteto / DevOps e **aprovador de PR Cézar Velazquez**, QA **Jonathan Alves**, GQA independente **Carol (Caroline)** e devs **Felipe Santos / Lucas Batista / Henry Oliveira**. Nas evidências legadas do Azure DevOps a aprovação de PR aparece sob a conta `Mateus Veloso`, que corresponde a **Cézar Velazquez**; os 6 PRs da Sprint 9 foram concluídos preservando essa aprovação (Approved, vote 10) e foi ativada **branch policy** exigindo ≥1 revisor em `develop` nos 3 repositórios, impedindo recorrência. Os 22 PRs históricos foram inicializados retroativamente e permanecem imutáveis (PR concluído é travado): não têm revisor registrado e são tratados como ressalva com causa-raiz (inicialização retroativa) — representado fielmente, sem afirmar aprovação onde não há. O PR #29 (MF-73) segue **ativo**, aprovado por Cézar Velazquez na conta própria dele no Azure (Approved, vote 10), aguardando merge.

Distribuição por repositório: API #1–#10 (S1–S8) + #11, #12, #28 (S9) concluídos + #29 (MF-73) ativo; Web #13–#20 (S1–S8) + #21, #22 (S9) concluídos; Crawler #23–#26 (S1–S8) + #27 (S9) concluídos. Pipelines (PowerShell@2, agente Default/Windows; triggers `develop`/`homolog`/`main`): "MilhasFacil API / Web / Crawler - Pipeline"; a pipeline da API possui gate JaCoCo de 80%. Builds reais #41–#60 quase todos `succeeded`; o build #42 ficou `canceled`. Baselines: v0.1.0 (S1) … v0.8.0 (S8), **v0.9.0 (release de 15/06/2026)**.

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

A padronização de nomenclatura de banco (MF-73, migration V10 — `route_preferences.is_active` + índices) está no **PR #29 ativo**, ainda não promovida a `main`.

Os requisitos não funcionais RNF01–RNF05 são rastreados às suas evidências no Documento de Design (PCP-MILHASFACIL01-001 §8) e à medição de cobertura do CI (RNF02, gate JaCoCo/Karma/pytest a partir da S4).

---

### Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-DEVOPS-01 | Lista dos 29 PRs (28 concluídos + 1 ativo, PR #29/MF-73) com revisor `Mateus Veloso` (= Cézar Velazquez) nos 6 PRs da Sprint 9 | Azure DevOps — Repos / Pull Requests dos repositórios MilhasFacil_api/web/crawler |
| IMG-JIRA-01 | Board 614 com os cartões MF-2..MF-72 distribuídos pelas sprints S1–S9 (MF-64/MF-65/MF-69 = Concluído) | Jira — board 614 |
| IMG-CI-01 | Builds #41–#60 com status `succeeded` (#42 `canceled`) e gate JaCoCo 80% na pipeline da API; tag de release v0.9.0 | Azure DevOps — Pipelines "MilhasFacil API/Web/Crawler - Pipeline" |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Preenchimento do PR da branch `fix/MF-42-estabilizacao` (RF03) na rastreabilidade backward com API #8 (conforme ITP-MILHASFACIL01-001 §5, Ordem 9 — estabilização da S6). |
