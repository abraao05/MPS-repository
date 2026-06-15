# Plano de Projeto — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | PLA-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo

Desenvolver o serviço **SensrJiraSync** (.NET 8 LTS, Azure Scheduled Job) que migra cards do Sensr para o Jira e mantém a sincronização incremental de status durante a transição gradual da AASP. Ver REQ-AASPGOV01-001 para os requisitos detalhados.

## 2. Escopo (GPR 1)

- **Incluído:** autenticação multi-desenvolvedor (Sensr/Jira); migração de Epics, Tasks e Subtasks com preservação de metadados; conversão HTML→ADF; sincronização incremental de status; histórico como comentários; idempotência por `#ID`; execução agendada via Azure Scheduler.
- **Não incluído:** sincronização bidirecional; atualização de cards já migrados além do status.

## 3. Adaptação do processo (GPR 2)

Processo-padrão (PRO-GPC-001) adaptado conforme GUIA-GPC-001. Registro completo em ADAP-AASPGOV01-001. Destaques: planejamento consolidado em documento único; sprints retroativos (S0–S3) para rastreabilidade de esforço; medição apurada ao encerramento.

## 4. Estimativas (GPR 3, 4)

**Esforço por fase**

| Fase | Período | Est. (h) | Real. (h) | Variação | Responsável principal |
|---|---|---|---|---|---|
| Fase 1 — Arquitetura | 14/04 – 16/04/2026 | 16 | 16 | 0% | Cezar Hiraki |
| Fase 2 — Mapeamento e Autenticação | 17/04 – 23/04/2026 | 40 | 44 | +10% | Raony Chagas / Allan Alves |
| Fase 3 — Desenvolvimento dos Serviços | 24/04 – 20/05/2026 | 120 | 128 | +6,7% | Raony Chagas / Allan Alves |
| Fase 4 — Homologação e Correções | 21/05 – 02/06/2026 | 40 | 48 | +20% | Raony Chagas / Caroline Sousa |
| **Total** | 14/04 – 02/06/2026 | **216** | **236** | **+9,3%** | — |

**Modelo de sprints retroativos (S0–S3)** — backlog de 17 itens (11 RF + 6 RNF), 59 SP. Detalhamento em GEST-AASPGOV01 (abas Backlog e Acompanhamento).

| Sprint | Fase | Story Points | Período | Velocity |
|---|---|---|---|---|
| S0 | Fase 1 — Arquitetura | 15 SP | 14/04 – 16/04/2026 | 15 SP/sprint |
| S1 | Fase 2 — Mapeamento | 16 SP | 17/04 – 23/04/2026 | 16 SP/sprint |
| S2 | Fase 3 — Desenvolvimento | 16 SP | 24/04 – 08/05/2026 | 16 SP/sprint |
| S3 | Fase 3+4 — Conclusão e HOM | 12 SP | 09/05 – 02/06/2026 | 12 SP/sprint |
| **Total** | 4 sprints | **59 SP** | 14/04 – 02/06/2026 | ~15 SP/sprint (média) |

## 5. Cronograma e marcos (GPR 5)

| Marco | Data |
|---|---|
| Kickoff | 14/04/2026 |
| Fim do mapeamento | 23/04/2026 |
| Fim do desenvolvimento | 20/05/2026 |
| Validação da homologação | 29/05/2026 |
| Aceite / encerramento | 02/06/2026 |

## 6. Recursos (GPR 6, 7)

| Papel | Membro | Período | Observação |
|---|---|---|---|
| Gerente de Projeto | Abraão Oliveira | 14/04 – 02/06/2026 | Todas as fases |
| Tech Lead / Arquiteto | Cezar Hiraki Velazquez | 14/04 – 02/06/2026 | Decisões técnicas e aprovação de design |
| Desenvolvedor Sênior | Raony Chagas | 14/04 – 02/06/2026 | Todas as fases |
| Desenvolvedor | Allan Alves | 17/04 – 02/06/2026 | A partir da Fase 2 |
| Analista de Testes (QA) | Caroline Sousa | 21/05 – 02/06/2026 | Fase 4 — homologação |
| Infraestrutura / DevOps | Lucas Batista | 14/04 – 02/06/2026 | CI/CD e pipelines Azure |

