# Plano de Verificação e Validação — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | VV-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.1 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | VV (evidência de projeto) |

---

## 1. Objetivo

Definir a estratégia e as atividades de Verificação e Validação (V&V) do sistema de Cadastro de Clientes — Rede D1000, garantindo que o produto atende aos requisitos especificados (verificação) e às necessidades do negócio D1000 (validação).

---

## 2. Escopo do plano

Este plano cobre as atividades de V&V aplicadas ao longo dos sprints do projeto, desde os testes unitários durante o desenvolvimento até os testes de homologação e o aceite formal com a D1000.

---

## 3. Estratégia de verificação e validação

### 3.1 Níveis de teste

| Nível | Tipo | Responsável | Ferramenta | Critério de entrada | Critério de saída |
|---|---|---|---|---|---|
| 1 | Testes unitários | Time Timeware (Dev + QA) | xUnit (.NET) / FluentAssertions | Código da feature concluído | Cobertura ≥ 80% nas camadas Domain e Application; todos os testes passando |
| 2 | Testes de integração | Time Timeware (Dev + QA) | xUnit + TestContainers (PostgreSQL local) | Testes unitários passando | Todos os fluxos críticos de integração (outbox, endpoints) executados sem falha |
| 3 | Revisão de código (peer review) | Tech Lead + Dev revisor | Azure DevOps Pull Requests | PR aberto com testes passando no CI | PR aprovado por pelo menos 1 revisor (Tech Lead ou Dev Senior) |
| 4 | Testes de sistema | QA Timeware (Lucas Batista) | Manual + scripts automatizados | Feature em ambiente de homologação | Todos os critérios de aceite do sprint cobertos |
| 5 | Testes de homologação (UAT) | QA D1000 (Julielle Santos) + QA Timeware | Roteiros de teste aprovados pela D1000 | Ambiente de homologação estável; roteiros aprovados | Aceite formal da D1000 por sprint ou fase |
| 6 | Testes de piloto (produção restrita) | D1000 + Timeware | Operação real — loja 9 | Aceite de homologação; GMUD aprovado | Operação estável por período definido; sem incidentes críticos |

### 3.2 Critérios de qualidade do projeto

| Critério | Meta | Base |
|---|---|---|
| Cenários de teste unitário | ≥ 273 | REQ RNF-11 |
| Cobertura de testes unitários | ≥ 80% (Domain + Application) | REQ RNF-11 |
| Testes de homologação passando | 100% dos cenários críticos | Acordo com D1000 |
| Defeitos críticos em produção | 0 no piloto antes de rollout | Meta do projeto |
| SLA de resposta (p95) — GET /clientes/{cpf} | ≤ 200ms | REQ RNF-07 |
| SLA de resposta (p95) — Call Center | ≤ 500ms | REQ RNF-13 |

---

## 4. Atividades de verificação por sprint

### 4.1 Verificação contínua (todos os sprints)

- **Revisão de requisitos:** antes do início de cada sprint, o Tech Lead e o QA verificam se os critérios de aceite das histórias de usuário são testáveis e completos
- **Revisão de código:** todo PR passa por revisão antes do merge; mudanças arquiteturais requerem aprovação do Armando Junior (D1000)
- **Pipeline CI:** a cada push, o pipeline Azure DevOps executa: build → testes unitários → análise estática; o merge no branch principal só é permitido com pipeline verde

### 4.2 Verificação por fase

| Fase | Sprint(s) | Foco da verificação |
|---|---|---|
| Fase 1 — Fundação | Sprints 1–3 | Endpoints de CRUD básico, outbox pattern, health check |
| Fase 2 — Integrações principais | Sprints 4–7 | ITEC outbox funcional, VTEX, Call Center, início Propz |
| Fase 3 — Integrações satélites | Sprints 8–10 | PBM, BlueSoft, CloseUp, worker LGPD |
| Fase 4 — Qualidade e carga | Sprints 11–13 | Carga inicial 7M CPFs, performance, cobertura de testes |
| Fase 5 — Homologação | Sprints 14–17 | UAT com D1000, roteiros formais, correções |
| Fase 6 — Piloto e encerramento | Sprints 18–19 | Loja 9 (PDV, Balcão, OMNI), rollout readiness |

---

## 5. Roteiros de teste por módulo

### 5.1 Módulo de cadastro (RF-01 a RF-10, RF-18)

| ID Teste | Cenário | Tipo | Resultado esperado |
|---|---|---|---|
| T-CAD-01 | Cadastro de cliente com todos os campos obrigatórios preenchidos e CPF válido | Funcional | HTTP 201; cliente persistido; evento outbox criado |
| T-CAD-02 | Cadastro com CPF já existente na base | Funcional | HTTP 409; mensagem de erro descritiva |
| T-CAD-03 | Cadastro com CPF inválido (dígitos verificadores incorretos) | Funcional | HTTP 422; validação rejeitada antes da persistência |
| T-CAD-04 | Consulta de cliente por CPF existente | Funcional | HTTP 200; todos os dados cadastrais retornados |
| T-CAD-05 | Consulta de CPF inexistente | Funcional | HTTP 404 |
| T-CAD-06 | Atualização parcial de telefone (PATCH) | Funcional | HTTP 200; dado atualizado; auditoria registrada |
| T-CAD-07 | Inativação lógica com motivo (LGPD) | Funcional | HTTP 200; ativo = false; evento outbox criado |
| T-CAD-08 | Tentativa de cadastro de cliente inativo (mesmo CPF) | Funcional | HTTP 409 com indicação de inativação |
| T-CAD-09 | Reativação de cliente inativo | Funcional | HTTP 200; ativo = true; auditoria registrada |
| T-CAD-10 | Busca por nome parcial com paginação | Funcional | HTTP 200; lista paginada com metadados |
| T-CAD-11 | HEAD /clientes/{cpf} com CPF existente | Funcional | HTTP 200 sem body |
| T-CAD-12 | GET /health com todos os componentes operacionais | Funcional | HTTP 200; status de todos componentes = healthy |

