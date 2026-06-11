# Coleta de Evidências Técnicas — Projeto Cadastro de Clientes (PROFARMA)
# Solicitação ao Tech Lead

| Campo | Valor |
|---|---|
| **Para** | Tiago Nascimento (Tech Lead) |
| **De** | Abraão Oliveira (GP / Responsável MPS-SW) |
| **Data** | 11/06/2026 |
| **Avaliador ASR** | Renato Ferraz Machado |
| **Ref.** | Relatório de Ajustes 2024 — itens REQUERIDO referentes ao projeto PROFARMA01 |
| **Prazo sugerido** | 5 dias úteis |

---

## Contexto

O consultor Renato Ferraz Machado (ASR Consultoria) identificou uma série de itens REQUERIDO que não puderam ser evidenciados na avaliação anterior. Para cada item abaixo, está indicado o **código do processo** que ele citou, **o que faltou** e **exatamente o que você precisa exportar ou capturar**.

Os documentos de texto do projeto (PLA, REQ, PCP, VV, GCO etc.) já estão prontos. O que falta é a **evidência das ferramentas reais**: Jira, Azure DevOps, Datadog.

---

## 1. Gerência de Projetos (GPR)

### GPR3 — Estimativas de dimensão (distribuição nas sprints)

**O que o consultor disse:** "Não foi possível verificar as estimativas de dimensão (distribuição nas tarefas nas sprints)."

**O que precisa:**
- Export do Jira com as histórias/tarefas dos sprints, mostrando story points (ou pontos de função) por sprint
- Se não tiver export, print do backlog do Jira ordenado por sprint, com coluna de estimativa visível

**Como exportar no Jira:**
`Board → Backlog → selecionar todos os sprints → Export to CSV` (ou `Reports → Sprint Report` por cada sprint-chave)

**Arquivo sugerido:** `jira-backlog-sprints-estimativas.csv` ou prints por fase (Sprints 1–3, 4–7, 8–13, 14–19)

---

### GPR4 — Estimativas de esforço

**O que o consultor disse:** "Não foi possível evidenciar as estimativas de esforço."

**O que precisa:**
- Documento ou planilha que mostre o esforço estimado por sprint ou por história (em horas ou story points)
- Pode ser a própria planilha de planejamento de sprint, se existir

**Observação:** Se as estimativas estão só em story points no Jira, é suficiente. O importante é mostrar que existe racional de estimativa — não precisa ser horas exatas.

---

### GPR5 — Orçamento total em horas do projeto

**O que o consultor disse:** "Não foi possível evidenciar orçamento total em horas do projeto."

**O que precisa:**
- Um número: total de horas alocadas ao projeto (3 devs pleno × N horas/mês × N meses)
- Pode ser extraído do contrato, de uma planilha interna ou calculado a partir da alocação declarada no TAP/PLA

**Sugestão rápida:** `3 devs × 160h/mês × 10 meses = 4.800h` — mas confirme o número real com o Abraão, que tem o contrato.

---

### GPR15 — Status reports do projeto

**O que o consultor disse:** "Não foi possível evidenciar os dados de status report do projeto."

**O que precisa:**
- Os e-mails de status report que foram enviados durante o projeto (os de 08/10, 14/10, 17/10/2025 existem — o Abraão tem)
- Se houver outros, encaminhar todos

**Ação:** Abraão localiza os e-mails de status e exporta como PDF. Não é necessidade do Tech Lead — só de saber onde estão.

---

### GPR16 — Monitoramento pós-implantação

**O que o consultor disse:** "Não foi possível evidenciar o monitoramento pós-implantação."

**O que precisa:**
- Print do Datadog mostrando que o monitoramento continua ativo na loja 9 após o aceite (Janeiro/2026 em diante)
- Basta um print do dashboard APM com data recente e o serviço `clientes-api` aparecendo

**Como capturar:**
`Datadog → APM → Services → clientes-api → trocar período para últimas semanas → print`

---

## 2. Engenharia de Requisitos (REQ)

### REQ2+ — Refinamento dos requisitos

**O que o consultor disse:** "Não foi possível evidenciar o refinamento dos requisitos."

**O que precisa:**
- Print do Jira mostrando histórias com critérios de aceite escritos (os campos "Acceptance Criteria" ou descrição detalhada das histórias)
- Não precisa de todas — 3 a 5 histórias representativas são suficientes

**Como capturar:**
`Jira → Issues → abrir qualquer história de Sprint 4 em diante → print mostrando: título, descrição, critérios de aceite, sprint e status`

---

### REQ4 — Rastreabilidade entre requisitos e código

**O que o consultor disse:** "Não foi possível evidenciar a rastreabilidade entre requisitos e com código."

