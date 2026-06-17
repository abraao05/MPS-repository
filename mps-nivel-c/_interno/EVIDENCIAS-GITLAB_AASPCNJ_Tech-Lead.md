# Evidências Técnicas — Projeto AASP_CNJ (Agente de Captura de Andamentos Processuais)
# Fonte: GitLab (self-hosted)

| Campo | Valor |
|---|---|
| **Para** | Raony Chagas (Desenvolvedor Sênior / Principal) |
| **De** | Abraão Oliveira (GP / Responsável MPS-SW) |
| **Data** | 17/06/2026 |
| **Projeto** | AASPCNJ01 — Agente de Captura de Andamentos Processuais |
| **Fonte das evidências** | **GitLab self-hosted** — `http://191.234.192.153/aasp/cnj` |

---

## Contexto

Este documento substitui a fonte das evidências técnicas: o que antes era coletado em **Azure DevOps** (repositórios, PRs, pipelines, tags) e **ClickUp** (cards/bugs/horas) passa a ser extraído do **GitLab self-hosted** da Timeware, onde o projeto foi consolidado. A estrutura por documento (PCP, ITP, GCO, VV, RASTR, MED, GDE, CAP) é a mesma — **apenas a origem da evidência mudou**.

**Projeto no GitLab:** `http://191.234.192.153/aasp/cnj` (branch padrão `prod`).

Estado conferido (17/06/2026): repositório único com as soluções **`CapturaServices/`** e **`WorkerAndamentos/`**; **21 branches** (GitFlow: `prod`, `homolog`, `develop`, `feature/NN-*`, `release/v220..v240`, `hotfix/v241`); **21 merge requests** (20 merged + 1 aberto = US-18 GMUD); **40 work items** (20 histórias US-xx, 10 bugs BUG-xx, 7 decisões D-xx, 2 CR, 1 ATA); **12 milestones** (Discovery + Sprints 1–11); **5 tags/releases** de baseline; **15 pipelines** verdes (`build → test → deploy`).

**Permanecem em ferramenta de runtime** (não há equivalente em versionamento): estado no banco (SSMS), índice Elasticsearch/Kibana, fila RabbitMQ Management, relatório de horas (ClickUp) e contrato/custo. Onde há registro equivalente no GitLab (bug, história, decisão, código da feature), ele está indicado.

---

## 1. PCP — Documento de Design (arquitetura)

### 1.1 Arquitetura da solução (PCP §2.1)
**O documento afirma:** CapturaServer + WorkerAndamentos + RabbitMQ + webhook → API AndamentosProcessuais → Elasticsearch.
**Evidência no GitLab:** estrutura das soluções no repositório — `CapturaServices/` e `WorkerAndamentos/` (+ `WorkersAndamentos.sln`).
`http://191.234.192.153/aasp/cnj/-/tree/prod`
**Complemento externo:** diagrama de fluxo (se houver, anexar ao PCP). A API AndamentosProcessuais (lado do webhook/indexação) está em `http://191.234.192.153/aasp/andamentosprocessuais`.

### 1.2 Tabelas de controle (PCP §2.2)
**O documento afirma:** `ProcessoCaptura`, `ProcessoCapturaLogin`, `ProcessoCapturaMovimentacaoStatus`, `PonteAPI`.
**Evidência:** o schema/DDL não está versionado no repositório do CNJ (pasta `db/` vazia) — a evidência das tabelas **permanece no banco** (script `CREATE` / print de colunas via SSMS/Azure Data Studio). *(Se desejar centralizar no GitLab, posso adicionar o DDL em `/db` do repositório.)*

### 1.3 Roteamento por CodigoFonteAPI e fallback (PCP §2.4/2.5 · RF-01, RF-02, RF-07 · US-04, US-09, US-11)
**O documento afirma:** roteamento por `CodigoFonteAPI` + fallback em 3 níveis (CNJ → EPROC/ESAJ → parceiras por prioridade).
**Evidência no GitLab:** branch/feature do roteamento e do fallback:
- `feature/16-codigofonteapi` → `http://191.234.192.153/aasp/cnj/-/tree/feature/16-codigofonteapi`
- `feature/20-parceiras-fallback` → `http://191.234.192.153/aasp/cnj/-/tree/feature/20-parceiras-fallback`
Código em `CapturaServices/` (engine/roteamento da captura).

---

## 2. ITP — Estratégia de Integração

### 2.1 Integração DataJud/CNJ (ITP §1 · RF-01, RF-05 · US-04, US-05)
**Evidência no GitLab:** features da integração CNJ e do token Bearer compartilhado:
- `feature/14-cnj-datajud` → `…/-/tree/feature/14-cnj-datajud`
- `feature/15-token-cnj` → `…/-/tree/feature/15-token-cnj`
Histórias: **US-04** (DataJud/CNJ fonte primária) e **US-05** (Token Bearer CNJ) — work items em `…/-/issues?label_name[]=tipo::historia`.
**Permanece externo:** coleção Postman da API CNJ (não versionada no repo) e a tabela `PonteAPI` (runtime/banco).

