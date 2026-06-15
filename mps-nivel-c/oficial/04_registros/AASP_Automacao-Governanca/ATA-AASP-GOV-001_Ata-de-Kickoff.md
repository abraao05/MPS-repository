# Ata de Reunião — Abertura do projeto (Kickoff) AASP_Automacao-Governanca

| Campo | Valor |
|---|---|
| **Reunião** | Reunião de abertura — definição de escopo e autorização do projeto SensrJiraSync |
| **Projeto / contexto** | AASP_Automacao-Governanca — SensrJiraSync |
| **Data** | 14/04/2026 |
| **Responsável pela ata** | Cezar Hiraki Velazquez |

---

## 1. Participantes

| Nome | Papel | Organização |
|---|---|---|
| Marcos Correa Fernandez Turnes | Patrocinador / Cliente | AASP |
| Cezar Hiraki Velazquez | Gerente de Projeto / Tech Lead | Timeware Brasil |
| Raony Chagas | Desenvolvedor Sênior | Timeware Brasil |

## 2. Pauta

- Apresentação da motivação: migração gradual da gestão de projetos do Sensr para o Jira, com operação em paralelo durante a transição.
- Definição do escopo do serviço de sincronização (SensrJiraSync).
- Autorização do projeto e definição da arquitetura inicial.

## 3. Discussões e definições

Foi apresentada a necessidade de um serviço automatizado que migre os cards do Sensr para o Jira, preservando hierarquia, descrição, status, responsáveis, labels e histórico, e que mantenha a sincronização incremental de status enquanto a transição estiver em andamento. Definiu-se que a sincronização seria **unidirecional** (Sensr → Jira) e que a atualização de cards já migrados se limitaria ao status. O escopo foi estabelecido nesta reunião e estabilizado antes do início do desenvolvimento (ver REQ-AASP-GOV-001 e ADAP-AASP-GOV-001).

## 4. Decisões e aceites

| Decisão / aceite | Responsável | Data |
|---|---|---|
| Autorização formal do projeto (Termo de Abertura) | Marcos Correa Fernandez Turnes / Cezar Hiraki Velazquez | 14/04/2026 (TAP-AASP-GOV-001) |
| Estruturar a solução em três camadas: Core, Infrastructure e App (D01) | Cezar Hiraki Velazquez / time | 14/04/2026 |
| Autenticação por desenvolvedor no Sensr — token JWT individual (D02) | Cezar Hiraki Velazquez / time | 14/04/2026 |

(Decisões detalhadas em GDE-AASP-GOV-001.)

## 5. Ações (follow-up)

| Ação | Responsável | Prazo |
|---|---|---|
| Definir a arquitetura em camadas e o modelo de configuração (Fase 1) | Cezar Hiraki Velazquez / Raony Chagas | 16/04/2026 |
| Mapear os endpoints das APIs Sensr e Jira (Fase 2) | Raony Chagas | 23/04/2026 |

## 6. Próximos passos

Início da Fase 1 (Arquitetura): definição da estrutura de projetos, contratos de interface e modelo de configuração.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Ata da reunião de abertura (14/04/2026) reconstituída a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
