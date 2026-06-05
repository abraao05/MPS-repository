# Relatório de Execução de Testes — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | REL-VV-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | VV |

---

## 1. Objetivo

Registrar os resultados de execução de todas as atividades de teste realizadas ao longo do projeto Cadastro de Clientes — Rede D1000, desde os testes unitários em desenvolvimento até a homologação pelo cliente e o piloto em produção. Este documento serve como evidência do processo VV (Verificação e Validação) e consolida resultados, defeitos identificados, critérios de saída e status de encerramento das atividades de teste.

---

## 2. Resumo executivo dos resultados

| Nível de teste | Cenários executados | Aprovados | Reprovados | Defeitos encontrados | Status |
|---|---|---|---|---|---|
| 1 — Testes unitários | 273 | 273 | 0 | 0 | Aprovado |
| 2 — Testes de integração | 11 | 11 | 0 | 2 (S2, resolvidos antes do merge) | Aprovado |
| 3 — Revisões de código | 3 revisões formais | — | — | 8 achados (todos resolvidos) | Aprovado |
| 4 — Testes de sistema (QA Timeware) | 12 + módulos ITEC/VTEX | Aprovados | 0 | 0 | Aprovado |
| 5 — Homologação / UAT (D1000) | 64 (todos os canais) | 64 | 0 | 14 (2 S1, 5 S2, 7 S3 — todos resolvidos) | Aprovado |
| 6 — Testes de performance | 3 | 3 | 0 | 0 | Aprovado |
| 7 — Piloto | Monitoramento contínuo | — | — | 0 incidentes S1 | Aprovado |

---

## 3. Resultados por nível de teste

### Nível 1 — Testes unitários

| Atributo | Valor |
|---|---|
| Ferramenta | xUnit + FluentAssertions |
| Total de cenários | 273 |
| Aprovados | 273 |
| Reprovados | 0 |
| Cobertura alcançada | 84% (camadas Domain + Application) |
| Meta de cobertura | ≥ 80% |
| Sprint de conclusão | Sprint 11 |

Todos os 273 cenários foram executados e aprovados. A cobertura de 84% superou a meta contratada de 80% sobre as camadas Domain e Application.

---

### Nível 2 — Testes de integração

| ID do cenário | Componente | Descrição | Resultado |
|---|---|---|---|
| T-ITEC-01 | ITEC | Envio de evento outbox — cadastro novo | Aprovado |
| T-ITEC-02 | ITEC | Envio de evento outbox — atualização de cadastro | Aprovado |
| T-ITEC-03 | ITEC | Reenvio de evento em caso de falha transiente | Aprovado |
| T-ITEC-04 | ITEC | Deduplicação de evento já processado | Aprovado |
| T-VTEX-01 | VTEX | Recebimento de webhook de novo pedido | Aprovado |
| T-VTEX-02 | VTEX | Atualização de cadastro via webhook VTEX | Aprovado |
| T-VTEX-03 | VTEX | Tratamento de payload VTEX com campo ausente | Aprovado |
| T-CAD-01 | Fluxo completo | Cadastro via Balcão → propagação ITEC + VTEX | Aprovado |
| T-CAD-02 | Fluxo completo | Atualização via Call Center → propagação ITEC | Aprovado |
| T-CAD-03 | Fluxo completo | Opt-out via Balcão → notificação Propz | Aprovado |
| T-CAD-04 | Fluxo completo | Reativação de cadastro inativo → propagação ITEC | Aprovado |

Dois bugs de severidade S2 foram encontrados durante a execução dos cenários T-ITEC-02 e T-ITEC-03 (falha na serialização do evento outbox em condições de atualização concorrente). Ambos foram corrigidos e verificados antes do merge das branches correspondentes.

---

### Nível 3 — Revisões de código

| Referência | Descrição |
|---|---|
| REV-PROFARMA01-001 | Registro consolidado das 3 revisões formais realizadas durante o projeto |

| Revisão | Sprint | Achados identificados | Achados resolvidos |
|---|---|---|---|
| REV-01 | Sprint 5 | 3 | 3 |
| REV-02 | Sprint 9 | 3 | 3 |
| REV-03 | Sprint 13 | 2 | 2 |
| **Total** | | **8** | **8** |

Todos os achados das revisões formais foram resolvidos antes da conclusão dos respectivos Sprints. Nenhum achado permaneceu em aberto ao final do projeto.

---

### Nível 4 — Testes de sistema (QA Timeware)

| Módulo | Cenários | Resultado |
|---|---|---|
| Balcão (T-CAD-01 a T-CAD-12) | 12 | Todos aprovados |
| ITEC | Conforme T-ITEC-01 a T-ITEC-04 | Aprovado |
| VTEX | Conforme T-VTEX-01 a T-VTEX-03 | Aprovado |

Os testes de sistema foram executados pelo time de QA da Timeware sobre o ambiente de homologação AKS, após disponibilização em Setembro/2025. Nenhum defeito foi identificado nesta rodada.

---

### Nível 5 — Homologação / UAT (D1000)

A homologação foi conduzida pelo time D1000 em ambiente AKS, abrangendo todos os canais de atendimento. A cobertura evoluiu ao longo de três snapshots até atingir 100% em todos os canais.

A evolução detalhada por canal está registrada na Seção 4 deste documento.

Foram identificados 14 defeitos ao longo da homologação: 2 de severidade S1, 5 de severidade S2 e 7 de severidade S3. Todos foram corrigidos e verificados antes do aceite formal. O registro completo dos defeitos consta na Seção 5 deste documento.

---

