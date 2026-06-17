# Plano de Verificação e Validação — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | VV-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Versão** | 1.3 |
| **Data** | 02/06/2026 |

---

## 1. Itens a verificar e validar (VV 1)

| Item | Método |
|---|---|
| Código dos serviços (SensrService, JiraService, SyncService, StatusMapper, HtmlHelper) | Code review via Pull Request no Azure DevOps + testes unitários |
| Fluxo de migração inicial (Sensr → Jira: Epic + Task + Subtask) | Teste de integração E2E em ambiente real de homologação |
| Fluxo de sincronização incremental de status | Teste de integração E2E + execuções repetidas sobre os mesmos dados |
| Idempotência (não criar duplicatas em execuções repetidas) | Teste de fluxo com execução múltipla e verificação de ausência de duplicatas por prefixo `#ID` |
| Conversão HTML → texto plano → ADF (descrição e histórico) | Teste unitário do HtmlHelper + teste de integração no JiraService |
| Mapeamento de status (5 status Sensr → 5 status Jira) | Teste unitário do StatusMapper com todos os mapeamentos |
| Sanitização de labels (espaços, barras) | Teste unitário do método SanitizeLabel |
| Resiliência por desenvolvedor (falha de 1 não interrompe os demais) | Teste de fluxo com credencial inválida em 1 DeveloperConfig |
| Configuração via appsettings.json (múltiplos desenvolvedores) | Teste de bootstrap com injeção de dependências |
| Requisitos RF01–RF11 + RNF01–RNF06 | Validação por amostragem com o Sponsor Marcos Correa Fernandez Turnes em ambiente real (REQ5) |

## 2. Métodos e critérios (VV 3)

- **Testes unitários:** cobertura dos métodos críticos das camadas Core e Infrastructure — `StatusMapper.MapSensrToJira`, `HtmlHelper.ToPlainText`, `HtmlHelper.ParseDescriptionHistory`, `JiraService.SanitizeLabel`, `SyncService.ExtractSensrId`.
- **Testes de integração:** execução dos serviços contra as APIs reais do Sensr e do Jira v3 em ambiente de homologação, validando autenticação JWT por desenvolvedor, criação de hierarquia de issues e aplicação de transições.
- **Testes de fluxo (E2E):** ciclo completo de migração inicial seguido de ciclo subsequente de sincronização incremental, cobrindo criação, idempotência e atualização de status.
- **Testes do QA (Jonathan Alves, a partir da Fase 4):** validação dos 12 cenários funcionais (CT-01 a CT-12), edge cases e regressão após correção dos defeitos BUG-01 a BUG-05.
- **Ferramentas:** Azure DevOps (Pull Requests e code review), Postman (validação manual de contratos das APIs Sensr e Jira), ClickUp (gestão de tarefas de teste).
- **Ambientes:** homologação executada diretamente contra os ambientes reais do Sensr e do Jira do AASP (workspace de teste configurado para o projeto piloto indicado pelo Sponsor). Conforme ADAP-AASPGOV01-001, o uso de mocks não seria representativo da compatibilidade real com as APIs de destino.

## 3. Critérios de aceite

| # | Critério | Evidência esperada |
|---|---|---|
| CA01 | Migração sem duplicatas | Execuções repetidas não geram cards duplicados — verificação pelo prefixo `#ID` no summary do Jira |
| CA02 | Fidelidade da hierarquia | Cada projeto → Epic; atividade → Task; sub-atividade → Subtask vinculada corretamente à Task pai |
| CA03 | Fidelidade do conteúdo | Descrição, labels e histórico migrados com HTML convertido para texto plano legível no Jira |
| CA04 | Fidelidade do status | Status de cada atividade corresponde ao equivalente no Jira conforme mapeamento do StatusMapper |
| CA05 | Sincronização incremental | Status alterado no Sensr reflete no Jira na execução seguinte do serviço |
| CA06 | Migração do histórico | Entradas do `description_history` presentes como comentários individuais na Task correspondente |
| CA07 | Resiliência por desenvolvedor | Falha de autenticação ou processamento de um desenvolvedor não interrompe o ciclo dos demais |

## 4. Execução e registro (VV 4)

A execução e o registro de todos os testes estão documentados em `REL-VV-AASPGOV01-001_Relatorio-de-Execucao-de-Testes.md`. O relatório detalha os testes realizados por fase (Fases 1 a 4), os 5 defeitos identificados durante a Fase 4 de Homologação (BUG-01 a BUG-05) e seus tratamentos, os resultados individuais dos cenários CT-01 a CT-12 e a validação dos critérios de aceite CA01 a CA07.

## 5. Análise e comunicação dos resultados (VV 5)

