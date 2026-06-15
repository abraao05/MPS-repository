# Documento de Requisitos — AASP_GOV · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | REQ-AASPGOV01-001 |
| **Projeto** | AASP_GOV — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |
| **Responsáveis (Discovery)** | Cezar Hiraki (Tech Lead) · Abraão Oliveira (GP) |

---

## 1. Contexto e objetivo

A AASP utilizava o Sensr como ferramenta de gerenciamento de projetos e atividades do time de desenvolvimento. Em função de requisitos operacionais e de governança, foi tomada a decisão de migrar para o Jira. Como a migração é gradual — e não substituição imediata — o time precisaria operar nas duas ferramentas simultaneamente durante um período de transição, com risco real de divergência entre os registros. O processo manual de migração de cards entre as plataformas representaria volume elevado de trabalho operacional e estaria sujeito a erros humanos: dados de descrição, status, subtarefas, responsáveis e histórico de alterações precisariam ser replicados com fidelidade para cada atividade de cada desenvolvedor em cada projeto.

O objetivo do projeto é desenvolver um serviço automatizado capaz de realizar essa migração de forma confiável e de manter a sincronização entre as duas ferramentas enquanto a transição estiver em andamento. O serviço deverá criar no Jira todos os cards existentes no Sensr — preservando sua estrutura hierárquica — e atualizar automaticamente o status dos cards já migrados quando houver movimentação no Sensr.

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| Marcos Correa Fernandez Turnes (Sponsor — AASP) | Eliminar trabalho manual de migração; garantir consistência entre Sensr e Jira durante a transição |
| Time de desenvolvimento da AASP | Continuar usando o Sensr normalmente sem precisar duplicar registros no Jira durante o período de migração |
| Gerência de projetos da AASP | Ter visibilidade atualizada no Jira (ferramenta-alvo) sem aguardar o término da migração |

## 3. Visão geral da solução

Serviço .NET 8 executado como Azure Scheduled Job que, a cada execução, autentica-se nas APIs do Sensr (por desenvolvedor) e do Jira, busca atividades pendentes de migração e cria no Jira a hierarquia correspondente (Epic → Task → Subtask). Para cards já migrados, verifica divergência de status e aplica a transição equivalente no Jira. **O projeto não tem interface de usuário** — toda interação humana ocorre nas plataformas Sensr e Jira, fora do escopo do serviço. A aplicabilidade de design UX/UI é "não aplicável", conforme registrado em ADAP-AASPGOV01-001.

## 4. Requisitos funcionais

