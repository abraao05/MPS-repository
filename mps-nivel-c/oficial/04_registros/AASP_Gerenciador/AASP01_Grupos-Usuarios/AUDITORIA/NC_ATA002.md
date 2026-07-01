# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Ata de Aceite — Sprint 1
**Código:** ATA-AASP01-002
**Versão auditada:** 1.1
**Data do documento:** 06/06/2026 (reunião) / versão 1.1 não datada separadamente
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 1 | 0 | 0 |
| Conteúdo (CNT) | 0 | 1 | 1 | 0 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 1 | 0 | 0 | 0 |
| **TOTAL** | **1** | **3** | **1** | **0** |

**Veredicto:** NÃO-CONFORME CRÍTICO

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-ATA002-01 — Processo MPS-SW declarado como "AQU/GRE" — mesmo erro da ATA-001
**Severidade:** 🔴 Grave
**RAP impactado:** GPR / VV — classificação correta do aceite como evidência
**Localização:** Cabeçalho — campo Processo MPS-SW
**Problema:** A ata de aceite da Sprint 1 é uma evidência crítica de VV (validação formal pelo cliente) e GPR (conclusão de fase). O processo declarado "AQU / GRE" está incorreto e pode fazer com que avaliadores não encontrem esta evidência ao verificar o RAP de validação. AQU (Aquisição) não se aplica em nenhum contexto a esta ata. Esta classificação incorreta é grave porque o aceite formal é um dos RAPs mais verificados na avaliação MPS.BR.
**Evidência:** > "Processo MPS-SW | AQU / GRE (evidência de projeto)"
**Referência normativa:** VV RAP 3 — validação com confirmação pelo cliente documentada. GPR RAP 6 — conclusão de fase documentada.
**Ação corretiva:** Corrigir para "Processo MPS-SW: VV / GPR (evidência de validação formal e aceite de fase)".

---

### NC-ATA002-02 — Aceite por declaração verbal em reunião Teams sem assinatura ou e-mail formal
**Severidade:** 🟡 Moderada
**RAP impactado:** VV RAP 3 — validação com evidência formal
**Localização:** Seção 7 — Aceite Formal
**Problema:** O aceite é registrado como "declaração de aceite (registrada em reunião via Microsoft Teams em 06/06/2026)". Embora o trecho da declaração de Marcos Turnes esteja transcrito na ata, não há evidência de que Marcos Turnes assinou digitalmente o documento, enviou e-mail de confirmação, ou que a gravação da reunião Teams está disponível. O _DOSSIE-EVIDENCIAS confirma que as comunicações estão faltando como evidência externa: "❌ falta comunicação+Jira" para ATA-002.
**Evidência:** > "Confirmo o aceite formal dos entregáveis da Sprint 1 [...] — Marcos Turnes, AASP, 06/06/2026"
**Referência normativa:** VV RAP 3 — o aceite do cliente deve ser evidenciado por canal rastreável (e-mail, assinatura digital, ou referência a gravação arquivada).
**Ação corretiva:** Obter e arquivar: (a) e-mail de confirmação de Marcos Turnes do aceite da Sprint 1, OU (b) referência ao registro da gravação Teams arquivada, OU (c) assinatura digital do documento. Registrar a referência no documento.

---

### NC-ATA002-03 — Histórico de revisões com versão 1.1 sem data separada identificável
**Severidade:** 🟡 Moderada
**RAP impactado:** GCO RAP 2 — rastreabilidade de versões
**Localização:** Histórico de Revisões — versão 1.1
**Problema:** O histórico de revisões da ATA-AASP01-002 foi truncado no arquivo .md lido (o texto termina com "aceite c#" — corte no arquivo). Não é possível verificar completamente a versão 1.1. A versão 1.0 está datada de 06/06/2026, e a v1.1 pela descrição padrão dos demais documentos seria de 24/06/2026. Este corte no documento pode indicar problema de integridade do arquivo.
**Evidência:** > "1.0 | 06/06/2026 | Abraão | Versão inicial — ata de aceite formal da Sprint 1 (AG-20, AG-21, AG-22); aceite c#" — texto truncado.
**Referência normativa:** GCO — integridade dos documentos.
**Ação corretiva:** Verificar e corrigir o arquivo .md e .docx correspondente. O truncamento indica possível problema de conversão ou edição.

---

### NC-ATA002-04 — Próximos passos sem rastreamento posterior
**Severidade:** 🟢 Leve
**RAP impactado:** GPR RAP 4 — acompanhamento de ações
**Localização:** Seção 8 — Próximos Passos
**Problema:** A seção de próximos passos lista 5 ações com responsável e prazo. Nenhuma versão posterior do documento registra o status dessas ações. Em particular: "Confirmar ambiente de homologação Sprint 2 recebido e validado — Leonardo Francisco Pereira — 11/06/2026" — o RAC e o REL-VV indicam que a Sprint 2 estava em andamento mas sem testes UAT executados até 15/06/2026, sugerindo que o ambiente pode não ter sido confirmado no prazo.
**Evidência:** > "Confirmar ambiente de homologação Sprint 2 recebido e validado | Leonardo Francisco Pereira (AASP) | 11/06/2026" — sem confirmação de cumprimento.
**Referência normativa:** GPR RAP 4 — ações devem ser acompanhadas até conclusão.
**Ação corretiva:** Adicionar coluna "Status" e registrar cumprimento ou pendência de cada ação.
