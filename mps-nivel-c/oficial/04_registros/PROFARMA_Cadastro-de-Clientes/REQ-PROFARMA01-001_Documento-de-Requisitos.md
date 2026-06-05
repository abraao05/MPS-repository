# Documento de Requisitos — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | REQ-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.3 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | REQ (evidência de projeto) |

---

## 1. Objetivo

Registrar os requisitos funcionais e não funcionais do sistema de Cadastro de Clientes da Rede D1000, servindo como base para o desenvolvimento, testes e rastreabilidade. Os requisitos foram levantados ao longo de sprints 1–4 (março a junho de 2025) e estabilizaram-se na Sprint 5, com ajustes pontuais documentados no histórico de revisões.

---

## 2. Glossário

| Termo | Definição |
|---|---|
| CPF | Cadastro de Pessoas Físicas — chave primária do cliente no novo sistema |
| ITEC | Sistema legado de retaguarda da Rede D1000 |
| Outbox | Padrão de persistência de eventos para integração assíncrona confiável com o ITEC |
| PDV | Ponto de Venda — terminal nas lojas físicas |
| Balcão | Canal de atendimento em loja físico-digital |
| OMNI | Canal e-commerce integrado via plataforma VTEX |
| PBM | Programa de Benefícios em Medicamentos — Interplayers |
| GMUD | Gerenciamento de Mudanças (Change Management) — processo de autorização de deploy em produção |
| AKS | Azure Kubernetes Service — plataforma de orquestração de containers |
| LGPD | Lei Geral de Proteção de Dados (Lei nº 13.709/2018) |

---

## 3. Requisitos Funcionais

### 3.1 Cadastro e gerenciamento de clientes

| ID | Requisito | Prioridade | Sprint de origem |
|---|---|---|---|
| RF-01 | O sistema deve permitir o cadastro de um novo cliente com CPF como chave primária única. Os campos obrigatórios são: CPF, nome completo, data de nascimento, telefone e e-mail. | Alta | Sprint 1 |
| RF-02 | O sistema deve rejeitar cadastro de CPF já existente na base, retornando erro HTTP 409 com mensagem descritiva. | Alta | Sprint 1 |
| RF-03 | O sistema deve permitir a consulta de cliente por CPF via endpoint GET, retornando todos os dados cadastrais ativos. | Alta | Sprint 1 |
| RF-04 | O sistema deve permitir a atualização parcial (PATCH) dos dados cadastrais de um cliente existente (nome, endereço, telefone, e-mail, dados complementares). | Alta | Sprint 2 |
| RF-05 | O sistema deve permitir a inativação lógica de um cliente (LGPD — direito ao esquecimento), preservando integridade referencial e registrando o motivo e data da inativação. | Alta | Sprint 3 |
| RF-06 | O sistema deve permitir a consulta de cliente por nome parcial (search) com paginação de resultados. | Média | Sprint 2 |
| RF-07 | O sistema deve registrar log de auditoria para toda operação de criação, atualização e inativação, com identificação do operador, canal de origem e timestamp. | Alta | Sprint 3 |
| RF-08 | O sistema deve suportar a carga inicial de aproximadamente 7 milhões de CPFs saneados da base legada ITEC, via worker batch dedicado. | Alta | Sprint 4 |
| RF-09 | O sistema deve expor endpoint de verificação de existência de CPF (HEAD /clientes/{cpf}) para uso do PDV sem retornar dados pessoais completos. | Média | Sprint 2 |
| RF-10 | O sistema deve permitir a reativação de um cliente previamente inativado, mediante registro de motivo. | Média | Sprint 4 |

### 3.2 Integrações

| ID | Requisito | Prioridade | Sprint de origem |
|---|---|---|---|
| RF-11 | O sistema deve publicar eventos de criação/atualização/inativação de cliente no outbox do banco de dados (PostgreSQL), consumidos pelo worker de integração com o ITEC legado. A consistência é eventual e tolerante a falhas transientes. | Alta | Sprint 3 |
| RF-12 | O sistema deve expor os endpoints de cadastro e consulta de cliente compatíveis com o contrato de API consumido pela plataforma VTEX (canal OMNI). | Alta | Sprint 5 |
| RF-13 | O sistema deve expor os endpoints necessários para o Call Center consultar e cadastrar clientes em tempo real (SLA de resposta: 95% das requisições em até 500ms). | Alta | Sprint 5 |
| RF-14 | O sistema deve notificar o Propz CRM de eventos de criação e atualização de cliente via Azure Service Bus, seguindo o schema de mensagem definido pela Propz. | Média | Sprint 7 |
| RF-15 | O sistema deve integrar-se com a BlueSoft para sincronização de dados de endereço e score de crédito do cliente, quando disponíveis. | Baixa | Sprint 8 |
| RF-16 | O sistema deve integrar-se com a CloseUp para consulta de histórico de compras do cliente, retornando dados agregados no endpoint de perfil completo. | Baixa | Sprint 9 |

### 3.3 Worker de expurgo (LGPD)

