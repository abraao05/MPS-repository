# Change Request — [preencher: TÍTULO DA MUDANÇA]

> **O que é este documento.** Registro formal de uma solicitação de mudança que afeta o escopo, prazo ou custo do projeto. O CR é o mecanismo que mantém a baseline do Plano do Projeto íntegra: toda mudança passa por análise de impacto e decisão documentada antes de ser executada. Mudança executada sem CR é desvio de escopo — mesmo que pequena.
>
> **Como usar.** Abra um CR assim que identificar qualquer mudança que afete o comprometimento original. Preencha a análise de impacto antes de solicitar a decisão — o decisor precisa saber o que está aprovando. Após a decisão, registre o reflexo no projeto (backlog, plano, rastreabilidade).
>
> **Regra de ouro.** O CR não é burocracia — é o mecanismo que mantém o plano honesto. Se uma mudança foi acordada oralmente e não passou por CR, o escopo real já divergiu do planejado sem registro. A regra de quando formalizar é simples: se o impacto seria difícil de reverter, formaliza.

---

## Identificação

| Campo | Valor |
|---|---|
| Documento | `[preencher — ex.: CR-PROJ-001]` |
| Projeto | `[preencher — nome do projeto]` |
| Título da mudança | `[preencher — descrição curta da mudança solicitada]` |
| Solicitante | `[preencher — nome / papel]` |
| Data da solicitação | `[preencher — dd/mm/aaaa]` |
| Gerente de Projeto | `[preencher]` |

---

## 1. Descrição da mudança

`[preencher — descreva o que se quer mudar, com clareza suficiente para quem não estava na conversa entender. Inclua: o que está no plano atual, o que se propõe mudar e qual o estado desejado após a mudança.]`

---

## 2. Justificativa

`[preencher — por que esta mudança está sendo solicitada? Qual o problema, oportunidade ou restrição que a motiva? A justificativa precisa ser suficientemente forte para sustentar a análise de impacto que vem a seguir.]`

---

## 3. Análise de impacto

| Dimensão | Impacto | Detalhamento |
|---|---|---|
| Escopo | `[Alto / Médio / Baixo / Nenhum]` | `[preencher — o que muda no escopo incluído ou excluído]` |
| Prazo | `[Alto / Médio / Baixo / Nenhum]` | `[preencher — quantos dias/semanas de impacto no cronograma, se houver]` |
| Esforço / custo | `[Alto / Médio / Baixo / Nenhum]` | `[preencher — horas adicionais estimadas; impacto no orçamento, se houver]` |
| Riscos introduzidos | `[Alto / Médio / Baixo / Nenhum]` | `[preencher — novos riscos que esta mudança introduz ao projeto]` |

---

## 4. Tipo de tratamento proposto

> Marque o tipo de tratamento recomendado pelo Gerente de Projeto:

- [ ] **Aditivo** — a mudança amplia o escopo e gera custo adicional a ser contratado
- [ ] **Crédito** — a mudança reduz o escopo e gera crédito (reembolso ou abatimento futuro)
- [ ] **Troca de prioridade** — o item entra no escopo em substituição a outro de igual esforço (escopo total mantido, sem impacto financeiro)
- [ ] **Parqueamento** — o item é formalmente removido do escopo atual e registrado para versão futura (sem impacto financeiro imediato)

`[preencher — descreva brevemente a lógica do tratamento proposto]`

---

## 5. Decisão

| Campo | Valor |
|---|---|
| Decisão | `[Aprovado / Rejeitado / Aprovado com condições]` |
| Responsável pela decisão | `[preencher — nome e papel]` |
| Data da decisão | `[preencher — dd/mm/aaaa]` |
| Referência à ata ou registro | `[preencher — ex.: ATA-PROJ-XXX ou e-mail de decisão]` |
| Condições (se houver) | `[preencher — ou "Nenhuma"]` |

---

## 6. Reflexo no projeto

> Preencha após a decisão ser aprovada. Registra como a mudança se reflete nos artefatos do projeto.

- **Backlog / rastreador de tarefas:** `[preencher — quais issues foram criadas, fechadas ou movidas? Referencie os IDs]`
- **Rastreabilidade:** `[preencher — quais requisitos foram adicionados, removidos ou alterados?]`
- **Baseline do Plano do Projeto:** `[preencher — nova versão do Plano gerada? Qual? Ou o impacto é coberto por este CR sem alterar o Plano?]`
- **Outros artefatos afetados:** `[preencher — ou "Nenhum"]`
