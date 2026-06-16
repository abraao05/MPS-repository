# Registro de Medição — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | MED-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.1 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | MED — Medição (evidência de projeto) |

---

## 1. Objetivo

Registrar as medidas coletadas ao longo do projeto Grupos de Usuários, conforme PLA-MED-001 (Plano de Medição Organizacional Timeware), para apoiar a análise de aderência ao prazo, qualidade das entregas e capacidade de processo. Este documento e atualizado ao encerramento de cada sprint e serve como evidência objetiva do desempenho do projeto perante o processo MED do MPS-SW nível C.

---

## 2. Plano de Medição Aplicado

Este registro e vinculado ao catalogo organizacional **PLA-MED-001** da Timeware, que define o conjunto de indicadores padrão de projetos de desenvolvimento de software. As medidas são coletadas por sprint e consolidadas neste documento ao longo de todo o ciclo de vida do projeto.

| Atributo | Valor |
|---|---|
| **Plano de referência** | PLA-MED-001 — Plano de Medição Organizacional Timeware |
| **Frequência de coleta** | Por sprint (a cada 2 semanas) |
| **Responsável pela coleta** | Abraão Oliveira (Gerente de Projeto) |
| **Repositório dos dados** | Azure DevOps — Boards + Repositório ms.auxo.gruposusuarios |
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
| Encerramento Sprint 2 (previsto) | 20/06/2026 | — | Em andamento | Posição: ~60% concluido em 15/06/2026 |
| Início Sprint 3 | 23/06/2026 | — | Planejado | — |
| Encerramento Sprint 3 (previsto) | 04/07/2026 | — | Planejado | — |
| Início Sprint 4 | 07/07/2026 | — | Planejado | — |
| Encerramento final (previsto) | 11/07/2026 | — | Planejado | — |

### 3.2 Story Points — Planejado vs. Realizado

| Sprint | SP Planejado | SP Realizado | Desvio | Velocity | Observação |
|---|---|---|---|---|---|
| Sprint 1 | 34 | 34 | 0 (0%) | 34 | 0% desvio — meta <= 10% atingida |
| Sprint 2 | 28 | Em andamento | — | — | ~60% concluido em 15/06/2026 |
| Sprint 3 | 20 | Planejado | — | — | — |
| Sprint 4 | 8 | Planejado | — | — | — |
| **TOTAL** | **90** | **34 realizados + 56 planejados** | — | — | — |

---

## 4. Medidas de Qualidade de Produto

### 4.1 Testes Unitários e Cobertura

| Sprint | Métodos Testados | Total Métodos | Cobertura Est. | Meta | Status |
|---|---|---|---|---|---|
| Sprint 1 | 22 | ~26 | 85% | >= 80% | Meta atingida |
| Sprint 2 | — | — | — | >= 80% | Em andamento |
| Sprint 3 | — | — | — | >= 80% | Planejado |
| Sprint 4 | — | — | — | >= 80% | Planejado |

> Nota: Cobertura estimada com base no total de métodos públicos das camadas de serviço (GruposService, PermissoesService) e repositório (GruposRepository, PermissoesRepository) implementados na Sprint 1. Medição exata disponível no relatório de execução xUnit (REL-VV-AASP01-001).

### 4.2 Defeitos por Fase

| Sprint | Tipo | Encontrados | Severidade | Resolvidos Antes do Aceite | Origem |
|---|---|---|---|---|---|
| Sprint 1 | Achados code review (REV) | 5 | P2: 3 / P3: 2 | 5 de 5 (100%) | PRs #11, #12, #13, #14, #15 |
| Sprint 2 | — | — | — | — | Em andamento |
| Sprint 3 | — | — | — | — | Planejado |
| Sprint 4 | — | — | — | — | Planejado |

> Nenhum defeito aberto em produção ou homologação ao longo da Sprint 1. Todos os achados foram registrados e resolvidos antes do merge conforme processo REV (REV-AASP01-001).

