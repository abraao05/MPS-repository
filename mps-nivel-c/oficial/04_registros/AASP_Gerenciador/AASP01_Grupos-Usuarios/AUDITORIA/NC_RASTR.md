# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Matriz de Rastreabilidade
**Código:** RASTR-AASP01-001
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
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **3** | **1** | **1** |

**Veredicto:** NÃO-CONFORME

---

## OBSERVAÇÕES POSITIVAS

A RASTR-AASP01-001 é um dos pontos fortes do projeto. A rastreabilidade bidirecional RF→Endpoint→MR→Caso de Teste está completa para todos os requisitos da Sprint 1. O resumo de cobertura quantitativo (seção 5) é preciso e útil para avaliação.

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-RASTR-01 — RF-07 e RF-08 permanecem "Em andamento" apesar da Sprint 2 ter encerrado
**Severidade:** 🟡 Moderada
**RAP impactado:** REQ RAP 3 — rastreabilidade atualizada com estado real
**Localização:** Seção 2 — Rastreabilidade, RF-07 e RF-08
**Problema:** Na data de auditoria (30/06/2026), a Sprint 2 encerrou em 20/06/2026. A RASTR v1.3 (24/06/2026) ainda registra RF-07 e RF-08 como "⏳ Em andamento". Se a Sprint 2 foi aceita, esses requisitos deveriam estar "✅ Entregue" com MR e caso de teste preenchidos. Se não foram entregues, isso é um desvio de escopo que deve ser explicitado.
**Evidência:** > "RF-07 | AG-23 | Registrar auditoria [...] | *(planejado — não implementado)* | MR pendente | AUD-01 | S2 | ⏳ Em andamento"
**Referência normativa:** REQ RAP 3 — estado dos requisitos deve ser atualizado.
**Ação corretiva:** Atualizar RF-07 e RF-08 com o estado pós-Sprint 2 (entregue com aceite, ou postergado com justificativa).

---

### NC-RASTR-02 — RNF-01 validado por "Swagger/testes de performance" sem evidência formal arquivada
**Severidade:** 🟡 Moderada
**RAP impactado:** VV RAP 2 — validação de RNFs documentada com evidência
**Localização:** Seção 2.1 — RNF-01
**Problema:** O RNF-01 (tempo de resposta ≤ 500 ms) está marcado como "✅ Validado" com resultado "≤ 280 ms", com validação atribuída a "Swagger/testes de performance". O MED-AASP01-001 confirma esta medição, mas o _DOSSIE-EVIDENCIAS classifica a evidência de pipeline e performance como lacuna. Medições feitas via Swagger UI manualmente não constituem evidência formal de performance — especialmente porque foram feitas em "ambiente dev local", não em homologação ou produção.
**Evidência:** > "RNF-01 | Tempo de resposta ≤ 500 ms em condições normais de carga | [...] | Validado via Swagger/testes de performance (resultado obtido: ≤ 280 ms) | ✅ Validado"
**Referência normativa:** VV RAP 2 — validação de requisitos não funcionais deve ter evidência rastreável e metodologia documentada.
**Ação corretiva:** Registrar formalmente: (a) a ferramenta usada para medição (Swagger UI não é ferramenta de performance), (b) a metodologia (quantas requisições, percentil, carga), (c) o ambiente (dev local ≠ produção), (d) e arquivar a evidência. Ou qualificar o resultado como "indicativo em dev — validação formal em homologação na Sprint 3".

---

### NC-RASTR-03 — Endereço IP do GitLab exposto em campo público do documento
**Severidade:** 🟢 Leve
**RAP impactado:** GCO — segurança de configuração
**Localização:** Cabeçalho — campo Repositório
**Problema:** O campo "Repositório" expõe o endereço IP interno do GitLab: "http://191.234.192.153". IPs de infraestrutura interna não devem ser incluídos em documentos que possam ser compartilhados externamente (como pacotes de auditoria MPS.BR).
**Evidência:** > "Repositório | GitLab · http://191.234.192.153/aasp/ms.auxo.usuarios"
**Referência normativa:** Boas práticas de segurança da informação.
**Ação corretiva:** Substituir pelo hostname/domínio ou remover o endereço IP do campo de repositório, mantendo apenas "GitLab — aasp/ms.auxo.usuarios".

---

### NC-RASTR-04 — Rastreabilidade Sprint 1 completa e bidirecional
**Severidade:** 🔵 Obs
**RAP impactado:** —
**Localização:** Seção 2 — Sprint 1 completa; Seção 5 — Resumo
**Problema:** —
**Evidência:** A rastreabilidade RF→AG→Endpoint→MR→Caso de Teste está 100% completa para os 6 RFs da Sprint 1, com MRs !1 a !5 e 10 casos de teste identificados. O resumo quantitativo (seção 5) é preciso.
**Referência normativa:** —
**Ação corretiva:** Manter o padrão. Garantir a mesma completude para RF-07, RF-08 e RF-09 quando entregues.
