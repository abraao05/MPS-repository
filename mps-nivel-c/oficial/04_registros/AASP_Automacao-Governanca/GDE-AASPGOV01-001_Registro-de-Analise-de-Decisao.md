# Registro de Análise de Decisão (RAD) — AASP_Automacao-Governanca · Formato de envio de texto para a API Jira v3

| Campo | Valor |
|---|---|
| **Documento** | GDE-AASPGOV01-001 |
| **Projeto / contexto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Data** | 06/05/2026 |
| **Responsável pela decisão** | Cezar Hiraki (com o time de desenvolvimento) |

---

## 1. Problema / decisão a tomar

Definir o formato de envio de conteúdo textual — descrições de atividades, histórico de descrição convertido e comentários — para a API Jira v3, garantindo compatibilidade com a plataforma e legibilidade do conteúdo migrado do Sensr. O Sensr armazena seus campos de texto em HTML; o Jira v3 impõe um formato próprio de serialização de documentos. A escolha impacta diretamente a camada de transformação de dados no `JiraService` e a qualidade percebida pelo usuário final ao visualizar os cards migrados.

## 2. Gatilho

Decisão de escolha de tecnologia com alto impacto arquitetural: o formato de serialização de texto escolhido afeta toda a camada de transformação de dados do `SensrJiraSync.Infrastructure`, a serialização das requisições ao Jira e a estrutura do método `BuildAdfDocument`. Atinge os dois gatilhos do PRO-GDE-001 que exigem análise formal de decisão: impacto em tecnologia (formato de dados da integração principal) e impacto arquitetural significativo (afeta múltiplos componentes da Infrastructure e o contrato com a API destino).

## 3. Alternativas consideradas

| # | Alternativa | Descrição |
|---|---|---|
| A | Texto plano | Enviar o conteúdo textual como string plana, sem formatação, após remoção das tags HTML do Sensr. Implementação mínima: apenas `HtmlHelper.ToPlainText`. |
| B | HTML | Encaminhar o HTML original do Sensr diretamente para o Jira, sem conversão de formato. Implementação mínima: passar o campo `description` sem transformação. |
| C | ADF (Atlassian Document Format) | Converter o conteúdo para ADF — formato JSON estruturado com árvore de nós tipados (paragraph, text, hardBreak, etc.) — conforme exigido pela API Jira v3. Requer implementação de `BuildAdfDocument` e `HtmlHelper`. |

## 4. Critérios de avaliação

| Critério | Peso | Justificativa |
|---|---|---|
| Compatibilidade com a API Jira v3 | 3 | Requisito não negociável da plataforma destino; alternativa incompatível resulta em falha de integração |
| Fidelidade visual do conteúdo migrado | 3 | Diretamente ligada à experiência do usuário final no Jira e à CA03 (critério de aceite de fidelidade do conteúdo) |
| Esforço de implementação | 2 | Impacta o cronograma da Fase 3; deve ser considerado, mas não pode sobrepor requisitos funcionais |
| Manutenibilidade futura | 2 | Facilidade de evolução do serviço frente a mudanças da API Jira ou dos campos do Sensr |

## 5. Avaliação (matriz de decisão)

Escala de notas: 1 = baixo / inadequado · 2 = médio / parcial · 3 = alto / adequado

| Critério | Peso | Alt. A — Texto plano | Alt. B — HTML | Alt. C — ADF |
|---|---|---|---|---|
| Compatibilidade com a API Jira v3 | 3 | 1 | 1 | 3 |
| Fidelidade visual do conteúdo migrado | 3 | 1 | 2 | 3 |
| Esforço de implementação | 2 | 3 | 3 | 1 |
| Manutenibilidade futura | 2 | 2 | 2 | 3 |
| **Total ponderado** | | **16** | **19** | **26** |

Detalhamento: Alt. A = (1×3) + (1×3) + (3×2) + (2×2) = 3 + 3 + 6 + 4 = **16**. Alt. B = (1×3) + (2×3) + (3×2) + (2×2) = 3 + 6 + 6 + 4 = **19**. Alt. C = (3×3) + (3×3) + (1×2) + (3×2) = 9 + 9 + 2 + 6 = **26**.

## 6. Decisão e justificativa

**Decisão: Alternativa C — ADF (Atlassian Document Format).**