### 2.2 Fila RabbitMQ unificada (ITP §3 · RF-03, RF-12 · US-08, US-09)
**Evidência no GitLab:** `feature/18-rabbitmq-fila` → `…/-/tree/feature/18-rabbitmq-fila` (código do produtor/consumidor da fila unificada). Histórias **US-08/US-09**.
**Permanece externo:** print do RabbitMQ Management (fila/consumidores) é estado de runtime.

### 2.3 Webhook → Elasticsearch (ITP §6 · RF-11 · US-07)
**Evidência no GitLab:** `feature/17-webhook-indexacao` → `…/-/tree/feature/17-webhook-indexacao`; endpoint do webhook na API: `http://191.234.192.153/aasp/andamentosprocessuais`.
**Permanece externo:** documento indexado no Elasticsearch / log de indexação (runtime, Kibana).

### 2.4 Pipeline CI/CD (ITP §4)
**Evidência no GitLab:** pipelines do projeto (15 execuções, todas `success`; estágios `build → test → deploy`):
`http://191.234.192.153/aasp/cnj/-/pipelines`

---

## 3. GCO — Gerência de Configuração

### 3.1 Repositórios e GitFlow (GCO §2/§3)
**Evidência no GitLab:** branches no padrão GitFlow (`prod`, `homolog`, `develop`, `feature/NN-*`, `release/v220..v240`, `hotfix/v241`):
`http://191.234.192.153/aasp/cnj/-/branches`

### 3.2 Baseline / tag de versão (GCO §4)
**O documento afirma:** baseline de publicação `v240`. **No GitLab a numeração é semântica** — a baseline de go-live do CNJ é a **`v2.0.0` (BL-CNJ)**.
**Evidência no GitLab:** tags + releases com data e commit:
`http://191.234.192.153/aasp/cnj/-/tags` · `…/-/releases`

| Baseline | Tag | Data |
|---|---|---|
| BL-INFRA | `v0.9.0` | 10/02/2026 |
| BL-EPROC | `v1.0.0` | 24/03/2026 |
| **BL-CNJ (go-live)** | **`v2.0.0`** | 01/06/2026 |
| Patch | `v2.0.1` | 02/06/2026 |
| BL-HOTFIX | `v2.0.2` | 05/06/2026 |

### 3.3 Pull Requests revisados (GCO §6 + REV — code review)
**O documento afirma:** merge para `develop`/`prod` exige ≥ 1 revisor além do autor.
**Evidência no GitLab:** 21 merge requests com **revisor vinculado** (revisão cruzada Raony ↔ Cezar):
`http://191.234.192.153/aasp/cnj/-/merge_requests?state=all`
- Ex.: **MR !1** (`feature/11-eproc-crawler`, autor Raony, revisor Cezar) `…/-/merge_requests/1`; **MR !8** (`feature/18-rabbitmq-fila`) ; **MR !21** (`feature/28-gmud-implantacao` — US-18, aberto/em andamento).
> Estes mesmos MRs atendem o registro **REV-AASPCNJ01-001** (revisão por pares / VV2).

---

## 4. VV / REL-VV — Verificação e Validação

### 4.1 Defeitos registrados (REL-VV §3 — BUG-01 a BUG-10)
**Evidência no GitLab:** os 10 defeitos como work items (`tipo::bug`), com status e severidade:
`http://191.234.192.153/aasp/cnj/-/issues?label_name[]=tipo::bug`
- Inclui os críticos da fila de 137 mil itens (**BUG-05/BUG-06**).

### 4.2 Fluxo de captura validado (VV §6 / REL-VV §4 — CA01..CA07 · US-16)
**Evidência no GitLab:** a validação E2E está registrada na história **US-16 — Validar fluxo E2E por amostragem** `…/-/issues?label_name[]=tipo::historia`.
**Permanece externo (runtime):** os prints de `ProcessoCaptura` (status 3), `ProcessoCapturaLogin`, `ProcessoCapturaMovimentacaoStatus`, erro parcial por instância (CA05) e o documento indexado no Elasticsearch/Kibana (CA04) — são estado de banco/índice, não de versionamento.

### 4.3 Desligamento nas APIs parceiras (CA06 · RF-04 · US-10)
**Evidência no GitLab:** `feature/20-parceiras-fallback` (lógica de desligamento do NUP após captura CNJ) + história **US-10**. Log de execução permanece em runtime.

### 4.4 Segredo de justiça por instância (CA07 · RF-10 · US-13)
**Evidência no GitLab:** `feature/23-segredo-instancia` → `…/-/tree/feature/23-segredo-instancia` + história **US-13**.

### 4.5 Retry de webhook (US-17 · RNF-02)
**Evidência no GitLab:** `feature/27-retry-webhook` → `…/-/tree/feature/27-retry-webhook` + história **US-17**.

---

## 5. RASTR / REQ — Rastreabilidade requisito → código → teste

### 5.1 Vínculo card ↔ código (REQ4)
**Evidência no GitLab (forte):** a convenção de branch referencia o número do work item — `feature/NN-descricao` (ex.: `feature/14-cnj-datajud`, `feature/17-webhook-indexacao`, `feature/23-segredo-instancia`), e cada MR fecha a história correspondente.
`http://191.234.192.153/aasp/cnj/-/branches` + `…/-/merge_requests?state=merged`

