# Relatório de Execução de Testes — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | REL-VV-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Referência** | VV-AASPCNJ01-001 (Plano de V&V) |

---

## 1. Objetivo

Registrar a execução dos testes do projeto e os defeitos identificados e tratados, em complemento ao Plano de V&V (VV-AASPCNJ01-001).

## 2. Testes executados por fase

| Fase | Tipo de teste | Descrição |
|---|---|---|
| Fase 1 | Análise de desempenho | Estudo do comportamento do captcha Cloudflare nos portais do TJSP e estratégias de contorno |
| Fase 2 | Teste de desempenho | Throughput e estabilidade do fluxo EPROC com múltiplos workers simultâneos |
| Fase 2 | Teste de integração | Endpoint de publicação no RabbitMQ e webhook de indexação no Elasticsearch |
| Fase 3 | Regressão / bug | Reteste das falhas: timeout após captcha, nullabilidade em `ProcessoCapturaLogin`, `DataUltimaAtualizacao` |
| Fase 4 | Teste de integração | Fluxo completo de captura CNJ (consulta, autenticação, JSON, webhook) |
| Fase 4 | Teste de integração | Desligamento de NUP nas APIs parceiras após captura via CNJ |
| Fase 5 | Teste de fluxo (E2E) | Captura CNJ: sucesso, fallback e erro parcial por instância |
| Fase 5 | Teste de persistência | Persistência das movimentações e atualização da coluna de exclusão |
| Fase 5 | Teste de integração | Indexação e exclusão de processos nas APIs parceiras |

## 3. Defeitos registrados e tratados

| ID | Descrição | Fase | Resolução |
|---|---|---|---|
| BUG-01 | Timeout após o captcha Cloudflare no EPROC | Fase 3 | Ajuste no tempo de espera e no tratamento de resposta após autenticação |
| BUG-02 | `ProcessoCapturaLogin` retornando null em certos processos | Fase 3 | Correção da condição de nulidade e criação do registro quando ausente |
| BUG-03 | Nullabilidade em campos opcionais | Fase 3 | Verificações de nulo antes de operações de gravação |
| BUG-04 | `DataUltimaAtualizacao` não atualizado corretamente | Fase 3 | Correção da lógica de atualização na rotina de movimentações |
| BUG-05 | Fila RabbitMQ acumulando 137 mil itens não processados | Fase 4 | Correção na publicação com tratamento de exceção e logging; atualização do pacote AWS |
| BUG-06 | Falha na publicação no RabbitMQ sem registro de erro | Fase 4 | `try/catch` na publicação com log detalhado |
| BUG-07 | Campos do modelo CNJ com dados do TJSP hardcoded | Fase 4 | Remoção dos valores fixos e parametrização por tribunal |
| BUG-08 | Erro de referências na solução AndamentosProcessuais após merge | Fase 5 | Correção das referências de projeto e recompilação |
| BUG-09 | Falha no fluxo de indexação e exclusão nas APIs parceiras | Fase 5 | Correção na ordem de operações e validação do fluxo completo |

**Resumo:** 9 defeitos identificados e **100% resolvidos** antes da validação final do fluxo.

## 4. Resultado dos critérios de aceite

A validação foi conduzida por amostragem (repetição do mesmo processo na fila, sem impacto no índice de produção), conforme ADAP-AASPCNJ01-001.

| # | Critério | Resultado |
|---|---|---|
| CA01 | Status de captura correto em `ProcessoCaptura` | Validado por amostragem |
| CA02 | Registro de sucesso por instância | Validado por amostragem |
| CA03 | Atualização das movimentações | Validado (teste de persistência, Fase 5) |
| CA04 | Indexação no Elasticsearch (`IModelElastic`) | Validado por amostragem |
| CA05 | Tratamento de erro por instância | Validado (teste de fluxo, Fase 5) |
| CA06 | Desligamento de API parceira | Validado (teste de integração, Fase 5) |
| CA07 | Segredo de justiça por instância | Validado (teste de fluxo, Fase 5) |

## 5. Conclusão

Os testes cobriram os fluxos de captura (CNJ, EPROC/ESAJ e parceiras), fallback, persistência e indexação. Todos os defeitos identificados foram tratados e os critérios de aceite foram validados por amostragem. A ausência de ambiente de Elasticsearch dedicado é a principal limitação da estratégia de teste (ver ADAP-AASPCNJ01-001).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Relatório de execução de testes consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
