# Relatório de Eficácia de Treinamento — Ciclo 2025

| Campo | Valor |
|---|---|
| **Documento** | REL-CAP-001 — Relatório de Eficácia de Treinamento — Ciclo 2025 |
| **Versão** | 1.0 |
| **Data** | 15/10/2025 |
| **Referência** | TPL-CAP-002; PLA-CAP-001 §6; REG-CAP-001, REG-CAP-001B, REG-CAP-002, REG-CAP-002B, REG-CAP-003 |

---

## 1. Identificação do Relatório

| Campo | Preenchimento |
|---|---|
| **Código do relatório** | REL-CAP-001 |
| **Período avaliado** | dez/2024 a set/2025 |
| **Data do relatório** | 15/10/2025 |
| **Responsável** | Patricia Lima (Time de Melhoria Contínua) |
| **Sessões referenciadas** | REG-CAP-001, REG-CAP-001B, REG-CAP-002, REG-CAP-002B, REG-CAP-003 |

---

## 2. Resumo das Sessões Realizadas

| Sessão | Data | Processos cobertos | Participantes | Aprovados (1ª tentativa) | Taxa |
|---|---|---|---|---|---|
| REG-CAP-001 | 12/12/2024 | GPR, REQ, PCP | 6 | 5 | 83% |
| REG-CAP-001B | 17/01/2025 | GPR (reforço) | 1 | 1 | 100% |
| REG-CAP-002 | 14/03/2025 | VV, GCO, ITP, GDE | 6 | 4 | 67% |
| REG-CAP-002B | 26/09/2025 | VV, GCO (reforço) | 2 | 2 | 100% |
| REG-CAP-003 | 08/08/2025 | MED, GPC, OSW | 4 | 4 | 100% |
| **Total do período** | — | — | **19 participações** | **16 (1ª tentativa)** | **84% (1ª tent.)** |

> Considerando retakes: **100%** de aprovação ao final do ciclo.

Meta de taxa de aprovação: **≥ 80%** por sessão. REG-CAP-002 ficou abaixo da meta (67%) — gerando ações de melhoria.

---

## 3. Análise por Processo / Avaliação

| Avaliação | Média de notas | Questões com maior taxa de erro | Interpretação |
|---|---|---|---|
| AVA-CAP-001 v1.0 (dez/2024) | 74,5 | Bloco 2 (medição) — questão sobre burndown; bloco 4 (nomenclatura) | Participantes confundiam burndown com indicador; convenção pouco praticada |
| AVA-CAP-001 v1.1 (mar/2025) | 83,5 | — | Melhora após revisão do bloco de medição |
| AVA-CAP-002 (GPR) | 90 | — | Papel bem preparado |
| AVA-CAP-003 v1.1 (técnicos) | 78,3 | Questões 7–10 (VV/Gherkin) — Letícia Moraes com 68 | Gherkin pouco trabalhado no material original |
| AVA-CAP-004 v1.0 (GCO/ITP) | 74 | Questão 1 (baselines × releases) — Rafael Cunha com 65 | Material original sem diferenciação clara entre baseline e release |
| AVA-CAP-005 (GPC/MED/CAP) | 83,5 | — | Resultado satisfatório |

---

## 4. Análise por Papel

| Papel | Sessões participadas | Média geral | Tendência | Observação |
|---|---|---|---|---|
| GP / PO (Abraão Oliveira) | 2 | 86,5 | ↑ | Aprovado em todas as tentativas |
| Tech Lead (Cézar Hiraki) | 2 | 84 | ↑ | Notas melhores na segunda onda |
| Dev (Fernando Oliveira) | 2 | 73,7 | ↑ | Precisou de reforço na 1ª sessão; aprovado em retake |
| Dev (Henry Komatsu) | 2 | 73,7 | → | Notas consistentes |
| QA (Letícia Moraes) | 2 | 75 | ↑ | Dificuldade em VV/Gherkin; aprovada após revisão do material |
| DevOps (Rafael Cunha) | 2 | 71,5 | ↑ | Dificuldade em GCO; aprovado após revisão do material |
| GCO Baseline (Mariana Teixeira) | 2 | 89 | ↑ | Melhor desempenho consistente |
| Resp. Medição (Thiago Nunes) | 1 | 81 | — | Primeira sessão com resultado satisfatório |
| Time de Melhoria (Patricia Lima) | 1 | 89 | — | |

---

## 5. Conclusão de Eficácia

| Critério | Resultado | Atende? |
|---|---|---|
| Taxa de aprovação geral ≥ 80% (1ª tentativa) | 84% | Sim |
| Taxa de aprovação geral incluindo retakes | 100% | Sim |
| Nenhum papel com média final < 70 | Mínimo: 71,5 (Rafael Cunha) | Sim |
| Retakes concluídos dentro do período | Todos encerrados em set/2025 | Sim |

**O treinamento do período foi eficaz?** Parcialmente.

Justificativa: a meta de 80% de aprovação na primeira tentativa foi atingida no agregado (84%), porém a segunda onda (VV, GCO, ITP) ficou abaixo com 67%. Os materiais GUIA-CAP-004 (VV) e GUIA-CAP-005 (GCO) foram identificados como insuficientes nas seções de Gherkin e baselines. Os retakes confirmam que, com o material corrigido, os participantes atingiram o nível esperado. Ao final do ciclo: 100% dos participantes aprovados.

---

## 6. Ações de Melhoria Identificadas

| ID | Problema observado | Material afetado | Ação | Responsável | Prazo | Status |
|---|---|---|---|---|---|---|
| AM-01 | Gherkin não coberto adequadamente | GUIA-CAP-004, MAT-CAP-020 | Incluir seção dedicada a Gherkin com exemplos práticos | Time de Melhoria | 22/09/2025 | Concluído (v1.1) |
| AM-02 | Diferença baseline × release confusa | GUIA-CAP-005, MAT-CAP-021 | Rever seção de baselines com exemplos de Git tags × releases | Time de Melhoria | 22/09/2025 | Concluído (v1.1) |
| AM-03 | Bloco de medição do AVA-CAP-001 gerou confusão sobre burndown | AVA-CAP-001, GUIA-CAP-008 | Reforçar no material que burndown é ferramenta de sprint, não indicador | Time de Melhoria | 10/03/2025 | Concluído (v1.1) |
| AM-04 | Convenção de nomenclatura pouco praticada | AVA-CAP-001 (bloco 4) | Incluir exercício prático de nomenclatura nas próximas sessões | Time de Melhoria | jan/2026 | Incorporado em REG-CAP-004 |

---

## 7. Assinatura

| Campo | Preenchimento |
|---|---|
| **Responsável pelo relatório** | Patricia Lima |
| **Data** | 15/10/2025 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/10/2025 | Time de Melhoria Contínua | Versão inicial — relatório de eficácia do ciclo 2025 |
