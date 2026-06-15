# Registro de Gerência de Configuração — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | GCO-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsável GCO** | Cezar Hiraki Velazquez (Gerente de Projeto / Tech Lead) |
| **Processo MPS-SW** | GCO (evidência de projeto) |

---

## 1. Objetivo

Registrar o gerenciamento de configuração do projeto: itens de configuração (ICs), estratégia de controle de versão, branches e gestão de mudanças. Conforme ADAP-AASP-GOV-001, a Gerência de Configuração foi mantida integralmente, com controle de versão via Azure DevOps e GitFlow.

## 2. Itens sob controle de configuração

| ID | Item de configuração | Tipo | Repositório / Localização |
|---|---|---|---|
| IC-01 | `SensrJiraSync.Core` | Código-fonte (.NET 8) | Azure DevOps — repositório SensrJiraSync |
| IC-02 | `SensrJiraSync.Infrastructure` | Código-fonte (.NET 8) | Azure DevOps — repositório SensrJiraSync |
| IC-03 | `SensrJiraSync.App` | Código-fonte (.NET 8) | Azure DevOps — repositório SensrJiraSync |
| IC-04 | `appsettings.json` | Arquivo de configuração | Gerenciado fora do repositório; fornecido ao Azure de forma segura |
| IC-05 | Executável publicado | Artefato de implantação | Azure — ambiente de hospedagem do Scheduled Job |

## 3. Controle de versão e branches

GitFlow no Azure DevOps:

| Branch | Papel |
|---|---|
| `main` | Produção |
| `develop` | Integração |
| `feature/*` | Funcionalidades |
| `bugfix/*` | Correções |

- O merge para `develop` exige revisão de ao menos um membro além do autor (ver REV-AASP-GOV-001).
- O `appsettings.json` é mantido **fora do repositório** para proteger credenciais (RNF05).

## 4. Gestão de mudanças

- Mudanças de escopo formalizadas por alinhamento entre o time. O escopo permaneceu fixo desde a abertura; não houve solicitações de mudança de escopo (apenas correções de defeitos na Fase 4).
- A implantação no Azure é realizada manualmente após a validação em homologação, com substituição do artefato anterior e verificação do agendamento.

## 5. Auditoria de configuração

| Item verificado | Resultado | Observação |
|---|---|---|
| ICs versionados no Azure DevOps | ✅ Conforme | IC-01 a IC-03 no repositório SensrJiraSync |
| Credenciais fora do código e dos logs | ✅ Conforme | `appsettings.json` fornecido ao Azure de forma segura (RNF05) |
| Merges revisados antes da integração | ✅ Conforme | PR com no mínimo 1 revisor além do autor (ver REV-AASP-GOV-001) |
| Artefato de implantação verificado no agendamento | ✅ Conforme | Substituição do artefato e verificação do Azure Scheduled Job |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de configuração consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
