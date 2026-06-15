# Registro de Capacitação da Equipe — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | CAP-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Abraão Oliveira |

---

## 1. Objetivo

Registrar a composição da equipe e as práticas de transferência de conhecimento adotadas no projeto, em especial a integração de um desenvolvedor na Fase 2 e de uma analista de testes na Fase 4. O Plano de Capacitação Organizacional aplicável é o PLA-CAP-001.

## 2. Equipe alocada

| Membro (papel) | Período de atuação | Observação |
|---|---|---|
| Abraão Oliveira — Gerente de Projeto | 14/04 – 02/06/2026 | Todas as fases |
| Cezar Hiraki Velazquez — Tech Lead / Arquiteto | 14/04 – 02/06/2026 | Decisões técnicas e aprovação de design |
| Raony Chagas — Desenvolvedor Sênior | 14/04 – 02/06/2026 | Todas as fases |
| Allan Alves — Desenvolvedor | 17/04 – 02/06/2026 | Incorporado na Fase 2 |
| Caroline Sousa — Analista de Testes (QA) | 21/05 – 02/06/2026 | Incorporada na Fase 4 (homologação) |
| Lucas Batista — Infraestrutura / DevOps | 14/04 – 02/06/2026 | CI/CD e pipelines Azure |

## 3. Transferência de conhecimento (integração de membros)

| Membro | Fase | Conteúdo da transferência |
|---|---|---|
| Allan Alves (Desenvolvedor) | Fase 2 (17/04) | Onboarding técnico: arquitetura em camadas, contratos das APIs Sensr e Jira, padrões de código e fluxo de migração — conduzido pelo Tech Lead e pelo Desenvolvedor Sênior |
| Caroline Sousa (QA) | Fase 4 (21/05) | Contexto de homologação: cenários de teste (CT-01 a CT-12), critérios de aceite (CA01–CA07) e estratégia de testes em ambiente real (Sensr/Jira) |

## 4. Práticas de transferência de conhecimento

| Prática | Descrição |
|---|---|
| Revisão de código (Pull Request) | Revisão nas integrações de branches no Azure DevOps, garantindo ciência das mudanças por todo o time (ver REV-AASPGOV01-001) |
| Definição colaborativa da arquitetura | Arquitetura em camadas definida e avaliada na Fase 1, documentada nos contratos do Core (D01) |
| Documentação de contratos de API | Swagger/OpenAPI das APIs Sensr e Jira versionados (IC-04, IC-05) como referência da equipe |
| Reuniões de alinhamento | Decisões técnicas compartilhadas e registradas nas atas (ATA-001 a ATA-004) |

## 5. Observações

A equipe já dominava as tecnologias core (.NET 8 LTS, Azure DevOps), dispensando treinamento formal específico. As ações de preparo focaram no contexto do projeto (integrações Sensr/Jira e estratégia de testes). A capacitação organizacional de referência está registrada no PLA-CAP-001.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de capacitação consolidado a partir do INTAKE-AASPGOV01 (14/06/2026), Blocos 2 e 4.2. |
