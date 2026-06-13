# Material de Treinamento — Tech Lead / Arquiteto

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-016 — Trilha Tech Lead / Arquiteto |
| **Versão** | 1.2 |
| **Data** | 15/02/2026 |
| **Papel** | Tech Lead / Arquiteto |
| **Processos cobertos** | REQ, PCP, ITP, GDE, GCO (operação) |

---

## 1. O fluxo do processo-padrão da Timeware

```
Faixa 1 — entrada, abertura e requisitos
  1. Originação → 2. Escritório de Projetos → 3. Abertura
  → 4. Discovery + Requisitos  ← você entra aqui

Faixa 2 — concepção e aprovação do plano
  5. Concepção [Trilha Projeto + Trilha Produto]  ← você lidera a trilha técnica
  → 6. Planejamento e aprovação (baseline)

Faixa 3 — construção e entrega
  7. Grooming → Planning → Dev + code review → QA (V&V) → Homologação
  → Encerramento
```

---

## 2. Seu papel no geral

Você é a **autoridade técnica do projeto**. Conduz o discovery junto com o PO/PM, desenha a arquitetura e o design, decide questões técnicas relevantes, comanda a integração e opera a gerência de configuração no dia a dia. Você participa de cinco processos:

| Processo | Seu envolvimento | Etapa no fluxo |
|---|---|---|
| REQ | Protagonista técnico — conduz discovery com PO/PM | Discovery → Requisitos |
| PCP | Protagonista — desenha arquitetura/design, guia os Devs | Trilha técnica, Dev nas sprints |
| ITP | Co-conduz com DevOps | Homolog / staging / produção |
| GDE | Protagonista técnico — junto com GP | Decisões de arquitetura |
| GCO (operação) | Operação no dia a dia | Transversal (todo o projeto) |

---

## 3. REQ — Engenharia de Requisitos

Processo de referência: **PRO-REQ-001**. Templates: **TPL-REQ-001** (Documento de Requisitos), **TPL-REQ-002** (Matriz de Rastreabilidade).

**Input:** Projeto aberto (Termo de Abertura, do GP). Necessidades do cliente a levantar.

**O que você faz:** Conduz o discovery junto com o PO/PM: levanta e confirma o entendimento das necessidades. Especifica, prioriza e aloca os requisitos. Garante a rastreabilidade bidirecional (requisito ↔ design ↔ teste). Analisa se os requisitos são necessários e suficientes; valida com o cliente.

**Output:** Documento de Requisitos → template **TPL-REQ-001**. Matriz de Rastreabilidade → template **TPL-REQ-002**. Registro de análise e de validação de requisitos.

**Onde fica:** Confluence (nó "Requisitos" do projeto).

**Atende:** REQ 1, 2, 4, 5, 6, 7 (o compromisso da equipe — REQ 3 — é registrado em ata pelo GP).

---

## 4. PCP — Projeto e Construção do Produto

Processo de referência: **PRO-PCP-001**. Template: **TPL-PCP-001** (Documento de Design / Arquitetura).

### 4.1 Design / Arquitetura

**Input:** Documento de Requisitos aprovado.

**O que você faz:** Desenvolve o design da solução (arquitetura, modelo de dados, integrações), mantendo rastreabilidade com os requisitos. Conduz a revisão do design e trata os problemas encontrados.

> **Tailoring:** se o projeto não tem front-end (só API/backend), a etapa de design UX/UI não se aplica — você mantém apenas o design técnico.

**Output:** Documento de Design / Arquitetura → template **TPL-PCP-001**. Registro de revisão de design.

**Onde fica:** Confluence (nó "Design" do projeto).

**Atende:** PCP 1, 2.

### 4.2 Construção (nas sprints)

**Input:** Design aprovado.

**O que você faz:** Guia os Devs na implementação conforme o design. Garante que o produto implementado seja rastreável ao design e que a documentação técnica seja mantida.

**Output:** Código + build + documentação técnica → Git / Azure DevOps.

