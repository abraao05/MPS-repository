# Registro de Change Request — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | CR-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.1 |
| **Data** | 15/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Tech Lead / Arquiteto / DevOps** | Cézar Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Contexto

O projeto MilhasFacil é executado em sprints de 2 semanas, com mudanças de escopo formalizadas via change request antes da implementação. Até a Sprint 9, foi registrado **1 change request** (CR-MF-001), tratando a antecipação dos filtros avançados de busca da Sprint 10 para a Sprint 9. O CR vincula-se ao risco R-04 (mudança de escopo).

---

## 2. Registro do Change Request

| CR | Descrição da mudança | Escopo afetado | Sprint origem → destino | Data | Solicitante | Impacto | Aprovado por | Status |
|---|---|---|---|---|---|---|---|---|
| CR-MF-001 | Antecipação dos filtros avançados de busca (`maxMiles` / `cabinType`) da Sprint 10 para a Sprint 9 | RF13 — filtros avançados de busca | S10 → S9 | 28/05/2026 | PO Hub de Milhas | +10 h; 0 dia de atraso macro | Abraão (GP) | ✅ Aprovado |

---

## 3. Detalhamento do CR-MF-001

| Item | Valor |
|---|---|
| **Identificador** | CR-MF-001 |
| **Data da solicitação** | 28/05/2026 |
| **Solicitante** | PO Hub de Milhas |
| **Mudança** | Antecipar a implementação dos filtros avançados de busca (RF13 — `maxMiles` e `cabinType`) da Sprint 10 para a Sprint 9 |
| **Justificativa** | Demanda do cliente por disponibilizar os filtros avançados mais cedo no ciclo, agregando valor à busca antes da entrega final |
| **Impacto em esforço** | +10 horas |
| **Impacto em prazo** | 0 dia de atraso macro (sem alteração do término previsto em 26/07/2026) |
| **Aprovação** | Abraão (GP) |
| **Risco vinculado** | R-04 — Mudança de escopo (Prob. 2 · Impacto 3 · Exposição 6) |
| **Situação** | Aprovado e absorvido na Sprint 9 — RF13 (filtros avançados) **entregue na release v0.9.0 (released em main)** |

A absorção do CR-MF-001 na Sprint 9 é evidenciada pela entrega de RF13: os PRs #11/#21/#27 (filtros `maxMiles`/`cabinType`) foram **concluídos em 15/06/2026 com revisor Cézar Velazquez (TL) — Approved, vote 10 (conta legada `Mateus Veloso` no Azure DevOps) — e mergeados em develop**, e a release **v0.9.0** foi promovida a main (tag nos três repositórios), deixando RF13 **Entregue (released em main)**; o card MF-65 foi transicionado para "Concluído" no Jira (board 614).

---

## 4. Tipo de tratamento

**Tipo de tratamento: Aditivo.** A mudança acrescenta esforço adicional ao projeto (+10 h, absorvidas na Sprint 9 — sprint de maior planejamento, 69 SP), caracterizando uma mudança aditiva conforme o modelo da Timeware (TPL-GPR-006 §4), e não uma troca de prioridade de mesmo tamanho nem um crédito ao cliente.

---

## 5. Impacto consolidado

| Dimensão | Impacto |
|---|---|
| **Prazo** | 0 dia de atraso macro; término previsto mantido em 26/07/2026 |
| **Esforço** | +10 horas absorvidas dentro da Sprint 9 |
| **Escopo** | Antecipação de RF13 (filtros avançados) de S10 para S9, entregue na release v0.9.0 (main) na S9; nenhum requisito novo adicionado |
| **Risco** | Materialização controlada do risco R-04 (mudança de escopo), tratada via change request formal |

---

## 6. Rastreabilidade

| Referência | Relação |
|---|---|
| PLA-MILHASFACIL01-001 | Plano de projeto — escopo e cronograma macro impactados |
| RAC-MILHASFACIL01-001 | Acompanhamento da Sprint 9 (RF13 entregue na release v0.9.0) |
| TAP-MILHASFACIL01-001 §8 | Risco R-04 (mudança de escopo) vinculado ao CR-MF-001 |
| GEST-MILHASFACIL01-001 | Planilha de gestão — fonte da verdade do registro do CR |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Aderência ao TPL-GPR-006: inclusão da classificação explícita do tipo de tratamento (Aditivo, §4), com justificativa coerente ao impacto de +10 h. Renumeração das seções subsequentes. |
