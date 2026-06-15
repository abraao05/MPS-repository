# Registro de Análise de Decisão (RAD) — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | GDE-AASP-GOV-001 |
| **Projeto / contexto** | AASP_Automacao-Governanca — SensrJiraSync |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsável pelas decisões** | Cezar Hiraki Velazquez (com o time de desenvolvimento) |

---

## 1. Objetivo

Registrar as decisões técnicas relevantes do projeto, com justificativa e impacto, conforme o processo de Gerência de Decisões (GDE). As decisões abaixo orientaram a arquitetura e a lógica de sincronização do serviço SensrJiraSync (ver PCP-AASP-GOV-001).

## 2. Decisões relevantes registradas

| # | Data | Decisão | Justificativa | Impacto |
|---|---|---|---|---|
| D01 | Abr/2026 | Estruturar a solução em três camadas: Core, Infrastructure e App | Separar contratos e modelos da implementação permite substituir serviços sem impactar a lógica de domínio e facilita a evolução futura | Três projetos distintos; dependências unidirecionais (App → Infrastructure → Core) |
| D02 | Abr/2026 | Autenticação por desenvolvedor no Sensr (token JWT individual) | A API do Sensr retorna atividades filtradas por usuário; autenticação compartilhada retornaria dados sem filtragem adequada | `DeveloperConfig` inclui credenciais Sensr; `SensrService` realiza login por desenvolvedor a cada execução |
| D03 | Abr/2026 | Identificar cards migrados pelo prefixo `#ID` no summary do Jira | Simples, sem dependência de campos personalizados; o `#ID` é único por projeto e permite lookup eficiente sem persistir estado entre execuções | `SyncService` extrai `#ID` via `ExtractSensrId`; `GetIssuesByEpicAsync` constrói dicionário indexado por `#ID` |
| D04 | Mai/2026 | Utilizar ADF para campos de texto no Jira | A API Jira v3 exige ADF; o envio de texto plano resulta em erro. O ADF é JSON estruturado representando documentos como árvore de nós | Implementação do `BuildAdfDocument` no `JiraService` para conversão antes de qualquer envio |
| D05 | Mai/2026 | Converter HTML do Sensr para texto plano antes de enviar ao Jira | Enviar HTML diretamente resultaria em tags visíveis para o usuário; a conversão preserva o conteúdo sem poluição de marcação | Implementação do HtmlHelper com HtmlAgilityPack |
| D06 | Mai/2026 | Sincronização incremental limitada a status | Atualizar descrição e subtarefas a cada execução criaria risco de sobrescrever edições manuais feitas no Jira durante a transição | `UpdateIssueIfNeededAsync` verifica e atualiza apenas o status; demais campos imutáveis após a criação inicial |
| D07 | Mai/2026 | Executar o serviço como Azure Scheduled Job stateless | Persistir estado adicionaria complexidade desnecessária; a idempotência por `#ID` elimina a necessidade de rastrear o que já foi migrado | Cada execução consulta o estado atual de ambas as plataformas, sem dependências externas além das APIs |

## 3. Decisão de maior impacto — Fonte de identificação de cards (D03)

| Item | Conteúdo |
|---|---|
| **Problema** | Como reconhecer, de forma confiável e sem estado externo, quais atividades do Sensr já foram migradas para o Jira |
| **Alternativas** | (A) Persistir um mapa Sensr→Jira em base de dados; (B) usar um campo personalizado no Jira; (C) prefixar o summary com `#ID` |
| **Escolha** | Alternativa C — prefixo `#ID` no summary |
| **Justificativa** | Dispensa base de dados e campos personalizados; o `#ID` é único por projeto e permite reconstruir o índice a cada execução, garantindo idempotência (RNF01) e execução stateless (D07) |
| **Riscos** | Cards criados manualmente sem o prefixo `#ID` não são reconhecidos — restrição documentada em REQ-AASP-GOV-001 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro consolidado de decisões (D01–D07) a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
