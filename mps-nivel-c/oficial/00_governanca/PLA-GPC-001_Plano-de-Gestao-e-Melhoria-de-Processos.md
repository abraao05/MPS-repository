# Plano de Gestão e Melhoria de Processos — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PLA-GPC-001 — Plano de Gestão e Melhoria de Processos |
| **Versão** | 1.2 |
| **Data** | 26/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este plano define como a Timeware mantém o conjunto de ativos de processo da organização, estabelece os ambientes-padrão de trabalho, implanta os processos nas equipes e conduz a melhoria contínua dos processos a partir das avaliações de seus resultados.

## 2. Inventário de ativos de processo

A Timeware mantém uma **biblioteca de ativos de processo**, no Confluence, contendo todos os ativos necessários à definição, execução, verificação e melhoria dos seus processos. O inventário abaixo identifica os ativos da organização:

| Código | Ativo | Tipo |
|---|---|---|
| POL-ORG-001 | Política Organizacional de Processos | Política |
| CONV-ORG-001 | Convenção de Nomenclatura e Versionamento | Convenção |
| PRO-GPC-001 | Processo-Padrão Organizacional | Processo |
| GUIA-GPC-001 | Guia de Adaptação do Processo-Padrão | Guia |
| PRO-GPC-002 | Definição do Time de Melhoria Contínua | Processo |
| EST-GPC-001 | Estratégia de Garantia da Qualidade | Estratégia |
| EST-GPC-002 | Estratégia de Gerência de Riscos e Oportunidades | Estratégia |
| PLA-GPC-001 | Plano de Gestão e Melhoria de Processos (este documento) | Plano |

O inventário é mantido atualizado pelo Time de Melhoria Contínua à medida que novos ativos são criados ou revisados (processos de apoio, templates e registros são incorporados ao inventário conforme produzidos).

## 3. Ambientes-padrão de trabalho

A Timeware define ambientes-padrão de trabalho que apoiam a execução consistente dos processos:

| Ambiente | Ferramenta | Uso |
|---|---|---|
| Gestão de projetos, riscos e ações | Jira | Planejamento, acompanhamento, backlog, riscos. |
| Repositório de código e versionamento | Git + Azure DevOps | Código-fonte, baselines, controle de versão. |
| Integração e entrega | Azure DevOps (Pipelines) | Build, integração contínua, ambientes. |
| Testes / qualidade do produto | Azure Test Plans + Jira/Xray | Casos de teste, execução, resultados. |
| Documentação e biblioteca de processos | Confluence | Ativos de processo, definições, registros. |

Esses ambientes constituem a infraestrutura padrão dos projetos e são adaptados conforme a necessidade de cada projeto.

## 4. Implantação dos processos

A implantação dos processos-padrão nas equipes é conduzida pelo Time de Melhoria Contínua e compreende:

- disponibilização dos ativos na biblioteca de processos (Confluence);
- comunicação dos processos às equipes;
- apoio (mentoria) às equipes na adoção e adaptação dos processos aos projetos;
- capacitação relacionada aos processos, conforme o Plano de Capacitação (CAP).

A adoção dos processos pelos projetos é verificada pela Garantia da Qualidade (EST-GPC-001).

## 5. Identificação e melhoria de processos

A melhoria de processos é contínua e baseada em evidências.

### 5.1. Identificação e registro de oportunidades

As **fontes de oportunidades de melhoria** são:

- achados das verificações da Garantia da Qualidade;
- indicadores de medição (defeitos, retrabalho, prazos), conforme o Plano de Medição (MED);
- lições aprendidas registradas no encerramento dos projetos;
- sugestões das equipes.

Todas as oportunidades identificadas são mantidas em um **Registro de Oportunidades de Melhoria**, no Jira, que funciona como repositório vivo. Cada oportunidade contém, no mínimo: identificação, origem (fonte), descrição, data de identificação, prioridade, responsável e situação (identificada, em análise, planejada, em implementação, implementada, descartada).

O Registro é mantido atualizado pelo Time de Melhoria Contínua, que revisa as oportunidades em suas reuniões mensais, garantindo que nenhuma seja perdida e que o status de cada uma esteja sempre visível.

### 5.2. Planejamento e implementação das melhorias

As oportunidades registradas são analisadas e **priorizadas** pelo Time de Melhoria Contínua conforme sua contribuição aos objetivos de negócio. As melhorias priorizadas são planejadas — com responsável, prazo e resultado esperado — e implementadas, com o progresso acompanhado no mesmo registro.

## 6. Avaliação da efetividade das melhorias

Após a implementação de uma melhoria, o Time de Melhoria Contínua avalia sua **efetividade**, verificando se o resultado esperado foi alcançado — por exemplo, comparando indicadores antes e depois da mudança. O resultado da avaliação é registrado e comunicado, e realimenta o ciclo de melhoria: melhorias efetivas são consolidadas no processo-padrão; melhorias que não atingiram o esperado são reavaliadas.

## 7. Papéis

| Papel | Responsabilidade |
|---|---|
| **Time de Melhoria Contínua** | Mantém o inventário e os ambientes; conduz implantação, melhoria e avaliação de efetividade. |
| **Equipes de Projeto** | Utilizam os ativos e ambientes; contribuem com sugestões e lições aprendidas. |
| **COO (Operações)** | Garante recursos operacionais para a melhoria; prioriza melhorias de impacto operacional; reporta ao CEO. |
| **Founder e CEO** | Patrocina a melhoria no nível estratégico; assegura alinhamento aos objetivos de negócio. |

## 8. Documentos relacionados

- POL-ORG-001 — Política Organizacional de Processos
- PRO-GPC-001 — Processo-Padrão Organizacional
- PRO-GPC-002 — Definição do Time de Melhoria Contínua
- EST-GPC-001 — Estratégia de Garantia da Qualidade
- Plano de Medição (MED) e Plano de Capacitação (CAP)

## 9. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde a **vários resultados** do processo **Gerência de Processos (GPC)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| GPC 1 — ativos de processo necessários identificados (inventário de ativos) | Seção 2 |
| GPC 4 — oportunidades de melhoria identificadas e mantidas | Seção 5.1 |
| GPC 5 — plano de implementação das melhorias de processo | Seção 5.2 |
| GPC 8 — ambientes padrão de trabalho estabelecidos | Seção 3 |
| GPC 10 — processos-padrão implantados/acompanhados na organização | Seção 4 |
| GPC 11 — efetividade das melhorias avaliada e relatada | Seção 6 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 25/08/2025 | Time de Melhoria Contínua | Definição inicial do plano de gestão e melhoria de processos |
| 1.1 | 19/11/2025 | Time de Melhoria Contínua | Inclusão do Registro de Oportunidades de Melhoria (GPC 4) na seção 5 |
| 1.2 | 26/11/2025 | Time de Melhoria Contínua | Inclusão da camada COO nos papéis |
