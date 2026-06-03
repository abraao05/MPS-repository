# Processo de Engenharia de Requisitos — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-REQ-001 — Processo de Engenharia de Requisitos |
| **Versão** | 1.1 |
| **Data** | `<dd/mm/aaaa>` |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Processos MPS-SW relacionados** | REQ 1 a REQ 7 |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware levanta, especifica, analisa, valida e mantém os requisitos dos seus projetos de software sob medida, assegurando o entendimento comum entre cliente e equipe e a rastreabilidade entre necessidades e o que é construído.

> **Mapa de resultados atendidos neste documento:**
> - Seção 3 → **REQ 1** (necessidades identificadas e entendimento confirmado)
> - Seção 4 → **REQ 2** (requisitos especificados, priorizados, alocados)
> - Seção 5 → **REQ 3** (compromisso da equipe)
> - Seção 6 → **REQ 4** (rastreabilidade)
> - Seção 7 → **REQ 5, 6, 7** (revisão de consistência, análise e validação)

## 2. Visão geral

Os requisitos são trabalhados a partir do **Discovery**, conduzido em conjunto por **Tech Lead e Product Owner** junto ao cliente, após a abertura formal do projeto (kickoff gerencial). O Documento de Requisitos reúne a especificação funcional e técnica e alimenta a concepção (arquitetura, design, estimativas). Os requisitos evoluem ao longo do projeto: mudanças estruturais identificadas no design adiantado podem atualizá-los — sempre com controle e rastreabilidade; após a aprovação do plano, mudanças de escopo seguem o fluxo de change request.

## 3. Identificação de necessidades e entendimento (REQ 1)

- As necessidades das partes interessadas são identificadas durante o **Discovery** (Tech Lead + PO), por meio de reuniões, levantamento e análise junto ao cliente.
- O **entendimento** das necessidades é confirmado com o cliente, evitando interpretações divergentes.
- As necessidades identificadas dão origem aos requisitos, registrados no **Documento de Requisitos** (TPL-REQ-001).

## 4. Especificação, priorização e alocação (REQ 2)

- Os requisitos são **especificados** de forma clara e verificável (como épicos e histórias, com critérios de aceite).
- São **priorizados** conforme valor e dependências, e organizados no backlog.
- São **alocados** aos incrementos/sprints e aos componentes do produto.

## 5. Compromisso da equipe técnica (REQ 3)

- A equipe técnica revisa os requisitos e **assume o compromisso** com o que será desenvolvido, registrando esse aceite (ata ou registro no Jira).
- Mudanças relevantes nos requisitos exigem novo comprometimento.

## 6. Rastreabilidade (REQ 4)

- É mantida a **rastreabilidade bidirecional** entre necessidades, requisitos, itens do backlog, design, código e testes.
- A rastreabilidade é registrada na **Matriz de Rastreabilidade** (TPL-REQ-002) e/ou pelos vínculos do Jira (épico → história → tarefa → caso de teste).
- A rastreabilidade permite avaliar o impacto de mudanças e garantir que todo requisito seja atendido e verificado.

## 7. Revisão, análise e validação (REQ 5, 6, 7)

- **Revisão de consistência (REQ 5):** planos e produtos de trabalho são revisados quanto à consistência com os requisitos; inconsistências são tratadas.
- **Análise (REQ 6):** os requisitos são analisados quanto a serem necessários, suficientes, viáveis e verificáveis.
- **Validação (REQ 7):** os requisitos são validados com o cliente, garantindo que refletem suas necessidades reais — incluindo a validação por meio de protótipos/wireframes quando há UX/UI.

## 8. Gestão de mudanças de requisitos

Mudanças de requisito são avaliadas quanto ao impacto (escopo, prazo, design), aprovadas pelo PO em conjunto com o cliente, refletidas no backlog e na rastreabilidade, e comunicadas à equipe. Esse fluxo conecta-se ao acompanhamento do design antecipado (PRO-GPC-001) e à gerência de projetos (PRO-GPR-001).

## 9. Papéis

| Papel | Responsabilidade |
|---|---|
| **Product Owner** | Conduz o levantamento com o cliente; mantém e prioriza requisitos; valida entregas. |
| **Tech Lead** | Conduz o Discovery com o PO; analisa viabilidade técnica dos requisitos. |
| **Equipe** | Revisa requisitos e assume compromisso; implementa conforme especificado. |
| **Cliente** | Fornece e valida as necessidades e requisitos. |

## 10. Documentos e artefatos relacionados

- PRO-GPC-001 — Processo-Padrão Organizacional
- TPL-REQ-001 — Template de Documento de Requisitos
- TPL-REQ-002 — Template de Matriz de Rastreabilidade
- PRO-GPR-001 — Processo de Gerência de Projetos
- Processo de Verificação e Validação (VV)

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Definição inicial do processo de engenharia de requisitos |
| 1.1 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Contextualização do Discovery no novo fluxo (após kickoff gerencial; alimenta a concepção) |
