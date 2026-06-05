# Registro de Garantia da Qualidade — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | GQA-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GQA (evidência de projeto) |

---

## 1. Objetivo

Registrar as atividades de Garantia da Qualidade (GQA) realizadas ao longo do projeto Cadastro de Clientes — Rede D1000, incluindo auditorias de processo, não conformidades identificadas e ações corretivas.

---

## 2. Responsável pela GQA no projeto

| Papel | Responsável |
|---|---|
| Responsável por GQA (auditor de processo) | COO (Operações Timeware) |
| Ponto de contato no projeto | Abraão Oliveira (Gerente de Projeto) |
| Tech Lead (verificação técnica) | Tiago Nascimento |

---

## 3. Auditorias de processo realizadas

### Auditoria GQA-P01 — Verificação de aderência ao processo no Sprint 5

| Item | Valor |
|---|---|
| Data | 20/06/2025 |
| Escopo | Verificação da aderência ao processo-padrão Timeware nos Sprints 1–5 |
| Auditor | COO (Operações) |
| Resultado | Conforme com ressalvas (2 não conformidades) |

**Checklist verificado:**

| Item verificado | Resultado | Observação |
|---|---|---|
| Plano de projeto documentado antes do início dos sprints | Conforme | PLA-PROFARMA01-001 disponível |
| Requisitos documentados antes da implementação | Não conforme (NC-01) | Sprints 1–3 sem documento formal de requisitos; levantamento realizado informalmente |
| Revisão de código em todos os PRs | Conforme | Evidenciado no histórico do Azure DevOps |
| Pipeline CI executando testes a cada push | Conforme | Pipeline configurada desde Sprint 1 |
| Rastreabilidade histórias → tarefas | Não conforme (NC-02) | Jira adotado apenas a partir do Sprint 4; Sprints 1–3 sem rastreabilidade formal |
| Registro de riscos atualizado | Conforme | Riscos registrados no PLA |
| Sprint Review com presença do cliente | Conforme | Helena Moreira e Armando Junior presentes nas reviews documentadas |

**Não conformidades identificadas:**

| ID | Descrição | Severidade | Ação corretiva | Prazo | Status |
|---|---|---|---|---|---|
| NC-01 | Documentação de requisitos elaborada retroativamente para Sprints 1–3 | Menor | Elaborar REQ-PROFARMA01-001 cobrindo todos os requisitos identificados; manter atualizado prospectivamente a partir do Sprint 6 | 30/06/2025 | Resolvida |
| NC-02 | Sprints 1–3 sem rastreabilidade formal de histórias para tarefas no Jira | Menor | Registro retroativo das histórias dos Sprints 1–3 no Jira; uso consistente a partir do Sprint 4 | 30/06/2025 | Resolvida |

---

### Auditoria GQA-P02 — Verificação de processo na fase de homologação

| Item | Valor |
|---|---|
| Data | 10/10/2025 |
| Escopo | Verificação da aderência ao processo de V&V e gestão de defeitos durante a fase de homologação |
| Auditor | COO (Operações) |
| Resultado | Conforme |

**Checklist verificado:**

| Item verificado | Resultado | Observação |
|---|---|---|
| Plano de V&V documentado | Conforme | VV-PROFARMA01-001 disponível |
| Roteiros de teste formalizados e aprovados pelo cliente | Conforme | Aprovados por Julielle Santos (QA D1000) |
| Defeitos registrados e classificados por severidade | Conforme | Todos os defeitos registrados no Jira com severidade e responsável |
| SLA de correção de defeitos S1 e S2 cumprido | Conforme | Nenhum S1 aberto há mais de 24h; S2 dentro do prazo de 3 dias |
| Aceites parciais de sprint documentados | Conforme | Emails de aceite arquivados por Helena Moreira |
| Change requests formalizados antes da implementação | Conforme | 12 CRs registrados; todos com aprovação antes da implementação |

---

### Auditoria GQA-P03 — Verificação de encerramento do projeto

| Item | Valor |
|---|---|
| Data | 05/06/2026 |
| Escopo | Verificação da completude dos artefatos de encerramento e conformidade com o processo de GPR |
| Auditor | COO (Operações) |
| Resultado | Conforme |

**Checklist verificado:**

| Item verificado | Resultado | Observação |
|---|---|---|
| Termo de abertura (TAP) disponível | Conforme | TAP-PROFARMA01-001 |
| Plano de projeto (PLA) disponível | Conforme | PLA-PROFARMA01-001 |
| Documento de requisitos (REQ) disponível | Conforme | REQ-PROFARMA01-001 |
| Documento de design (PCP) disponível | Conforme | PCP-PROFARMA01-001 |
| Plano de V&V (VV) disponível | Conforme | VV-PROFARMA01-001 |
| Registro de adaptação (ADAP) disponível | Conforme | ADAP-PROFARMA01-001 |
| Lições aprendidas (LI) disponível | Conforme | LI-PROFARMA01-001 |
| Termo de encerramento (TAE) disponível | Conforme | TAE-PROFARMA01-001 |
| Aceite formal do cliente documentado | Conforme | Registrado no TAE |
| Lições aprendidas comunicadas à organização | Conforme | Oportunidades de melhoria identificadas e encaminhadas ao COO |

---

## 4. Resumo das não conformidades

| ID | Sprint/Fase | Categoria | Severidade | Status |
|---|---|---|---|---|
| NC-01 | Sprints 1–3 | Documentação de requisitos | Menor | Resolvida (30/06/2025) |
| NC-02 | Sprints 1–3 | Rastreabilidade (Jira) | Menor | Resolvida (30/06/2025) |

Total de não conformidades identificadas: **2**
Total resolvidas: **2**
Total em aberto: **0**

---

## 5. Parecer final de GQA

O projeto Cadastro de Clientes — Rede D1000 atendeu aos requisitos do processo-padrão Timeware com as adaptações formalmente registradas em ADAP-PROFARMA01-001. As duas não conformidades identificadas na Auditoria GQA-P01 foram de natureza menor (ausência de formalização retroativa) e foram corrigidas dentro do prazo estabelecido. O projeto encerrou em conformidade com os processos GPR, REQ, PCP e VV.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — reconstituída consolidando as três auditorias realizadas ao longo do projeto |
