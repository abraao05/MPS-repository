# Tarefas de Captura de Evidências — Tiago Nascimento
# Projeto Cadastro de Clientes (PROFARMA01)

| Campo | Valor |
|---|---|
| **Para** | Tiago Nascimento (Tech Lead / DevOps) |
| **De** | Abraão Oliveira |
| **Data** | 11/06/2026 |
| **Objetivo** | Capturar evidências das ferramentas para fechar os gaps MPS-SW identificados pelo consultor Renato (ASR) |
| **Prazo sugerido** | 5 dias úteis |

---

## Como usar este documento

Cada item tem:
- **O arquivo esperado** — nome exato para salvar
- **Onde buscar** — ferramenta e caminho
- **Qual documento alimenta** — qual artefato MPS-SW recebe essa evidência

Ao capturar, enviar os arquivos organizados em pastas por ferramenta (ver §5).

---

## Divisão de responsabilidades

| Responsável | O que tem |
|---|---|
| **Abraão** | Print do WhatsApp 17/07/2025 com Armando Junior (aprovação design); e-mails de status report Out/2025; e-mails de aceite de sprint da Helena Moreira |
| **Tiago** | Acesso ao Azure DevOps, Jira, Datadog, GanttPro — tudo listado abaixo |

---

## 1. GanttPro — Planejamento do projeto

### Tarefa G1 — Export do cronograma com fases e sprints

| Campo | Valor |
|---|---|
| **Link** | `https://app.ganttPro.com/shared/token/27dcf78b2c39382b705b2c7e15a192a46783fd0ea91b2c527893832abbebae88/1838981` |
| **O que capturar** | Export PDF ou PNG do Gantt mostrando as 4 fases (Fase 1–4), com datas e, se possível, recursos/duração por tarefa |
| **Arquivo esperado** | `ganttPro-cronograma-fases-profarma.pdf` |
| **Documentos alimentados** | RAC-PROFARMA01-001 §2 (planejado vs. realizado), MED-PROFARMA01-001 §1 (SPI) |
| **Gaps fechados** | GPR3 (estimativas de dimensão), GPR4 (estimativas de esforço) |

---

## 2. Azure DevOps — Repositório `loja-backend`

### Tarefa AD1 — Estrutura de pastas (Clean Architecture)

| Campo | Valor |
|---|---|
| **Onde** | `profarma.visualstudio.com/rede-d1000/` → Repos → `loja-backend` → `src/` |
| **O que capturar** | Print da estrutura de pastas mostrando as 4 camadas: `Domain/`, `Application/`, `Infrastructure/`, `API/` |
| **Arquivo esperado** | `azuredevops-repo-estrutura-clean-arch.png` |
| **Documentos alimentados** | PCP-PROFARMA01-001 §2 (componentes), REL-VV-PROFARMA01-001 §2 |
| **Gaps fechados** | PCP3 (produto desenvolvido conforme o design) |

### Tarefa AD2 — Resultado do pipeline com cobertura de testes

| Campo | Valor |
|---|---|
| **Onde** | Azure DevOps → Pipelines → último run de `loja-backend` → aba **Tests** |
| **O que capturar** | Print mostrando: total de testes (273), % de cobertura (84%), resultado passed/failed |
| **Arquivo esperado** | `azuredevops-pipeline-cobertura-273-testes.png` |
| **Documentos alimentados** | REL-VV-PROFARMA01-001 §3 (testes unitários), MED-PROFARMA01-001 §2 |
| **Gaps fechados** | PCP3 (produto desenvolvido conforme o design), VV4/VV5 (resultados de testes) |

### Tarefa AD3 — Tags de baseline no repositório

| Campo | Valor |
|---|---|
| **Onde** | Azure DevOps → Repos → `loja-backend` → **Tags** |
| **O que capturar** | Print da lista de tags mostrando `25.12.1.1` e `26.1.1.1` com data e hash do commit |
| **Arquivo esperado** | `azuredevops-tags-baselines-2512-e-2611.png` |
| **Documentos alimentados** | GCO-PROFARMA01-001 §4 (baselines BL-01 e BL-02) |
| **Gaps fechados** | GCO3 (baselines geradas nos projetos) |

**Alternativa via terminal (se preferir):**
```bash
git tag -l --sort=-version:refname | head -10
git show 26.1.1.1 --stat | head -5
```
Salvar output como `git-tags-baselines.txt`.

### Tarefa AD4 — Pull Requests aprovados (code review)

| Campo | Valor |
|---|---|
| **Onde** | Azure DevOps → Repos → Pull Requests → filtrar **Completed** |
| **O que capturar** | Print de 2 a 3 PRs mostrando: autor, revisor, status "Approved", comentários e data de merge. Um deles deve ter aprovação do Armando Junior. |
| **Arquivos esperados** | `azuredevops-pr-aprovado-01.png`, `azuredevops-pr-aprovado-02.png` |
| **Documentos alimentados** | REV-PROFARMA01-001, REL-VV-PROFARMA01-001 §3 |
| **Gaps fechados** | VV2 (aprovações de pull requests / code review) |