**Ambiente e ferramentas:** .NET 8 LTS (C#); Azure DevOps (Git + Pipelines, GitFlow); Azure Scheduled Job (produção); Azure Key Vault (credenciais). Ver GCO-AASPGOV01-001.

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Marcos Correa Fernandez Turnes (Patrocinador — AASP) | Validação e aceite formal | Reuniões de kickoff, alinhamento e homologação (ATA-001 a 004) |
| Time de desenvolvimento | Execução e decisões técnicas | Alinhamento direto e revisão de código (PR) |
| Jonathan Alves (Auditor GQA) | Aderência ao processo | Auditoria ao encerramento |

## 8. Transição e suporte (GPR 8, 16)

| Item | Descrição |
|---|---|
| Fluxo de deploy | Homologação (Azure Scheduler staging) → release candidate → produção (Azure Scheduler prod) |
| Responsável | Lucas Batista (DevOps) — pipelines Azure |
| Aprovador do go-live | Abraão Oliveira (GP), com aceite do Patrocinador |
| Baselines | BL-DEV-001 (v0.9.0, 20/05) → BL-HOM-001 (v1.0.0-rc.1, 29/05) → BL-PROD-001 (v1.0.0, 02/06) |
| Monitoramento | Logs estruturados por execução/desenvolvedor/card (RNF04); execução agendada não supervisionada |

## 9. Riscos (GPR 10)

| ID | Risco | Probab. | Impacto | Estratégia de mitigação | Situação |
|---|---|---|---|---|---|
| R01 | Mudança no contrato da API do Sensr ou Jira durante o projeto | Baixa | Alto | Monitoramento de changelogs; testes em homologação antes de qualquer atualização em produção | ✅ Sob controle |
| R02 | Credenciais inválidas de um desenvolvedor bloqueando a execução completa | Média | Médio | Isolamento por desenvolvedor: falha de um não interrompe os demais (CT-09) | ✅ Tratado |
| R03 | Scope creep — campos ou comportamentos além do mapeado | Média | Médio | Escopo fixado no TAP-AASPGOV01-001; adição requer CR formal e aprovação do Sponsor | ✅ Não ocorreu |
| R04 | Performance insuficiente para grandes volumes (>50 cards/Epic) | Baixa | Médio | Paginação via `nextPageToken` (CT-10); validada em homologação com dados reais | ✅ Tratado |
| R05 | Divergência de status entre Sensr e Jira por mapeamento incorreto | Baixa | Alto | StatusMapper testado em CT-05; validação explícita do CA04 no aceite | ✅ Tratado |

## 10. Viabilidade (GPR 11)

Projeto viável: escopo delimitado, equipe alocada e arquitetura em camadas que isola integrações. A eliminação do trabalho manual de migração e a manutenção da consistência durante a transição justificam o esforço estimado (216 h). Riscos de maior impacto (R01, R05) endereçados por monitoramento e por testes em ambiente real.

## 11. Aprovação do plano (GPR 13)

| Envolvido | Papel | Aceite | Data |
|---|---|---|---|
| Marcos Correa Fernandez Turnes | Patrocinador / Cliente (AASP) | Autorização do projeto | 14/04/2026 (ATA-AASPGOV01-001) |
| Abraão Oliveira | Gerente de Projeto | Baseline do plano | 14/04/2026 |

Aceite final registrado no encerramento (TAE-AASPGOV01-001, 02/06/2026).

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Plano consolidado a partir do INTAKE-AASPGOV01 (14/06/2026) e do RDP-AASPGOV01-001 v3.0. |
