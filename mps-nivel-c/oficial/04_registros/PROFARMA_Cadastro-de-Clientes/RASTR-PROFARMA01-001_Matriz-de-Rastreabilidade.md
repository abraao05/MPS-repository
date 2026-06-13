# Matriz de Rastreabilidade — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | RASTR-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.1 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | REQ (evidência de projeto — rastreabilidade) |

---

## 1. Objetivo

Registrar a rastreabilidade entre requisitos, componentes de implementação, casos de teste e status de entrega, garantindo que todos os requisitos funcionais e não funcionais foram implementados e verificados.

---

## 2. Rastreabilidade — Requisitos Funcionais

| Requisito | Descrição (resumida) | Endpoint(s) | Sprint | Casos de teste | Status |
|---|---|---|---|---|---|
| RF-01 | Cadastro de novo cliente (CPF como PK) | POST /clientes | Sprint 1 | T-CAD-01, T-CAD-03 | Entregue |
| RF-02 | Rejeição de CPF duplicado (HTTP 409) | POST /clientes | Sprint 1 | T-CAD-02 | Entregue |
| RF-03 | Consulta por CPF (GET) | GET /clientes/{cpf} | Sprint 1 | T-CAD-04, T-CAD-05 | Entregue |
| RF-04 | Atualização parcial (PATCH) | PATCH /clientes/{cpf} | Sprint 2 | T-CAD-06 | Entregue |
| RF-05 | Inativação lógica (LGPD) | DELETE /clientes/{cpf} | Sprint 3 | T-CAD-07, T-CAD-08 | Entregue |
| RF-06 | Busca por nome parcial com paginação | GET /clientes?nome= | Sprint 2 | T-CAD-10 | Entregue |
| RF-07 | Log de auditoria (criação, atualização, inativação) | GET /clientes/{cpf}/auditoria (interno) | Sprint 3 | Testes de auditoria Sprint 3 | Entregue |
| RF-08 | Carga inicial (~7M CPFs) via worker batch | POST /clientes/lote | Sprint 4 + execução Sprint 13 | T-PERF-03 | Entregue |
| RF-09 | Verificação de existência de CPF (HEAD) | HEAD /clientes/{cpf} | Sprint 2 | T-CAD-11 | Entregue |
| RF-10 | Reativação de cliente inativo | PUT /clientes/{cpf}/reativar | Sprint 4 | T-CAD-09 | Entregue |
| RF-11 | Outbox pattern para integração ITEC | Worker interno + tabela outbox_eventos | Sprint 3 | T-ITEC-01 a T-ITEC-04 | Entregue |
| RF-12 | Endpoints compatíveis com VTEX (OMNI) | POST /clientes/vtex; GET /clientes/vtex/{cpf} | Sprint 5 | T-VTEX-01 a T-VTEX-03 | Entregue |
| RF-13 | Endpoints para Call Center (SLA 500ms) | GET /clientes/{cpf}/call-center | Sprint 5 | Testes de performance Call Center | Entregue |
| RF-14 | Notificação Propz CRM via Service Bus | Worker Azure Service Bus | Sprint 7 | Testes integração Propz Sprint 7 | Entregue |
| RF-15 | Integração BlueSoft (endereço + score) | GET /clientes/{cpf}/perfil-completo (parcial) | Sprint 8 | Testes integração BlueSoft Sprint 8 | Entregue |
| RF-16 | Integração CloseUp (histórico de compras) | GET /clientes/{cpf}/perfil-completo | Sprint 9 | Testes integração CloseUp Sprint 9 | Entregue |
| RF-17 | Worker de expurgo LGPD | Worker batch diário interno | Sprint 6 | Testes worker LGPD Sprint 10 | Entregue |
| RF-18 | Health check (/health) | GET /health | Sprint 1 | T-CAD-12 | Entregue |
| RF-19 | Métricas Prometheus (/metrics) | GET /metrics | Sprint 5 | Verificação Datadog Sprint 12 | Entregue |

**Cobertura de RF: 19/19 (100%)**

---

## 3. Rastreabilidade — Requisitos Não Funcionais

