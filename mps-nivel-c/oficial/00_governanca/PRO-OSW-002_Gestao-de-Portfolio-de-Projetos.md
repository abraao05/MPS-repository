# Gestão de Portfólio de Projetos — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-OSW-002 — Gestão de Portfólio de Projetos |
| **Versão** | 1.4 |
| **Data** | 13/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Responsável** | Wilson Yamada |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este documento define como a Timeware gerencia seu **portfólio de projetos** — o conjunto de projetos em andamento, olhados de forma consolidada — priorizando oportunidades, alocando recursos compartilhados e acompanhando os projetos quanto aos compromissos assumidos. A gestão do portfólio é responsabilidade das Operações (COO), por meio do escritório de portfólio de projetos.

## 2. Contexto

A Timeware conduz múltiplos projetos de software sob medida simultaneamente. Alguns recursos são **dedicados a um único projeto** (por exemplo, desenvolvedores), enquanto outros são **compartilhados entre projetos** — notadamente Tech Lead, Arquiteto e Product Owner. Essa característica cria a necessidade de gerenciar o portfólio, equilibrando a demanda dos projetos com a capacidade disponível desses recursos compartilhados.

## 3. Priorização de oportunidades e projetos

As oportunidades de negócio e os projetos são priorizados pelo COO (Operações), considerando critérios como:

- alinhamento com os objetivos de negócio (crescer com qualidade e previsibilidade);
- compromissos contratuais e prazos com clientes;
- disponibilidade de recursos, especialmente os compartilhados;
- retorno e relevância estratégica.

A priorização define quais projetos a organização assume e em que ordem de prioridade, de forma que os compromissos assumidos sejam compatíveis com a capacidade real da organização.

## 4. Recursos, capacidade e autoridade

### 4.1. Gestão de capacidade (capacity)

A Timeware mantém um **quadro de capacity** que registra a alocação dos recursos compartilhados (Tech Lead, Arquiteto, PO) entre os projetos. O quadro permite visualizar a ocupação desses recursos e identificar conflitos de alocação antes que afetem os projetos.

Quando a demanda excede a capacidade disponível, a organização atua de duas formas:

- **realoca recursos** de colaboradores da Timeware de fora da unidade, quando disponíveis;
- **contrata** novos recursos, quando necessário.

#### Estrutura do quadro de capacity

O quadro de capacity é mantido no Jira (ou página estruturada no Confluence), com os seguintes campos mínimos:

| Campo | Descrição |
|---|---|
| Colaborador | Nome/papel do recurso compartilhado (Tech Lead, Arquiteto, PO) |
| Projeto | Projeto(s) ao(s) qual(is) está alocado |
| Alocação (%) | Percentual da capacidade dedicado a cada projeto no período |
| Período | Sprint ou mês de referência |
| Status | Disponível · Alocado · Sobrecarregado |

**Cadência de atualização:** o quadro é revisado antes do início de cada sprint e sempre que ocorre mudança de alocação.

**Responsável pela manutenção:** COO (Operações), com apoio dos Gerentes de Projeto.

**Critério de escalada:** quando um recurso compartilhado ultrapassa 100% de alocação por duas sprints consecutivas, o COO convoca reunião de repriorização com os GPs envolvidos para ajustar escopo ou prazos.

### 4.2. Autoridade

A autoridade para decidir sobre a priorização do portfólio e a alocação de recursos compartilhados é do **COO (Operações)**, responsável pelo escritório de portfólio de projetos, apoiado pelas informações de capacity e pela situação dos projetos. Decisões de natureza estratégica são reportadas ao CEO.

## 5. Acompanhamento do portfólio

Os projetos do portfólio são acompanhados de forma consolidada quanto ao cumprimento dos compromissos (prazo, escopo, recursos). O acompanhamento:

- consolida a situação dos projetos em andamento;
- identifica projetos que se desviam dos acordos assumidos;
- direciona o tratamento dos desvios — realocação de recursos, repriorização ou ações específicas no projeto.

O acompanhamento do portfólio é apoiado pelas informações do Jira (situação dos projetos) e pelo quadro de capacity, e é tratado nas análises críticas pela direção (PRO-OSW-001). A consolidação periódica dessa operação, para fins de governança e auditoria, é registrada no **Painel de Portfólio (REG-OSW-001)**.

## 6. Papéis

| Papel | Responsabilidade |
|---|---|
| **COO (Operações)** | Prioriza o portfólio; decide alocação de recursos compartilhados; acompanha os projetos consolidadamente; reporta ao CEO o que for estratégico. |
| **Gerentes de Projeto** | Reportam a situação de seus projetos; sinalizam necessidades e conflitos de recursos. |
| **Time de Melhoria Contínua** | Apoia com informações de capacity e indicadores; trata riscos organizacionais relacionados ao portfólio. |

## 7. Documentos relacionados

- POL-ORG-001 — Política Organizacional de Processos
- PRO-OSW-001 — Governança Organizacional de Processos
- EST-GPC-002 — Estratégia de Gerência de Riscos e Oportunidades
- REG-OSW-001 — Painel de Portfólio de Projetos (registro consolidado)
- Processo de Gerência de Projetos (GPR)

## 8. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados **OSW 8, 9, 10** do processo **Gerência Organizacional de Software (OSW)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| OSW 8 — oportunidades de negócio/investimentos priorizados (portfólio) | Seção 3; evidência consolidada em REG-OSW-001 §3–4 |
| OSW 9 — recursos, orçamento e autoridade do portfólio estabelecidos | Seção 4; evidência consolidada em REG-OSW-001 §5 |
| OSW 10 — projetos do portfólio mantidos e tratados conforme os acordos | Seção 5; evidência consolidada em REG-OSW-001 §7 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.4 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Wilson Yamada |
| 1.0 | 29/08/2025 | Time de Melhoria Contínua | Definição inicial da gestão de portfólio de projetos |
| 1.1 | 24/11/2025 | Time de Melhoria Contínua | Atribuição da autoridade do portfólio ao COO (escritório de portfólio de projetos) |
| 1.2 | 20/03/2026 | Time de Melhoria Contínua | Detalhamento da estrutura e cadência do quadro de capacity (§4.1): campos, responsável e critério de escalada |
| 1.3 | 13/06/2026 | Time de Melhoria Contínua | Referência ao Painel de Portfólio (REG-OSW-001) como registro consolidado do acompanhamento (§5, §7 e §8 de rastreabilidade) |