**Atende:** PCP 3.

---

## 5. ITP — Integração do Produto

Processo de referência: **PRO-ITP-001**. Template: **TPL-ITP-001** (Estratégia de Integração). Você co-conduz com o DevOps.

**Input:** Componentes desenvolvidos, design e interfaces definidos.

**O que você faz:** Define a estratégia de integração e as interfaces. Avalia a prontidão dos componentes antes de integrar. Garante que os componentes sejam integrados conforme a estratégia e que o produto integrado seja testado. Acompanha a entrega do produto e do material de apoio.

**Output:** Estratégia / Plano de Integração → template **TPL-ITP-001**. Definição do ambiente de integração → Azure DevOps. Registros de prontidão, integração, testes de integração e entrega.

**Onde fica:** Template/registros no Confluence; ambiente e integração no Azure DevOps.

**Atende:** ITP 1 a 6.

> **Ambientes Timeware:** Dev, QA, Homologação e Stage (réplica de produção para o cliente) → Produção. Stage não é obrigatório em todo projeto.

---

## 6. GDE — Gerência de Decisões

Processo de referência: **PRO-GDE-001**. Template: **TPL-GDE-001** (Registro de Análise de Decisão — RAD). Você é o protagonista técnico, junto com o GP.

**Input:** Uma decisão técnica que se enquadra nos **gatilhos** de decisão formal (PRO-GDE-001 §3) — tipicamente escolha de arquitetura, tecnologia ou abordagem com impacto relevante.

**O que você faz:** Reconhece que a decisão exige análise formal (nem toda decisão exige). Estrutura: problema, alternativas, critérios, método de avaliação, decisão.

**Output:** Registro de Análise de Decisão (RAD) → template **TPL-GDE-001**.

**Onde fica:** Confluence (decisões do projeto).

**Atende:** GDE 1 a 6.

> Toda decisão de arquitetura vira RAD? Não — só as que se enquadram nos gatilhos do PRO-GDE-001 §3.

---

## 7. GCO — Gerência de Configuração (operação)

Processo de referência: **PLA-GCO-001**. Convenção: **CONV-ORG-001**.

**Input:** Itens de configuração do projeto (código, artefatos) e a convenção de nomenclatura/versionamento.

**O que você faz:** Identifica e controla os itens de configuração conforme os níveis definidos. Estabelece baselines (tags/releases) e registra itens e modificações. Opera o controle de mudanças (junto com o Change Request do GP).

**Output:** Baselines, tags/releases, registros de itens e modificações → Git / Azure DevOps.

**Atende:** GCO 2, 3, 4 (operação).

---

## 8. O que é medido no seu trabalho

Você gera dado que alimenta indicadores de **qualidade** (PLA-MED-001). Você registra, não calcula — o Responsável de Medição consolida.

| O que você/o time registra | Vira o indicador |
|---|---|
| Defeitos identificados × esforço (via Jira) | Densidade de defeitos |
| Bugs reabertos / subtarefas de bug | Retrabalho |

---

## 9. Referência rápida

| Momento | Você entrega | Template | Onde |
|---|---|---|---|
| Requisitos | Doc. de Requisitos + Matriz | TPL-REQ-001 / 002 | Confluence |
| Design | Documento de Design / Arquitetura | TPL-PCP-001 | Confluence |
| Construção | Código + doc. técnica | — | Git / Azure |
| Integração | Estratégia de Integração | TPL-ITP-001 | Confluence / Azure |
| Decisão formal | RAD | TPL-GDE-001 | Confluence |
| Configuração | Baselines + registros | (CONV-ORG-001) | Git / Azure |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/03/2025 | Time de Melhoria Contínua | Versão inicial |
| 1.1 | 22/09/2025 | Time de Melhoria Contínua | Inclusão da seção GDE e revisão da seção GCO |
| 1.2 | 15/02/2026 | Time de Melhoria Contínua | Atualização das seções ITP e VV conforme revisões dos processos |
