# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Índice de Registros do Projeto — Mapa de Registros
**Código:** INDICE-AASP01-001
**Versão auditada:** 1.1
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 1 | 0 |
| Conteúdo (CNT) | 0 | 1 | 1 | 0 |
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **3** | **2** | **0** |

**Veredicto:** NÃO-CONFORME

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-INDICE-01 — Status "em execução" desatualizado no cabeçalho
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR — atualização do plano
**Localização:** Seção 1 — Contexto e momento do projeto
**Problema:** O documento afirma "Status atual (15/06/2026): em execução — Sprint 1 concluída e aceita; Sprint 2 em andamento". A data de referência interna é 15/06/2026, mas o documento foi atualizado em 24/06/2026 (versão 1.1). Na data de auditoria (30/06/2026) a Sprint 2 já deveria ter sido encerrada (período 09/06–20/06/2026) e a Sprint 3 estar em andamento. O índice não reflete a realidade do projeto na data do documento.
**Evidência:** > "Status atual (15/06/2026): em execução — Sprint 1 concluída e aceita (06/06/2026); Sprint 2 em andamento; Sprints 3 e 4 planejadas."
**Referência normativa:** GPR RAP 4 — o plano deve refletir o estado atual; atualização deve ser feita quando o estado muda.
**Ação corretiva:** Atualizar a seção 1 para refletir o status em 24/06/2026 (data da versão 1.1): Sprint 2 encerrada (ou em encerramento), Sprint 3 em andamento. Remover a data 15/06/2026 do corpo do documento — ela é a data da v1.0, não da v1.1.

---

### NC-INDICE-02 — Referência a "Sprints 3 e 4" quando há apenas 3 sprints
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR RAP 1 — plano consistente com o escopo aprovado
**Localização:** Seção 1 — Contexto e momento do projeto
**Problema:** O índice menciona "Sprints 3 e 4 planejadas", mas todos os demais documentos (PLA, TAP, RAC, MED, REQ, VV) descrevem o projeto como tendo 3 sprints (S1, S2, S3). Não há Sprint 4 em nenhum outro artefato. Esta inconsistência cria ambiguidade sobre o escopo real do projeto.
**Evidência:** > "Sprint 1 concluída e aceita (06/06/2026); Sprint 2 em andamento; Sprints 3 e 4 planejadas."
**Referência normativa:** Coerência entre documentos — o índice é o ponto de controle central; inconsistência aqui contamina todos os documentos referenciados.
**Ação corretiva:** Corrigir para "Sprint 3 planejada" (sem Sprint 4), alinhando com PLA-AASP01-001, TAP-AASP01-001 e RAC-AASP01-001.

---

### NC-INDICE-03 — "Time de Melhoria Contínua" como autor de atualização sem identificação nominal
**Severidade:** 🟢 Leve
**RAP impactado:** GCO RAP 1 — identificação de responsável por alteração
**Localização:** Histórico de Revisões — versão 1.1
**Problema:** O autor da versão 1.1 é registrado como "Time de Melhoria Contínua", sem identificar a pessoa física responsável. O processo GCO exige rastreabilidade nominal para alterações em itens de configuração.
**Evidência:** > "1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab"
**Referência normativa:** GCO RAP 2 — cada versão de item de configuração deve ter responsável identificável nominalmente.
**Ação corretiva:** Identificar o responsável nominal pela alteração da versão 1.1 (ex.: "Silvio Baroni — Time de Melhoria Contínua / SEPG" ou o nome real).

---

### NC-INDICE-04 — Contagem de artefatos inconsistente (19 vs 21 listados)
**Severidade:** 🟢 Leve
**RAP impactado:** GCO RAP 1 — inventário de itens de configuração
**Localização:** IC-05 no GCO-AASP01-001 vs tabela da Seção 2
**Problema:** O GCO-AASP01-001 registra "19 artefatos (18 .docx + 1 .xlsx)" na BL-02, mas o índice lista 23 itens (21 entregues + 2 previstos). Mesmo excluindo os previstos (TAE e LI), o número é 21, não 19. Os dois artefatos não contabilizados no GCO são provavelmente o GQA-AASP01-001 (Registro de GQA) e o CAP-AASP01-001 (Registro de Capacitação) — ambos presentes no índice e no repositório. Esta inconsistência compromete a integridade do inventário de configuração.
**Evidência:** > "IC-05 | Documentação MPS-SW | [...] Total: 19 artefatos (18 .docx + 1 .xlsx)."
**Referência normativa:** GCO RAP 1 — todos os itens de configuração devem estar identificados na baseline.
**Ação corretiva:** Reconciliar a contagem: o GCO deve ser atualizado para 21 artefatos (ou 23 incluindo TAE e LI previstos). Identificar nominalmente quais dos 23 documentos estão incluídos na BL-02.

---

### NC-INDICE-05 — Processo MPS-SW do GQA listado como "GPC" na tabela
**Severidade:** 🟡 Moderada
**RAP impactado:** GQA — identificação correta do processo
**Localização:** Tabela da Seção 2, linha 18 (GQA-AASP01-001)
**Problema:** O índice associa o GQA-AASP01-001 ao processo "GPC", mas o próprio documento GQA-AASP01-001 afirma no cabeçalho "Processo MPS-SW: GPC — Garantia da Qualidade do Processo". O processo correto no MPS.BR Nível C é GQA (Garantia da Qualidade do Processo e do Produto), não GPC. O uso inconsistente da sigla pode causar confusão em revisão de avaliação.
**Evidência:** > "18 | GQA-AASP01-001 | Registro de Verificação de GQA | GPC | ✅"
**Referência normativa:** MPS.BR Guia de Implementação — Nível C: processo denominado GQA (Garantia da Qualidade do Processo e do Produto).
**Ação corretiva:** Padronizar a sigla do processo em todos os documentos: usar GQA (não GPC). Atualizar o índice e o cabeçalho do próprio GQA-AASP01-001.
