# Processo de Integração do Produto — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-ITP-001 — Processo de Integração do Produto |
| **Versão** | 1.1 |
| **Data** | 15/03/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware integra os componentes do produto de software, garantindo que sejam combinados de forma controlada, testados como conjunto e entregues com o material de apoio necessário.

## 2. Visão geral

A integração na Timeware é majoritariamente **contínua e automatizada**, apoiada pelo Azure DevOps (Pipelines). O código produzido nas sprints é integrado de forma incremental, com build e testes automatizados a cada integração, reduzindo riscos de integração tardia.

## 3. Estratégia de integração e interfaces

- Para cada projeto, define-se a **estratégia de integração**: a ordem e a forma como os componentes são combinados, e as **interfaces** entre eles (internas e com sistemas externos).
- A estratégia é registrada no template TPL-ITP-001 e adaptada ao porte do projeto.

## 4. Ambiente de integração

- O **ambiente de integração** é estabelecido com o Azure DevOps (Pipelines) e os ambientes de build/homologação, conforme os ambientes-padrão (PLA-GCO-001 / PLA-GPC-001).

## 5. Prontidão dos componentes

- Antes de serem integrados, os componentes são **avaliados quanto à prontidão**: atendem aos critérios de aceite, passaram por code review e pelos testes aplicáveis (Definição de Pronto).

## 6. Integração

- Os componentes são **integrados conforme a estratégia**, via pipelines de integração contínua, com build automatizado e verificação de que a integração não quebrou o produto.

## 7. Teste do produto integrado

- O **produto integrado** é testado quanto ao funcionamento em conjunto — testes de integração e validação do comportamento end-to-end, conforme o processo de Verificação e Validação (VV).
- Problemas identificados são registrados e tratados antes da entrega.

Os testes do produto integrado consideram os seguintes critérios de conclusão:

| Critério | Descrição |
|---|---|
| Build sem erros | Pipeline de build executado sem erros ou falhas críticas |
| Testes automatizados passando | Suíte de testes (unitários e de integração) dentro do limiar definido no Plano de V&V |
| Testes de regressão | Funcionalidades existentes verificadas para garantir que a integração não introduziu regressões |
| Interfaces verificadas | Interfaces com sistemas externos testadas nas condições representativas de uso |
| Defeitos críticos zerados | Nenhum defeito de severidade crítica em aberto antes do avanço para homologação |

Defeitos encontrados na integração são registrados no Jira e tratados antes do avanço para a etapa de homologação.

## 8. Entrega e material de apoio

- O produto integrado e testado é **entregue** em homologação para aprovação do cliente e, após aprovação, promovido para produção (conforme o processo-padrão).
- O **material de apoio** necessário (documentação técnica, instruções de uso/implantação, quando aplicável) é disponibilizado junto à entrega.

## 9. Papéis

| Papel | Responsabilidade |
|---|---|
| **Tech Lead / Arquiteto** | Definem a estratégia de integração e as interfaces. |
| **Equipe de Desenvolvimento** | Integra os componentes; mantém os pipelines. |
| **QA** | Testa o produto integrado (ver VV). |
| **Gerente de Projeto** | Garante a entrega e o material de apoio. |

## 10. Documentos e artefatos relacionados

- PRO-GPC-001 — Processo-Padrão Organizacional
- TPL-ITP-001 — Template de Estratégia de Integração
- PLA-GCO-001 — Plano de Gerência de Configuração
- Processo de Verificação e Validação (VV)

## 11. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados do processo **Integração do Produto (ITP)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| ITP 1 — estratégia de integração e interfaces | Seção 3 |
| ITP 2 — ambiente de integração | Seção 4 |
| ITP 3 — prontidão dos componentes | Seção 5 |
| ITP 4 — integração conforme a estratégia | Seção 6 |
| ITP 5 — teste do produto integrado | Seção 7 |
| ITP 6 — entrega e material de apoio | Seção 8 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 20/10/2025 | Time de Melhoria Contínua | Definição inicial do processo de integração do produto |
| 1.1 | 15/03/2026 | Time de Melhoria Contínua | Adição dos critérios de conclusão da integração com checklist de qualidade (§7) |
