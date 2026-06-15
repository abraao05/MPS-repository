# Plano de Verificação e Validação — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | VV-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | VV (evidência de projeto) |

---

## 1. Itens a verificar e validar (VV 1)

| Item | Método |
|---|---|
| Código da API AndamentosProcessuais e do CapturaServer | Code review (PR) + testes de fluxo |
| Webhook de indexação multi-fonte (EPROC/ESAJ e CNJ) | Teste de integração |
| Publicação na fila unificada WorkerAndamentos (RabbitMQ) | Teste de integração |
| Histórico de movimentações por instância (inativação/criação) | Teste de persistência |
| Verificação e desligamento do NUP nas APIs parceiras (Solucionário, Botmax) | Teste de integração |
| Tratamento de erro e segredo de justiça por instância | Teste de fluxo (cenários de falha) |
| Retrocompatibilidade do fluxo EPROC/ESAJ em produção | Teste de regressão |
| Requisitos (12 RF + 5 RNF) | Validação por amostragem com o representante AASP |

## 2. Métodos e critérios (VV 3)

- **Testes do desenvolvedor:** critérios de aceite por requisito (seção 3), validados pelos cenários CT-01 a CT-12 (seção 6), executados pelo time de desenvolvimento (Raony Chagas / Mateus Veloso).
- **Testes do QA (Caroline Sousa, a partir da Fase 4):** testes de fluxo (E2E), integração, persistência e regressão.
- **Testes de desempenho:** throughput e estabilidade do fluxo EPROC com múltiplos workers (Fases 1–2).
- **Ferramentas:** ClickUp para controle das atividades de teste (horas estimadas/realizadas); Azure DevOps para código e Pull Requests.
- **Ambientes:** homologação por amostragem, em ambiente compartilhado com AASP_CNJ, sem Elasticsearch dedicado — validação por repetição do mesmo processo na fila, sem impacto no índice de produção.

## 3. Critérios de aceite por requisito

Os critérios de aceite são os próprios requisitos (RF/RNF) do REQ-AASPAP01-001, validados pelos cenários de teste CT-01 a CT-12 (seção 6). Não há numeração de critério (CA) à parte — cada RF é aceito quando o(s) cenário(s) correspondente(s) é(são) aprovado(s).

| Requisito | Critério (condição de aceite) | Cenário(s) de validação |
|---|---|---|
| RF01 | CapturaServer publica na fila `WorkerAndamentos` com `SegmentoTribunal`, independente do tribunal | CT-02, CT-03 |
| RF02 | Webhook indexa dados de qualquer fonte (EPROC/ESAJ e CNJ), sem campos fixos por tribunal | CT-01, CT-04 |
| RF03 | `ProcessoCapturaMovimentacaoStatus` inativa o registro anterior e cria um novo | CT-05 |
| RF04 | `DataUltimaAtualizacao` atualizada no registro ativo mesmo sem novas movimentações | CT-06 |
| RF05 / RF06 | Após captura via CNJ, NUP verificado e desligado nas parceiras, com registro do retorno | CT-07 |
| RF07 / RF08 | Erro parcial: `ProcessoCaptura` mantém status 3 e só a instância afetada é marcada (com `Observacao`) | CT-09 |
| RF09 | NUP inválido pela parceira: `CodigoProcessoCapturaStatus=8` e `CodigoProcessoCapturaResposta=10` em todas as instâncias | CT-10 |
| RF10 | `CodigoFonteAPI` atualizado em `ProcessoCaptura` após cada captura | CT-08 (E2E) |
| RF11 | Campo `Segredo` atualizado por instância, sem impactar instâncias não restritas | CT-11 |
| RF12 | `RunUpdater` desmembrado para priorização de retorno por tipo de resultado | Validado na Fase 4 |
| RNF01 (retrocompatibilidade) | Fluxo EPROC/ESAJ em produção não impactado pelas refatorações | CT-12 |

## 4. Execução e registro (VV 4)

A execução dos testes por fase e o registro de defeitos estão consolidados em REL-VV-AASPAP01-001. Os testes foram organizados em três ciclos de execução (Fases 1–2, Fase 3 e Fase 4) e 12 cenários de teste (CT-01 a CT-12, 100% aprovados). Defeitos foram registrados e tratados ao longo das Fases 3 e 4 (5 defeitos catalogados, todos resolvidos antes da implantação).

