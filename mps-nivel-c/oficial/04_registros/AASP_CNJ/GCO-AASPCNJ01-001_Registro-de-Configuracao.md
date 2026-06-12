# Registro de Gerência de Configuração — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | GCO-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto / Responsável GCO** | Abraão Oliveira |
| **Processo MPS-SW** | GCO (evidência de projeto) |

---

## 1. Objetivo

Registrar o gerenciamento de configuração do projeto: itens de configuração (ICs), estratégia de controle de versão, baselines e gestão de mudanças. Conforme ADAP-AASPCNJ01-001, o papel de responsável por GCO foi acumulado pelo Gerente de Projeto (Abraão Oliveira), dada a maturidade do controle de versão via Azure DevOps e GitFlow.

## 2. Estratégia de gerência de configuração

| Item | Descrição |
|---|---|
| Plataforma | Azure DevOps (controle de versão e pipeline CI/CD) |
| Modelo de branching | GitFlow — `feature/*` e `bugfix/*` → `develop`; `release` → `main`; `hotfix/*` a partir de `main` |
| Convenção de tags | Numeração sequencial de versão (ex.: `v240`, referenciada nas atividades de GMUD) |
| Aprovação de PR | Mínimo 1 revisor além do autor para merge de `feature`/`bugfix` em `develop` |
| Gestão de segredos | Token Bearer da CNJ centralizado em `PonteAPI`, sem exposição em logs (RNF-05) |
| Documentação | Coleções Postman da API CNJ e scripts de banco versionados no Azure DevOps |

## 3. Itens de configuração (ICs)

| ID | Tipo | Descrição | Repositório / Localização |
|---|---|---|---|
| IC-01 | Código-fonte (.NET) | WorkerAndamentos | Azure DevOps — repositório WorkerAndamentos |
| IC-02 | Código-fonte (.NET) | CapturaServer | Azure DevOps — repositório CapturaServer |
| IC-03 | Código-fonte (.NET) | API AndamentosProcessuais | Azure DevOps — repositório AndamentosProcessuais |
| IC-04 | Banco de dados | Scripts DDL / migrations | Azure DevOps — pasta `/db` do repositório correspondente |
| IC-05 | Artefato de implantação | Pacotes de publicação (GMUD) | Servidor de artefatos interno |
| IC-06 | Documentação de API | Coleções Postman da API CNJ | Azure DevOps — pasta `/docs` |
| IC-07 | Artefato de gestão | Planilha de gestão (backlog, sprints, tarefas) — base para carga no Jira | GEST-AASPCNJ01_Planilha-de-Gestao-do-Projeto.xlsx |

## 4. Baselines estabelecidas

| ID | Descrição | Referência | Componentes |
|---|---|---|---|
| BL-EPROC | Baseline de publicação do fluxo EPROC/ESAJ (pós-Fase 3) | Tag de versão / GMUD (EPROC) | IC-01, IC-02, IC-03 |
| BL-CNJ | Baseline de publicação do fluxo CNJ | `v240` (referenciada nas atividades de GMUD) | IC-01, IC-02, IC-03, IC-04 |

> A baseline de encerramento será registrada no fechamento do projeto (Onda 3).

## 5. Gestão de mudanças

- Mudanças de escopo/arquitetura são formalizadas em reuniões de alinhamento registradas como atividades no ClickUp (participantes, data, decisões e impacto).
- A interrupção do desenvolvimento da captura de 2ª instância no EPROC (card 4462) foi acordada formalmente com o cliente, com retomada planejada — formalizada em CR-AASPCNJ01-001.
- A implantação em produção segue o rito de GMUD: montagem de pacote, validação em homologação e agendamento com a Infraestrutura.

## 6. Auditoria de configuração

| Item verificado | Resultado | Observação |
|---|---|---|
| ICs versionados no Azure DevOps | Conforme | IC-01 a IC-04 nos repositórios; IC-06 em `/docs` |
| Baseline de publicação identificada por tag | Conforme | `v240` referenciada nas atividades de GMUD |
| Token/segredos não expostos em logs | Conforme | Token Bearer centralizado em `PonteAPI` (RNF-05) |
| Merges revisados antes da integração | Conforme | PR com no mínimo 1 revisor além do autor (ver REV-AASPCNJ01-001) |

> A auditoria de configuração de encerramento será registrada no fechamento do projeto.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de configuração consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
