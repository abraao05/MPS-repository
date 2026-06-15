# Termo de Abertura do Projeto — AASP_GOV · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | TAP-AASPGOV01-001 |
| **Projeto** | AASP_GOV — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data de abertura** | 14/04/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Objetivo do projeto

Desenvolver e entregar o serviço SensrJiraSync — uma solução .NET 8 executada como Azure Scheduled Job — que realiza a migração automatizada de cards do Sensr para o Jira e mantém a sincronização incremental de status entre as duas plataformas durante o período de transição da AASP. A solução elimina o trabalho manual de migração e o risco de divergência entre as duas ferramentas enquanto a transição estiver em andamento, preservando hierarquia, descrição, status, responsáveis, labels, datas e histórico de cada atividade migrada.

## 2. Escopo macro

- **Incluído (macro):**
  - Autenticação nas APIs do Sensr (por desenvolvedor, via JWT) e do Jira (Basic Auth com API Token).
  - Migração de projetos (Epics), atividades (Tasks) e sub-atividades (Subtasks) com preservação de hierarquia, descrição, status, responsáveis, labels e histórico.
  - Sincronização incremental de status para cards já migrados.
  - Execução agendada e não supervisionada via Azure Scheduler.
  - Suporte a múltiplos desenvolvedores e projetos com credenciais independentes por desenvolvedor.
  - Conversão de HTML do Sensr para texto plano compatível com o formato ADF (Atlassian Document Format) do Jira.
  - Mapeamento dos status do Sensr (TODO, DOING, VALIDATION, STOPPED, DONE) para os equivalentes do Jira (To Do, In Progress, To Test, Blocked, Done).

- **Não incluído:**
  - Sincronização bidirecional — atualizações no Jira não são propagadas ao Sensr.
  - Atualização de campos além de status para cards já migrados — descrição, labels e demais campos são imutáveis após a criação inicial.
  - Migração de cards sem prefixo `#ID` no summary — cards sem esse prefixo não são reconhecidos pela sincronização.

## 3. Partes interessadas

| Parte interessada | Responsabilidade | Organização |
|---|---|---|
| Marcos Correa Fernandez Turnes (Sponsor / Patrocinador) | Validação dos requisitos, homologação e aceite formal das entregas | AASP |
| Abraão Oliveira (Gerente de Projeto) | Alinhamento com o cliente, gestão das entregas e comunicação | Timeware Brasil |
| Cezar Hiraki (Tech Lead / Arquiteto) | Decisões técnicas, arquitetura da solução e aprovação do design | Timeware Brasil |
| Jonathan Alves (Auditor GQA — independente) | Verificação de aderência ao processo MPS-SW | Timeware Brasil |

## 4. Equipe do projeto

| Papel | Responsável |
|---|---|
| Gerente de Projeto | Abraão Oliveira |
| Tech Lead / Arquiteto (acumula 2 papéis) | Cezar Hiraki |
| Desenvolvedor Sênior | Raony Chagas |
| Desenvolvedor (Suporte) | Allan Alves (incorporado em 17/04/2026, ao início da Fase 2) |
| Analista de Testes (QA) | Caroline Sousa (a partir da Fase 4 — 21/05/2026) |
| Infraestrutura / DevOps | Lucas Batista |

## 5. Macroplanejamento (datas-alvo)

| Marco | Data-alvo |
|---|---|
| Kickoff (abertura) | 14/04/2026 |
| Fim do Discovery / Mapeamento de APIs (Fase 2) | 23/04/2026 |
| Fim do Desenvolvimento (Fase 3) | 20/05/2026 |
| Início da Homologação (Fase 4) | 21/05/2026 |
| Validação de homologação | 29/05/2026 |
| Aceite e encerramento | 02/06/2026 |

## 6. Agenda das próximas atividades (na abertura)

- Definição da arquitetura em camadas (Core, Infrastructure, App) — Fase 1.
- Definição do modelo de configuração (AppSettings, DeveloperConfig, ProjectConfig).
- Mapeamento dos endpoints das APIs Sensr e Jira — Fase 2.
- Implementação dos fluxos de autenticação (JWT no Sensr, Basic Auth no Jira).
- Provisionamento dos acessos ao Azure DevOps e workspaces de teste.

## 7. Premissas e restrições iniciais

**Premissas:**
- As APIs do Sensr e do Jira permanecem disponíveis e com contratos de autenticação estáveis durante o período de operação.
- O workspace Jira da AASP inclui os status necessários: To Do, In Progress, To Test, Blocked e Done.
- Cada desenvolvedor da AASP possui credenciais válidas no Sensr e JiraAccountId válido no workspace configurado.

**Restrições:**
- Sincronização unidirecional (Sensr → Jira); alterações no Jira não são propagadas de volta.
- Sincronização de status é a única atualização aplicada a cards já existentes no Jira.
- A API Jira v3 exige ADF (Atlassian Document Format) para campos de texto rico; versões anteriores não são suportadas.
- Identificação de cards migrados depende do prefixo `#ID` no summary; cards sem esse prefixo não são reconhecidos.

---

## Registro de abertura

O projeto foi formalmente aberto em 14/04/2026 com a reunião de kickoff entre o Gerente de Projeto, o Tech Lead e o Sponsor da AASP. A ata correspondente registra a apresentação do escopo, a aprovação do TAP pelo Sponsor e a autorização para início da Fase 1 (Arquitetura).

| Reunião de kickoff realizada em | Ref. da ata |
|---|---|
| 14/04/2026 | ATA-AASPGOV01-001 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Termo de abertura consolidado a partir do Registro de Projeto AASP_GOV v2.0 (08/06/2026). |
