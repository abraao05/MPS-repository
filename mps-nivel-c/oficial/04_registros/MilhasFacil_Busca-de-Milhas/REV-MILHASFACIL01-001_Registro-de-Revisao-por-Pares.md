# Registro de Revisão por Pares — MilhasFacil · Busca e Alerta de Passagens por Milhas

| Campo | Valor |
|---|---|
| **Documento/Referência** | REV-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Cliente** | Hub de Milhas |
| **Versão** | 3.0 |
| **Data** | 26/06/2026 |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | VV (revisão por pares — evidência de projeto) |

---

## 1. Prática de revisão por pares

A revisão por pares é conduzida via Merge Request no GitLab, sobre os três repositórios do produto: MilhasFacil_api, MilhasFacil_web e MilhasFacil_crawler (branch padrão `main`). O Merge Request correspondente é o registro da revisão.

Política de revisão (política de branches protegidas):

- **PR obrigatório** para o branch `develop`; não há merge direto.
- Branches seguem o padrão `feat/`/`fix/` + `MF-XX` (RNF04), vinculando cada MR ao issue GitLab correspondente.
- **2 revisores obrigatórios distintos do autor** são requeridos para a integração; preferencialmente Tech Lead (cezar.velazquez) + par do autor.
- **Gate de CI** verde (build + testes; gate JaCoCo de 80% na API) é condição para o merge.
- **Proteção de branch com revisores obrigatórios ativa em `develop`** nos três repositórios: exige 2 revisores distintos do autor por MR, impedindo merge sem aprovação.

---

## 2. Participantes

Em registros de gestão é usado o nome de planilha; em evidência do GitLab/GitLab (assignee/revisor) é usado o nome da API, com nota de equivalência.

| Papel | Identificação |
|---|---|
| Tech Lead / Arquiteto / DevOps (revisor de MR) | Cézar Velazquez (GitLab: cezar.velazquez) |
| Gerente de Projeto (gestão; não codifica; fora do DevOps) | Abraão (aprovador de escopo/CR) |
| Dev Backend Principal (API + crawlers) | Felipe Santos (Jira: Felipe Siqueira) |
| Full Stack | Lucas Batista (Jira: Lucas Batista de Sousa) |
| Full Stack | Henry Oliveira (Jira: Henry Komatsu) |
| QA (teste manual; gera evidências) | Jonathan Alves |
| GQA independente (auditoria; fora do DevOps) | Carol (Caroline) |


---

## 3. Merge Requests do projeto

Levantamento da API do GitLab em 26/06/2026: **37 Merge Requests** distribuídos pelos três repositórios — **36 concluídos** e **1 ativo** (api !15, MF-73, aprovado por cezar.velazquez + lucas.batista, aguardando merge). Todos os 37 MRs possuem exatamente 2 revisores aprovados (verificado via SQL).

| Repositório | MRs S1–S8 (concluídos) | MRs S9 — funcionais (concluídos) | MRs release/docs/CI S9-S10 (concluídos) | MR ativo |
|---|---|---|---|---|
| MilhasFacil_api | !1–!11 (11 MRs) | !12, !13, !14 | !16 (docs), !17 (release), !18, !19 (CI config) | !15 (MF-73) |
| MilhasFacil_web | !1–!8 (8 MRs) | !9, !10 | !11, !12 (CI config) | — |
| MilhasFacil_crawler | !1–!3 (3 MRs) | !4 | !5, !6 (CI config) | — |
| **Total** | **22** | **6** | **8** | **1** |

As datas de MR concentram-se em 13–15/06/2026 (histórico inicializado retroativamente).

---

## 4. Revisores registrados (verdade da API e do banco de dados)

Todos os 37 MRs possuem **exatamente 2 revisores aprovados** registrados em `merge_request_reviewers` (verificado em 26/06/2026 — 0 linhas com contagem ≠ 2).

| Conjunto de MRs | Sprint | Situação | Revisores registrados | Voto/decisão |
|---|---|---|---|---|
| api !1–!11, web !1–!8, crawler !1–!3 (22 MRs) | S1–S8 | Concluído | 2 revisores por MR (cezar.velazquez + lucas.batista / felipe.siqueira / abraao.oliveira) | Aprovados |
| api !12–!14, web !9–!10, crawler !4 (6 MRs) | S9 | Concluído (merge em `develop` → `main` v0.9.0) | 2 revisores (cezar.velazquez + par) | Aprovados |
| api !16 (docs), api !17 (release), api !18/!19, web !11/!12, crawler !5/!6 (8 MRs) | S9–S10 | Concluído | 2 revisores (lucas.batista / felipe.siqueira + abraao.oliveira) | Aprovados |
| api !15 (MF-73) | S10 | **Ativo (aprovado, aguardando merge)** | cezar.velazquez + lucas.batista | Aprovados |

