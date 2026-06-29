# Plano de Projeto — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | PLA-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.2 |
| **Data** | 26/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Tech Lead / Arquiteto / DevOps** | Cézar Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Desenvolver a plataforma MilhasFacil, solução de busca e alerta de passagens por milhas que consulta em paralelo Smiles, Azul e Latam, com cadastro/login JWT, histórico paginado, rotas favoritas com alertas e notificação WhatsApp. A solução é composta por três aplicações: API (Spring Boot 3.2.5 / Java 21, base `/api/v1`, JWT HS256 stateless), Web (Angular 17.3 standalone / Tailwind 3.4) e Crawler (FastAPI 0.111 / SeleniumBase 4.27.4).

A fonte da verdade de gestão deste projeto é a planilha `GEST-MILHASFACIL01-001` (xlsx), da qual derivam os valores de sprint, medição e riscos deste plano.

## 2. Escopo (GPR 1)

- **Incluído:** RF01 a RF15. Em síntese: cadastro BCrypt (RF01), login JWT access+refresh (RF02), busca paralela Smiles/Azul/Latam (RF03), SearchPage skeleton (RF04), histórico paginado (RF05), rotas favoritas + alertas (RF06), perfil GET/PATCH `/users/me` (RF07), alertas Spring Scheduler (RF08), WhatsApp Z-API (RF09), assinaturas BASIC/PRO/ENTERPRISE (RF10), refresh token rotation (RF11), logout blacklist Redis jti (RF12), filtros avançados maxMiles/cabinType (RF13), export CSV UTF-8 BOM (RF14), push PWA (RF15).
- **Não incluído:** telas de perfil/alertas/assinatura no front-end web; integração com programas além de Smiles, Azul e Latam.

## 3. Adaptação do processo (GPR 2)

Detalhamento completo em `ADAP-MILHASFACIL01-001_Registro-de-Adaptacao.md`. Resumo:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Cadência de entrega | Sprints de 2 semanas | Equipe enxuta (3 desenvolvedores efetivos); previsibilidade de entrega |
| Pipeline de CI | Docker (runner-vm-docker) no GitLab CI/CD | Padronização do agente disponível; risco R-05 |
| Controle de versão | GitLab — repositórios MilhasFacil_api, MilhasFacil_web, MilhasFacil_crawler (branch padrão main) | Três aplicações independentes |
| Gate de cobertura | Ativado a partir da Sprint 4 (JaCoCo 80% na API) | NC-001 (cobertura <80%) tratada com gate de CI |
| Gestão de backlog | Jira (board 614) + planilha GEST-MILHASFACIL01-001 | Rastreabilidade e gestão consolidada |

## 4. Estimativas e orçamento de esforço (GPR 3, 4)

- **Modelo de sprints:** iterações de 2 semanas, 12 sprints (S1–S12).
- **Duração total:** 09/02/2026 a 26/07/2026.
- **Velocity média (S1–S8):** 33,9 SP por sprint.

**Composição da equipe por papel (base do esforço):**

| Papel | Pessoas | No DevOps? |
|---|---|---|
| Gerente de Projeto (gestão; não codifica) | 1 (Abraão) | Não |
| Tech Lead / Arquiteto / DevOps (revisor de MR) | 1 (Cézar Velazquez) | Sim |
| Desenvolvedor | 3 (Felipe Santos, Lucas Batista, Henry Oliveira) | Sim |
| QA (teste manual; gera evidências) | 1 (Jonathan Alves) | Sim |
| GQA independente (auditoria de processo) | 1 (Carol/Caroline) | Não |

> **DevOps (GitLab) = 5 pessoas:** Cézar (TL) + Felipe/Lucas/Henry (devs) + Jonathan (QA). Abraão (GP) e Carol (GQA) ficam fora do DevOps. Detalhamento dos papéis e da combinação em `ADAP-MILHASFACIL01-001` (A-06) e §6 deste plano.

**Orçamento de esforço — controle por sprint/equipe (decisão de adaptação):** o esforço do projeto é estimado e acompanhado **por sprint, no nível da equipe** (story points → horas planejadas vs. realizadas), e **não é decomposto por papel**. Essa é uma decisão de adaptação coerente com a equipe enxuta e com a fonte da verdade de gestão (planilha `GEST-MILHASFACIL01-001`), que registra a série de horas por sprint (§5.1), não por pessoa/papel. O total estimado do ciclo planejado é de **614 h** (S1–S8), com **666 h** realizadas (+8,5%).

**Acumulado realizado S1–S8 (planilha §7):**

