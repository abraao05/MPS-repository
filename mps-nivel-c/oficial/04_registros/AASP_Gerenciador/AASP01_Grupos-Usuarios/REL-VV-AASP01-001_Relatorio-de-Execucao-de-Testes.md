# Relatório de Execução de Testes (V&V) — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | REL-VV-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.3 |
| **Data** | 23/06/2026 |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | VV (evidência de projeto) |

---

## 1. Objetivo

Registrar os resultados da execução das atividades de Verificação e Validação (V&V) por sprint, incluindo code review, testes de sistema e testes de homologação (UAT), conforme planejado no VV-AASP01-001. Testes unitários e de integração automatizados não se aplicam a este projeto. Este documento é a evidência formal de execução do processo VV do MPS.BR Nível C para o projeto Grupos de Usuários — AASP Gerenciador. Os endpoints referem-se ao controller real `GerenciarGruposController` (rota base `api/gerenciar/grupos`, HTTP 200/400).

---

## 2. Legenda de Status

| Símbolo | Significado |
|---|---|
| OK | Teste executado e aprovado |
| FALHOU | Teste executado e reprovado (requer correção antes do aceite) |
| Em andamento | Sprint em execução — resultados parciais |
| Planejado | Sprint não iniciada — testes ainda não executados |

---

## 3. Sprint 1 — Resultados (26/05–06/06/2026)

### 3.1 Status Geral — Sprint 1

| Item | Valor |
|---|---|
| **Período** | 26/05/2026 a 06/06/2026 |
| **Status** | Concluído — aceite formal em 06/06/2026 |
| **Total Story Points entregue** | 34 SP (100% do planejado — 0% de desvio) |
| **Histórias entregues** | AG-20 (Concluído) / AG-21 (Concluído) / AG-22 (Concluído) |
| **MRs mergeados** | !1, !2, !3, !4, !5 — todos aprovados e mergeados para main |

---

### 3.2 Testes Unitários — Sprint 1

**Não se aplica** — o projeto não possui testes unitários automatizados.

---

### 3.3 Testes de Integração — Sprint 1

**Não se aplica** — o projeto não possui testes de integração automatizados.

---

### 3.4 Testes de Homologação — Sprint 1 (UAT)

**Executados por:** Leonardo Francisco Pereira (AASP — QA/Homologadora)
**Data de execução:** 06/06/2026
**Ambiente:** Homologação AASP — banco auxo3

| ID | História | Cenário de Aceite | Resultado |
|---|---|---|---|
| GRP-01 | AG-20 | Criar grupo com dados válidos (`incluirgrupo`) — HTTP 200, "Grupo incluido com sucesso" | OK |
| GRP-02 | AG-20 | Listar grupos com paginação (`listargrupo`) — retorno correto | OK |
| GRP-03 | AG-20 | Consultar usuários de um grupo (`buscargrupoporid`) — retorno correto | OK |
| GRP-04 | AG-20 | Alterar nome e membros do grupo (`alterargrupo`) — persistência validada | OK |
| GRP-05 | AG-20 | Excluir grupo (`excluirgrupo`) — soft delete `excluido=1`; some da listagem | OK |
| GRP-06 | AG-20 | Ativar/desativar grupo (`ativardesativar`) — campo `ativo` atualizado | OK |
| GRP-07 | AG-20 | Tentar criar grupo com nome duplicado — sad path; HTTP 400 "Grupo já existe" | OK |
| FUNC-01 | AG-21 | Alterar função do usuário no grupo (`alterarfuncaodousuario`) — Usuario→Administrador | OK |
| VINC-01 | AG-22 | Vincular usuários ao grupo (lista de membros) — registros em `grupos_usuarios_vinculos` | OK |
| VINC-02 | AG-22 | Remover usuário do grupo (`removerusuario`) — soft delete do vínculo validado | OK |
| **Total** | | **10 cenários de aceite** | **10/10 (100%) — Meta de 95% ATINGIDA** |

---

### 3.5 Code Review — Sprint 1

