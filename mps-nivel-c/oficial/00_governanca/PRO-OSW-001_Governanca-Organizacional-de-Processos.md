# Governança Organizacional de Processos — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-OSW-001 — Governança Organizacional de Processos |
| **Versão** | 1.3 |
| **Data** | 12/03/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações), com patrocínio do Founder e CEO |
| **Responsável** | Wilson Yamada |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este documento define como a direção da Timeware governa seus processos: como garante recursos, estabelece autoridade e competências, gerencia riscos organizacionais, utiliza medidas e informações de governança, e analisa criticamente o alinhamento dos processos aos objetivos de negócio.

## 2. Objetivos de negócio

Os processos da Timeware existem para servir ao objetivo central de **crescer com qualidade e previsibilidade**: entregar software conforme o acordado, dentro de prazos e custos planejados, de forma sustentável ao crescimento da organização. Toda a governança de processos descrita aqui é orientada a esse objetivo.

## 3. Garantia de recursos

A direção da Timeware garante os recursos necessários para definir, executar, verificar e melhorar os processos, incluindo:

- pessoas alocadas ao Time de Melhoria Contínua;
- tempo dos colaboradores para participar das atividades de processo (definição, verificação, melhoria, capacitação);
- ferramentas e ambientes de trabalho (Jira, Git, Azure DevOps, Confluence e demais);
- recursos para capacitação, conforme o Plano de Capacitação (CAP).

A provisão de recursos é tratada pela direção e revisada nas análises críticas (seção 7).

## 4. Autoridade, competências e papéis

A organização define a autoridade e as competências necessárias para a operação dos processos:

| Nível | Papel | Autoridade / responsabilidade |
|---|---|---|
| Direção estratégica | Founder e CEO | Patrocina os processos no nível estratégico; assegura o alinhamento aos objetivos de negócio; recebe o reporte da análise crítica. |
| Direção operacional | COO (Operações) | Responde operacionalmente pelos processos, pelo escritório de portfólio de projetos e pelo Time de Melhoria Contínua; garante recursos; decide impasses operacionais; conduz a análise crítica e reporta ao CEO. |
| Processos | Time de Melhoria Contínua | Define, mantém, verifica e melhora os processos. |
| Projeto | Gerente de Projeto | Conduz o projeto conforme os processos. |
| Execução | Equipes de Engenharia / QA | Executam o trabalho conforme os processos e padrões. |

As competências necessárias a cada papel são desenvolvidas por meio da capacitação (CAP), alinhando os colaboradores aos objetivos da organização.

### 4.1. Competências por papel

A tabela abaixo descreve as competências esperadas de cada papel para a operação dos processos, alinhadas ao objetivo de negócio de crescer com qualidade e previsibilidade:

| Papel | Competências esperadas |
|---|---|
| Founder e CEO | Liderança estratégica; tomada de decisão orientada a resultados; compreensão do negócio e do mercado de software. |
| COO (Operações) | Gestão de operações e portfólio; leitura de indicadores de processo; tomada de decisão baseada em dados; gestão de pessoas e recursos. |
| Time de Melhoria Contínua | Conhecimento do modelo MPS-SW e dos processos da Timeware; análise e melhoria de processos; elaboração de planos e documentação; facilitação de grupos. |
| Gerente de Projeto | Planejamento e controle de projetos; gestão de riscos e partes interessadas; comunicação com o cliente; uso das ferramentas (Jira, Confluence); conhecimento dos processos organizacionais. |
| Equipes de Engenharia / QA | Engenharia de software e/ou qualidade; uso das ferramentas (Git, Azure DevOps, Jira, Xray); seguimento dos processos e padrões; colaboração em equipe. |

O desenvolvimento dessas competências é planejado e acompanhado conforme o Plano de Capacitação (PLA-CAP-001).

### 4.2. Matriz RACI das atividades-chave de governança

A matriz abaixo indica a responsabilidade de cada papel nas principais atividades de governança dos processos. Legenda: **R** = Responsável pela execução · **A** = Autoridade (aprova/decide) · **C** = Consultado · **I** = Informado.