---

## 6. MED — Medição

### 6.1 Esforço (MED §3 — 586 est. / ~624 real)
**Evidência no GitLab:** a distribuição do esforço por iteração está nas **milestones** (Discovery + Sprints 1–11) e nos work items alocados a cada uma:
`http://191.234.192.153/aasp/cnj/-/milestones`
**Permanece externo:** o relatório de horas por atividade (ClickUp, projetos id 213 EPROC/ESAJ e id 256 CNJ).

### 6.2 Custo e economia (MED §4)
**Permanece externo:** comprovação de custo/volume (contrato/fatura da API CNJ e da Solucionário) — não é dado de versionamento. (Abraão tem o contrato.)

---

## 7. GDE — Decisão (fonte primária CNJ, 06–07/04/2026)

**Evidência no GitLab:** as decisões de arquitetura estão como work items (`tipo::decisao`, D-01..D-07) e a ata do alinhamento como `tipo::ata`:
`http://191.234.192.153/aasp/cnj/-/issues?label_name[]=tipo::decisao` · `…/-/issues?label_name[]=tipo::ata`
- **D-02 — DataJud/CNJ como fonte primária** e **ATA-AASPCNJ01-001** registram a decisão de 06–07/04/2026.

---

## 8. CAP — Capacitação / transferência de conhecimento

**Evidência no GitLab:** a transferência de conhecimento via **code review** está nos 21 MRs (revisão cruzada Raony ↔ Cezar), evidenciando ciência das mudanças por todo o time.
`http://191.234.192.153/aasp/cnj/-/merge_requests?state=merged`
**Permanece externo:** a coleção Postman da API CNJ não está versionada no repositório (pasta `docs/` vazia). *(Se desejar, posso adicioná-la a `/docs` do repo para centralizar no GitLab.)*

---

## 9. Prioridade máxima (fonte GitLab)

| # | Item | Onde buscar no GitLab |
|---|---|---|
| 1 | PRs aprovados (code review) — GCO/REV | `…/-/merge_requests?state=all` (21 MRs, revisor vinculado) |
| 2 | Baseline (tags/releases) — GCO | `…/-/tags` (`v2.0.0` BL-CNJ) + `…/-/releases` |
| 3 | Pipeline CI/CD verde — ITP | `…/-/pipelines` (15 success, `build/test/deploy`) |
| 4 | Bugs (BUG-05/06 da fila) — VV | `…/-/issues?label_name[]=tipo::bug` |
| 5 | Rastreabilidade card↔código — RASTR | `…/-/branches` (`feature/NN-*`) + MRs |
| 6 | Decisão fonte primária CNJ — GDE | `…/-/issues?label_name[]=tipo::decisao` (D-02) |
| 7 | Distribuição de esforço por sprint — MED | `…/-/milestones` |

---

## 10. Mapa de equivalência — fonte anterior → GitLab

| Fonte anterior | Evidência | Onde está agora no GitLab |
|---|---|---|
| Azure DevOps — Repos / estrutura | PCP §2.1 | `…/-/tree/prod` (`CapturaServices`, `WorkerAndamentos`) |
| Azure DevOps — branches/GitFlow | GCO §2/§3, REQ4 | `…/-/branches` (`feature/NN-*`) |
| Azure DevOps — Pull Requests | GCO §6 / REV | `…/-/merge_requests` (revisor vinculado) |
| Azure DevOps — Tags / baseline | GCO §4 | `…/-/tags` + `…/-/releases` (`v2.0.0` BL-CNJ) |
| Azure DevOps — Pipelines | ITP §4 | `…/-/pipelines` (15 success) |
| ClickUp — cards de bug | REL-VV §3 | work items `tipo::bug` (BUG-01..10) |
| ClickUp — backlog/histórias | RASTR / US-xx | work items `tipo::historia` (US-01..20) |
| ClickUp — time tracking (horas) | MED §3 | Externo (ClickUp) + milestones p/ distribuição |
| RabbitMQ Management | ITP §3 (CA) | Externo (runtime) + `feature/18-rabbitmq-fila` |
| Elasticsearch / Kibana | ITP §6 / VV CA04 | Externo (runtime) + `feature/17-webhook-indexacao` |
| Banco / SSMS (tabelas) | PCP §2.2 / VV CA01-03 | Externo (runtime) — `db/` vazio no repo |
| Postman (API CNJ) | ITP §2.1 / CAP | Externo — `docs/` vazio no repo |
| Contrato / fatura | MED §4 | Externo (contrato) |

---

*Documento gerado a partir do estado real do GitLab self-hosted (`aasp/cnj`) em 17/06/2026. Itens de runtime (banco, Elasticsearch, RabbitMQ, ClickUp/horas, contrato) permanecem nas suas fontes; onde há registro equivalente no GitLab (história, bug, decisão, código da feature, MR), ele está indicado. Nenhum dado foi inventado.*
