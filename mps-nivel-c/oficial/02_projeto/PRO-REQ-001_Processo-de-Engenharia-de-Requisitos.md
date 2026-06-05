# Processo de Engenharia de Requisitos — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-REQ-001 — Processo de Engenharia de Requisitos |
| **Versão** | 1.1 |
| **Data** | 15/12/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware levanta, especifica, analisa, valida e mantém os requisitos dos seus projetos de software sob medida, assegurando o entendimento comum entre cliente e equipe e a rastreabilidade entre necessidades e o que é construído.

## 2. Visão geral

Os requisitos são trabalhados a partir do **Discovery**, conduzido em conjunto por **Tech Lead e Product Owner** junto ao cliente, após a abertura formal do projeto (kickoff gerencial). O Documento de Requisitos reúne a especificação funcional e técnica e alimenta a concepção (arquitetura, design, estimativas). Os requisitos evoluem ao longo do projeto: mudanças estruturais identificadas no design adiantado podem atualizá-los — sempre com controle e rastreabilidade; após a aprovação do plano, mudanças de escopo seguem o fluxo de change request.

## 3. Identificação de necessidades e entendimento

- As necessidades das partes interessadas são identificadas durante o **Discovery** (Tech Lead + PO), por meio de reuniões, levantamento e análise junto ao cliente.
- O **entendimento** das necessidades é confirmado com o cliente, evitando interpretações divergentes.
- As necessidades identificadas dão origem aos requisitos, registrados no **Documento de Requisitos** (TPL-REQ-001).

## 4. Especificação, priorização e alocação

- Os requisitos são **especificados** de forma clara e verificável (como épicos e histórias, com critérios de aceite).
- São **priorizados** conforme valor e dependências, e organizados no backlog.
- São **alocados** aos incrementos/sprints e aos componentes do produto.

## 5. Compromisso da equipe técnica

- A equipe técnica revisa os requisitos e **assume o compromisso** com o que será desenvolvido, registrando esse aceite (ata ou registro no Jira).
- Mudanças relevantes nos requisitos exigem novo comprometimento.

## 6. Rastreabilidade

- É mantida a **rastreabilidade bidirecional** entre necessidades, requisitos, itens do backlog, design, código e testes.
- A rastreabilidade é registrada na **Matriz de Rastreabilidade** (TPL-REQ-002) e/ou pelos vínculos do Jira (épico → história → tarefa → caso de teste).
- A rastreabilidade permite avaliar o impacto de mudanças e garantir que todo requisito seja atendido e verificado.

## 7. Revisão, análise e validação

- **Revisão de consistência:** planos e produtos de trabalho são revisados quanto à consistência com os requisitos; inconsistências são tratadas.
- **Análise:** os requisitos são analisados quanto a serem necessários, suficientes, viáveis e verificáveis.
- **Validação:** os requisitos são validados com o cliente, garantindo que refletem suas necessidades reais — incluindo a validação por meio de protótipos/wireframes quando há UX/UI.

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

## 11. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados do processo **Engenharia de Requisitos (REQ)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| REQ 1 — necessidades identificadas e entendimento confirmado | Seção 3 |
| REQ 2 — requisitos especificados, priorizados e alocados | Seção 4 |
| REQ 3 — compromisso da equipe | Seção 5 |
| REQ 4 — rastreabilidade | Seção 6 |
| REQ 5 — revisão de consistência | Seção 7 |
| REQ 6 — análise | Seção 7 |
| REQ 7 — validação | Seção 7 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/10/2025 | Time de Melhoria Contínua | Definição inicial do processo de engenharia de requisitos |
| 1.1 | 15/12/2025 | Time de Melhoria Contínua | Contextualização do Discovery no novo fluxo (após kickoff gerencial; alimenta a concepção) |