| Atividade | CEO | COO | TMC | GP | Equipes |
|---|---|---|---|---|---|
| Definir e manter processos-padrão | I | A | R | C | I |
| Garantir recursos para os processos | A | R | C | — | — |
| Conduzir análise crítica dos processos | I | R/A | C | I | — |
| Verificar aderência dos projetos (GQA) | — | I | R | C | C |
| Planejar e conduzir capacitação | I | A | C | C | — |
| Priorizar e implementar melhorias | A | R | R | C | C |
| Gerenciar portfólio e alocar recursos | I | R/A | C | C | — |

## 5. Riscos e oportunidades organizacionais

A Timeware gerencia riscos e oportunidades de natureza organizacional — que afetam a empresa além de um projeto isolado, como concorrência de recursos entre projetos do portfólio, dependência de pessoas-chave e riscos de negócio.

Esses riscos são tratados conforme a Estratégia de Gerência de Riscos e Oportunidades (EST-GPC-002), com acompanhamento pela direção e pelo Time de Melhoria Contínua. Riscos de maior exposição são levados à análise crítica pela direção.

## 6. Informações de governança e medidas organizacionais

A direção identifica e utiliza informações de governança para acompanhar o desempenho da organização e dos seus processos. As principais fontes são:

- **medidas organizacionais**, coletadas e analisadas conforme o Plano de Medição (MED) — por exemplo, indicadores de prazo, qualidade, defeitos e retrabalho consolidados entre projetos;
- **resultados das verificações** da Garantia da Qualidade (EST-GPC-001);
- **situação do portfólio** de projetos.

Essas informações são consolidadas e usadas como base para as decisões da direção e para a análise crítica.

## 7. Análise crítica pela direção

A direção da Timeware realiza, **trimestralmente**, uma **análise crítica dos processos**, com o objetivo de verificar se eles continuam alinhados aos objetivos de negócio e se estão produzindo os resultados esperados.

A análise crítica é **conduzida pelo COO** (direção operacional), que a **reporta ao CEO**, e considera:

- o desempenho dos processos (medidas organizacionais);
- os resultados das verificações da Garantia da Qualidade;
- o andamento das melhorias de processo;
- os riscos organizacionais de maior exposição;
- a adequação dos recursos alocados aos processos.

As decisões e encaminhamentos da análise crítica são registrados (ata mantida no Confluence) e acompanhados pelo Time de Melhoria Contínua. Quando a análise identifica desalinhamento, são definidas ações de ajuste — nos processos, nos recursos ou nos próprios objetivos.

## 8. Documentos relacionados

- POL-ORG-001 — Política Organizacional de Processos
- PRO-GPC-002 — Definição do Time de Melhoria Contínua
- EST-GPC-001 — Estratégia de Garantia da Qualidade
- EST-GPC-002 — Estratégia de Gerência de Riscos e Oportunidades
- PLA-GPC-001 — Plano de Gestão e Melhoria de Processos
- Plano de Medição (MED) e Plano de Capacitação (CAP)
- PRO-OSW-002 — Gestão de Portfólio de Projetos

## 9. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados **OSW 2 a OSW 7** do processo **Gerência Organizacional de Software (OSW)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| OSW 2 — recursos e treinamento garantidos pela gerência | Seção 3 |
| OSW 3 — informações de governança identificadas e usadas | Seção 6 |
| OSW 4 — autoridade, responsabilidades e competências definidas e alinhadas aos objetivos | Seção 4 |
| OSW 5 — riscos e oportunidades organizacionais geridos | Seção 5 |
| OSW 6 — coleta, análise e uso de medidas organizacionais garantidos | Seção 6 |
| OSW 7 — alinhamento dos processos aos objetivos garantido (análise crítica) | Seção 7 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.3 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Wilson Yamada |
| 1.0 | 27/08/2025 | Time de Melhoria Contínua | Definição inicial da governança organizacional de processos |
| 1.1 | 24/11/2025 | Time de Melhoria Contínua | Inclusão da camada COO na autoridade; análise crítica conduzida pelo COO com reporte ao CEO |
| 1.2 | 12/03/2026 | Time de Melhoria Contínua | Adição da tabela de competências por papel (§4.1) e da matriz RACI das atividades-chave de governança (§4.2) |
