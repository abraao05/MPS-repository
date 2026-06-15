# Matriz de Rastreabilidade — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | RASTR-AASP01-001 |
| **Projeto** | AG — Grupos de Usuários |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Produto** | ms.auxo.gruposusuarios |
| **Repositório** | Azure DevOps · komatsuhenry67/gerenciador-aasp/ms.auxo.gruposusuarios |
| **GP / Tech Lead** | Abraão (GP) · Cezar Hiraki (TL) — Timeware Brasil |
| **Desenvolvedores** | Renan Kiyoshi, Henry Komatsu, Mateus Veloso — Timeware Brasil |
| **PO** | Marcos Turnes — AASP |
| **QA** | Leonardo Francisco Pereira — AASP |
| **Data base** | 26/05/2026 |
| **Versão** | 1.1 |
| **Status** | Ativo |

---

## 1. Objetivo

Registrar a rastreabilidade entre histórias do Jira (AG-XX), requisitos funcionais e não funcionais, endpoints implementados, Pull Requests do Azure DevOps, casos de teste e status de entrega. Este documento evidencia o atributo de rastreabilidade exigido pelo processo GPR e pelo processo de Gerência de Requisitos (GRE) do nível C do MPS.BR, garantindo que cada requisito possa ser rastreado desde sua origem até a entrega verificada.

---

## 2. Rastreabilidade — Requisitos Funcionais

| Req. (RF) | História Jira | Descrição | Endpoint(s) | PR(s) | Casos de Teste | Sprint | Status |
|---|---|---|---|---|---|---|---|
| RF-01 | AG-20 | Criar grupo de usuários (POST) | POST /grupos | PR #11 | GRP-01 | S1 | ✅ Entregue |
| RF-02 | AG-20 | Listar e consultar grupos (GET) | GET /grupos · GET /grupos/{id} | PR #11 | GRP-02, GRP-03 | S1 | ✅ Entregue |
| RF-03 | AG-20 | Atualizar dados de grupo (PUT) | PUT /grupos/{id} | PR #12 | GRP-04 | S1 | ✅ Entregue |
| RF-04 | AG-20 | Remover grupo com soft delete (DELETE) | DELETE /grupos/{id} | PR #12 | GRP-05 | S1 | ✅ Entregue |
| RF-05 | AG-21 | Gerenciar permissões RBAC do grupo (PUT) | PUT /grupos/{id}/permissoes | PR #13 | PERM-01, PERM-02 | S1 | ✅ Entregue |
| RF-06 | AG-22 | Vincular e desvincular usuário de grupo (POST/DELETE) | POST /grupos/{id}/usuarios · DELETE /grupos/{id}/usuarios/{uid} | PR #14, PR #15 | VINC-01, VINC-02, VINC-03 | S1 | ✅ Entregue |
| RF-07 | AG-23 | Registrar auditoria de ações em AuditoriaGrupos | (interno — tabela AuditoriaGrupos) | PR pendente | AUD-01 | S2 | ⏳ Em andamento |
| RF-08 | AG-24 | Integrar com ms.temis.vinculos via HTTP POST | HTTP POST ms.temis.vinculos/api/vinculos | PR pendente | INT-01 | S2 | ⏳ Em andamento |
| RF-09 | AG-25 | Gerar relatório consolidado de grupos e usuários (GET) | GET /grupos/relatorio | PR pendente | REL-01 | S3 | 📅 Planejado |

### 2.1 Rastreabilidade — Requisitos Não Funcionais

| Req. (RNF) | Descrição | Escopo | PR(s) | Sprint | Caso de Teste / Validação | Status |
|---|---|---|---|---|---|---|
| RNF-01 | Tempo de resposta ≤ 500 ms em condições normais de carga | Todos os endpoints | — | S1–S3 | Validado via Swagger/testes de performance (resultado obtido: ≤ 280 ms) | ✅ Validado |
| RNF-02 | Autenticação e autorização via JWT Bearer Token | Todos os endpoints | PR #11 | S1 | Validado em code review e testes de integração | ✅ Validado |
| RNF-03 | Rastreabilidade de ações via tabela AuditoriaGrupos | Operações de escrita (POST, PUT, DELETE) | PR pendente | S2 | AUD-01 — pendente conclusão de AG-23 | ⏳ Pendente |

---

## 3. Cobertura por Sprint

| Sprint | Período | RFs Cobertos | Casos de Teste Executados | Aprovados | Status |
|---|---|---|---|---|---|
| S1 | 26/05–06/06/2026 | RF-01, RF-02, RF-03, RF-04, RF-05, RF-06 | 10 (GRP-01 a GRP-05, PERM-01, PERM-02, VINC-01, VINC-02, VINC-03) | 10/10 (100%) | ✅ Aceite formal 06/06/2026 |
| S2 | 09/06–20/06/2026 | RF-07, RF-08 | AUD-01, INT-01 (em construção) | — | ⏳ Em andamento |
| S3 | 23/06–04/07/2026 | RF-09 | REL-01 (planejado) | — | 📅 Planejado |
| S4 | 07/07–11/07/2026 | Validação final (todos os RFs) | Regressão completa | — | 📅 Planejado |

---

## 4. Itens Rastreados sem Cobertura de Teste Concluída

Os itens abaixo possuem requisito definido e rastreabilidade registrada, mas ainda não possuem casos de teste executados e aprovados, pois estão em sprints em andamento ou futuras.

| História | Requisito | Caso de Teste | Motivo da Pendência | Sprint Prevista |
|---|---|---|---|---|
| AG-23 | RF-07 (Auditoria) | AUD-01 | Triggers de auditoria em revisão de code review; implementação ~70% concluída | S2 (09/06–20/06/2026) |
| AG-24 | RF-08 (Integração ms.temis) | INT-01 | Cliente HTTP implementado; testes de integração em construção; contrato de API definido | S2 (09/06–20/06/2026) |
| AG-25 | RF-09 (Relatório consolidado) | REL-01 | Escopo planejado para S3; depende de AG-23 e AG-24 concluídos | S3 (23/06–04/07/2026) |

---

## 5. Resumo de Cobertura

- **Requisitos funcionais entregues:** 6 de 9 (67%) — RF-01 a RF-06 com aceite formal em S1
- **Requisitos funcionais em execução:** 2 de 9 (22%) — RF-07 e RF-08 em andamento na S2
- **Requisitos funcionais planejados:** 1 de 9 (11%) — RF-09 previsto para S3
- **Requisitos não funcionais validados:** 2 de 3 (67%) — RNF-01 e RNF-02 validados em S1
- **Requisitos não funcionais pendentes:** 1 de 3 (33%) — RNF-03 depende da conclusão de AG-23 (S2)
- **Casos de teste Sprint 1:** 10 de 10 (100%) aprovados por Leonardo Francisco Pereira (AASP)
- **Rastreabilidade req → teste:** 100% para todos os requisitos entregues até S1
- **Rastreabilidade req → PR:** 100% para requisitos entregues (PRs #11, #12, #13, #14, #15)

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão | Versão inicial — estrutura da matriz com requisitos RF-01 a RF-09 e RNF-01 a RNF-03 |
| 1.1 | 09/06/2026 | Abraão | Atualizado pós-Sprint 1: PRs #11 a #15 registrados, status de entrega e resultados dos casos de teste incorporados |
