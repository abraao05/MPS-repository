# Estratégia de Integração — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | ITP-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |

---

## 1. Componentes a integrar

| Componente | Descrição |
|---|---|
| SensrJiraSync.Core | Contratos, modelos de domínio e mapeadores. Sem dependências externas. Contém: AppSettings, DeveloperConfig, ProjectConfig, SensrModels, JiraModels, StatusMapper. |
| SensrJiraSync.Infrastructure | Implementação dos serviços de integração e helpers de transformação. Depende de Core. Contém: SensrService, JiraService, SyncService, HtmlHelper. |
| SensrJiraSync.App | Ponto de entrada, composição de dependências via injeção de dependências (DI) e execução do fluxo principal. Depende de Core e Infrastructure. Contém: Program.cs, appsettings.json. |

## 2. Interfaces

| Interface | Entre | Tipo / Contrato |
|---|---|---|
| Autenticação Sensr | SensrService ↔ API Sensr | REST — endpoint `login`; autenticação JWT por desenvolvedor (D02); token utilizado nas chamadas subsequentes da sessão |
| Captura de atividades Sensr | SensrService ↔ API Sensr | REST — endpoints `getactivitiesbyprojectstatus`, `getsingleactivity`, `subactivity`; retorno em JSON com campos de texto em HTML |
| Criação e busca de issues Jira | JiraService ↔ API Jira v3 | REST — Basic Auth (e-mail + API Token); endpoints de criação de Epic, Task e Subtask; busca paginada via `nextPageToken`; conteúdo em ADF (Atlassian Document Format) (D04) |
| Transições de status Jira | JiraService ↔ API Jira v3 | REST — consulta prévia de transições disponíveis via `GetTransitionsAsync`; aplicação de transição por ID; mapeamento via StatusMapper (D06) |
| Adição de comentários Jira | JiraService ↔ API Jira v3 | REST — endpoint de comentários; conteúdo ADF gerado por `BuildAdfDocument` a partir do histórico HTML convertido via HtmlHelper |
| Agendamento e execução | SensrJiraSync.App ↔ Azure Scheduler | Executável .NET 8 auto-contido; retorna exit code `0` em sucesso e `1` em falha; stateless entre execuções (D07) |

## 3. Estratégia e ordem de integração

A integração foi realizada de forma incremental, seguindo as quatro fases do projeto:

**Fase 1 — Arquitetura (14/04–16/04/2026):** Definição da estrutura em três camadas (Core, Infrastructure, App) e dos contratos de interface entre os componentes. A separação garante que a lógica de domínio não depende das implementações de integração (D01).

**Fase 2 — Mapeamento e Autenticação (17/04–23/04/2026):** Mapeamento completo dos endpoints das APIs Sensr e Jira v3. Definição da estratégia de autenticação JWT por desenvolvedor (D02), da identificação de cards por prefixo `#ID` no summary (D03) e do uso de ADF para campos de texto (D04). Decisões formalizadas em GDE-AASPGOV01-001.

**Fase 3 — Desenvolvimento dos Serviços (24/04–20/05/2026):** Implementação incremental de SensrService, JiraService, SyncService, HtmlHelper e StatusMapper. Cada componente integrado ao conjunto após revisão de código (PR aprovado por mínimo 1 revisor) e merge em `develop` via GitFlow. A ordem de implementação seguiu as dependências: Core → Infrastructure → App.

**Fase 4 — Homologação e Correções (21/05–02/06/2026):** Execução do fluxo integrado completo em ambiente real (APIs Sensr e Jira de produção do cliente em modo homologação). Identificação e correção de 5 defeitos (BUG-01 a BUG-05). Reexecução dos cenários de teste com 100% de aprovação. Implantação final no Azure Scheduler em 02/06/2026.

## 4. Ambiente de integração

O ambiente de integração e homologação utilizou os sistemas reais do cliente — não foi criado um ambiente simulado ou mock — garantindo que todos os cenários de teste foram validados contra as APIs de produção Sensr e Jira v3 do AASP. Esta abordagem cobriu os requisitos de integração testável em ambiente real (GAP ITP4 e ITP5).