### Tarefa AD5 — Nomenclatura de branches com rastreabilidade ao Jira

| Campo | Valor |
|---|---|
| **Onde** | Azure DevOps → Repos → `loja-backend` → **Branches** (ou qualquer PR com branch linkado) |
| **O que capturar** | Print da lista de branches mostrando a convenção `feature/PROFARMA-NNN-descricao` OU print de 1 commit que referencia ID do Jira no comentário |
| **Arquivo esperado** | `azuredevops-branches-nomenclatura-jira.png` |
| **Documentos alimentados** | GCO-PROFARMA01-001 §3 (changelog/rastreabilidade), REQ-PROFARMA01-001 §8 |
| **Gaps fechados** | REQ4 (rastreabilidade entre requisitos e código) |

### Tarefa AD6 — Ambiente de homologação no AKS / Azure Portal

| Campo | Valor |
|---|---|
| **Onde** | Portal Azure → Kubernetes Service → cluster de homologação (`d1000_homologacao`) → Workloads |
| **O que capturar** | Print mostrando os pods/serviços em status **Running** (especialmente `clientes-api`) |
| **Arquivo esperado** | `azure-aks-homologacao-pods-running.png` |
| **Documentos alimentados** | ITP-PROFARMA01-001 §4 (ambiente de homologação), REL-VV-PROFARMA01-001 §4 |
| **Gaps fechados** | ITP2, ITP4, ITP5 (integrações prontas para testes em homologação), VV3 (ambiente de testes e homologação) |

### Tarefa AD7 — Pipeline com stage de deploy para homologação

| Campo | Valor |
|---|---|
| **Onde** | Azure DevOps → Pipelines → pipeline do `loja-backend` → ver estágios (stages) |
| **O que capturar** | Print do pipeline mostrando os stages: `build → test → deploy-homologacao` (ou equivalente) |
| **Arquivo esperado** | `azuredevops-pipeline-stages-deploy-hom.png` |
| **Documentos alimentados** | ITP-PROFARMA01-001 §4, REL-VV-PROFARMA01-001 §4 |
| **Gaps fechados** | VV3 (ambientes de testes e homologação) |

---

## 3. Jira — Projeto PROFARMA

### Tarefa J1 — Sprint backlog com story points

| Campo | Valor |
|---|---|
| **Onde** | Jira → Board → Backlog → selecionar todos os sprints → **Export to CSV** |
| **O que capturar** | CSV com colunas: ID da história, título, sprint, story points, status |
| **Arquivo esperado** | `jira-backlog-sprints-story-points.csv` |
| **Documentos alimentados** | RAC-PROFARMA01-001 §2, MED-PROFARMA01-001 §1 |
| **Gaps fechados** | GPR3, GPR4 (complementa o GanttPro — se GanttPro já cobrir, este é opcional) |

### Tarefa J2 — Histórias com critérios de aceite (3 a 5 exemplos)

| Campo | Valor |
|---|---|
| **Onde** | Jira → Issues → abrir histórias de Sprint 4 em diante |
| **O que capturar** | Print de 3 a 5 histórias mostrando: título, descrição, critérios de aceite, sprint e status |
| **Arquivo esperado** | `jira-historia-criterios-aceite-01.png`, `...02.png`, `...03.png` |
| **Documentos alimentados** | REQ-PROFARMA01-001 §3 (refinamento) |
| **Gaps fechados** | REQ2+ (refinamento dos requisitos) |

### Tarefa J3 — Bugs registrados na homologação

| Campo | Valor |
|---|---|
| **Onde** | Jira → Issues → filtrar por tipo **Bug** + projeto PROFARMA → Export to CSV OU prints individuais |
| **O que capturar** | Export ou prints dos bugs: BAL-B03, PDV-B01, CC-B01, PBI-26, API-B01, BAL-B01, BAL-B02 — mostrando título, severidade, responsável e status (resolved/done) |
| **Arquivos esperados** | `jira-bugs-homologacao.csv` OU `jira-bug-bal-b03.png`, `jira-bug-pdv-b01.png` (os S1 são prioritários) |
| **Documentos alimentados** | REL-VV-PROFARMA01-001 §5 (registro de defeitos), CTQ-PROFARMA01-001 §9.1 |
| **Gaps fechados** | VV1 (resultados de testes e registro de bugs), ITP3 (cenários de testes de integração executados) |

---

## 4. Datadog — Monitoramento pós-implantação

### Tarefa DD1 — Dashboard APM com monitoramento ativo (pós go-live)