| Métrica | Valor |
|---|---|
| SP planejado (S1–S8) | 309 |
| SP real (S1–S8) | 271 |
| Carry acumulado | 38 |
| Horas estimadas | 614 |
| Horas reais | 666 (+8,5%) |

A série de horas estimadas e realizadas **por sprint** (S1–S8, com S9 em WIP) consta na §5.1.

## 5. Cronograma e marcos (GPR 5)

### 5.1 Sprints — WBS por sprint, SP e horas

| Sprint | Período | SP plan | SP real | Aderência | Carry | h_est | h_real | Desvio h | Entregas (WBS) |
|---|---|---|---|---|---|---|---|---|---|
| S1 | 09–22/02/2026 | 23 | 20 | 87% | 3 | 40 | 45 | +12% | RF01 cadastro BCrypt; RF02 login JWT; SearchPage inicial |
| S2 | 23/02–08/03/2026 | 40 | 35 | 88% | 5 | 80 | 88 | +10% | RF03 busca paralela; RF04 skeleton |
| S3 | 09–22/03/2026 | 38 | 34 | 89% | 4 | 76 | 82 | +8% | RF05 histórico paginado; RF06 rotas favoritas+alertas |
| S4 | 23/03–05/04/2026 | 45 | 41 | 91% | 4 | 88 | 93 | +6% | RF07 perfil; RF08 alertas Scheduler; gate de cobertura |
| S5 | 06–19/04/2026 | 35 | 33 | 94% | 2 | 76 | 80 | +5% | RF10 assinaturas; RF11 refresh rotation |
| S6 | 20/04–03/05/2026 | 33 | 30 | 91% | 3 | 72 | 78 | +9% | Estabilização e observabilidade |
| S7 | 04–17/05/2026 | 37 | 30 | 81% | 7 | 70 | 76 | +9% | RF09 WhatsApp Z-API |
| S8 | 18–31/05/2026 | 58 | 48 | 83% | 10 | 112 | 124 | +11% | RF12 logout blacklist Redis; correção de parsers (MF-59) |
| S9 | 01–14/06/2026 | 69 | WIP | WIP | WIP | 138 | WIP | WIP | RF13 filtros avançados e RF14 export CSV entregues; MF-64 airport ILIKE entregue; release v0.9.0 promovida a main |
| S10 | 15–28/06/2026 | 40 | — | — | — | — | — | — | RF15 push PWA (não iniciada) |
| S11 | 29/06–12/07/2026 | 35 | — | — | — | — | — | — | Refinamentos e testes (não iniciada) |
| S12 | 13–26/07/2026 | 30 | — | — | — | — | — | — | Fechamento e entrega (não iniciada) |
| **Total S1–S8** | | **309** | **271** | | **38** | **614** | **666** | **+8,5%** | |

### 5.2 Baselines de versão

| Baseline | Sprint | Situação |
|---|---|---|
| v0.1.0 … v0.8.0 | S1 … S8 | Liberadas |
| v0.9.0 | S9 | Released em main (tag nos três repositórios, 15/06/2026) |

A baseline da S9 foi promovida de develop para main na release **v0.9.0** (develop→homolog→main nos três repositórios, com tag v0.9.0), entregando RF13 (filtros avançados maxMiles/cabinType), RF14 (export CSV UTF-8 BOM) e MF-64 (airport ILIKE).

## 6. Recursos (GPR 6, 7)

**Equipe Timeware:**

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto (gestão; não codifica; fora do DevOps) | Abraão | Gestão, comunicação e aprovação de escopo/CR |
| Tech Lead / Arquiteto / DevOps (revisor de MR; no DevOps) | Cézar Velazquez | Arquitetura, infraestrutura, pipelines, Docker Compose e aprovação de PRs |
| Dev Backend Principal (API + crawlers; no DevOps) | Felipe Santos | Integral |
| Full Stack (no DevOps) | Lucas Batista | Integral (S1 Angular; S2+ backend) |
| Full Stack (no DevOps) | Henry Oliveira | Integral (S3 Angular; S4+ backend) |
| QA (teste manual; gera evidências; no DevOps) | Jonathan Alves | Execução de testes manuais e geração de evidências |
| GQA independente (auditoria; não codifica; fora do DevOps) | Carol (Caroline) | Auditorias de processo (GQA) |

> DevOps (GitLab) = 5 pessoas: Cézar (TL) + Henry/Lucas/Felipe (devs) + Jonathan (QA). Abraão (GP) e Carol (GQA) ficam fora do DevOps.

**Ambiente e ferramentas:**