| ID | Requisito | Prioridade | Sprint de origem |
|---|---|---|---|
| RF-17 | O sistema deve incluir um worker de expurgo que anonimize dados pessoais de clientes inativados há mais de 5 anos, conforme política LGPD, gerando log de auditoria de cada registro processado. | Média | Sprint 6 |

### 3.4 Administração e operação

| ID | Requisito | Prioridade | Sprint de origem |
|---|---|---|---|
| RF-18 | O sistema deve expor endpoint de health check (GET /health) retornando status dos componentes: banco de dados, filas e dependências externas críticas. | Alta | Sprint 1 |
| RF-19 | O sistema deve expor métricas no formato Prometheus para coleta pelo Datadog. | Média | Sprint 5 |

---

## 4. Requisitos Não Funcionais

| ID | Requisito | Categoria |
|---|---|---|
| RNF-01 | A API deve ser desenvolvida em .NET 8, seguindo os princípios de Clean Architecture (camadas Domain, Application, Infrastructure, API). | Arquitetura |
| RNF-02 | O banco de dados principal deve ser PostgreSQL hospedado no Azure (Azure Database for PostgreSQL — Flexible Server). | Infraestrutura |
| RNF-03 | O deploy da aplicação deve ser realizado em contêineres Docker orquestrados pelo Azure Kubernetes Service (AKS). | Infraestrutura |
| RNF-04 | Todas as URLs, strings de conexão e segredos devem ser armazenados no banco de dados ou Azure Key Vault — nunca hardcoded no código ou nos arquivos de configuração do repositório. | Segurança |
| RNF-05 | A API deve implementar autenticação via API Key para canais PDV e Balcão; autenticação OAuth 2.0 para integrações sistema-a-sistema (VTEX, Propz). | Segurança |
| RNF-06 | O sistema deve suportar pico de 500 requisições/segundo no endpoint de consulta por CPF (GET /clientes/{cpf}) sem degradação de SLA. | Performance |
| RNF-07 | O tempo de resposta do endpoint de consulta por CPF deve ser ≤ 200ms (percentil 95) em condições normais de carga. | Performance |
| RNF-08 | O sistema deve estar disponível 99,5% do tempo medido mensalmente (excluindo janelas de manutenção programadas via GMUD). | Disponibilidade |
| RNF-09 | O banco de dados deve ter backup automático com retenção de 7 dias e capacidade de point-in-time recovery. | Resiliência |
| RNF-10 | Todos os dados pessoais tratados pelo sistema devem seguir os princípios da LGPD: finalidade, adequação, necessidade, livre acesso, qualidade dos dados, transparência, segurança, prevenção, não discriminação e responsabilização. | Conformidade (LGPD) |
| RNF-11 | A cobertura de testes unitários deve ser de no mínimo 80% das linhas de código da camada de Application e Domain. O projeto deve atingir ao menos 273 cenários de teste unitário. | Qualidade |
| RNF-12 | O pipeline CI/CD deve ser configurado no Azure DevOps com gates de qualidade: build, testes unitários (passagem obrigatória) e análise estática. | DevOps |
| RNF-13 | O monitoramento e observabilidade do sistema em produção devem ser realizados via Datadog (APM, logs e alertas). | Observabilidade |
| RNF-14 | Mudanças arquiteturais significativas na solução requerem aprovação do Tech Lead D1000 (Armando Junior) antes da implementação. | Governança |

---

## 5. Requisitos de Integração — Detalhamento

### 5.1 ITEC (Legado)

- **Padrão:** Outbox pattern + worker assíncrono
- **Direção:** Cadastro de Clientes → ITEC
- **Eventos publicados:** ClienteCriado, ClienteAtualizado, ClienteInativado
- **Garantia:** At-least-once delivery com idempotência no ITEC
- **Schema:** JSON definido em conjunto com a equipe ITEC durante Sprint 3

### 5.2 VTEX (OMNI)

- **Padrão:** REST síncrono
- **Direção:** VTEX → Cadastro de Clientes
- **Endpoints expostos:** RF-12 (cadastro e consulta)
- **Autenticação:** API Key
- **Schema:** Contrato VTEX CustomerProfile API adaptado

### 5.3 Propz CRM

- **Padrão:** Azure Service Bus (mensageria assíncrona)
- **Direção:** Cadastro de Clientes → Propz
- **Eventos publicados:** ClienteCriado, ClienteAtualizado
- **Schema:** definido pela Propz, validado em Sprint 7
- **Deadline de integração:** 04/12/2025 (marco contratual)

### 5.4 PBM / Interplayers

- **Padrão:** REST síncrono
- **Direção:** bidirecional (consulta e atualização de programa de benefícios)
- **Endpoints:** identificados em Sprint 8

### 5.5 BlueSoft

- **Padrão:** REST síncrono
- **Direção:** Cadastro de Clientes → BlueSoft (consulta de score/endereço)
- **Sprint de implementação:** Sprint 8

### 5.6 CloseUp

