# Documento de Design — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | PCP-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Responsáveis** | Cézar (Arquiteto) · Abraão Oliveira (GP / Tech Lead) |

---

## 1. Visão geral da solução

A solução é composta por dois componentes que operam de forma coordenada: o **CapturaServer**, serviço Windows que identifica processos pendentes de captura e os enfileira no RabbitMQ; e o **WorkerAndamentos**, conjunto de workers que lê a fila, executa as consultas nas fontes de dados e envia os resultados à API AndamentosProcessuais via webhook. O design atende aos requisitos de cobertura universal (RF-01), unificação de fila (RF-03, RF-12), fallback (RF-02, RF-07) e observabilidade (RF-09), operando com múltiplas instâncias concorrentes sem conflito (RNF-01).

## 2. Design técnico (arquitetura) — sempre aplicável

### 2.1. Arquitetura

A solução opera com múltiplas instâncias de workers concorrentes, usando o campo `CodigoFonteAPI` como mecanismo de roteamento por processo e a reserva de status na tabela `ProcessoCaptura` para evitar processamento duplicado.

- **CapturaServer (Serviço Windows):** consulta `ProcessoCaptura` por NUPs com `CodigoProcessoCapturaStatus = 1` (aguardando captura); reserva cada NUP setando status `2` (em processamento); publica o NUP na fila unificada do RabbitMQ, independente do tribunal.
- **WorkerAndamentos (Workers de Captura):** lê os itens da fila e verifica `CodigoFonteAPI`. Se nulo, tenta captura via DataJud/CNJ; se indicar fonte específica, direciona à fonte configurada. Gerencia o token Bearer CNJ via tabela `PonteAPI` (renovação automática compartilhada). Executa fallback para EPROC/ESAJ e, depois, para APIs parceiras por prioridade. Envia o resultado ao webhook da API AndamentosProcessuais e atualiza as tabelas de controle.

### 2.2. Modelo de dados (tabelas de controle)

| Tabela | Papel |
|---|---|
| `ProcessoCaptura` | Status global do processo e a fonte de captura (`CodigoFonteAPI`) |
| `ProcessoCapturaLogin` | Status de captura por instância processual, com campos de resposta, `Segredo` e observação de erro |
| `ProcessoCapturaMovimentacaoStatus` | Histórico de movimentações por instância, com `Ativo` e `DataUltimaAtualizacao` |
| `PonteAPI` | Token Bearer compartilhado da API CNJ e sua data de expiração |

### 2.3. Integrações

Detalhamento em ITP-AASPCNJ01-001. Resumo:

| Componente / Serviço | Tipo | Papel |
|---|---|---|
| API DataJud — CNJ | API REST pública | Fonte primária de captura |
| RabbitMQ | Message broker | Fila unificada de NUPs |
| API AndamentosProcessuais | API REST interna | Recebe dados via webhook e indexa no Elasticsearch |
| Elasticsearch | Motor de busca | Armazenamento dos andamentos para o front-end da AASP |
| EPROC/ESAJ (TJSP) | Portal judicial (crawler) | Fonte secundária via engine Puppeteer |
| APIs Parceiras (Solucionário, Botmax) | APIs REST pagas | Fontes terciárias (fallback final) |

### 2.4. Decisões de design

| Decisão | Alternativas consideradas | Escolha e justificativa | RAD |
|---|---|---|---|
| Fonte primária de captura | APIs privadas; crawler próprio universal; DataJud/CNJ | DataJud/CNJ — cobertura universal, custo R$ 0,01/processo, modelo padronizado | GDE-AASPCNJ01-001 (D02) |
| Fila de mensagens | Filas separadas por tribunal; fila única | Fila única — simplifica fluxo e escalonamento (RF-03) | GDE-AASPCNJ01-001 (D03) |
| Gestão do token Bearer CNJ | Token por worker; token compartilhado | Token compartilhado em `PonteAPI` — evita renovações paralelas e condições de corrida | GDE-AASPCNJ01-001 (D04) |
| Local da normalização do JSON CNJ | Na API; no worker | No worker — entrega `IModelElastic` pronto, simplificando a API | GDE-AASPCNJ01-001 (D05) |

### 2.5. Estratégia de fallback (três níveis)

| Nível | Fonte | Condição de ativação |
|---|---|---|
| 1 | API DataJud/CNJ | Primeira tentativa para NUPs com `CodigoFonteAPI` nulo |
| 2 | Engine EPROC/ESAJ | CNJ falhou e o tribunal está configurado para API AASP-EPROC |
| 3 | APIs Parceiras (por prioridade) | CNJ e EPROC/ESAJ falharam; menor `Prioridade` em `APIEmpresa` (`ApiAASP = 0`) |

## 3. Design de produto (UX/UI) — não aplicável

Projeto de back-end/worker, sem interface de usuário. Conforme ADAP-AASPCNJ01-001, o design de UX/UI não se aplica.

## 4. Rastreabilidade requisito → design

| Requisito (ID) | Elemento de design |
|---|---|
| RF-01, RF-05 | WorkerAndamentos — captura DataJud/CNJ + token `PonteAPI` |
| RF-02 | Engine EPROC/ESAJ (Puppeteer) — fallback nível 2 |
| RF-03, RF-12 | CapturaServer — enfileiramento unificado RabbitMQ |
| RF-04 | Rotina de desligamento de NUP nas APIs parceiras |
| RF-06, RF-09 | Tabelas `ProcessoCaptura` / `ProcessoCapturaLogin` |
| RF-07 | Fallback nível 3 (`APIEmpresa` por prioridade) |
| RF-10 | Campo `Segredo` em `ProcessoCapturaLogin` (por instância) |
| RF-11 | Webhook → API AndamentosProcessuais → Elasticsearch |

Matriz completa em RASTR-AASPCNJ01-001.

## 5. Avaliação do design (PCP 2)

| Item avaliado | Avaliador | Problema encontrado | Tratamento |
|---|---|---|---|
| Fluxo de captura CNJ e roteamento | Time de desenvolvimento | Campos do modelo CNJ com dados do TJSP hardcoded | Parametrização por tribunal (BUG-07) |
| Modelo de gravação no Elasticsearch | Raony Chagas | Alinhamento de campos CNJ com `IModelElastic` | Ajuste do mapeamento (Abr/2026) |
| Concorrência de token | Cézar / Raony Chagas | Risco de renovações paralelas | Token compartilhado em `PonteAPI` (D04) |

A decisão pela DataJud/CNJ como fonte primária foi formalizada na reunião de alinhamento técnico de 06/04/2026.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Documento de design consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026) — seção 4 (rotulada "OSW" na fonte) reclassificada como PCP. |
