# Matriz de Rastreabilidade — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | RASTR-AASP01-001 |
| **Projeto** | AG — Grupos de Usuários |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Produto** | ms.auxo.usuarios |
| **Repositório** | GitLab · http://191.234.192.153/aasp/ms.auxo.usuarios |
| **GP / Tech Lead** | Abraão (GP) · Cezar Hiraki (TL) — Timeware Brasil |
| **Desenvolvedores** | Renan Kiyoshi, Henry Komatsu, Mateus Veloso — Timeware Brasil |
| **PO** | Marcos Turnes — AASP |
| **QA** | Leonardo Francisco Pereira — AASP |
| **Data base** | 01/07/2026 |
| **Versão** | 1.4 |
| **Status** | Ativo |

---

## 1. Objetivo

Registrar a rastreabilidade entre histórias do Jira (AG-XX), requisitos funcionais e não funcionais, endpoints implementados, Merge Requests do GitLab, casos de teste e status de entrega. Este documento evidência o atributo de rastreabilidade exigido pelo processo GPR e pelo processo de Gerência de Requisitos (GRE) do nível C do MPS.BR, garantindo que cada requisito possa ser rastreado desde sua origem até a entrega verificada. Os endpoints referem-se ao controller real `GerenciarGruposController` (rota base `api/gerenciar/grupos`).

---

## 2. Rastreabilidade — Requisitos Funcionais

| Req. (RF) | História Jira | Descrição | Endpoint(s) | MR(s) | Casos de Teste | Sprint | Status |
|---|---|---|---|---|---|---|---|
| RF-01 | AG-20 | Criar grupo de usuários | POST incluirgrupo | MR !1 | GRP-01, GRP-07 | S1 | ✅ Entregue |
| RF-02 | AG-20 | Listar grupos e consultar usuários do grupo | GET listargrupo · GET buscargrupoporid | MR !1 | GRP-02, GRP-03 | S1 | ✅ Entregue |
| RF-03 | AG-20 | Alterar grupo e ativar/desativar | POST alterargrupo · POST ativardesativar | MR !2 | GRP-04, GRP-06 | S1 | ✅ Entregue |
| RF-04 | AG-20 | Excluir grupo (com notificação opcional) | POST excluirgrupo | MR !2 | GRP-05 | S1 | ✅ Entregue |
| RF-05 | AG-21 | Definir função do usuário no grupo (Usuario/Administrador) | POST alterarfuncaodousuario | MR !3 | FUNC-01 | S1 | ✅ Entregue |
| RF-06 | AG-22 | Vincular usuário (lista de membros) e remover usuário do grupo | POST incluirgrupo/alterargrupo (GrupoDeUsuarios) · POST removerusuario | MR !4, MR !5 | VINC-01, VINC-02 | S1 | ✅ Entregue |
| RF-07 | AG-23 | Registrar auditoria de ações em AuditoriaGrupos | `auditoria` (interceptor de escrita) | MR !6 | AUD-01, AUD-02 | S2 | ✅ Entregue — aceite 20/06/2026 |
| RF-08 | AG-24 | Integrar com ms.temis.vinculos | HTTP REST `api/gerenciar/grupos/vinculados` (ms.temis.vinculos) | MR !7 | INT-01, INT-02 | S2 | ✅ Entregue — aceite 20/06/2026 |
| RF-09 | AG-25 | Gerar relatório consolidado de grupos | *(planejado — não implementado)* | MR pendente | REL-01 | S3 | 📅 Planejado |

### 2.1 Rastreabilidade — Requisitos Não Funcionais

| Req. (RNF) | Descrição | Escopo | MR(s) | Sprint | Caso de Teste / Validação | Status |
|---|---|---|---|---|---|---|
| RNF-01 | Tempo de resposta ≤ 500 ms em condições normais de carga | Todos os endpoints | — | S1–S3 | Validado via Swagger/testes de performance (resultado obtido: ≤ 280 ms) | ✅ Validado |
| RNF-02 | Autenticação e autorização via JWT Bearer Token | Todos os endpoints | MR !1 | S1 | Validado em code review e testes de integração | ✅ Validado |
| RNF-03 | Rastreabilidade de ações via auditoria (AuditoriaGrupos) | Operações de escrita | MR !6 | S2 | AUD-01, AUD-02 — executados e aprovados em 20/06/2026 | ✅ Validado |

---

## 3. Cobertura por Sprint

| Sprint | Período | RFs Cobertos | Casos de Teste Executados | Aprovados | Status |
|---|---|---|---|---|---|
| S1 | 26/05–06/06/2026 | RF-01, RF-02, RF-03, RF-04, RF-05, RF-06 | 10 (GRP-01 a GRP-07, FUNC-01, VINC-01, VINC-02) | 10/10 (100%) | ✅ Aceite formal 06/06/2026 |
| S2 | 09/06–20/06/2026 | RF-07, RF-08 | AUD-01, AUD-02, INT-01, INT-02 (4 cenários) | 4/4 (100%) | ✅ Aceite formal 20/06/2026 |
| S3 | 23/06–04/07/2026 | RF-09 | REL-01 (planejado) | — | 📅 Planejado |

---

## 4. Itens Rastreados sem Cobertura de Teste Concluída

Os itens abaixo possuem requisito definido e rastreabilidade registrada, mas ainda não possuem casos de teste executados e aprovados, pois estão em sprint futura e ainda não foram implementados no código.

| História | Requisito | Caso de Teste | Motivo da Pendência | Sprint Prevista |
|---|---|---|---|---|
| AG-25 | RF-09 (Relatório consolidado + CSV) | REL-01, REL-02 | Escopo planejado para S3; em desenvolvimento desde 23/06/2026 | S3 (23/06–04/07/2026) |

---

## 5. Resumo de Cobertura

- **Requisitos funcionais entregues:** 8 de 9 (89%) — RF-01 a RF-08 com aceite formal (S1: 06/06/2026; S2: 20/06/2026)
- **Requisitos funcionais em execução:** 1 de 9 (11%) — RF-09 em andamento na S3
- **Requisitos não funcionais validados:** 3 de 3 (100%) — RNF-01, RNF-02 validados em S1; RNF-03 validado em S2 (AUD-01, AUD-02)
- **Casos de teste Sprint 1:** 10 de 10 (100%) aprovados por Leonardo Francisco Pereira (AASP)
- **Casos de teste Sprint 2:** 4 de 4 (100%) aprovados por Leonardo Francisco Pereira (AASP)
- **Rastreabilidade req → teste:** 100% para todos os requisitos entregues (RF-01 a RF-08)
- **Rastreabilidade req → MR:** 100% para requisitos entregues (MRs !1, !2, !3, !4, !5, !6, !7)

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão | Versão inicial — estrutura da matriz com requisitos RF-01 a RF-09 e RNF-01 a RNF-03 |
| 1.1 | 09/06/2026 | Abraão | Atualizado pós-Sprint 1: MRs !1 a !5 registrados, status de entrega e resultados dos casos de teste incorporados |
| 1.2 | 15/06/2026 | Abraão | Endpoints, casos de teste e cobertura alinhados à API real (GerenciarGruposController) |
| 1.3 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
| 1.4 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: RF-07 e RF-08 marcados como entregues (MRs !6 e !7, aceite 20/06/2026); cenários AUD-01/AUD-02/INT-01/INT-02 adicionados; RNF-03 validado; Sprint 2 cobertura atualizada; resumo percentuais corrigidos (89% entregues). |
