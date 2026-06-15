# Relatório de Acompanhamento — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | RAC-AASP01-001 |
| **Projeto** | AG — Grupos de Usuários |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Produto** | ms.auxo.gruposusuarios |
| **Repositório** | Azure DevOps · komatsuhenry67/gerenciador-aasp/ms.auxo.gruposusuarios |
| **GP / Tech Lead** | Abraão (GP) · Cezar Hiraki (TL) — Timeware Brasil |
| **Desenvolvedores** | Renan Kiyoshi, Henry Komatsu, Mateus Veloso — Timeware Brasil |
| **PO** | Marcos Turnes — AASP |
| **QA** | Leonardo Francisco Pereira — AASP |
| **Data do relatório** | 15/06/2026 |
| **Versão** | 1.1 |
| **Status geral** | Em andamento — Sprint 2 |

---

## 1. Objetivo

Monitorar o progresso do projeto em relação ao plano estabelecido, identificar desvios de prazo, esforço e qualidade, e registrar ações corretivas adotadas. Este documento constitui evidência do processo GPR (Gerência de Projeto) do nível C do MPS.BR, atendendo ao atributo de monitoramento e controle do progresso do projeto.

---

## 2. Sprint 1 — Snapshot de Progresso (06/06/2026)

| Atributo | Valor |
|---|---|
| **Status geral** | ✅ Concluído com aceite formal |
| **Período** | 26/05/2026 – 06/06/2026 |
| **Data de aceite** | 06/06/2026 |
| **Responsável pelo aceite** | Marcos Turnes (PO — AASP) |
| **Ressalvas no aceite** | Nenhuma |

### 2.1 Itens Planejados vs. Entregues

| História | Requisitos Cobertos | SP Planejado | SP Realizado | Desvio | Status | Observação |
|---|---|---|---|---|---|---|
| AG-20 — CRUD Grupos | RF-01, RF-02, RF-03, RF-04 | 13 | 13 | 0% | ✅ Entregue | PRs #11 e #12 aprovados e mergeados; casos GRP-01 a GRP-05 aprovados |
| AG-21 — Permissões RBAC | RF-05 | 11 | 11 | 0% | ✅ Entregue | PR #13 aprovado; 8 testes unitários; casos PERM-01 e PERM-02 aprovados |
| AG-22 — Vínculo Usuário-Grupo | RF-06 | 10 | 10 | 0% | ✅ Entregue | PRs #14 e #15 aprovados; casos VINC-01, VINC-02, VINC-03 aprovados |
| **Total Sprint 1** | **RF-01 a RF-06** | **34** | **34** | **0%** | **✅ 100% entregue** | — |

### 2.2 Desvios Identificados

Nenhum desvio de prazo, escopo ou esforço identificado na Sprint 1. Todas as histórias foram entregues dentro do período planejado, com Story Points realizados iguais aos planejados.

### 2.3 Qualidade — Sprint 1

| Indicador | Resultado | Meta | Status |
|---|---|---|---|
| Testes unitários implementados | 22 métodos testados | — | ✅ |
| Cobertura estimada de código | 85% | ≥ 80% | ✅ Meta atingida |
| Achados de code review | 5 (P2: 3 achados · P3: 2 achados) | ≤ P2 (sem P1 críticos) | ✅ Sem criticidades |
| Resolução dos achados | Todos resolvidos antes do merge final | 100% antes do merge | ✅ |
| Cenários de aceite executados | 10 cenários | 10 planejados | ✅ |
| Cenários de aceite aprovados | 10 de 10 (100%) | ≥ 95% | ✅ Meta superada |
| Aceite formal do PO | Marcos Turnes — 06/06/2026 — sem ressalvas | Aceite formal obrigatório | ✅ |

---

## 3. Sprint 2 — Snapshot de Progresso (15/06/2026 — Em Andamento)

| Atributo | Valor |
|---|---|
| **Status geral** | ⏳ Em andamento |
| **Período** | 09/06/2026 – 20/06/2026 |
| **Data do snapshot** | 15/06/2026 (meio de sprint) |

### 3.1 Status Atual das Histórias

