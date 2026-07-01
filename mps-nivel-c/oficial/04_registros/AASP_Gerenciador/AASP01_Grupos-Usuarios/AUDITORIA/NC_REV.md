# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Registro de Revisão Técnica
**Código:** REV-AASP01-001
**Versão auditada:** 1.3
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 1 | 1 | 1 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 1 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **3** | **1** | **1** |

**Veredicto:** NÃO-CONFORME

---

## OBSERVAÇÕES POSITIVAS

O REV-AASP01-001 é o documento mais bem evidenciado do projeto. Cada revisão (REV-001, REV-002, REV-003) tem: data, MRs cobertos, revisor, autor do código, resultado, lista de achados com ID/severidade/ação/status. A rastreabilidade MR→achado→resolução é completa para todos os 5 MRs da Sprint 1. O consolidado da seção 5 confirma 0 achados P1 e 100% de resolução antes do merge.

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-REV-01 — Versão 1.2 e 1.3 criadas na mesma data (24/06/2026) com descrições sobrepostas
**Severidade:** 🟡 Moderada
**RAP impactado:** GCO RAP 2 — histórico de versões rastreável
**Localização:** Histórico de revisões — versões 1.2 e 1.3
**Problema:** O histórico registra duas versões na mesma data (24/06/2026): v1.2 "Reconciliação com o GitLab: 2 revisores por MR" e v1.3 "Reconciliação com o estado real do GitLab". Duas versões criadas no mesmo dia com descrições similares sugerem que foram criadas pela mesma pessoa/ferramenta de forma artificial, não por eventos de evolução distintos. Isso prejudica a rastreabilidade de "quem mudou o quê e por quê".
**Evidência:** > "1.2 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o GitLab: 2 revisores por MR — Cezar (TL) + Abraão (GP) (antes 1). | 1.3 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab"
**Referência normativa:** GCO RAP 2 — cada versão representa uma mudança distinta com motivo claro.
**Ação corretiva:** Consolidar as alterações das v1.2 e v1.3 em uma única versão com descrição completa das mudanças realizadas. Evitar criar múltiplas versões no mesmo dia sem distinção clara de motivo.

---

### NC-REV-02 — Cezar Hiraki e Abraão como revisores contradiz a adaptação A-07 (revisor único)
**Severidade:** 🟡 Moderada
**RAP impactado:** ADAP — consistência entre processo adaptado e registros
**Localização:** Seções 2, 3 e 4 — campo "Revisor responsável"
**Problema:** O ADAP-AASP01-001 A-07 define "Revisor único (Cezar Hiraki como Tech Lead) nos MRs de código crítico; revisão cruzada entre os desenvolvedores nos MRs de menor risco". A versão 1.2 do REV foi criada exatamente para reconciliar "2 revisores por MR — Cezar (TL) + Abraão (GP) (antes 1)". Agora o REV diz que TODOS os MRs foram revisados por 2 pessoas (Cezar + Abraão), o que contradiz a adaptação A-07 que previa revisor único. O GCO também registra "Mínimo de 2 revisores aprovados". Esta inconsistência entre ADAP (1 revisor) e REV/GCO (2 revisores) é sistêmica e não foi resolvida no ADAP.
**Evidência:** > "Revisor responsável | Cezar Hiraki (Tech Lead — Timeware) e Abraão (GP — Timeware)" em todas as revisões.
**Referência normativa:** ADAP A-07 vs REV v1.2/GCO — inconsistência não reconciliada.
**Ação corretiva:** Atualizar o ADAP-AASP01-001: ou corrigir A-07 para "2 revisores (Cezar Hiraki + Abraão)" removendo a adaptação, ou manter A-07 com "revisor único" e corrigir o REV/GCO para refletir a realidade da adaptação. O ADAP é o documento de referência — ele deve estar correto.

---

### NC-REV-03 — Seção 6 (próximas revisões — Sprint 2) sem atualização de resultado
**Severidade:** 🟢 Leve
**RAP impactado:** VV — registro de revisões para todas as sprints
**Localização:** Seção 6 — Próximas Revisões Sprint 2
**Problema:** A seção 6 prevê revisões dos MRs !6 (AG-23) e !7 (AG-24) na Sprint 2. Na data de auditoria (30/06/2026), a Sprint 2 encerrou. Se os MRs foram criados e revisados, os achados devem estar registrados neste documento. A ausência de dados é consistente com a lacuna geral de informações da Sprint 2.
**Evidência:** > "Revisões técnicas previstas para a Sprint 2, cobrindo as historias AG-23 e AG-24 — ambas ainda não implementadas."
**Referência normativa:** VV — registro de revisões deve ser mantido por sprint.
**Ação corretiva:** Adicionar seção "REV-004" com os resultados das revisões dos MRs da Sprint 2.

---

### NC-REV-04 — Qualidade geral do documento é exemplar
**Severidade:** 🔵 Obs
**RAP impactado:** —
**Localização:** Documento inteiro
**Problema:** —
**Evidência:** O registro de achados com ID, severidade P2/P3 (0 achados P1), ação tomada e status de resolução é rastreável e bem estruturado. A organização por MR e a cross-referência com CTQ (GRP-07, FUNC-01, VINC-02) demonstra integração efetiva entre os documentos de V&V.
**Referência normativa:** —
**Ação corretiva:** Manter o padrão para a Sprint 2.