**O que precisa:**
- Evidência de que os commits ou branches referenciam o requisito/história do Jira
- Exemplo: se os branches se chamam `feature/PROFARMA-123-endpoint-head-cpf`, isso já é rastreabilidade

**Como capturar:**
- Print da lista de branches no Azure DevOps mostrando a convenção de nomenclatura
- OU print de um commit no Azure DevOps que referencia um item do Jira no comentário
- OU print de um PR linkado a uma história do Jira

**Alternativa via git:**
```bash
git log --oneline -30 | head -30
```
Se os commits referenciam IDs do Jira (ex.: `PFRM-45: implementa RF-09 HEAD endpoint`), salvar o output como `git-log-rastreabilidade.txt`.

---

### REQ7 — Aprovação formal dos requisitos pelo cliente

**O que o consultor disse:** "Não foi possível evidenciar a aprovação formal dos requisitos."

**O que precisa:**
- E-mail ou print de Teams onde o cliente (Armando Junior ou Helena Moreira) aprova formalmente os requisitos ou a entrega de uma sprint/fase
- O aceite de cada sprint por e-mail (Helena Moreira) já cobre isso — o Abraão tem esses e-mails

**Ação:** Abraão localiza os e-mails de aceite de sprint de Helena Moreira e exporta como PDF.

---

## 3. Projeto e Construção do Produto (PCP)

### PCP2 — Evidência da avaliação do design

**O que o consultor disse:** "Não foi possível evidenciar a avaliação do design. Evidenciar o aceite do design arquitetônico pelo time ou pelo líder técnico."

**O que precisa:**
- Print da revisão do design no Azure DevOps — especificamente o PR onde o Armando Junior aprovou a arquitetura em 09/05/2025
- Se não houver PR específico de design, um e-mail de Armando Junior aprovando a arquitetura serve

**Temos:** o documento REV-PROFARMA01-001 descreve a REV-001 (09/05/2025). O que falta é a evidência do sistema: o PR ou e-mail original.

**Como capturar:**
`Azure DevOps → Repos → Pull Requests → filtrar por data 09/05/2025 ou por "arquitetura/design" → print do PR com aprovação do Armando Junior`

---

### PCP3+ — Produto desenvolvido conforme o design

**O que o consultor disse:** "Não foi possível evidenciar que o produto foi desenvolvido conforme o design."

**O que precisa:**
- Print do resultado de cobertura de testes do pipeline (273 testes, 84% cobertura) — isso mostra que o código foi desenvolvido e testado
- Print da estrutura de pastas do repositório mostrando as camadas Clean Architecture (Domain, Application, Infrastructure, API)

**Como capturar:**
- Azure DevOps → Pipeline → último run → aba Tests → print
- Azure DevOps → Repos → `loja-backend/src/` → print da estrutura de pastas mostrando as 4 camadas

---

## 4. Integração do Produto (ITP)

### ITP2 / ITP4 / ITP5 — Integrações prontas para testes no ambiente de homologação

**O que o consultor disse:** "Não foi possível evidenciar que as integrações estão prontas para testes em ambiente de testes e homologação."

**O que precisa:**
- Print do ambiente `d1000_homologacao` no AKS mostrando os pods/serviços rodando
- Print de um teste de integração sendo executado (ou resultado) no ambiente de homologação

**Como capturar:**
`Portal Azure → Kubernetes Service → cluster de homologação → Workloads → print mostrando os pods da API em Running`

---

### ITP3 — Cenários de testes de integração no plano de testes

**O que o consultor disse:** "Não foi possível evidenciar os cenários de testes de integrações no plano de testes."

**Já temos:** CTQ-PROFARMA01-001 tem os cenários T-ITEC-01..04, T-VTEX-01..03, PROPZ-01..13 e REL-VV-PROFARMA01-001 tem os resultados.

**O que ainda falta:** evidência de que esses cenários foram executados no Jira (bugs linkados a cenários de teste). Se os bugs BAL-B03, PDV-B01 etc. estão registrados no Jira, mostrar esses tickets já evidencia a execução.

---

### ITP6 — Documentação do produto entregue (APIs, manuais)

**O que o consultor disse:** "Não foi possível evidenciar a documentação dos componentes entregues (documentos de APIs, manuais de instalação, etc.)."

**O que precisa:**
- Print ou export do Swagger/OpenAPI da API (a documentação automática do .NET que fica em `/swagger`)
- Se houver PDF ou Word com os endpoints exportado, esse arquivo

**Como capturar:**
- Acessar o ambiente de homologação em `https://<url-api>/swagger` → print ou salvar como PDF
- OU exportar o `openapi.json` do endpoint `/swagger/v1/swagger.json` e renomear para `api-documentation-openapi.json`

