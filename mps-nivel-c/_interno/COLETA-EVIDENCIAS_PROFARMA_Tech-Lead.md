# Coleta de Evidências Técnicas — Projeto Cadastro de Clientes (PROFARMA)
# Solicitação ao Tech Lead

| Campo | Valor |
|---|---|
| **Para** | Tiago Nascimento (Tech Lead) |
| **De** | Abraão Oliveira (GP / Responsável MPS-SW) |
| **Data** | 11/06/2026 |
| **Ref.** | Avaliação MPS-SW Nível C — evidências técnicas do projeto PROFARMA01 |
| **Prazo sugerido** | 5 dias úteis |

---

## Contexto

O consultor da ASR Consultoria apontou que os documentos do projeto estão bem estruturados, mas há **evidências técnicas que precisam ser complementadas com capturas diretas das ferramentas** (Azure DevOps, Datadog, GMUD). Esses itens não podem ser gerados retroativamente — precisam vir do projeto real.

Precisamos da sua ajuda para coletar e organizar essas evidências antes da avaliação.

---

## O que precisa ser coletado

### 1. Azure DevOps — Pipeline CI/CD

**Por que é necessário:** o plano e os documentos descrevem o pipeline, mas o avaliador quer ver que ele realmente rodou com status verde.

**O que coletar:**

| # | Item | Como exportar / capturar |
|---|---|---|
| 1.1 | Print de um run de pipeline bem-sucedido no branch `main` ou `release/*` | Azure DevOps → Pipelines → `loja-backend` → último run verde → Print da tela com todas as etapas (Build / Test / Publish) em verde |
| 1.2 | Print do sumário de testes unitários dentro do pipeline | No mesmo run → aba "Tests" → print mostrando 273 testes passando e cobertura ≥ 80% |
| 1.3 | Print do histórico de runs dos últimos 3 sprints (lista com status) | Pipelines → `loja-backend` → lista de runs → print mostrando datas e status |

---

### 2. Azure DevOps — Pull Requests e Revisão de Código

**Por que é necessário:** evidência de peer review (processo VV/GCO). Os documentos mencionam PRs aprovados — o avaliador quer ver ao menos 2 ou 3 exemplos reais.

**O que coletar:**

| # | Item | Como exportar / capturar |
|---|---|---|
| 2.1 | Print de um PR com aprovação do Armando Junior | Repos → `loja-backend` → Pull Requests → buscar PRs de mudança arquitetural (ex.: outbox, VTEX) → print mostrando aprovador, comentários e status "Completed" |
| 2.2 | Print de um PR de funcionalidade com aprovação de pelo menos 1 revisor | Qualquer PR de feature — o importante é ver: autor, revisor, aprovação, data de merge |
| 2.3 | Print do PR 10684 (última correção S2 antes do aceite) | Repos → PR 10684 → print completo com título, commits e aprovação |

---

### 3. Azure DevOps — Tags e Baselines

**Por que é necessário:** evidência de controle de configuração (GCO). As tags `25.12.1.1` e `26.1.1.1` são as baselines declaradas — precisamos comprovar que existem no repositório.

**O que coletar:**

| # | Item | Como exportar / capturar |
|---|---|---|
| 3.1 | Print da lista de tags do repositório `loja-backend` | Repos → `loja-backend` → Tags → print mostrando as tags com data e commit associado |
| 3.2 | Print da tag `26.1.1.1` (baseline do piloto) | Clicar na tag → print mostrando hash do commit, data e autor |
| 3.3 | Print da tag `25.12.1.1` (baseline de homologação) | Idem |

**Alternativa via Git (se preferir linha de comando):**
```bash
git log --tags --simplify-by-decoration --pretty="format:%ai %d %H" | grep -E "25\.|26\."
```
Copiar o output e salvar como `git-tags-baseline.txt`.

---

### 4. Azure DevOps — Jira / Boards (Sprint Backlog e Bugs)

**Por que é necessário:** evidência de rastreabilidade de histórias e gestão de defeitos.

**O que coletar:**

| # | Item | Como exportar / capturar |
|---|---|---|
| 4.1 | Export do board de um sprint da fase de homologação (Sprint 14–17) | Jira → Sprint → Export to CSV ou print do quadro Kanban/Scrum com colunas Done |
| 4.2 | Print do bug BAL-B03 ou PDV-B01 (S1) no Jira — mostrando abertura, assignee e resolução | Jira → Issues → buscar por BAL-B03 ou "sala de guerra" → print da issue completa |
| 4.3 | Print do PBI-26 (bug CC-B01 Call Center) | Jira ou Azure DevOps Work Items → PBI-26 → print com título, descrição, resolução |
| 4.4 | Velocity chart ou burn-down de qualquer sprint (evidência de monitoramento) | Jira → Reports → Velocity Chart → print |

---

### 5. Datadog — Performance e Monitoramento

**Por que é necessário:** os resultados de performance (p95 = 142ms, disponibilidade ≥ 99,5%) estão declarados nos documentos. O avaliador quer ver a evidência do dado.

**O que coletar:**

