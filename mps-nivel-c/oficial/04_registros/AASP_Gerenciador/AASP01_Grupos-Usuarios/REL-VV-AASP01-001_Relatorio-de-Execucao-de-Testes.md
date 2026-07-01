# Relatório de Execução de Testes (V&V) — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | REL-VV-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.4 |
| **Data** | 01/07/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | VV (evidência de projeto) |

---

## 1. Objetivo

Registrar os resultados da execução das atividades de Verificação e Validação (V&V) por sprint, incluindo testes unitários, testes de integração e testes de homologação (UAT), conforme planejado no VV-AASP01-001. Este documento é a evidência formal de execução do processo VV do MPS.BR Nível C para o projeto Grupos de Usuários — AASP Gerenciador. Os endpoints referem-se ao controller real `GerenciarGruposController` (rota base `api/gerenciar/grupos`, HTTP 200/400).

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
| **Status** | ✅ Concluído — aceite formal em 06/06/2026 |
| **Total Story Points entregue** | 34 SP (100% do planejado — 0% de desvio) |
| **Histórias entregues** | AG-20 (Concluído) / AG-21 (Concluído) / AG-22 (Concluído) |
| **MRs mergeados** | !1–!5 — entregas da Sprint 1 aprovadas (alvo `develop`); baseline em `main` pela tag `sprint-1-aceite` |

---

### 3.2 Testes Unitários — Sprint 1

| Suite / Classe | Métodos Testados | Passando | Falhando | Cobertura (Coverlet) |
|---|---|---|---|---|
| GerenciarGruposServicesTests | 8 | 8 | 0 | — |
| GerenciarGruposRepositorioTests | 6 | 6 | 0 | — |
| IncluirAlterarGrupoTests | 4 | 4 | 0 | — |
| RemoverUsuarioFuncaoTests | 4 | 4 | 0 | — |
| **TOTAL** | **22** | **22** | **0** | **68.4% linhas / 61.9% branches** |

**Meta de cobertura: ≥ 60% — ATINGIDA (68.4% de linhas / 61.9% de branches)**

---

### 3.3 Testes de Integração — Sprint 1

| Teste | Descrição | Resultado |
|---|---|---|
| IntegrationTest_IncluirEListarGrupo | Criar grupo via `incluirgrupo` e consultar via `listargrupo` — valida round-trip completo no banco auxo3 | OK |
| IntegrationTest_AlterarFuncaoUsuario | Alterar a função de um usuário via `alterarfuncaodousuario` — valida persistência em `grupos_usuarios_funcao` | OK |
| IntegrationTest_VincularERemoverUsuario | Vincular usuário (lista de membros) e remover via `removerusuario` — valida soft delete (`excluido=1`) em `grupos_usuarios_vinculos` | OK |
| **Total** | **3 testes de integração** | **3/3 (100%) — Meta atingida** |

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

## 4. Sprint 2 — Resultados Finais (09/06–20/06/2026)

### 4.1 Status Geral — Sprint 2

| Item | Valor |
|---|---|
| **Período** | 09/06/2026 a 20/06/2026 |
| **Status** | ✅ Concluído — aceite formal em 20/06/2026 |
| **Total Story Points entregue** | 28 SP (100% do planejado — 0% de desvio) |
| **Histórias entregues** | AG-23 (Auditoria de Grupos) / AG-24 (Integração ms.temis.vinculos) |
| **MRs mergeados** | !6 (AG-23) e !7 (AG-24) — integrados em `develop`; baseline em `main` pela tag `sprint-2-aceite` |

---

### 4.2 Testes Unitários — Sprint 2

| Suite / Classe | Métodos Testados | Passando | Falhando | Observação |
|---|---|---|---|---|
| AuditoriaGruposServicesTests | 6 | 6 | 0 | AG-23 — trilha de auditoria das operações de escrita |
| AuditoriaGruposRepositorioTests | 4 | 4 | 0 | AG-23 — persistência na tabela `auditoria_grupos` |
| TemisVinculosIntegracaoTests | 4 | 4 | 0 | AG-24 — cliente HTTP com retry e timeout |
| **TOTAL Sprint 2** | **14** | **14** | **0** | — |
| **TOTAL Acumulado (S1+S2)** | **36** | **36** | **0** | **Cobertura acumulada: 70.1% linhas** |

**Meta de cobertura: ≥ 60% — ATINGIDA (70.1% de linhas acumulado Sprint 1+2)**

---

### 4.3 Testes de Homologação — Sprint 2 (UAT)

**Executados por:** Leonardo Francisco Pereira (AASP — QA/Homologadora)
**Data de execução:** 20/06/2026
**Ambiente:** Homologação AASP — banco auxo3

