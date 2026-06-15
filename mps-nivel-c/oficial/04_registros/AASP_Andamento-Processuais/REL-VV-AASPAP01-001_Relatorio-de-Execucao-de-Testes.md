# Relatório de Execução de Testes — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | REL-VV-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | VV (evidência de projeto) |
| **Referência** | VV-AASPAP01-001 (Plano de V&V) |

---

## 1. Objetivo

Registrar a execução dos testes do projeto e os defeitos identificados e tratados, em complemento ao Plano de V&V (VV-AASPAP01-001).

## 2. Ciclos e testes executados por fase

| Ciclo / Fase | Módulo | Tipo de teste | Descrição | Período |
|---|---|---|---|---|
| Fases 1–2 | Webhook EPROC / RabbitMQ | Integração e desempenho | Recebimento, serialização e indexação no Elasticsearch; publicação na fila WorkerAndamentos; homologação por amostragem | Jan–Mar/2026 |
| Fase 3 | Webhook multi-fonte / Movimentações / Parceiras | Integração e persistência | Dados CNJ; inativação/criação de registro; DataUltimaAtualizacao; desligamento nas parceiras | Abr–Mai/2026 |
| Fase 4 | Erros / Segredo / E2E / Regressão | Fluxo (E2E), regressão | Erro parcial; NUP inválido; segredo por instância; fluxo E2E; regressão EPROC | Mai–Jun/2026 |

Os cenários CT-01 a CT-12 (ver VV-AASPAP01-001 §6) foram executados ao longo destes ciclos, com **100% de aprovação**.

## 3. Defeitos registrados e tratados

| ID | Descrição | Fase | Resolução |
|---|---|---|---|
| BUG-01 | Defeito identificado na Fase 3 (webhook multi-fonte / movimentações) | Fase 3 | Parametrização dos campos do modelo |
| BUG-02 a BUG-05 | Defeitos identificados na Fase 4 (validação) | Fase 4 | Correção de merge, Observacao, ordem do desligamento e CodigoFonteAPI |

**Resumo:** 5 defeitos identificados e **100% resolvidos** (100% contidos antes da implantação; 0 defeitos escapados para produção).

## 4. Resultado dos cenários de teste (CT-01 a CT-12)

A validação foi conduzida por amostragem (repetição do mesmo processo na fila, em ambiente compartilhado com AASP_CNJ, sem impacto no índice de produção). Cenários conforme VV-AASPAP01-001 §6 e INTAKE-PROJETO_AASPAP01 v1.0.

| CT | Fase | Tipo | Cenário | Situação |
|---|---|---|---|---|
| CT-01 | F1 | Happy | Dados EPROC enviados ao webhook → serializa e indexa no Elasticsearch | Aprovado |
| CT-02 | F2 | Happy | CapturaServer publica na fila WorkerAndamentos com SegmentoTribunal | Aprovado |
| CT-03 | F2 | Integração | Fluxo completo de captura e indexação EPROC por amostragem | Aprovado |
| CT-04 | F3 | Happy | Dados da API CNJ ao webhook → indexação multi-fonte sem campos fixos do TJSP | Aprovado |
| CT-05 | F3 | Happy | Instância com registro ativo → inativação do anterior e criação de novo | Aprovado |
| CT-06 | F3 | Happy | Instância sem novas movimentações → DataUltimaAtualizacao atualizado | Aprovado |
| CT-07 | F3 | Integração | Processo capturado via CNJ e cadastrado em parceira → desligamento na parceira | Aprovado |
| CT-08 | F4 | E2E | Processo multi-instância via CNJ → captura com sucesso em todas | Aprovado |
| CT-09 | F4 | Sad | Falha em uma instância → ProcessoCaptura status 3 e só a instância marcada | Aprovado |
| CT-10 | F4 | Sad | Parceira retorna NUP inválido → Status=8 e Resposta=10 em todas as instâncias | Aprovado |
| CT-11 | F4 | Happy | Uma instância em segredo e outra não → campo Segredo atualizado por instância | Aprovado |
| CT-12 | F4 | Regressão | Refatorações aplicadas → fluxo EPROC/ESAJ em produção não impactado | Aprovado |

## 5. Conclusão

Os testes cobriram os fluxos de captura e indexação multi-fonte (EPROC/ESAJ e CNJ), publicação na fila unificada, histórico de movimentações por instância, desligamento nas APIs parceiras, tratamento de erro e segredo por instância, além da regressão do fluxo EPROC em produção (CT-12). Todos os 12 cenários de teste foram aprovados e os 5 defeitos identificados foram tratados antes da implantação. A ausência de ambiente de Elasticsearch dedicado e a baixa cobertura de testes automatizados/CI são as principais limitações da estratégia de teste (registradas em lições aprendidas).

---


## Evidências

- `andamentos_retry_webhook.jpeg` — Retry no envio do webhook (RNF04)

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Relatório de execução de testes consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais e do INTAKE-PROJETO_AASPAP01 v1.0. |
