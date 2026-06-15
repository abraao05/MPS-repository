# Registro de Medicao — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | MED-AASP01-001 |
| **Projeto** | Grupos de Usuarios — AASP Gerenciador |
| **Cliente** | AASP — Associacao dos Advogados de Sao Paulo |
| **Versao** | 1.1 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | MED — Medicao (evidencia de projeto) |

---

## 1. Objetivo

Registrar as medidas coletadas ao longo do projeto Grupos de Usuarios, conforme PLA-MED-001 (Plano de Medicao Organizacional Timeware), para apoiar a analise de aderencia ao prazo, qualidade das entregas e capacidade de processo. Este documento e atualizado ao encerramento de cada sprint e serve como evidencia objetiva do desempenho do projeto perante o processo MED do MPS-SW nivel C.

---

## 2. Plano de Medicao Aplicado

Este registro e vinculado ao catalogo organizacional **PLA-MED-001** da Timeware, que define o conjunto de indicadores padrao de projetos de desenvolvimento de software. As medidas sao coletadas por sprint e consolidadas neste documento ao longo de todo o ciclo de vida do projeto.

| Atributo | Valor |
|---|---|
| **Plano de referencia** | PLA-MED-001 — Plano de Medicao Organizacional Timeware |
| **Frequencia de coleta** | Por sprint (a cada 2 semanas) |
| **Responsavel pela coleta** | Abraão Oliveira (Gerente de Projeto) |
| **Repositorio dos dados** | Azure DevOps — Boards + Repositorio ms.auxo.gruposusuarios |
| **Destinatarios** | Abraão Oliveira (interno), Marcos Turnes (AASP, status semanal) |

---

## 3. Medidas de Prazo e Progresso

### 3.1 Marcos do Projeto — Planejado vs. Realizado

| Marco | Data Prevista | Data Realizada | Variacao | Observacao |
|---|---|---|---|---|
| Kickoff | 19/05/2026 | 19/05/2026 | 0 dias | Realizado conforme planejado; todos os participantes presentes |
| Inicio Sprint 1 | 26/05/2026 | 26/05/2026 | 0 dias | — |
| Aceite Sprint 1 | 06/06/2026 | 06/06/2026 | 0 dias | Aceite formal Marcos Turnes sem ressalvas |
| Inicio Sprint 2 | 09/06/2026 | 09/06/2026 | 0 dias | — |
| Encerramento Sprint 2 (previsto) | 20/06/2026 | — | Em andamento | Posicao: ~60% concluido em 15/06/2026 |
| Inicio Sprint 3 | 23/06/2026 | — | Planejado | — |
| Encerramento Sprint 3 (previsto) | 04/07/2026 | — | Planejado | — |
| Inicio Sprint 4 | 07/07/2026 | — | Planejado | — |
| Encerramento final (previsto) | 11/07/2026 | — | Planejado | — |

### 3.2 Story Points — Planejado vs. Realizado

| Sprint | SP Planejado | SP Realizado | Desvio | Velocity | Observacao |
|---|---|---|---|---|---|
| Sprint 1 | 34 | 34 | 0 (0%) | 34 | 0% desvio — meta <= 10% atingida |
| Sprint 2 | 28 | Em andamento | — | — | ~60% concluido em 15/06/2026 |
| Sprint 3 | 20 | Planejado | — | — | — |
| Sprint 4 | 8 | Planejado | — | — | — |
| **TOTAL** | **90** | **34 realizados + 56 planejados** | — | — | — |

---

## 4. Medidas de Qualidade de Produto

### 4.1 Testes Unitarios e Cobertura

| Sprint | Metodos Testados | Total Metodos | Cobertura Est. | Meta | Status |
|---|---|---|---|---|---|
| Sprint 1 | 22 | ~26 | 85% | >= 80% | Meta atingida |
| Sprint 2 | — | — | — | >= 80% | Em andamento |
| Sprint 3 | — | — | — | >= 80% | Planejado |
| Sprint 4 | — | — | — | >= 80% | Planejado |

> Nota: Cobertura estimada com base no total de metodos publicos das camadas de servico (GruposService, PermissoesService) e repositorio (GruposRepository, PermissoesRepository) implementados na Sprint 1. Medicao exata disponivel no relatorio de execucao xUnit (REL-VV-AASP01-001).

### 4.2 Defeitos por Fase