Os resultados dos testes são analisados pelo QA (Jonathan Alves) e comunicados ao Gerente de Projeto (Abraão Oliveira) durante as reuniões de revisão registradas nas atas ATA-AASPGOV01-001 a ATA-AASPGOV01-003. Defeitos identificados são registrados com ID, descrição, fase e tratamento no REL-VV-AASPGOV01-001 e acompanhados até resolução. Os indicadores de qualidade (taxa de aprovação de cenários, contagem e severidade de defeitos, e status dos critérios de aceite) alimentam o documento de Medição `MED-AASPGOV01-001`. A validação final dos critérios de aceite CA01–CA07 pelo Sponsor Marcos Correa Fernandez Turnes foi registrada na ATA-AASPGOV01-003 (29/05/2026) e formalizada no TAE-AASPGOV01-001 (02/06/2026).

## 6. Cenários de teste (Gherkin) e evidências

```gherkin
Funcionalidade: Migração e sincronização de cards entre Sensr e Jira

  Cenário: CT-01 — Migração inicial de cards (happy path)
    Dado que o Sensr contém projetos com atividades, sub-atividades e histórico de descrição
    E o Jira não possui nenhum card para os projetos correspondentes
    Quando o serviço SensrJiraSync executa pela primeira vez para um desenvolvedor configurado
    Então um Epic é criado no Jira para cada projeto do Sensr
    E uma Task é criada para cada atividade com summary no formato "#ID Nome"
    E uma Subtask é criada para cada sub-atividade e vinculada à Task pai
    E a descrição, as labels sanitizadas, o status mapeado e o histórico são preservados nos cards criados
    E nenhum card duplicado é gerado

  Cenário: CT-02 — Idempotência sem duplicatas (happy path)
    Dado que o Jira já possui os cards migrados da execução anterior com prefixo "#ID" no summary
    E os dados do Sensr permanecem inalterados desde a última execução
    Quando o serviço SensrJiraSync executa novamente sobre os mesmos dados
    Então nenhum novo Epic, Task ou Subtask é criado
    E os cards existentes permanecem inalterados
    E o serviço encerra sem erros com exit code 0

  Cenário: CT-03 — Atualização de status: Sensr DOING → Jira In Progress (happy path)
    Dado que uma atividade já migrada possui status "DOING" no Sensr
    E o card correspondente no Jira está com status diferente de "In Progress"
    Quando o serviço SensrJiraSync executa o ciclo de sincronização incremental
    Então o StatusMapper converte "DOING" para "In Progress"
    E o serviço consulta as transições disponíveis via GetTransitionsAsync
    E a transição para "In Progress" é aplicada no card do Jira
    E o card no Jira exibe o status "In Progress"

  Cenário: CT-04 — Status já sincronizado, nenhuma transição aplicada (happy path)
    Dado que uma atividade migrada possui status "DONE" no Sensr
    E o card correspondente no Jira já está com status "Done"
    Quando o serviço SensrJiraSync executa o ciclo de sincronização incremental
    Então o StatusMapper identifica que os status são equivalentes
    E nenhuma transição é aplicada no card do Jira
    E o serviço registra em log que o status já está sincronizado

  Cenário: CT-05 — HTML inválido ou complexo na descrição do Sensr (sad path)
    Dado que uma atividade no Sensr contém campos de descrição com HTML inválido ou estrutura não convencional
    Quando o serviço SensrJiraSync processa a atividade e invoca HtmlHelper.ToPlainText
    Então o HtmlHelper extrai o texto disponível sem lançar exceção
    E o conteúdo resultante é convertido para ADF via BuildAdfDocument
    E o card é criado no Jira com o conteúdo textual legível sem tags de marcação visíveis
    E a execução continua normalmente para as demais atividades do desenvolvedor

  Cenário: CT-06 — Falha de autenticação em 1 desenvolvedor (sad path)
    Dado que o appsettings.json contém 2 desenvolvedores configurados
    E as credenciais do primeiro desenvolvedor estão inválidas ou expiradas
    Quando o serviço SensrJiraSync executa o ciclo de sincronização
    Então SensrService.LoginAsync falha para o primeiro desenvolvedor
    E o SyncService registra o erro em log e avança para o próximo desenvolvedor
    E o segundo desenvolvedor é processado normalmente até conclusão
    E o serviço encerra com exit code 1 indicando falha parcial

  Cenário: CT-07 — Mapeamento de status: Sensr TODO → Jira To Do (happy path)
    Dado que uma atividade no Sensr possui status "TODO"
    Quando o StatusMapper.MapSensrToJira é invocado com o valor "TODO"
    Então o resultado retornado é "To Do"
    E a transição correspondente é localizada no Jira e aplicada corretamente ao card

  Cenário: CT-08 — Mapeamento de status: Sensr VALIDATION → Jira To Test (happy path)
    Dado que uma atividade no Sensr possui status "VALIDATION"
    Quando o StatusMapper.MapSensrToJira é invocado com o valor "VALIDATION"
    Então o resultado retornado é "To Test"
    E a transição correspondente é localizada no Jira e aplicada corretamente ao card

  Cenário: CT-09 — Sub-atividade vinculada corretamente à Task pai (happy path)
    Dado que uma atividade no Sensr possui sub-atividades associadas
    E a Task pai foi criada ou já existe no Jira com prefixo "#ID" no summary
    Quando o serviço SensrJiraSync processa as sub-atividades via JiraService.CreateSubtaskAsync
    Então cada Subtask é criada no Jira com summary no formato "#ID Nome"
    E cada Subtask está vinculada à Task pai correta no Epic correspondente
    E a descrição da Subtask é convertida de HTML para texto plano antes do envio

  Cenário: CT-10 — Label com espaços e barras é sanitizada antes do envio ao Jira (happy path)
    Dado que uma atividade no Sensr possui tags contendo espaços ou barras no nome
    Quando o serviço SensrJiraSync invoca JiraService.SanitizeLabel para cada tag
    Então os espaços e barras são substituídos por underscore
    E a label sanitizada é aceita pelo Jira sem erro de validação
    E a label aparece corretamente no card criado no Jira

  Cenário: CT-11 — Histórico de descrição migrado como comentários individuais (happy path)
    Dado que uma atividade no Sensr possui múltiplas entradas no campo description_history em HTML
    Quando o serviço SensrJiraSync processa o histórico via HtmlHelper.ParseDescriptionHistory
    Então cada entrada do histórico é convertida individualmente de HTML para texto plano
    E cada entrada convertida é adicionada como comentário separado na Task do Jira via JiraService.AddCommentAsync
    E os comentários aparecem na Task na ordem correspondente ao histórico original

  Cenário: CT-12 — Falha temporária na API Jira durante criação de Task (sad path)
    Dado que o serviço SensrJiraSync está processando uma lista de atividades de um desenvolvedor
    E a API Jira v3 retorna erro HTTP durante a criação de uma Task específica
    Quando o SyncService captura a exceção lançada pelo JiraService
    Então o erro é registrado em log com identificação da atividade afetada
    E o serviço avança para a próxima atividade do mesmo desenvolvedor
    E as demais atividades do desenvolvedor são processadas normalmente
    E o serviço prossegue para os demais desenvolvedores configurados
```