### 4.3 Cenários de Teste de Aceite (Homologação)

| Sprint | Cenários Executados | Aprovados | % Aprovação | Meta | Status |
|---|---|---|---|---|---|
| Sprint 1 | 10 | 10 | 100% | >= 95% | Meta atingida |
| Sprint 2 | A executar | — | — | >= 95% | Planejado para 20/06/2026 |
| Sprint 3 | A executar | — | — | >= 95% | Planejado |
| Sprint 4 | A executar | — | — | >= 95% | Planejado |

---

## 5. Medidas de Performance e Confiabilidade

| Métrica | Valor Medido | Meta | Ambiente | Status |
|---|---|---|---|---|
| Tempo de resposta p95 — GET /grupos/{id} | <= 280 ms | <= 500 ms | Dev (Swagger UI) | Meta atingida |
| Tempo de resposta p95 — POST /grupos | <= 310 ms | <= 500 ms | Dev (Swagger UI) | Meta atingida |
| Tempo de resposta p95 — GET /grupos | <= 260 ms | <= 500 ms | Dev (Swagger UI) | Meta atingida |
| Disponibilidade ambiente dev | > 99% no período da Sprint 1 | >= 99% | Dev (local) | Meta atingida |

> Medições realizadas via Swagger UI em ambiente dev local durante a Sprint 1. Medições em ambiente de homologação AASP serao realizadas a partir da Sprint 2 (ambiente disponível a partir de 09/06/2026 — Leonardo Francisco Pereira).

---

## 6. Indicadores Consolidados (M1-M8)

| Código | Indicador | Resultado | Meta | Status | Referência |
|---|---|---|---|---|---|
| M1 | % de entregas no prazo | 100% (Sprint 1 aceita em 06/06/2026) | >= 90% | Atingido | RAC-AASP01-001 |
| M2 | Desvio de esforco (SP) | 0% Sprint 1 (34 planejado x 34 realizado) | <= 10% | Atingido | RAC-AASP01-001 |
| M3 | Índice de defeitos por SP | 0,088 def/SP (3 achados P2 / 34 SP) | <= 0,20 | Atingido | REV-AASP01-001 |
| M4 | Cobertura testes unitários | 85% estimado Sprint 1 | >= 80% | Atingido | REL-VV-AASP01-001 |
| M5 | Taxa de aprovação no aceite | 100% (10/10 cenários Sprint 1) | >= 95% | Atingido | CTQ-AASP01-001 |
| M6 | Tempo médio de resposta API | <= 280 ms (Swagger dev, endpoint p95) | <= 500 ms | Atingido | Evidência Swagger Sprint 1 |
| M7 | % de requisitos rastreados | 100% (AG-20 a AG-25 rastreados) | 100% | Atingido | RASTR-AASP01-001 |
| M8 | Satisfação do cliente | Aceite formal sem ressalvas (Marcos Turnes, 06/06/2026) | Aceite formal | Atingido | ATA-AASP01-002 |

---

## 7. Próximo Ponto de Medição

**Encerramento Sprint 2 — previsto para 20/06/2026:**

- Atualizar M1 com status de prazo da Sprint 2
- Atualizar M2 com SP realizado vs. planejado (28 SP)
- Atualizar M3 com achados de code review PRs #16 e #17
- Atualizar M4 com cobertura de testes unitários AG-23 e AG-24
- Atualizar M5 após UAT Sprint 2 (Leonardo Francisco Pereira)
- Atualizar M6 com medições de performance em ambiente homologação AASP
- Confirmar M7 com rastreabilidade AG-23 e AG-24
- Atualizar M8 após aceite formal Sprint 2 (Marcos Turnes)

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão Oliveira | Versão inicial — pós-encerramento Sprint 1; registros M1-M8 com dados reais Sprint 1 |
| 1.1 | 15/06/2026 | Abraão Oliveira | Atualização com status parcial Sprint 2 (~60% concluido em 15/06); seção 7 atualizada com próximo ponto de medição |
