# Ata de Reunião — Alinhamento de APIs e Autenticação · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASPGOV01-002 |
| **Reunião** | Alinhamento: mapeamento das APIs Sensr e Jira, autenticação |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync |
| **Data** | 23/04/2026 |
| **Responsável pela ata** | Abraão Oliveira |

---

## 1. Participantes

| Nome | Papel | Organização |
|---|---|---|
| Abraão Oliveira | Gerente de Projeto | Timeware Brasil |
| Cezar Hiraki Velazquez | Tech Lead / Arquiteto | Timeware Brasil |
| Raony Chagas | Desenvolvedor Sênior | Timeware Brasil |
| Allan Alves | Desenvolvedor | Timeware Brasil |

## 2. Pauta

- Resultado do mapeamento dos endpoints das APIs Sensr e Jira.
- Definições de autenticação e de formato de dados.
- Autorização para a Fase 3 (Desenvolvimento dos Serviços).

## 3. Discussões e definições

Apresentado o mapeamento dos contratos (Swagger/OpenAPI, IC-04/IC-05). Confirmado que a API Jira v3 exige ADF para texto rico e não oferece busca por referência externa, o que orientou as decisões de design. Autenticação no Sensr definida como JWT por desenvolvedor.

## 4. Decisões e aceites

| Decisão / aceite | Responsável | Data |
|---|---|---|
| Adotar ADF para texto rico no Jira (D02) | Cezar Hiraki Velazquez / time | 23/04/2026 |
| Idempotência por prefixo `#ID` no summary (D03) | Cezar Hiraki Velazquez / time | 23/04/2026 |
| Runtime como Azure Scheduled Job (D04) | Cezar Hiraki Velazquez / time | 23/04/2026 |
| Autorização para a Fase 3 | Abraão Oliveira | 23/04/2026 |

(Decisões detalhadas em GDE-AASPGOV01-001.)

## 5. Ações (follow-up)

| Ação | Responsável | Prazo |
|---|---|---|
| Desenvolver serviços de migração (Epics, Tasks, Subtasks) | Allan Alves / Raony Chagas | Fase 3 |
| Implementar HtmlHelper (HTML→ADF) e StatusMapper | Raony Chagas | Fase 3 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Ata de alinhamento reconstituída a partir do INTAKE-AASPGOV01 (14/06/2026), Bloco 10.1. |