**Tabela resumo dos cenários:**

| ID | Cenário | Tipo | Critério de aceite | Evidência | Situação |
|---|---|---|---|---|---|
| CT-01 | Migração inicial de cards | Happy | CA01, CA02, CA03 | Execução em ambiente real — projeto piloto AASP | Aprovado |
| CT-02 | Idempotência sem duplicatas | Happy | CA01 | Reexecução sobre dados já migrados | Aprovado |
| CT-03 | Atualização de status DOING → In Progress | Happy | CA05 | Execução incremental em ambiente real | Aprovado |
| CT-04 | Status já sincronizado — sem transição | Happy | CA05 | Verificação de ausência de transição em log | Aprovado |
| CT-05 | HTML inválido na descrição | Sad | CA03 | Processamento sem exceção; card legível no Jira | Aprovado |
| CT-06 | Falha de autenticação em 1 desenvolvedor | Sad | CA07 | Processamento contínuo dos demais devs | Aprovado |
| CT-07 | Mapeamento TODO → To Do | Happy | CA04 | Resultado do StatusMapper + transição no Jira | Aprovado |
| CT-08 | Mapeamento VALIDATION → To Test | Happy | CA04 | Resultado do StatusMapper + transição no Jira | Aprovado |
| CT-09 | Sub-atividade vinculada à Task pai | Happy | CA02 | Hierarquia Task → Subtask verificada no Jira | Aprovado |
| CT-10 | Label com espaços e barras sanitizada | Happy | CA03 | Label sem erro no Jira; underscore no nome | Aprovado |
| CT-11 | Histórico migrado como comentários individuais | Happy | CA06 | Comentários na Task no Jira correspondentes ao histórico Sensr | Aprovado |
| CT-12 | Falha temporária na API Jira | Sad | CA07 | Log de erro isolado; demais atividades processadas | Aprovado |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Plano de V&V consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0. |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Responsável pelos testes de QA atualizado: Jonathan Alves substituiu Caroline Sousa. |
| 1.2 | 15/06/2026 | Time de Melhoria Contínua | Jonathan Alves (QA) corrigido de grafia anterior. |
| 1.3 | 16/06/2026 | Time de Melhoria Contínua | Reconciliação: nome padronizado (AASP_Automacao-Governanca); sobrenomes (Henry Komatsu, Felipe Siqueira, Jonathan Alves). |
