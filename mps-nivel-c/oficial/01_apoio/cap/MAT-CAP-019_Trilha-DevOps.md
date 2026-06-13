# Material de Treinamento — DevOps

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-019 — Trilha DevOps |
| **Versão** | 1.1 |
| **Data** | 22/09/2025 |
| **Papel** | DevOps |
| **Processos cobertos** | ITP (Integração do Produto), GCO (Configuração — operação) |

---

## 1. O fluxo do processo-padrão da Timeware

```
Faixa 1 — entrada, abertura e requisitos
  1. Originação → 2. Escritório de Projetos → 3. Abertura → 4. Discovery + Requisitos

Faixa 2 — concepção e aprovação do plano
  5. Concepção → 6. Planejamento e aprovação

Faixa 3 — construção e entrega
  7. Grooming → Planning → Dev → QA → Homologação  ← você entra aqui
  → (Stage) → Produção
```

---

## 2. Seu papel no geral

Você opera a integração do produto e o pipeline até produção, junto com o Tech Lead, e cuida da configuração no dia a dia (baselines, releases).

| Processo | Seu envolvimento | Etapa no fluxo |
|---|---|---|
| ITP | Co-conduz com Tech Lead | Homolog / staging / produção |
| GCO (operação) | Operação (baselines/releases) | Transversal |

---

## 3. ITP — Integração do Produto

Processo de referência: **PRO-ITP-001**. Template: **TPL-ITP-001** (Estratégia de Integração).

**Input:** Componentes desenvolvidos. Estratégia/interfaces de integração (definida com o Tech Lead).

**O que você faz:** Estabelece o ambiente de integração. Garante que os componentes sejam integrados conforme a estratégia. Conduz o caminho de promoção entre ambientes até produção.

**Output:** Definição do ambiente de integração → Azure DevOps. Registro de integração → Azure DevOps. Contribuição na Estratégia/Plano de Integração (TPL-ITP-001).

**Onde fica:** Azure DevOps (ambientes, integração); template no Confluence.

**Atende:** ITP 2, 4 (e apoia 1, 3, 5, 6 com o Tech Lead).

> **Ambientes Timeware:** Dev, QA, Homologação e Stage (réplica de produção para o cliente) → Produção. O fluxo de promoção é: homolog → (stage) → cliente aprova → produção.

---

## 4. GCO — Gerência de Configuração (operação)

Plano de referência: **PLA-GCO-001**. Convenção: **CONV-ORG-001**.

**Input:** Builds e releases a controlar.

**O que você faz:** Estabelece baselines (tags/releases) no caminho até produção. Registra itens de configuração e modificações de release. Opera o controle de mudanças no pipeline (com o Change Request do GP).

**Output:** Baselines, tags/releases → Git / Azure DevOps (PLA-GCO-001 §5). Registros de itens e modificações → Git / Azure DevOps (§6).

**Onde fica:** Git / Azure DevOps.

**Atende:** GCO 3, 4 (operação).

---

## 5. O que é medido no seu trabalho

Você contribui com um dado de **qualidade**: defeitos em homologação × produção, porque você opera a promoção entre ambientes. Você registra, não calcula.

---

## 6. Referência rápida

| Momento | Você entrega | Referência | Onde |
|---|---|---|---|
| Integração | Ambiente + registro de integração | TPL-ITP-001 | Azure DevOps |
| Promoção | Caminho homolog → stage → produção | PRO-ITP-001 | Azure DevOps |
| Configuração | Baselines + releases | CONV-ORG-001 / PLA-GCO-001 | Git / Azure |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/03/2025 | Time de Melhoria Contínua | Versão inicial — baseada nos processos ITP e GCO |
| 1.1 | 22/09/2025 | Time de Melhoria Contínua | Revisão após dúvidas recorrentes sobre o fluxo de promoção entre ambientes |