| Ferramenta / Ambiente | Uso |
|---|---|
| GitLab CI/CD (MilhasFacil_api, MilhasFacil_web, MilhasFacil_crawler) | Repositórios, PRs e pipelines (Docker, runner-vm-docker) |
| Jira (board 614) | Gestão de backlog e sprints |
| Planilha GEST-MILHASFACIL01-001 | Fonte da verdade de gestão |
| Redis | Blacklist de tokens (`token:invalidated:`, TTL 7 dias) |
| Z-API (WhatsApp) | Notificação de alertas |
| Docker Compose | Disponibilidade dos serviços |

## 7. Partes interessadas e comunicação (GPR 9)

Partes interessadas conforme `TAP-MILHASFACIL01-001` §5:

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| PO Hub de Milhas (cliente) | Priorização do backlog, valor de negócio e aprovação de escopo/CR | Relatório de status periódico (RAC) do GP; reuniões/entregas por sprint (Planning/Review); aprovação de CR |
| Gerente de Projeto (Abraão) | Gestão, prazo, escopo e comunicação | Daily (Teams); consolidação do RAC; ponto de contato com o PO |
| Tech Lead / Arquiteto / DevOps (Cézar Velazquez) | Arquitetura, infraestrutura, pipelines e aprovação técnica de MR | Daily (Teams); Sprint Planning/Review/Retrospectiva |
| Equipe de desenvolvimento e QA (Felipe, Lucas, Henry, Jonathan) | Execução das entregas e evidências de teste | Daily (Teams); cerimônias de sprint |
| GQA independente (Carol/Caroline) | Auditoria de processo (conformidade) | Auditorias de GQA por ciclo |

**Cadência (conforme ATA-MILHASFACIL01-001 §3.5):**

| O quê | Para quem | Frequência |
|---|---|---|
| Daily | Equipe Timeware | Dias úteis (Microsoft Teams, canal dedicado) |
| Sprint Planning / Review / Retrospectiva | Equipe + PO | Início e fechamento de cada sprint (2 semanas) |
| Relatório de status (RAC-MILHASFACIL01-001) | PO Hub de Milhas | Periódico (instrumento de acompanhamento do GP ao cliente) |
| Aprovação de mudança de escopo (CR) | GP ↔ PO | Sob demanda (antes da implementação) |

## 8. Modelo de sprints

- Iterações de 2 semanas, com planejamento, execução e revisão por sprint.
- Política de branches: MR obrigatório para develop, aprovação de MR pelo Tech Lead (Cézar Velazquez), gate de CI e nomenclatura `feat/`|`fix/` + `MF-XX`. Na S9 foi ativada a **política de branches protegidas** de revisor (≥1 revisor) em develop nos três repositórios. A aprovação de escopo/CR é do GP (Abraão).
- Gate de cobertura (≥80% JaCoCo/Karma/pytest) ativo a partir da Sprint 4.
- Baselines de versão por sprint (v0.1.0 … v0.8.0; **v0.9.0** released em main na S9).

## 9. Transição e suporte pós-go-live (GPR 8, GPR 16)

> **Projeto ABERTO (Sprint 10 de 12).** O encerramento formal e o aceite ocorrerão ao fim do projeto (término previsto em **26/07/2026**), quando serão emitidos a Ata de Aceite Final (ATA-MILHASFACIL01-003) e o Termo de Encerramento e Aceite (TAE-MILHASFACIL01-001), ainda não aplicáveis nesta fase (ver `00_INDICE-MILHASFACIL01`, Onda 3).

### 9.1 Estratégia de transição para produção

A passagem para produção segue a esteira de promoção definida na gerência de configuração (`GCO-MILHASFACIL01-001` §4) e na estratégia de integração (`ITP-MILHASFACIL01-001`):

| Item | Descrição |
|---|---|
| **Fluxo de promoção** | `develop` (integração) → `homolog` (homologação) → `main` (produção), nos três repositórios (`MilhasFacil_api`, `MilhasFacil_web`, `MilhasFacil_crawler`) |
| **Versionamento** | Tag de versão semântica por release (`v0.1.0`–`v0.9.0`); a release v0.9.0 foi promovida a `main` (tag nos três repositórios, 15/06/2026) |
| **Política de revisão** | MR obrigatório para `develop` com aprovação técnica do Tech Lead (Cézar Velazquez) e **proteção de branch com revisores obrigatórios (≥1 revisor)** ativada em `develop` na S9, impedindo merge sem revisão |
| **Verificação de prontidão** | Smoke checks por *healthcheck*: `/actuator/health` (API, Spring Boot Actuator) e `GET /health` (Crawler) respondendo com sucesso; pipelines verdes (Docker, runner-vm-docker) e gate de cobertura JaCoCo ≥80% na API — condições verificadas antes da promoção entre ambientes |
| **Responsável pela operação de promoção** | Tech Lead / Arquiteto / DevOps (Cézar Velazquez) |
| **Aprovação de escopo/entrega** | Gerente de Projeto (Abraão); validação funcional manual da QA (Jonathan Alves) em homologação |

