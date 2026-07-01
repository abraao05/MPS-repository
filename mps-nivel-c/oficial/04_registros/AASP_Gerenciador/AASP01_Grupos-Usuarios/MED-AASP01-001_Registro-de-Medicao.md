# Registro de Medição — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | MED-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.3 |
| **Data** | 01/07/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | MED — Medição (evidência de projeto) |

---

## 1. Objetivo

Registrar as medidas coletadas ao longo do projeto Grupos de Usuários, conforme PLA-MED-001 (Plano de Medição Organizacional Timeware), para apoiar a análise de aderência ao prazo, qualidade das entregas e capacidade de processo. Este documento é atualizado ao encerramento de cada sprint e serve como evidência objetiva do desempenho do projeto perante o processo MED do MPS-SW nível C.

---

## 2. Plano de Medição Aplicado

Este registro é vinculado ao catálogo organizacional **PLA-MED-001** da Timeware, que define o conjunto de indicadores padrão de projetos de desenvolvimento de software. As medidas são coletadas por sprint e consolidadas neste documento ao longo de todo o ciclo de vida do projeto.

| Atributo | Valor |
|---|---|
| **Plano de referência** | PLA-MED-001 — Plano de Medição Organizacional Timeware |
| **Frequência de coleta** | Por sprint (a cada 2 semanas) |
| **Responsável pela coleta** | Abraão Oliveira (Gerente de Projeto) |
| **Repositório dos dados** | GitLab — Boards + Repositório ms.auxo.usuarios |
| **Destinatários** | Abraão Oliveira (interno), Marcos Turnes (AASP, status semanal) |

---

## 3. Medidas de Prazo e Progresso

### 3.1 Marcos do Projeto — Planejado vs. Realizado

| Marco | Data Prevista | Data Realizada | Variação | Observação |
|---|---|---|---|---|
| Kickoff | 19/05/2026 | 19/05/2026 | 0 dias | Realizado conforme planejado; todos os participantes presentes |
| Início Sprint 1 | 26/05/2026 | 26/05/2026 | 0 dias | — |
| Aceite Sprint 1 | 06/06/2026 | 06/06/2026 | 0 dias | Aceite formal Marcos Turnes sem ressalvas |
| Início Sprint 2 | 09/06/2026 | 09/06/2026 | 0 dias | — |
| Aceite Sprint 2 | 20/06/2026 | 20/06/2026 | 0 dias | Aceite formal Marcos Turnes sem ressalvas — Sprint Review 14h00 Teams |
| Início Sprint 3 | 23/06/2026 | 23/06/2026 | 0 dias | Em andamento |
| Encerramento Sprint 3 (previsto) | 04/07/2026 | — | Planejado | — |

### 3.2 Story Points — Planejado vs. Realizado

| Sprint | SP Planejado | SP Realizado | Desvio | Velocity | Observação |
|---|---|---|---|---|---|
| Sprint 1 | 34 | 34 | 0 (0%) | 34 | 0% desvio — meta ≤ 10% atingida |
| Sprint 2 | 28 | 28 | 0 (0%) | 28 | 0% desvio — meta ≤ 10% atingida |
| Sprint 3 | 20 | Em andamento | — | — | Em desenvolvimento desde 23/06/2026 |
| **TOTAL S1+S2** | **62** | **62** | **0 (0%)** | — | Acumulado Sprints 1 e 2 |

---

## 4. Medidas de Qualidade de Produto

### 4.1 Testes Unitários e Cobertura

| Sprint | Métodos Testados | Cobertura de Linha | Cobertura de Branch | Meta | Status |
|---|---|---|---|---|---|
| Sprint 1 | 22 | 68.4% | 61.9% | ≥ 60% | ✅ Meta atingida |
| Sprint 2 | 14 novos (36 acumulados) | 70.1% (acumulado) | — | ≥ 60% | ✅ Meta atingida |
| Sprint 3 | A apurar | — | — | ≥ 60% | Planejado |

> Cobertura medida pelo Coverlet 3.1.2 na execução xUnit. Sprint 2 cobre AG-23 (trilha de auditoria) e AG-24 (cliente HTTP + retry com ms.temis.vinculos). Detalhes no REL-VV-AASP01-001.

### 4.2 Defeitos por Fase

| Sprint | Tipo | Encontrados | Severidade | Resolvidos Antes do Aceite | Origem |
|---|---|---|---|---|---|
| Sprint 1 | Achados code review (REV) | 5 | P2: 3 / P3: 2 | 5 de 5 (100%) | MRs !1, !2, !3, !4, !5 |
| Sprint 2 | Achados code review (REV) | 3 | P2: 2 / P3: 1 | 3 de 3 (100%) | MRs !6, !7 |
| **Total S1+S2** | — | **8** | P2: 5 / P3: 3 | 8 de 8 (100%) | — |
| Sprint 3 | A apurar | — | — | — | Planejado |

