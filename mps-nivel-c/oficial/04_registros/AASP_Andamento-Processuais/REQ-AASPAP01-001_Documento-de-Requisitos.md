# Documento de Requisitos — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | REQ-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez (GP / Tech Lead / Arquiteto) |
| **Processo MPS-SW** | REQ (evidência de projeto) |

---

## 1. Contexto e objetivo

A AASP oferece a seus associados uma plataforma centralizada de monitoramento de processos judiciais. A Timeware opera a solução legada de captura de andamentos (API AndamentosProcessuais + CapturaServer), em .NET, com cerca de 20 anos de operação. Com a adoção do novo modelo de captura via DataJud/CNJ e WorkerAndamentos (projeto irmão AASP_CNJ), a solução existente precisa ser refatorada de forma cirúrgica para suportar fila unificada, webhook multi-fonte, histórico de movimentações por instância, desligamento dos processos nas APIs parceiras e controle de erros e segredo de justiça por instância — tudo sem interromper a operação em produção. O objetivo deste documento é registrar os requisitos funcionais (RF01–RF12) e não funcionais (RNF01–RNF05) que delimitam essa refatoração.

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| Associados da AASP | Acompanhamento confiável e atualizado dos andamentos em todos os tribunais, sem regressão durante a transição |
| Marcos Correa Fernandez Turnes (Sponsor / PO — AASP) | Refatoração controlada da solução legada, suporte ao novo modelo CNJ e aceite por fase |
| Operação Timeware | Rastreabilidade de estados, parametrização para novas fontes e preservação do histórico de movimentações |

## 3. Visão geral da solução

Refatoração delimitada de dois componentes em produção: o **CapturaServer** (serviço Windows que passa a publicar na fila unificada WorkerAndamentos no RabbitMQ, com `SegmentoTribunal`) e a **API AndamentosProcessuais** (webhook de indexação parametrizado para múltiplas fontes, controle de movimentações por instância, verificação/desligamento nas APIs parceiras e tratamento de erros e segredo por instância). Projeto de back-end/refatoração, **sem interface de usuário** (UX/UI não aplicável). O restante da solução AndamentosProcessuais permanece inalterado.

## 4. Requisitos funcionais

| ID | Origem | Requisito | Prioridade |
|---|---|---|---|
| RF01 | Arquitetura unificada | CapturaServer publica mensagens na fila WorkerAndamentos (RabbitMQ), independente do tribunal de origem | Alta |
| RF02 | Suporte multi-fonte | Webhook de indexação aceita dados de qualquer fonte de captura, sem campos fixos por tribunal específico | Alta |
| RF03 | Histórico de movimentações | Histórico de movimentações por instância em `ProcessoCapturaMovimentacaoStatus`, com inativação do registro anterior e criação de novo | Alta |
| RF04 | Atualização incremental | Atualizar `DataUltimaAtualizacao` no registro ativo mesmo sem novas movimentações | Média |
| RF05 | Custo de parceiras | Após captura via CNJ, verificar as APIs parceiras e acionar a exclusão do NUP se estiver cadastrado | Alta |
| RF06 | Rastreabilidade do desligamento | Registrar o resultado do desligamento nas tabelas de cadastro de cada parceira | Alta |
| RF07 | Observabilidade | Campo `Observacao` em `ProcessoCapturaLogin` registra o detalhe do erro por instância | Alta |
| RF08 | Tratamento de erro parcial | Erro parcial: `ProcessoCaptura` recebe status 3 e apenas a instância afetada é marcada individualmente | Alta |
| RF09 | Tratamento de retornos | NUP inválido pela parceira: `CodigoProcessoCapturaStatus`=8 e `CodigoProcessoCapturaResposta`=10 em todas as instâncias | Alta |
| RF10 | Rastreabilidade da fonte | Atualizar `CodigoFonteAPI` em `ProcessoCaptura` após cada captura | Alta |
| RF11 | Segredo de justiça | Atualizar o campo `Segredo` em `ProcessoCapturaLogin` por instância (via CNJ ou EPROC/ESAJ) | Alta |
| RF12 | Priorização operacional | `RunUpdater` desmembrado para executar priorizações de retorno por tipo de resultado | Média |

## 5. Requisitos não funcionais

| ID | Categoria | Requisito | Critério |
|---|---|---|---|
| RNF01 | Retrocompatibilidade | Refatorações não interrompem o fluxo de captura existente durante a transição | Fluxo EPROC/ESAJ em produção sem regressão |
| RNF02 | Rastreabilidade | Todo estado de processamento registrado nas tabelas de controle | Data, status e observação de erro quando aplicável |
| RNF03 | Manutenibilidade | Webhook parametrizável para novas fontes | Sem alteração na camada de serialização (`IModelElastic`) |
| RNF04 | Confiabilidade | Retry no envio do webhook | Não-perda de dados em falhas transitórias |
| RNF05 | Integridade | Histórico de movimentações preservado integralmente | Sem sobrescrita de registros anteriores |

## 6. Restrições e premissas

**Restrições:**
- Alterações cirúrgicas: o restante da solução AndamentosProcessuais permanece inalterado, sem reescrita do sistema legado.
- Sem migração de dados no Elasticsearch e sem alteração estrutural do `IModelElastic`.
- Homologação por amostragem, em ambiente compartilhado com o projeto AASP_CNJ; sem Elasticsearch dedicado para testes.

**Premissas:**
- A solução legada (.NET) e as tabelas de controle em SQL Server permanecem disponíveis durante a refatoração.
- A API DataJud/CNJ é consumida via WorkerAndamentos (projeto irmão AASP_CNJ).
- As APIs parceiras (Solucionário, Botmax) expõem endpoints de verificação e exclusão de NUP.

## 7. Validação dos requisitos

| Requisito/conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| Fluxo EPROC/ESAJ e fila RabbitMQ (RF01) | Homologação por amostragem em ambiente compartilhado | Jan–Mai/2026 | Validado (CT-01 a CT-03) |
| Webhook multi-fonte e movimentações (RF02–RF06, RF10) | Validação de fluxo da Fase 3 | Abr–Mai/2026 | Validado (CT-04 a CT-07) |
| Tratamento de erros e segredo (RF07–RF09, RF11, RF12) | Testes E2E e de regressão da Fase 4 | Mai–Jun/2026 | Validado (CT-08 a CT-12) |

## 8. Confirmação de entendimento e compromisso

| Envolvido | Papel | Confirmação | Data |
|---|---|---|---|
| Marcos Correa Fernandez Turnes | AASP (Sponsor / PO) | Aceite das entregas das Fases 1–2 | Mar/2026 |
| Marcos Correa Fernandez Turnes | AASP (Sponsor / PO) | Aceite das entregas das Fases 3–4 | Jun/2026 |
| Time de desenvolvimento | Timeware | Compromisso técnico assumido no alinhamento do fluxo CNJ | 07/04/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Documento de requisitos consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais (REG-AASPAP01-001) e da Planilha de Gestão (aba Backlog). |