| Campo | Valor |
|---|---|
| **Onde** | Datadog → APM → Services → `clientes-api` → trocar período para **últimas semanas** (Janeiro/2026 em diante) |
| **O que capturar** | Print do dashboard APM mostrando: nome do serviço (`clientes-api`), latência p95, throughput e data recente |
| **Arquivo esperado** | `datadog-apm-clientes-api-pos-golive.png` |
| **Documentos alimentados** | MED-PROFARMA01-001 §2 (p95=142ms, uptime ≥ 99,5%), ATA-PROFARMA01-002 §3 |
| **Gaps fechados** | GPR16 (monitoramento pós-implantação) |

---

## 5. Swagger/OpenAPI — Documentação da API

### Tarefa SW1 — Export da documentação OpenAPI

| Campo | Valor |
|---|---|
| **Onde** | Ambiente de homologação: `https://<url-api>/swagger` → print OU `https://<url-api>/swagger/v1/swagger.json` → salvar |
| **O que capturar** | Print da UI Swagger mostrando os endpoints OU arquivo `swagger.json` exportado |
| **Arquivo esperado** | `api-swagger-ui-screenshot.png` OU `api-documentation-openapi.json` |
| **Documentos alimentados** | ITP-PROFARMA01-001 §3 (interfaces externas), REQ-PROFARMA01-001 §6 (endpoints) |
| **Gaps fechados** | ITP6 (documentação dos componentes entregues) |

---

## 6. Organização dos arquivos para entrega

Entregar os arquivos na seguinte estrutura de pasta:

```
evidencias-profarma-tiago/
├── ganttPro/
│   └── ganttPro-cronograma-fases-profarma.pdf          ← G1
├── azure-devops/
│   ├── azuredevops-repo-estrutura-clean-arch.png        ← AD1
│   ├── azuredevops-pipeline-cobertura-273-testes.png    ← AD2
│   ├── azuredevops-tags-baselines-2512-e-2611.png       ← AD3
│   ├── azuredevops-pr-aprovado-01.png                   ← AD4
│   ├── azuredevops-pr-aprovado-02.png                   ← AD4
│   ├── azuredevops-branches-nomenclatura-jira.png       ← AD5
│   ├── azure-aks-homologacao-pods-running.png           ← AD6
│   └── azuredevops-pipeline-stages-deploy-hom.png       ← AD7
├── jira/
│   ├── jira-backlog-sprints-story-points.csv            ← J1
│   ├── jira-historia-criterios-aceite-01.png            ← J2
│   ├── jira-historia-criterios-aceite-02.png            ← J2
│   ├── jira-historia-criterios-aceite-03.png            ← J2
│   └── jira-bugs-homologacao.csv                        ← J3
├── datadog/
│   └── datadog-apm-clientes-api-pos-golive.png          ← DD1
└── swagger/
    └── api-swagger-ui-screenshot.png                    ← SW1
```

---

## 7. Prioridade máxima (se o prazo for curto)

Foco nos 6 itens de maior peso. O resto pode vir numa segunda rodada.

| # | Tarefa | Tempo estimado | Gap fechado |
|---|---|---|---|
| 1 | **AD3** — Tags de baseline (25.12.1.1 e 26.1.1.1) | 5 min | GCO3 |
| 2 | **AD4** — 2 PRs aprovados com code review | 5 min | VV2 |
| 3 | **AD2** — Pipeline com 273 testes e 84% cobertura | 5 min | PCP3, VV4/5 |
| 4 | **AD6** — AKS homologação com pods Running | 5 min | ITP2/4/5, VV3 |
| 5 | **J3** — Bugs no Jira (BAL-B03 e PDV-B01 são S1 — obrigatórios) | 10 min | VV1, ITP3 |
| 6 | **DD1** — Datadog APM pós go-live | 5 min | GPR16 |

---

## 8. O que o Abraão vai fazer com as evidências

Após receber os arquivos, Abraão vai:

| Evidência | Onde vai no documento |
|---|---|
| AD3 — Tags | GCO-PROFARMA01-001 §4: confirmar BL-01 e BL-02 com data e hash reais |
| AD4 — PRs aprovados | REV-PROFARMA01-001 §4 e REL-VV-PROFARMA01-001 §3: linkar prints como evidência física |
| AD2 — Pipeline/cobertura | REL-VV-PROFARMA01-001 §3: confirmar 273 cenários e 84% de cobertura |
| AD6/AD7 — AKS | ITP-PROFARMA01-001 §4: confirmar ambiente d1000_homologacao ativo |
| J3 — Bugs | REL-VV-PROFARMA01-001 §5: confirmar IDs, datas e severidades dos defeitos |
| DD1 — Datadog | MED-PROFARMA01-001 §2: confirmar p95 e uptime com dados reais recentes |
| G1 — GanttPro | RAC-PROFARMA01-001 §2: confirmar datas planejadas vs. realizadas por fase |
| SW1 — Swagger | ITP-PROFARMA01-001 §3: referenciar documentação da API como entregável |
