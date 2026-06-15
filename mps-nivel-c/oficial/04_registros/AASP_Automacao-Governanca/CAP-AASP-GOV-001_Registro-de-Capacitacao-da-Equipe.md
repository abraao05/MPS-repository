# Registro de Capacitação da Equipe — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | CAP-AASP-GOV-001 — Registro de Capacitação da Equipe |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Aprovação** | Cezar Hiraki Velazquez |

---

## 1. Objetivo

Registrar a composição da equipe e as práticas de transferência de conhecimento adotadas ao longo do projeto. O projeto foi desenvolvido por uma equipe de três pessoas com papéis complementares; a transferência de conhecimento ocorreu de forma orgânica nas fases de mapeamento de APIs e revisão de código.

## 2. Equipe alocada

| Membro (papel) | Período de atuação | Fases |
|---|---|---|
| Cezar Hiraki Velazquez — Gerente de Projeto / Tech Lead | 14/04 – 02/06/2026 | Todas |
| Raony Chagas — Desenvolvedor Sênior | 14/04 – 02/06/2026 | 1, 2, 3 e 4 |
| Allan Barbosa Patrocínio Alves — Desenvolvedor | 17/04 – 02/06/2026 | 2, 3 e 4 |

## 3. Práticas de transferência de conhecimento

| Prática | Descrição |
|---|---|
| Mapeamento compartilhado de APIs | Mapeamento dos endpoints das APIs do Sensr e do Jira na Fase 2, com participação de todos os membros, evitando concentração de conhecimento |
| Revisão de código | Revisão nas integrações de branches no Azure DevOps, com rastreabilidade das decisões de implementação (ver REV-AASP-GOV-001) |
| Definição colaborativa da arquitetura | Arquitetura em camadas definida em conjunto na Fase 1 e documentada nos contratos de interface do Core como referência para o desenvolvimento subsequente |
| Documentação inline | Comentários XML nos métodos públicos dos serviços, especialmente nos casos de comportamento não óbvio (parsing de histórico HTML e identificação de issues por `#ID`) |

## 4. Observações

A equipe já atuava com as tecnologias core (.NET 8, Azure DevOps), dispensando treinamento formal específico. As ações de preparo concentraram-se no contexto das integrações com as APIs do Sensr e do Jira. O Plano de Capacitação Organizacional aplicável está registrado em PLA-CAP-001.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de capacitação da equipe consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
