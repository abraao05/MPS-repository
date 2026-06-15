# Documento de Design — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | PCP-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez (Arquiteto / Tech Lead) |
| **Processo MPS-SW** | PCP (evidência de projeto) |

---

## 1. Visão geral da solução

A solução legada AndamentosProcessuais (.NET) é refatorada de forma cirúrgica em dois componentes coordenados: o **CapturaServer**, serviço Windows que passa a publicar os processos pendentes na fila unificada WorkerAndamentos (RabbitMQ) com o `SegmentoTribunal`; e a **API AndamentosProcessuais**, que recebe os dados capturados via webhook multi-fonte, serializa para `IModelElastic`, indexa no Elasticsearch e atualiza as tabelas de controle. O design atende à unificação de fila (RF01), ao suporte multi-fonte (RF02), ao histórico de movimentações por instância (RF03, RF04), ao desligamento nas parceiras (RF05, RF06), ao tratamento de erros e segredo por instância (RF07–RF11) e à priorização de retorno (RF12), preservando a retrocompatibilidade do fluxo existente (RNF01).

## 2. Design técnico (arquitetura) — sempre aplicável

### 2.1. Arquitetura

A refatoração evolui a solução legada em camadas (API .NET + CapturaServer + workers) sem reescrita. O roteamento por fonte é feito pelo campo `CodigoFonteAPI`, e o histórico de movimentações é mantido por inativação de registros (nunca por sobrescrita).

- **CapturaServer (Serviço Windows):** identifica processos pendentes de captura e publica na fila unificada **WorkerAndamentos** do RabbitMQ, com NUP e `SegmentoTribunal`, independente do tribunal de origem. Migração da fila anterior (`EprocTjsp`) para a fila única (decisão D02).
- **API AndamentosProcessuais (webhook multi-fonte):** recebe os dados de qualquer fonte (EPROC/ESAJ, DataJud/CNJ) sem campos fixos por tribunal (decisão D03), serializa para `IModelElastic` e indexa no Elasticsearch. Atualiza `ProcessoCaptura` (incl. `CodigoFonteAPI`), gerencia o histórico em `ProcessoCapturaMovimentacaoStatus` e o controle por instância em `ProcessoCapturaLogin` (`Observacao`, `Segredo`). Após captura via CNJ, aciona a verificação e o desligamento do NUP nas APIs parceiras pela camada da API (decisão D05), via controladores específicos por parceira (decisão D06). O `RunUpdater` foi desmembrado para priorizar os retornos por tipo de resultado (RF12).

### 2.2. Modelo de dados (tabelas de controle)

| Tabela | Papel |
|---|---|
| `ProcessoCaptura` | Status global do processo e a fonte de captura (`CodigoFonteAPI`); recebe status 3 em erro parcial |
| `ProcessoCapturaLogin` | Status de captura por instância, com `Observacao` (erro), `Segredo` e códigos de status/resposta |
| `ProcessoCapturaMovimentacaoStatus` | Histórico de movimentações por instância, com `Ativo` e `DataUltimaAtualizacao` (inativação + novo registro) |

### 2.3. Integrações

Detalhamento em ITP-AASPAP01-001. Resumo:

| Componente / Serviço | Tipo | Papel |
|---|---|---|
| RabbitMQ | Message broker | Fila unificada WorkerAndamentos (NUP + `SegmentoTribunal`) |
| API DataJud — CNJ | API REST | Fonte de captura universal (consumida via WorkerAndamentos) |
| EPROC/ESAJ (TJSP) | Portal judicial (crawler) | Fonte de captura do TJSP |
| Elasticsearch | Motor de busca | Armazenamento dos andamentos para o front-end da AASP |
| SQL Server | Banco de dados | Persistência das tabelas de controle |
| APIs Parceiras (Solucionário, Botmax) | APIs REST | Verificação e desligamento de NUP após captura via CNJ |

### 2.4. Decisões de design

