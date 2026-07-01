# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Registro de Change Requests
**Código:** CR-AASP01-001
**Versão auditada:** 1.0
**Data do documento:** 06/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 1 | 1 | 0 |
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 0 | 0 | 0 |
| MPS.BR (MPS) | 1 | 0 | 0 | 0 |
| **TOTAL** | **1** | **2** | **1** | **0** |

**Veredicto:** NÃO-CONFORME CRÍTICO

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-CR-01 — Classificação como evidência de GRE (Gestão de Riscos) está incorreta
**Severidade:** 🔴 Grave
**RAP impactado:** GMUDS — controle formal de mudanças (processo de mudança)
**Localização:** Cabeçalho — campo Processo MPS-SW
**Problema:** O documento CR declara "Processo MPS-SW: GRE (evidência de projeto)". O controle de mudanças é evidência do processo GMUDS (Gerência de Mudanças), não de GRE (Gerência de Riscos). A classificação incorreta faz com que este documento seja encontrado quando o avaliador procura evidência de GRE, mas não seja encontrado quando procura evidência de GMUDS — o único processo que evidencia controle formal de escopo. Esta é uma NC grave porque o GMUDS é um processo obrigatório do Nível C.
**Evidência:** > "Processo MPS-SW | GRE (evidência de projeto)"
**Referência normativa:** MPS.BR Nível C — GMUDS (Gerência de Mudanças no Software) é processo obrigatório; evidência primária é o registro de CRs.
**Ação corretiva:** Corrigir para "Processo MPS-SW: GMUDS / GPR (evidência de controle de mudanças de escopo)".

---

### NC-CR-02 — Documento não atualizado desde 06/06/2026 — Sprint 2 pode ter gerado CRs implícitos
**Severidade:** 🟡 Moderada
**RAP impactado:** GMUDS RAP 1 — todas as mudanças formalizadas
**Localização:** Seção 2 — Registro Consolidado; data do documento
**Problema:** O documento está na versão 1.0, datado de 06/06/2026, e não foi atualizado na versão 1.1 como os demais documentos. Na data de auditoria (30/06/2026), a Sprint 2 já encerrou (20/06/2026) e a Sprint 3 está em andamento (desde 23/06/2026). O RAC-AASP01-001 (15/06/2026) mostra que AG-23 e AG-24 ainda não estavam implementados — mas o projeto continua. Se qualquer ajuste de escopo, prazo ou requisito ocorreu durante a Sprint 2 e Sprint 3 (mesmo que informal), ele deveria ter gerado ou explicitamente confirmado a não-geração de CRs.
**Evidência:** > "Nenhum Change Request foi registrado até 15/06/2026." — sem atualização para 30/06/2026.
**Referência normativa:** GMUDS RAP 1 — o registro de mudanças deve ser mantido atualizado.
**Ação corretiva:** Atualizar o CR para a data atual (30/06/2026), confirmando explicitamente que zero CRs foram gerados durante toda a Sprint 2 e início da Sprint 3, ou registrando os CRs que possam ter ocorrido.

---

### NC-CR-03 — Processo de CR prevê "assinatura ou confirmação formal por e-mail" mas nenhum mecanismo de arquivamento é definido
**Severidade:** 🟢 Leve
**RAP impactado:** GCO RAP 3 — evidências de aprovação arquivadas
**Localização:** Seção 4 — Processo de Gestão de Change Requests, passo 4
**Problema:** O processo prevê "assinatura (ou confirmação formal por e-mail)" para aprovação de CRs, mas não define onde esses e-mails ou assinaturas serão arquivados como evidência. Se um CR for aprovado, a evidência de aprovação ficaria em e-mail pessoal, inacessível ao avaliador MPS.BR.
**Evidência:** > "A mudança somente é aprovada com assinatura (ou confirmação formal por e-mail) de Marcos Turnes (AASP) e Abraão (Timeware). Mudanças sem aprovação dupla não são implementadas."
**Referência normativa:** GCO RAP 3 — evidências de aprovação de mudanças devem ser arquivadas com os itens de configuração.
**Ação corretiva:** Adicionar ao processo: "E-mails de aprovação arquivados no repositório MPS-SW como anexo ao CR aprovado, ou cópia do registro de aprovação no GitLab Issues."
