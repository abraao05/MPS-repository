# Registro de Gerência de Configuração — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | GCO-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.2 |
| **Data** | 24/06/2026 |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | GCO (evidência de projeto) |

---

## 1. Objetivo

Estabelecer e registrar a estratégia de gerência de configuração adotada no projeto AASP01 — Grupos de Usuários (ms.auxo.usuarios), identificando os itens de configuração (ICs), as baselines estabelecidas, os mecanismos de controle de mudanças e os procedimentos de auditoria de configuração.

Este documento cobre toda a vida útil do projeto, desde a baseline inicial (BL-01, TAP aprovado em 19/05/2026) até o encerramento previsto em 11/07/2026. E mantido e atualizado pelo responsável de GCO (Cezar Hiraki) a cada evento relevante de configuração.

---

## 2. Estratégia de gerência de configuração

| Item | Descrição |
|---|---|
| **Repositório de código** | GitLab · grupo aasp · projeto ms.auxo.usuarios (instancia GitLab http://191.234.192.153). Acesso restrito aos membros da equipe do projeto (Renan Kiyoshi, Henry Komatsu e Mateus Veloso — Timeware; acesso somente-leitura para Marcos Turnes e Caroline Sousa — AASP). |
| **Estratégia de branching** | Git Flow (modelo Atlassian): `main` (produção, protegido — recebe merge de `release/*` e `hotfix/*`, com tags), `develop` (integração continua), `feature/ag-{id}` (desenvolvimento de requisito; sai de e retorna a `develop`, ex: feature/ag-20), `release/sprint-N` (preparação de entrega; mescla em `main` com tag e retorna ao `develop`), `hotfix/vX.Y.Z` (correção urgente de produção; sai de `main`, mescla em `main` com nova tag e retorna ao `develop`). Nenhum commit direto em main ou develop. |
| **Tags de baseline** | Versionamento semantico em `main`: a release da sprint gera a tag de aceite `sprint-N-aceite`, equivalente a `vX.Y.0` (ex: sprint-1-aceite = v1.0.0 — 06/06/2026); correções de produção via hotfix geram tag `vX.Y.Z` (ex: v1.0.1). Tags imutaveis criadas após o aceite/correção formal. |
| **Gate de merge (CI)** | Pipeline GitLab CI obrigatório antes de qualquer merge em develop ou main: (1) build sem erros, (2) todos os testes unitarios passando, (3) análise estática sem violações bloqueantes. MRs com pipeline vermelho são bloqueados automaticamente. |
| **Aprovação de Merge Request** | Mínimo de 2 revisores aprovados; Cezar Hiraki e revisor principal de todos os MRs de código critico. MRs squash-merged após aprovação para manter histórico linear em develop. |
| **Segredos e dados sensiveis** | Connection strings (auxo3 e temis3), chaves JWT e credenciais de serviço nunca commitadas no repositório. Gerenciadas via variáveis de ambiente no servidor de aplicação (IIS / servidor de aplicação). Arquivos appsettings.*.json versionados somente com placeholders (`${DB_CONNECTION_STRING}`). |
| **Documentação MPS-SW** | Artefatos de processo versionados no repositório MPS Timeware (separado do repositório de código). Convenção de nome: SIGLA-AASP01-NNN_Descricao.{docx|xlsx|md}. Versão controlada pelo cabeçalho de cada documento. |

---

## 3. Itens de configuração (ICs)

| ID | Tipo | Descrição | Repositório / Localização | Convenção de versão | Status atual |
|---|---|---|---|---|---|
| IC-01 | Código-fonte | API ms.auxo.usuarios — .NET 5.0 (net5.0) / Dapper / SQL Server. Inclui controllers, services, repositories, models e testes unitarios. | GitLab: aasp/ms.auxo.usuarios | Tags sprint-N-aceite; branches por Git Flow | Baseline BL-02 (tag sprint-1-aceite, 06/06/2026); Sprint 2 em desenvolvimento em feature branches |
| IC-02 | Scripts SQL | Migrations do banco auxo3: criação das tabelas grupos_usuarios, grupos_usuarios_vinculos e grupos_usuarios_funcao. Scripts idempotentes, aplicados em ordem sequencial. | /sql/migrations/ no repositório ms.auxo.usuarios | Numeração sequencial (001_criar_grupos_usuarios.sql, 002_criar_grupos_usuarios_vinculos.sql, 003_criar_grupos_usuarios_funcao.sql, ...) | 3 migrations aplicadas e validadas (Sprint 1); migration de auditoria prevista para Sprint 2 |
| IC-03 | Pipeline CI/CD | Arquivo .gitlab-ci.yml define etapas de build, teste unitario e análise estática. Versionado junto ao código-fonte. | Raiz do repositório: /.gitlab-ci.yml | Versionado com o código (sem versão própria) | Ativo; executado em todo MR aberto para develop ou main |
| IC-04 | Configuração de ambiente | Arquivos appsettings.json, appsettings.Development.json e appsettings.Production.json com configurações estruturais (sem valores sensiveis). Variáveis sensiveis injetadas via ambiente. | /src/ms.auxo.usuarios/appsettings/ | Versionado com o código | Ativo; appsettings.Production.json atualizado no inicio da Sprint 2 para apontar ao ambiente AASP |
| IC-05 | Documentação MPS-SW | Pacote completo de artefatos do processo MPS-SW para o projeto AASP01: TAP, PLA, REQ, PCP, GCO, ADAP, GDE, ITP, VV, CTQ, REL-VV, RAC, ATA, CR, RASTR, MED, GEST e REV. Total: 19 artefatos (18 .docx + 1 .xlsx). | Repositório MPS Timeware: /mps-nível-c/oficial/04_registros/AASP_Gerenciador/AASP01_Grupos-Usuários/ | Versão por documento (cabeçalho); baselinado em conjunto com o código a cada sprint aceita | 19 artefatos presentes; BL-02 inclui versões de todos os documentos S1 |
| IC-06 | Documentação de API | Especificação OpenAPI/Swagger gerada automaticamente pelo Swashbuckle a partir das anotações do código-fonte. Disponível no endpoint /swagger em runtime. | Endpoint /swagger (runtime); não versionada separadamente — derivada do IC-01 | Vinculada ao código (IC-01); versão da API no cabeçalho HTTP (v1) | Validada ao final da Sprint 1; todos os 8 endpoints implementados documentados |

---

## 4. Baselines estabelecidas

| ID Baseline | Data | Evento desencadeador | Itens de configuração incluidos | Aprovador |
|---|---|---|---|---|
| BL-01 | 19/05/2026 | TAP aprovado — inicio formal do projeto | IC-01 (repositório criado, commit inicial vazio), IC-05 (TAP-AASP01-001, PLA-AASP01-001, REQ-AASP01-001 em versão inicial) | Abraão (Timeware) + Marcos Turnes (AASP) |
| BL-02 | 06/06/2026 | Aceite formal da Sprint 1 por Marcos Turnes (ATA-AASP01-002) | IC-01 (tag sprint-1-aceite no GitLab; MRs !1–!5 — entregas da Sprint 1 integradas em `develop`; baseline em `main` pela tag `sprint-1-aceite`), IC-02 (3 migrations aplicadas no banco auxo3), IC-03 (.gitlab-ci.yml v1), IC-04 (appsettings validados), IC-05 (todos os artefatos MPS-SW da Sprint 1), IC-06 (Swagger v1 validado) | Marcos Turnes — aceite formal (PO AASP) + Cezar Hiraki — aprovação técnica (Timeware) |

**Próxima baseline prevista:** BL-03 — após aceite formal da Sprint 2 (previsto para 20/06/2026), incluindo IC-01 (tag sprint-2-aceite), IC-02 (migration 004 para AuditoriaGrupos), e atualizações de IC-05 (artefatos revisados na S2).

---

## 5. Auditoria de configuração

**Situação atual (15/06/2026):** Baseline BL-02 valida e integra. Sprint 2 em desenvolvimento ativo em feature branches (feature/ag-23 e feature/ag-24) no repositório develop. Nenhuma violação de configuração identificada. Próxima baseline (BL-03) será estabelecida após aceite formal da Sprint 2, previsto para 20/06/2026.

| Data | Tipo de auditoria | O que foi verificado | Resultado | Responsável |
|---|---|---|---|---|
| 19/05/2026 | Auditoria de baseline inicial (BL-01) | Criação do repositório no GitLab; estrutura de branches (main, develop) conforme Git Flow; presenca dos artefatos iniciais (TAP, PLA, REQ) no repositório MPS; permissões de acesso configuradas corretamente | Aprovado — repositório criado, branches configurados, artefatos presentes, permissões corretas | Cezar Hiraki |
| 06/06/2026 | Auditoria de baseline Sprint 1 (BL-02) | Tag sprint-1-aceite criada e imutavel; MRs !1–!5 (entregas da Sprint 1, alvo `develop`) com pipeline verde; baseline em `main` pela tag `sprint-1-aceite`; 3 migrations SQL aplicadas no banco auxo3 (ambiente local e homologação); 19 artefatos MPS-SW presentes e versionados; Swagger /swagger respondendo com todos os endpoints da Sprint 1 | Aprovado — todos os itens de configuração presentes e consistentes; tag criada após recepção da ATA-AASP01-002 assinada por Marcos Turnes | Cezar Hiraki |
| 15/06/2026 | Auditoria de acompanhamento (meio de Sprint 2) | Verificação de que feature branches (feature/ag-23, feature/ag-24) estão derivados de develop pos-BL-02; nenhum commit direto em main ou develop; pipeline CI executando em todos os MRs abertos; artefatos MPS-SW da S2 em elaboração (RAC, ATA planejadas) | Aprovado — branches corretos, histórico limpo, pipeline ativo, sem desvios de processo | Cezar Hiraki |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Abraão | Versão inicial |
| 1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o GitLab: política de MR para 2 revisores aprovados (antes 1). |
| 1.2 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
