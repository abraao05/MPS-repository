# Plano de Projeto — AASP_GOV · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | PLA-AASPGOV01-001 |
| **Projeto** | AASP_GOV — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

A AASP utilizava o Sensr como ferramenta de gerenciamento de projetos e atividades do time de desenvolvimento. Em função de requisitos operacionais e de governança, foi tomada a decisão de migrar para o Jira. Por se tratar de uma migração gradual — e não de uma substituição imediata — o time precisaria operar nas duas ferramentas simultaneamente durante um período de transição, com risco real de divergência entre os registros e volume elevado de trabalho operacional para replicação manual de cards. O projeto entrega o serviço SensrJiraSync, uma solução .NET 8 executada como Azure Scheduled Job que realiza a migração automatizada e a sincronização incremental entre as duas plataformas. Ver REQ-AASPGOV01-001 para os requisitos detalhados.

## 2. Escopo (GPR 1)

- **Incluído:** autenticação JWT por desenvolvedor no Sensr e Basic Auth com API Token no Jira; criação de Epics (projetos), Tasks (atividades) e Subtasks (sub-atividades) com preservação de hierarquia, descrição, status, responsáveis, labels e histórico; sincronização incremental de status para cards já migrados; conversão HTML → ADF; mapeamento dos 5 status do Sensr para os equivalentes do Jira; sanitização de labels; idempotência via prefixo `#ID` no summary; execução agendada e não supervisionada via Azure Scheduler; configuração multi-desenvolvedor via appsettings.json.
- **Não incluído:** sincronização bidirecional (Jira → Sensr); atualização de campos além de status para cards já migrados; migração de cards sem prefixo `#ID` no summary; desenvolvimento de UI/UX (projeto sem front-end).

Detalhamento em REQ-AASPGOV01-001.

## 3. Adaptação do processo (GPR 2)

O processo-padrão (PRO-GPC-001) foi adaptado a este projeto conforme o GUIA-GPC-001. Registro completo em ADAP-AASPGOV01-001. Principais decisões:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Design UX/UI | Não aplicável | Projeto de back-end / serviço sem interface de usuário |
| Nível de documentação | Padrão | Projeto de pequeno porte (~7 semanas), integração crítica entre duas ferramentas de gestão |
| Estimativa e cadência | Execução por horas (fases waterfall); backlog modelado retroativamente em sprints e story points (4 sprints, ~59 SP) para evidência ágil e carga no Jira | Concilia a gestão real por fases com a rastreabilidade ágil exigida na avaliação |
| Combinação de papéis | Tech Lead acumula Arquiteto | Projeto de pequeno porte com escopo bem delimitado; não justifica papel dedicado de Arquiteto separado |
| Ambiente de stage | Não adotado — homologação contra APIs reais | Comportamento crítico depende da compatibilidade real entre Sensr e Jira; mocks não seriam representativos |

## 4. Estimativas (GPR 3, 4)

O projeto foi estimado e acompanhado por **horas de esforço** registradas por fase. Para a evidência de gestão ágil e a carga no Jira, o backlog foi **modelado retroativamente** em **~20 histórias / ~59 SP** derivadas dos requisitos (RF01–RF11 + RNF01–RNF06), distribuídas em **4 sprints de 2 semanas** com velocity média de ~15 SP/sprint, conciliadas com as horas reais. Detalhamento em GEST-AASPGOV01-001 (abas Backlog, Tarefas e Acompanhamento) e em ADAP-AASPGOV01-001.

**Tamanho e prazo**

- **Tamanho estimado:** ~59 SP
- **Velocity de referência:** ~15 SP/sprint
- **Número de sprints:** 4 (Sprint 0 a Sprint 3)
- **Duração:** 7 semanas (14/04/2026 – 02/06/2026)
- **Base histórica utilizada:** projetos Timeware de pequeno porte (.NET, integração de APIs REST)
- **Fator de conversão SP ↔ horas:** 1 SP = 4 h

**Orçamento de horas por papel**

Referência de capacidade: 168 h/mês disponíveis por pessoa (21 dias × 8 h); deduzindo ~28 h de cerimônias ágeis e reuniões (~15%), a capacidade efetiva é de **140 h/mês por FTE** ou **70 h por sprint de 2 semanas por FTE**.