---

## 5. Verificação e Validação (VV)

### VV1 / VV4 / VV5 — Resultados de testes e registro de bugs

**O que o consultor disse:** "Não foi possível evidenciar os resultados de testes. Mostrar os resultados de testes ou bugs de testes no Jira."

**O que precisa:**
- Export ou print dos bugs registrados no Jira durante a homologação (BAL-B03, PDV-B01, CC-B01 — PBI-26, API-B01, BAL-B01, BAL-B02)
- Print de pelo menos 2 bugs mostrando: título, descrição, severidade, responsável, status (resolved/done)

**Como capturar:**
`Jira → Issues → filtrar por tipo Bug + projeto PROFARMA → Export to CSV` ou prints individuais dos bugs mais críticos

---

### VV2 — Aprovações de Pull Requests (code review)

**O que o consultor disse:** "Não foi possível evidenciar que as Pull Requests foram aprovadas. Evidência de code review."

**O que precisa:**
- Print de 2 a 3 PRs aprovados no Azure DevOps, mostrando: autor, revisor, aprovação, comentários e status merged
- Um dos PRs deve ter aprovação do Armando Junior (mudança arquitetural)

**Como capturar:**
`Azure DevOps → Repos → Pull Requests → filtrar Completed → print de 2 PRs`

---

### VV3 — Ambientes de testes e homologação

**O que o consultor disse:** "Não foi possível evidenciar os ambientes de testes e homologação."

**O que precisa:**
- Print do ambiente `d1000_homologacao` (AKS ou Azure Portal) mostrando o ambiente rodando
- Print do pipeline com o stage de deploy para homologação (se o pipeline tiver stages: build → test → deploy-hom)

---

## 6. Gerência de Configuração (GCO)

### GCO3 — Baselines geradas no projeto

**O que o consultor disse:** "Não foi possível evidenciar as baselines geradas nos projetos. Mostrar A EVIDÊNCIA DAS BASELINES GERADAS."

**O que precisa:**
- Print da lista de tags no repositório `loja-backend` mostrando `25.12.1.1` e `26.1.1.1` com datas

**Como capturar:**
`Azure DevOps → Repos → Tags → print mostrando as tags com data e commit`

**Alternativa via git:**
```bash
git tag -l --sort=-version:refname | head -10
git show 26.1.1.1 --stat | head -10
```

---

## 7. Resumo — O que é prioridade máxima

Se o prazo for curto, foque nestes 7 itens que têm maior peso na avaliação:

| # | Item | Onde buscar | Esforço |
|---|---|---|---|
| 1 | VV2 — PRs aprovados (code review) | Azure DevOps → Pull Requests | 5 min |
| 2 | GCO3 — Tags de baseline | Azure DevOps → Repos → Tags | 5 min |
| 3 | PCP2 — Aprovação de design pelo Armando Junior | Azure DevOps → PR de arquitetura / e-mail | 10 min |
| 4 | PCP3 — Cobertura de testes no pipeline | Azure DevOps → Pipeline → Tests | 5 min |
| 5 | ITP6 — Swagger/OpenAPI da API | `https://<url>/swagger` → print/PDF | 5 min |
| 6 | VV1 — Bugs no Jira (homologação) | Jira → Issues → tipo Bug | 10 min |
| 7 | GPR16 — Datadog pós-implantação | Datadog → APM → print com data atual | 5 min |

---

## 8. Como organizar e entregar

Pasta sugerida:

```
evidencias-tecnicas-profarma/
├── GPR/
│   ├── jira-backlog-sprints.csv          (GPR3/4)
│   ├── esforco-total-projeto.txt         (GPR5)
│   └── datadog-monitoramento-pos-go-live.png  (GPR16)
├── REQ/
│   ├── jira-historia-com-criterios-aceite.png (REQ2)
│   └── azuredevops-branches-nomenclatura.png  (REQ4)
├── PCP/
│   ├── pr-aprovacao-armando-design.png   (PCP2)
│   ├── pipeline-cobertura-273-testes.png (PCP3)
│   └── repo-estrutura-clean-arch.png     (PCP3)
├── ITP/
│   ├── aks-ambiente-homologacao.png      (ITP2/4/5)
│   └── api-swagger-openapi.pdf           (ITP6)
├── VV/
│   ├── pr-aprovado-1.png                 (VV2)
│   ├── pr-aprovado-2.png                 (VV2)
│   ├── jira-bugs-homologacao.csv         (VV1)
│   └── aks-ambiente-homologacao-vv3.png  (VV3)
└── GCO/
    └── azuredevops-tags-baselines.png    (GCO3)
```

Qualquer dúvida sobre onde encontrar algum item específico, me chama diretamente.