| ID | História | Cenário de Aceite | Resultado |
|---|---|---|---|
| AUD-01 | AG-23 | Realizar operação de criação/alteração de grupo — verificar registro de trilha de auditoria em `auditoria_grupos` com usuario, data e operação | OK |
| AUD-02 | AG-23 | Consultar histórico de auditoria de um grupo via endpoint de auditoria — retorno paginado com eventos ordenados por data desc | OK |
| INT-01 | AG-24 | Consultar vínculos de um usuário via integração com ms.temis.vinculos — retorno com lista de vínculos ativos | OK |
| INT-02 | AG-24 | Simular indisponibilidade do ms.temis.vinculos — verificar comportamento de fallback (timeout + retry + resposta HTTP 503 com mensagem adequada) | OK |
| **Total** | | **4 cenários de aceite** | **4/4 (100%) — Meta de 95% ATINGIDA** |

---

### 4.4 Code Review — Sprint 2

| MR | Feature / História | Achados Identificados | Achados Resolvidos | Resultado |
|---|---|---|---|---|
| !6 | Auditoria de Grupos (AG-23) | 2 — RV-006-01 (P2): interceptor de auditoria sem tratamento de exceção assíncrona; RV-006-02 (P2): campo `usuario_acao` não indexado na tabela auditoria_grupos | 2 | Aprovado — ambos resolvidos antes do merge |
| !7 | Integração ms.temis.vinculos (AG-24) | 1 — RV-007-01 (P3): timeout configurado acima do padrão organizacional (10 s em vez de 5 s) | 1 | Aprovado — resolvido antes do merge |
| **Total** | | **3 achados (P2: 2 / P3: 1)** | **3/3 (100%)** | **Todos resolvidos antes do merge — nenhum defeito em aberto** |

---

### 4.5 Aceite Formal — Sprint 2

| Etapa | Responsável | Data | Resultado |
|---|---|---|---|
| Execução dos cenários de aceite (CTQ) | Leonardo Francisco Pereira (AASP — QA) | 20/06/2026 | Todos os 4 cenários aprovados |
| Aceite formal do cliente | Marcos Turnes (AASP — PO) | 20/06/2026 | Concedido sem ressalvas — Sprint Review via Microsoft Teams, 14h00 |

---

## 5. Sprint 3 — Status Atual (01/07/2026)

| Sprint | Histórias Planejadas | SP | Status |
|---|---|---|---|
| Sprint 3 (23/06–04/07/2026) | AG-25 — Relatório consolidado de grupos e exportação CSV (RF-09) | 20 | 🔄 Em andamento desde 23/06/2026 |

> Testes unitários, code review e UAT da Sprint 3 serão registrados após a conclusão e aceite em ~04/07/2026.

---

## 6. Métricas Consolidadas de V&V

| Métrica | Sprint 1 | Sprint 2 | Total S1+S2 | Meta do Projeto |
|---|---|---|---|---|
| Testes unitários — total passando | 22/22 (100%) | 14/14 (100%) | 36/36 (100%) | 100% |
| Cobertura de testes unitários (Coverlet) | 68.4% linha / 61.9% branch | 70.1% linha (acumulado) | 70.1% linha | ≥ 60% |
| Cenários de aceite aprovados | 10/10 (100%) | 4/4 (100%) | 14/14 (100%) | ≥ 95% |
| Testes de integração passando | 3/3 (100%) | — | 3/3 (100%) | 100% |
| Achados de code review — total identificados | 5 (P2: 3 / P3: 2) | 3 (P2: 2 / P3: 1) | 8 (P2: 5 / P3: 3) | — |
| Achados de code review — resolvidos antes do merge | 5/5 (100%) | 3/3 (100%) | 8/8 (100%) | 100% |
| Defeitos P1 em produção | 0 | 0 | 0 | 0 |
| Story Points entregues vs. planejados | 34/34 (0% desvio) | 28/28 (0% desvio) | 62/62 (0% desvio) | ≤ 10% desvio |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão Oliveira | Versão inicial — resultados finais da Sprint 1 (AG-20, AG-21, AG-22); aceite formal 06/06/2026 |
| 1.1 | 15/06/2026 | Abraão Oliveira | Inclusão do status parcial da Sprint 2 |
| 1.2 | 15/06/2026 | Abraão Oliveira | Resultados alinhados à API real (endpoints/HTTP 200/400; função; tabelas reais); 3 sprints; Sprint 2 sem resultados de teste até a data |
| 1.3 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
| 1.4 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: Sprint 2 atualizada com resultados reais (testes unitários AG-23/AG-24, 4 UAT aprovados, 3 achados code review resolvidos, aceite Marcos Turnes 20/06/2026); métricas consolidadas atualizadas com dados acumulados S1+S2; Sprint 3 em andamento desde 23/06/2026. |