| ID | Requisito (história) | Prioridade | SP | Sprint | Critérios de aceite |
|---|---|---|---|---|---|
| RF-01 | Como serviço de sincronização, quero autenticar-me no Sensr por desenvolvedor utilizando credenciais individuais (token JWT) para obter a lista de atividades por projeto filtrada pelo usuário | Alta | 5 | Sprint 0 | Autenticação realizada com credenciais por DeveloperConfig; token JWT válido obtido; lista de projetos do desenvolvedor recuperada com sucesso; falha de autenticação em um desenvolvedor não interrompe os demais (RNF-02) |
| RF-02 | Como serviço de migração, quero criar ou reutilizar um Epic no Jira por projeto do Sensr (identificado pelo nome) para preservar a hierarquia de projetos | Alta | 3 | Sprint 1 | Epic criado se inexistente; Epic existente reutilizado se já presente (sem duplicar); identificação por nome do projeto |
| RF-03 | Como serviço de migração, quero criar uma Task no Jira para cada atividade do Sensr ainda não migrada, com summary no formato `#ID Nome` e preservando descrição, responsável, labels, data de início e status | Alta | 4 | Sprint 1 | Task criada com summary correto; campos descrição, responsável (mapeado pelo JiraAccountId), labels, data de início e status preservados; vínculo correto ao Epic do projeto |
| RF-04 | Como serviço de migração, quero criar uma Subtask no Jira para cada sub-atividade vinculada a uma atividade do Sensr, mantendo a hierarquia Task → Subtask | Média | 2 | Sprint 1 | Subtask criada vinculada à Task pai correta; summary no formato `#ID Nome`; descrição convertida de HTML para texto plano |
| RF-05 | Como serviço de sincronização, quero verificar se o status de uma atividade do Sensr já existente no Jira (identificada pelo `#ID` no summary) mudou e aplicar a transição correspondente | Alta | 4 | Sprint 2 | Status divergente detectado pela comparação case-insensitive; transição aplicada via API Jira; sem transição aplicada quando os status estão equivalentes |
| RF-06 | Como serviço de migração, quero migrar o histórico de alterações da atividade (`description_history`) como comentários individuais na Task correspondente no Jira | Média | 3 | Sprint 2 | Cada entrada do `description_history` extraída via HtmlHelper; comentário individual adicionado à Task; ordem cronológica preservada |
| RF-07 | Como serviço de transformação, quero converter HTML da descrição e do histórico do Sensr para texto plano compatível com o formato ADF (Atlassian Document Format) do Jira | Alta | 3 | Sprint 1 | HTML convertido para texto legível via HtmlAgilityPack; resultado serializado em ADF via BuildAdfDocument; sem tags HTML visíveis no Jira |
| RF-08 | Como serviço de transformação, quero mapear os status do Sensr (TODO, DOING, VALIDATION, STOPPED, DONE) para os status equivalentes do Jira (To Do, In Progress, To Test, Blocked, Done) | Alta | 2 | Sprint 1 | StatusMapper retorna o status Jira correto para cada status Sensr; mapeamento completo dos 5 status; sem status órfão |
| RF-09 | Como serviço de transformação, quero sanitizar labels contendo espaços ou caracteres especiais antes da criação no Jira (substituindo espaços e barras por underscore) | Média | 2 | Sprint 1 | SanitizeLabel converte espaços e barras em underscore; demais caracteres preservados; nenhum erro de criação por label inválido |
| RF-10 | Como administrador do serviço, quero configurar o serviço via `appsettings.json`, com suporte a múltiplos desenvolvedores (cada um com credenciais Sensr, ID de usuário Sensr, ID de conta Jira e lista de projetos) | Alta | 2 | Sprint 0 | Configuração via appsettings.json carregada via Microsoft.Extensions.Configuration; estrutura DeveloperConfig + ProjectConfig validada; suporte a N desenvolvedores |
| RF-11 | Como operador, quero que o serviço seja executável como processo isolado, compatível com agendamento via Azure Scheduler, retornando código de saída diferente de zero em caso de falha | Alta | 3 | Sprint 2 | Executável auto-contido .NET 8; exit code 0 em sucesso; exit code 1 em falha; compatível com Azure Scheduled Job |

## 5. Requisitos não funcionais

| ID | Requisito não funcional | Prioridade | SP | Sprint | Critério |
|---|---|---|---|---|---|
| RNF-01 | Idempotência: execuções repetidas não devem criar cards duplicados no Jira | Alta | 3 | Sprint 2 | Verificação de existência pelo prefixo `#ID` no summary antes de qualquer criação; zero duplicatas em testes de execução repetida |
| RNF-02 | Confiabilidade: falhas na sincronização de um desenvolvedor ou projeto não devem interromper o processamento dos demais | Alta | 2 | Sprint 2 | Tratamento de exceção por DeveloperConfig no SyncService; continuidade comprovada em teste com credencial inválida (CT-06) |
| RNF-03 | Rastreabilidade: todas as operações realizadas devem ser registradas em log estruturado, permitindo auditoria completa de cada execução | Média | 1 | Sprint 2 | Log estruturado via Microsoft.Extensions.Logging em todos os serviços; eventos relevantes registrados (login, criação, atualização, erro) |
| RNF-04 | Manutenibilidade: solução organizada em camadas (Core, Infrastructure, App) para facilitar evolução sem impacto nas demais camadas | Média | 3 | Sprint 0 | 3 projetos .NET distintos com dependências unidirecionais (App → Infrastructure → Core); Core sem dependências externas |
| RNF-05 | Segurança: credenciais armazenadas no arquivo de configuração, sem exposição em código-fonte ou logs | Alta | 1 | Sprint 0 | `appsettings.json` mantido fora do repositório; nenhum token impresso em log; auditoria de configuração registrada em GCO-AASPGOV01-001 |
| RNF-06 | Compatibilidade: serviço compatível com .NET 8 e executável em ambiente Windows no Azure | Alta | 1 | Sprint 0 | TargetFramework `net8.0` em todos os projetos; publicação self-contained validada no Azure Scheduled Job |

