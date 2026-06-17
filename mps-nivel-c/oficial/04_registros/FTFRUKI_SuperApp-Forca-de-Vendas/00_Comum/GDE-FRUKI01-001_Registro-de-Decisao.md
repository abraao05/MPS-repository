# Registro de Análise de Decisão — SuperApp Fruki · Tratamento de Dados de API no Front-End

| Campo | Valor |
|---|---|
| **Documento** | GDE-FRUKI01-001 |
| **Projeto / contexto** | SuperApp Fruki — Força de Vendas (Pacote 1 + Pacote Final 24) |
| **Data** | 05/06/2026 |
| **Responsável pela decisão** | Abraão Oliveira |

---

## Decisão 1: Tratamento de dados da API no front-end vs. solicitação de correção ao time Fruki

### 1. Problema / decisão a tomar

Durante o Pacote 1 (Jul/2025), identificou-se que a API `/acompanhamentoMetasFamilias` retornava latência de ~3,10s para 5 pedidos e registros duplicados de famílias de produtos. A mesma situação se repetiu no Pacote Final 24 com a API de Pedidos Não Alocados, que retornava dados em formato não padronizado. A decisão é: solicitar correção ao time de TI da Fruki ou tratar os problemas no front-end React Native.

### 2. Gatilho

Decisão técnica com impacto direto no prazo e na experiência do usuário; envolve definição de responsabilidade entre Timeware (front-end) e Fruki (back-end/API) — decisão com impacto no escopo e na arquitetura.

### 3. Alternativas consideradas

| # | Alternativa | Descrição |
|---|---|---|
| A | Solicitar correção das APIs ao time Fruki (Jardel/Renan) | Abrir requisição formal de correção da latência, remoção de duplicatas e normalização do formato da resposta; aguardar correção antes de prosseguir |
| B | Tratar os problemas de dados no front-end React Native | Implementar deduplicação, normalização de formato e loading state (skeleton screen) diretamente no `metasService.ts` e `pedidosNaoAlocadosService.ts`; continuar o desenvolvimento em paralelo |

### 4. Critérios de avaliação

| Critério | Peso |
|---|---|
| Impacto no prazo de entrega | Alto |
| Capacidade de execução pela equipe | Médio |
| Risco de retrabalho futuro | Médio |
| Dependência do cliente (Fruki TI) | Alto |

### 5. Avaliação (matriz de decisão)

| Critério | Peso | Alt. A (solicitar correção) | Alt. B (tratar no front-end) |
|---|---|---|---|
| Impacto no prazo | Alto | Negativo — risco de bloqueio por 1–2 semanas aguardando correção do time Fruki | Positivo — desenvolvimento continua sem dependência |
| Capacidade de execução | Médio | Negativo — fora do controle da Timeware | Positivo — equipe Timeware tem autonomia total |
| Risco de retrabalho futuro | Médio | Positivo (se corrigido) — dados normalizados na origem | Neutro — solução de contorno funcional; pode exigir ajuste se API mudar |
| Dependência do cliente | Alto | Negativo — disponibilidade do time Fruki é incerta no sprint atual | Positivo — elimina dependência |
| **Total ponderado** | | **Desfavorável** | **Favorável** |

### 6. Decisão e justificativa

**Alternativa B — Tratar os problemas de dados no front-end.**

O time de TI da Fruki (Jardel/Renan) não tinha disponibilidade para corrigir as APIs no prazo das sprints em andamento. A implementação de deduplicação, normalização e loading state no front-end é tecnicamente simples para a equipe Timeware e elimina a dependência de um pré-requisito externo. A solução é encapsulada nos serviços (`metasService.ts` e `pedidosNaoAlocadosService.ts`) e pode ser removida futuramente se a API for corrigida sem impacto na interface.

### 7. Riscos associados à decisão

| Risco | Resposta |
|---|---|
| A API mudar o formato no futuro, invalidando a normalização | O código de normalização é centralizado nos services; manutenção futura isolada |
| A latência piorar e o loading state não ser suficiente | Monitorar em campo; paginação ou cache local como contingência se necessário |

### 8. Premissas (para revisão futura)

- O time de TI da Fruki não tem capacidade de corrigir as APIs no prazo do projeto
- A normalização no front-end não afeta a corretude dos dados apresentados ao usuário
- As APIs não mudarão de formato durante o projeto ativo

---

## Decisão 2: Renomeação de "Caixa Preta" para "Regra de Ouro" (Pacote Final 24)

### 1. Problema / decisão a tomar

O módulo de composição detalhada da remuneração variável era denominado internamente pela Fruki como "Caixa Preta". Durante a revisão de protótipos com Cecília Ribeiro em 22/10/2025, surgiu a discussão sobre a nomenclatura adequada para a interface do usuário.

### 2. Gatilho

Decisão de UX/nomenclatura com impacto na experiência do usuário e na comunicação interna da Fruki — envolveu alinhamento com o cliente.

### 3. Alternativas consideradas

| # | Alternativa | Descrição |
|---|---|---|
| A | Manter "Caixa Preta" conforme denominação interna Fruki | Usar o mesmo nome que o time usa internamente para o sistema |
| B | Renomear para "Regra de Ouro" | Adotar nomenclatura mais positiva e compreensível para os vendedores em campo |

### 4. Critérios de avaliação

| Critério | Peso |
|---|---|
| Experiência do usuário (vendedor em campo) | Alto |
| Alinhamento com o cliente (Fruki) | Alto |
| Esforço de implementação | Baixo |

### 5. Avaliação

| Critério | Alt. A ("Caixa Preta") | Alt. B ("Regra de Ouro") |
|---|---|---|
| Experiência do usuário | Neutro — nome conhecido internamente | Positivo — nome mais motivador para o vendedor |
| Alinhamento com cliente | Neutro | Positivo — sugestão aceita por Cecília Ribeiro em 22/10/2025 |
| Esforço | Nenhum | Mínimo — ajuste de texto nas telas e documentação |

### 6. Decisão e justificativa

**Alternativa B — "Regra de Ouro".**

Cecília Ribeiro aprovou a nomenclatura "Regra de Ouro" por ser mais positiva e motivadora para os representantes comerciais. O esforço de implementação é mínimo. Decisão tomada em 22/10/2025 durante revisão de protótipos.

### 7. Riscos associados à decisão

| Risco | Resposta |
|---|---|
| Comunicação interna da Fruki continuar usando "Caixa Preta" causando confusão | Leandro Lottermann e Cecília comunicarão a mudança de nomenclatura ao time |

### 8. Premissas

- Cecília Ribeiro tem autoridade para aprovar a mudança de nomenclatura na interface
- O time de vendas da Fruki aceitará a nova nomenclatura sem dificuldades

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — duas decisões registradas: tratamento front-end de dados de API e renomeação "Caixa Preta" → "Regra de Ouro" |
