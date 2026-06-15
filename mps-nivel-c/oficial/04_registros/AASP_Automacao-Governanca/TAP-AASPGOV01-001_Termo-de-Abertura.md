# Termo de Abertura do Projeto — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | TAP-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data de emissão** | 14/04/2026 |
| **Patrocinador / Cliente** | Marcos Correa Fernandez Turnes — AASP |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Objetivo e produto do projeto

Desenvolver e entregar o serviço **SensrJiraSync**: solução .NET 8 LTS (C#) executada como **Azure Scheduled Job** que realiza a migração automatizada de cards do Sensr para o Jira e mantém a sincronização incremental de status entre as duas plataformas durante o período de transição da AASP. A solução elimina o trabalho manual de migração, preservando hierarquia, descrição, status, responsáveis, labels, datas e histórico de cada atividade migrada.

## 2. Justificativa do projeto

A AASP migra sua ferramenta de gestão de projetos do Sensr para o Jira de forma gradual, exigindo operação em paralelo das duas plataformas durante a transição. O risco de divergência de informações e o volume de trabalho manual de replicação (descrição, status, subtarefas, responsáveis e histórico de cada atividade de cada desenvolvedor) justificam o desenvolvimento de um serviço automatizado de migração e sincronização.

## 3. Escopo macro

- **Incluído:**
  - Autenticação multi-desenvolvedor no Sensr (JWT por credencial) e no Jira (Basic Auth com API Token).
  - Migração de projetos (Epics), atividades (Tasks) e sub-atividades (Subtasks) com preservação de metadados, hierarquia, descrição, status, responsáveis, labels, datas e histórico.
  - Sincronização incremental de status (Sensr → Jira) para cards já migrados.
  - Conversão de HTML do Sensr para ADF (Atlassian Document Format) e migração do histórico como comentários.
  - Execução agendada e não supervisionada via Azure Scheduler.
- **Não incluído:**
  - Sincronização bidirecional (apenas Sensr → Jira); alterações no Jira não retornam ao Sensr.
  - Atualização de cards já migrados além do status.

## 4. Partes interessadas

| Papel | Responsabilidade | Organização |
|---|---|---|
| Marcos Correa Fernandez Turnes (Patrocinador / Cliente) | Validação do comportamento esperado e aceite formal da entrega | AASP |
| Abraão Oliveira (Gerente de Projeto) | Gestão das entregas, planejamento, acompanhamento e comunicação com o cliente | Timeware Brasil |
| Cezar Hiraki Velazquez (Tech Lead / Arquiteto) | Decisões técnicas e aprovação do design | Timeware Brasil |
| Jonathan Alves (Auditor GQA — independente) | Verificação de aderência ao processo MPS-SW; sem participação na execução | Timeware Brasil |

## 5. Equipe do projeto

| Papel | Responsável | Período de atuação | Observação |
|---|---|---|---|
| Gerente de Projeto | Abraão Oliveira | 14/04 – 02/06/2026 | Todas as fases |
| Tech Lead / Arquiteto | Cezar Hiraki Velazquez | 14/04 – 02/06/2026 | Decisões técnicas e aprovação de design |
| Desenvolvedor Sênior | Raony Chagas | 14/04 – 02/06/2026 | Todas as fases |
| Desenvolvedor | Allan Alves | 17/04 – 02/06/2026 | A partir da Fase 2 |
| Analista de Testes (QA) | Caroline Sousa | 21/05 – 02/06/2026 | Fase 4 — homologação |
| Infraestrutura / DevOps | Lucas Batista | 14/04 – 02/06/2026 | CI/CD e pipelines Azure |

## 6. Marcos do projeto

| Marco | Data |
|---|---|
| Kickoff / início (Fase 1 — Arquitetura) | 14/04/2026 |
| Fim do mapeamento e autenticação (Fase 2) | 23/04/2026 |
| Fim do desenvolvimento dos serviços (Fase 3) | 20/05/2026 |
| Validação da homologação (HOM) | 29/05/2026 |
| Aceite e encerramento | 02/06/2026 |

## 7. Premissas e restrições

**Premissas:**
- As APIs do Sensr e do Jira permanecem disponíveis e com contratos de autenticação estáveis durante o projeto.
- O workspace Jira inclui os status mapeados (To Do, In Progress, To Test, Blocked, Done).
- Cada desenvolvedor possui credenciais válidas no Sensr e conta válida no workspace Jira.

**Restrições:**
- Sincronização unidirecional (Sensr → Jira); a sincronização de status é a única atualização aplicada a cards já migrados.
- A API Jira v3 exige ADF para texto rico; a identificação de cards migrados depende do prefixo `#ID` no summary.
- Escopo fixo desde a abertura; qualquer adição requer Change Request formal e aprovação do Patrocinador.

## 8. Critérios de sucesso e aceite

- 100% dos cards existentes no Sensr migrados para o Jira sem duplicatas.
- Sincronização de status funcionando corretamente em execuções repetidas.
- Critérios de aceite CA01–CA07 aprovados pelo Patrocinador (ver VV-AASPGOV01-001).
- Homologação aprovada pelo representante do cliente.

## 9. Aprovação

| Papel | Responsável | Data |
|---|---|---|
| Patrocinador / Cliente | Marcos Correa Fernandez Turnes — AASP | 14/04/2026 |
| Gerente de Projeto | Abraão Oliveira — Timeware Brasil | 14/04/2026 |

Autorização registrada na reunião de kickoff (ATA-AASPGOV01-001, 14/04/2026).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Termo de abertura consolidado a partir do INTAKE-AASPGOV01 (14/06/2026) e do RDP-AASPGOV01-001 v3.0. |
