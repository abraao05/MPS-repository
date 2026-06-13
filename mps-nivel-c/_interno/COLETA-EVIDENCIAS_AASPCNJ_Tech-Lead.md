# Coleta de Evidências Técnicas — Projeto AASP_CNJ (WorkerAndamentos)
# Solicitação ao Desenvolvedor Sênior / Tech Lead do projeto

| Campo | Valor |
|---|---|
| **Para** | Raony Chagas (Desenvolvedor Sênior / Principal) |
| **De** | Abraão Oliveira (GP / Responsável MPS-SW) |
| **Data** | 12/06/2026 |
| **Projeto** | AASPCNJ01 — Agente de Captura de Andamentos Processuais |
| **Prazo sugerido** | 5 dias úteis |

---

## Contexto

Os documentos de texto do projeto (PCP, ITP, VV, GCO, MED etc.) já estão prontos e versionados em `oficial/04_registros/AASP_CNJ/`. Para a avaliação MPS-SW Nível C, cada afirmação técnica precisa de **evidência da ferramenta real**: Azure DevOps, ClickUp, RabbitMQ, banco de dados (tabelas de controle), Elasticsearch/Kibana e a coleção Postman da API CNJ.

Abaixo, **por documento**, está: o que o registro afirma, **exatamente o que capturar/exportar** e **onde**. Tire prints com data e identificação visíveis. Onde o dado não existir mais, anote — não invente.

> **Como funciona o vínculo:** cada item aponta o documento (ex.: `PCP §2.2`), o requisito (`RF-xx`) e/ou a história do backlog (`US-xx` da planilha GEST-AASPCNJ01). Assim a evidência cai direto no lugar certo.

---

## 1. PCP — Documento de Design (arquitetura)

### 1.1 Arquitetura da solução (PCP §2.1)
**O documento afirma:** CapturaServer (serviço Windows) + WorkerAndamentos (workers concorrentes) + RabbitMQ + webhook → API AndamentosProcessuais → Elasticsearch.
**Evidência a trazer:** diagrama de arquitetura do fluxo (se houver no repositório/Confluence, exportar; se não, um desenho simples já serve). Print da estrutura de pastas/projetos das 3 soluções no Azure DevOps.
**Onde:** `Azure DevOps → Repos → WorkerAndamentos / CapturaServer / AndamentosProcessuais → print da árvore de pastas`.
**Arquivo:** `pcp-arquitetura-diagrama.png`, `pcp-estrutura-repos.png`

### 1.2 Tabelas de controle (PCP §2.2)
**O documento afirma:** `ProcessoCaptura`, `ProcessoCapturaLogin`, `ProcessoCapturaMovimentacaoStatus`, `PonteAPI`.
**Evidência a trazer:** print do schema (colunas) de cada tabela — ou o script DDL.
**Onde:** SSMS/Azure Data Studio → cada tabela → script `CREATE` ou print das colunas; ou a pasta `/db` no Azure DevOps.
**Arquivo:** `pcp-schema-tabelas-controle.png` (ou `.sql`)

### 1.3 Roteamento por CodigoFonteAPI e fallback (PCP §2.4/2.5 · RF-01, RF-02, RF-07 · US-04, US-09, US-11)
**O documento afirma:** roteamento por `CodigoFonteAPI` e fallback em 3 níveis (CNJ → EPROC/ESAJ → parceiras por prioridade).
**Evidência a trazer:** print do trecho de código onde o worker decide a fonte pelo `CodigoFonteAPI` e onde aciona o fallback.
**Onde:** Azure DevOps → Repos → WorkerAndamentos → arquivo do roteamento/fallback → print.
**Arquivo:** `pcp-roteamento-codigofonteapi.png`

---

## 2. ITP — Estratégia de Integração

### 2.1 Integração DataJud/CNJ (ITP §1 · RF-01, RF-05 · US-04, US-05)
**Evidência a trazer:** coleção Postman da API CNJ (export `.json`) e/ou print de uma chamada de consulta com retorno; print do mecanismo de token Bearer compartilhado (tabela `PonteAPI` com data de expiração — sem expor o token).
**Onde:** Postman → Export collection; Azure DevOps → pasta `/docs`.
**Arquivo:** `itp-postman-cnj.json`, `itp-token-ponteapi.png`

### 2.2 Fila RabbitMQ unificada (ITP §3 · RF-03, RF-12 · US-08, US-09)
**Evidência a trazer:** print do RabbitMQ Management mostrando a fila unificada (nome, mensagens, consumidores/workers ativos).
**Onde:** RabbitMQ Management UI → Queues → a fila de captura → print.
**Arquivo:** `itp-rabbitmq-fila.png`

