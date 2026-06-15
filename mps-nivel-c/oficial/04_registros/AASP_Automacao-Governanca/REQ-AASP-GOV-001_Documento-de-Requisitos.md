# Documento de Requisitos — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | REQ-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsáveis** | Cezar Hiraki Velazquez (GP / Tech Lead) |

---

## 1. Contexto e objetivo

A AASP utilizava o Sensr para gerenciamento de projetos e atividades do time de desenvolvimento e decidiu migrar para o Jira de forma gradual, exigindo operação simultânea das duas ferramentas durante a transição. A migração gradual criava três problemas simultâneos que precisavam ser resolvidos sem impacto na operação do time:

- **Volume de dados:** o Sensr acumulava histórico de atividades, subtarefas, descrições e comentários que precisariam ser replicados no Jira com fidelidade, inviabilizando qualquer abordagem manual.
- **Sincronização durante a transição:** enquanto a migração não estivesse completa, as atividades continuariam sendo atualizadas no Sensr; qualquer divergência de status comprometeria a visibilidade do gestor no Jira.
- **Diferenças estruturais entre as plataformas:** Sensr e Jira possuem modelos de dados, formatos de autenticação, estruturas hierárquicas e convenções de status diferentes, exigindo mapeamento e transformação em cada sincronização.

O objetivo é desenvolver o serviço **SensrJiraSync**, que migra atividades do Sensr para o Jira e mantém a sincronização incremental de status durante a transição.

## 2. Objetivos do projeto

- Desenvolver serviço automatizado que migre atividades do Sensr para o Jira, preservando hierarquia, descrição, status, responsáveis, labels, datas e histórico.
- Implementar sincronização incremental de status para cards já migrados.
- Executar a sincronização via Azure Scheduled Job de forma não supervisionada.
- Suportar múltiplos desenvolvedores e projetos com credenciais independentes por desenvolvedor.
- Garantir idempotência: execuções repetidas não criam duplicatas nem sobrescrevem dados corretos.

## 3. Requisitos funcionais

| ID | Origem | Descrição |
|---|---|---|
| RF01 | Migração de dados | O serviço deve autenticar-se no Sensr por desenvolvedor utilizando credenciais individuais e obter a lista de atividades por projeto |
| RF02 | Migração de dados | Para cada projeto no Sensr, o serviço deve criar ou reutilizar um Epic correspondente no Jira, identificado pelo nome do projeto |
| RF03 | Migração de dados | Para cada atividade do Sensr ainda não existente no Jira, o serviço deve criar uma Task com summary no formato `#ID Nome`, preservando descrição, responsável, labels, data de início e status |
| RF04 | Migração de dados | Para cada sub-atividade vinculada a uma atividade do Sensr, o serviço deve criar uma Subtask correspondente no Jira, vinculada à Task pai |
| RF05 | Sincronização | Para cada atividade do Sensr já existente no Jira (identificada pelo `#ID` no summary), o serviço deve verificar se o status mudou e aplicar a transição correspondente no Jira |
| RF06 | Migração de dados | O histórico de alterações da atividade (`description_history`) deve ser migrado como comentários individuais na Task correspondente no Jira |
| RF07 | Transformação de dados | O serviço deve converter HTML da descrição e do histórico do Sensr para texto plano compatível com o formato ADF (Atlassian Document Format) do Jira |
| RF08 | Transformação de dados | O serviço deve mapear os status do Sensr (TODO, DOING, VALIDATION, STOPPED, DONE) para os equivalentes do Jira (To Do, In Progress, To Test, Blocked, Done) |
| RF09 | Transformação de dados | Labels contendo espaços ou caracteres especiais devem ser sanitizados antes da criação no Jira, substituindo espaços e barras por underscore |
| RF10 | Configuração | O serviço deve ser configurável via `appsettings.json`, com suporte a múltiplos desenvolvedores, cada um com credenciais Sensr, ID de usuário Sensr, ID de conta Jira e lista de projetos |
| RF11 | Execução | O serviço deve ser executável como processo isolado, compatível com agendamento via Azure Scheduler, retornando código de saída diferente de zero em caso de falha |

## 4. Requisitos não funcionais

| ID | Categoria | Descrição |
|---|---|---|
| RNF01 | Idempotência | Execuções repetidas não devem criar cards duplicados no Jira; verificação de existência pelo `#ID` no summary antes de qualquer criação |
| RNF02 | Confiabilidade | Falhas na sincronização de um desenvolvedor ou projeto não devem interromper o processamento dos demais; erros registrados em log com continuidade |
| RNF03 | Rastreabilidade | Todas as operações realizadas devem ser registradas em log estruturado, permitindo auditoria completa de cada execução |
| RNF04 | Manutenibilidade | Solução organizada em camadas (Core, Infrastructure, App) para facilitar evolução sem impacto nas demais camadas |
| RNF05 | Segurança | Credenciais armazenadas no arquivo de configuração, sem exposição em código-fonte ou logs |
| RNF06 | Compatibilidade | Compatível com .NET 8 e executável em ambiente Windows no Azure |

## 5. Restrições e premissas

**Restrições:**
- Sincronização unidirecional (Sensr → Jira); atualizações no Jira não são propagadas ao Sensr.
- A sincronização de status é a única atualização aplicada a cards já existentes no Jira.
- A API Jira v3 exige ADF para campos de texto rico; versões anteriores não são suportadas.
- A identificação de cards migrados depende do prefixo `#ID` no summary; cards sem esse prefixo não são reconhecidos.

**Premissas:**
- As APIs do Sensr e do Jira permanecem disponíveis e com contratos de autenticação estáveis.
- O workspace Jira inclui os status: To Do, In Progress, To Test, Blocked e Done.
- Cada desenvolvedor possui credenciais válidas no Sensr e `JiraAccountId` válido no workspace configurado.

## 6. Validação dos requisitos

| Requisito/conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| Escopo e requisitos (RF01–RF11, RNF01–RNF06) | Definição e validação interna com o cliente na reunião de abertura | 14/04/2026 | Validado (ver TAP-AASP-GOV-001 e ATA-AASP-GOV-001) |
| Fluxo completo e critérios de aceite | Homologação em ambiente real e comparação de cards (Fase 4) | 21/05 – 02/06/2026 | Validado (ver VV-AASP-GOV-001 e REL-VV-AASP-GOV-001) |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Documento de requisitos consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
