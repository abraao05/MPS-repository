# Matriz de Rastreabilidade — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | RASTR-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |

---

## 1. Rastreabilidade Requisito × Sprint × Cenário de Teste × Critério de Aceite

Rastreabilidade bidirecional (REQ 4): de cada requisito ao sprint de implementação, ao cenário de teste que o exercita e ao critério de aceite que o valida (ver REQ-AASPGOV01-001 e VV-AASPGOV01-001).

| Requisito | Descrição resumida | Sprint | Cenário(s) de teste | Critério de aceite | Situação |
|---|---|---|---|---|---|
| RF01 | Autenticação multi-dev no Sensr (JWT) | S0 | CT-09 | CA07 | ✅ Verificado |
| RF02 | Autenticação no Jira (Basic Auth) | S0 | CT-01 | CA02 | ✅ Verificado |
| RF03 | Migração de projetos como Epics | S1 | CT-01 | CA02 | ✅ Verificado |
| RF04 | Migração de atividades como Tasks | S1 | CT-01 | CA02 | ✅ Verificado |
| RF05 | Migração de sub-atividades como Subtasks | S1 | CT-04 | CA02 | ✅ Verificado |
| RF06 | Sincronização incremental de status | S2 | CT-03 | CA05 | ✅ Verificado |
| RF07 | Conversão de HTML para ADF | S1 | CT-06 | CA03 | ✅ Verificado |
| RF08 | Mapeamento de status Sensr → Jira | S1 | CT-05 | CA04 | ✅ Verificado |
| RF09 | Migração do histórico como comentários | S2 | CT-07 | CA06 | ✅ Verificado |
| RF10 | Idempotência por prefixo `#ID` | S1 | CT-02 | CA01 | ✅ Verificado |
| RF11 | Paginação via `nextPageToken` (>50 issues) | S3 | CT-10 | CA02 | ✅ Verificado |
| RNF01 | Ciclo completo ≤ 30 min | S3 | Execução cronometrada em HOM | — | ✅ Atingida |
| RNF02 | Zero duplicatas (idempotência) | S2 | CT-01, CT-02 | CA01 | ✅ Atingida |
| RNF03 | Logs estruturados por evento | S2 | CT-09, CT-11 | CA07 | ✅ Atingida |
| RNF04 | Arquitetura em camadas (Core/Infra/App) | S0 | Avaliação de design (D01) | — | ✅ Atingida |
| RNF05 | .NET 8 LTS / manutenibilidade | S3 | Entrega e build CI/CD | — | ✅ Atingida |
| RNF06 | Credenciais em Azure Key Vault | S0 | Auditoria de configuração (GCO) | — | ✅ Atingida |

## 2. Cenários de teste × Critérios de aceite (12 CT)

| Cenário | Tipo | Requisito(s) | Critério de aceite | Situação |
|---|---|---|---|---|
| CT-01 — Migração inicial completa | Happy | RF02, RF03, RF04 | CA01, CA02 | ✅ Aprovado |
| CT-02 — Idempotência (sem duplicatas) | Happy | RF10, RNF02 | CA01 | ✅ Aprovado |
| CT-03 — Sincronização incremental de status | Happy | RF06 | CA05 | ✅ Aprovado |
| CT-04 — Subtasks vinculadas à Task pai | Happy | RF05 | CA02 | ✅ Aprovado |
| CT-05 — Mapeamento de todos os status | Happy | RF08 | CA04 | ✅ Aprovado |
| CT-06 — Conversão de HTML para ADF | Happy | RF07 | CA03 | ✅ Aprovado |
| CT-07 — Histórico como comentários | Happy | RF09 | CA06 | ✅ Aprovado |
| CT-08 — Migração de labels com normalização | Happy | RF03, RF04 | CA03 | ✅ Aprovado |
| CT-09 — Credencial inválida: isolamento | Sad | RF01, RNF03 | CA07 | ✅ Aprovado |
| CT-10 — Paginação de Epic (>50 issues) | Happy | RF11 | CA02 | ✅ Aprovado |
| CT-11 — Transição indisponível: log de aviso | Sad | RF08, RNF03 | CA04 | ✅ Aprovado |
| CT-12 — Sanitização de labels | Sad | RF03, RF04 | CA03 | ✅ Aprovado |

## 3. Cobertura

- **Requisitos sem cobertura:** nenhum — todos os RF têm cenário de teste e critério de aceite associados; os RNF são verificados de forma transversal (performance cronometrada, idempotência, logs, design em camadas, build .NET 8 e auditoria de configuração).
- **Cenários sem requisito associado:** nenhum — CT-08 e CT-12 cobrem a preservação/sanitização de labels, parte da migração de metadados (RF03/RF04).
- Critérios de aceite CA01–CA07 detalhados em VV-AASPGOV01-001; decisões D01–D07 em GDE-AASPGOV01-001.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Matriz de rastreabilidade consolidada a partir do INTAKE-AASPGOV01 (14/06/2026); cruzamento RF×CT×CA derivado das listas do Bloco 3 e 9. |
