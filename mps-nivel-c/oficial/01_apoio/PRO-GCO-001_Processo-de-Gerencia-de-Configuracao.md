# Processo de Gerência de Configuração — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-GCO-001 — Processo de Gerência de Configuração |
| **Versão** | 1.1 |
| **Data** | 10/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Responsável** | Cézar Velázquez |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware gerencia a configuração dos seus produtos de trabalho em projetos de software sob medida — identificando e controlando itens de configuração, controlando versões e mudanças, estabelecendo baselines e garantindo a integridade da configuração por meio de auditorias regulares.

O processo de Gerência de Configuração (GCO) é um processo de apoio: aplica-se a todos os projetos no escopo da organização e atravessa o ciclo de vida do projeto desde a abertura até o encerramento.

## 2. Conceitos fundamentais

| Conceito | Definição operacional |
|---|---|
| **Item de configuração (IC)** | Produto de trabalho colocado sob controle formal de configuração (código, documento, artefato de teste, release). |
| **Baseline** | Versão de referência, aprovada e estável, de um conjunto de ICs em um determinado momento; a partir dela as mudanças passam a ser controladas formalmente. |
| **Controle de mudança** | Mecanismo pelo qual uma alteração em um IC sob configuração é proposta, avaliada, aprovada e registrada antes de ser aplicada. |
| **Auditoria de configuração** | Verificação objetiva de que as baselines estão íntegras e de que as regras de configuração foram seguidas. |

## 3. Entradas do processo

- Artefatos de projeto (código-fonte, documentos de requisitos, design, planos de teste, planos de projeto).
- Ativos organizacionais: convenção de nomenclatura (CONV-ORG-001), processo-padrão (PRO-GPC-001) e plano operacional de configuração (PLA-GCO-001).
- Acordos e contratos (definem o escopo dos ICs a controlar por projeto).

## 4. Atividades do processo

### 4.1 Identificação dos itens de configuração

Ao início de cada projeto, os ICs a ser controlados são identificados e formalizados. O Gerente de Projeto, com apoio do Tech Lead, registra os ICs do projeto no Registro de Adaptação (TPL-GPR-003), incluindo o nível de controle aplicado a cada item.

Os ICs mínimos obrigatórios por projeto são definidos no plano operacional (PLA-GCO-001 §3.1) e incluem repositório de código, documentos-chave (requisitos, design, plano de projeto, plano de V&V) e baselines de release.

### 4.2 Controle de versão e de mudanças

O código-fonte é versionado no Git (Azure Repos) com a estrutura de branches definida em CONV-ORG-001: `main` (produção), `develop` (integração) e branches de funcionalidade (`feature/...`).

Toda mudança no código entra exclusivamente via **Pull Request** revisado e aprovado antes do merge. Não há merge direto na `main`. A aprovação do Pull Request constitui o controle de mudança de código.

Mudanças de escopo ou requisito são avaliadas e aprovadas pelo Product Owner em conjunto com o cliente antes de se tornarem trabalho; são refletidas no backlog com rastreabilidade.

Mudanças em documentos sob controle seguem o versionamento conforme CONV-ORG-001 (incremento de versão + linha no histórico de revisões).

### 4.3 Estabelecimento de baselines

As baselines de código são estabelecidas por meio de **tags/releases no Git** com versionamento semântico (`MAIOR.MENOR.CORREÇÃO`), criadas a cada entrega aprovada e promovida para produção. A tag constitui uma baseline imutável e recuperável.

Para documentos, a baseline corresponde à versão aprovada (1.0 ou superior), conforme CONV-ORG-001.

A promoção entre ambientes (Dev → QA → Homologação → Stage → Produção) garante que apenas código que passou por todas as verificações anteriores avança. A promoção para produção exige aprovação formal do cliente.

### 4.4 Registro e rastreabilidade de modificações

O histórico de modificações é mantido continuamente pelas ferramentas:

- **Git** registra todo o histórico de alterações do código (autor, data, descrição) e os Pull Requests registram revisões e aprovações.
- **Azure DevOps** registra builds, releases e a rastreabilidade entre itens de trabalho e código.
- **Documentos** mantêm histórico de revisões interno (conforme CONV-ORG-001) e versionamento no Confluence.

Esse conjunto permite identificar, a qualquer momento, o estado de cada IC e o histórico completo de suas mudanças.

### 4.5 Auditoria de configuração

Periodicamente, o responsável pela auditoria de configuração (GCO Baseline / Auditoria) conduz auditorias verificando:

- se as baselines estão íntegras e correspondem ao que está em produção;
- se os ICs estão versionados e armazenados corretamente;
- se as mudanças seguiram o controle definido (PRs revisados, aprovações registradas);
- se a rastreabilidade entre itens de trabalho, código e releases está mantida.

Os achados das auditorias são registrados e tratados como ações corretivas. As auditorias de configuração integram a atuação da Garantia da Qualidade de Processo (EST-GPC-001).

## 5. Saídas do processo

- Repositório de código versionado com histórico completo de modificações.
- Registro de ICs do projeto (no Registro de Adaptação TPL-GPR-003).
- Baselines de releases (tags Git) e baselines de documentos (versões aprovadas).
- Registros de Pull Requests (controle de mudança de código).
- Registros de auditorias de configuração.

## 6. Papéis

| Papel | Responsabilidade no processo |
|---|---|
| **Equipe de Desenvolvimento** | Versiona o código conforme CONV-ORG-001; abre e revisa Pull Requests; mantém os ICs sob controle. |
| **Tech Lead / Arquiteto** | Define a estrutura de branches do projeto; aprova mudanças técnicas relevantes. |
| **Product Owner** | Avalia e aprova mudanças de escopo com o cliente; mantém rastreabilidade no backlog. |
| **Gerente de Projeto** | Garante que a GCO seja seguida no projeto; registra os ICs no início do projeto. |
| **GCO Baseline / Auditoria** | Conduz as auditorias de configuração; verifica a integridade das baselines. |
| **Garantia da Qualidade (GQA)** | Verifica objetivamente a aderência ao processo de configuração. |

## 7. Documentos relacionados

- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento
- PLA-GCO-001 — Plano Operacional de Gerência de Configuração (detalha os ICs mínimos, estrutura de branches e frequência de auditorias)
- GUIA-GCO-001 — Guia de Nomenclaturas Técnicas
- PRO-GPC-001 — Processo-Padrão Organizacional
- GUIA-GPC-001 — Guia de Adaptação do Processo-Padrão
- EST-GPC-001 — Estratégia de Garantia da Qualidade

## 8. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados do processo **Gerência de Configuração (GCO)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| GCO 1 — itens de configuração identificados e níveis de controle definidos | Seção 4.1 (identificação); PLA-GCO-001 §3 (tabela de ICs e níveis) |
| GCO 2 — sistema de gerência de configuração e de controle de mudanças estabelecido | Seção 4.2 (Git/Azure DevOps/PR); PLA-GCO-001 §4 |
| GCO 3 — baselines estabelecidas | Seção 4.3; PLA-GCO-001 §5 |
| GCO 4 — modificações e liberações controladas; registros mantidos | Seção 4.4; PLA-GCO-001 §6 |
| GCO 5 — integridade das baselines garantida (auditorias de configuração) | Seção 4.5; PLA-GCO-001 §7 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Cézar Velázquez |
| 1.0 | 10/06/2026 | Time de Melhoria Contínua | Versão inicial — definição formal do processo de gerência de configuração, complementando o plano operacional PLA-GCO-001 |
