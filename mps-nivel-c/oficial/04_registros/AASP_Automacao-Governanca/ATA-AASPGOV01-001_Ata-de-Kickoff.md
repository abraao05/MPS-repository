# Ata de Reunião — Kickoff do Projeto SensrJiraSync

| Campo | Valor |
|---|---|
| **Reunião** | Kickoff |
| **Projeto / contexto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Data** | 14/04/2026 |
| **Local / meio** | Videoconferência |
| **Responsável pela ata** | Abraão Oliveira |

---

## 1. Participantes

| Nome | Papel | Organização |
|---|---|---|
| Abraão Oliveira | Gerente de Projeto | Timeware |
| Cezar Hiraki | Tech Lead / Arquiteto | Timeware |
| Marcos Correa Fernandez Turnes | Sponsor / Patrocinador | AASP |

## 2. Pauta

- Apresentação do escopo do projeto SensrJiraSync.
- Alinhamento das fases e cronograma (~7 semanas).
- Definição da equipe Timeware alocada ao projeto.
- Autorização formal do início do projeto mediante aprovação do TAP-AASPGOV01-001.

## 3. Discussões e definições

O Gerente de Projeto apresentou o escopo completo do SensrJiraSync: serviço .NET 8 executado como Azure Scheduled Job, responsável pela migração automatizada de cards do Sensr para o Jira e pela sincronização incremental de status durante o período de transição entre as duas plataformas. Foram apresentados os 11 requisitos funcionais (RF01–RF11) e os 6 requisitos não-funcionais (RNF01–RNF06) que compõem a baseline do projeto.

O Tech Lead Cezar Hiraki apresentou a proposta de arquitetura em três camadas — Core, Infrastructure e App —, fundamentada na necessidade de separar contratos e modelos de domínio da implementação concreta, permitindo substituição de serviços sem impacto na lógica de negócio (D01). O Sponsor validou a abordagem e manifestou concordância com a duração estimada de aproximadamente sete semanas, compreendendo quatro fases: Arquitetura (14/04–16/04), Mapeamento e Autenticação (17/04–23/04), Desenvolvimento dos Serviços (24/04–20/05) e Homologação e Correções (21/05–02/06/2026).

A equipe Timeware foi formalmente apresentada ao Sponsor: além do Gerente de Projeto e do Tech Lead, compõem o time Henry (Desenvolvedor), Allan Alves (Desenvolvedor), Felipe (Desenvolvedor), Jonatan (QA) e Caroline Sousa (GQA Independente). O Sponsor declarou que o critério determinante para o aceite final será a fidelidade da migração e da sincronização de status verificada em ambiente real.

## 4. Decisões e aceites

| Decisão / aceite | Responsável | Data |
|---|---|---|
| Aprovação do TAP-AASPGOV01-001 pelo Sponsor, autorizando início formal do projeto | Marcos Correa Fernandez Turnes | 14/04/2026 |
| Baseline do escopo estabelecida (RF01–RF11 e RNF01–RNF06) | Abraão Oliveira | 14/04/2026 |
| Adotar arquitetura em três camadas: Core, Infrastructure e App (D01) | Cezar Hiraki | 14/04/2026 |
| Autorização para início imediato da Fase 1 — Arquitetura em 14/04/2026 | Abraão Oliveira | 14/04/2026 |

## 5. Ações (follow-up)

| Ação | Responsável | Prazo |
|---|---|---|
| Iniciar Fase 1 — definição de contratos de interface, modelo de configuração e estrutura de camadas | Cezar Hiraki | 16/04/2026 |
| Provisionar acessos ao Azure DevOps para o time de desenvolvimento | Cezar Hiraki | 16/04/2026 |
| Preparar e disponibilizar credenciais de acesso ao Sensr e ao Jira para uso nas Fases 2 e 3 | Marcos Correa Fernandez Turnes | 17/04/2026 |

## 6. Próximos passos

Execução da Fase 1 — Arquitetura (14/04 a 16/04/2026), com entrega da estrutura em três camadas, definição dos contratos de interface e modelo de configuração. Ao término da Fase 2 — Mapeamento e Autenticação (17/04–23/04/2026) — será realizada reunião de alinhamento técnico para validação dos endpoints mapeados e autorização para início da Fase 3.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Ata reconstituída a partir do Registro de Projeto AASP_GOV v2.0. |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Atualização da composição da equipe apresentada ao Sponsor e responsável pela ação de provisionamento de acessos. |
