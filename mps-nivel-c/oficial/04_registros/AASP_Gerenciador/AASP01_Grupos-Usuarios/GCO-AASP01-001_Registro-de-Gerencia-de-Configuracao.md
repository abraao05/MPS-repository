# Registro de Gerência de Configuração — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | GCO-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 26/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GCO (evidência de projeto) |

---

## 1. Objetivo

Estabelecer e registrar a estratégia de gerência de configuração adotada no projeto AASP01 — Grupos de Usuários (ms.auxo.gruposusuarios), identificando os itens de configuração (ICs), as baselines estabelecidas, os mecanismos de controle de mudanças e os procedimentos de auditoria de configuração.

Este documento cobre toda a vida útil do projeto, desde a baseline inicial (BL-01, TAP aprovado em 19/05/2026) até o encerramento previsto em 11/07/2026. E mantido e atualizado pelo responsável de GCO (Cézar Velázquez) a cada evento relevante de configuração.

---

## 2. Estratégia de gerência de configuração

| Item | Descrição |
|---|---|
| **Repositório de código** | Azure DevOps · organização komatsuhenry67 · projeto gerenciador-aasp · repositório ms.auxo.gruposusuarios. Acesso restrito aos membros da equipe do projeto (Renan Kioshi, Henry Komatsu e Mateus Veloso — Timeware; acesso somente-leitura para Marcos Turnes e Leonardo Francisco Pereira — AASP). |
| **Estratégia de branching** | Git Flow: `main` (produção, protegido — merge somente via release/*), `develop` (integração continua), `feature/ag-{id}` (desenvolvimento de requisito individual, ex: feature/ag-20), `release/sprint-N` (preparação de entrega por sprint). Nenhum commit direto em main ou develop. |
| **Tags de baseline** | Tags semânticas após aceite formal de sprint: `sprint-N-aceite` (ex: sprint-1-aceite — 06/06/2026). Tags imutáveis criadas pelo GP após recebimento da ata de aceite assinada pelo PO cliente. |
| **Gate de merge (CI)** | Pipeline Azure DevOps obrigatório antes de qualquer merge em develop ou main: (1) build sem erros, (2) todos os testes unitários passando, (3) análise estática sem violações bloqueantes. PRs com pipeline vermelho são bloqueados automaticamente. |
| **Aprovação de Pull Request** | Mínimo de 1 revisor aprovado; Cézar Velázquez e revisor principal de todos os PRs de código crítico. PRs squash-merged após aprovação para manter histórico linear em develop. |
| **Segredos e dados sensíveis** | Connection strings (auxo3 e temis3), chaves JWT e credenciais de serviço nunca commitadas no repositório. Gerenciadas via variáveis de ambiente no servidor de aplicação (IIS / Azure App Service). Arquivos appsettings.*.json versionados somente com placeholders (`${DB_CONNECTION_STRING}`). |
| **Documentação MPS-SW** | Artefatos de processo versionados no repositório MPS Timeware (separado do repositório de código). Convenção de nome: SIGLA-AASP01-NNN_Descricao.{docx|xlsx|md}. Versão controlada pelo cabecalho de cada documento. |

---

## 3. Itens de configuração (ICs)

| ID | Tipo | Descrição | Repositório / Localização | Convenção de versão | Status atual |
|---|---|---|---|---|---|
| IC-01 | Código-fonte | API ms.auxo.gruposusuarios — .NET Framework 4.7.2 / Dapper / SQL Server. Inclui controllers, services, repositories, models e testes unitários. | Azure DevOps: komatsuhenry67/gerenciador-aasp/ms.auxo.gruposusuarios | Tags sprint-N-aceite; branches por Git Flow | Baseline BL-02 (tag sprint-1-aceite, 06/06/2026); Sprint 2 em desenvolvimento em feature branches |
| IC-02 | Scripts SQL | Migrations do banco auxo3: criação das tabelas Grupos, PermissoesGrupo, UsuariosGrupo e AuditoriaGrupos. Scripts idempotentes, aplicados em ordem sequencial. | /sql/migrations/ no repositório ms.auxo.gruposusuarios | Numeração sequencial (001_criar_grupos.sql, 002_criar_permissoes.sql, 003_criar_usuarios_grupo.sql, ...) | 3 migrations aplicadas e validadas (Sprint 1); migration 004 (AuditoriaGrupos) prevista para Sprint 2 |
| IC-03 | Pipeline CI/CD | Arquivo azure-pipelines.yml define etapas de build, teste unitário e análise estática. Versionado junto ao código-fonte. | Raiz do repositório: /azure-pipelines.yml | Versionado com o código (sem versão própria) | Ativo; executado em todo PR aberto para develop ou main |
| IC-04 | Configuração de ambiente | Arquivos appsettings.json, appsettings.Development.json e appsettings.Production.json com configurações estruturais (sem valores sensíveis). Variáveis sensíveis injetadas via ambiente. | /src/ms.auxo.gruposusuarios/appsettings/ | Versionado com o código | Ativo; appsettings.Production.json atualizado no início da Sprint 2 para apontar ao ambiente AASP |
| IC-05 | Documentação MPS-SW | Pacote completo de artefatos do processo MPS-SW para o projeto AASP01: TAP, PLA, REQ, PCP, GCO, ADAP, GDE, ITP, VV, CTQ, REL-VV, RAC, ATA, CR, RASTR, MED, GEST e REV. Total: 19 artefatos (18 .docx + 1 .xlsx). | Repositório MPS Timeware: /mps-nível-c/oficial/04_registros/AASP_Gerenciador/AASP01_Grupos-Usuarios/ | Versão por documento (cabecalho); baselinado em conjunto com o código a cada sprint aceita | 19 artefatos presentes; BL-02 inclui versões de todos os documentos S1 |
| IC-06 | Documentação de API | Especificação OpenAPI/Swagger gerada automaticamente pelo Swashbuckle a partir das anotações do código-fonte. Disponível no endpoint /swagger em runtime. | Endpoint /swagger (runtime); não versionada separadamente — derivada do IC-01 | Vinculada ao código (IC-01); versão da API no cabecalho HTTP (v1) | Validada ao final da Sprint 1; todos os 8 endpoints implementados documentados |

---

## 4. Baselines estabelecidas

| ID Baseline | Data | Evento desencadeador | Itens de configuração incluidos | Aprovador |
|---|---|---|---|---|
| BL-01 | 19/05/2026 | TAP aprovado — início formal do projeto | IC-01 (repositório criado, commit inicial vazio), IC-05 (TAP-AASP01-001, PLA-AASP01-001, REQ-AASP01-001 em versão inicial) | Abraão Oliveira (Timeware) + Marcos Turnes (AASP) |
| BL-02 | 06/06/2026 | Aceite formal da Sprint 1 por Marcos Turnes (ATA-AASP01-002) | IC-01 (tag sprint-1-aceite no Azure DevOps; PRs #11, #12, #13, #14, #15 merged em main), IC-02 (3 migrations aplicadas no banco auxo3), IC-03 (azure-pipelines.yml v1), IC-04 (appsettings validados), IC-05 (todos os artefatos MPS-SW da Sprint 1), IC-06 (Swagger v1 validado) | Marcos Turnes — aceite formal (PO AASP) + Cézar Velázquez — aprovação técnica (Timeware) |

**Próxima baseline prevista:** BL-03 — após aceite formal da Sprint 2 (previsto para 20/06/2026), incluindo IC-01 (tag sprint-2-aceite), IC-02 (migration 004 para AuditoriaGrupos), e atualizações de IC-05 (artefatos revisados na S2).

---

## 5. Auditoria de configuração

**Situação atual (15/06/2026):** Baseline BL-02 valida e integra. Sprint 2 em desenvolvimento ativo em feature branches (feature/ag-23 e feature/ag-24) no repositório develop. Nenhuma violação de configuração identificada. Próxima baseline (BL-03) será estabelecida após aceite formal da Sprint 2, previsto para 20/06/2026.

| Data | Tipo de auditoria | O que foi verificado | Resultado | Responsável |
|---|---|---|---|---|
| 19/05/2026 | Auditoria de baseline inicial (BL-01) | Criação do repositório no Azure DevOps; estrutura de branches (main, develop) conforme Git Flow; presença dos artefatos iniciais (TAP, PLA, REQ) no repositório MPS; permissões de acesso configuradas corretamente | Aprovado — repositório criado, branches configurados, artefatos presentes, permissões corretas | Cézar Velázquez |
| 06/06/2026 | Auditoria de baseline Sprint 1 (BL-02) | Tag sprint-1-aceite criada e imutável; PRs #11-#15 merged em main com pipeline verde; 3 migrations SQL aplicadas no banco auxo3 (ambiente local e homologação); 19 artefatos MPS-SW presentes e versionados; Swagger /swagger respondendo com todos os endpoints da Sprint 1 | Aprovado — todos os itens de configuração presentes e consistentes; tag criada após recepção da ATA-AASP01-002 assinada por Marcos Turnes | Cézar Velázquez |
| 15/06/2026 | Auditoria de acompanhamento (meio de Sprint 2) | Verificação de que feature branches (feature/ag-23, feature/ag-24) estao derivados de develop pós-BL-02; nenhum commit direto em main ou develop; pipeline CI executando em todos os PRs abertos; artefatos MPS-SW da S2 em elaboração (RAC, ATA planejadas) | Aprovado — branches corretos, histórico limpo, pipeline ativo, sem desvios de processo | Cézar Velázquez |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Abraão Oliveira | Versão inicial |