### 2.3 Webhook → Elasticsearch (ITP §6 · RF-11 · US-07)
**Evidência a trazer:** print do endpoint de webhook na API AndamentosProcessuais e de um log/registro de indexação bem-sucedida.
**Onde:** código do endpoint (Azure DevOps) + log da aplicação (AWS/CloudWatch ou arquivo de log).
**Arquivo:** `itp-webhook-indexacao.png`

### 2.4 Pipeline CI/CD (ITP §4)
**Evidência a trazer:** print do pipeline de build/publicação no Azure DevOps (último run verde).
**Onde:** `Azure DevOps → Pipelines → último run → print`.
**Arquivo:** `itp-pipeline-cicd.png`

---

## 3. GCO — Gerência de Configuração

### 3.1 Repositórios e GitFlow (GCO §2/§3)
**Evidência a trazer:** print da lista de repositórios e das branches (`main`, `develop`, `feature/*`, `bugfix/*`) mostrando a convenção GitFlow.
**Onde:** `Azure DevOps → Repos → Branches → print`.
**Arquivo:** `gco-branches-gitflow.png`

### 3.2 Baseline / tag de versão (GCO §4)
**O documento afirma:** baseline de publicação `v240`.
**Evidência a trazer:** print da lista de tags mostrando `v240` (ou a tag real da publicação) com data e commit. **Confirme com o Abraão a numeração exata da tag.**
**Onde:** `Azure DevOps → Repos → Tags → print`. Alternativa: `git tag -l --sort=-version:refname | head`.
**Arquivo:** `gco-tags-baseline.png`

### 3.3 Pull Requests revisados (GCO §6 + REV — code review)
**O documento afirma:** merge para `develop` exige ≥ 1 revisor além do autor.
**Evidência a trazer:** print de **2–3 PRs concluídos (merged)** mostrando autor (Raony Chagas / Levi Santos), revisor, comentários e aprovação.
**Onde:** `Azure DevOps → Repos → Pull Requests → filtrar Completed → print`.
**Arquivo:** `gco-pr-aprovado-1.png`, `gco-pr-aprovado-2.png`
> Estes mesmos prints atendem o registro **REV-AASPCNJ01-001** (revisão por pares / VV2).

---

## 4. VV / REL-VV — Verificação e Validação

### 4.1 Defeitos registrados (REL-VV §3 — BUG-01 a BUG-09)
**Evidência a trazer:** prints (ou export) dos cards dos 9 defeitos no ClickUp/Azure Boards, mostrando título, descrição, status (resolvido) e responsável. Pelo menos os críticos (BUG-05/06 — fila de 137 mil itens).
**Onde:** ClickUp → busca pelos cards de bug; ou Azure Boards.
**Arquivo:** `vv-bugs-clickup.csv` (ou prints `vv-bug-05-fila.png` etc.)

### 4.2 Fluxo de captura validado (VV §6 / REL-VV §4 — CA01..CA07 · US-16)
**Evidência a trazer (prints do banco/Elasticsearch para um processo de exemplo):**
- `ProcessoCaptura` com `CodigoProcessoCapturaStatus = 3` (Capturado) — **CA01**
- `ProcessoCapturaLogin` com sucesso por instância (`CodigoProcessoCapturaResposta = 1`) — **CA02**
- `ProcessoCapturaMovimentacaoStatus` com `Ativo = 1` e `DataUltimaAtualizacao` — **CA03**
- documento indexado no Elasticsearch (capa, partes, advogados, andamentos) — **CA04** (print do Kibana/consulta)
- caso de **erro parcial**: uma instância com status 8 e o processo mantendo status 3 — **CA05**
**Onde:** SSMS (consultas nas tabelas) + Kibana/consulta ao índice.
**Arquivo:** `vv-ca01-processocaptura.png` … `vv-ca05-erro-parcial.png`

### 4.3 Desligamento nas APIs parceiras (CA06 · RF-04 · US-10)
**Evidência a trazer:** print do log de desligamento do NUP na parceira após captura via CNJ.
**Arquivo:** `vv-ca06-desligamento-parceira.png`

### 4.4 Segredo de justiça por instância (CA07 · RF-10 · US-13)
**Evidência a trazer:** print de `ProcessoCapturaLogin` com o campo `Segredo` setado em uma instância, sem afetar as demais do mesmo processo.
**Arquivo:** `vv-ca07-segredo-instancia.png`

### 4.5 Retry de webhook (US-17 · RNF-02)
**Evidência a trazer:** print do trecho de código do retry e/ou log de reenvio.
**Arquivo:** `vv-retry-webhook.png`

---

