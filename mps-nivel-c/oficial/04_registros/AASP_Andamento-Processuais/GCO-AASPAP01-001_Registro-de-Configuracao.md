# Registro de Gerência de Configuração — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | GCO-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto / Responsável GCO** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GCO (evidência de projeto) |

---

## 1. Objetivo

Registrar o gerenciamento de configuração do projeto: itens de configuração (ICs), estratégia de controle de versão, baselines e gestão de mudanças. Conforme ADAP-AASPAP01-001, o papel de responsável por GCO foi acumulado pelo Gerente de Projeto (Cezar Hiraki Velazquez), dada a maturidade do controle de versão via Azure DevOps e GitFlow.

## 2. Estratégia de gerência de configuração

| Item | Descrição |
|---|---|
| Plataforma | Azure DevOps (controle de versão e pipeline CI/CD) |
| Modelo de branching | GitFlow — `feature/*` e `bugfix/*` → `develop`; `release` → `main`; `hotfix/*` a partir de `main` |
| Convenção de tags | Numeração sequencial de versão (ex.: `v240`, referenciada nas atividades de GMUD) |
| Aprovação de PR | Mínimo 1 revisor além do autor para merge de `feature`/`bugfix` em `develop` |
| Gestão de segredos | Credenciais das APIs parceiras e da fila centralizadas em configuração protegida, sem exposição em logs (RNF-02) |
| Documentação | Scripts de banco (DDL) e contratos do webhook multi-fonte versionados no Azure DevOps |

## 3. Itens de configuração (ICs)

| ID | Tipo | Descrição | Repositório / Localização |
|---|---|---|---|
| IC-01 | Código-fonte (.NET) | API AndamentosProcessuais (webhook multi-fonte, controle de movimentações) | Azure DevOps — repositório AndamentosProcessuais |
| IC-02 | Código-fonte (.NET) | CapturaServer (publicação na fila WorkerAndamentos / SegmentoTribunal) | Azure DevOps — repositório AndamentosProcessuais |
| IC-03 | Banco de dados | Scripts DDL / migrations (Observacao, Segredo, CodigoFonteAPI) | Azure DevOps — pasta `/db` do repositório correspondente |
| IC-04 | Artefato de implantação | Pacotes de publicação (GMUD) | Servidor de artefatos interno |
| IC-05 | Documentação técnica | Contratos do webhook multi-fonte e integração com APIs parceiras | Azure DevOps — pasta `/docs` |
| IC-06 | Artefato de gestão | Planilha de gestão (backlog, sprints, tarefas) — base para carga no Jira | GEST-AASPAP01_Planilha-de-Gestao-do-Projeto.xlsx |

## 4. Baselines estabelecidas

| ID | Descrição | Referência | Componentes |
|---|---|---|---|
| BL-LEGADO | Baseline inicial da solução legada (ponto de partida da refatoração) | `v220` (referenciada nas atividades de GMUD) | IC-01, IC-02 |
| BL-WEBHOOK | Baseline de publicação do webhook EPROC/ESAJ e fila RabbitMQ (Fases 1–2) | `v230` (referenciada nas atividades de GMUD) | IC-01, IC-02, IC-03 |
| BL-CNJ | Baseline de publicação da refatoração multi-fonte CNJ e tratamento de erros (Fases 3–4) | `v240` (referenciada nas atividades de GMUD) | IC-01, IC-02, IC-03 |
| BL-HOTFIX | Correção pós-implantação aplicada em `main` (nullabilidade em CapturaLogin sob carga) | `v241` (referenciada nas atividades de GMUD) | IC-01 |

> A baseline de encerramento será registrada no fechamento do projeto (Fase 5 — implantação).

## 5. Gestão de mudanças

- Mudanças de escopo/arquitetura são formalizadas em reuniões de alinhamento registradas como atividades no ClickUp (participantes, data, decisões e impacto).
- O escopo adicional de homologação EPROC/ESAJ e devolutiva aos associados foi acordado formalmente com o cliente — formalizado em CR-AASPAP01-001.
- O escopo adicional da Fase 4 (campos Observacao, Segredo e CodigoFonteAPI e tratamentos de erro por instância) foi acordado com o cliente — formalizado em CR-AASPAP01-002.
- A implantação em produção segue o rito de GMUD: montagem de pacote, validação em homologação e agendamento com a Infraestrutura.

## 6. Auditoria de configuração

| Item verificado | Resultado | Observação |
|---|---|---|
| ICs versionados no Azure DevOps | Conforme | IC-01 a IC-03 no repositório; IC-05 em `/docs` |
| Baseline de publicação identificada por tag | Conforme | `v230` e `v240` referenciadas nas atividades de GMUD |
| Credenciais/segredos não expostos em logs | Conforme | Configuração protegida das parceiras e da fila (RNF-02) |
| Merges revisados antes da integração | Conforme | PR com no mínimo 1 revisor além do autor |

> A auditoria de configuração de encerramento será registrada no fechamento do projeto.

---


## Evidências

- `devops_andamentos_branches.png` — GitFlow no Azure DevOps — branches do AndamentosProcessuais
- `devops_andamentos_commits.png` — Histórico de commits (Azure DevOps)
- `devops_andamentos_tags.png` — Tags de baseline (v220/v230/v240/v241)
- `devops_andamentos_estrutura.png` — Estrutura do repositório AndamentosProcessuais
- `estrutura_andamentosProcessuais.png` — Estrutura da solução AndamentosProcessuais
- `devops_andamentos_pipeline_ci.png` — Pipeline CI
- `devops_andamentos_pipeline_cicd.png` — Pipeline CI/CD

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de configuração consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais. |