- **Padrão:** REST síncrono
- **Direção:** Cadastro de Clientes → CloseUp (consulta de histórico)
- **Sprint de implementação:** Sprint 9

---

## 6. Endpoints da API (resumo dos 16 endpoints)

| # | Método | Rota | Descrição | RF relacionado |
|---|---|---|---|---|
| 1 | POST | /clientes | Criação de novo cliente | RF-01, RF-02 |
| 2 | GET | /clientes/{cpf} | Consulta cliente por CPF | RF-03 |
| 3 | PATCH | /clientes/{cpf} | Atualização parcial de dados | RF-04 |
| 4 | DELETE | /clientes/{cpf} | Inativação lógica (LGPD) | RF-05 |
| 5 | GET | /clientes | Busca por nome (search + paginação) | RF-06 |
| 6 | HEAD | /clientes/{cpf} | Verificação de existência de CPF | RF-09 |
| 7 | PUT | /clientes/{cpf}/reativar | Reativação de cliente | RF-10 |
| 8 | GET | /clientes/{cpf}/perfil-completo | Perfil completo com histórico CloseUp | RF-16 |
| 9 | GET | /clientes/{cpf}/programa-beneficios | Dados PBM / Interplayers | RF-15 |
| 10 | POST | /clientes/lote | Carga em lote (migration worker) | RF-08 |
| 11 | GET | /clientes/{cpf}/auditoria | Log de auditoria do cliente | RF-07 |
| 12 | GET | /health | Health check dos componentes | RF-18 |
| 13 | GET | /metrics | Métricas Prometheus | RF-19 |
| 14 | POST | /clientes/vtex | Endpoint compatível VTEX | RF-12 |
| 15 | GET | /clientes/vtex/{cpf} | Consulta compatível VTEX | RF-12 |
| 16 | GET | /clientes/{cpf}/call-center | Perfil resumido para Call Center | RF-13 |

---

## 7. Restrições e premissas

- Os requisitos foram levantados de forma iterativa ao longo dos sprints; as mudanças de escopo foram formalizadas via processo de change request conforme GMUD.
- A base legada ITEC tem inconsistências históricas (duplicatas por CPF, registros incompletos); o saneamento foi responsabilidade do DBA Marcus Ribeiro (Profarma) com suporte do time Timeware.
- Requisitos de integração com BlueSoft e CloseUp entraram no escopo após Sprint 6 (change request aprovado em agosto/2025).
- O requisito RF-14 (Propz CRM) teve sua implementação e testes acelerados para atender ao marco de 04/12/2025.

---

## 8. Confirmação de entendimento dos requisitos

| Envolvido | Papel | Forma de confirmação | Data |
|---|---|---|---|
| Armando Junior | Tech Lead D1000 | Revisão de design (REV-001, 09/05/2025) + aprovação das decisões arquiteturais GDE-001/GDE-002 | 09/05/2025 |
| Helena Moreira | Coordenadora de Projeto D1000 | Participação nas Sprint Reviews + aceites parciais por e-mail (Sprints 1–17) | Contínuo Sprints 1–17 |
| Julielle Santos | QA D1000 | Aprovação dos roteiros de teste (VV §5) + execução UAT + aceite de homologação | Set/2025–Jan/2026 |
| Humberto Erler | Gerente de TI D1000 | Aceite formal do projeto (ATA-PROFARMA01-002, 29/01/2026) | 29/01/2026 |

Os requisitos foram revisados e confirmados de forma iterativa ao longo do projeto:

- **Versão 1.0 (RF-01 a RF-10, RNF-01 a RNF-08):** confirmados na Sprint Review da Fase 1 (Junho/2025) com presença de Armando Junior e Helena Moreira.
- **Change requests CR-01 a CR-12:** cada requisito adicionado ou alterado foi confirmado com aprovação formal antes da implementação, evidenciado na RASTR-PROFARMA01-001 §5 e auditado na GQA-P02 (10/10/2025).
- **Confirmação final:** aceite formal de Humberto Erler em 29/01/2026 (ATA-PROFARMA01-002), atestando que todos os 19 RF e 14 RNF foram atendidos conforme os critérios de saída verificados.

A GQA-P01 registrou NC-01 (requisitos documentados retroativamente para os Sprints 1–3); a ação corretiva foi executada até 30/06/2025 e confirmada como resolvida na GQA-P02.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 28/04/2025 | Time de Melhoria Contínua | Versão inicial — requisitos RF-01 a RF-10, RNF-01 a RNF-08 |
| 1.1 | 15/08/2025 | Time de Melhoria Contínua | Adição de RF-15, RF-16 (BlueSoft e CloseUp), RF-17 (worker expurgo LGPD), RNF-09 a RNF-14 |
| 1.2 | 05/06/2026 | Time de Melhoria Contínua | Versão de encerramento — reconstituída com base nas entregas, change requests e transcrições do período 04/2025–01/2026 |
| 1.3 | 05/06/2026 | Time de Melhoria Contínua | Adição da seção §8 (Confirmação de entendimento dos requisitos) para conformidade com MPS-SW REQ |