**Total:** 11 RF (32 SP) + 6 RNF (11 SP) + atividades técnicas (16 SP — mapeamento de endpoints/auth Jira na Sprint 0, correções Fase 4/Sprint 3) = **~59 SP em 4 sprints**.

## 6. Restrições e premissas

**Restrições:**
- Sincronização unidirecional (Sensr → Jira); atualizações no Jira não são propagadas ao Sensr.
- Sincronização de status é a única atualização aplicada a cards já existentes no Jira (descrição, labels e demais campos são imutáveis após criação inicial).
- A API Jira v3 exige ADF para campos de texto rico; versões anteriores não são suportadas.
- Identificação de cards migrados depende do prefixo `#ID` no summary; cards sem esse prefixo não são reconhecidos.

**Premissas:**
- As APIs do Sensr e do Jira permanecem disponíveis e com contratos de autenticação estáveis durante o período de operação.
- O workspace Jira da AASP inclui os status mapeados: To Do, In Progress, To Test, Blocked e Done.
- Cada desenvolvedor possui credenciais válidas no Sensr e `JiraAccountId` válido no workspace configurado.

## 7. Validação dos requisitos

| Requisito/conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| RF-01 a RF-11 + RNF-01 a RNF-06 (escopo completo) | Apresentação na reunião de Kickoff (14/04/2026) ao Sponsor da AASP | 14/04/2026 | Validado e aprovado (ATA-AASPGOV01-001) |
| Estratégia de mapeamento de APIs e autenticação | Reunião de Alinhamento de Mapeamento de APIs (23/04/2026) | 23/04/2026 | Validado (ATA-AASPGOV01-002) |
| Critérios de aceite CA01–CA07 | Validação por amostragem em ambiente real Sensr/Jira | 29/05/2026 | 100% aprovados (ATA-AASPGOV01-003) |
| Aceite final dos requisitos entregues | Reunião de Aceite Final com Sponsor da AASP | 02/06/2026 | Aceite formal emitido (ATA-AASPGOV01-004 + TAE-AASPGOV01-001) |

## 8. Confirmação de entendimento e compromisso

| Envolvido | Papel | Confirmação | Data |
|---|---|---|---|
| Marcos Correa Fernandez Turnes | Sponsor (AASP) | Entendimento confirmado dos 11 RF + 6 RNF e do escopo macro | 14/04/2026 (ATA-AASPGOV01-001) |
| Abraão Oliveira | Gerente de Projeto (Timeware) | Compromisso assumido pela equipe Timeware com a entrega no prazo de 7 semanas | 14/04/2026 (ATA-AASPGOV01-001) |
| Cezar Hiraki | Tech Lead / Arquiteto (Timeware) | Compromisso técnico com a arquitetura em 3 camadas e os critérios de aceite | 14/04/2026 (ATA-AASPGOV01-001) |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Documento de requisitos consolidado a partir do Registro de Projeto AASP_GOV v2.0 (08/06/2026). Adicionada priorização, Story Points e Sprint para cada RF/RNF conforme modelagem agile retroativa (ADAP-AASPGOV01-001). |