| Decisão | Alternativas consideradas | Escolha e justificativa | RAD |
|---|---|---|---|
| Primeiro entregável (D01, Dez/2025) | Alterar fluxo legado; webhook dedicado | Webhook de indexação específico para EPROC/ESAJ — viabiliza captura nativa TJSP sem regressão | GDE-AASPAP01-001 (D01) |
| Ponto de entrada do pipeline (D02, Fev/2026) | Fila por tribunal; fila única | Migrar CapturaServer para a fila única WorkerAndamentos — unifica o pipeline | GDE-AASPAP01-001 (D02) |
| Webhook multi-fonte (D03, Abr/2026) | Novo webhook; parametrizar o existente | Parametrizar o webhook — evita duplicação e reduz manutenção | GDE-AASPAP01-001 (D03) |
| Histórico de movimentações (D04, Abr/2026) | Update no registro; inativação | Inativação de registro (não update) — preserva histórico por instância | GDE-AASPAP01-001 (D04) |
| Onde tratar parceiras (D05, Abr/2026) | No worker; na API | Verificação/desligamento na camada da API — worker agnóstico; controladores já existem | GDE-AASPAP01-001 (D05) |
| Parceiras heterogêneas (D06, Mai/2026) | Controlador genérico; por parceira | Controladores específicos por parceira (Solucionário, Botmax) com interface comum | GDE-AASPAP01-001 (D06) |
| Escopo do segredo (D07, Mai/2026) | Por processo; por instância | Campo `Segredo` por instância — um processo pode ser segredo só em uma instância | GDE-AASPAP01-001 (D07) |

## 3. Design de produto (UX/UI) — não aplicável

Projeto de back-end/refatoração, sem interface de usuário. Conforme INTAKE/registro do projeto, o design de UX/UI não se aplica.

## 4. Rastreabilidade requisito → design

| Requisito (ID) | Elemento de design |
|---|---|
| RF01 | CapturaServer — enfileiramento unificado RabbitMQ (fila WorkerAndamentos) |
| RF02 | Webhook multi-fonte parametrizado (sem campos fixos por tribunal) |
| RF03, RF04 | Histórico por inativação em `ProcessoCapturaMovimentacaoStatus` |
| RF05, RF06 | Verificação/desligamento nas parceiras (controladores por parceira) |
| RF07, RF08, RF09 | Campo `Observacao` e códigos de status/resposta em `ProcessoCapturaLogin` |
| RF10 | Campo `CodigoFonteAPI` em `ProcessoCaptura` |
| RF11 | Campo `Segredo` por instância em `ProcessoCapturaLogin` |
| RF12 | Desmembramento do `RunUpdater` (priorização por tipo de retorno) |

Matriz completa em RASTR-AASPAP01-001.

## 5. Avaliação do design (PCP 2)

| Item avaliado | Avaliador | Problema encontrado | Tratamento |
|---|---|---|---|
| Webhook multi-fonte com campos do TJSP | Time de desenvolvimento | Campos do modelo com dados do TJSP fixos | Parametrização dos campos do modelo (BUG-01) |
| Alinhamento de campos CNJ com `IModelElastic` | Raony Chagas | Mapeamento dos campos CNJ ao modelo Elastic | Ajuste do mapeamento (Abr/2026) |
| Histórico de movimentações | Cezar Hiraki Velazquez / Raony Chagas | Risco de perda de histórico em update | Modelo por inativação de registro (D04) |

A decisão pela parametrização do webhook e pelo histórico por inativação foi formalizada nas reuniões de alinhamento de 07/04/2026 e 08/05/2026.

---


## Evidências

- `andamentos_arquitetura.svg` — Arquitetura da solução refatorada
- `andamentos_ApisParceiras.jpg` — Integração com APIs parceiras (Solucionário/Botmax)
- `andamentos_historicoPreservado.jpeg` — Histórico de movimentações preservado por inativação
- `andamentos_historicoPreservado1.jpg` — Histórico preservado — detalhe 1
- `andamentos_historicoPreservado2.jpg` — Histórico preservado — detalhe 2

## Histórico de revisões

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Documento de design consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais, do INTAKE-PROJETO_AASPAP01 e do GDE-AASPAP01-001. |
