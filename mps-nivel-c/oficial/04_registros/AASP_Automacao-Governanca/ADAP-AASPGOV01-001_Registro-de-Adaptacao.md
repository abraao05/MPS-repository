# Registro de Adaptação do Processo — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | ADAP-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.1 |
| **Data** | 02/06/2026 |
| **Responsável pela adaptação** | Abraão Oliveira (Gerente de Projeto) |

---

## 1. Decisões de adaptação

Adaptação do processo-padrão (PRO-GPC-001) a este projeto, conforme o GUIA-GPC-001.

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto (com/sem front-end) | Sem UX/UI — apenas serviço de back-end (.NET 8 Scheduled Job) | A solução é um serviço de sincronização entre APIs (Sensr e Jira); não há interface de usuário. Toda interação humana ocorre nas plataformas externas, fora do escopo deste projeto. |
| Origem dos requisitos e do design | Timeware elabora; AASP valida e homologa | Os requisitos derivam de problemas operacionais identificados pela AASP na transição entre Sensr e Jira; a Timeware estruturou os RF/RNF e o desenho técnico, validados em homologação pelo Sponsor (Marcos Correa Fernandez Turnes). |
| Porte do projeto | Pequeno → nível de formalidade padrão | ~236 h realizadas em 7 semanas, equipe de 6 pessoas com escopo bem delimitado (11 RF + 6 RNF). Não justifica documentação reforçada nem reuniões formais por sprint. |
| Equipe e papéis (acúmulo) | Tech Lead acumula Arquiteto (Cezar Hiraki) | Projeto de pequeno porte com arquitetura bem definida desde a Fase 1 (3 camadas: Core/Infrastructure/App). Não justifica papel dedicado de Arquiteto separado do Tech Lead. |
| Estimativa e cadência | Execução acompanhada por horas em 4 fases (waterfall); backlog modelado retroativamente em **sprints e story points** (4 sprints, ~59 SP) para evidência ágil e carga no Jira | Concilia a gestão real por fases com a rastreabilidade ágil exigida na avaliação MPS-SW. O fator de conversão adotado foi **1 SP = 4 h** (referência de projetos B2B de pequeno porte), validado pela velocity resultante de ~15 SP/sprint. |
| Cadência de entrega ao cliente | Por marco/fase, com 4 reuniões de marco registradas em ata | Acordada com a AASP no Kickoff (ATA-AASPGOV01-001); resultados comunicados em Kickoff (14/04), Alinhamento de Mapeamento de APIs (23/04), Validação de Homologação (29/05) e Aceite Final (02/06). |
| Ambiente de stage | Não adotado — homologação por amostragem contra APIs reais | Comportamento crítico do serviço depende da compatibilidade real entre Sensr e Jira (autenticação, formato ADF, transições de status, paginação). Mocks ou ambientes simulados não seriam representativos — homologação executada contra workspaces de teste reais do Sensr e do Jira, validados por amostragem. |
| Cadência de reuniões internas | Reuniões pontuais de alinhamento entre o time + revisão via PR no Azure DevOps | Equipe pequena (6 pessoas) com comunicação direta; sprints formais (planning, review, retro) não foram adotados — a modelagem em sprints é retroativa, apenas para evidência. |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | Não | Projeto sem front-end (serviço back-end). Seção §3 do PCP-AASPGOV01-001 registra "não aplicável". |
| Mapa de teste por história (story) | Não | Projeto modelado em sprints retroativamente — testes organizados por funcionalidade técnica (12 cenários CT-01 a CT-12), não por história. Ver VV-AASPGOV01-001. |
| Documento de Design (arquitetura) | Sim | PCP-AASPGOV01-001 com arquitetura em 3 camadas + aceite do Tech Lead/Arquiteto. |
| Estratégia de Integração | Sim | ITP-AASPGOV01-001 detalhando integrações com Sensr, Jira v3 e Azure Scheduler. |
| Plano e execução de V&V | Sim | VV-AASPGOV01-001 (Plano) + REL-VV-AASPGOV01-001 (Execução). |
| Revisão por pares (code review) | Sim | REV-AASPGOV01-001 — Pull Request obrigatório com revisão por pelo menos 1 membro além do autor antes do merge em `develop`. |
| Gerência de Configuração | Sim | GCO-AASPGOV01-001 com Azure DevOps + GitFlow + baselines (BL-DEV, BL-HOM, BL-PROD). |
| Registro de decisões (GDE) | Sim | GDE-AASPGOV01-001 com 7 decisões (D01–D07) e RAD detalhado para D04 (uso de ADF). |
| Capacitação da equipe (CAP) | Sim | CAP-AASPGOV01-001 documentando equipe, integração de membros e práticas de transferência de conhecimento. |
| Medição (MED) | Sim | MED-AASPGOV01-001 alimentando os indicadores M1–M7 do PLA-MED-001. |
| Aquisição (AQU) | Não | Não há subcontratação de desenvolvimento; APIs Sensr/Jira e Azure Scheduler são insumos de serviço, tratados em ITP e nos riscos do PLA. |

## 3. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados (REQ-AASPGOV01-001 + ATA-AASPGOV01-001)
- [x] Plano de Projeto aprovado pelo cliente (baseline) — aprovado em 14/04/2026 (ATA-AASPGOV01-001)
- [x] Definição de Pronto aplicada (critérios de aceite CA01–CA07, ver VV-AASPGOV01-001)
- [x] Verificação e validação realizadas (VV-AASPGOV01-001 + REL-VV-AASPGOV01-001)
- [x] Encerramento formal com aceite (TAE-AASPGOV01-001 + ATA-AASPGOV01-004, em 02/06/2026)

Todos os pontos de controle obrigatórios foram cumpridos.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Registro de adaptação consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
| 1.1 | 16/06/2026 | Time de Melhoria Contínua | Reconciliação: nome padronizado (AASP_Automacao-Governanca); sobrenomes (Henry Komatsu, Felipe Siqueira, Jonathan Alves). |
