# Registro de Gerencia de Configuracao — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | GCO-AASP01-001 |
| **Projeto** | Grupos de Usuarios — AASP Gerenciador |
| **Cliente** | AASP — Associacao dos Advogados de Sao Paulo |
| **Versao** | 1.0 |
| **Data** | 26/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GCO (evidencia de projeto) |

---

## 1. Objetivo

Estabelecer e registrar a estrategia de gerencia de configuracao adotada no projeto AASP01 — Grupos de Usuarios (ms.auxo.gruposusuarios), identificando os itens de configuracao (ICs), as baselines estabelecidas, os mecanismos de controle de mudancas e os procedimentos de auditoria de configuracao.

Este documento cobre toda a vida util do projeto, desde a baseline inicial (BL-01, TAP aprovado em 19/05/2026) ate o encerramento previsto em 11/07/2026. E mantido e atualizado pelo responsavel de GCO (Cézar Velázquez) a cada evento relevante de configuracao.

---

## 2. Estrategia de gerencia de configuracao

| Item | Descricao |
|---|---|
| **Repositorio de codigo** | Azure DevOps · organizacao komatsuhenry67 · projeto gerenciador-aasp · repositorio ms.auxo.gruposusuarios. Acesso restrito aos membros da equipe do projeto (Renan Kioshi, Henry Komatsu e Mateus Veloso — Timeware; acesso somente-leitura para Marcos Turnes e Leonardo Francisco Pereira — AASP). |
| **Estrategia de branching** | Git Flow: `main` (producao, protegido — merge somente via release/*), `develop` (integracao continua), `feature/ag-{id}` (desenvolvimento de requisito individual, ex: feature/ag-20), `release/sprint-N` (preparacao de entrega por sprint). Nenhum commit direto em main ou develop. |
| **Tags de baseline** | Tags semanticas apos aceite formal de sprint: `sprint-N-aceite` (ex: sprint-1-aceite — 06/06/2026). Tags imutaveis criadas pelo GP apos recebimento da ata de aceite assinada pelo PO cliente. |
| **Gate de merge (CI)** | Pipeline Azure DevOps obrigatorio antes de qualquer merge em develop ou main: (1) build sem erros, (2) todos os testes unitarios passando, (3) analise estatica sem violacoes bloqueantes. PRs com pipeline vermelho sao bloqueados automaticamente. |
| **Aprovacao de Pull Request** | Minimo de 1 revisor aprovado; Cézar Velázquez e revisor principal de todos os PRs de codigo critico. PRs squash-merged apos aprovacao para manter historico linear em develop. |
| **Segredos e dados sensiveis** | Connection strings (auxo3 e temis3), chaves JWT e credenciais de servico nunca commitadas no repositorio. Gerenciadas via variaveis de ambiente no servidor de aplicacao (IIS / Azure App Service). Arquivos appsettings.*.json versionados somente com placeholders (`${DB_CONNECTION_STRING}`). |
| **Documentacao MPS-SW** | Artefatos de processo versionados no repositorio MPS Timeware (separado do repositorio de codigo). Convencao de nome: SIGLA-AASP01-NNN_Descricao.{docx|xlsx|md}. Versao controlada pelo cabecalho de cada documento. |

---

## 3. Itens de configuracao (ICs)

| ID | Tipo | Descricao | Repositorio / Localizacao | Convencao de versao | Status atual |
|---|---|---|---|---|---|
| IC-01 | Codigo-fonte | API ms.auxo.gruposusuarios — .NET Framework 4.7.2 / Dapper / SQL Server. Inclui controllers, services, repositories, models e testes unitarios. | Azure DevOps: komatsuhenry67/gerenciador-aasp/ms.auxo.gruposusuarios | Tags sprint-N-aceite; branches por Git Flow | Baseline BL-02 (tag sprint-1-aceite, 06/06/2026); Sprint 2 em desenvolvimento em feature branches |
| IC-02 | Scripts SQL | Migrations do banco auxo3: criacao das tabelas Grupos, PermissoesGrupo, UsuariosGrupo e AuditoriaGrupos. Scripts idempotentes, aplicados em ordem sequencial. | /sql/migrations/ no repositorio ms.auxo.gruposusuarios | Numeracao sequencial (001_criar_grupos.sql, 002_criar_permissoes.sql, 003_criar_usuarios_grupo.sql, ...) | 3 migrations aplicadas e validadas (Sprint 1); migration 004 (AuditoriaGrupos) prevista para Sprint 2 |
| IC-03 | Pipeline CI/CD | Arquivo azure-pipelines.yml define etapas de build, teste unitario e analise estatica. Versionado junto ao codigo-fonte. | Raiz do repositorio: /azure-pipelines.yml | Versionado com o codigo (sem versao propria) | Ativo; executado em todo PR aberto para develop ou main |
| IC-04 | Configuracao de ambiente | Arquivos appsettings.json, appsettings.Development.json e appsettings.Production.json com configuracoes estruturais (sem valores sensiveis). Variaveis sensiveis injetadas via ambiente. | /src/ms.auxo.gruposusuarios/appsettings/ | Versionado com o codigo | Ativo; appsettings.Production.json atualizado no inicio da Sprint 2 para apontar ao ambiente AASP |
| IC-05 | Documentacao MPS-SW | Pacote completo de artefatos do processo MPS-SW para o projeto AASP01: TAP, PLA, REQ, PCP, GCO, ADAP, GDE, ITP, VV, CTQ, REL-VV, RAC, ATA, CR, RASTR, MED, GEST e REV. Total: 19 artefatos (18 .docx + 1 .xlsx). | Repositorio MPS Timeware: /mps-nivel-c/oficial/04_registros/AASP_Gerenciador/AASP01_Grupos-Usuarios/ | Versao por documento (cabecalho); baselinado em conjunto com o codigo a cada sprint aceita | 19 artefatos presentes; BL-02 inclui versoes de todos os documentos S1 |
| IC-06 | Documentacao de API | Especificacao OpenAPI/Swagger gerada automaticamente pelo Swashbuckle a partir das anotacoes do codigo-fonte. Disponivel no endpoint /swagger em runtime. | Endpoint /swagger (runtime); nao versionada separadamente — derivada do IC-01 | Vinculada ao codigo (IC-01); versao da API no cabecalho HTTP (v1) | Validada ao final da Sprint 1; todos os 8 endpoints implementados documentados |

---

## 4. Baselines estabelecidas

| ID Baseline | Data | Evento desencadeador | Itens de configuracao incluidos | Aprovador |
|---|---|---|---|---|
| BL-01 | 19/05/2026 | TAP aprovado — inicio formal do projeto | IC-01 (repositorio criado, commit inicial vazio), IC-05 (TAP-AASP01-001, PLA-AASP01-001, REQ-AASP01-001 em versao inicial) | Abraão Oliveira (Timeware) + Marcos Turnes (AASP) |
| BL-02 | 06/06/2026 | Aceite formal da Sprint 1 por Marcos Turnes (ATA-AASP01-002) | IC-01 (tag sprint-1-aceite no Azure DevOps; PRs #11, #12, #13, #14, #15 merged em main), IC-02 (3 migrations aplicadas no banco auxo3), IC-03 (azure-pipelines.yml v1), IC-04 (appsettings validados), IC-05 (todos os artefatos MPS-SW da Sprint 1), IC-06 (Swagger v1 validado) | Marcos Turnes — aceite formal (PO AASP) + Cézar Velázquez — aprovacao tecnica (Timeware) |

**Proxima baseline prevista:** BL-03 — apos aceite formal da Sprint 2 (previsto para 20/06/2026), incluindo IC-01 (tag sprint-2-aceite), IC-02 (migration 004 para AuditoriaGrupos), e atualizacoes de IC-05 (artefatos revisados na S2).

---

## 5. Auditoria de configuracao

**Situacao atual (15/06/2026):** Baseline BL-02 valida e integra. Sprint 2 em desenvolvimento ativo em feature branches (feature/ag-23 e feature/ag-24) no repositorio develop. Nenhuma violacao de configuracao identificada. Proxima baseline (BL-03) sera estabelecida apos aceite formal da Sprint 2, previsto para 20/06/2026.

| Data | Tipo de auditoria | O que foi verificado | Resultado | Responsavel |
|---|---|---|---|---|
| 19/05/2026 | Auditoria de baseline inicial (BL-01) | Criacao do repositorio no Azure DevOps; estrutura de branches (main, develop) conforme Git Flow; presenca dos artefatos iniciais (TAP, PLA, REQ) no repositorio MPS; permissoes de acesso configuradas corretamente | Aprovado — repositorio criado, branches configurados, artefatos presentes, permissoes corretas | Cézar Velázquez |
| 06/06/2026 | Auditoria de baseline Sprint 1 (BL-02) | Tag sprint-1-aceite criada e imutavel; PRs #11-#15 merged em main com pipeline verde; 3 migrations SQL aplicadas no banco auxo3 (ambiente local e homologacao); 19 artefatos MPS-SW presentes e versionados; Swagger /swagger respondendo com todos os endpoints da Sprint 1 | Aprovado — todos os itens de configuracao presentes e consistentes; tag criada apos recepcao da ATA-AASP01-002 assinada por Marcos Turnes | Cézar Velázquez |
| 15/06/2026 | Auditoria de acompanhamento (meio de Sprint 2) | Verificacao de que feature branches (feature/ag-23, feature/ag-24) estao derivados de develop pos-BL-02; nenhum commit direto em main ou develop; pipeline CI executando em todos os PRs abertos; artefatos MPS-SW da S2 em elaboracao (RAC, ATA planejadas) | Aprovado — branches corretos, historico limpo, pipeline ativo, sem desvios de processo | Cézar Velázquez |

---

## Historico de revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 15/06/2026 | Abraão Oliveira | Versao inicial |
