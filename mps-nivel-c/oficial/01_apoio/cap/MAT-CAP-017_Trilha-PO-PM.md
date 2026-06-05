# Material de Treinamento — PO / PM

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-017 — Trilha PO / PM |
| **Versão** | 1.0 |
| **Data** | 01/06/2026 |
| **Papel** | PO / PM (papel acumulável) |
| **Processos cobertos** | REQ (Engenharia de Requisitos) |

---

## 1. O fluxo do processo-padrão da Timeware

```
Faixa 1 — entrada, abertura e requisitos
  1. Originação → 2. Escritório de Projetos → 3. Abertura
  → 4. Discovery + Requisitos  ← você entra aqui

Faixa 2 — concepção e aprovação do plano
  5. Concepção → 6. Planejamento e aprovação

Faixa 3 — construção e entrega
  7. Grooming → Planning → Dev → QA → Homologação → Encerramento
```

---

## 2. Seu papel no geral

Você representa a voz do cliente/produto e conduz, junto com o Tech Lead, o discovery que vira os requisitos. Garante priorização e que o que foi levantado reflete a necessidade real.

| Processo | Seu envolvimento | Etapa no fluxo |
|---|---|---|
| REQ | Protagonista (lado produto/cliente) | Discovery → Requisitos |

---

## 3. REQ — Engenharia de Requisitos

Processo de referência: **PRO-REQ-001**. Templates: **TPL-REQ-001** (Documento de Requisitos), **TPL-REQ-002** (Matriz de Rastreabilidade).

### 3.1 Discovery e levantamento

**Input:** Projeto aberto (Termo de Abertura, do GP). Acesso às partes interessadas / cliente.

**O que você faz:** Conduz o discovery junto com o Tech Lead: levanta as necessidades das partes interessadas e confirma o entendimento. Prioriza os requisitos (visão de produto/valor).

**Output:** Documento de Requisitos → template **TPL-REQ-001** (produzido junto com o Tech Lead).

**Onde fica:** Confluence (nó "Requisitos" do projeto).

**Atende:** REQ 1, 2.

### 3.2 Validação e rastreabilidade

**Input:** Requisitos levantados.

**O que você faz:** Valida com o cliente que os requisitos refletem a necessidade (REQ 7). Apoia a rastreabilidade (requisito ↔ entrega).

**Output:** Contribuição para a **Matriz de Rastreabilidade** → **TPL-REQ-002**. Registro de validação de requisitos.

**Onde fica:** Confluence.

**Atende:** REQ 4, 7.

> **Fronteira de papéis:** o compromisso da equipe técnica (REQ 3) é registrado em ata pelo GP; a análise técnica de suficiência (REQ 6) é do Tech Lead. Você é o lado produto/cliente.

---

## 4. O que é medido no seu trabalho

Você contribui com um dado de previsibilidade: **itens entregues × planejados** (junto com o GP), pela visão do backlog de produto. Você registra no Jira — o Responsável de Medição consolida.

---

## 5. Referência rápida

| Momento | Você entrega | Template | Onde |
|---|---|---|---|
| Discovery | Documento de Requisitos | TPL-REQ-001 | Confluence |
| Rastreabilidade | Contribuição na Matriz | TPL-REQ-002 | Confluence |
| Validação | Registro de validação | — | Confluence |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 01/06/2026 | Time de Melhoria Contínua | Versão inicial — baseada no processo REQ |
