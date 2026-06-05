# Plano do Projeto

> **O que é este documento.** Documento gerencial que define o que o projeto vai entregar, com quais recursos, prazos, riscos e responsabilidades. É a referência (baseline) contra a qual o andamento é acompanhado no *Relatório de Acompanhamento*. O gestor o usa para entender e decidir; o time o usa para executar; serve como registro de aprendizagem do projeto.
>
> **Como usar.** Preencha os campos marcados `[preencher]`. Os campos marcados `‹padrão›` vêm do processo da organização e mudam pouco entre projetos. Seções marcadas como *baseline* são versionadas: quando mudam, gere uma nova versão deste documento e preserve a anterior — é assim que se enxerga o que foi combinado originalmente versus o que mudou.
>
> **Regra de ouro do preenchimento.** Nenhum campo fica em branco sem explicação. Se algo não se aplica a este projeto, escreva "não se aplica" e o porquê — em vez de deixar vazio. Um campo vazio é ambíguo (esqueceram? não existe?); um "não se aplica porque X" é informação.

---

## 0. Identificação e controle de versão

| Campo | Valor |
|---|---|
| Projeto | `[preencher]` |
| Código / chave no rastreador de tarefas | `[preencher]` |
| Gestor responsável | `[preencher]` |
| Data de abertura | `[preencher]` |
| Versão deste plano | `[preencher — ex.: v1]` |
| Data desta versão | `[preencher]` |
| O que mudou em relação à versão anterior | `[preencher — em branco na v1]` |

---

## 1. Escopo do trabalho

- **Objetivo de negócio.** Que problema este projeto resolve, e para quem. `[preencher]`
- **Escopo incluído.** O que será entregue. `[preencher]`
- **Escopo excluído.** O que explicitamente *não* será feito (tão importante quanto o incluído — evita mal-entendido). `[preencher]`
- **Critério de pronto do projeto.** Como saberemos que o projeto terminou. `[preencher]`
- **Controle de mudança de escopo.** Mudanças de escopo são registradas como ação no Relatório de Acompanhamento e, se aprovadas, geram nova versão deste plano.

---

## 2. Abordagem de condução do projeto

- **Abordagem-padrão da organização.** ‹padrão — descreva o método de trabalho: o ciclo de vida que todo projeto segue, da concepção à entrega, e a lista de tipos de tarefa que serão executadas.›
- **Adaptações para este projeto.** O que foi ajustado em relação ao padrão, e por quê. `[preencher]`

> A justificativa de adaptação é obrigatória mesmo quando a resposta é "nenhuma adaptação". Nesse caso, escreva: "Segue a abordagem-padrão integralmente, sem adaptações." Isso registra que a decisão foi consciente, não um esquecimento.

---

## 3. Estimativas

### 3.1 Método de estimativa

- **Dimensão (tamanho do trabalho).** ‹padrão — Story Points, estimados por história de usuário, via Planning Poker com a equipe.›
- **Esforço e duração.** Derivados da dimensão, usando a velocidade de referência da equipe (ver 3.4). O racional da derivação é registrado em 3.3.
- **Custo.** Não é estimado a partir do esforço. O custo é definido comercialmente e entra na seção 4 como dado. As estimativas desta seção servem para **prazo e alocação interna da equipe**.

> **Por que dimensão e esforço são coisas separadas.** Dimensão é o tamanho do trabalho (quão grande é a história). Esforço é quanto trabalho a equipe gasta para entregá-la (em horas/dias). Tempo gasto (horas) **não** é dimensão — é esforço. A regra do processo é: primeiro estima-se a dimensão, depois deriva-se o esforço a partir dela. Nunca o contrário.

### 3.2 Histórias de usuário e dimensão estimada

> Esta é a única seção do documento em granularidade de história. As histórias são **linhas** de uma tabela; não se cria um plano por história.

| ID da história | História (como… quero… para…) | Pontos (estimado) | Fase alocada | Status |
|---|---|---|---|---|
| `[preencher]` | | | | |

- **Total de pontos estimados do projeto (baseline):** `[soma da coluna Pontos]`
- Histórias podem ser adicionadas ao longo do planejamento. Cada adição relevante atualiza o total e gera nova versão deste plano. O total congelado aqui é o baseline contra o qual o realizado é medido no Relatório de Acompanhamento.

### 3.3 Esforço e duração agregados

| Métrica | Valor estimado | Como foi calculado (racional obrigatório) |
|---|---|---|
| Esforço total | `[preencher]` | total de pontos × esforço médio por ponto (ver 3.4) |
| Duração | `[preencher]` | esforço ÷ capacidade da equipe por período |
| Premissas assumidas | `[preencher]` | `[ex.: equipe dedicada, sem férias no período, etc.]` |

### 3.4 Velocidade e referência de esforço