| Componente de ambiente | Descrição |
|---|---|
| Controle de versão e CI/CD | Azure DevOps — repositório SensrJiraSync com GitFlow; pipeline de build para validação de PR |
| Execução agendada | Azure Scheduler — hospedagem do executável .NET 8 auto-contido no ambiente do cliente |
| API Sensr (homologação) | Ambiente real do Sensr com dados e desenvolvedores do AASP configurados em appsettings.json |
| API Jira v3 (homologação) | Instância Jira do cliente (projeto piloto designado pelo Sponsor para validação da migração) |

## 5. Critérios de prontidão para integração

Um componente ou conjunto de alterações deve atender a todos os critérios abaixo antes de ser integrado à branch `develop` e considerado pronto para testes integrados (GAP ITP2):

- Code review aprovado por no mínimo 1 membro da equipe além do autor antes do merge em `develop`, conforme REV-AASPGOV01-001.
- Testes unitários da camada Infrastructure passando sem falhas no pipeline de build do Azure DevOps.
- Tratamento de exceção por desenvolvedor implementado no `SyncService`, garantindo que a falha de autenticação ou processamento de um desenvolvedor não interrompa o ciclo dos demais (RNF02 — resiliência).
- Logs estruturados de operações ativos em todos os serviços modificados, permitindo rastreabilidade de execução (RNF03).
- Testes de fluxo executados localmente ou em homologação com as APIs Sensr e Jira reais antes da solicitação de merge, cobrindo os cenários afetados pela alteração.

## 6. Testes do produto integrado

O fluxo integrado completo — autenticação Sensr → captura de atividades → resolução de Epics no Jira → criação ou atualização de Tasks, Subtasks e comentários → sincronização de status — foi validado por 5 cenários de teste E2E (CT-01 a CT-05), todos executados em ambiente real de homologação contra as APIs Sensr e Jira v3 do AASP (GAP ITP3):

| Cenário | Tipo | Descrição |
|---|---|---|
| CT-01 | Happy path | Migração inicial completa: projeto → Epic, atividade → Task, sub-atividade → Subtask, histórico → comentários |
| CT-02 | Happy path | Idempotência: reexecução sobre cards já migrados não gera duplicatas (verificação por prefixo `#ID`) |
| CT-03 | Happy path | Atualização de status: status alterado no Sensr reflete no Jira via transição correta |
| CT-04 | Happy path | Status idêntico: execução não aplica transição desnecessária quando status já está em acordo |
| CT-05 | Sad path | Resiliência a HTML inválido: campo com estrutura HTML incomum é tratado pelo HtmlHelper sem interromper a execução |

Todos os cenários foram aprovados após a correção dos defeitos BUG-01 a BUG-05 identificados durante a Fase 4. Resultados detalhados em VV-AASPGOV01-001 (plano de V&V) e REL-VV-AASPGOV01-001 (relatório de resultados).

## 7. Entrega e material de apoio

A entrega em produção foi realizada via implantação manual no Azure Scheduler, com substituição do artefato anterior pelo executável publicado na baseline BL-PROD-001 (tag `v1.0.0`) e verificação do agendamento após a implantação. O Sponsor Marcos Correa Fernandez Turnes emitiu o Termo de Aceite e Encerramento (TAE-AASPGOV01-001) em 02/06/2026 (GAP ITP6).

Material de apoio entregue junto ao artefato:

| Item | Descrição |
|---|---|
| Executável .NET 8 auto-contido | Artefato publicado para o Azure Scheduler (IC-05, baseline BL-PROD-001) |
| Documentação do appsettings.json | Estrutura completa do arquivo de configuração, com campos obrigatórios por desenvolvedor, por projeto e credenciais de acesso às APIs |
| Documentação de endpoints consumidos | Endpoints Sensr (login, getactivitiesbyprojectstatus, getsingleactivity, subactivity) e Jira v3 (search, create, transitions, comments) com descrição de contrato e autenticação |
| Mapeamento de status documentado | Tabela de equivalência TODO/DOING/VALIDATION/STOPPED/DONE → To Do/In Progress/To Test/Blocked/Done |
| Instruções de troubleshooting | Exit codes (0 = sucesso, 1 = falha), interpretação de logs estruturados, cenários de erro comuns e ações corretivas |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Estratégia de integração consolidada a partir do Registro de Projeto AASP_Automacao-Governanca v2.0. |
