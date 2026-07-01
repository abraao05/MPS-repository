# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Cenários de Teste e Homologação
**Código:** CTQ-AASP01-001
**Versão auditada:** 1.3
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 1 | 2 | 1 |
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **3** | **2** | **1** |

**Veredicto:** NÃO-CONFORME

---

## OBSERVAÇÕES POSITIVAS

O CTQ-AASP01-001 tem a melhor estrutura de cenários de teste do conjunto. Cada cenário segue o padrão: ID, tipo, pré-condição, passos, resultado esperado, status e observação. Os cenários da Sprint 1 cobrem happy path e sad path. A rastreabilidade entre cenários e histórias (AG-20, AG-21, AG-22) está clara.

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-CTQ-01 — Sprint 2 mostra "3 cenários planejados, 3 não testados" quando Sprint 2 encerrou
**Severidade:** 🟡 Moderada
**RAP impactado:** VV — resultados de V&V documentados após execução
**Localização:** Seção 2 — Resumo de cobertura por sprint; Seções 6 e 7
**Problema:** Na data de auditoria (30/06/2026), a Sprint 2 deveria ter encerrado em 20/06/2026. Os cenários AUD-01, AUD-02 (AG-23) e INT-01 (AG-24) permanecem como "A executar" na versão 1.3 do documento (24/06/2026). Se a Sprint 2 foi concluída e aceita, os resultados de execução dos cenários devem estar registrados. Se os cenários não foram executados, isso indica que o aceite da Sprint 2 ocorreu sem cobertura completa de UAT.
**Evidência:** > "Sprint 2 | AG-23, AG-24 | 3 (planejados) | — | — | 3 | A executar"
**Referência normativa:** VV RAP — resultados de testes devem ser registrados.
**Ação corretiva:** Atualizar o CTQ com o resultado da execução dos cenários AUD-01, AUD-02 e INT-01, ou registrar formalmente que foram postergados para a Sprint 3 com justificativa.

---

### NC-CTQ-02 — Cenário GRP-07 (sad path — nome duplicado) não tem cenário equivalente de "grupo inativo com mesmo nome"
**Severidade:** 🟡 Moderada
**RAP impactado:** VV — cobertura adequada de casos de fronteira
**Localização:** Seção 3 — Cenários AG-20, GRP-07
**Problema:** O cenário GRP-07 testa a tentativa de criar um grupo com nome já existente (status ativo). Porém a RN-01 define "nome do grupo deve ser único no banco" sem distinguir se grupos excluídos (excluido=1) bloqueiam a reutilização do nome. Este cenário de fronteira — criar um grupo com o mesmo nome de um grupo já excluído via soft delete — não está coberto. É um caso de regressão que pode revelar bugs na validação de unicidade.
**Evidência:** > "GRP-07 | Tentar criar grupo com nome já existente — sad path | [...] | Grupo com nome 'Administradores' já existe no escritorio | [...] | HTTP 400; 'Grupo ja existe'"
**Referência normativa:** VV — cobertura de casos de fronteira.
**Ação corretiva:** Adicionar cenário GRP-08 (sad path): "Tentar criar grupo com mesmo nome de grupo excluído (excluido=1) — comportamento esperado: HTTP 200 (nome liberado) OU HTTP 400 (nome bloqueado mesmo após exclusão). Verificar e documentar a regra de negócio aplicável."

---

### NC-CTQ-03 — Cenários FUNC-01 e VINC-01/02 sem sad path definido
**Severidade:** 🟢 Leve
**RAP impactado:** VV — cobertura de fluxos alternativos
**Localização:** Seções 4 e 5 — AG-21 e AG-22
**Problema:** Os cenários de AG-21 (função do usuário) e AG-22 (vínculo) cobrem apenas happy path. Não há cenários sad path para: (a) `alterarfuncaodousuario` com função inválida (além do RV-002-01 que foi corrigido); (b) `removerusuario` para um usuário não vinculado; (c) vincular um usuário inexistente. O VV previa cobertura de fluxos alternativos.
**Evidência:** > "FUNC-01 | Alterar função do usuário no grupo — happy path | Happy | [...]"
**Referência normativa:** VV — cenários sad path para cada funcionalidade testada.
**Ação corretiva:** Adicionar cenários sad path: FUNC-02 (função inválida), VINC-03 (remover usuário não vinculado), VINC-04 (vincular usuário inexistente).

---

### NC-CTQ-04 — Cenários de Sprint 3 (REL-01, REL-02) sem critério de aprovação definido
**Severidade:** 🟢 Leve
**RAP impactado:** VV — critérios de aceite pré-definidos
**Localização:** Seção 7 — Cenários Sprint 3
**Problema:** Os cenários REL-01 e REL-02 estão registrados com tipo "Happy" e status "Planejado", mas sem pré-condição, passos, resultado esperado ou critério de aprovação. Como a Sprint 3 já iniciou (23/06/2026), esses cenários precisam ser detalhados para que Leonardo Francisco Pereira possa executá-los.
**Evidência:** > "REL-01 | AG-25 | Relatório consolidado de grupos com seus membros e funções em uma única resposta | Happy | Planejado — Sprint 3"
**Referência normativa:** VV — cenários devem ter critérios de aceite antes de serem executados.
**Ação corretiva:** Detalhar REL-01 e REL-02 com pré-condições, passos de execução e resultado esperado (campos obrigatórios na resposta, formato CSV) antes do início dos testes da Sprint 3.

---

### NC-CTQ-05 — Arquivo .md truncado na versão 1.3 do histórico
**Severidade:** 🔵 Obs
**RAP impactado:** GCO — integridade do documento
**Localização:** Histórico de revisões — versão 1.3
**Problema:** O arquivo .md foi lido com truncamento na descrição da versão 1.3 ("Reconciliação com o estado real do GitLab [...] com baseline pela tag sprint-1-aceite). A leitura do final do arquivo foi interrompida, indicando possível problema de conversão ou tamanho do arquivo.
**Evidência:** Observado durante leitura do arquivo — texto cortado no final.
**Referência normativa:** GCO — integridade dos documentos.
**Ação corretiva:** Verificar o arquivo .docx correspondente para confirmar integridade.