| Papel | Pessoas | Dedicação | h efetivas/sprint | Nº sprints | **h estimadas** |
|---|---|---|---|---|---|
| Gerente de Projeto | 1 | 40% | 28 h | 4 | 112 h (efetiva no projeto: ~16 h registradas) |
| Tech Lead / Arquiteto | 1 | 70% | 49 h | 4 | 196 h (efetiva no projeto: ~40 h registradas) |
| Desenvolvedor Sênior | 1 | 100% | 70 h | 4 | 280 h (efetiva no projeto: ~120 h registradas) |
| Desenvolvedor (Suporte) | 1 | 80% | 56 h | 3 (S1–S3) | 168 h (efetiva no projeto: ~40 h registradas) |
| QA | 1 | 80% | 56 h | 1 (S3) | 56 h (efetiva no projeto: ~16 h registradas) |
| DevOps | 1 | 20% | 14 h | 4 | 56 h (efetiva no projeto: ~4 h registradas) |
| **Total estimado** | | | | | **216 h** (planejado) / **236 h** (realizado) |

> *Referência de cálculo:* h efetivas/sprint = 70 h × (% dedicação). Ex.: Dev 100% = 70 h/sprint; GP 40% = 28 h/sprint. Os totais informados refletem o esforço efetivamente registrado por papel dentro do projeto AASP_GOV (escopo de pequeno porte), não a capacidade total disponível dos profissionais.

**Esforço estimado × realizado por fase**

| Fase | Esforço estimado (h) | Esforço realizado (h) | Variação |
|---|---|---|---|
| Fase 1 — Arquitetura | 16 | 16 | 0% |
| Fase 2 — Mapeamento e Autenticação | 40 | 44 | +10% |
| Fase 3 — Desenvolvimento dos Serviços | 120 | 128 | +6,7% |
| Fase 4 — Homologação e Correções | 40 | 48 | +20% |
| **Total** | **216** | **236** | **+9,3%** |

## 5. Cronograma, marcos e orçamento (GPR 5)

**Marcos**

| Marco | Data prevista | Data realizada | Situação |
|---|---|---|---|
| Kickoff (abertura) | 14/04/2026 | 14/04/2026 | ✅ Realizado (ATA-AASPGOV01-001) |
| Fim do Mapeamento de APIs (Fase 2) | 23/04/2026 | 23/04/2026 | ✅ Realizado (ATA-AASPGOV01-002) |
| Fim do Desenvolvimento (Fase 3) | 20/05/2026 | 20/05/2026 | ✅ Realizado |
| Validação de homologação | 29/05/2026 | 29/05/2026 | ✅ Realizado (ATA-AASPGOV01-003) |
| Aceite e encerramento | 02/06/2026 | 02/06/2026 | ✅ Realizado (ATA-AASPGOV01-004 + TAE-AASPGOV01-001) |

**Estrutura de sprints (modelagem retroativa)**

| Sprint | Período | SP | Foco |
|---|---|---|---|
| Sprint 0 — Setup & Mapeamento | 14/04 – 24/04/2026 | 15 SP | Arquitetura 3 camadas + mapeamento APIs Sensr/Jira + autenticação |
| Sprint 1 — Core de Migração | 27/04 – 08/05/2026 | 16 SP | RF02, RF03, RF04, RF07, RF08, RF09 (criação Epic/Task/Subtask) |
| Sprint 2 — Sincronização | 11/05 – 22/05/2026 | 16 SP | RF05, RF06, RF11, RNF01, RNF02, RNF03 (sync incremental + idempotência) |
| Sprint 3 — Homologação | 25/05 – 02/06/2026 | 12 SP | Correção BUG-01 a BUG-05 + validação CA01–CA07 |
| **Total** | 7 semanas | **59 SP** | |

**Orçamento total**

| Item | Valor |
|---|---|
| Horas totais estimadas | 216 h |
| Horas realizadas | 236 h |
| Período | 14/04/2026 a 02/06/2026 |
| Sprints | 4 sprints de 2 semanas (Sprint 3 com ~1,5 sem) |

## 6. Recursos (GPR 6, 7)

