# Relatório de Acompanhamento (Status Report) — [NOME DO PROJETO]

> **TEMPLATE (TPL-GPR-005).** Acompanhamento periódico do projeto, reportado às partes interessadas na cadência acordada (GPR 14, GPR 15). Modelo executivo: priorize clareza e a leitura do decisor. Substitua os campos `[ ]` e remova as instruções em itálico na versão final. Seções não aplicáveis ao período podem ser omitidas, exceto a §1 (Situação geral), que é obrigatória.

| Campo | Valor |
|---|---|
| **Projeto** | [Nome do projeto] |
| **Cliente** | [Cliente] |
| **Período de referência** | [ex.: Sprint 7 · 02/06–13/06/2026 / Quinzena / Mês] |
| **Data do relatório** | [dd/mm/aaaa] |
| **Gerente de Projeto** | [responsável] |
| **Destinatários** | [partes interessadas que recebem este report] |

---

## 1. Situação geral

*[Uma frase executiva: onde o projeto está e o que o decisor precisa saber agora. Em seguida, o painel RAG.]*

| Dimensão | Status | Comentário (1 linha) |
|---|---|---|
| **Prazo** | 🟢 No prazo / 🟡 Atenção / 🔴 Atrasado | [...] |
| **Escopo** | 🟢 Estável / 🟡 Em mudança / 🔴 Crítico | [...] |
| **Risco** | 🟢 Sob controle / 🟡 Atenção / 🔴 Crítico | [...] |
| **Qualidade** | 🟢 Dentro do esperado / 🟡 Atenção / 🔴 Crítico | [...] |

> *Convenção de cores:* 🟢 sem ação necessária · 🟡 sob acompanhamento, ação em curso · 🔴 exige decisão/atenção do cliente.

## 2. Resumo do período

*[Visão narrativa curta (3–5 linhas) do que aconteceu no período. Linguagem de negócio, não técnica. É a única seção que muitos decisores leem — torne-a autossuficiente.]*

**Indicadores do período (destaque):**

| Indicador | Valor |
|---|---|
| Horas trabalhadas no período | [h] |
| Entregas concluídas | [n] |
| Avanço do projeto (acumulado) | [%] |
| [outro indicador-chave do projeto] | [...] |

### 2.1 Registro de dailys internas

*[Seção interna — registra presença da equipe Timeware nas dailys e os principais temas tratados na sprint. Omita ou resuma na versão enviada ao cliente, se aplicável.]*

**Presenças por daily:**

| Data | Equipe presente | Ausência / motivo |
|---|---|---|
| [dd/mm] | [papéis presentes] | [motivo ou —] |

**Resumo semanal:**

| Semana | Principais tópicos e decisões internas |
|---|---|
| [dd/mm – dd/mm] | [...] |
| [dd/mm – dd/mm] | [...] |

---

## 3. Entregas realizadas no período

*[O que foi concluído e o valor que gera para o cliente. Liste entregáveis, não tarefas. Quando houver entrega "além do contrato" ou cortesia, destaque — é informação executiva relevante.]*

| Entrega | Resultado / valor para o cliente | Situação |
|---|---|---|
| [...] | [...] | ✅ Concluído |
| [...] | [...] | ✅ Concluído |

## 4. Planejado para o próximo período

*[O que será atacado no próximo ciclo e os marcos associados.]*

| Item / marco | Data prevista | Observação |
|---|---|---|
| [...] | [dd/mm/aaaa] | [...] |

## 5. Indicadores do projeto (acompanhamento)

*[Indicadores acompanhados conforme a Medição (PLA-MED-001). Use a tendência para mostrar evolução em relação ao report anterior.]*

| Indicador | Meta / referência | Período atual | Tendência |
|---|---|---|---|
| Aderência ao prazo (SPI) | [≥ 0,90] | [...] | ⬆️ / ➡️ / ⬇️ |
| Esforço estimado × realizado | [≤ 10% desvio] | [...] | ⬆️ / ➡️ / ⬇️ |
| Velocity | [referência] | [...] | ⬆️ / ➡️ / ⬇️ |
| Defeitos / qualidade | [...] | [...] | ⬆️ / ➡️ / ⬇️ |

## 6. Diário de bordo (eventos e impactos)

*[Registre eventos relevantes do período — bloqueios, dependências externas, decisões — com o impacto em prazo. Esta seção dá rastreabilidade objetiva dos desvios e protege o projeto: cada atraso fica documentado com causa e responsável.]*

| Data | Evento / motivo | Origem | Impacto (dias) | Situação |
|---|---|---|---|---|
| [dd/mm] | [...] | [Cliente / Timeware / Externo] | [+N / 0] | [Resolvido / Em curso] |

## 7. Pontos de atenção, riscos e plano de ação

*[Para cada item relevante, use o formato Ponto → Risco → Ação. Mantenha só o que exige acompanhamento ou decisão; o registro completo de riscos fica no Jira (EST-GPC-002).]*

**[Título do ponto de atenção]** — 🔴 Crítico / 🟡 Médio / 🟢 Baixo
- **Ponto:** [o que está em jogo]
- **Risco:** [o que pode dar errado e o impacto]
- **Ação:** [o que será feito, por quem e até quando]

**[Título do próximo ponto, se houver]** — 🟡 Médio
- **Ponto:** [...]
- **Risco:** [...]
- **Ação:** [...]

## 8. Mudanças (change requests)

*[Change requests abertos, em análise ou aprovados no período. Mostrar o tempo em aberto evidencia agilidade na tratativa.]*

| ID | Descrição | Abertura | Dias em aberto | Status | Aceite final |
|---|---|---|---|---|---|
| [CR-XX] | [...] | [dd/mm] | [N] | [Pendente avaliação / Pendente aceite / Aprovada] | [dd/mm] |

> *Status possíveis:* Pendente avaliação → Pendente análise técnica → Pendente aceite → Aprovada. A aprovação ajusta a baseline conforme o fluxo de change request (TPL-GPR-006).

## 9. Decisões necessárias

*[Itens que dependem de decisão das partes interessadas para destravar o próximo período. Se não houver, registrar "Nenhuma decisão pendente".]*

| Decisão necessária | Responsável pela decisão | Prazo desejado |
|---|---|---|
| [...] | [cliente / PO / patrocinador] | [dd/mm/aaaa] |

---

## Cadência de reporte

*[Defina e mantenha visível a cadência acordada com o cliente — periodicidade, participantes e formato.]*

| Item | Definição |
|---|---|
| **Periodicidade** | [ex.: quinzenal / mensal] |
| **Participantes obrigatórios** | [papéis/partes] |
| **Participantes opcionais** | [papéis/partes] |
| **Canal** | [ex.: reunião + envio do report em PDF] |

---

## Histórico de revisões do template

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/09/2025 | Time de Melhoria Contínua | Versão inicial do template de relatório de acompanhamento |
| 2.0 | 11/06/2026 | Time de Melhoria Contínua | Reestruturação completa para padrão executivo, incorporando os melhores padrões praticados pela Timeware: painel RAG de 4 dimensões com convenção de cores (§1), resumo do período com indicadores em destaque (§2), entregas com foco em valor (§3), diário de bordo com impacto em dias (§6), riscos no formato Ponto→Risco→Ação (§7), tabela de change requests com dias em aberto (§8), seção de decisões necessárias (§9) e definição de cadência de reporte |
| 2.1 | 12/06/2026 | Time de Melhoria Contínua | Adição de §2.1 Registro de dailys internas: tabela de presenças por daily e resumo semanal de tópicos e decisões internas |