> Nenhum defeito P1 (crítico) aberto em produção ou homologação ao longo das Sprints 1 e 2. Todos os achados foram registrados e resolvidos antes do merge conforme processo REV (REV-AASP01-001).

### 4.3 Cenários de Teste de Aceite (Homologação)

| Sprint | Cenários Executados | Aprovados | % Aprovação | Meta | Status |
|---|---|---|---|---|---|
| Sprint 1 | 10 | 10 | 100% | ≥ 95% | ✅ Meta atingida |
| Sprint 2 | 4 (AUD-01, AUD-02, INT-01, INT-02) | 4 | 100% | ≥ 95% | ✅ Meta atingida |
| **Total S1+S2** | **14** | **14** | **100%** | — | — |
| Sprint 3 | A executar | — | — | ≥ 95% | Planejado |

---

## 5. Medidas de Performance e Confiabilidade

| Métrica | Valor Medido | Meta | Ambiente | Status |
|---|---|---|---|---|
| Tempo de resposta p95 — GET buscargrupoporid | ≤ 280 ms | ≤ 500 ms | Dev (Swagger UI) | ✅ Meta atingida |
| Tempo de resposta p95 — POST incluirgrupo | ≤ 310 ms | ≤ 500 ms | Dev (Swagger UI) | ✅ Meta atingida |
| Tempo de resposta p95 — GET listargrupo | ≤ 260 ms | ≤ 500 ms | Dev (Swagger UI) | ✅ Meta atingida |
| Disponibilidade ambiente dev | > 99% (Sprints 1 e 2) | ≥ 99% | Dev (local) | ✅ Meta atingida |

> Medições em ambiente de homologação AASP previstas para Sprint 3 (homologação final — Leonardo Francisco Pereira).

---

## 6. Indicadores Consolidados (M1-M8) — Sprints 1 e 2

| Código | Indicador | Resultado | Meta | Status | Referência |
|---|---|---|---|---|---|
| M1 | % de entregas no prazo | 100% (Sprint 1: aceite 06/06/2026; Sprint 2: aceite 20/06/2026) | ≥ 90% | ✅ Atingido | RAC-AASP01-001 |
| M2 | Desvio de esforço (SP) | 0% (62 SP planejados × 62 SP realizados nas Sprints 1+2) | ≤ 10% | ✅ Atingido | RAC-AASP01-001 |
| M3 | Índice de defeitos por SP | 0,129 def/SP (8 achados P2/P3 / 62 SP — S1: 5/34 SP; S2: 3/28 SP) | ≤ 0,20 | ✅ Atingido | REV-AASP01-001 |
| M4 | Cobertura testes unitários | 70.1% linha (acumulado Sprint 1+2; 36 métodos testados) | ≥ 60% | ✅ Atingido | REL-VV-AASP01-001 |
| M5 | Taxa de aprovação no aceite | 100% (14/14 cenários: 10 Sprint 1 + 4 Sprint 2) | ≥ 95% | ✅ Atingido | CTQ-AASP01-001 |
| M6 | Tempo médio de resposta API | ≤ 280 ms (Swagger dev, endpoint p95, validado nas Sprints 1 e 2) | ≤ 500 ms | ✅ Atingido | Evidência Swagger |
| M7 | % de requisitos rastreados | 100% (RF-01 a RF-08 rastreados; RF-09 em Sprint 3) | 100% | ✅ Atingido (parcial) | RASTR-AASP01-001 |
| M8 | Satisfação do cliente | Aceite formal sem ressalvas — Marcos Turnes (06/06/2026 e 20/06/2026) | Aceite formal | ✅ Atingido | ATA-AASP01-002 |

---

## 7. Próximo Ponto de Medição

**Encerramento Sprint 3 — previsto para 04/07/2026:**

- Atualizar M1 com status de prazo da Sprint 3
- Atualizar M2 com SP realizado vs. planejado (20 SP)
- Atualizar M3 com achados de code review MR AG-25
- Atualizar M4 com cobertura de testes unitários AG-25
- Atualizar M5 após UAT Sprint 3 e homologação final de regressão (Leonardo Francisco Pereira)
- Atualizar M6 com medições de performance em ambiente de homologação AASP
- Confirmar M7 com rastreabilidade RF-09 (AG-25)
- Atualizar M8 após aceite formal Sprint 3 e encerramento (Marcos Turnes)

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão Oliveira | Versão inicial — pós-encerramento Sprint 1; registros M1-M8 com dados reais Sprint 1 |
| 1.1 | 15/06/2026 | Abraão Oliveira | Atualização com status parcial Sprint 2 (~60% concluído em 15/06); seção 7 atualizada com próximo ponto de medição |
| 1.2 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
| 1.3 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: Sprint 2 atualizada com dados reais (28/28 SP, aceite 20/06/2026, 14 métodos testados, 3 achados code review, 4/4 UAT aprovados); M3 corrigido para 0,129 (8 achados/62 SP — Sprint 1: 5 achados; Sprint 2: 3 achados); todos os marcos S2 preenchidos; indicadores M1–M8 atualizados com dados acumulados. |