| MR | Feature / História | Achados Identificados | Achados Resolvidos | Resultado |
|---|---|---|---|---|
| !1 | `incluirgrupo` / `listargrupo` (AG-20) | 1 — RV-001-01 (P2): falta de validação de unicidade do nome (retornava exceção do banco) | 1 | Aprovado — resolvido antes do merge |
| !2 | `buscargrupoporid` / `alterargrupo` / `excluirgrupo` / `ativardesativar` (AG-20) | 1 — RV-001-02 (P3): retorno de campos desnecessários no DTO de listagem | 1 | Aprovado — resolvido antes do merge |
| !3 | `alterarfuncaodousuario` (AG-21) | 1 — RV-002-01 (P2): ausência de validação do enum de função | 1 | Aprovado — resolvido antes do merge |
| !4 | Vínculo usuário-grupo (AG-22) | 1 — RV-003-01 (P2): falta de verificação de vínculo duplicado antes do INSERT | 1 | Aprovado — resolvido antes do merge |
| !5 | `removerusuario` (AG-22) | 1 — RV-003-02 (P3): soft delete do vínculo (`excluido`) não aplicado em todos os caminhos | 1 | Aprovado — resolvido antes do merge |
| **Total** | | **5 achados (P2: 3 / P3: 2)** | **5/5 (100%)** | **Todos resolvidos antes do merge — nenhum defeito em aberto** |

---

### 3.6 Aceite Formal — Sprint 1

| Etapa | Responsável | Data | Resultado |
|---|---|---|---|
| Execução dos cenários de aceite (CTQ) | Leonardo Francisco Pereira (AASP — QA) | 06/06/2026 | Todos os 10 cenários aprovados |
| Aceite formal do cliente | Marcos Turnes (AASP — PO) | 06/06/2026 | Concedido sem ressalvas |

---

## 4. Sprint 2 — Em Andamento (09/06–20/06/2026)

### 4.1 Status Geral — Sprint 2

| Item | Valor |
|---|---|
| **Período** | 09/06/2026 a 20/06/2026 |
| **Status** | Em andamento — implementação ainda não iniciada no código na data de referência (15/06/2026) |
| **AG-23 — Auditoria de Grupos** | Em planejamento — ainda não implementado |
| **AG-24 — Integração ms.temis.vinculos** | Em planejamento — ainda não implementado |

### 4.2 Resultados de V&V — Sprint 2

Não há resultados de V&V registrados para a Sprint 2 até a data de referência (15/06/2026). Os testes de sistema e de homologação dos cenários AUD-01, AUD-02 (AG-23) e INT-01 (AG-24) serão executados após a implementação das funcionalidades. Testes automatizados não se aplicam a este projeto.

### 4.3 Pendências — Sprint 2

| Pendência | Responsável | Previsão |
|---|---|---|
| Implementar a trilha de auditoria das operações de escrita (AG-23) | Renan Kiyoshi | Sprint 2 |
| Implementar a integração com ms.temis.vinculos (AG-24) | Mateus Veloso | Sprint 2 |
| UAT — Leonardo Francisco Pereira executa cenários AUD-01, AUD-02 e INT-01 | Leonardo Francisco Pereira (AASP) | 19–20/06/2026 |
| Sprint Review e aceite formal Sprint 2 com Marcos Turnes | Abraão + Marcos Turnes | 20/06/2026 |

---

## 5. Sprint 3 — Status

| Sprint | Histórias Planejadas | Status |
|---|---|---|
| Sprint 3 (23/06–04/07/2026) | AG-25 — Relatório consolidado de grupos | Planejado — aguarda conclusão da Sprint 2 |

---

## 6. Métricas Consolidadas de V&V

| Métrica | Sprint 1 | Sprint 2 (15/06/2026) | Meta do Projeto |
|---|---|---|---|
| Testes unitários automatizados | **Não se aplica** | **Não se aplica** | N/A |
| Testes de integração automatizados | **Não se aplica** | **Não se aplica** | N/A |
| Cenários de aceite aprovados | 10/10 (100%) | — | 95% |
| Achados de code review — total identificados | 5 (P2: 3 / P3: 2) | — | — |
| Achados de code review — resolvidos antes do merge | 5/5 (100%) | — | 100% |
| Defeitos P1 em produção | 0 | 0 | 0 |
| Story Points entregues vs. planejados | 34/34 (0% desvio) | Em apuração | 0% desvio |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão | Versão inicial — resultados finais da Sprint 1 (AG-20, AG-21, AG-22); aceite formal 06/06/2026 |
| 1.1 | 15/06/2026 | Abraão | Inclusão do status parcial da Sprint 2 |
| 1.2 | 15/06/2026 | Abraão | Resultados alinhados à API real (endpoints/HTTP 200/400; função; tabelas reais); 3 sprints; Sprint 2 sem resultados de teste até a data |
| 1.3 | 23/06/2026 | Abraão | Testes unitários e de integração marcados como Não se aplica (projeto sem testes automatizados) |