| História | Requisito | Progresso | Detalhamento | Próximos Passos |
|---|---|---|---|---|
| AG-23 — Auditoria de Ações | RF-07 | ~70% | Tabela AuditoriaGrupos criada e populada nas operações de CRUD; triggers de auditoria implementados e em revisão de code review | Concluir revisão dos triggers; abrir PR; executar caso AUD-01 |
| AG-24 — Integração ms.temis.vinculos | RF-08 | ~40% | Contrato de API definido e documentado; cliente HTTP implementado com timeout de 5 s e retry de 1 tentativa; testes de integração em construção | Finalizar testes INT-01; validar cenários de falha e retry; abrir PR |

### 3.2 Riscos Ativos — Sprint 2

| Código | Descrição | Probabilidade | Impacto | Mitigação | Status |
|---|---|---|---|---|---|
| R-04 | Falha ou instabilidade na integração com ms.temis.vinculos | Média | Alto | Contrato de API definido; retry implementado; cliente HTTP com timeout configurado | Em monitoramento |
| R-01 | Atraso na disponibilização do ambiente de homologação AASP | Baixa | Médio | Aguardando confirmação de janela de testes por Leonardo Francisco Pereira (AASP) | Em monitoramento |

### 3.3 Projeção de Encerramento — Sprint 2

Com AG-23 em ~70% e AG-24 em ~40% na metade da sprint, a projeção é de conclusão dentro do prazo (20/06/2026), desde que os PRs sejam abertos e aprovados até 18/06/2026. Nenhuma ação corretiva foi necessária até o momento.

---

## 4. Sprints 3 e 4 — Status Planejado

| Sprint | Período | Histórias / Entregas | SP | Status | Observação |
|---|---|---|---|---|---|
| S3 | 23/06–04/07/2026 | AG-25 — Relatórios consolidados (RF-09 · GET /grupos/relatorio) | 20 | 📅 Planejado | Sem ajustes de escopo até o momento; depende de AG-23 e AG-24 concluídos |
| S4 | 07/07–11/07/2026 | Encerramento: TAE (Testes de Aceite Final), LI (Lições Aprendidas), GQA (revisão de qualidade), homologação final em ambiente AASP | 8 | 📅 Planejado | Depende do aceite formal de S3 por Marcos Turnes; homologação conduzida por Leonardo Francisco Pereira |

---

## 5. Métricas Consolidadas (até 15/06/2026)

| Código | Métrica | Valor Atual | Meta | Status |
|---|---|---|---|---|
| M1 | Entregas no prazo | 100% (Sprint 1 com aceite em 06/06/2026) | ≥ 90% | ✅ Meta atingida |
| M2 | Desvio de Story Points acumulado | 0% (34 SP plan × 34 SP real na S1) | ≤ 10% | ✅ Meta atingida |
| M3 | Defeitos por Story Point | 0,088 (3 achados P2/P3 em 34 SP — todos resolvidos antes do merge) | ≤ 0,20 | ✅ Meta atingida |
| M4 | Cobertura de testes unitários | 85% (estimada — S1) | ≥ 80% | ✅ Meta atingida |
| M5 | Taxa de aceite dos cenários | 100% (10 de 10 aprovados em S1) | ≥ 95% | ✅ Meta superada |
| M6 | Tempo de resposta dos endpoints | ≤ 280 ms (validado via Swagger em S1) | ≤ 500 ms | ✅ Meta superada |
| M7 | Rastreabilidade req → teste | 100% (para todos os RFs entregues em S1) | 100% | ✅ Meta atingida |
| M8 | Satisfação do cliente | Aceite formal sem ressalvas — Marcos Turnes (06/06/2026) | Aceite formal | ✅ Meta atingida |

---

## 6. Próximo Relatório

O próximo relatório de acompanhamento está previsto para **20/06/2026**, ao encerramento da Sprint 2, e incluirá os resultados de AG-23 e AG-24, os casos de teste AUD-01 e INT-01, e a atualização das métricas M3, M4 e M5.

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão | Versão inicial — snapshot pós-Sprint 1 com resultados de entrega, qualidade e aceite formal |
| 1.1 | 15/06/2026 | Abraão | Atualização com status parcial de Sprint 2 (AG-23 ~70%, AG-24 ~40%), riscos ativos e métricas consolidadas |