| # | Item | Como exportar / capturar |
|---|---|---|
| 5.1 | Dashboard APM — latência p95 do endpoint `GET /clientes/{cpf}` | Datadog → APM → Services → `clientes-api` → aba Latency → filtrar por p95 → print mostrando o valor ≤ 200ms |
| 5.2 | Dashboard de disponibilidade (uptime ≥ 99,5%) | Datadog → Monitors ou SLOs → print mostrando uptime no período de piloto (Jan/2026) |
| 5.3 | Print de um alerta configurado (ex.: alerta de latência ou erro 5xx) | Datadog → Monitors → listar os alertas ativos do projeto → print da lista |
| 5.4 | Screenshot do dashboard principal do projeto (visão geral APM) | Datadog → Dashboards → dashboard do projeto → print mostrando request rate, latência, errors |

---

### 6. Registro de GMUD

**Por que é necessário:** o documento GCO e o ITP citam o GMUD 2624117 como aprovação do deploy para produção. O avaliador pode pedir o comprovante.

**O que coletar:**

| # | Item | Como exportar / capturar |
|---|---|---|
| 6.1 | Print ou PDF do GMUD 2624117 | Sistema de GMUD da D1000 (Rede D1000 ops) → buscar GMUD 2624117 → print ou exportar PDF mostrando: número, solicitante, data de aprovação, janela de deploy e status |
| 6.2 | Se não tiver acesso direto | Solicitar ao Fagner Pereira (Operações D1000) um print/PDF do registro |

---

### 7. E-mail de Aceite Formal

**Por que é necessário:** o aceite de Humberto Erler está declarado nos documentos (ATA-PROFARMA01-002 e TAE), mas o avaliador quer o e-mail original de domínio externo (@profarma.com.br ou @d1000.com.br) como evidência.

**O que coletar:**

| # | Item | Como exportar / capturar |
|---|---|---|
| 7.1 | E-mail de aceite enviado por Humberto Erler em 29/01/2026 | Abraão — verificar na caixa do seu e-mail corporativo (@timeware.com.br) por e-mail de humberto.erler@... com data 29/01/2026 → exportar como PDF (Gmail: Print → Save as PDF) |
| 7.2 | Alternativamente: e-mail de confirmação via Teams | Se o aceite foi pelo Teams, tirar print da conversa mostrando remetente, data e texto de aceite |

---

### 8. Azure Infrastructure — Evidências de Ambiente

**Por que é necessário:** confirmar que a infraestrutura foi provisionada conforme descrito (AKS, PostgreSQL, Key Vault).

**O que coletar (screenshots rápidos do portal Azure):**

| # | Item | Como exportar / capturar |
|---|---|---|
| 8.1 | AKS — cluster em execução | Portal Azure → Kubernetes Service → cluster D1000 → print mostrando status "Running" e número de nós |
| 8.2 | PostgreSQL Flexible Server | Portal Azure → Azure Database for PostgreSQL → instância D1000 → print mostrando status, tier e região |
| 8.3 | Azure Key Vault em uso | Portal Azure → Key Vault → instância D1000 → print mostrando secrets cadastrados (nomes, sem valores) |
| 8.4 | Azure Service Bus (fila Propz) | Portal Azure → Service Bus → namespace D1000 → print mostrando as filas/tópicos configurados |

---

## Como organizar e entregar

**Formato:** uma pasta (zip ou OneDrive) com subpastas nomeadas conforme os grupos acima:

```
evidencias-tecnicas-profarma/
├── 01_azure-devops-pipeline/
│   ├── pipeline-run-verde.png
│   ├── test-summary-273.png
│   └── pipeline-historico.png
├── 02_pull-requests/
│   ├── pr-armando-aprovacao.png
│   ├── pr-feature-exemplo.png
│   └── pr-10684.png
├── 03_tags-baselines/
│   ├── tags-lista.png
│   ├── tag-26.1.1.1.png
│   └── tag-25.12.1.1.png
├── 04_jira-backlog/
│   ├── sprint-board.png
│   ├── bug-bal-b03.png
│   └── pbi-26.png
├── 05_datadog/
│   ├── apm-latencia-p95.png
│   ├── uptime-sla.png
│   └── alertas.png
├── 06_gmud/
│   └── gmud-2624117.pdf
├── 07_aceite-formal/
│   └── email-aceite-humberto-29jan2026.pdf
└── 08_azure-infra/
    ├── aks-running.png
    ├── postgresql.png
    ├── keyvault.png
    └── servicebus.png
```

**Prioridade:** se o prazo for curto, priorize nessa ordem:
1. **Alta:** pipeline verde com testes (1.1 + 1.2), PR com aprovação do Armando (2.1), e-mail de aceite (7.1)
2. **Média:** tags (3.x), Datadog p95 (5.1), GMUD (6.1)
3. **Baixa:** Jira boards (4.x), infra Azure (8.x)

---

## Dúvidas

Qualquer dúvida sobre o que exatamente tirar print ou exportar, me chama. O avaliador da ASR está focado principalmente em ver que o **pipeline CI rodou de verdade**, que houve **revisão de código real**, e que os **dados de performance existem no Datadog**.