## 5. Análise e comunicação dos resultados (VV 5)

Os resultados de validação foram analisados por Raony Chagas e por Cezar Hiraki Velazquez (GP / Tech Lead / Arquiteto), com apoio de Caroline Sousa (QA) na Fase 4, e comunicados nas reuniões de alinhamento (atas de 07/04/2026, 28/04/2026, 08/05/2026). Indicadores de qualidade (taxa de defeitos em homologação, defeitos escapados para produção) alimentam a Medição (ver MED-AASPAP01-001).

## 6. Cenários de teste (Gherkin) e evidências

```gherkin
Funcionalidade: Captura e indexação multi-fonte com tratamento por instância

  Cenário: Indexação multi-fonte via webhook (happy path)
    Dado dados de andamentos de uma fonte EPROC/ESAJ ou CNJ
    Quando o webhook de indexação recebe os dados
    Então eles são serializados e indexados no Elasticsearch
    E nenhum campo fixo por tribunal é exigido

  Cenário: Histórico de movimentações por inativação (happy path)
    Dado uma instância com registro de movimentação ativo
    Quando uma nova captura é processada
    Então o registro anterior é inativado e um novo registro é criado
    E a DataUltimaAtualizacao é atualizada mesmo sem novas movimentações

  Cenário: Erro parcial por instância (sad path)
    Dado um processo multi-instância pendente via CNJ
    Quando ocorre falha na captura de uma instância e sucesso nas demais
    Então ProcessoCaptura mantém status 3
    E apenas a instância afetada é marcada com a Observacao do erro

  Cenário: NUP inválido pela parceira (sad path)
    Dado um NUP cadastrado em uma API parceira
    Quando a parceira retorna NUP inválido
    Então todas as instâncias recebem CodigoProcessoCapturaStatus=8 e CodigoProcessoCapturaResposta=10

  Cenário: Segredo de justiça por instância (happy path)
    Dado um processo com uma instância em segredo e outra não
    Quando a captura é processada via CNJ ou EPROC/ESAJ
    Então o campo Segredo é atualizado apenas na instância restrita

  Cenário: Regressão do fluxo EPROC em produção
    Dado o fluxo EPROC/ESAJ em produção
    Quando as refatorações multi-fonte são aplicadas
    Então o fluxo EPROC não é impactado (retrocompatibilidade)
```

| CT | Fase | Tipo | Cenário | Situação |
|---|---|---|---|---|
| CT-01 | F1 | Happy | Dados EPROC enviados ao webhook → serialização e indexação no Elasticsearch | Aprovado |
| CT-02 | F2 | Happy | Processo pendente → CapturaServer publica na fila WorkerAndamentos com SegmentoTribunal | Aprovado |
| CT-03 | F2 | Integração | Processos EPROC pendentes → fluxo completo → captura e indexação por amostragem | Aprovado |
| CT-04 | F3 | Happy | Dados da API CNJ ao webhook → indexação multi-fonte OK | Aprovado |
| CT-05 | F3 | Happy | Instância com registro ativo → nova captura → registro anterior inativado e novo criado | Aprovado |
| CT-06 | F3 | Happy | Instância sem novas movimentações → DataUltimaAtualizacao atualizado | Aprovado |
| CT-07 | F3 | Integração | Processo capturado via CNJ e cadastrado em parceira → verificação e desligamento na parceira | Aprovado |
| CT-08 | F4 | E2E | Processo multi-instância pendente via CNJ → captura com sucesso em todas | Aprovado |
| CT-09 | F4 | Sad | Falha em uma instância e sucesso nas demais → status 3 e só a instância marcada | Aprovado |
| CT-10 | F4 | Sad | Parceira retorna NUP inválido → Status=8 e Resposta=10 em todas as instâncias | Aprovado |
| CT-11 | F4 | Happy | Uma instância em segredo e outra não → campo Segredo atualizado por instância | Aprovado |
| CT-12 | F4 | Regressão | Fluxo EPROC/ESAJ em produção → refatorações aplicadas → fluxo EPROC não impactado | Aprovado |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Plano de V&V consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais e do INTAKE-PROJETO_AASPAP01 v1.0. |