- **Equipe:** Abraão Oliveira (Gerente de Projeto, todas as fases); Cezar Hiraki (Tech Lead/Arquiteto, todas as fases); Raony Chagas (Desenvolvedor Sênior, todas as fases); Allan Alves (Desenvolvedor de Suporte, Fases 2–4); Caroline Sousa (Analista de Testes, Fase 4); Lucas Batista (Infraestrutura/DevOps, Fases 1 e 4).
- **Ambiente e ferramentas:**
  - **Controle de versão / CI/CD:** Azure DevOps (repositório `SensrJiraSync` + pipeline)
  - **Hospedagem do serviço:** Azure (Scheduled Job em ambiente Windows)
  - **Gestão de tarefas e backlog:** Jira (carga retroativa via JIRA-AASPGOV01_Backlog-Import.csv)
  - **Plataforma alvo da migração:** Jira (workspace AASP)
  - **Plataforma fonte da migração:** Sensr (workspace AASP)
  - **Frameworks / Bibliotecas:** .NET 8, Microsoft.Extensions.* (DI, configuração, logging), HtmlAgilityPack (parsing HTML), Newtonsoft.Json (serialização JSON)
  - **Ambiente de homologação:** workspaces de teste do Sensr e do Jira (sem ambiente de stage isolado — homologação contra APIs reais, conforme ADAP §3.3)

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Marcos Correa Fernandez Turnes (Sponsor — AASP) | Validação, homologação e aceite formal | Reuniões de marco (Kickoff, Alinhamento APIs, Validação Homologação, Aceite Final) — 4 atas |
| Abraão Oliveira (GP — Timeware) | Gestão de entregas, comunicação com cliente | Acompanhamento contínuo + reuniões de marco |
| Time de desenvolvimento (Timeware) | Execução técnica e decisões de implementação | Reuniões de alinhamento por sprint; revisão de código via PR no Azure DevOps |
| Jonathan Alves (Auditor GQA — Timeware) | Verificação de aderência ao processo MPS-SW | Auditoria única ao encerramento (ver GQA-AASPGOV01-001) |

## 8. Transição e suporte pós-go-live (GPR 8, GPR 16)

### 8.1 Estratégia de transição para produção

| Item | Descrição |
|---|---|
| **Fluxo de deploy** | Homologação aprovada → publicação manual do executável .NET 8 auto-contido no Azure → configuração do Scheduled Job → verificação da primeira execução |
| **Responsável pela execução do deploy** | Lucas Batista (DevOps) |
| **Aprovador do go-live** | Marcos Correa Fernandez Turnes (Sponsor AASP) + Abraão Oliveira (GP) |
| **Processo de mudança do cliente** | Não aplicável — implantação direta no Azure Scheduler da Timeware (não há GMUD do cliente) |
| **Janela de deploy** | Horário comercial (serviço novo, sem usuários ativos no momento do deploy) |
| **Plano de rollback** | Substituição do artefato pelo executável da baseline anterior (BL-HOM-001) + reativação do agendamento; APIs Sensr e Jira não sofrem alterações (sincronização unidirecional não destrutiva) |

### 8.2 Critérios de prontidão para go-live (go-live readiness)

| Critério | Obrigatório? | Verificado por |
|---|---|---|
| Todos os defeitos críticos (S1) resolvidos | Sim | Caroline Sousa (QA) / Abraão Oliveira |
| Homologação aprovada pelo cliente | Sim | Marcos Correa Fernandez Turnes |
| Documentação de entrega completa (appsettings, endpoints, troubleshooting) | Sim | Cezar Hiraki (Tech Lead) |
| Cenários CT-01 a CT-12 aprovados | Sim | Caroline Sousa (QA) |
| Baseline de configuração registrada (tag de versão) | Sim | Lucas Batista (DevOps) |
| Credenciais e permissões de produção confirmadas | Sim | Lucas Batista (DevOps) |
| Aceite formal do Sponsor registrado em ata | Sim | Abraão Oliveira (GP) |

### 8.3 Suporte e monitoramento pós-go-live

| Item | Descrição |
|---|---|
| **Período de suporte pós-go-live** | 10 dias úteis após o go-live (02/06 a 12/06/2026) |
| **Responsável pela sustentação** | Cezar Hiraki (Tech Lead) + Abraão Oliveira (GP) |
| **Canal de atendimento** | Teams (canal direto com o Sponsor da AASP) + e-mail |
| **SLA de resposta (incidentes críticos S1)** | Resposta em 2 h; resolução em 24 h |
| **SLA de resposta (incidentes S2/S3)** | Resposta em 1 dia útil; resolução em 3 dias úteis |