### 9.2 Definição de pronto (prontidão de entrega)

Uma entrega é considerada pronta para promoção quando atende, de forma cumulativa (conforme `ITP-MILHASFACIL01-001` §5–§7 e `VV-MILHASFACIL01-001` §7):

- Critério de aceite do requisito (RF) atendido e caso de teste correspondente **Aprovado** (validação manual da QA em homologação);
- MR revisado e aprovado pelo Tech Lead, com **gate de CI verde** e cobertura ≥80% na API (a partir da S4);
- *Healthcheck* dos componentes respondendo (`/actuator/health`, `GET /health`);
- Baseline marcada por tag de versão e promovida `develop` → `homolog` → `main`.

### 9.3 Suporte pós-go-live e encerramento

O projeto ainda **não teve release de produção formalizada ao cliente** (o ciclo opera em homologação/`develop`→`main` com a release v0.9.0; não há, até a S9, registro de defeito em produção — `MED-MILHASFACIL01-001` M6). Não há, na documentação do projeto, SLA de suporte, janela de plantão ou canal de atendimento de produção definidos; **o suporte pós-go-live seguirá as condições contratuais/de garantia** acordadas com o Hub de Milhas. O **plano de transição detalhado** (período de acompanhamento, responsáveis, critérios de encerramento do suporte e eventuais SLAs) será **consolidado no Termo de Encerramento e Aceite (TAE-MILHASFACIL01-001)** ao fim do projeto (~26/07/2026), junto ao aceite formal.

## 10. Riscos (GPR 10)

| ID | Risco | Prob. | Impacto | Exposição | Resposta / status |
|---|---|---|---|---|---|
| R-01 | Redesign das companhias quebra os parsers | 3 | 3 | 9 | Ocorreu na S8 (MF-59), corrigido |
| R-02 | Cobertura de testes abaixo de 80% | 3 | 3 | 9 | NC-001 (S2–S4), encerrada na S5 (JaCoCo 82%) |
| R-03 | Indisponibilidade da Z-API | 2 | 2 | 4 | Fallback por e-mail |
| R-04 | Mudança de escopo | 2 | 3 | 6 | Tratada via CR-MF-001 |
| R-05 | Pipeline de CI em agente Windows | 2 | 2 | 4 | Padronização com Docker (runner-vm-docker) no GitLab CI/CD |

## 11. Viabilidade (GPR 11)

O projeto está em execução dentro do cronograma macro, com Sprint 10 de 12 em andamento. A velocity média de 33,9 SP (S1–S8) supera a meta de ≥30 SP, com aderência média de SP de ~88% (faixa de 81% a 94% por sprint), e o desvio acumulado de horas (+8,5%) está dentro de faixa gerenciável. A não conformidade de cobertura (NC-001) foi aberta na S2 e encerrada na S5 com o gate de CI ativado na S4, confirmando a viabilidade da abordagem. A promoção da release v0.9.0 a main na S9 (RF13/RF14/MF-64 entregues) consolida a viabilidade do ciclo de entrega.

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S10 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Aderência ao TPL-GPR-001: correção do RF10 (PREMIUM → PRO); inclusão da seção de Transição e suporte pós-go-live (§9, GPR 8/16); plano de comunicação e partes interessadas (§7, GPR 9); orçamento de esforço com composição da equipe por papel e registro do controle de horas por sprint/equipe (§4, GPR 4). Renumeração das seções subsequentes. Uniformização do desvio acumulado de horas para +8,5% (M2), consistente com MED e GEST. |
| 1.2 | 26/06/2026 | Time de Melhoria Contínua | Correção de referências de CI: PowerShell@2/agente Windows substituído por Docker (runner-vm-docker); Azure Pipelines/Azure DevOps substituído por GitLab CI/CD em todas as ocorrências (§3, §6, §9.1, §10/R-05). |
| 1.3 | 29/06/2026 | Auditoria MPS.BR Nível C | Terminologia "PR obrigatório" → "MR obrigatório" em §8 (modelo de sprints) e §9.1 (política de revisão). |