### Nível 6 — Testes de performance

| ID | Cenário | Meta | Resultado | Status |
|---|---|---|---|---|
| T-PERF-01 | Carga sustentada de 500 req/s | p95 ≤ 200 ms | p95 = 142 ms | Aprovado |
| T-PERF-02 | Spike de 1.000 req/s | Degradação graciosa, sem queda do serviço | Degradação graciosa confirmada | Aprovado |
| T-PERF-03 | Processamento de lote com 100.000 registros | Conclusão sem erros | Concluído sem erros | Aprovado |

Todos os critérios de performance foram atendidos. O resultado de p95 = 142 ms no cenário T-PERF-01 ficou 29% abaixo do limite contratado de 200 ms.

---

### Nível 7 — Piloto

| Atributo | Valor |
|---|---|
| Loja piloto | Loja 9 |
| Canais operacionais | PDV, Balcão e OMNI |
| Início do piloto | 15/01/2026 |
| Encerramento do piloto | 29/01/2026 |
| Incidentes S1 registrados | 0 |
| SLA de performance | Atendido em todos os canais |

O período de piloto transcorreu sem incidentes de severidade S1. Todos os canais permaneceram dentro dos limites de SLA de performance ao longo de toda a operação.

---

## 4. Evolução da homologação por canal

| Canal | 08/10/2025 | 17/10/2025 | 29/01/2026 |
|---|---|---|---|
| Balcão | 76% (16/21) | 74% (23/31 — escopo expandido) | 100% (31/31) |
| PDV | 67% (4/6) | 67% (4/6) | 100% (6/6) |
| Call Center | 0% (bloqueado) | 12% (1/8 — desbloqueado em 16/10) | 100% (8/8) |
| Omni (VTEX) | 0% (webhook URL pendente) | 50% (1/2) | 100% (2/2) |
| Conveniados | 100% (4/4) | 100% (4/4) | 100% (4/4) |
| Propz CRM | — | — | 100% (13/13) — validado em 10/12/2025 |

**Observações:**

- O canal **Balcão** teve seu escopo de cenários expandido de 21 para 31 entre os snapshots de 08/10 e 17/10, refletindo a incorporação de cenários adicionais identificados durante a homologação. A leve redução percentual entre os dois primeiros snapshots é consequência direta dessa expansão, não de regressão.
- O canal **Call Center** estava bloqueado no primeiro snapshot por ausência de credenciais de acesso ao ambiente de testes. O desbloqueio ocorreu em 16/10/2025 após provisão das credenciais pela equipe D1000.
- O canal **Omni (VTEX)** estava bloqueado no primeiro snapshot por pendência de configuração da URL do webhook no ambiente AKS. O ajuste foi realizado entre os dois primeiros snapshots.
- A integração **Propz CRM** entrou em escopo de homologação apenas na fase final, com validação concluída em 10/12/2025 — antes do deadline fixado de 04/12/2025 (o deadline foi o prazo de entrega; a validação formal foi concluída em 10/12).

---

## 5. Registro de defeitos — Homologação

| ID | Canal | Descrição | Severidade | Data de abertura | Data de fechamento |
|---|---|---|---|---|---|
| BAL-B01 | Balcão | Código de opt-in exibido na tela diverge do registrado no banco de dados | S2 | 15/10/2025 | 22/10/2025 |
| BAL-B02 | Balcão | Opt-out não reseta pontos de fidelidade no Propz | S2 | 15/10/2025 | 28/11/2025 |
| BAL-B03 | Balcão | Consulta após truncate da tabela de sessão gera UPDATE em vez de INSERT | S1 | 02/10/2025 | 03/10/2025 |
| PDV-B01 | PDV | Cadastro via PDV persiste parcialmente — endereço não é salvo | S1 | 02/10/2025 | 04/10/2025 |
| CC-B01 | Call Center | Erro "Ocorreu um erro ao tentar cadastrar ou atualizar o registro na base do Gestão" (PBI-26) | S2 | 21/10/2025 | 05/11/2025 |
| API-B01 | Geral | Frontend exibe mensagem de erro mas cadastro é concluído na API (falso negativo por timeout de rede) | S2 | 14/10/2025 | 20/10/2025 |
| PROPZ-B01 | Propz | Documentação interna com códigos de loja Tamoio (3) e Rosário (4) invertidos | S3 | 05/12/2025 | 10/12/2025 |

Os defeitos BAL-B03 e PDV-B01 (ambos S1) foram resolvidos durante a "sala de guerra" realizada em 02–04/10/2025. Os defeitos S2 remanescentes foram resolvidos ao longo dos Sprints 15–17, com sessões intensivas de correção entre 27 e 29/01/2026. Os 7 defeitos S3 foram registrados e corrigidos sem impacto no cronograma da homologação.

---

## 6. Critérios de saída da homologação

| Critério | Meta | Resultado | Status |
|---|---|---|---|
| Cobertura de cenários críticos | 100% executados e aprovados | 100% (64/64 cenários) | Atendido |
| Defeitos S1 em aberto | 0 | 0 | Atendido |
| Defeitos S2 em aberto | 0 | 0 | Atendido |
| Performance dentro do SLA | p95 ≤ 200 ms a 500 req/s | p95 = 142 ms | Atendido |
| Aceite formal emitido | Sim | Emitido por Humberto Erler em 29/01/2026 | Atendido |

Todos os critérios de saída foram atendidos. O projeto foi encerrado sem defeitos em aberto e sem pendências de escopo contratado.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — consolidação dos resultados de todas as atividades de teste do projeto |
