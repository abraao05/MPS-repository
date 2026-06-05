# Plano de Gerência de Configuração — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PLA-GCO-001 — Plano de Gerência de Configuração |
| **Versão** | 1.1 |
| **Data** | 15/01/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este plano define como a Timeware gerencia a configuração dos seus produtos de trabalho — identificando itens de configuração, controlando suas versões e mudanças, estabelecendo baselines e auditando a integridade da configuração ao longo dos projetos.

## 2. Conceitos

- **Item de configuração (IC):** produto de trabalho colocado sob controle de configuração (código, documento, artefato de teste, release).
- **Baseline:** versão de referência, aprovada e estável, de um conjunto de itens em um determinado momento, a partir da qual as mudanças passam a ser controladas.
- **Controle de mudança:** processo pelo qual uma alteração em um item sob configuração é proposta, avaliada, aprovada e registrada.

## 3. Itens de configuração e níveis de controle

A Timeware coloca sob controle de configuração os seguintes itens:

| Item de configuração | Repositório | Nível de controle |
|---|---|---|
| Código-fonte | Git (Azure Repos) | Controle de versão + Pull Request com revisão |
| Documentos de processo (ativos organizacionais) | Confluence / repositório de documentos | Versionamento conforme CONV-ORG-001 |
| Documentos de projeto (requisitos, design, plano) | Confluence / repositório do projeto | Versionamento + aprovação |
| Artefatos de teste (casos, planos, resultados) | Azure Test Plans / Xray | Controle de versão na ferramenta |
| Artefatos de build e release | Azure DevOps (Pipelines/Artifacts) | Controle automatizado |

O **nível de controle** define o rigor aplicado a cada item: itens críticos (código, baselines, documentos aprovados) exigem aprovação formal para mudança; itens em elaboração têm controle mais leve até serem aprovados.

### 3.1. Itens de configuração mínimos por projeto

Todo projeto da Timeware mantém, no mínimo, os seguintes ICs sob controle de configuração:

| IC mínimo | Obrigatório para |
|---|---|
| Repositório de código-fonte (Git) | Todos os projetos |
| Plano de Projeto (TPL-GPR-001) | Todos os projetos |
| Documento de Requisitos (TPL-REQ-001 ou backlog estruturado) | Todos os projetos |
| Documento de Design (TPL-PCP-001) | Projetos com componente técnico significativo |
| Estratégia de Integração (TPL-ITP-001) | Projetos com integração com sistemas externos |
| Plano de V&V (TPL-VV-001) | Todos os projetos |
| Registros de revisão por pares (TPL-VV-002) | Todos os projetos |
| Baselines de release (tags Git) | Todos os projetos |
| Registros de GQA (TPL-GPC-001) | Todos os projetos |

O Gerente de Projeto confirma, no início do projeto, quais ICs se aplicam e registra no Registro de Adaptação do Processo (TPL-GPR-003).

## 4. Sistema de gerência de configuração e controle de mudanças

### 4.1. Estrutura de versionamento do código (branches)

A Timeware adota uma estratégia de branches baseada nas melhores práticas de mercado:

- **`main`** — contém sempre o código estável, equivalente ao que está em produção; é a linha de referência.
- **`develop`** — integração do trabalho em andamento antes de compor uma release (quando aplicável ao projeto).
- **branches de funcionalidade** (`feature/...`) — cada funcionalidade é desenvolvida em sua própria branch e integrada via Pull Request.

### 4.2. Controle de mudanças

As mudanças são controladas de forma combinada:

- **Mudanças de código:** entram exclusivamente via **Pull Request**, com **code review** aprovado antes do merge. Não há merge direto na `main`.
- **Mudanças de escopo/requisito:** são avaliadas e aprovadas pelo **PO em conjunto com o cliente** antes de virarem trabalho, e refletidas no backlog e na rastreabilidade.
- **Promoção entre ambientes:** o Azure DevOps (Pipelines) garante que o código só é promovido após build e testes bem-sucedidos.

## 5. Baselines

As baselines são estabelecidas por meio de **tags/releases no Git**, utilizando **versionamento semântico** (`MAIOR.MENOR.CORREÇÃO`):

- a cada entrega aprovada pelo cliente e promovida para produção, cria-se uma **tag** marcando exatamente aquele ponto do código;
- a tag constitui uma baseline: versão de referência, imutável e recuperável a qualquer momento;
- a evolução das versões segue o versionamento semântico: correções incrementam o último número (`v1.0.1`), novas funcionalidades o número intermediário (`v1.1.0`), e mudanças estruturais o primeiro (`v2.0.0`).

Para documentos, a baseline corresponde à versão aprovada (`1.0` ou superior), conforme a Convenção de Nomenclatura e Versionamento (CONV-ORG-001).

## 6. Registro de itens e modificações

O histórico de itens e suas modificações é mantido automaticamente pelas ferramentas:

- **Git** registra todo o histórico de alterações do código (autor, data, descrição) e os Pull Requests registram as revisões e aprovações;
- o **Azure DevOps** registra builds, releases e a rastreabilidade entre itens de trabalho (Jira) e código;
- os **documentos** mantêm histórico de revisões interno (conforme CONV-ORG-001) e o versionamento da ferramenta (Confluence).

Esse conjunto permite, a qualquer momento, identificar o estado de cada item de configuração e o histórico de suas mudanças.

## 7. Auditoria de configuração

Periodicamente, são realizadas **auditorias de configuração** para assegurar a integridade da configuração, verificando:

- se as baselines estão íntegras e correspondem ao que está em produção (a versão em produção corresponde à tag registrada);
- se os itens de configuração estão versionados e armazenados corretamente;
- se as mudanças seguiram o controle definido (PRs revisados, aprovações registradas);
- se a rastreabilidade entre itens de trabalho, código e releases está mantida.

As auditorias de configuração são conduzidas no contexto da Garantia da Qualidade (EST-GPC-001), e seus achados são registrados e tratados como ações corretivas quando necessário.

## 8. Papéis

| Papel | Responsabilidade |
|---|---|
| **Equipe de Desenvolvimento** | Versiona o código; abre e revisa Pull Requests; mantém os itens sob controle. |
| **Tech Lead / Arquiteto** | Define a estrutura de branches do projeto; aprova mudanças técnicas relevantes. |
| **Product Owner** | Avalia e aprova mudanças de escopo com o cliente. |
| **Gerente de Projeto** | Garante que a gerência de configuração seja seguida no projeto. |
| **Garantia da Qualidade (GQA)** | Conduz as auditorias de configuração. |

## 9. Documentos relacionados

- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento
- PRO-GPC-001 — Processo-Padrão Organizacional
- EST-GPC-001 — Estratégia de Garantia da Qualidade
- Processo de Verificação e Validação (VV)

## 10. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados do processo **Gerência de Configuração (GCO)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| GCO 1 — itens de configuração identificados e níveis de controle definidos | Seção 3 |
| GCO 2 — sistema de gerência de configuração e de controle de mudanças estabelecido | Seção 4 |
| GCO 3 — baselines estabelecidas | Seção 5 |
| GCO 4 — modificações e liberações controladas; registros mantidos | Seção 6 |
| GCO 5 — integridade das baselines garantida (auditorias de configuração) | Seção 7 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 12/09/2025 | Time de Melhoria Contínua | Definição inicial do plano de gerência de configuração |
| 1.1 | 15/01/2026 | Time de Melhoria Contínua | Adição da lista mínima de itens de configuração por projeto (§3.1) |