| Requisito | Descrição (resumida) | Evidência de atendimento | Status |
|---|---|---|---|
| RNF-01 | .NET 8 / Clean Architecture | Repositório Azure DevOps — estrutura de camadas | Atendido |
| RNF-02 | PostgreSQL no Azure | Azure Database for PostgreSQL Flexible Server provisionado | Atendido |
| RNF-03 | Deploy em AKS | Manifests Kubernetes no repositório; deploy confirmado | Atendido |
| RNF-04 | Sem hardcode de URLs/segredos | Revisão de código: zero ocorrências de segredos em código; Azure Key Vault configurado | Atendido |
| RNF-05 | Autenticação API Key + OAuth 2.0 | Middlewares de autenticação implementados e testados | Atendido |
| RNF-06 | 500 req/s no GET /clientes/{cpf} | Teste T-PERF-01: 500 req/s sem erros | Atendido |
| RNF-07 | Latência p95 ≤ 200ms | Teste T-PERF-01: p95 = 142ms | Atendido |
| RNF-08 | Disponibilidade 99,5% mensal | Monitoramento Datadog: disponibilidade acima de 99,5% no piloto | Atendido |
| RNF-09 | Backup automático 7 dias + PITR | Azure Database backup configurado (7 dias); PITR testado | Atendido |
| RNF-10 | Conformidade LGPD | RF-05 (inativação), RF-17 (expurgo), campos de auditoria, dados mínimos | Atendido |
| RNF-11 | ≥ 273 testes unitários; cobertura ≥ 80% | 273 testes unitários; cobertura: 84% Domain + Application | Atendido |
| RNF-12 | Pipeline CI/CD com gates de qualidade | Pipeline Azure DevOps configurada desde Sprint 1 | Atendido |
| RNF-13 | Monitoramento Datadog (APM, logs, alertas) | Datadog APM e alertas configurados; Sprint 12 | Atendido |
| RNF-14 | Mudanças arquiteturais aprovadas por Armando Junior | Evidências nos PRs do Azure DevOps com aprovação de Armando Junior | Atendido |

**Cobertura de RNF: 14/14 (100%)**

---

## 4. Rastreabilidade — Casos de teste por módulo

| Módulo | Total de cenários | Executados | Passaram | Taxa de sucesso |
|---|---|---|---|---|
| Cadastro e gerenciamento | 12 | 12 | 12 | 100% |
| ITEC Outbox | 4 | 4 | 4 | 100% |
| VTEX | 3 | 3 | 3 | 100% |
| Performance e carga | 3 | 3 | 3 | 100% |
| Testes unitários (273 cenários) | 273 | 273 | 273 | 100% |
| Outros (integração, segurança, LGPD) | ~50 (estimado) | ~50 | ~50 | ~100% |

---

## 5. Rastreabilidade — Change Requests e impacto em requisitos

| Change Request | Data de aprovação | Requisitos adicionados/alterados | Sprint de implementação |
|---|---|---|---|
| CR-01 | 15/05/2025 | RF-07 (auditoria detalhada com canal de origem) | Sprint 3 |
| CR-02 | 20/06/2025 | RF-09 (HEAD endpoint para PDV) | Sprint 2 retroativo |
| CR-03 | 01/08/2025 | RF-10 (reativação de cliente) | Sprint 4 |
| CR-04 | 15/08/2025 | RF-15 (BlueSoft), RF-16 (CloseUp) — novas integrações | Sprints 8–9 |
| CR-05 | 15/08/2025 | RF-17 (worker LGPD) | Sprint 6 retroativo |
| CR-06 | 20/08/2025 | RNF-09 (backup + PITR) explicitado | Sprint 11 |
| CR-07 | 01/09/2025 | RF-14 acelerado — deadline Propz 04/12/2025 confirmado | Sprint 7 |
| CR-08 | 15/09/2025 | RF-19 (métricas Prometheus para Datadog) | Sprint 5 retroativo |
| CR-09 | 01/10/2025 | Ajuste de contrato VTEX (novo schema CustomerProfile) | Sprint 9 |
| CR-10 | 15/10/2025 | Ajuste de contrato BlueSoft (novo campo score_credito) | Sprint 11 |
| CR-11 | 01/11/2025 | Adição de campo telefone_secundario em RF-01 | Sprint 14 |
| CR-12 | 15/12/2025 | Ajuste de SLA Call Center de 1000ms para 500ms (RNF-13 atualizado) | Sprint 16 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 28/04/2025 | Time de Melhoria Contínua | Versão inicial — RF-01 a RF-10, RNF-01 a RNF-08 |
| 1.1 | 05/06/2026 | Time de Melhoria Contínua | Versão de encerramento — cobertura total dos requisitos, change requests e status de entrega |
