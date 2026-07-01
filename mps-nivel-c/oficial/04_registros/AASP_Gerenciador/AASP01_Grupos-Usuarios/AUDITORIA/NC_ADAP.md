# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Registro de Adaptação ao Processo-Padrão
**Código:** ADAP-AASP01-001
**Versão auditada:** 1.1
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 1 | 1 | 0 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 1 | 0 | 0 |
| Coerência (CON) | 0 | 0 | 0 | 0 |
| MPS.BR (MPS) | 0 | 1 | 0 | 0 |
| **TOTAL** | **0** | **3** | **1** | **0** |

**Veredicto:** NÃO-CONFORME

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-ADAP-01 — Adaptação A-08 (acúmulo de papéis por Cezar Hiraki) não foi aprovada formalmente pelo SEPG
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR RAP 6 — adaptações aprovadas formalmente
**Localização:** Seção 2, item A-08
**Problema:** A adaptação A-08 permite que Cezar Hiraki acumule os papéis de Arquiteto, Tech Lead, DevOps, Revisor e GCO simultaneamente. Esta é a adaptação de maior impacto no processo — o responsável pelo GCO também é o responsável pelo code review e pelo desenvolvimento de arquitetura, criando potencial conflito de interesse na auditoria de configuração. O documento afirma que as adaptações "foram avaliadas e aprovadas pelo Gerente de Projeto antes do início das atividades", mas não registra se o SEPG (Silvio Baroni) também aprovou esta adaptação específica. O GQA-AASP01-001 não menciona análise da A-08.
**Evidência:** > "A-08 | Papeis separados de Gerente de Projeto, GCO, Arquiteto e Tech Lead | Cezar Hiraki acumula os papeis de Arquiteto, Tech Lead, DevOps, Revisor e GCO"
**Referência normativa:** ADAP — adaptações ao processo-padrão requerem aprovação do SEPG/responsável pelo processo organizacional, não apenas do GP.
**Ação corretiva:** Documentar a aprovação explícita do SEPG (Silvio Baroni) para a A-08, incluindo data e declaração de que os riscos foram avaliados e aceitos. Se o SEPG não aprovou, obter aprovação retroativa.

---

### NC-ADAP-02 — A-02 (Sprint Planning informal nas Sprints 1 e 2) já deveria ter sido encerrada
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR RAP 3 — formalização conforme planejado
**Localização:** Seção 2, item A-02
**Problema:** A adaptação A-02 previa "formalização completa a partir da S3". Na data do documento (24/06/2026), a Sprint 3 já foi iniciada (23/06/2026). O documento não registra que a formalização do Sprint Planning da Sprint 3 foi de fato realizada, deixando a adaptação em estado indefinido — ainda ativa ou já encerrada?
**Evidência:** > "A-02 | [...] formalização completa a partir da S3"
**Referência normativa:** GPR RAP 3 — adaptações temporárias devem ter prazo definido e ser encerradas formalmente quando o prazo se esgota.
**Ação corretiva:** Atualizar o ADAP-AASP01-001 com o status de encerramento da A-02: se o Sprint Planning da Sprint 3 foi formalizado (como planejado), registrar "Encerrada em 23/06/2026 — Sprint 3 iniciada com planejamento formal". Se não foi, registrar a pendência.

---

### NC-ADAP-03 — Adaptação A-06 cria dependência crítica não mitigada adequadamente
**Severidade:** 🟡 Moderada
**RAP impactado:** GCO RAP 3 — documentação técnica rastreável
**Localização:** Seção 4, impacto A-06
**Problema:** A adaptação A-06 define que os MRs do GitLab servem como "documentação viva" para especificações de baixo nível. A mitigação prevista é "MRs exportados como PDF e arquivados no pacote documental MPS-SW a cada baseline". Porém o dossiê de evidências (_DOSSIE-EVIDENCIAS_AASP01.md) confirma que os MRs **não foram exportados como PDF** — os MRs são evidências citadas nos documentos mas não materializadas no pacote documental. Esta mitigação não foi implementada.
**Evidência:** No _DOSSIE-EVIDENCIAS: > "pull_requests/ (MR) | ⚠️ falta Jira" — evidência dos MRs está incompleta.
**Referência normativa:** GCO RAP 3 — itens de configuração devem ser recuperáveis. Documentos que dependem de sistemas externos (GitLab) precisam de cópia offline ou link permanente verificável.
**Ação corretiva:** Implementar a mitigação prometida: exportar os MRs !1 a !5 como PDF e incluir no pacote documental MPS-SW. Ou atualizar o ADAP para registrar que a mitigação mudou (ex.: link permanente ao GitLab).

---

### NC-ADAP-04 — "Time de Melhoria Contínua" sem identificação nominal
**Severidade:** 🟢 Leve
**RAP impactado:** GCO RAP 2
**Localização:** Histórico de revisões — versão 1.1
**Problema:** Problema sistêmico: autor não identificado nominalmente.
**Evidência:** > "1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação..."
**Referência normativa:** GCO RAP 2.
**Ação corretiva:** Identificar o responsável nominal.