### 5.2 Módulo de integração — ITEC Outbox (RF-11)

| ID Teste | Cenário | Tipo | Resultado esperado |
|---|---|---|---|
| T-ITEC-01 | Cadastro gera evento ClienteCriado no outbox | Integração | Registro criado em outbox_eventos; processado_em = null |
| T-ITEC-02 | Worker processa evento pendente e chama ITEC com sucesso | Integração | processado_em preenchido; tentativas = 1 |
| T-ITEC-03 | Worker tenta processar evento com ITEC indisponível | Integração | tentativas incrementa; backoff exponencial; evento não perdido |
| T-ITEC-04 | Evento processado não é reprocessado pelo worker | Integração | Worker ignora eventos com processado_em preenchido |

### 5.3 Integração VTEX (RF-12)

| ID Teste | Cenário | Tipo | Resultado esperado |
|---|---|---|---|
| T-VTEX-01 | POST /clientes/vtex com payload VTEX válido | Integração | HTTP 201; mapeamento correto de campos VTEX → domínio |
| T-VTEX-02 | GET /clientes/vtex/{cpf} retorna perfil no schema VTEX | Integração | HTTP 200; resposta compatível com CustomerProfile VTEX |
| T-VTEX-03 | Autenticação com API Key inválida | Segurança | HTTP 401 |

### 5.4 Performance (RNF-06, RNF-07)

| ID Teste | Cenário | Tipo | Meta |
|---|---|---|---|
| T-PERF-01 | Carga de 500 req/s no GET /clientes/{cpf} por 5 minutos | Carga | Zero erros; latência p95 ≤ 200ms |
| T-PERF-02 | Spike de 1000 req/s por 30 segundos | Stress | Degradação graciosa; sem crash; retorno à normalidade |
| T-PERF-03 | Carga batch de 100k registros via /clientes/lote | Volume | Processamento concluído sem timeout; zero perdas |

---

## 6. Gestão de defeitos

| Severidade | Definição | SLA de correção | Impacto no aceite |
|---|---|---|---|
| Crítico (S1) | Funcionalidade principal inoperante; perda de dados | 24 horas | Bloqueia aceite de sprint / fase |
| Alto (S2) | Funcionalidade principal com comportamento incorreto, mas com workaround | 3 dias úteis | Bloqueia aceite de sprint se não resolvido |
| Médio (S3) | Funcionalidade secundária com comportamento incorreto | Próximo sprint | Não bloqueia aceite; registrado no backlog |
| Baixo (S4) | Melhorias cosméticas, textos, formatação | A critério | Não bloqueia aceite |

Todos os defeitos encontrados em testes de homologação são registrados no Jira pelo QA D1000 (Julielle Santos) e atribuídos ao time Timeware para triagem e correção.

---

## 7. Validação formal (UAT)

### 7.1 Processo de aceite de sprint

1. QA Timeware (Lucas Batista) conclui os testes de sistema e certifica que os critérios de aceite das histórias foram atendidos
2. Time Timeware apresenta a entrega na Sprint Review (presença de Armando Junior, Helena Moreira e Julielle Santos da D1000)
3. D1000 executa testes de homologação com roteiros aprovados em ambiente dedicado
4. Defeitos identificados são classificados por severidade e corrigidos conforme SLA
5. Após resolução de todos os defeitos S1 e S2, Helena Moreira (D1000) emite aceite formal do sprint por e-mail

### 7.2 Aceite do piloto (loja 9)

- Período de operação piloto: mínimo 2 semanas em condições reais antes do rollout
- Critérios de saída do piloto: zero incidentes S1 no período; todos os canais (PDV, Balcão, OMNI) operando conforme esperado; métricas de performance dentro do SLA
- Responsável pelo aceite: Humberto Erler (Gerente de TI D1000)

---

## 8. Eventos de V&V realizados (registro histórico)

| Evento | Data | Resultado |
|---|---|---|
| Primeira revisão técnica com Armando Junior | 09/05/2025 | Aprovação da arquitetura do Sprint 1; 3 ajustes de nomenclatura |
| Testes de integração ITEC (outbox) | 20/06/2025 | 2 bugs S2 identificados e corrigidos na semana seguinte |
| Início dos testes formais de homologação | Setembro/2025 | 14 defeitos identificados (2 S1, 5 S2, 7 S3) |
| Sala de guerra — resolução de incidentes homologação | 02/10/2025 | S1 e S2 críticos resolvidos; aceite parcial |
| Testes de performance | Novembro/2025 | Latência p95 GET = 142ms; requisito atendido |
| Testes de integração Propz CRM | Dezembro/2025 | Integração validada; aceite Propz em 10/12/2025 |
| Liberação formal para homologação final | 22/01/2026 | Ambiente estável; roteiros de homologação entregues |
| Rodada final de correções e PRs | 27–29/01/2026 | Todos os defeitos S1 e S2 resolvidos |
| Aceite formal D1000 | 29/01/2026 | Aceite emitido por Humberto Erler |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 28/04/2025 | Time de Melhoria Contínua | Versão inicial — estratégia de V&V e roteiros de teste |
| 1.1 | 05/06/2026 | Time de Melhoria Contínua | Versão de encerramento — inclusão do registro histórico dos eventos de V&V realizados |