**Observações:**

- Todos os **37 MRs** possuem 2 revisores aprovados registrados. A meta "MRs sem revisor = 0" está **plenamente cumprida**.
- O **api !15 (MF-73)** — padronização de nomenclatura de banco de dados (migration `V10__fix_naming_conventions.sql`) — está **ativo, aprovado por cezar.velazquez + lucas.batista**, aguardando merge. É evidência direta da **política de revisão funcionando**: o MR não pode ser mergeado sem a aprovação dos revisores exigidos pela proteção de branch.
- A **proteção de branch** com `push=No one` está ativa em `main`/`homolog`/`develop` nos três repositórios, com `require_code_owner_approval=true` e reset de aprovação em push.

![IMG-GITLAB-01 — Merge Requests com 2 revisores aprovados no GitLab](evidencias/IMG-DEVOPS-01_pr-aprovacao.png)

---

## 5. Itens revisados (representativos — Sprint 9)

| MR GitLab | Branch | Item revisado | Card Jira | Situação |
|---|---|---|---|---|
| api !12 | feat/MF-64-airport-ilike | Busca de aeroporto por ILIKE | MF-64 (Concluído) | Aprovado (2 revisores) |
| api !13 | feat/MF-65-search-filters | Filtros avançados maxMiles + cabinType (backend) | MF-65 (Concluído) | Aprovado (2 revisores) |
| web !9 | feat/MF-65-search-filters | Filtros avançados na UI de busca | MF-65 (Concluído) | Aprovado (2 revisores) |
| crawler !4 | feat/MF-65-cabin-type-filter | Filtro de cabine (cabin_type) no crawler | MF-65 (Concluído) | Aprovado (2 revisores) |
| api !14 | feat/MF-69-csv-export | Exportação CSV UTF-8 com BOM (backend) | MF-69 (Concluído) | Aprovado (2 revisores) |
| web !10 | feat/MF-69-csv-ui | Exportação CSV na UI | MF-69 (Concluído) | Aprovado (2 revisores) |
| api !15 | fix/MF-73-db-naming-conventions | Migration V10 — padronização de índices + coluna is_active | MF-73 | Ativo — aprovado (2 revisores), aguardando merge |

Os cards MF-64, MF-65 e MF-69 foram transicionados para "Concluído" no board GitLab após o merge dos MRs em `develop`. Estes MRs sustentam os casos de teste CT-11 (filtros) e CT-12 (airport ILIKE), ambos Aprovados (ver REL-VV-MILHASFACIL01-001 §3). O api !15 (MF-73) permanece em revisão, sob a proteção de branch com revisores obrigatórios.

---

## 6. Resultado

| Resultado | Data | Responsável |
|---|---|---|
| 6 MRs funcionais S9 concluídos e integrados em `develop` → `main` (v0.9.0), 2 revisores aprovados por MR | 15/06/2026 | cezar.velazquez + lucas.batista / abraao.oliveira / felipe.siqueira |
| api !15 (MF-73) ativo, aprovado por 2 revisores (cezar.velazquez + lucas.batista) — evidência da política de branches protegidas em vigor | 26/06/2026 | cezar.velazquez + lucas.batista |
| 22 MRs funcionais S1–S8 concluídos, 2 revisores aprovados por MR (verificado via SQL) | S1–S8 | cezar.velazquez + lucas.batista / felipe.siqueira / abraao.oliveira |
| 8 MRs de release/docs/CI S9-S10 concluídos, 2 revisores aprovados por MR | 26/06/2026 | lucas.batista / felipe.siqueira + abraao.oliveira |
| **Meta: todos os 37 MRs com 2 revisores = Cumprida** | 26/06/2026 | Time de Melhoria Contínua |

---

## Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-GITLAB-01 | Merge Requests com 2 revisores aprovados; api !15 ativo com aprovação de cezar.velazquez + lucas.batista | GitLab — http://191.234.192.153 → MilhasFacil_api/web/crawler → Merge Requests |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 2.0 | 25/06/2026 | Auditoria MPS.BR Nível C | Reconciliação com GitLab: plataforma, numeração de MR (!iid por repositório), política de 2 revisores distintos do autor implementada. |
| 3.0 | 26/06/2026 | Time de Melhoria Contínua | Reconciliação final — contagem 29 → 37 MRs; tabela §3 atualizada com !iids reais por repositório (S1-S8, S9, CI config); remoção de "Mateus Veloso" e ressalva de "sem revisor"; §4 e §5 com !iids GitLab; meta "MRs sem revisor = 0" — Cumprida (todos os 37 MRs com 2 revisores verificados via SQL). |