| Sprint | Tipo | Encontrados | Severidade | Resolvidos Antes do Aceite | Origem |
|---|---|---|---|---|---|
| Sprint 1 | Achados code review (REV) | 5 | P2: 3 / P3: 2 | 5 de 5 (100%) | PRs #11, #12, #13, #14, #15 |
| Sprint 2 | — | — | — | — | Em andamento |
| Sprint 3 | — | — | — | — | Planejado |
| Sprint 4 | — | — | — | — | Planejado |

> Nenhum defeito aberto em producao ou homologacao ao longo da Sprint 1. Todos os achados foram registrados e resolvidos antes do merge conforme processo REV (REV-AASP01-001).

### 4.3 Cenarios de Teste de Aceite (Homologacao)

| Sprint | Cenarios Executados | Aprovados | % Aprovacao | Meta | Status |
|---|---|---|---|---|---|
| Sprint 1 | 10 | 10 | 100% | >= 95% | Meta atingida |
| Sprint 2 | A executar | — | — | >= 95% | Planejado para 20/06/2026 |
| Sprint 3 | A executar | — | — | >= 95% | Planejado |
| Sprint 4 | A executar | — | — | >= 95% | Planejado |

---

## 5. Medidas de Performance e Confiabilidade

| Metrica | Valor Medido | Meta | Ambiente | Status |
|---|---|---|---|---|
| Tempo de resposta p95 — GET /grupos/{id} | <= 280 ms | <= 500 ms | Dev (Swagger UI) | Meta atingida |
| Tempo de resposta p95 — POST /grupos | <= 310 ms | <= 500 ms | Dev (Swagger UI) | Meta atingida |
| Tempo de resposta p95 — GET /grupos | <= 260 ms | <= 500 ms | Dev (Swagger UI) | Meta atingida |
| Disponibilidade ambiente dev | > 99% no periodo da Sprint 1 | >= 99% | Dev (local) | Meta atingida |

> Medicoes realizadas via Swagger UI em ambiente dev local durante a Sprint 1. Medicoes em ambiente de homologacao AASP serao realizadas a partir da Sprint 2 (ambiente disponivel a partir de 09/06/2026 — Leonardo Francisco Pereira).

---

## 6. Indicadores Consolidados (M1-M8)

| Codigo | Indicador | Resultado | Meta | Status | Referencia |
|---|---|---|---|---|---|
| M1 | % de entregas no prazo | 100% (Sprint 1 aceita em 06/06/2026) | >= 90% | Atingido | RAC-AASP01-001 |
| M2 | Desvio de esforco (SP) | 0% Sprint 1 (34 planejado x 34 realizado) | <= 10% | Atingido | RAC-AASP01-001 |
| M3 | Indice de defeitos por SP | 0,088 def/SP (3 achados P2 / 34 SP) | <= 0,20 | Atingido | REV-AASP01-001 |
| M4 | Cobertura testes unitarios | 85% estimado Sprint 1 | >= 80% | Atingido | REL-VV-AASP01-001 |
| M5 | Taxa de aprovacao no aceite | 100% (10/10 cenarios Sprint 1) | >= 95% | Atingido | CTQ-AASP01-001 |
| M6 | Tempo medio de resposta API | <= 280 ms (Swagger dev, endpoint p95) | <= 500 ms | Atingido | Evidencia Swagger Sprint 1 |
| M7 | % de requisitos rastreados | 100% (AG-20 a AG-25 rastreados) | 100% | Atingido | RASTR-AASP01-001 |
| M8 | Satisfacao do cliente | Aceite formal sem ressalvas (Marcos Turnes, 06/06/2026) | Aceite formal | Atingido | ATA-AASP01-002 |

---

## 7. Proximo Ponto de Medicao

**Encerramento Sprint 2 — previsto para 20/06/2026:**

- Atualizar M1 com status de prazo da Sprint 2
- Atualizar M2 com SP realizado vs. planejado (28 SP)
- Atualizar M3 com achados de code review PRs #16 e #17
- Atualizar M4 com cobertura de testes unitarios AG-23 e AG-24
- Atualizar M5 apos UAT Sprint 2 (Leonardo Francisco Pereira)
- Atualizar M6 com medicoes de performance em ambiente homologacao AASP
- Confirmar M7 com rastreabilidade AG-23 e AG-24
- Atualizar M8 apos aceite formal Sprint 2 (Marcos Turnes)

---

## Historico de Revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão Oliveira | Versao inicial — pos-encerramento Sprint 1; registros M1-M8 com dados reais Sprint 1 |
| 1.1 | 15/06/2026 | Abraão Oliveira | Atualizacao com status parcial Sprint 2 (~60% concluido em 15/06); secao 7 atualizada com proximo ponto de medicao |
