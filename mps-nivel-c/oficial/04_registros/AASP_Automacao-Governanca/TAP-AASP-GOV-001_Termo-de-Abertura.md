# Termo de Abertura do Projeto — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | TAP-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data de emissão** | 14/04/2026 |
| **Patrocinador / Cliente** | Marcos Correa Fernandez Turnes — AASP |
| **Gerente de Projeto** | Cezar Hiraki Velazquez (Gerente de Projeto / Tech Lead) |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Objetivo e produto do projeto

Desenvolver e entregar o serviço **SensrJiraSync**: uma solução .NET 8 executada como Azure Scheduled Job que realiza a migração automatizada de cards do Sensr para o Jira e mantém a sincronização de status entre as plataformas durante o período de transição.

A AASP utilizava o Sensr como ferramenta de gerenciamento de projetos e atividades do time de desenvolvimento e, por requisitos operacionais e de governança, decidiu migrar para o Jira. Por se tratar de uma migração gradual — não de uma substituição imediata — o time precisaria operar nas duas ferramentas simultaneamente durante a transição, com risco real de divergência entre os registros. O serviço deve criar no Jira todos os cards existentes no Sensr, preservando sua estrutura hierárquica, e atualizar automaticamente o status dos cards já migrados quando houver movimentação no Sensr.

## 2. Justificativa do projeto

A AASP decidiu migrar sua ferramenta de gestão de projetos do Sensr para o Jira. A migração será realizada de forma gradual, exigindo que ambas as ferramentas operem em paralelo durante o período de transição. O risco de divergência de informações entre as plataformas e o volume de trabalho manual envolvido na migração — replicar descrição, status, subtarefas, responsáveis e histórico de cada atividade de cada desenvolvedor em cada projeto — justificam o desenvolvimento de um serviço automatizado de sincronização.

## 3. Escopo resumido

- **Incluído:**
  - Autenticação nas APIs do Sensr (por desenvolvedor) e do Jira.
  - Migração de projetos (Epics), atividades (Tasks) e sub-atividades (Subtasks) com preservação de hierarquia, descrição, status, responsáveis, labels e histórico.
  - Sincronização incremental de status para cards já migrados.
  - Execução agendada e não supervisionada via Azure Scheduler.

- **Não incluído / restrições de escopo:**
  - Sincronização unidirecional (Sensr → Jira); alterações no Jira não são propagadas de volta.
  - Sincronização de status é a única atualização aplicada a cards já migrados.

## 4. Partes interessadas

| Papel | Responsabilidade | Organização |
|---|---|---|
| Marcos Correa Fernandez Turnes (Patrocinador / Cliente) | Validação do comportamento esperado da sincronização e aceite formal da entrega | AASP |
| Cezar Hiraki Velazquez (Gerente de Projeto / Tech Lead) | Definição dos requisitos, arquitetura da solução, acompanhamento do desenvolvimento e entrega ao cliente | Timeware Brasil |
| Raony Chagas (Desenvolvedor Sênior) | Desenvolvimento dos serviços de integração, camada de infraestrutura e lógica de sincronização | Timeware Brasil |
| Allan Barbosa Patrocínio Alves (Desenvolvedor) | Suporte ao desenvolvimento, mapeamento de endpoints e testes de integração | Timeware Brasil |
| Jonathan Barbosa (Auditor GQA — independente) | Verificação de aderência ao processo MPS-SW; não participa da execução do projeto | Timeware Brasil |

## 5. Equipe do projeto

| Papel | Responsável | Período | Fases |
|---|---|---|---|
| Gerente de Projeto / Tech Lead | Cezar Hiraki Velazquez | 14/04 – 02/06/2026 | Todas |
| Desenvolvedor Sênior | Raony Chagas | 14/04 – 02/06/2026 | 1, 2, 3 e 4 |
| Desenvolvedor | Allan Barbosa Patrocínio Alves | 17/04 – 02/06/2026 | 2, 3 e 4 |

## 6. Macroplanejamento (datas-alvo)

| Marco | Data-alvo |
|---|---|
| Data de início autorizada (Fase 1 — Arquitetura) | 14/04/2026 |
| Fim do mapeamento e autenticação (Fase 2) | 23/04/2026 |
| Fim do desenvolvimento dos serviços (Fase 3) | 20/05/2026 |
| Homologação e correções (Fase 4) | 02/06/2026 |
| Data de encerramento prevista | 02/06/2026 |

## 7. Premissas e restrições iniciais

**Premissas:**
- As APIs do Sensr e do Jira permanecem disponíveis e estáveis durante o período de operação.
- Workspace Jira configurado com os status mapeados (To Do, In Progress, To Test, Blocked, Done).

**Restrições:**
- Sincronização unidirecional (Sensr → Jira); alterações no Jira não são propagadas de volta.
- A sincronização de status é a única atualização aplicada a cards já migrados.

## 8. Critérios de sucesso e aceite

- 100% dos cards existentes no Sensr migrados para o Jira sem duplicatas.
- Sincronização de status funcionando corretamente em execuções repetidas.
- Homologação aprovada pelo representante do cliente.

## 9. Aprovação

| Papel | Responsável | Data |
|---|---|---|
| Patrocinador / Cliente | Marcos Correa Fernandez Turnes — AASP | 14/04/2026 |
| Gerente de Projeto | Cezar Hiraki Velazquez — Timeware Brasil | 14/04/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Termo de abertura consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
