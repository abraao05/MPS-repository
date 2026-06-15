# Plano de Verificação e Validação — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | VV-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Processo** | PRO-VV-001 |

---

## 1. Estratégia de testes (VV 1, VV 3)

Testes de integração executados diretamente nos ambientes reais do Sensr e do Jira em modo de homologação. Mocks não foram utilizados para comportamentos críticos de API (conforme ADAP-AASPGOV01-001 §2), pois a fidelidade depende da compatibilidade real entre as plataformas. A validação foi feita por comparação direta entre os cards criados no Jira e os registros originais do Sensr. A revisão por pares (verificação) é evidenciada via Pull Request no GitFlow (ver REV-AASPGOV01-001).

## 2. Itens a verificar e validar

| Item | Método |
|---|---|
| Código dos serviços (SensrService, JiraService, SyncService, StatusMapper, HtmlHelper) | Revisão por pares (PR) + build CI |
| Migração inicial (Epics, Tasks, Subtasks) | Teste de integração + comparação com o Sensr |
| Idempotência | Reexecução sobre os mesmos dados |
| Sincronização incremental de status | Teste de integração com status divergente/igual |
| Conversão HTML→ADF e migração de histórico/labels | Teste com conteúdo real do Sensr |
| Resiliência (credencial inválida, transição indisponível, paginação) | Cenários sad + volume real |

## 3. Critérios de aceite

| # | Critério | Validado em |
|---|---|---|
| CA01 | Migração sem duplicatas — execuções repetidas não geram cards duplicados | ATA-AASPGOV01-003 · 29/05/2026 |
| CA02 | Fidelidade da hierarquia — projeto→Epic, atividade→Task, sub-atividade→Subtask | ATA-AASPGOV01-003 · 29/05/2026 |
| CA03 | Fidelidade do conteúdo — descrição, labels e histórico migrados corretamente | ATA-AASPGOV01-003 · 29/05/2026 |
| CA04 | Fidelidade do status — cada atividade com status equivalente correto no Jira | ATA-AASPGOV01-003 · 29/05/2026 |
| CA05 | Sincronização incremental — status alterado no Sensr reflete no Jira na próxima execução | ATA-AASPGOV01-003 · 29/05/2026 |
| CA06 | Migração do histórico — entradas do `description_history` como comentários | ATA-AASPGOV01-003 · 29/05/2026 |
| CA07 | Resiliência por desenvolvedor — falha de um não interrompe os demais | ATA-AASPGOV01-003 · 29/05/2026 |

## 4. Cenários de teste (12 cenários: 8 happy + 4 sad)

| CT | Cenário | Tipo | Resultado |
|---|---|---|---|
| CT-01 | Migração inicial completa de projetos, atividades e sub-atividades | Happy | ✅ Aprovado |
| CT-02 | Idempotência — reexecução sem geração de cards duplicados | Happy | ✅ Aprovado |
| CT-03 | Sincronização incremental de status de cards já migrados | Happy | ✅ Aprovado |
| CT-04 | Migração de sub-atividades (Subtasks) vinculadas à Task pai correta | Happy | ✅ Aprovado |
| CT-05 | Mapeamento de todos os status (TODO, DOING, VALIDATION, STOPPED, DONE) | Happy | ✅ Aprovado |
| CT-06 | Conversão de HTML (Sensr) para ADF (Jira v3) com preservação de formatação | Happy | ✅ Aprovado |
| CT-07 | Migração do histórico (`description_history`) como comentários individuais | Happy | ✅ Aprovado |
| CT-08 | Migração de labels com normalização para formato aceito pelo Jira | Happy | ✅ Aprovado |
| CT-09 | Credencial inválida de desenvolvedor — isolamento sem interrupção dos demais | Sad | ✅ Aprovado |
| CT-10 | Paginação de Epic com mais de 50 issues via `nextPageToken` | Happy | ✅ Aprovado |
| CT-11 | Transição de status indisponível no workflow Jira — log de aviso sem erro fatal | Sad | ✅ Aprovado |
| CT-12 | Sanitização de labels com espaços, barras ou caracteres especiais | Sad | ✅ Aprovado |

### 4.1 Cenários representativos (Gherkin)

```gherkin
Funcionalidade: Migração e sincronização de atividades Sensr → Jira

  Cenário: Migração inicial completa (CT-01, happy)
    Dado que o Sensr contém projetos, atividades e sub-atividades com histórico
      E o Jira não possui cards para aqueles projetos
    Quando o serviço executa pela primeira vez
    Então os Epics, Tasks e Subtasks são criados com hierarquia, descrição, labels e status corretos
      E nenhum card duplicado é gerado

  Cenário: Idempotência (CT-02, happy)
    Dado que o Jira já possui os cards migrados na execução anterior
    Quando o serviço executa novamente sobre os mesmos dados
    Então nenhum novo card é criado (verificação pelo prefixo #ID no summary)

  Cenário: Credencial inválida de desenvolvedor (CT-09, sad)
    Dado um desenvolvedor com credencial inválida no Sensr
    Quando o serviço processa a lista de desenvolvedores
    Então a falha é isolada e registrada em log
      E o processamento dos demais desenvolvedores continua sem interrupção

  Cenário: Transição de status indisponível (CT-11, sad)
    Dado um card cujo status alvo não está disponível no workflow do Jira
    Quando o serviço tenta aplicar a transição
    Então um log de aviso é registrado
      E a execução prossegue sem erro fatal
```

## 5. Métodos, critérios e ambientes (VV 3)

- **Ambientes:** homologação (Azure Scheduler staging) contra Sensr e Jira reais; sem ambiente de testes dedicado (ADAP §2).
- **Critérios:** CA01–CA07 (seção 3).
- **Ferramentas:** Azure DevOps (CI/build), Pull Requests para revisão por pares.

## 6. Execução, análise e comunicação (VV 4, VV 5)

A execução dos 12 cenários e o registro dos 5 defeitos estão consolidados em REL-VV-AASPGOV01-001. Os resultados foram analisados e comunicados na validação da homologação com o Patrocinador (ATA-AASPGOV01-003, 29/05/2026) e alimentam a Medição (MED-AASPGOV01-001).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Plano de V&V consolidado a partir do INTAKE-AASPGOV01 (14/06/2026), Bloco 9. |
