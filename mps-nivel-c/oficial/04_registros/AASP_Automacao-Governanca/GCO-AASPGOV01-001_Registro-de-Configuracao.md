# Registro de Gerência de Configuração — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | GCO-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |
| **Gerente de Projeto / Responsável GCO** | Abraão Oliveira |
| **Processo MPS-SW** | GCO (evidência de projeto) |

---

## 1. Objetivo

Registrar o gerenciamento de configuração do projeto AASP_Automacao-Governanca: itens de configuração (ICs), estratégia de controle de versão, baselines estabelecidas, gestão de mudanças e auditoria de configuração. Conforme ADAP-AASPGOV01-001, o papel de responsável por GCO foi acumulado pelo Gerente de Projeto (Abraão Oliveira), dada a maturidade do controle de versão via Azure DevOps com GitFlow e o porte do projeto. O controle de configuração abrange código-fonte, configuração, artefatos de implantação e documentação de gestão do projeto.

## 2. Estratégia de gerência de configuração

| Item | Descrição |
|---|---|
| Plataforma | Azure DevOps — controle de versão Git e pipeline CI/CD para validação de PRs |
| Modelo de branching | GitFlow: `feature/*` e `bugfix/*` integradas em `develop`; `develop` promovida a `main` nas baselines de publicação |
| Convenção de tags | Versionamento semântico: `v0.9.0` (desenvolvimento concluído), `v1.0.0-rc.1` (homologação aprovada), `v1.0.0` (produção) |
| Aprovação de PR | Merge em `develop` exige revisão e aprovação de no mínimo 1 membro da equipe além do autor (conforme REV-AASPGOV01-001) |
| Gestão de segredos | `appsettings.json` mantido fora do repositório; credenciais de acesso às APIs Sensr e Jira armazenadas de forma segura no ambiente Azure, sem exposição em logs de execução (RNF05) |
| Documentação | Artefatos de gestão (planilha IC-06) versionados no repositório do projeto |

## 3. Itens de configuração (ICs)

| ID | Tipo | Descrição | Repositório / Localização |
|---|---|---|---|
| IC-01 | Código-fonte (.NET 8) | SensrJiraSync.Core — contratos, modelos de domínio, mapeadores e configurações | Azure DevOps — repositório SensrJiraSync |
| IC-02 | Código-fonte (.NET 8) | SensrJiraSync.Infrastructure — serviços de integração (SensrService, JiraService, SyncService, HtmlHelper) | Azure DevOps — repositório SensrJiraSync |
| IC-03 | Código-fonte (.NET 8) | SensrJiraSync.App — ponto de entrada, composição de DI e bootstrap da execução | Azure DevOps — repositório SensrJiraSync |
| IC-04 | Arquivo de configuração | appsettings.json — configuração de desenvolvedores, projetos e credenciais de acesso às APIs | Gerenciado fora do repositório; fornecido ao Azure de forma segura (RNF05) |
| IC-05 | Artefato de implantação | Executável .NET 8 auto-contido publicado para o Azure Scheduler | Azure — ambiente de hospedagem do Scheduled Job (baseline BL-PROD-001) |
| IC-06 | Artefato de gestão | Planilha de gestão do projeto — backlog, tarefas e acompanhamento | GEST-AASPGOV01_Planilha-de-Gestao-do-Projeto.xlsx |

## 4. Baselines estabelecidas

| ID | Descrição | Referência | Componentes |
|---|---|---|---|
| BL-DEV-001 | Baseline de desenvolvimento concluído — fim da Fase 3, antes do início da homologação | Tag `v0.9.0` no Azure DevOps | IC-01, IC-02, IC-03 |
| BL-HOM-001 | Baseline de homologação aprovada — após correção dos BUG-01 a BUG-05 e aprovação dos CT-01 a CT-05 | Tag `v1.0.0-rc.1` no Azure DevOps | IC-01, IC-02, IC-03, IC-04 |
| BL-PROD-001 | Baseline de produção — encerramento formal do projeto em 02/06/2026, artefato implantado no Azure Scheduler | Tag `v1.0.0` no Azure DevOps | IC-01, IC-02, IC-03, IC-04, IC-05 |

## 5. Gestão de mudanças

Mudanças de escopo e de arquitetura foram formalizadas por alinhamento entre o time durante as reuniões registradas nas atas ATA-AASPGOV01-001 a ATA-AASPGOV01-003. Decisões técnicas com impacto arquitetural foram registradas no GDE-AASPGOV01-001 (D01–D07).

Não houve Change Request durante a execução do projeto — o escopo permaneceu estável desde o Kickoff até o encerramento (02/06/2026).

A implantação em produção seguiu o seguinte rito: (1) validação do executável publicado em ambiente de homologação contra as APIs Sensr e Jira reais; (2) geração da baseline BL-PROD-001 com tag `v1.0.0`; (3) substituição manual do artefato anterior no Azure Scheduler; (4) verificação do agendamento e da execução bem-sucedida pós-implantação; (5) emissão do TAE-AASPGOV01-001 pelo Sponsor em 02/06/2026.

## 6. Auditoria de configuração

| Item verificado | Resultado | Observação |
|---|---|---|
| ICs versionados no Azure DevOps | Conforme | IC-01, IC-02 e IC-03 nos repositórios SensrJiraSync; histórico de commits rastreável por branch e PR |
| appsettings.json fora do repositório | Conforme | IC-04 gerenciado externamente ao Git; ausente do `.gitignore` confirmado; credenciais não expostas no repositório (RNF05) |
| Baselines de publicação identificadas por tag | Conforme | BL-DEV-001 (`v0.9.0`), BL-HOM-001 (`v1.0.0-rc.1`) e BL-PROD-001 (`v1.0.0`) versionadas no Azure DevOps |
| Tokens e segredos não expostos em logs de execução | Conforme | API Tokens Sensr (JWT) e Jira (Basic Auth) armazenados fora do código-fonte; logging estruturado não registra tokens ou credenciais (RNF05) |
| Merges revisados antes da integração em develop | Conforme | Todos os PRs de feature/* e bugfix/* aprovados por no mínimo 1 revisor além do autor antes do merge (REV-AASPGOV01-001) |
| Planilha de gestão (IC-06) sob controle | Conforme | GEST-AASPGOV01_Planilha-de-Gestao-do-Projeto.xlsx versionada no repositório do projeto |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Registro de gerência de configuração consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0. |
