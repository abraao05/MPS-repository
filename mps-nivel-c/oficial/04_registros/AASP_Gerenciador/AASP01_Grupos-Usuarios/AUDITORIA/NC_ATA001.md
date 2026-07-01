# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Ata de Kickoff
**Código:** ATA-AASP01-001
**Versão auditada:** 1.1
**Data do documento:** 19/05/2026 (reunião) / 24/06/2026 (revisão 1.1)
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 1 | 0 |
| Conteúdo (CNT) | 0 | 1 | 1 | 0 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 1 |
| **TOTAL** | **0** | **2** | **2** | **1** |

**Veredicto:** NÃO-CONFORME

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-ATA001-01 — Processo MPS-SW declarado como "AQU/GRE" mas a ata é evidência de GPR/ORG
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR — classificação correta de evidências
**Localização:** Cabeçalho — campo Processo MPS-SW
**Problema:** A ata de kickoff declara "Processo MPS-SW: AQU / GRE (evidência de projeto)". AQU (Aquisição) não se aplica — o projeto não tem subcontratação. GRE (Gerência de Requisitos) é parcialmente pertinente, mas a ata de kickoff é primariamente evidência de GPR (abertura formal do projeto) e ORG (comunicação organizacional). A classificação incorreta pode dificultar a localização desta evidência durante a avaliação.
**Evidência:** > "Processo MPS-SW | AQU / GRE (evidência de projeto)"
**Referência normativa:** GPR RAP 1 — início formal do projeto requer evidência de kickoff, classificada como GPR.
**Ação corretiva:** Corrigir para "Processo MPS-SW: GPR / ORG (evidência de início formal do projeto e comunicação)".

---

### NC-ATA001-02 — Ações imediatas sem confirmação de cumprimento registrada
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR RAP 4 — monitoramento de ações
**Localização:** Seção 5 — Ações Imediatas
**Problema:** A seção 5 lista 9 ações com responsável e prazo (a maioria até 23/05/2026 e 26/05/2026). Nenhuma ação tem coluna de "Status" ou "Confirmação de cumprimento". Na revisão 1.1 (24/06/2026) — um mês após todos os prazos — as ações não foram marcadas como cumpridas ou pendentes. O ADAP-AASP01-001 confirma indiretamente que alguns acessos foram providenciados (banco auxo3 acessível desde Sprint 1), mas esta confirmação não está na própria ata.
**Evidência:** > "| Providenciar acesso ao repositório GitLab [...] | Marcos Turnes | 23/05/2026 |" — sem coluna de status.
**Referência normativa:** GPR RAP 4 — itens de ação devem ter acompanhamento documentado.
**Ação corretiva:** Adicionar coluna "Status" à tabela de ações imediatas, marcando cada ação como "Cumprida" com a data real de cumprimento, ou registrar pendências.

---

### NC-ATA001-03 — "Todos os dias úteis" para daily não especifica quando a ata foi atualizada para refletir mudanças
**Severidade:** 🟢 Leve
**RAP impactado:** GPR — plano de comunicação
**Localização:** Seção 3.4 — Cadência de Trabalho
**Problema:** A ata registra "Daily Standup: todos os dias úteis às 09h30 via Microsoft Teams (todas as partes — Abraão, Cezar e os desenvolvedores; quando necessário Marcos Turnes e Leonardo Francisco Pereira)". O PLA-AASP01-001 registra a mesma cadência, mas o _DOSSIE-EVIDENCIAS indica que não há evidência de realização das dailies. A ata não registra se esta cadência foi mantida ou alterada ao longo do projeto.
**Evidência:** > "Daily Standup: todos os dias úteis as 09h30 via Microsoft Teams"
**Referência normativa:** GPR RAP 5 — comunicação planejada deve ser evidenciada.
**Ação corretiva:** Observação — não é NC crítica, mas a ausência de evidência das dailies (mencionada no dossiê de evidências) deve ser resolvida para garantir que o processo de comunicação seja comprovável.

---

### NC-ATA001-04 — GQA não incluído nas partes interessadas do kickoff
**Severidade:** 🔵 Obs
**RAP impactado:** GQA RAP 1 — auditor independente informado desde o início
**Localização:** Seção 1 — Participantes
**Problema:** O auditor GQA (Silvio Baroni — SEPG) não está listado como participante do kickoff, o que é aceitável dado que o GQA é independente. Porém, não há menção de que o SEPG foi notificado sobre o início do projeto — requisito mínimo para que o GQA possa planejar a auditoria intermediária (que ocorre em 15/06/2026).
**Evidência:** Lista de participantes sem Silvio Baroni.
**Referência normativa:** GQA — auditor deve ter acesso desde o início do projeto.
**Ação corretiva:** Observação para futuros projetos: registrar na ata de kickoff o canal pelo qual o SEPG foi notificado sobre o início do projeto.
