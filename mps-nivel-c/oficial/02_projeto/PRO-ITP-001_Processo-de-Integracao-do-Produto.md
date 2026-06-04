# Processo de Integração do Produto — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-ITP-001 — Processo de Integração do Produto |
| **Versão** | 1.0 |
| **Data** | 20/10/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Processos MPS-SW relacionados** | ITP 1 a ITP 6 |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware integra os componentes do produto de software, garantindo que sejam combinados de forma controlada, testados como conjunto e entregues com o material de apoio necessário.

> **Mapa de resultados atendidos neste documento:**
> - Seção 3 → **ITP 1** (estratégia de integração e interfaces)
> - Seção 4 → **ITP 2** (ambiente de integração)
> - Seção 5 → **ITP 3** (prontidão dos componentes)
> - Seção 6 → **ITP 4** (integração conforme a estratégia)
> - Seção 7 → **ITP 5** (teste do produto integrado)
> - Seção 8 → **ITP 6** (entrega e material de apoio)

## 2. Visão geral

A integração na Timeware é majoritariamente **contínua e automatizada**, apoiada pelo Azure DevOps (Pipelines). O código produzido nas sprints é integrado de forma incremental, com build e testes automatizados a cada integração, reduzindo riscos de integração tardia.

## 3. Estratégia de integração e interfaces (ITP 1)

- Para cada projeto, define-se a **estratégia de integração**: a ordem e a forma como os componentes são combinados, e as **interfaces** entre eles (internas e com sistemas externos).
- A estratégia é registrada no template TPL-ITP-001 e adaptada ao porte do projeto.

## 4. Ambiente de integração (ITP 2)

- O **ambiente de integração** é estabelecido com o Azure DevOps (Pipelines) e os ambientes de build/homologação, conforme os ambientes-padrão (PLA-GCO-001 / PLA-GPC-001).

## 5. Prontidão dos componentes (ITP 3)

- Antes de serem integrados, os componentes são **avaliados quanto à prontidão**: atendem aos critérios de aceite, passaram por code review e pelos testes aplicáveis (Definição de Pronto).

## 6. Integração (ITP 4)

- Os componentes são **integrados conforme a estratégia**, via pipelines de integração contínua, com build automatizado e verificação de que a integração não quebrou o produto.

## 7. Teste do produto integrado (ITP 5)

- O **produto integrado** é testado quanto ao funcionamento em conjunto — testes de integração e validação do comportamento end-to-end, conforme o processo de Verificação e Validação (VV).
- Problemas identificados são registrados e tratados antes da entrega.

## 8. Entrega e material de apoio (ITP 6)

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

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 20/10/2025 | Time de Melhoria Contínua | Definição inicial do processo de integração do produto |
