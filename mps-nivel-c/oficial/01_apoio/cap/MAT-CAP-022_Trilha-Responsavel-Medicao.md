# Material de Treinamento — Responsável de Medição

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-022 — Trilha Responsável de Medição |
| **Versão** | 1.1 |
| **Data** | 10/01/2026 |
| **Papel** | Responsável de Medição (operação) |
| **Processos cobertos** | MED (Medição — operação) |

---

## 1. O fluxo do processo-padrão da Timeware

```
MED é transversal — coleta contínua por sprint, consolidação mensal.
Os outros papéis registram o dado bruto no Jira/Azure/Xray;
você coleta, verifica, consolida e comunica.
```

---

## 2. Seu papel no geral

Você é quem transforma o dado bruto das sprints em indicador organizacional. Coleta do Jira/Azure/Xray, verifica, consolida mensalmente e mantém o repositório de medidas. Você não decide ações — isso é da análise crítica trimestral (COO). Você participa de um processo:

| Processo | Seu envolvimento | Etapa no fluxo |
|---|---|---|
| MED | Protagonista (operação) | Transversal — coleta contínua por sprint, consolidação mensal |

> **Separação de papéis:** você **calcula e consolida** o indicador (os outros papéis registram o dado bruto). Quem **usa** para decidir é a análise crítica.

---

## 3. MED — Medição

Processo/plano de referência: **PLA-MED-001**. Repositório: **Jira**.

### 3.1 Catálogo de indicadores

O catálogo (PLA-MED-001 §3) tem 7 indicadores, divididos em previsibilidade e qualidade:

| Categoria | Indicador | De onde vem o dado |
|---|---|---|
| Previsibilidade | Aderência ao prazo | Jira (GP, Devs) |
| Previsibilidade | Esforço estimado × real | Jira (GP, Devs) |
| Previsibilidade | Velocity | Jira (GP, Devs) |
| Previsibilidade | Itens entregues × planejados | Jira (GP, PO) |
| Qualidade | Densidade de defeitos | Jira/Xray (QA) |
| Qualidade | Defeitos homolog × produção | Jira/Xray (QA, DevOps) |
| Qualidade | Retrabalho | Jira (subtarefas de bug — Devs, QA) |

> Burndown **não é** indicador organizacional — é ferramenta de sprint. Não o apresente como um dos 7.

### 3.2 Coleta, consolidação e repositório

**Input:** Dados brutos registrados por sprint pelos papéis de execução (Jira/Azure/Xray). Objetivos de medição e definições operacionais (PLA-MED-001 §2 e §3).

**O que você faz:** Coleta contínua por sprint. Verifica e armazena as medidas. **Consolida mensalmente** (esta é a etapa que gera tendências — consolidação ao longo do tempo). Mantém o repositório organizacional de medidas.

**Output:** Medidas coletadas, verificadas e armazenadas → Jira (PLA-MED-001 §4). Consolidação mensal → Jira / camada de consolidação.

**Onde fica:** Jira (repositório).

**Atende:** MED 2, 3.

### 3.3 Análise e comunicação

**Input:** Medidas consolidadas.

**O que você faz:** Apoia a análise do desempenho organizacional (PLA-MED-001 §5). Comunica os resultados periodicamente. Avalia periodicamente a qualidade do próprio repositório de medidas (PLA-MED-001 §8).

**Output:** Análise de desempenho → Jira / Confluence. Comunicação periódica dos resultados → Confluence (PLA-MED-001 §7). Avaliação de qualidade do repositório → Confluence (PLA-MED-001 §8).

**Onde fica:** Jira + Confluence.

**Atende:** MED 4, 6, 7; e GPC 9 (repositório + qualidade de medidas).

---

## 4. O que é medido no seu trabalho

Você opera a medição; quem usa para decidir é a análise crítica trimestral (COO). Quem identifica ações corretivas a partir das medidas (MED 5) é o nível de gestão — você consolida e reporta.

---

## 5. Referência rápida

| Momento | Você entrega | Referência | Onde |
|---|---|---|---|
| Coleta | Medidas verificadas e armazenadas | PLA-MED-001 §4 | Jira |
| Consolidação | Indicadores consolidados (mensal) | PLA-MED-001 §3 | Jira / camada a definir |
| Comunicação | Resultados periódicos | PLA-MED-001 §7 | Confluence |
| Qualidade | Avaliação do repositório | PLA-MED-001 §8 | Confluence |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/08/2025 | Time de Melhoria Contínua | Versão inicial — baseada no processo MED |
| 1.1 | 10/01/2026 | Time de Melhoria Contínua | Alinhamento com PLA-MED-001 v1.3 e atualização dos exemplos |
