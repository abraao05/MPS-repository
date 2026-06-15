# Estratégia de Integração — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | ITP-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |

---

## 1. Componentes a integrar (ITP 1)

| Componente | Descrição |
|---|---|
| SensrJiraSync (serviço) | Orquestra leitura no Sensr, transformação e gravação no Jira |
| API Sensr | Fonte dos dados — autenticação, atividades, sub-atividades e histórico |
| API Jira v3 | Destino — Epics, Tasks, Subtasks, transições e comentários |
| Azure Scheduler | Agendamento e execução periódica |
| Azure Key Vault | Provê as credenciais em tempo de execução (sem hardcode) |

## 2. Interfaces

| Interface | Entre | Tipo / contrato |
|---|---|---|
| Autenticação e leitura Sensr | SensrJiraSync ↔ API Sensr | REST; JWT por desenvolvedor |
| Gravação e sincronização Jira | SensrJiraSync ↔ API Jira v3 | REST; Basic Auth (e-mail + API Token); texto rico em ADF |
| Credenciais | SensrJiraSync ↔ Azure Key Vault | Managed Identity; sem secrets em código (RNF06) |
| Agendamento | Azure Scheduler ↔ Executável | Processo isolado; execução não supervisionada |

## 3. Estratégia e ordem de integração (ITP 1)

Integração entregue de forma incremental pelos sprints:

1. **S0–S1 — Autenticação e leitura:** contratos das APIs Sensr e Jira mapeados (Swagger/OpenAPI, IC-04/IC-05); fluxos de autenticação implementados (JWT no Sensr; Basic Auth no Jira).
2. **S1–S2 — Migração e transformação:** Epics/Tasks/Subtasks, conversão HTML→ADF, StatusMapper, histórico como comentários, idempotência por `#ID`.
3. **S2–S3 — Sincronização e robustez:** atualização incremental de status, paginação `nextPageToken`, isolamento de falha por desenvolvedor.

## 4. Ambiente de integração (ITP 2)

| Ambiente | Descrição |
|---|---|
| Desenvolvimento | Local (.NET 8 LTS) |
| Homologação | Azure Scheduler staging — testes nos ambientes reais do Sensr e do Jira |
| Produção | Azure Scheduler prod |

CI/CD via **Azure Pipelines** (build automático em push para `develop` e `main`); pipeline versionado como IC-03 (`azure-pipelines.yml`). Ver GCO-AASPGOV01-001.

## 5. Critérios de prontidão para integração (ITP 3)

- Code review aprovado (mínimo 1 revisor além do autor) antes do merge em `develop` (ver REV-AASPGOV01-001).
- Build de CI verde no Azure Pipelines.
- Tratamento de erro por desenvolvedor implementado (isolamento, CT-09).
- Verificação de existência por `#ID` antes de qualquer criação (idempotência, CT-02).

## 6. Testes do produto integrado (ITP 5)

O fluxo integrado (autenticação → leitura → transformação → criação/atualização no Jira) foi validado por testes de integração nos ambientes reais do Sensr e do Jira em homologação, cobrindo os 12 cenários (CT-01 a CT-12). Detalhes em VV-AASPGOV01-001 e REL-VV-AASPGOV01-001.

## 7. Entrega e implantação (ITP 6)

Entrega via baselines no Azure DevOps: BL-DEV-001 (v0.9.0, 20/05) → BL-HOM-001 (v1.0.0-rc.1, 29/05, validado pelo Sponsor em ATA-003) → BL-PROD-001 (v1.0.0, 02/06, aceite formal em TAE-AASPGOV01-001). Material de apoio: contratos de API (Swagger/OpenAPI) versionados como IC-04 e IC-05.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Estratégia de integração consolidada a partir do INTAKE-AASPGOV01 (14/06/2026), Blocos 6 e 9. |
