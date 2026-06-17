# Registro de Capacitação da Equipe — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | CAP-AASPGOV01-001 — Registro de Capacitação da Equipe |
| **Versão** | 1.3 |
| **Data** | 15/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Aprovação** | Abraão Oliveira |

---

## 1. Objetivo

Registrar a composição da equipe alocada ao projeto AASP_Automacao-Governanca, as ações de integração formal de membros ao time e as práticas de transferência de conhecimento adotadas ao longo das quatro fases do projeto (Arquitetura, Mapeamento e Autenticação, Desenvolvimento dos Serviços e Homologação e Correções).

## 2. Equipe alocada

| Membro (papel) | Período de atuação | Fases |
|---|---|---|
| Abraão Oliveira — Gerente de Projeto | 14/04/2026 – 02/06/2026 | Todas |
| Cezar Hiraki — Tech Lead / DevOps / Arquiteto | 14/04/2026 – 02/06/2026 | Todas |
| Henry Komatsu — Desenvolvedor | 14/04/2026 – 02/06/2026 | Todas |
| Allan Alves — Desenvolvedor | 17/04/2026 – 02/06/2026 | 2, 3, 4 |
| Felipe Siqueira — Desenvolvedor | 17/04/2026 – 02/06/2026 | 2, 3, 4 |
| Jonathan Alves — QA | 21/05/2026 – 02/06/2026 | 4 |
| Caroline Sousa — GQA (Independente) | 02/06/2026 | Auditoria final |

## 3. Integração formal de membros ao time

Em **17/04/2026**, o Desenvolvedor Allan Alves foi incorporado ao time para auxiliar nas atividades de mapeamento de APIs e desenvolvimento, a partir da Fase 2. A integração foi conduzida na reunião de alinhamento técnico registrada em ATA-AASPGOV01-002, na qual foram apresentados a estrutura da solução em 3 camadas (Core / Infrastructure / App), o mapeamento completo dos endpoints das APIs Sensr e Jira v3, a estratégia de autenticação JWT por desenvolvedor (D02) e o modelo de mapeamento de entidades Sensr → Jira. O onboarding permitiu a atuação imediata de Allan Alves nas atividades de desenvolvimento da Fase 3 em parceria com Henry Komatsu.

Em **21/05/2026**, o QA Jonathan Alves foi incorporado ao time para condução da Fase 4 de Homologação. O briefing de entrada cobriu os critérios de aceite CA01 a CA07, os 12 cenários de teste planejados no VV-AASPGOV01-001 (CT-01 a CT-12), e a estratégia de homologação executada diretamente em ambiente real Sensr / Jira (sem uso de mocks), conforme ADAP-AASPGOV01-001. A integração foi conduzida pelo Gerente de Projeto e pelo Tech Lead, garantindo plena capacidade de execução dos testes a partir do primeiro dia da Fase 4.

## 4. Práticas de transferência de conhecimento

| Prática | Descrição |
|---|---|
| Revisão de código (Pull Request) | Toda mudança em `develop` exige revisão de ao menos 1 membro da equipe além do autor. O code review funciona como mecanismo de disseminação técnica: o revisor é exposto às decisões de implementação e pode questionar abordagens antes da integração. Registrado em REV-AASPGOV01-001. |
| Reuniões de alinhamento | Três marcos do projeto foram formalizados em atas: Kickoff (ATA-AASPGOV01-001, 14/04/2026), Mapeamento de APIs (ATA-AASPGOV01-002, 23/04/2026) e Validação de Homologação (ATA-AASPGOV01-003, 29/05/2026). As reuniões garantiram alinhamento técnico e de escopo entre todos os membros ativos em cada fase. |
| Documentação técnica inline | Comentários XML nos métodos públicos dos serviços, com ênfase nos comportamentos não óbvios: parsing de histórico HTML no HtmlHelper, mecanismo de identificação por prefixo `#ID` no SyncService e estruturação do ADF no BuildAdfDocument. |
| Definição colaborativa da arquitetura | A arquitetura em 3 camadas foi definida na Fase 1 com participação de toda a equipe técnica (Cezar Hiraki, Henry Komatsu), documentada nos contratos de interface do Core como referência compartilhada para o desenvolvimento subsequente. |
| Pareamento técnico (pair programming pontual) | Sessões pontuais entre Henry Komatsu (Desenvolvedor) e Allan Alves (Desenvolvedor) para implementação das partes de maior complexidade técnica: `BuildAdfDocument` (geração de ADF) e `HtmlHelper` (conversão de HTML). |

## 5. Observações

A equipe já atuava com as tecnologias centrais do projeto (.NET 8, Azure DevOps, GitFlow, APIs RESTful, Jira), não havendo necessidade de treinamento formal específico. As ações de preparação focaram nos elementos particulares do projeto: contratos das APIs Sensr e Jira v3, o Atlassian Document Format (ADF) como requisito da API Jira v3, e as particularidades do Azure Scheduler como ambiente de execução. O Plano de Capacitação Organizacional aplicável está registrado em PLA-CAP-001. A auditoria independente de qualidade foi conduzida por Caroline Sousa (GQA Independente) ao encerramento do projeto, com resultado registrado em GQA-AASPGOV01-001.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Registro de capacitação consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0. |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Atualização da composição da equipe: Henry Komatsu substituiu Raony Chagas, Cezar absorveu DevOps, Felipe Siqueira adicionado como Desenvolvedor, Jonathan Alves como QA, Caroline Sousa como GQA Independente. |
| 1.2 | 15/06/2026 | Time de Melhoria Contínua | Jonathan Alves (QA) corrigido de grafia anterior. |
| 1.3 | 16/06/2026 | Time de Melhoria Contínua | Reconciliação: nome padronizado (AASP_Automacao-Governanca); sobrenomes (Henry Komatsu, Felipe Siqueira, Jonathan Alves). |