- **Esforço médio por ponto usado nesta estimativa:** `[preencher]`
- **Velocidade da equipe usada (pontos por período):** `[preencher]`
- **Origem desta referência:** `[preencher]`

> **Estado da referência organizacional.** A referência consolidada de esforço/velocidade da organização está em construção. Enquanto não existir um histórico consolidado, registre aqui a base efetivamente usada (estimativa da própria equipe, dados de projetos anteriores se houver) e trate o número como **premissa revisável**, não como dado validado. Conforme os projetos acumulam dados reais (estimado vs. realizado), esta referência amadurece.

---

## 4. Orçamento, cronograma e marcos  *(baseline)*

- **Orçamento total (comercial, contratado):** `[preencher]` — é o valor de referência do projeto, definido comercialmente. O custo não é calculado a partir das estimativas de esforço.
- **Cronograma macro:** início `[preencher]` → término previsto `[preencher]`

### 4.1 Marcos

| Marco | Data prevista | Critério de conclusão (como sabemos que o marco foi atingido) |
|---|---|---|
| `[preencher]` | | |

### 4.2 Fases e alocação  *(tabela viva — o número de fases não é fixo)*

> As fases não são conhecidas de antemão: elas surgem conforme o planejamento detalha o trabalho. Esta tabela cresce à medida que novas fases são planejadas. O baseline de cada fase é registrado no momento em que a fase é planejada, não no início do projeto.

| Fase | Histórias incluídas | Esforço estimado | Início | Fim | Parcela do orçamento alocada |
|---|---|---|---|---|---|
| `[preencher]` | | | | | |

> **Sobre a parcela de orçamento por fase.** É uma alocação gerencial do custo total para fins de acompanhamento — não uma soma de estimativas de esforço. A soma das parcelas é igual ao orçamento total. Reestimativas de uma fase remanejam parcelas entre fases, sem alterar o total contratado, salvo mudança formal de escopo.

---

## 5. Recursos humanos

| Papel | Pessoa | Habilidades necessárias | Lacuna (a contratar / a treinar) |
|---|---|---|---|
| `[preencher]` | | | |

> Se faltar alguém com a habilidade necessária, registre na coluna de lacuna se a estratégia é contratar ou treinar. Lacuna não preenchida é risco — leve para a seção 9.

---

## 6. Recursos materiais e ambiente de trabalho

- **Ambientes.** `[preencher — ex.: desenvolvimento, homologação, produção]`
- **Ferramentas e infraestrutura.** `[preencher]`
- **Padrão organizacional de referência.** ‹padrão — descreva o ambiente-padrão de trabalho da organização do qual este projeto deriva seu ambiente.›

---

## 7. Estratégia de transição para operação e suporte

- **Como o produto entra em operação.** O processo de entrega/publicação. `[preencher]`
- **Quem opera e dá suporte após a entrega.** `[preencher]`
- **Tarefas e cronograma de transição.** `[preencher]`

> Esta seção responde "e depois que entregar, quem cuida?". Sem ela, o produto entra no ar sem dono de sustentação — uma das falhas mais comuns.

---

## 8. Partes interessadas

| Parte interessada | Papel / interesse no projeto | Como e quando é envolvida |
|---|---|---|
| `[preencher]` | | |

> Liste quem afeta ou é afetado pelo projeto (cliente, usuário, patrocinador, áreas internas). Para cada um, defina como e quando será envolvido — isso é o plano contra o qual o envolvimento é monitorado no Relatório.

---

## 9. Riscos e oportunidades

> **O registro de riscos é obrigatório — esta tabela nunca fica vazia.** Risco = incerteza que pode prejudicar o projeto. Oportunidade = incerteza que pode beneficiá-lo. Para cada risco, defina o tratamento (como reduzir a chance/impacto, ou o que fazer se acontecer).

| ID | Risco / Oportunidade | Probabilidade × Impacto | Tratamento (mitigação / contingência ou alavancagem) | Responsável | Situação |
|---|---|---|---|---|---|
| `[preencher]` | | | | | |

---

## 10. Viabilidade, integração e compromisso

### 10.1 Viabilidade
- As estimativas, recursos e restrições tornam o projeto viável? `[preencher]`
- Ajustes realizados para viabilizá-lo: `[preencher]`

### 10.2 Consistência do plano
- Confirmação de que escopo, estimativas, orçamento, cronograma, recursos e riscos são consistentes entre si (não se contradizem): `[preencher]`

### 10.3 Revisão e compromisso
- Plano revisado com os interessados em: `[data]`
- Dependências críticas identificadas e tratadas: `[preencher]`
- Compromisso formal com o plano obtido de: `[preencher — nomes e papéis de quem assumiu o compromisso]`

> "Compromisso obtido" significa que as pessoas-chave concordaram com o plano e se comprometeram a executá-lo/apoiá-lo. Registre quem e quando.
