# Processo de Medição — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-MED-001 — Processo de Medição |
| **Versão** | 1.1 |
| **Data** | 10/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Responsável** | Silvio Baroni |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware coleta, verifica, armazena, analisa e comunica medidas relacionadas aos seus projetos e processos, de forma a apoiar decisões informadas e o alcance dos objetivos de negócio — crescer com qualidade e previsibilidade.

O processo de Medição (MED) é um processo de apoio organizacional: aplica-se continuamente a todos os projetos em andamento e alimenta a governança organizacional.

## 2. Princípio de alinhamento

As medidas da Timeware são derivadas de objetivos de negócio, não coletadas por obrigação. Cada medida responde a uma pergunta de gestão, e seu valor justifica o esforço de coleta. Medidas sem objetivos claros não são mantidas.

Os objetivos de medição são revisados trimestralmente na análise crítica organizacional (PRO-OSW-001), garantindo que permaneçam alinhados à estratégia da organização.

## 3. Entradas do processo

- Objetivos de negócio e de melhoria da organização.
- Dados registrados pelas equipes de projeto ao longo das sprints (Jira, Azure DevOps, Xray).
- Catálogo de medidas vigente (PLA-MED-001 §3) e objetivos de medição definidos.
- Resultados de ciclos anteriores (repositório organizacional de medidas).

## 4. Atividades do processo

### 4.1 Definição dos objetivos de medição

Os objetivos de medição são derivados dos objetivos de negócio e das necessidades de informação da gestão. Para o ciclo atual, os quatro objetivos são: aumentar a previsibilidade de prazo e esforço (OM1), acompanhar a capacidade de entrega (OM2), reduzir defeitos e retrabalho (OM3) e antecipar a detecção de defeitos (OM4). A definição e manutenção desses objetivos é responsabilidade do Time de Melhoria Contínua, revisada trimestralmente com o COO.

### 4.2 Definição das medidas

Para cada objetivo de medição, são definidas medidas com definições operacionais precisas: nome, objetivo ao qual serve, definição, fórmula (quando aplicável), fonte dos dados e frequência de coleta. O catálogo de medidas (M1–M7) está definido no plano operacional PLA-MED-001 §3 e abrange as medidas de previsibilidade (M1–M4) e de qualidade (M5–M7).

As definições operacionais garantem que o mesmo dado seja coletado da mesma forma em todos os projetos.

### 4.3 Coleta e verificação dos dados

Os dados são coletados continuamente ao longo das sprints pelas equipes de projeto, por meio do registro no Jira conforme as definições operacionais de cada medida:

- desenvolvedores registram estimativas, esforço real, pontos e defeitos no Jira;
- o QA registra defeitos encontrados em VV e homologação;
- o Gerente de Projeto garante a integridade dos registros do projeto.

O Time de Melhoria Contínua verifica os dados antes da consolidação, checando integridade (dados completos), consistência (definição operacional aplicada uniformemente) e atualidade (período correto). Inconsistências são corrigidas na origem.

### 4.4 Armazenamento no repositório organizacional

Os dados coletados por projeto são consolidados pelo Time de Melhoria Contínua no **repositório organizacional de medidas** (planilha/dashboard no Confluence), com frequência mensal. A estrutura do repositório (campos, acesso e localização) é definida em PLA-MED-001 §4.1.

O repositório mantém o histórico comparativo entre projetos e entre períodos, permitindo análise de tendências e benchmarking interno.

### 4.5 Análise do desempenho

O Time de Melhoria Contínua analisa as medidas mensalmente, comparando o desempenho realizado com os objetivos de medição e com ciclos anteriores. A análise identifica tendências, desvios e oportunidades de melhoria.

Os resultados da análise mensal constituem as **informações de governança** levadas à análise crítica trimestral (PRO-OSW-001) para apoiar decisões organizacionais pelo COO e CEO.

### 4.6 Ações corretivas e melhoria

Quando a análise indica desvio em relação aos objetivos, são definidas ações corretivas com responsável e prazo, rastreadas no Jira até a conclusão. Ações que impliquem mudança de processo são encaminhadas ao ciclo de melhoria organizacional (PLA-GPC-001).

### 4.7 Comunicação dos resultados

Os resultados consolidados são comunicados à organização mensalmente (Confluence) e trimestralmente na análise crítica. Resultados relevantes a um projeto específico são comunicados à respectiva equipe pelo Time de Melhoria Contínua.

### 4.8 Avaliação periódica do repositório

O repositório organizacional de medidas é avaliado periodicamente para assegurar a qualidade dos dados (integridade, consistência, atualidade), com registro da avaliação. Medidas ou definições operacionais desatualizadas são revisadas no catálogo.

## 5. Saídas do processo

- Catálogo de medidas com definições operacionais (PLA-MED-001 §3).
- Repositório organizacional de medidas atualizado (Confluence).
- Relatório de análise mensal de desempenho.
- Informações de governança para a análise crítica trimestral (PRO-OSW-001).
- Ações corretivas rastreáveis (Jira).

## 6. Papéis

| Papel | Responsabilidade no processo |
|---|---|
| **Equipes de Projeto** | Registram os dados no Jira ao longo das sprints, conforme as definições operacionais. |
| **Gerente de Projeto** | Garante que as medidas do projeto sejam coletadas corretamente e nos prazos definidos. |
| **Responsável de Medição** | Consolida as medidas dos projetos no repositório organizacional; verifica a qualidade dos dados; apoia as análises do Time de Melhoria Contínua. |
| **Time de Melhoria Contínua** | Mantém o catálogo e o repositório; analisa as medidas; comunica os resultados; propõe ações corretivas. |
| **COO (Operações)** | Usa as medidas na governança e na análise crítica trimestral; alinha os objetivos de medição à estratégia. |

## 7. Documentos relacionados

- PLA-MED-001 — Plano Operacional de Medição (catálogo de medidas M1–M7, estrutura do repositório, frequência de consolidação)
- POL-ORG-001 — Política Organizacional de Processos
- PRO-OSW-001 — Governança Organizacional de Processos (análise crítica trimestral)
- PRO-GPC-001 — Processo-Padrão Organizacional
- PLA-GPC-001 — Plano de Gestão e Melhoria de Processos
- EST-GPC-001 — Estratégia de Garantia da Qualidade

## 8. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados do processo **Medição (MED)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| MED 1 — objetivos de medição derivados dos objetivos de negócio | Seção 4.1; PLA-MED-001 §2 |
| MED 2 — medidas definidas com definições operacionais | Seção 4.2; PLA-MED-001 §3 |
| MED 3 — procedimentos de coleta e armazenamento das medidas | Seções 4.3 e 4.4; PLA-MED-001 §4 |
| MED 4 — procedimentos de análise das medidas | Seção 4.5; PLA-MED-001 §5 |
| MED 5 — coleta e análise realizadas; ações a partir das medidas | Seções 4.3, 4.5 e 4.6 |
| MED 6 — resultados comunicados aos interessados | Seção 4.7; PLA-MED-001 §7 |
| MED 7 — repositório de medidas avaliado periodicamente (qualidade das medidas) | Seção 4.8; PLA-MED-001 §8 |

Este processo também sustenta o repositório organizacional de medidas (GPC 9) e o uso de medidas pela governança (OSW 6).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Silvio Baroni |
| 1.0 | 10/06/2026 | Time de Melhoria Contínua | Versão inicial — definição formal do processo de medição, complementando o plano operacional PLA-MED-001 |
