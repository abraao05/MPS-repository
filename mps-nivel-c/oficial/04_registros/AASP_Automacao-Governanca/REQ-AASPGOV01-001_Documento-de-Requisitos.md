# Documento de Requisitos — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | REQ-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsáveis** | Abraão Oliveira (GP) · Cezar Hiraki Velazquez (Tech Lead / Arquiteto) |

---

## 1. Objetivo do sistema

Serviço .NET 8 LTS (C#) executado como **Azure Scheduled Job** que realiza a migração automatizada de cards do Sensr para o Jira e mantém a sincronização incremental de status entre as duas plataformas durante o período de transição da AASP. A solução elimina o trabalho manual de migração e preserva hierarquia, descrição, status, responsáveis, labels, datas e histórico de cada atividade migrada.

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| Marcos Correa Fernandez Turnes (Patrocinador — AASP) | Migração fiel e automatizada, sem divergência durante a transição |
| Gestores da AASP | Visibilidade das atividades no Jira durante a migração gradual |
| Time de desenvolvimento (Timeware) | Idempotência, rastreabilidade e isolamento de falha por desenvolvedor |

## 3. Requisitos funcionais

| ID | Descrição | Prioridade | Sprint |
|---|---|---|---|
| RF01 | Autenticação multi-desenvolvedor no Sensr via JWT por credencial individual | Alta | S0 |
| RF02 | Autenticação no Jira via Basic Auth com API Token por workspace | Alta | S0 |
| RF03 | Migração de projetos Sensr como Epics no Jira com preservação de metadados | Alta | S1 |
| RF04 | Migração de atividades como Tasks no Jira vinculadas ao Epic correspondente | Alta | S1 |
| RF05 | Migração de sub-atividades como Subtasks vinculadas à Task pai | Alta | S1 |
| RF06 | Sincronização incremental de status (Sensr → Jira) para cards já migrados | Alta | S2 |
| RF07 | Conversão de conteúdo HTML do Sensr para ADF (Atlassian Document Format) | Alta | S1 |
| RF08 | Mapeamento de status: TODO→To Do, DOING→In Progress, VALIDATION→To Test, STOPPED→Blocked, DONE→Done | Alta | S1 |
| RF09 | Migração do histórico (`description_history`) como comentários individuais na Task | Média | S2 |
| RF10 | Idempotência: prefixo `#ID` no summary impede duplicação em reexecuções | Alta | S1 |
| RF11 | Paginação de resultados via `nextPageToken` para Epics com mais de 50 issues | Média | S3 |

## 4. Requisitos não funcionais

| ID | Descrição | Categoria | Meta | Resultado |
|---|---|---|---|---|
| RNF01 | Execução completa do ciclo em no máximo 30 minutos | Performance | ≤ 30 min | ✅ Atingida |
| RNF02 | Zero duplicatas em execuções repetidas (idempotência) | Confiabilidade | 0 duplicatas | ✅ 0 duplicatas (CT-01, CT-02) |
| RNF03 | Disponibilidade contínua via Azure Scheduler (sem intervenção manual) | Disponibilidade | 24/7 | ✅ Atingida (Azure Scheduler) |
| RNF04 | Logs estruturados por desenvolvedor, por execução e por card processado | Rastreabilidade | Log por evento | ✅ Atingida |
| RNF05 | Cobertura de testes e estrutura .NET 8 LTS para manutenção de longo prazo | Manutenibilidade | .NET 8 LTS | ✅ Atingida |
| RNF06 | Credenciais armazenadas em Azure Key Vault; sem hardcode em código-fonte | Segurança | Key Vault | ✅ Atingida |

## 5. Restrições e premissas

**Restrições:**
- Sincronização unidirecional (Sensr → Jira); a sincronização de status é a única atualização aplicada a cards já migrados.
- A API Jira v3 exige ADF para campos de texto rico.
- A identificação de cards migrados depende do prefixo `#ID` no summary.

**Premissas:**
- As APIs do Sensr e do Jira permanecem disponíveis e com contratos estáveis.
- O workspace Jira inclui os status mapeados (To Do, In Progress, To Test, Blocked, Done).
- Cada desenvolvedor possui credenciais válidas no Sensr e conta válida no Jira.

## 6. Validação dos requisitos

| Requisito/conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| Escopo e requisitos (RF01–RF11, RNF01–RNF06) | Validação interna com o cliente na reunião de abertura | 14/04/2026 | Validado (TAP-AASPGOV01-001 · ATA-AASPGOV01-001) |
| Critérios de aceite CA01–CA07 | Validação da homologação com o Patrocinador | 29/05/2026 | Aprovado (ATA-AASPGOV01-003) |

Rastreabilidade RF × CA × CT em RASTR-AASPGOV01-001.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Documento de requisitos consolidado a partir do INTAKE-AASPGOV01 (14/06/2026) e do RDP-AASPGOV01-001 v3.0. |
