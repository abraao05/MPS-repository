# Relatório de Execução de Testes (V&V) — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | REL-VV-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.1 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | VV (evidência de projeto) |

---

## 1. Objetivo

Registrar os resultados da execução das atividades de Verificação e Validação (V&V) por sprint, incluindo testes unitários, testes de integração e testes de homologação (UAT), conforme planejado no VV-AASP01-001. Este documento é a evidência formal de execução do processo VV do MPS.BR Nível C para o projeto Grupos de Usuários — AASP Gerenciador.

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
| **PRs mergeados** | #11, #12, #13, #14, #15 — todos aprovados e mergeados para main |

---

### 3.2 Testes Unitários — Sprint 1

| Suite / Classe | Métodos Testados | Passando | Falhando | Cobertura Estimada |
|---|---|---|---|---|
| GrupoServiceTests | 8 | 8 | 0 | 90% (camada service) |
| GrupoRepositoryTests | 6 | 6 | 0 | 85% (repositório Dapper) |
| PermissaoServiceTests | 4 | 4 | 0 | 88% |
| VinculoServiceTests | 4 | 4 | 0 | 82% |
| **TOTAL** | **22** | **22** | **0** | **85% est. média** |

**Meta de cobertura: 80% — ATINGIDA**

---

### 3.3 Testes de Integração — Sprint 1

| Teste | Descrição | Resultado |
|---|---|---|
| IntegrationTest_CriarEBuscarGrupo | Criar grupo via POST /grupos e buscar via GET /grupos/{id} — valida round-trip completo no banco auxo3 | OK |
| IntegrationTest_AssociarPermissoes | Criar grupo e associar permissões via PUT /grupos/{id}/permissoes — valida persistência na tabela PermissoesGrupo | OK |
| IntegrationTest_VincularEDesvincularUsuario | Vincular usuário via POST e desvincular via DELETE — valida soft delete (campo Ativo=false) na tabela UsuariosGrupo | OK |
| **Total** | **3 testes de integração** | **3/3 (100%) — Meta atingida** |

---

### 3.4 Testes de Homologação — Sprint 1 (UAT)

**Executados por:** Leonardo Francisco Pereira (AASP — QA/Homologadora)
**Data de execução:** 06/06/2026
**Ambiente:** Homologação AASP — banco auxo3

| ID | História | Cenário de Aceite | Resultado |
|---|---|---|---|
| GRP-01 | AG-20 | Criar grupo com dados válidos — happy path; nome único aceito pelo sistema | OK |
| GRP-02 | AG-20 | Listar todos os grupos ativos com paginação — retorno correto dos campos | OK |
| GRP-03 | AG-20 | Atualizar nome e descrição de grupo existente via PUT — persistência validada | OK |
| GRP-04 | AG-20 | Soft delete de grupo — campo Ativo=false; grupo não aparece em listagem ativa | OK |
| GRP-05 | AG-20 | Tentar criar grupo com nome duplicado — sad path; erro 409 retornado corretamente | OK |
| PERM-01 | AG-21 | Associar permissões válidas (Leitura, Escrita, Administracao) a um grupo — persistência validada | OK |
| PERM-02 | AG-21 | Tentar associar permissão inválida (fora do enum) — sad path; erro 400 retornado corretamente | OK |
| VINC-01 | AG-22 | Vincular usuário ativo a um grupo — associação registrada em UsuariosGrupo | OK |
| VINC-02 | AG-22 | Desvincular usuário de um grupo via DELETE — soft delete do vínculo validado | OK |
| VINC-03 | AG-22 | Tentar vincular usuário inexistente — sad path; erro 404 retornado corretamente | OK |
| **Total** | | **10 cenários de aceite** | **10/10 (100%) — Meta de 95% ATINGIDA** |

---

### 3.5 Code Review — Sprint 1

| PR | Feature / História | Achados Identificados | Achados Resolvidos | Resultado |
|---|---|---|---|---|
| #11 | POST /grupos (AG-20) | 1 — RV-001-01 (P2): falta de validação de comprimento máximo do campo Nome | 1 | Aprovado — resolvido antes do merge |
| #12 | GET / PUT / DELETE /grupos (AG-20) | 1 — RV-001-02 (P3): retorno de campos desnecessários no DTO de listagem | 1 | Aprovado — resolvido antes do merge |
| #13 | Permissões RBAC (AG-21) | 1 — RV-002-01 (P2): ausência de tratamento de exceção para enum inválido | 1 | Aprovado — resolvido antes do merge |
| #14 | POST vínculo usuário-grupo (AG-22) | 1 — RV-003-01 (P2): falta de verificação de vínculo duplicado antes do INSERT | 1 | Aprovado — resolvido antes do merge |
| #15 | DELETE vínculo usuário-grupo (AG-22) | 1 — RV-003-02 (P3): log de auditoria não registrava o usuário executor da ação | 1 | Aprovado — resolvido antes do merge |
| **Total** | | **5 achados (P2: 3 / P3: 2)** | **5/5 (100%)** | **Todos resolvidos antes do merge — nenhum defeito em aberto** |

