# Matriz de Rastreabilidade — Milhas3 · Plataforma de Busca e Monitoramento de Milhas

| Campo | Valor |
|---|---|
| **Documento** | RASTR-MILHASFACIL01-001 — Matriz de Rastreabilidade |
| **Versão** | 1.0 |
| **Data** | 16/05/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Processo MPS-SW** | REQ — Engenharia de Requisitos |

---

## 1. Objetivo

Rastrear a cobertura dos requisitos funcionais e não funcionais definidos em REQ-MILHASFACIL01-001 ao longo dos artefatos técnicos e de verificação do projeto.

## 2. Matriz de rastreabilidade — Requisitos funcionais

| Requisito | Descrição resumida | PCP (seção) | ITP | VV (item) | Sprint | Status final |
|---|---|---|---|---|---|---|
| RF-01 | Cadastro de usuário | §3.2, §4 | INT-07 | VV-01 | Sprint 1 | Entregue |
| RF-02 | Autenticação JWT | §3.2, §4 | INT-07 | VV-01 | Sprint 1 | Entregue |
| RF-03 | Logout | §3.2, §4 | INT-07 | VV-01 | Sprint 1 | Entregue |
| RF-04 | Busca consolidada (5 programas) | §3.3, §5 | INT-01–05, INT-06 | VV-07 | Sprint 5 | Entregue |
| RF-05 | Rastreamento LATAM Pass | §3.3 | INT-01 | VV-02 | Sprint 2 | Entregue |
| RF-06 | Rastreamento Smiles / GOL | §3.3 | INT-02 | VV-03 | Sprint 3 | Entregue |
| RF-07 | Rastreamento TudoAzul / Azul | §3.3 | INT-03 | VV-04 | Sprint 3 | Entregue |
| RF-08 | Rastreamento TAP Miles&Go | §3.3 | INT-04 | VV-05 | Sprint 4 | Entregue |
| RF-09 | Rastreamento Iberia Plus | §3.3 | INT-05 | VV-06 | Sprint 4 | Entregue |
| RF-10 | Assinatura de rotas de interesse | §3.2, §4 | INT-06 | VV-08 | Sprint 6 | Entregue |
| RF-11 | Alertas automáticos | §3.2, §4 | INT-06, INT-09 | VV-08 | Sprint 6 | Entregue |
| RF-12 | Histórico de buscas | §3.2, §4 | INT-07 | VV-09 | Sprint 7 | Entregue |
| RF-13 | Preferências / rotas favoritas | §3.2, §4 | INT-07 | VV-10 | Sprint 7 | Entregue |
| RF-14 | Notificações in-app | §3.1, §4 | INT-07 | VV-11 | Sprint 8 | Entregue |
| RF-15 | Notificações por e-mail | §3.2, §4 | INT-09 | VV-12 | Sprint 8 | Entregue |
| RF-16 | Chat / suporte integrado | §3.1, §3.2 | INT-07 | VV-13 | Sprint 9 | Entregue |

## 3. Matriz de rastreabilidade — Requisitos não funcionais

| Requisito | Descrição resumida | PCP (seção) | ITP | VV (item) | Status final |
|---|---|---|---|---|---|
| RNF-01 | Java 17 + Spring Boot 3.x | §3.2 | — | VV-14 | Conforme |
| RNF-02 | Angular 16+ | §3.1 | — | VV-14 | Conforme |
| RNF-03 | PostgreSQL + Flyway | §3.2, §4 | INT-08 | VV-14 | Conforme |
| RNF-04 | VM Linux | §6 | — | VV-14 | Conforme |
| RNF-05 | Azure DevOps CI/CD | §6 | — | VV-14 | Conforme |
| RNF-06 | Busca ≤ 30s | §3.3, §6 | — | VV-14 | Conforme |
| RNF-07 | API p95 ≤ 500ms | §3.2 | — | VV-14 | Conforme |
| RNF-08 | JWT + bcrypt | §3.2 | — | VV-14 | Conforme — Sprint 1 |
| RNF-09 | LGPD | §3.2 | — | VV-14 | Conforme — Sprint 1 |
| RNF-10 | Selenium + bypass Akamai | §3.3, §7 | INT-01–05 | VV-02–06 | Conforme — GDE-MILHASFACIL01-001 |
| RNF-11 | Cobertura ≥ 70% | — | — | VV-14 | Conforme — 74% medido no Sprint 10 |
| RNF-12 | Uptime ≥ 99% | §6 | — | VV-14 | [A CONFIRMAR] — monitoramento pós-entrega |

## 4. Rastreabilidade de Change Requests

Nenhuma Change Request formal registrada no projeto. Ajustes menores de escopo tratados como refinamento de backlog dentro das sprints.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/05/2025 | Time de Melhoria Contínua | Versão inicial — baseline do projeto |