A API Jira v3 retorna erro HTTP 400 ao receber texto plano ou HTML diretamente nos campos de descrição e comentário; ADF é o único formato suportado pela plataforma. A alternativa A falha no critério de compatibilidade e entregaria conteúdo sem nenhuma estrutura visual. A alternativa B também falha no critério de compatibilidade e, mesmo que fosse aceita, resultaria em tags HTML visíveis ao usuário final no Jira — degradando severamente a legibilidade. A alternativa C, apesar do maior esforço de implementação (nota 1 no critério), é a única que atende aos requisitos funcionais e ao critério de aceite CA03. O encapsulamento da lógica no método `JiraService.BuildAdfDocument`, aliado ao `HtmlHelper` para conversão prévia do HTML do Sensr para texto plano, resulta em uma camada coesa, testável e isolada para futuras manutenções.

## 7. Riscos associados à decisão

| Risco | Resposta / Mitigação |
|---|---|
| Evolução do esquema ADF pela Atlassian em versões futuras da API Jira | Toda a criação de ADF está encapsulada em `BuildAdfDocument` (ponto único de mudança), facilitando atualização futura sem impacto no restante do serviço |
| Complexidade do parser HTML → ADF para estruturas HTML mais complexas | Uso da biblioteca HtmlAgilityPack (madura e amplamente adotada em .NET) e separação da lógica em `HtmlHelper`, permitindo testes unitários isolados da camada de transformação |

## 8. Premissas (para revisão futura)

- A API Jira v3 mantém o suporte a ADF como formato padrão de campos de texto rico ao longo do período de transição do cliente.
- A biblioteca HtmlAgilityPack permanece compatível com .NET 8 e recebe atualizações de manutenção conforme necessário.
- O escopo dos campos de texto migrados (descrição, histórico, comentários) não sofre expansão significativa que exija nós ADF não cobertos pela implementação atual de `BuildAdfDocument`.

---

## Anexo — Registro consolidado de decisões do projeto

| # | Data | Decisão | Justificativa |
|---|---|---|---|
| D01 | Abr/2026 | Estruturar a solução em três camadas: Core, Infrastructure e App | Separar contratos e modelos de domínio da implementação permite substituir serviços sem impactar a lógica de negócio e facilita a evolução futura do serviço |
| D02 | Abr/2026 | Autenticação por desenvolvedor no Sensr (token JWT individual por `DeveloperConfig`) | A API do Sensr retorna atividades filtradas pelo usuário autenticado; autenticação compartilhada retornaria dados sem filtragem adequada por desenvolvedor |
| D03 | Abr/2026 | Identificar cards migrados pelo prefixo `#ID` no campo summary do Jira | Abordagem simples, sem dependência de campos personalizados no Jira; permite lookup eficiente sem necessidade de persistir estado entre execuções do serviço |
| D04 | Mai/2026 | Utilizar ADF (Atlassian Document Format) para campos de texto rico no Jira v3 | A API Jira v3 exige ADF; envio de texto plano ou HTML resulta em erro HTTP 400. ADF é JSON estruturado com árvore de nós tipados — único formato suportado (RAD detalhado neste documento) |
| D05 | Mai/2026 | Converter HTML do Sensr para texto plano antes de montar o ADF no Jira | Enviar HTML diretamente resultaria em tags de marcação visíveis para o usuário final no Jira; a conversão via `HtmlHelper.ToPlainText` preserva o conteúdo sem poluição visual |
| D06 | Mai/2026 | Sincronização incremental limitada ao campo de status | Atualizar descrição e subtarefas a cada execução criaria risco real de sobrescrever edições manuais realizadas pelos desenvolvedores diretamente no Jira durante o período de transição |
| D07 | Mai/2026 | Executar o serviço como Azure Scheduled Job stateless | Persistir estado entre execuções adicionaria complexidade arquitetural desnecessária; a idempotência garantida pelo prefixo `#ID` elimina a necessidade de rastrear externamente o que já foi migrado |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | RAD da escolha do formato ADF para a API Jira v3 (D04) e registro consolidado das decisões D01–D07, reconstituídos a partir do Registro de Projeto AASP_Automacao-Governanca v2.0. |
| 1.1 | 16/06/2026 | Time de Melhoria Contínua | Reconciliação: nome padronizado (AASP_Automacao-Governanca); sobrenomes (Henry Komatsu, Felipe Siqueira, Jonathan Alves); data do RAD de D04 alinhada a 06/05/2026 (RAC). |
