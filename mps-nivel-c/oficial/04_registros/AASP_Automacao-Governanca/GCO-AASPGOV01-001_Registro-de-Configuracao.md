# Registro de Gerência de Configuração — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | GCO-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsável GCO / DevOps** | Lucas Batista (com o Gerente de Projeto, Abraão Oliveira) |
| **Processo MPS-SW** | GCO (evidência de projeto) · PLA-GCO-001 · GUIA-GCO-001 |

---

## 1. Ambiente e plataforma

| Item | Descrição |
|---|---|
| Plataforma de desenvolvimento | .NET 8 LTS (C#) — estrutura em camadas Core, Infrastructure, App |
| Repositório e controle de versão | Azure DevOps — GitFlow (`main`, `develop`, `feature/*`, `hotfix/*`) |
| CI/CD | Azure Pipelines — build automático em push para `develop` e `main` |
| Runtime de produção | Azure Scheduled Job (execução agendada, não supervisionada) |
| Ambientes | Desenvolvimento (local) · Homologação (Azure Scheduler staging) · Produção (Azure Scheduler prod) |
| Gestão de segredos | Azure Key Vault (RNF06) — sem hardcode de credenciais no código |

## 2. Itens de configuração (IC)

| IC | Item de configuração | Descrição | Tipo |
|---|---|---|---|
| IC-01 | SensrJiraSync | Código-fonte completo da solução (.NET 8) | Software |
| IC-02 | `appsettings.json` | Configuração de ambiente (DeveloperConfig, ProjectConfig, Azure) | Configuração |
| IC-03 | `azure-pipelines.yml` | Pipeline de CI/CD do Azure DevOps | Configuração |
| IC-04 | Contrato API Sensr | Swagger/OpenAPI — endpoints de autenticação e atividades | Documentação |
| IC-05 | Contrato API Jira | OpenAPI v3 — Issues, Transitions, Epics, Subtasks | Documentação |
| IC-06 | GEST-AASPGOV01.xlsx | Planilha de gestão do projeto (9 abas) | Gerência |

## 3. Controle de versão e branches

GitFlow no Azure DevOps. Merge de `feature/*` e `bugfix/*` para `develop` exige no mínimo 1 revisor além do autor e build de CI verde (ver REV-AASPGOV01-001). Releases promovidas de `develop` para `main` com tag de baseline.

## 4. Baselines estabelecidas

| Baseline | Tag Git | Data | Descrição |
|---|---|---|---|
| BL-DEV-001 | `v0.9.0` | 20/05/2026 | Fim do desenvolvimento — entrou em homologação |
| BL-HOM-001 | `v1.0.0-rc.1` | 29/05/2026 | Release candidate validado pelo Sponsor (ATA-AASPGOV01-003) |
| BL-PROD-001 | `v1.0.0` | 02/06/2026 | Versão de produção — aceite formal em TAE-AASPGOV01-001 |

## 5. Gestão de mudanças

Escopo fixo desde o TAP-AASPGOV01-001; qualquer adição exigiria Change Request formal com aprovação do Patrocinador (R03). **Não houve mudanças de escopo** — apenas correções de defeitos na homologação (BUG-01 a BUG-05), integradas via Pull Request (PR-16 a PR-20). A promoção entre ambientes segue o pipeline de CI/CD com tag de baseline.

## 6. Auditoria de configuração

| Item verificado | Resultado | Observação |
|---|---|---|
| ICs identificados e controlados (IC-01 a IC-06) | ✅ Conforme | Código, configuração, contratos de API e planilha de gestão versionados/controlados |
| Baselines estabelecidas nos marcos | ✅ Conforme | BL-DEV-001, BL-HOM-001, BL-PROD-001 com tags `v0.9.0`, `v1.0.0-rc.1`, `v1.0.0` |
| Credenciais não expostas em código/logs | ✅ Conforme | Azure Key Vault (RNF06) |
| Merges revisados antes da integração | ✅ Conforme | PR com mínimo 1 revisor além do autor (REV-AASPGOV01-001) |
| ICs íntegros e consistentes com os documentos | ✅ Conforme | Verificado na auditoria de GQA (GQA-AASPGOV01-001, itens GCO-1/2/3) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de configuração consolidado a partir do INTAKE-AASPGOV01 (14/06/2026), Bloco 6. |
