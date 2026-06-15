# Registro de Adaptação do Processo — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | ADAP-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 14/04/2026 |
| **Processo de referência** | MR-MPS-SW:2024 — Nível C |
| **Responsável pela adaptação** | Cezar Hiraki Velazquez |

---

## 1. Justificativa da adaptação

O projeto AASP_Automacao-Governanca é um projeto de desenvolvimento de software de pequeno porte, com duração de aproximadamente 7 semanas, equipe de 3 pessoas e escopo bem delimitado. Em função dessas características, algumas práticas do processo MPS-SW padrão foram simplificadas sem comprometer a qualidade ou a rastreabilidade das entregas.

## 2. Adaptações aplicadas

| Processo | Adaptação | Justificativa |
|---|---|---|
| GPR — Gerência de Projeto | Planejamento e acompanhamento consolidados em documento único, sem plano de projeto separado | Projeto de curta duração com escopo fixo desde o início; o overhead de documento separado não agrega valor |
| GPR — Cronograma | Cronograma por atividade em vez de sprints formais com cerimônias | Equipe pequena com comunicação direta; sprints formais não foram adotados |
| REQ — Requisitos | Requisitos especificados e validados internamente com o cliente, sem documento de levantamento formal separado | Escopo definido em reunião de abertura; requisitos estabilizados antes do início do desenvolvimento |
| VV — Verificação e Validação | Testes executados diretamente nos ambientes reais do Sensr e do Jira, sem ambiente de testes dedicado | O comportamento crítico depende da compatibilidade real entre plataformas; mocks não seriam representativos |
| GPC — Garantia da Qualidade | Auditoria única ao encerramento, cobrindo todo o projeto retroativamente | Projeto de curta duração com entregável único; auditorias intermediárias não foram necessárias |
| MED — Medição | Indicadores apurados ao encerramento do projeto | Coleta contínua não aplicável a projeto sem sprints formais; indicadores apurados sobre o ciclo completo |

## 3. Processos mantidos integralmente

| Processo | Aplicação |
|---|---|
| OSW / PCP — Arquitetura e decisões técnicas | Documentadas integralmente, incluindo todas as decisões relevantes (ver PCP-AASP-GOV-001 e GDE-AASP-GOV-001) |
| ITP — Integração | Todas as integrações documentadas com contratos e fluxos de dados (ver ITP-AASP-GOV-001) |
| GCO — Gerência de Configuração | Controle de versão via Azure DevOps com GitFlow aplicado integralmente (ver GCO-AASP-GOV-001) |
| GDE — Gerência de Decisões | Todas as decisões relevantes registradas com justificativa e impacto (ver GDE-AASP-GOV-001) |
| AQU — Aquisição | Todas as dependências de terceiros identificadas e justificadas (ver AQU-AASP-GOV-001) |
| CAP — Capacitação | Transferência de conhecimento documentada (ver CAP-AASP-GOV-001) |

## 4. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados (REQ-AASP-GOV-001)
- [x] Plano de Projeto aprovado pelo cliente (baseline) — autorizado no Termo de Abertura (TAP-AASP-GOV-001)
- [x] Definição de Pronto aplicada (critérios de aceite CA01–CA07, ver VV-AASP-GOV-001)
- [x] Verificação e validação realizadas (VV / REL-VV-AASP-GOV-001)
- [x] Encerramento formal com aceite (TAE-AASP-GOV-001, aceite em 02/06/2026)

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de adaptação consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
