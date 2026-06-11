# Registro de Sessão de Treinamento — REG-CAP-011

| Campo | Valor |
|---|---|
| **Documento** | REG-CAP-011 |
| **Versão** | 1.0 |
| **Data** | 16/03/2026 |
| **Referência** | TPL-CAP-001 v1.0; PLA-CAP-001 §5; MAT-CAP-023 |

---

## 1. Identificação da Sessão

| Campo | Preenchimento |
|---|---|
| **Código do registro** | REG-CAP-011 |
| **Data da sessão** | 16/03/2026 e 18/03/2026 (duas sessões) |
| **Horário** | 09:00 — 13:00 (cada sessão) |
| **Modalidade** | Online |
| **Responsável pela sessão** | Flávio Fernandes (Azure Solutions Architect — AZ-305 / AZ-400) |

---

## 2. Conteúdo Coberto

| Campo | Preenchimento |
|---|---|
| **Trilha / Material** | MAT-CAP-023 §3 (módulo Azure); documentação Microsoft Learn (Azure API Management, Key Vault, Entra ID) |
| **Tipo** | Workshop técnico de aprofundamento (competência técnica específica) |
| **Motivação** | Preparação técnica da equipe para projetos de governança de APIs em Azure (capacitação prévia ao projeto Fundação Tecnológica GASMIG) |

**Tópicos abordados na sessão:**

- **Azure API Management (APIM):** arquitetura do gateway, produtos, APIs, versionamento (Versions/Revisions), políticas
- **Segurança:** Azure Key Vault e Named Values (sem segredos hard-coded); OAuth 2.0 com Microsoft Entra ID; política `validate-jwt`
- **Observabilidade:** Application Insights, Azure Monitor, dashboards, regras de alerta e Action Groups
- **Políticas de gateway:** CORS, `validate-content`, rate limiting, deprecation headers
- **IaC:** export de configuração como Bicep/ARM; versionamento no Azure DevOps

---

## 3. Lista de Participantes e Resultado

| Nome | Papel | Presente | Resultado | Evidência prática |
|---|---|---|---|---|
| Cézar (Velázquez) | Tech Lead | S | Concluído | Configurou APIM de laboratório com produto, API e política `validate-jwt` |
| Fernando Oliveira | Dev | S | Concluído | Configurou Named Values via Key Vault em ambiente de laboratório |
| Henry Komatsu | Dev | S | Concluído | Configurou política CORS e `validate-content` em API de laboratório |
| Rafael Cunha | DevOps | S | Concluído | Exportou configuração como Bicep e versionou no Azure DevOps |
| Raony Chagas | Dev | S | Concluído | Configurou dashboard no Application Insights e regra de alerta |

---

## 4. Observações e Pendências

Workshop técnico conduzido por Flávio Fernandes (Azure Solutions Architect Expert, certificações AZ-104/AZ-305/AZ-400), aproveitando competência técnica interna de alto nível. Capacitação prévia que habilitou a equipe a executar o projeto de governança de APIs da GASMIG (OS-001 e OS-002). Todos os participantes concluíram os exercícios práticos em ambiente de laboratório Azure. Sem pendências.

---

## 5. Assinatura

| Campo | Preenchimento |
|---|---|
| **Responsável pelo registro** | Time de Melhoria Contínua |
| **Data do registro** | 18/03/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 18/03/2026 | Time de Melhoria Contínua | Registro do workshop técnico de Azure API Management (preparação para projetos de governança de APIs) |
