# Plano de Projeto — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | PLA-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Tech Lead / Arquiteto / DevOps** | Cézar Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Desenvolver a plataforma MilhasFacil, solução de busca e alerta de passagens por milhas que consulta em paralelo Smiles, Azul e Latam, com cadastro/login JWT, histórico paginado, rotas favoritas com alertas e notificação WhatsApp. A solução é composta por três aplicações: API (Spring Boot 3.2.5 / Java 21, base `/api/v1`, JWT HS256 stateless), Web (Angular 17.3 standalone / Tailwind 3.4) e Crawler (FastAPI 0.111 / SeleniumBase 4.27.4).

A fonte da verdade de gestão deste projeto é a planilha `GEST-MILHASFACIL01-001` (xlsx), da qual derivam os valores de sprint, medição e riscos deste plano.

## 2. Escopo (GPR 1)

- **Incluído:** RF01 a RF15. Em síntese: cadastro BCrypt (RF01), login JWT access+refresh (RF02), busca paralela Smiles/Azul/Latam (RF03), SearchPage skeleton (RF04), histórico paginado (RF05), rotas favoritas + alertas (RF06), perfil GET/PATCH `/users/me` (RF07), alertas Spring Scheduler (RF08), WhatsApp Z-API (RF09), assinaturas BASIC/PREMIUM/ENTERPRISE (RF10), refresh token rotation (RF11), logout blacklist Redis jti (RF12), filtros avançados maxMiles/cabinType (RF13), export CSV UTF-8 BOM (RF14), push PWA (RF15).
- **Não incluído:** telas de perfil/alertas/assinatura no front-end web; integração com programas além de Smiles, Azul e Latam.

## 3. Adaptação do processo (GPR 2)

Detalhamento completo em `ADAP-MILHASFACIL01-001_Registro-de-Adaptacao.md`. Resumo:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Cadência de entrega | Sprints de 2 semanas | Equipe enxuta (3 desenvolvedores efetivos); previsibilidade de entrega |
| Pipeline de CI | Agente Windows (Default) com tasks PowerShell@2 | Padronização do agente disponível; risco R-05 |
| Controle de versão | Azure DevOps — repositórios MilhasFacil_api, MilhasFacil_web, MilhasFacil_crawler (branch padrão main) | Três aplicações independentes |
| Gate de cobertura | Ativado a partir da Sprint 4 (JaCoCo 80% na API) | NC-001 (cobertura <80%) tratada com gate de CI |
| Gestão de backlog | Jira (board 614) + planilha GEST-MILHASFACIL01-001 | Rastreabilidade e gestão consolidada |

## 4. Estimativas (GPR 3, 4)

- **Modelo de sprints:** iterações de 2 semanas, 12 sprints (S1–S12).
- **Duração total:** 09/02/2026 a 26/07/2026.
- **Velocity média (S1–S8):** 33,9 SP por sprint.

**Acumulado realizado S1–S8 (planilha §7):**

| Métrica | Valor |
|---|---|
| SP planejado (S1–S8) | 309 |
| SP real (S1–S8) | 271 |
| Carry acumulado | 38 |
| Horas estimadas | 614 |
| Horas reais | 666 (+8,3%) |

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
| **Total S1–S8** | | **309** | **271** | | **38** | **614** | **666** | **+8,3%** | |

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
| Tech Lead / Arquiteto / DevOps (revisor de PR; no DevOps) | Cézar Velazquez | Arquitetura, infraestrutura, pipelines, Docker Compose e aprovação de PRs |
| Dev Backend Principal (API + crawlers; no DevOps) | Felipe Santos | Integral |
| Full Stack (no DevOps) | Lucas Batista | Integral (S1 Angular; S2+ backend) |
| Full Stack (no DevOps) | Henry Oliveira | Integral (S3 Angular; S4+ backend) |
| QA (teste manual; gera evidências; no DevOps) | Jonathan Alves | Execução de testes manuais e geração de evidências |
| GQA independente (auditoria; não codifica; fora do DevOps) | Carol (Caroline) | Auditorias de processo (GQA) |

> DevOps (Azure) = 5 pessoas: Cézar (TL) + Henry/Lucas/Felipe (devs) + Jonathan (QA). Abraão (GP) e Carol (GQA) ficam fora do DevOps.

**Ambiente e ferramentas:**

| Ferramenta / Ambiente | Uso |
|---|---|
| Azure DevOps (MilhasFacil_api, MilhasFacil_web, MilhasFacil_crawler) | Repositórios, PRs e pipelines (PowerShell@2, agente Windows) |
| Jira (board 614) | Gestão de backlog e sprints |
| Planilha GEST-MILHASFACIL01-001 | Fonte da verdade de gestão |
| Redis | Blacklist de tokens (`token:invalidated:`, TTL 7 dias) |
| Z-API (WhatsApp) | Notificação de alertas |
| Docker Compose | Disponibilidade dos serviços |

## 7. Modelo de sprints

- Iterações de 2 semanas, com planejamento, execução e revisão por sprint.
- Política de branches: PR obrigatório para develop, aprovação de PR pelo Tech Lead (Cézar Velazquez), gate de CI e nomenclatura `feat/`|`fix/` + `MF-XX`. Na S9 foi ativada a **branch policy** de revisor (≥1 revisor) em develop nos três repositórios. A aprovação de escopo/CR é do GP (Abraão).
- Gate de cobertura (≥80% JaCoCo/Karma/pytest) ativo a partir da Sprint 4.
- Baselines de versão por sprint (v0.1.0 … v0.8.0; **v0.9.0** released em main na S9).

## 8. Riscos (GPR 10)

| ID | Risco | Prob. | Impacto | Exposição | Resposta / status |
|---|---|---|---|---|---|
| R-01 | Redesign das companhias quebra os parsers | 3 | 3 | 9 | Ocorreu na S8 (MF-59), corrigido |
| R-02 | Cobertura de testes abaixo de 80% | 3 | 3 | 9 | NC-001 (S2–S4), encerrada na S5 (JaCoCo 82%) |
| R-03 | Indisponibilidade da Z-API | 2 | 2 | 4 | Fallback por e-mail |
| R-04 | Mudança de escopo | 2 | 3 | 6 | Tratada via CR-MF-001 |
| R-05 | Pipeline de CI em agente Windows | 2 | 2 | 4 | Padronização com tasks PowerShell@2 |

## 9. Viabilidade (GPR 11)

O projeto está em execução dentro do cronograma macro, com Sprint 9 de 12 em andamento. A velocity média de 33,9 SP (S1–S8) supera a meta de ≥30 SP, com aderência média de SP de ~88% (faixa de 81% a 94% por sprint), e o desvio acumulado de horas (+8,3%) está dentro de faixa gerenciável. A não conformidade de cobertura (NC-001) foi aberta na S2 e encerrada na S5 com o gate de CI ativado na S4, confirmando a viabilidade da abordagem. A promoção da release v0.9.0 a main na S9 (RF13/RF14/MF-64 entregues) consolida a viabilidade do ciclo de entrega.

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
