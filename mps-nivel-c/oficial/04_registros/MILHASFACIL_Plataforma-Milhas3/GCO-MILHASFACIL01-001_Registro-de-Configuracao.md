# Registro de Gerência de Configuração — Milhas3

| Campo | Valor |
|---|---|
| **Documento** | GCO-MILHASFACIL01-001 — Registro de Gerência de Configuração |
| **Versão** | 1.0 |
| **Data** | 02/06/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Responsável GCO** | Caroline Sousa |
| **Processo MPS-SW** | GCO — Gerência de Configuração |

---

## 1. Itens de configuração (ICs)

| ID | Item de configuração | Localização | Responsável |
|---|---|---|---|
| IC-01 | Código-fonte back-end (Java / Spring Boot + Selenium) | Azure DevOps — repositório `milhas3-backend` | Henry Komatsu |
| IC-02 | Código-fonte front-end (Angular) | Azure DevOps — repositório `milhas3-frontend` | Beatriz Nunes |
| IC-03 | Scripts de migração de banco (Flyway) | Diretório `src/main/resources/db/migration` no IC-01 | Henry Komatsu |
| IC-04 | Scripts de infraestrutura e deploy (shell scripts, Nginx config) | Azure DevOps — repositório `milhas3-infra` | Henry Komatsu |
| IC-05 | Documentação MPS-SW (este repositório) | Azure DevOps — repositório `mps-repository` | Abraão Oliveira |
| IC-06 | Variáveis de ambiente e secrets de produção | Azure DevOps — Variable Groups (criptografados) | Abraão Oliveira |
| IC-07 | Pipeline de CI/CD (YAML) | Versionado dentro dos repositórios IC-01, IC-02 e IC-04 | Henry Komatsu |

## 2. Estratégia de branching

| Branch | Propósito | Política de merge |
|---|---|---|
| `main` | Código de produção (tag de release) | Somente via PR aprovado + pipeline CI/CD verde + aprovação do Tech Lead |
| `develop` | Integração contínua de features | PR aprovado por ao menos 1 revisor + CI verde |
| `feature/*` | Desenvolvimento de funcionalidades | PR para `develop`; aprovação de 1 revisor; link obrigatório com User Story do Azure DevOps Boards |
| `hotfix/*` | Correções críticas em produção | PR direto para `main` + `develop`; aprovação do Tech Lead |
| `release/*` | Preparação de entregas ao cliente (homologação) | Branching a partir de `develop`; merge em `main` após aceite formal |

## 3. Política de versionamento de código

- **Tags de release:** `v{MAIOR}.{MENOR}.{PATCH}` (ex.: `v1.0.0`)
- **Mensagem de commit:** formato Conventional Commits — `tipo(escopo): descrição` (ex.: `feat(scraping): adiciona suporte a LATAM Pass`)
- **Pull Requests:** obrigatórios para merge em `develop` e `main`; link com User Story ou Bug do Azure DevOps Boards obrigatório; pipeline CI/CD deve estar verde antes do merge

## 4. Baselines e controle de mudanças

| Baseline | Descrição | Data | Referência |
|---|---|---|---|
| BL-01 | Aprovação do Plano de Projeto | 16/05/2025 | PLA-MILHASFACIL01-001 v1.0 |
| BL-02 | Arquitetura base definida e repositórios criados | 02/06/2025 | PCP-MILHASFACIL01-001 v1.0 |
| BL-03 | Motor de rastreamento operacional (5 programas) | 25/07/2025 | Sprint 4 concluída |
| BL-04 | Build de homologação (`release/homolog`) | 06/10/2025 | Branch `release/homolog` criado |
| BL-05 | Build de produção — aceite formal | 16/11/2025 | Tag `v1.0.0` criada após ATA-MILHASFACIL01-002 |

Mudanças após BL-01 que alterem escopo, prazo ou equipe seguem o fluxo de Change Request (documentadas como CR no projeto).

## 5. Auditorias de configuração

| Auditoria | Data | Responsável | Resultado |
|---|---|---|---|
| Verificação de estrutura de branches e PR policy no Azure DevOps | 02/06/2025 | Caroline Sousa | Conforme — política configurada e validada |
| Verificação de ausência de secrets no repositório (scan de credenciais) | 06/10/2025 | Caroline Sousa | Conforme — secrets exclusivamente em Variable Groups; nenhuma credencial no código |
| Verificação de tag de release pós-aceite | 16/11/2025 | Caroline Sousa | Conforme — tag `v1.0.0` criada e validada |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2025 | Time de Melhoria Contínua | Documento inicial |
