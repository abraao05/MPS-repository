# Matriz de Rastreabilidade — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | RASTR-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |

---

## Matriz

Rastreabilidade bidirecional (REQ 4): de cada requisito ao design, à fonte de captura/componente e ao critério de aceite que o verifica.

| Necessidade | Requisito (ID) | História (Jira) | Item de design (PCP) | Componente / fonte | Critério de aceite (VV) | Situação |
|---|---|---|---|---|---|---|
| Custo e cobertura | RF-01 | US-04 | Captura DataJud/CNJ (fallback nível 1) | WorkerAndamentos + `PonteAPI` | CA01, CA04 | Atendido |
| Estabilidade de captura TJSP | RF-02 | US-01 / US-03 | Engine EPROC/ESAJ (fallback nível 2) | WorkerAndamentos (Puppeteer) | CA01, CA05 | Atendido |
| Arquitetura unificada | RF-03 | US-09 | Leitura unificada da fila | WorkerAndamentos | CA01 | Atendido |
| Custo de parceiras | RF-04 | US-10 | Rotina de desligamento de NUP | WorkerAndamentos | CA06 | Atendido |
| Operacional | RF-05 | US-05 | Token Bearer compartilhado | `PonteAPI` | CA01 | Atendido |
| Rastreabilidade da fonte | RF-06 | US-06 | Campo `CodigoFonteAPI` | `ProcessoCaptura` | CA01 | Atendido |
| Resiliência | RF-07 | US-11 | Fallback por prioridade (nível 3) | `APIEmpresa` | CA05 | Atendido |
| Tratamento de retornos | RF-08 | US-12 | Tratamento de NUP inválido/vazio/erro | WorkerAndamentos | CA05 | Atendido |
| Observabilidade | RF-09 | US-14 | Campo `Observacao` por instância | `ProcessoCapturaLogin` | CA05 | Atendido |
| Segredo de justiça | RF-10 | US-13 | Campo `Segredo` por instância | `ProcessoCapturaLogin` | CA07 | Atendido |
| Entrega ao Elasticsearch | RF-11 | US-07 | Webhook → indexação | API AndamentosProcessuais | CA04 | Atendido |
| Enfileiramento unificado | RF-12 | US-08 | Enfileiramento no RabbitMQ | CapturaServer | CA01 | Atendido |

## Cobertura

- **Requisitos sem cobertura de teste/critério:** nenhum — todos os RFs têm critério de aceite associado (CA01–CA07).
- **Itens desenvolvidos sem requisito associado:** nenhum identificado.
- Os requisitos não funcionais (RNF-01 a RNF-06) são verificados de forma transversal: RNF-01/02 nos testes de desempenho e de recuperação de fila; RNF-03/04 no design das tabelas de controle e do roteamento; RNF-05 na gestão centralizada do token; RNF-06 nos indicadores de custo (MED-AASPCNJ01-001).
- **Histórias de usuário (US-01 a US-20)** derivadas dos requisitos e seu mapeamento a épicos, sprints e tarefas: ver GEST-AASPCNJ01-001 (abas Backlog e Tarefas).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Matriz de rastreabilidade consolidada a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
