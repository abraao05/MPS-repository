# Estratégia de Integração — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | ITP-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | ITP (evidência de projeto) |

---

## 1. Componentes a integrar

| Componente | Descrição |
|---|---|
| CapturaServer | Serviço Windows que identifica processos pendentes e os publica na fila unificada WorkerAndamentos (RabbitMQ) |
| API AndamentosProcessuais | API REST que recebe os dados via webhook multi-fonte, serializa para `IModelElastic` e indexa no Elasticsearch |
| WorkerAndamentos | Workers (projeto irmão AASP_CNJ) que consomem a fila, consultam as fontes (CNJ / EPROC/ESAJ) e enviam os resultados ao webhook |

## 2. Interfaces

| Interface | Entre | Tipo/contrato |
|---|---|---|
| Enfileiramento | CapturaServer ↔ RabbitMQ | Mensagem com NUP e `SegmentoTribunal` (fila unificada WorkerAndamentos) |
| Captura | WorkerAndamentos ↔ API DataJud/CNJ e portais EPROC/ESAJ | Consulta às fontes, roteada por `CodigoFonteAPI` |
| Desligamento parceiras | API AndamentosProcessuais ↔ APIs Solucionário/Botmax | REST, controladores específicos por parceira (verificação e exclusão de NUP) |
| Gravação / indexação | WorkerAndamentos ↔ API AndamentosProcessuais | Webhook multi-fonte → serialização `IModelElastic` → indexação no Elasticsearch |
| Persistência | API AndamentosProcessuais ↔ SQL Server | Atualização das tabelas de controle (`ProcessoCaptura`, `ProcessoCapturaLogin`, `ProcessoCapturaMovimentacaoStatus`) |

## 3. Estratégia e ordem de integração

A integração foi entregue de forma incremental, alinhada às fases do projeto:
1. **Webhook EPROC/ESAJ e fila RabbitMQ (Fases 1–2):** criação do webhook de indexação para o TJSP e migração do CapturaServer para a fila unificada WorkerAndamentos com `SegmentoTribunal`.
2. **Webhook multi-fonte e movimentações (Fase 3):** parametrização do webhook para qualquer fonte (incl. DataJud/CNJ), histórico de movimentações por instância e roteamento por `CodigoFonteAPI`.
3. **Desligamento das parceiras (Fase 3) e tratamento de erros/segredo (Fase 4):** verificação e desligamento do NUP nas APIs parceiras após captura via CNJ, e tratamento de erros e segredo de justiça por instância.

Em retorno vazio/aguardando ou em falha transitória no envio ao webhook, o worker aplica retry (RNF04) antes de registrar o erro nas tabelas de controle.

## 4. Ambiente de integração

Azure DevOps (controle de versão e pipeline; repositório `andamentosProcessuais`/AndamentosProcessuais); desenvolvimento local em .NET + SQL Server; homologação por amostragem em ambiente compartilhado com o projeto AASP_CNJ (sem Elasticsearch dedicado); produção na AASP com SQL Server, Elasticsearch e RabbitMQ. Ver GCO-AASPAP01-001.

## 5. Critérios de prontidão para integração

- Code review aprovado (mínimo 1 revisor além do autor) antes do merge em `develop`, conforme GitFlow.
- Testes de fluxo executados para o cenário integrado e testes de regressão por amostragem antes de cada merge na Fase 4.
- Tratamento de erro por instância implementado e registrado nas tabelas de controle.

## 6. Testes do produto integrado

O fluxo integrado (CapturaServer → RabbitMQ → WorkerAndamentos → webhook → Elasticsearch) foi validado por testes de integração, E2E e de regressão, cobrindo cenários de sucesso, erro parcial por instância, NUP inválido, segredo de justiça e não-regressão do fluxo EPROC/ESAJ (CT-01 a CT-12, 100% aprovados). O mecanismo de retry no envio ao webhook foi implementado na Fase 4 para aumentar a resiliência. Detalhes na aba V&V — Testes da GEST-AASPAP01.

## 7. Entrega e material de apoio

A entrega em produção segue o rito de GMUD: montagem de pacote de publicação e scripts DDL versionados no Azure DevOps, validação em homologação e agendamento com a Infraestrutura. Tags de baseline: `v220` (legado / ponto de partida), `v230` (Fases 1–2), `v240`/`v241` (Fases 3–4). Escopo adicional formalizado em CR-AASPAP01-001 (homologação EPROC/ESAJ) e CR-AASPAP01-002 (campos `Observacao`/`Segredo`/`CodigoFonteAPI` e tratamentos de erro).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Estratégia de integração consolidada a partir do Registro de Projeto AASP_AndamentosProcessuais, do INTAKE-PROJETO_AASPAP01 e do GCO-AASPAP01-001. |
