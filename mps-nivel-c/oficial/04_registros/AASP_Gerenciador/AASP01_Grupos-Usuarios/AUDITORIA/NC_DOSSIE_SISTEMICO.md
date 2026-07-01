# NOTA SISTÊMICA DE AUDITORIA — Dossiê de Evidências e Plano de Regeneração
## Documentos: _DOSSIE-EVIDENCIAS_AASP01.md e _PLANO-REGENERACAO_AASP01.md
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## ACHADO CRÍTICO — EXISTÊNCIA DOS DOCUMENTOS _DOSSIE E _PLANO

A existência de dois documentos internos — _DOSSIE-EVIDENCIAS_AASP01.md e _PLANO-REGENERACAO_AASP01.md — no mesmo repositório dos artefatos MPS.BR é um achado de auditoria de primeira ordem.

### O que esses documentos revelam

O _DOSSIE-EVIDENCIAS classifica sistematicamente as evidências do projeto como:
- **✅ Já cobertos:** commits, branches, tags, code review (7 imagens), diagrama de arquitetura, Swagger (lista).
- **⚠️ Faltando:** pipeline CI verde, migrations SQL, Swagger de execução (request/response), Jira backlog/sprint.
- **❌ Lacunas críticas:** pipeline + Jira (destrava 7 documentos), comunicações (kickoff Teams, aceite PO via e-mail/Teams).

O _PLANO-REGENERACAO documenta que os documentos MPS.BR foram gerados com endpoints fictícios (REST clássico: `POST /grupos`→201, `GET /grupos/{id}`→200, `DELETE /grupos/{id}`→204) e depois **reconciliados** com o código real (rota `api/gerenciar/grupos`, verbos GET/POST, status 200/400).

### Implicação para a auditoria

1. **Retroconfecção documental confirmada:** Os documentos MPS.BR (REQ, RASTR, PCP, CTQ, VV, ITP, REL-VV, GCO) foram gerados com uma visão fictícia da API e posteriormente reescritos para bater com o código real. Isso não é necessariamente fraudulento — é documentação pós-implementação, prática comum em projetos ágeis — mas deve ser declarado formalmente no ADAP ou em uma adaptação adicional (A-09: "documentação elaborada em ciclo de retrospectiva após implementação").

2. **Evidências externas ausentes identificadas pelo próprio time:** O dossiê lista 6 categorias de lacunas de evidência. A existência deste documento demonstra autoconsciência do problema, mas não o resolve. As lacunas continuam presentes.

3. **Risco de avaliação:** Se um avaliador MPS.BR encontrar o _PLANO-REGENERACAO no pacote documental, a credibilidade de todo o projeto pode ser questionada. Este documento deve ser tratado como artefato interno de trabalho, não como parte do pacote de auditoria.

### Ação corretiva sistêmica

1. Mover _DOSSIE-EVIDENCIAS e _PLANO-REGENERACAO para pasta interna `_INTERNO/` ou removê-los do pacote documental de auditoria.
2. Adicionar adaptação A-09 no ADAP-AASP01-001: "Documentação técnica (REQ, PCP, CTQ, RASTR, VV, ITP, REL-VV) elaborada em ciclo de retroconfecção após cada sprint, com base no código implementado, e não antes da implementação. Justificativa: equipe enxuta com entrega prioritária; documentação mantida consistente com o código real. Risco: período sem documentação formal paralela à implementação. Mitigação: code reviews e MRs como documentação de design in-progress."
3. Implementar as ações do dossiê de evidências: exportar pipeline CI, migrations SQL, e obter confirmação formal do aceite da Sprint 1 por e-mail de Marcos Turnes.
