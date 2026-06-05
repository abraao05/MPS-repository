# Material de Treinamento — Time de Melhoria Contínua / SEPG

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-014 — Trilha Time de Melhoria Contínua / SEPG |
| **Versão** | 1.0 |
| **Data** | 01/06/2026 |
| **Papel** | Time de Melhoria Contínua / SEPG (inclui função de GQA em rodízio) |
| **Processos cobertos** | GPC (Gerência de Processos), GQA (Garantia da Qualidade) |

---

## 1. O fluxo do processo-padrão da Timeware

```
Faixa 1 — entrada, abertura e requisitos
  1. Originação → 2. Escritório de Projetos → 3. Abertura → 4. Discovery + Requisitos

Faixa 2 — concepção e aprovação do plano
  5. Concepção → 6. Planejamento e aprovação (cliente aprova → baseline)

Faixa 3 — construção e entrega
  7. Grooming → Planning → Dev + code review → QA (V&V) → Homologação
  → Encerramento formal + lições aprendidas
```

---

## 2. Seu papel no geral

Vocês são o grupo de processos (SEPG): definem a biblioteca de ativos (processos, templates), as estratégias de qualidade e de risco, e mantêm a melhoria contínua. A função de **GQA** é exercida por membros do time em **rodízio**, com independência (auditor de fora da equipe avaliada).

| Processo | Seu envolvimento | Etapa no fluxo |
|---|---|---|
| GPC | Protagonista — definem e mantêm os ativos | Organizacional |
| GQA | Protagonista — verificam aderência (rodízio) | Transversal — marcos + amostragem por sprint |

> **Princípio fundamental:** definir ≠ executar ≠ fiscalizar. Vocês definem os processos e fazem a GQA, mas a engenharia é quem executa. Na auditoria, o auditor não pode ser o autor do que está auditando.

---

## 3. GPC — Gerência de Processos

Documentos de referência: **PLA-GPC-001** (plano de gestão e melhoria), **PRO-GPC-001** (processo-padrão), **GUIA-GPC-001** (adaptação), **PRO-GPC-002** (definição do time), **EST-GPC-001** (estratégia de GQA), **EST-GPC-002** (estratégia de riscos).

### 3.1 Biblioteca de ativos de processo

**Input:** Objetivos de negócio e necessidades dos processos. Oportunidades de melhoria vindas dos projetos e da GQA.

**O que você faz:** Identifica e mantém os ativos de processo necessários (inventário). Define e mantém o processo-padrão organizacional e as diretrizes de adaptação. Estabelece a estrutura de apoio (SEPG), ambientes-padrão e o repositório de medidas.

**Output:** Inventário de ativos → PLA-GPC-001 §2 (Confluence). Processo-padrão → PRO-GPC-001 + GUIA-GPC-001 (Confluence). Definição do time → PRO-GPC-002 (Confluence).

**Onde fica:** Confluence (espaço Processos, edição restrita ao time).

**Atende:** GPC 1, 2, 6, 8, 9.

### 3.2 Estratégias de qualidade e risco

**O que você faz:** Define a estratégia e os planos de garantia da qualidade. Define a estratégia de gerência de riscos e oportunidades.

**Output:** EST-GPC-001 (Estratégia de GQA) + EST-GPC-002 (Estratégia de Riscos) → Confluence.

**Atende:** GPC 3, 7.

### 3.3 Melhoria contínua

**Input:** Oportunidades de melhoria de projetos, GQA, lições aprendidas.

**O que você faz:** Identifica e mantém as oportunidades de melhoria. Planeja, implementa e avalia a efetividade das melhorias. Implanta os processos-padrão na organização.

**Output:** Registro de oportunidades de melhoria → PLA-GPC-001 §5.1 (Jira). Plano de melhorias + avaliação de efetividade → PLA-GPC-001 §5 e §6 (Confluence).

**Atende:** GPC 4, 5, 10, 11.

---

## 4. GQA — Garantia da Qualidade

Estratégia de referência: **EST-GPC-001**. A GQA é função do time, exercida em **rodízio**.

**Input:** O processo definido (PRO-GPC-001) e os produtos de trabalho da engenharia. Cronograma de verificação (marcos + amostragem por sprints).

**O que você faz:** Verifica objetivamente a **aderência ao processo** (a engenharia seguiu o que está definido?). Avalia os **produtos de trabalho** vs. o padrão. Identifica oportunidades de melhoria durante a garantia da qualidade. Não avalia código (isso é V&V: Dev + QA) — apenas observa indicadores de bugs/retrabalho para melhoria.

**Output:** Registros de Garantia da Qualidade → Confluence. Ações de não-conformidade → Jira. Oportunidades de melhoria → alimentam GPC 4.

**Onde fica:** Confluence (registros) + Jira (ações).

**Atende:** GPC 3 (execução) e os atributos de capacidade CP (iv), (v), (vi).

> **Independência:** rodízio + auditor de fora da equipe avaliada. Ao auditar o próprio Time de Processos, o auditor não pode ser o autor do que está auditando. Reporte: GQA → Time; impasses escalam ao COO.

---

## 5. O que é medido no seu trabalho

Vocês não geram os 7 indicadores de projeto diretamente, mas **mantêm o repositório** e usam os dados de não-conformidade/melhoria. A efetividade das melhorias (GPC 11) é avaliada por vocês.

---

## 6. Referência rápida

| Tema | Vocês entregam | Documento | Onde |
|---|---|---|---|
| Inventário de ativos | Lista de ativos | PLA-GPC-001 §2 | Confluence |
| Processo-padrão | Processo + adaptação | PRO-GPC-001 / GUIA-GPC-001 | Confluence |
| Estratégia de qualidade | Estratégia de GQA | EST-GPC-001 | Confluence |
| Estratégia de risco | Estratégia de riscos | EST-GPC-002 | Confluence |
| Melhoria | Oportunidades + plano | PLA-GPC-001 §5 | Jira / Confluence |
| GQA | Registros de aderência | (EST-GPC-001) | Confluence / Jira |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 01/06/2026 | Time de Melhoria Contínua | Versão inicial — baseada nos processos GPC e GQA |
