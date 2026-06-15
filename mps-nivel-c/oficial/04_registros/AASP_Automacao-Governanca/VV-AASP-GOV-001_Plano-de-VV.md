# Plano de Verificação e Validação — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | VV-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Processo** | PRO-VV-001 |

---

## 1. Estratégia de testes (VV 1)

Testes de integração end-to-end executados diretamente contra os ambientes reais do Sensr e do Jira em modo de homologação. A validação foi feita por **comparação direta**: após cada execução, os cards criados no Jira foram confrontados com os registros originais do Sensr, verificando fidelidade de campos, hierarquia, status e histórico. Conforme ADAP-AASP-GOV-001, não houve ambiente de testes dedicado, pois o comportamento crítico depende da compatibilidade real entre as plataformas (mocks não seriam representativos).

## 2. Itens a verificar e validar

| Item | Método |
|---|---|
| Migração inicial de cards (hierarquia, descrição, labels, status) | Teste E2E + comparação com o Sensr |
| Idempotência (ausência de duplicatas) | Reexecução sobre os mesmos dados |
| Sincronização incremental de status | Teste E2E com status divergente e igual |
| Conversão de HTML da descrição e do histórico | Teste com HTML malformado / não reconhecido |
| Migração do histórico como comentários | Comparação de comentários no Jira |

## 3. Critérios de aceite

| # | Critério | Evidência esperada |
|---|---|---|
| CA01 | Migração sem duplicatas | Execuções repetidas não geram cards duplicados; verificação pelo prefixo `#ID` no summary |
| CA02 | Fidelidade da hierarquia | Cada projeto → Epic, atividade → Task, sub-atividade → Subtask vinculada corretamente |
| CA03 | Fidelidade do conteúdo | Descrição, labels e histórico migrados com HTML convertido para texto plano legível |
| CA04 | Fidelidade do status | Status de cada atividade corresponde ao equivalente no Jira conforme StatusMapper |
| CA05 | Sincronização incremental | Status alterado no Sensr reflete no Jira na execução seguinte do serviço |
| CA06 | Migração do histórico | Entradas do `description_history` presentes como comentários individuais na Task |
| CA07 | Resiliência por desenvolvedor | Falha de um desenvolvedor não interrompe o processamento dos demais |

## 4. Cenários de teste (Gherkin)

```gherkin
Funcionalidade: Migração e sincronização de atividades Sensr → Jira

  Cenário: Migração inicial de cards (happy path)
    Dado que o Sensr contém atividades com sub-atividades e histórico
      E o Jira não possui nenhum card para aquele projeto
    Quando o serviço executa pela primeira vez
    Então todos os cards são criados no Jira com hierarquia, descrição, labels e status corretos
      E nenhum card duplicado é gerado

  Cenário: Idempotência — sem duplicatas (happy path)
    Dado que o Jira já possui os cards migrados na execução anterior
    Quando o serviço executa novamente sobre os mesmos dados
    Então nenhum novo card é criado
      E os cards existentes permanecem inalterados

  Cenário: Atualização de status — status divergente (happy path)
    Dado que um card já existe no Jira com status "To Do"
      E a atividade correspondente no Sensr foi movida para "DOING"
    Quando o serviço executa
    Então a transição "In Progress" é aplicada no card do Jira
      E o status é atualizado corretamente

  Cenário: Atualização de status — status igual (happy path)
    Dado que um card já existe no Jira com status "In Progress"
      E a atividade no Sensr também está com status "DOING"
    Quando o serviço executa
    Então nenhuma transição é aplicada
      E o card permanece inalterado

  Cenário: HTML inválido na descrição do Sensr (sad path)
    Dado que uma atividade do Sensr possui HTML malformado ou com tags não reconhecidas na descrição
    Quando o serviço processa essa atividade
    Então o HtmlHelper extrai o texto legível disponível
      E o card é criado no Jira sem tags visíveis na descrição
```

## 5. Resumo dos testes

| Escopo | Total CT | Happy | Sad | % Aprovação |
|---|---|---|---|---|
| SensrJiraSync — Fluxo de Migração e Sincronização | 5 | 4 | 1 | 100% |

## 6. Execução, análise e comunicação (VV 4, VV 5)

A execução dos testes por fase e o registro de defeitos estão consolidados em REL-VV-AASP-GOV-001 (5 defeitos catalogados, todos resolvidos antes da entrega). Os resultados foram analisados pelo Tech Lead e comunicados na homologação; os indicadores de qualidade alimentam a Medição (ver MED-AASP-GOV-001).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Plano de V&V consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