**O que monitorar no período pós-go-live:**

| Indicador | Fonte | Meta / Limiar de alerta |
|---|---|---|
| Execuções do Azure Scheduled Job com exit code 0 | Logs Azure | 100% (zero falhas no agendamento) |
| Latência de cada execução | Logs Azure | ≤ 30 min por ciclo completo |
| Erros de integração com Sensr ou Jira | Logs estruturados do serviço | Taxa de erro ≤ 1% por desenvolvedor processado |
| Cards duplicados criados no Jira | Verificação manual amostral | 0 duplicatas |

### 8.4 Critério de encerramento do suporte pós-go-live

O período de suporte pós-go-live encerra quando:

- [ ] Período de 10 dias úteis transcorreu sem incidentes S1 abertos; **ou**
- [ ] Todos os incidentes abertos no período foram resolvidos e aceitos pelo cliente.

O encerramento é registrado no Termo de Encerramento e Aceite (TAE-AASPGOV01-001). Incidentes pós-período passam para a fila de manutenção contratual ou são tratados como novo escopo via Change Request.

## 9. Riscos (GPR 10)

Exposição = Probabilidade × Impacto (escala 1–3 por dimensão), conforme EST-GPC-002.

| ID | Risco | Prob. | Impacto | Exposição | Resposta | Status |
|---|---|---|---|---|---|---|
| R-01 | Criação de cards duplicados no Jira por execuções repetidas | 3 | 3 | 9 | Mitigar — verificação de existência pelo prefixo `#ID` no summary antes de qualquer criação | ✅ Controlado |
| R-02 | Diferenças de formato entre modelos de dados das plataformas | 3 | 2 | 6 | Mitigar — camada de transformação dedicada (StatusMapper + HtmlHelper) | ✅ Controlado |
| R-03 | Falha de autenticação de um desenvolvedor interrompendo toda a execução | 2 | 3 | 6 | Mitigar — tratamento de exceção por desenvolvedor no SyncService com continuidade | ✅ Controlado |
| R-04 | Comportamento inconsistente da API Jira para transições de status | 2 | 3 | 6 | Mitigar — consulta prévia das transições disponíveis antes de aplicar; log de aviso | ⚠️ Ocorreu — corrigido (BUG-02) |
| R-05 | Volume elevado de issues no Epic exigindo paginação | 2 | 2 | 4 | Mitigar — paginação via `nextPageToken` no GetIssuesByEpicAsync | ✅ Controlado |
| R-06 | Campos de texto rico do Sensr em HTML incompatível com Jira | 3 | 2 | 6 | Mitigar — HtmlHelper para conversão de HTML para texto plano e serialização para ADF | ⚠️ Ocorreu — corrigido (BUG-01) |

## 10. Viabilidade (GPR 11)

O projeto é viável: o esforço estimado (216 h, ~59 SP) é compatível com a duração planejada de 7 semanas e com a capacidade da equipe alocada. A escolha por uma arquitetura em 3 camadas e a estratégia de identificação por prefixo `#ID` no summary eliminam a necessidade de estado externo e simplificam a lógica de idempotência. Os principais riscos (criação de duplicatas, diferenças entre plataformas) são endereçados por mecanismos técnicos verificáveis (verificação prévia, camada de transformação dedicada). A solução atende a uma necessidade operacional clara da AASP (eliminação de migração manual + garantia de consistência durante a transição) e seu valor é mensurável via número de cards migrados e zero duplicatas em execuções repetidas.

## 11. Aprovação do Plano (GPR 13)

| Envolvido | Papel | Aceite | Data | Ref. da ata |
|---|---|---|---|---|
| Marcos Correa Fernandez Turnes | Sponsor (AASP) | Aprovado | 14/04/2026 | ATA-AASPGOV01-001 (Kickoff) |
| Abraão Oliveira | Gerente de Projeto (Timeware) | Aprovado | 14/04/2026 | ATA-AASPGOV01-001 (Kickoff) |

> A aprovação registrada estabeleceu a **baseline** do projeto em 14/04/2026. O aceite final das entregas foi registrado em 02/06/2026 (ver ATA-AASPGOV01-004 e TAE-AASPGOV01-001).

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Plano consolidado a partir do Registro de Projeto AASP_GOV v2.0 (08/06/2026), seguindo TPL-GPR-001 v1.2. |
