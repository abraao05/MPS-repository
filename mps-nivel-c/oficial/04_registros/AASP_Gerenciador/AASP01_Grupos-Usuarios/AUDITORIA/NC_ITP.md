# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Estratégia de Integração
**Código:** ITP-AASP01-001
**Versão auditada:** 1.2
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 2 | 1 | 0 |
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **4** | **1** | **0** |

**Veredicto:** NÃO-CONFORME

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-ITP-01 — Fase 2 (Sprint 2) permanece "Em andamento" quando Sprint 2 deveria ter encerrado
**Severidade:** 🟡 Moderada
**RAP impactado:** ITP — estado de integração atualizado
**Localização:** Seção 3 — Ordem de Integração dos Componentes, Fase 2
**Problema:** Na data de auditoria (30/06/2026), a Sprint 2 encerrou em 20/06/2026. O documento v1.2 de 24/06/2026 ainda marca AG-23 e AG-24 como "⏳ Em andamento". Se a Sprint 2 foi aceita, a Fase 2 deveria estar "✅ Concluído". Se não foi aceita, isso é um desvio que deve ser registrado. O documento não foi atualizado para refletir o resultado da Sprint 2.
**Evidência:** > "Fase 2 | S2 | Auditoria de ações (AG-23) | *(planejado — não implementado)* | [...] | ⏳ Em andamento"
**Referência normativa:** ITP — o documento de estratégia de integração deve refletir o estado real.
**Ação corretiva:** Atualizar o status da Fase 2 com o resultado da Sprint 2.

---

### NC-ITP-02 — Interface INT-01 sem contrato definido após 35 dias do início da Sprint 2
**Severidade:** 🟡 Moderada
**RAP impactado:** ITP RAP — contrato de integração definido antes da implementação
**Localização:** Seção 4.1 — Interface INT-01
**Problema:** O documento afirma que a Interface INT-01 (ms.auxo.usuarios → ms.temis.vinculos) tem "Tipo: HTTP REST (a definir na Sprint 2)", "Contrato: A finalizar no início da Sprint 2" e "Mecanismo de autenticação: a definir". Na data de auditoria, são 35 dias após o início da Sprint 2 (09/06/2026). O contrato ainda está "a definir" no documento oficial. Se a integração foi implementada na Sprint 2, o contrato deveria estar documentado. Se não foi, o ITP deve registrar o motivo do atraso.
**Evidência:** > "Tipo | HTTP REST (a definir na Sprint 2) | [...] | Contrato | A finalizar no início da Sprint 2 | [...] | Autenticação | Service-to-service (mecanismo a definir)"
**Referência normativa:** ITP — o contrato de integração deve ser definido antes da implementação (conforme A-03 do ADAP: "detalhes do contrato de API acordados no início da Sprint 2").
**Ação corretiva:** Atualizar a seção 4.1 com o contrato real definido na sessão técnica de 09/06/2026 (registrada no CAP como "Realizada"): endpoint de destino, DTO de requisição, autenticação, tratamento de falhas.

---

### NC-ITP-03 — Ambiente de integração contínua "previsto — ver GCO/MED" sem confirmação de implementação
**Severidade:** 🟡 Moderada
**RAP impactado:** ITP — ambiente de integração disponível
**Localização:** Seção 5 — Ambiente de Integração, linha CI
**Problema:** A linha de ambiente de integração contínua registra "SQL Server em container (CI) — *(previsto — ver GCO/MED)*", indicando que o ambiente CI com banco em container não estava implementado no momento da redação. O _DOSSIE-EVIDENCIAS confirma que o pipeline CI é uma lacuna de evidência. Se o CI não roda testes de integração em banco real, a estratégia de integração não está implementada conforme documentado.
**Evidência:** > "Integração contínua | Pipeline GitLab CI (build + testes a cada MR) | SQL Server em container (CI) | *(previsto — ver GCO/MED)*"
**Referência normativa:** ITP — ambientes de integração devem estar disponíveis conforme planejado.
**Ação corretiva:** Confirmar o status do ambiente de integração contínua com banco em container: implementado ou não? Se não implementado, atualizar o documento para refletir a realidade (ex.: testes de integração rodando em banco local dos desenvolvedores).

---

### NC-ITP-04 — Endereço IP do GitLab exposto novamente
**Severidade:** 🟢 Leve
**RAP impactado:** Segurança
**Localização:** Cabeçalho — campo Repositório
**Problema:** Mesmo problema do RASTR: IP interno `http://191.234.192.153` exposto.
**Evidência:** > "Repositório | GitLab · http://191.234.192.153/aasp/ms.auxo.usuarios"
**Referência normativa:** Boas práticas de segurança.
**Ação corretiva:** Substituir pelo hostname ou remover o IP.
