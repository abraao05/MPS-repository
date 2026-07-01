# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Registro de Verificação de GQA
**Código:** GQA-AASP01-001
**Versão auditada:** 1.0
**Data do documento:** 15/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 1 | 0 |
| Conteúdo (CNT) | 1 | 2 | 0 | 0 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 1 | 0 | 0 | 0 |
| **TOTAL** | **2** | **3** | **1** | **0** |

**Veredicto:** NÃO-CONFORME CRÍTICO

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-GQA-01 — Verificação do GQA avalia presença dos documentos, não conformidade de conteúdo
**Severidade:** 🔴 Grave
**RAP impactado:** GQA RAP 2 — verificação de conformidade do processo, não apenas de presença de artefatos
**Localização:** Seção 3 — Verificação de produtos de trabalho
**Problema:** A tabela de verificação da seção 3 lista 20 produtos de trabalho e marca todos como "✅" ou "⏳" sem qualquer critério ou comentário específico. Isso constitui uma verificação de existência (checklist de inventário), não uma verificação de conformidade de processo. Uma auditoria GQA real deve verificar se os documentos contêm os elementos exigidos e se o processo foi seguido — não apenas se o arquivo existe. As NCs identificadas nesta auditoria externa (ex.: TAP sem assinatura, PLA sem encerramento, GCO com conflito de interesse, ATA002 classificada como AQU/GRE) deveriam ter sido identificadas pelo GQA interno, mas não foram.
**Evidência:** > "Termo de Abertura | TAP-AASP01-001 | ✅" — sem critérios de verificação registrados.
**Referência normativa:** GQA RAP 2 — verificação de conformidade com critérios definidos, não apenas presença.
**Ação corretiva:** Refazer a seção 3 com critérios explícitos para cada documento verificado: o que foi verificado, qual o critério, qual a evidência de conformidade. Identificar e registrar as não-conformidades encontradas (mesmo que menores).

---

### NC-GQA-02 — Resultado "Conforme" sem NCs registradas é inverossímil dado o estado do projeto
**Severidade:** 🔴 Grave
**RAP impactado:** GQA RAP 3 — não-conformidades identificadas e tratadas
**Localização:** Seção 4 — Achados; Seção 5 — Resultado
**Problema:** O GQA registra apenas 2 "oportunidades de melhoria" e declara "Conforme" para o projeto inteiro. Esta auditoria independente identificou múltiplas NCs moderadas e graves nos documentos do projeto — particularmente na classificação incorreta de processos MPS-SW nas atas (AQU/GRE em vez de GPR/VV), na ausência de seção de encerramento no PLA, no conflito de interesse do GCO, e na ausência de evidências externas de aceite. Um GQA que não identifica nenhuma dessas NCs não constitui auditoria independente efetiva. Isso levanta dúvida sobre a profundidade da verificação realizada.
**Evidência:** > "Conforme. A aderência ao processo-padrão e às adaptações registradas está confirmada para todos os marcos verificados."
**Referência normativa:** GQA RAP 3 — identificação e tratamento de não-conformidades é o objetivo central do GQA.
**Ação corretiva:** Realizar nova verificação GQA com critérios explícitos (especialmente: classificação de processos, evidências formais de aceite, completude do PLA, conflito de interesse no GCO). Registrar as NCs identificadas e seu tratamento.

---

### NC-GQA-03 — Processo declarado como "GPC" em vez de "GQA"
**Severidade:** 🟡 Moderada
**RAP impactado:** GQA — identificação correta
**Localização:** Cabeçalho — campo Processo MPS-SW
**Problema:** O cabeçalho registra "Processo MPS-SW: GPC — Garantia da Qualidade do Processo". No MPS.BR Nível C o processo se chama GQA (Garantia da Qualidade do Processo e do Produto). A sigla GPC não existe no MPS.BR Nível C — pode ser confundida com uma denominação interna Timeware. Esta inconsistência é sistêmica (aparece no índice também).
**Evidência:** > "Processo MPS-SW | GPC — Garantia da Qualidade do Processo (evidência de projeto)"
**Referência normativa:** MPS.BR Guia de Implementação — Nível C, processo GQA.
**Ação corretiva:** Corrigir para "GQA — Garantia da Qualidade do Processo e do Produto" em todos os documentos que citam este processo.

---

### NC-GQA-04 — Auditoria intermediária não verifica o GCO com critérios de independência
**Severidade:** 🟡 Moderada
**RAP impactado:** GQA RAP 2 — processos críticos verificados
**Localização:** Seção 2 — Verificação de aderência ao processo, bloco GCO
**Problema:** A verificação do GCO pela auditoria GQA valida apenas a presença de baselines e o controle de versões, mas não verifica o conflito de interesse estrutural da adaptação A-08 (Cezar Hiraki como responsável simultâneo pelo GCO e pelo code review). Esta é exatamente a situação que a independência do GQA deveria escrutinar.
**Evidência:** > "GCO 1 — itens de configuração identificados | GCO-AASP01-001 §3 (IC-01 a IC-06) | ✅ | GCO 2 — controle de versões e baselines | [...] | ✅ | GCO 3 — controle de mudanças | [...] | ✅"
**Referência normativa:** GQA RAP 2 — verificação deve cobrir aspectos de risco ao processo, não apenas conformidade estrutural.
**Ação corretiva:** Incluir verificação explícita da independência do GCO na próxima auditoria: documentar que a adaptação A-08 foi avaliada quanto ao risco de conflito de interesse.

---

### NC-GQA-05 — Uma única auditoria intermediária para projeto de 7 semanas com 3 sprints
**Severidade:** 🟢 Leve
**RAP impactado:** GQA RAP 1 — frequência de auditoria adequada
**Localização:** Seção 1 — Escopo da verificação
**Problema:** O GQA prevê uma auditoria intermediária (realizada em 15/06) e uma auditoria de encerramento (Sprint 3). Para um projeto de ~7 semanas com 3 sprints, uma auditoria por fase é mínimo aceitável, mas o GQA-AASP01-001 foi elaborado apenas em 15/06/2026 — cobrindo Sprint 1 e metade da Sprint 2. Não há evidência de auditoria GQA nas fases de Concepção/Planejamento (antes de 26/05) e início do projeto.
**Evidência:** > "Esta é a auditoria intermediária prevista para projetos de Nível 2 de adaptação (GUIA-GPC-001, §5.2); a auditoria de encerramento ocorrerá na Sprint 3."
**Referência normativa:** GQA RAP 1 — auditoria deve cobrir todo o ciclo de vida, incluindo planejamento.
**Ação corretiva:** Para projetos futuros, realizar primeira auditoria GQA ao final da fase de Planejamento (antes do início do desenvolvimento). Para este projeto: verificar se a auditoria de encerramento cobre adequadamente os aspectos não cobertos pela auditoria intermediária.
