# Registro de Adaptação do Processo — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | ADAP-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 14/04/2026 |
| **Processo de referência** | MR-MPS-SW:2024 — Nível C · PRO-GPC-001 · GUIA-GPC-001 |
| **Responsável pela adaptação** | Abraão Oliveira |

---

## 1. Justificativa geral

Projeto de pequeno porte (~7 semanas, 49 dias corridos), equipe com comunicação direta e escopo fixo desde o início. As adaptações simplificam práticas do processo-padrão sem comprometer a rastreabilidade ou a qualidade das entregas.

## 2. Adaptações aplicadas

| Processo | Adaptação | Justificativa |
|---|---|---|
| GPR — Planejamento | Consolidado em documento único (RDP-AASPGOV01-001), sem Plano de Projeto separado | Curta duração e escopo fixo; o overhead de documento separado não agrega valor |
| GPR — Cronograma | Ciclos iterativos retroativos (S0–S3) em vez de sprints formais com cerimônias | Equipe com comunicação direta; sprints adotados retroativamente para rastreabilidade de esforço |
| REQ — Requisitos | Validados internamente com o cliente, sem documento de levantamento formal separado | Escopo definido em reunião de abertura (ATA-AASPGOV01-001) e estabilizado antes do desenvolvimento |
| VV — Verificação e Validação | Testes executados nos ambientes reais do Sensr e do Jira, sem ambiente de testes dedicado | O comportamento crítico depende da compatibilidade real entre plataformas; mocks não seriam representativos |
| GPC — Garantia da Qualidade | Auditoria única ao encerramento, cobrindo todo o projeto retroativamente | Projeto de curta duração com entregável único; auditorias intermediárias não foram necessárias |
| MED — Medição | Indicadores (M1–M7) apurados ao encerramento do projeto | Coleta contínua não aplicável a projeto sem sprints formais; indicadores apurados sobre o ciclo completo |

## 3. Processos mantidos integralmente

| Processo | Aplicação |
|---|---|
| OSW / PCP | Arquitetura e decisões técnicas documentadas integralmente, incluindo todas as decisões relevantes (D01–D07); design em camadas avaliado formalmente por Cezar Hiraki em 16/04/2026 |
| ITP | Todas as integrações documentadas com contratos de API, critérios de prontidão e estratégia de integração |
| GCO | Controle de versão via Azure DevOps com GitFlow aplicado integralmente; 3 baselines estabelecidas (BL-DEV/HOM/PROD) |
| GDE | Todas as decisões relevantes registradas com alternativas, justificativa e impacto (GDE-AASPGOV01-001) |
| CAP | Transferência de conhecimento documentada (Allan Alves na Fase 2; Caroline Sousa na Fase 4) |

## 4. Aquisição (AQU) — não aplicável

Não há subcontratação de desenvolvimento. As dependências de terceiros (.NET 8 LTS, API Jira v3, API Sensr) são insumos de serviço/biblioteca, identificadas e justificadas no escopo técnico (ver ITP-AASPGOV01-001 e PCP-AASPGOV01-001). Conforme o padrão organizacional (MAPA-ORG-001), AQU é não aplicável a este projeto e não gera registro próprio.

## 5. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados (REQ-AASPGOV01-001)
- [x] Plano de Projeto aprovado pelo cliente (baseline) — autorizado no TAP-AASPGOV01-001
- [x] Definição de Pronto aplicada (critérios de aceite CA01–CA07, ver VV-AASPGOV01-001)
- [x] Verificação e validação realizadas (VV / REL-VV-AASPGOV01-001)
- [x] Encerramento formal com aceite (TAE-AASPGOV01-001, aceite em 02/06/2026)

> Observação de auditoria (incorporada via L07): a adoção de **sprints retroativos (S0–S3)** é uma adaptação formal deste projeto, documentada nesta seção 2 para rastreabilidade de esforço sem cerimônias formais.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de adaptação consolidado a partir do INTAKE-AASPGOV01 (14/06/2026) e do RDP-AASPGOV01-001 v3.0. |
