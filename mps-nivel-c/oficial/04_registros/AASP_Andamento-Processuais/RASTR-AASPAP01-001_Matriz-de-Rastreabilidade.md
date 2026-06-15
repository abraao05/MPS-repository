# Matriz de Rastreabilidade — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | RASTR-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | REQ (evidência de projeto) |

---

## Matriz

Rastreabilidade bidirecional: de cada requisito à tarefa de implementação, ao item de design (PCP), à fonte/componente e ao cenário de teste (CT) que o verifica.

| Requisito (ID) | Tarefa (GEST) | Item de design (PCP) | Componente / tabela | Cenário de teste (CT) | Situação |
|---|---|---|---|---|---|
| RF01 | T-01..T-04 | Enfileiramento unificado RabbitMQ | CapturaServer / fila WorkerAndamentos | CT-02, CT-03 | Atendido |
| RF02 | T-08, T-09 | Webhook multi-fonte | API AndamentosProcessuais | CT-04 | Atendido |
| RF03 | T-10 | Histórico por inativação de registro | `ProcessoCapturaMovimentacaoStatus` | CT-05 | Atendido |
| RF04 | T-10 | Atualização de `DataUltimaAtualizacao` | `ProcessoCapturaMovimentacaoStatus` | CT-06 | Atendido |
| RF05 | T-11 | Verificação/desligamento nas parceiras (camada API) | Controladores Solucionário/Botmax | CT-07 | Atendido |
| RF06 | T-11 | Log de desligamento por parceira | Tabelas de cadastro das parceiras | CT-07 | Atendido |
| RF07 | T-14 | Campo `Observacao` por instância | `ProcessoCapturaLogin` | CT-09 | Atendido |
| RF08 | T-16, T-17 | Tratamento de erro parcial (status 3) | `ProcessoCaptura` / `ProcessoCapturaLogin` | CT-09 | Atendido |
| RF09 | T-16, T-17 | Tratamento de NUP inválido (status 8 / resposta 10) | `ProcessoCapturaLogin` | CT-10 | Atendido |
| RF10 | T-12 | Campo `CodigoFonteAPI` | `ProcessoCaptura` | CT-08 | Atendido |
| RF11 | T-14 | Campo `Segredo` por instância | `ProcessoCapturaLogin` | CT-11 | Atendido |
| RF12 | T-13 | Desmembramento do `RunUpdater` (priorização) | API AndamentosProcessuais | CT-08 | Atendido |

## Cobertura

- **Requisitos sem cobertura de teste:** nenhum — todos os RF01–RF12 têm cenário de teste (CT-01 a CT-12) associado, todos 100% aprovados (ver V&V — Testes da GEST-AASPAP01).
- **Itens desenvolvidos sem requisito associado:** as tarefas T-05 (homologação) e T-16/T-17 (testes e correção de bugs) referem-se a V&V; T-06, T-07 e T-18 são atividades de comunicação/entrega — nenhuma feature de produto sem requisito de origem.
- **Requisitos não funcionais (RNF01–RNF05)** verificados de forma transversal: RNF01 nos testes de regressão EPROC/ESAJ (CT-12); RNF02 no design das tabelas de controle; RNF03 no webhook parametrizável (CT-04); RNF04 no mecanismo de retry (T-15); RNF05 no histórico por inativação (CT-05).
- **Defeitos:** 5 bugs identificados em homologação (BUG-01 na Fase 3; BUG-02 a BUG-05 na Fase 4), 100% contidos antes da implantação; 0 defeitos escapados para produção.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Matriz de rastreabilidade consolidada a partir do Registro de Projeto AASP_AndamentosProcessuais e da Planilha de Gestão (abas Backlog, Tarefas e V&V — Testes). |
