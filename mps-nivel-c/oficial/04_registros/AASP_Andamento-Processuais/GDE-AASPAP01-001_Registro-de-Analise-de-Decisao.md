# Registro de Análise de Decisão (RAD) — AASP_AndamentosProcessuais · Modelo de histórico de movimentações

| Campo | Valor |
|---|---|
| **Documento** | GDE-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GDE (evidência de projeto) |
| **Responsável pela decisão** | Cezar Hiraki Velazquez (com o time de desenvolvimento) |

---

## 1. Problema / decisão a tomar

Definir como registrar o histórico de movimentações processuais por instância no novo modelo de captura, sem perda de dados e preservando a retrocompatibilidade com a solução legada `AndamentosProcessuais` (em produção há ~20 anos). Esta decisão (D04) é a de maior impacto sobre a integridade dos dados na refatoração.

## 2. Gatilho

Mudança estrutural no modelo de persistência de uma solução legada em produção, com risco de regressão e de perda de histórico — atinge os gatilhos do PRO-GDE-001 (alto impacto sobre dado em produção e sobre a arquitetura de persistência).

## 3. Alternativas consideradas

| # | Alternativa | Descrição |
|---|---|---|
| A | Update no registro existente | Atualizar o registro de movimentação ativo a cada nova captura |
| B | Histórico por inativação | Inativar o registro anterior e criar um novo a cada captura, preservando o histórico por instância |

## 4. Critérios de avaliação

| Critério | Peso |
|---|---|
| Preservação do histórico (integridade) | 3 |
| Retrocompatibilidade com o fluxo legado | 3 |
| Rastreabilidade por instância | 2 |
| Manutenibilidade | 2 |

## 5. Avaliação (matriz de decisão)

Escala 1–3 por critério (3 = melhor atende). Pontuação ponderada pelo peso.

| Critério | Peso | Alt. A (update) | Alt. B (inativação) |
|---|---|---|---|
| Preservação do histórico | 3 | 1 | 3 |
| Retrocompatibilidade | 3 | 2 | 3 |
| Rastreabilidade por instância | 2 | 2 | 3 |
| Manutenibilidade | 2 | 2 | 2 |
| **Total ponderado** | | **17** | **28** |

## 6. Decisão e justificativa

Escolhida a **Alternativa B — histórico por inativação de registro**. A nova captura inativa o registro anterior em `ProcessoCapturaMovimentacaoStatus` e cria um novo, sem sobrescrever dados. Preserva integralmente o histórico por instância (RNF05), elimina o risco de perda de movimentações na transição (R-03) e mantém a rastreabilidade exigida (RNF02). O modelo apenas adiciona registros, nunca os altera destrutivamente.

## 7. Riscos associados à decisão

| Risco | Resposta |
|---|---|
| Crescimento da tabela de movimentações | Aceito — volume controlado; registros inativos preservados para auditoria |
| Regressão no fluxo EPROC em produção | Mitigar com testes de regressão por amostragem (CT-12) e refatoração cirúrgica |

## 8. Premissas (para revisão futura)

- O fluxo de captura legado permanece operante durante toda a transição (RNF01).
- O `IModelElastic` não sofre alteração estrutural; o webhook é parametrizado, não reescrito.

---

## Anexo — Registro consolidado de decisões do projeto

Decisões formais registradas no levantamento do projeto (INTAKE-PROJETO_AASPAP01, BLOCO 7).

| # | Data | Contexto / Problema | Alternativas | Decisão | Justificativa |
|---|---|---|---|---|---|
| D01 | Dez/2025 | Primeiro entregável da solução | Alterar fluxo legado vs. webhook dedicado | Criar webhook de indexação específico para EPROC/ESAJ | Viabilizar captura via engine nativo TJSP sem regressão no fluxo legado |
| D02 | Fev/2026 | Ponto de entrada do pipeline | Manter fila por tribunal vs. fila única | Migrar o CapturaServer da fila `EprocTjsp` para a fila `WorkerAndamentos` | Unificar o pipeline e preparar para múltiplas fontes |
| D03 | Abr/2026 | Webhook com campos fixos do TJSP | Novo webhook vs. parametrizar o existente | Parametrizar o webhook para suporte multi-fonte | Evitar duplicação de lógica e reduzir manutenção futura |
| D04 | Abr/2026 | Histórico de movimentações | Update no registro vs. inativação | Histórico por inativação de registro (não por update) | Preservar o histórico por instância sem perda de dados (RAD detalhado acima) |
| D05 | Abr/2026 | Onde tratar as APIs parceiras | No worker vs. na API | Verificação/desligamento das parceiras na camada da API | Worker permanece agnóstico; controladores já existem na API |
| D06 | Mai/2026 | Parceiras heterogêneas | Controlador genérico vs. por parceira | Controladores específicos por parceira (Solucionário, Botmax) | Estruturas/endpoints diferentes; interface comum facilita novas parceiras |
| D07 | Mai/2026 | Escopo do segredo de justiça | Segredo por processo vs. por instância | Campo `Segredo` por instância em `ProcessoCapturaLogin` | Um processo pode estar em segredo em uma instância e não em outra |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | RAD do modelo de histórico de movimentações (D04) + registro consolidado das decisões D01–D07, a partir do INTAKE-PROJETO_AASPAP01 v1.0 (14/06/2026) e do Registro de Projeto REG-AASPAP01-001. |
