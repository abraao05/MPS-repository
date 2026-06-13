# Material de Treinamento — GCO Baseline / Auditoria de Configuração

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-021 — Trilha GCO Baseline / Auditoria |
| **Versão** | 1.1 |
| **Data** | 22/09/2025 |
| **Papel** | GCO — Baseline / Auditoria de Configuração |
| **Processos cobertos** | GCO (Gerência de Configuração) |

---

## 1. O fluxo do processo-padrão da Timeware

```
Faixa 1 — entrada, abertura e requisitos
  1. Originação → 2. Escritório de Projetos → 3. Abertura → 4. Discovery + Requisitos

Faixa 2 — concepção e aprovação do plano
  5. Concepção → 6. Planejamento e aprovação

Faixa 3 — construção e entrega
  7. Grooming → Planning → Dev → QA → Homologação → Encerramento
  ↑ GCO é transversal — presente em todas as faixas
```

---

## 2. Seu papel no geral

Você estabelece o sistema de gerência de configuração: define os itens de configuração e níveis de controle, garante o controle de mudanças e executa as auditorias de configuração. A operação (commits, baselines no dia a dia) é do time técnico; você governa e audita.

| Processo | Seu envolvimento | Etapa no fluxo |
|---|---|---|
| GCO | Protagonista — define + audita | Transversal (todo o projeto) |

> **Separação de papéis:** Tech Lead e DevOps **operam** a configuração no dia a dia (commits, baselines, releases); você **define os níveis de controle e audita**. Deixe essa fronteira clara.

---

## 3. GCO — Gerência de Configuração

Plano de referência: **PLA-GCO-001**. Convenção: **CONV-ORG-001** (nomenclatura e versionamento).

### 3.1 Definição do sistema de configuração

**Input:** Os artefatos e códigos dos projetos. A convenção de nomenclatura/versionamento (CONV-ORG-001).

**O que você faz:** Identifica os itens de configuração e define os níveis de controle. Estabelece o sistema de GC e o controle de mudanças.

**Output:** Definição de itens + níveis de controle → PLA-GCO-001 §3 (Confluence). Sistema de GC e controle de mudanças → PLA-GCO-001 §4 (Git/Azure DevOps).

**Onde fica:** Confluence (definição); Git/Azure DevOps (sistema).

**Atende:** GCO 1, 2.

### 3.2 Baselines e registros

**Input:** Itens de configuração em evolução.

**O que você faz:** Garante que as baselines sejam estabelecidas (a operação faz tags/releases; você valida que seguem o padrão). Garante que itens e modificações sejam registrados.

**Output:** Baselines estabelecidas → Git / Azure DevOps (PLA-GCO-001 §5). Registros de itens e modificações → Git / Azure DevOps (§6).

**Onde fica:** Git / Azure DevOps.

**Atende:** GCO 3, 4 (governança).

### 3.3 Auditoria de configuração

**Input:** Baselines e registros existentes.

**O que você faz:** Executa as auditorias de configuração: verifica a integridade das baselines e se o que está versionado bate com o que deveria. A auditoria pode ser conduzida via GQA.

**Output:** Registro de auditoria de configuração → PLA-GCO-001 §7 (Confluence).

**Onde fica:** Confluence.

**Atende:** GCO 5.

---

## 4. O que é medido no seu trabalho

Você não alimenta os 7 indicadores de projeto. O que você observa é a **integridade da configuração** (resultado das auditorias): divergências encontradas, baselines fora do padrão.

---

## 5. Referência rápida

| Momento | Você entrega | Referência | Onde |
|---|---|---|---|
| Definição | Itens + níveis de controle | PLA-GCO-001 §3 | Confluence |
| Sistema | Controle de mudanças | PLA-GCO-001 §4 | Git / Azure |
| Baselines | Validação das baselines | PLA-GCO-001 §5 | Git / Azure |
| Auditoria | Registro de auditoria | PLA-GCO-001 §7 | Confluence |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/03/2025 | Time de Melhoria Contínua | Versão inicial — baseada no processo GCO |
| 1.1 | 22/09/2025 | Time de Melhoria Contínua | Revisão da fronteira de papéis DevOps × GCO Baseline |
