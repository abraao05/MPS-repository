# Ata de Reunião — Alinhamento Técnico: Mapeamento de APIs Sensr e Jira

| Campo | Valor |
|---|---|
| **Reunião** | Alinhamento técnico |
| **Projeto / contexto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Data** | 23/04/2026 |
| **Local / meio** | Videoconferência |
| **Responsável pela ata** | Abraão Oliveira |

---

## 1. Participantes

| Nome | Papel | Organização |
|---|---|---|
| Abraão Oliveira | Gerente de Projeto | Timeware |
| Cezar Hiraki | Tech Lead / DevOps / Arquiteto | Timeware |
| Henry Komatsu | Desenvolvedor | Timeware |
| Allan Alves | Desenvolvedor | Timeware |

## 2. Pauta

- Revisão dos endpoints mapeados nas APIs Sensr e Jira ao término da Fase 2.
- Validação da estratégia de autenticação por desenvolvedor na API Sensr.
- Definição da estratégia de identificação de cards já migrados no Jira.
- Confirmação da necessidade do Atlassian Document Format (ADF) para campos de texto rico.
- Autorização para início da Fase 3 — Desenvolvimento dos Serviços.

## 3. Discussões e definições

O Tech Lead Cezar Hiraki apresentou o resultado do mapeamento completo de endpoints realizado durante a Fase 2. No lado Sensr, foram identificados e documentados os endpoints de login (autenticação JWT), `getactivitiesbyprojectstatus` (listagem de atividades por projeto e status), `getsingleactivity` (detalhamento de atividade) e `subactivity` (sub-atividades vinculadas). No lado Jira v3, foram mapeados os endpoints de busca (`search`), criação de issues (`create`), transições de status (`transitions`) e comentários (`comments`).

A equipe discutiu a estratégia de autenticação com a API Sensr. Ficou estabelecido que o token JWT deverá ser obtido individualmente por desenvolvedor, pois a API retorna atividades filtradas pelo usuário autenticado — um token genérico resultaria em listas incompletas ou incorretas (D02). Em sequência, foi definida a estratégia de identificação de cards migrados: o SyncService utilizará o prefixo `#ID` no campo summary do Jira para detectar se um card já foi migrado, evitando duplicatas sem necessidade de campos personalizados ou dependências adicionais na plataforma (D03).

Por fim, o Tech Lead confirmou que a API Jira v3 exige o uso do Atlassian Document Format (ADF) para todos os campos de texto rico, como descrição e comentários. O envio de texto plano resulta em erro de validação por parte da API. Com isso, ficou definida a necessidade de implementação do método `BuildAdfDocument` no JiraService para conversão do conteúdo antes do envio (D04). O Gerente de Projeto formalizou a autorização para início da Fase 3 a partir de 24/04/2026.

## 4. Decisões e aceites

| Decisão / aceite | Responsável | Data |
|---|---|---|
| Autenticação JWT individual por desenvolvedor no Sensr (D02) | Cezar Hiraki | 23/04/2026 |
| Identificação de cards migrados via prefixo #ID no summary do Jira (D03) | Cezar Hiraki | 23/04/2026 |
| Necessidade de ADF confirmada para campos de texto no Jira v3 (D04 formalizada na Fase 3 — ver GDE-AASPGOV01-001) | Henry Komatsu | 23/04/2026 |
| Aprovação para início da Fase 3 — Desenvolvimento dos Serviços em 24/04/2026 | Abraão Oliveira | 23/04/2026 |

## 5. Ações (follow-up)

| Ação | Responsável | Prazo |
|---|---|---|
| Implementar SensrService com mecanismo de login por desenvolvedor e gestão de tokens JWT | Henry Komatsu | Mai/2026 |
| Implementar JiraService incluindo método BuildAdfDocument para campos de texto rico | Henry Komatsu / Allan Alves | Mai/2026 |
| Preparar estrutura de testes e cenários para uso na Fase 4 de Homologação | Jonathan Alves | Mai/2026 |
| Provisionar ambiente de integração para execução dos serviços durante a Fase 3 | Cezar Hiraki | 24/04/2026 |

## 6. Próximos passos

Início da Fase 3 — Desenvolvimento dos Serviços (24/04 a 20/05/2026), com implementação do SensrService, JiraService, SyncService, StatusMapper, HtmlHelper e modelos de dados. Ao término da fase, os serviços serão submetidos à Fase 4 de Homologação em ambiente real do cliente.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Ata reconstituída a partir do Registro de Projeto AASP_Automacao-Governanca v2.0. |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Atualização dos participantes e responsáveis pelas ações: Henry Komatsu substituiu Raony Chagas, Cezar Hiraki substituiu Lucas Batista, Jonathan Alves substituiu Caroline Sousa nas ações de preparação de testes. |
| 1.2 | 15/06/2026 | Time de Melhoria Contínua | Papel de Cezar Hiraki atualizado para Tech Lead / DevOps / Arquiteto na tabela de participantes; Jonathan Alves (QA) corrigido de grafia anterior. |
| 1.3 | 16/06/2026 | Time de Melhoria Contínua | Reconciliação: nome padronizado (AASP_Automacao-Governanca); sobrenomes (Henry Komatsu, Felipe Siqueira, Jonathan Alves); D04 como necessidade confirmada em 23/04 (formalização na Fase 3). |
