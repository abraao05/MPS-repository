# Material de Treinamento — Desenvolvedores

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-018 — Trilha Desenvolvedores |
| **Versão** | 1.2 |
| **Data** | 10/01/2026 |
| **Papel** | Desenvolvedores |
| **Processos cobertos** | PCP (Projeto e Construção do Produto) |

---

## 1. O fluxo do processo-padrão da Timeware

```
Faixa 1 — entrada, abertura e requisitos
  1. Originação → 2. Escritório de Projetos → 3. Abertura → 4. Discovery + Requisitos

Faixa 2 — concepção e aprovação do plano
  5. Concepção → 6. Planejamento e aprovação

Faixa 3 — construção e entrega
  7. Grooming → Planning → Dev + code review  ← você está aqui
  → QA (V&V) → Homologação → Encerramento
```

---

## 2. Seu papel no geral

Você implementa o produto conforme o design definido pelo Tech Lead, dentro das sprints. Testa pelos critérios de aceite antes de passar para o QA, e mantém o código versionado e revisado.

| Processo | Seu envolvimento | Etapa no fluxo |
|---|---|---|
| PCP | Protagonista da construção | Dev nas sprints |

---

## 3. PCP — Projeto e Construção do Produto

Processo de referência: **PRO-PCP-001**. Design de referência: **TPL-PCP-001** (Documento de Design / Arquitetura, feito pelo Tech Lead). Convenção: **CONV-ORG-001** (nomenclatura e versionamento).

### 3.1 Implementação

**Input:** Documento de Design / Arquitetura aprovado (TPL-PCP-001). Itens do backlog com critérios de aceite (após grooming/refinamento).

**O que você faz:** Implementa o produto conforme o design, mantendo rastreabilidade (o código atende ao que o design especifica). Testa pelos critérios de aceite antes de entregar. Submete code review via pull request.

**Output:** Código + build → Git / Azure DevOps. Documentação técnica mantida. Pull request revisado (evidência de revisão por pares — VV 2).

**Onde fica:** Git / Azure DevOps.

**Atende:** PCP 3.

> **Definição de Pronto (Timeware):** critérios de aceite → code review → testes QA → homologação/staging. Você é responsável pelos dois primeiros (aceite + code review) antes de passar para o QA.

### 3.2 Configuração no dia a dia

**Input:** Convenção de versionamento (CONV-ORG-001).

**O que você faz:** Versiona conforme a convenção (branches, commits, tags). Registra modificações.

**Output:** Histórico de versões e modificações → Git / Azure DevOps.

**Atende:** Apoia GCO 4 (operação).

---

## 4. O que é medido no seu trabalho

Você gera dados de **previsibilidade** e **qualidade**. Você registra, não calcula.

| O que você registra (Jira) | Vira o indicador |
|---|---|
| Esforço estimado (planning poker) vs. real | Esforço estimado × real |
| Pontos entregues por sprint | Velocity |
| Subtarefas de bug / retrabalho | Retrabalho |
| Defeitos no seu código | Densidade de defeitos |

---

## 5. Referência rápida

| Momento | Você entrega | Referência | Onde |
|---|---|---|---|
| Construção | Código conforme design | TPL-PCP-001 | Git / Azure |
| Revisão | Pull request revisado | — | Git / Azure |
| Versionamento | Histórico + tags | CONV-ORG-001 | Git / Azure |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/12/2024 | Time de Melhoria Contínua | Versão inicial — baseada no processo PCP |
| 1.1 | 15/04/2025 | Time de Melhoria Contínua | Clarificação sobre dados a registrar no Jira para indicadores de medição |
| 1.2 | 10/01/2026 | Time de Melhoria Contínua | Atualização conforme PRO-PCP-001 v1.1 |
