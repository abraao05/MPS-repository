# Plano de Verificação e Validação — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | VV-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |

---

## 1. Itens a verificar e validar (VV 1)

| Item | Método |
|---|---|
| Código dos workers e do CapturaServer | Code review (PR) + testes de fluxo |
| Fluxo de captura CNJ (consulta, autenticação, JSON, webhook) | Teste de integração / E2E |
| Estratégia de fallback (CNJ → EPROC/ESAJ → parceiras) | Teste de fluxo (cenários de falha) |
| Persistência de movimentações | Teste de persistência |
| Desligamento de NUP nas APIs parceiras | Teste de integração |
| Requisitos | Validação por amostragem com o cliente |

## 2. Métodos e critérios (VV 3)

- **Testes do desenvolvedor:** critérios de aceite CA01–CA07 (seção 3).
- **Testes do QA (a partir da Fase 5):** testes de fluxo (E2E), integração e persistência.
- **Testes de desempenho:** throughput e estabilidade do fluxo EPROC com múltiplos workers.
- **Ferramentas:** coleções Postman (API CNJ); ClickUp para controle das atividades de teste.
- **Ambientes:** homologação por amostragem, sem Elasticsearch dedicado — validação por repetição do mesmo processo na fila, sem impacto no índice de produção (ver ADAP-AASPCNJ01-001).

## 3. Critérios de aceite

| # | Critério | Evidência esperada |
|---|---|---|
| CA01 | Registro de captura com status correto | `ProcessoCaptura` com `CodigoProcessoCapturaStatus = 3` e `Observacao` preenchido |
| CA02 | Registro por instância com sucesso | `ProcessoCapturaLogin` com `CodigoProcessoCapturaResposta = 1` (OK) por instância |
| CA03 | Atualização das movimentações | `ProcessoCapturaMovimentacaoStatus` com `DataUltimaAtualizacao` e `Ativo = 1` |
| CA04 | Indexação no Elasticsearch | Documento indexado com capa, partes, advogados e andamentos por instância (`IModelElastic`) |
| CA05 | Tratamento de erro por instância | Em erro parcial, só a instância afetada com status 8; `ProcessoCaptura` mantém status 3 |
| CA06 | Desligamento de API parceira | Processo removido das parceiras após captura via CNJ, com log de desligamento |
| CA07 | Segredo de justiça por instância | Campo `Segredo` atualizado por instância, sem impactar instâncias não restritas |

## 4. Execução e registro (VV 4)

A execução dos testes por fase e o registro de defeitos estão consolidados em REL-VV-AASPCNJ01-001. Defeitos foram registrados e tratados ao longo das Fases 3 a 5 (9 defeitos catalogados, todos resolvidos).

## 5. Análise e comunicação dos resultados (VV 5)

Os resultados de validação foram analisados por Raony Chagas e por Abraão Oliveira e comunicados nas reuniões de alinhamento. Indicadores de qualidade (estabilidade da fila, erros por instância) alimentam a Medição (ver MED-AASPCNJ01-001).

## 6. Cenários de teste (Gherkin) e evidências

```gherkin
Funcionalidade: Captura de andamentos via fonte primária e fallback

  Cenário: Captura bem-sucedida via DataJud/CNJ (happy path)
    Dado um NUP com CodigoFonteAPI nulo na fila RabbitMQ
    Quando o worker consulta a API DataJud/CNJ com token Bearer válido
    Então os andamentos são normalizados e enviados ao webhook
    E ProcessoCaptura recebe status 3 (Capturado)
    E o processo é desligado das APIs parceiras com log de desligamento

  Cenário: Fallback após falha da CNJ (sad path)
    Dado um NUP do TJSP cuja consulta à CNJ não retornou resultado
    Quando o worker identifica o tribunal configurado para API AASP-EPROC
    Então a captura é tentada via engine EPROC/ESAJ
    E, persistindo a falha, é acionada a API parceira de menor Prioridade

  Cenário: Erro parcial por instância (sad path)
    Dado um processo com múltiplas instâncias
    Quando ocorre erro na captura de uma instância específica
    Então apenas a instância afetada recebe status 8 em ProcessoCapturaLogin
    E ProcessoCaptura mantém status 3
```

| Cenário | Tipo | Evidência | Situação |
|---|---|---|---|
| Captura via CNJ | Happy | Validação por amostragem (Fase 5) | Aprovado |
| Fallback CNJ→EPROC→parceira | Sad | Teste de fluxo (Fase 5) | Aprovado |
| Erro parcial por instância | Sad | Teste de fluxo (Fase 5) | Aprovado |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Plano de V&V consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