---

### 3.6 Aceite Formal — Sprint 1

| Etapa | Responsável | Data | Resultado |
|---|---|---|---|
| Execução dos cenários de aceite (CTQ) | Leonardo Francisco Pereira (AASP — QA) | 06/06/2026 | Todos os 10 cenários aprovados |
| Aceite formal do cliente | Marcos Turnes (AASP — PO) | 06/06/2026 | Concedido sem ressalvas |

---

## 4. Sprint 2 — Resultados Parciais (09/06–15/06/2026 — Em Andamento)

### 4.1 Status Geral — Sprint 2

| Item | Valor |
|---|---|
| **Período** | 09/06/2026 a 20/06/2026 |
| **Status** | Em andamento — progresso estimado em 60% na data de referência (15/06/2026) |
| **AG-23 — Auditoria de Grupos** | Em andamento — aproximadamente 70% concluído |
| **AG-24 — Integração ms.temis.vinculos** | Em andamento — aproximadamente 40% concluído |

---

### 4.2 Testes Unitários — Sprint 2 (Parcial)

**AG-23 (AuditoriaGrupos):**
- 4 testes unitários criados e passando para operações de CREATE e UPDATE de grupos (registro automático em tabela de auditoria)
- Testes para triggers de DELETE ainda em desenvolvimento (implementação de DELETE em AG-23 não concluída em 15/06/2026)

**AG-24 (Integração ms.temis.vinculos):**
- Cliente HTTP implementado com injeção de dependência e configuração por environment
- 2 testes unitários com mock de HttpClient passando (cenário de sucesso e cenário de timeout)
- Testes de integração real pendentes — aguardam disponibilização do ambiente compartilhado de ms.temis.vinculos pela equipe de infraestrutura

---

### 4.3 Testes de Homologação — Sprint 2

**Status: Aguardando conclusão da implementação — previsto para 19 e 20/06/2026**

Os cenários de aceite da Sprint 2 (AUD-01, AUD-02 para AG-23; INT-01 para AG-24) serão executados por Leonardo Francisco Pereira (AASP) após conclusão da implementação e disponibilização do ambiente de homologação atualizado.

---

### 4.4 Pendências — Sprint 2

| Pendência | Responsável | Previsão |
|---|---|---|
| Completar implementação dos triggers de auditoria para operação DELETE (AG-23) | Renan Kioshi | 17/06/2026 |
| Testes de integração com ms.temis.vinculos em ambiente dev compartilhado (AG-24) | Renan Kioshi | 18/06/2026 |
| UAT — Leonardo Francisco Pereira executa cenários AUD-01, AUD-02 e INT-01 | Leonardo Francisco Pereira (AASP) | 19–20/06/2026 |
| Sprint Review e aceite formal Sprint 2 com Marcos Turnes | Abraão Oliveira + Marcos Turnes | 20/06/2026 — 14h00 Teams |

---

## 5. Sprint 3 e Sprint 4 — Status

| Sprint | Histórias Planejadas | Status |
|---|---|---|
| Sprint 3 (23/06–04/07/2026) | AG-25 — Relatórios (GET /grupos/relatorio) | Planejado — aguarda conclusão da Sprint 2 |
| Sprint 4 (07/07–11/07/2026) | Encerramento do projeto: TAE (Termo de Encerramento e Aceite), LI (Lições Aprendidas), GQA (Registro de Verificação de GQA), Homologação final com AASP | Planejado — aguarda conclusão da Sprint 3 |

---

## 6. Métricas Consolidadas de V&V

| Métrica | Sprint 1 | Sprint 2 (Parcial — 15/06/2026) | Meta do Projeto |
|---|---|---|---|
| Testes unitários — total passando | 22/22 (100%) | 6/6 (100% — parcial) | 100% |
| Cobertura estimada de testes unitários | 85% | Em apuração (parcial) | 80% |
| Cenários de aceite aprovados | 10/10 (100%) | — (pendente execução) | 95% |
| Testes de integração passando | 3/3 (100%) | Parcial (aguarda ambiente) | 100% |
| Achados de code review — total identificados | 5 (P2: 3 / P3: 2) | Em apuração | — |
| Achados de code review — resolvidos antes do merge | 5/5 (100%) | — | 100% |
| Defeitos P1 em produção | 0 | 0 | 0 |
| Story Points entregues vs. planejados | 34/34 (0% desvio) | Em apuração | 0% desvio |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão Oliveira | Versão inicial — resultados finais da Sprint 1 (AG-20, AG-21, AG-22); aceite formal 06/06/2026 |
| 1.1 | 15/06/2026 | Abraão Oliveira | Inclusão dos resultados parciais da Sprint 2 (AG-23 ~70%, AG-24 ~40%); seções 4 e 6 atualizadas |