## 5. RASTR / REQ — Rastreabilidade requisito → código → teste

### 5.1 Vínculo card ↔ código (REQ4)
**Evidência a trazer:** evidência de que branches/commits/PRs referenciam o card/história (ex.: branch `feature/256-captura-cnj`, ou commit citando o card do ClickUp).
**Onde:** `Azure DevOps → Repos → Branches/Commits → print`. Alternativa: `git log --oneline -30`.
**Arquivo:** `req4-rastreabilidade-branches.png`

---

## 6. MED — Medição

### 6.1 Esforço em horas (MED §3 — 586 est. / ~624 real)
**Evidência a trazer:** relatório de horas do ClickUp por atividade/fase dos projetos **id 213 (EPROC/ESAJ)** e **id 256 (CNJ)**.
**Onde:** ClickUp → Time tracking / relatório dos dois projetos → export CSV ou print.
**Arquivo:** `med-horas-clickup-213-256.csv`

### 6.2 Custo e economia (MED §4)
**O documento afirma:** Solucionário R$ 0,03/instância (~R$ 16.500/mês) → CNJ R$ 0,01/processo; economia ~R$ 14.670/mês.
**Evidência a trazer:** comprovação do custo (contrato/fatura da API CNJ e da Solucionário) e do volume (~550 mil instâncias / ~183 mil processos). **Parte disso o Abraão tem (contrato).**
**Arquivo:** `med-custo-cnj.pdf`, `med-volume-processos.png`

---

## 7. GDE — Decisão (fonte primária CNJ, 06–07/04/2026)

**Evidência a trazer:** registro do alinhamento técnico que formalizou a escolha da DataJud/CNJ (card/ata/convite do ClickUp ou e-mail de 06–07/04/2026).
**Arquivo:** `gde-alinhamento-cnj-0704.png`
> Mesmo print serve para a **ATA-AASPCNJ01-001** e para a integração do Levi Santos ao time (**CAP**).

---

## 8. CAP — Capacitação / transferência de conhecimento

**Evidência a trazer:** documentação técnica disponibilizada ao time (coleção Postman da API CNJ e registros de banco no Azure DevOps `/docs`) — print mostrando que está versionada e acessível.
**Arquivo:** `cap-docs-postman-repo.png` (pode reusar o `itp-postman-cnj.json`)

---

## 9. Prioridade máxima (se o prazo apertar)

| # | Item | Onde | Esforço |
|---|---|---|---|
| 1 | PRs aprovados (code review) — GCO/REV | Azure DevOps → Pull Requests | 5 min |
| 2 | Tag de baseline (v240) — GCO | Azure DevOps → Repos → Tags | 5 min |
| 3 | Captura OK: ProcessoCaptura status 3 + instância + Elasticsearch — VV (CA01–CA04) | Banco + Kibana | 15 min |
| 4 | Erro parcial por instância (CA05) e segredo por instância (CA07) — VV | Banco | 10 min |
| 5 | Bugs no ClickUp (BUG-05/06 da fila) — VV | ClickUp/Boards | 10 min |
| 6 | Fila RabbitMQ unificada — ITP | RabbitMQ Management | 5 min |
| 7 | Horas por fase (id 213 e 256) — MED | ClickUp → relatório | 10 min |

---

## 10. Como organizar e entregar

```
evidencias-tecnicas-aaspcnj/
├── PCP/
│   ├── pcp-arquitetura-diagrama.png
│   ├── pcp-schema-tabelas-controle.png
│   └── pcp-roteamento-codigofonteapi.png
├── ITP/
│   ├── itp-postman-cnj.json
│   ├── itp-rabbitmq-fila.png
│   ├── itp-webhook-indexacao.png
│   └── itp-pipeline-cicd.png
├── GCO/
│   ├── gco-branches-gitflow.png
│   ├── gco-tags-baseline.png
│   └── gco-pr-aprovado-1.png / -2.png
├── VV/
│   ├── vv-bugs-clickup.csv
│   ├── vv-ca01-processocaptura.png … vv-ca05-erro-parcial.png
│   ├── vv-ca06-desligamento-parceira.png
│   ├── vv-ca07-segredo-instancia.png
│   └── vv-retry-webhook.png
├── REQ/
│   └── req4-rastreabilidade-branches.png
├── MED/
│   ├── med-horas-clickup-213-256.csv
│   └── med-custo-cnj.pdf
└── GDE-CAP/
    └── gde-alinhamento-cnj-0704.png
```

Qualquer dúvida sobre onde encontrar um item, me chama. Conforme as evidências chegarem, eu anexo cada uma ao registro correspondente (PCP, ITP, VV, GCO, MED…).
