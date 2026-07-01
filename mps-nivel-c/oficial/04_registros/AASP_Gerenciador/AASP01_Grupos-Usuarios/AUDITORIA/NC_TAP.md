# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Termo de Abertura do Projeto
**Código:** TAP-AASP01-001
**Versão auditada:** 1.1
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 1 | 0 |
| Conteúdo (CNT) | 0 | 2 | 1 | 0 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 1 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 1 |
| **TOTAL** | **0** | **4** | **2** | **1** |

**Veredicto:** NÃO-CONFORME

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-TAP-01 — Contato do GP "a confirmar" após TAP aprovado
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR RAP 1 — papéis e responsabilidades identificados
**Localização:** Seção 3 — Partes Interessadas, linha GP
**Problema:** O campo de contato do Gerente de Projeto Abraão está registrado como "a confirmar" no TAP aprovado em 19/05/2026 e não foi corrigido nem na versão 1.1 (24/06/2026). Um TAP aprovado com informações de contato do GP indefinidas compromete o requisito de identificação completa das partes interessadas. Na data de auditoria (30/06/2026) — mais de 40 dias após a aprovação — o campo permanece vazio.
**Evidência:** > "Gerente de Projeto / TL | Abraão (GP) · Cezar Hiraki (TL) | Timeware | Abraão (a confirmar) · contato@cezarvelazquez.com.br"
**Referência normativa:** GPR RAP 1 — o plano de projeto deve identificar as partes interessadas e seus contatos. TAP aprovado deve conter informações completas.
**Ação corretiva:** Registrar o e-mail real do Gerente de Projeto Abraão. Se o nome completo não foi divulgado nos documentos, adicionar ao menos o e-mail corporativo (padrão: nome.sobrenome.timeware@outlook.com por analogia aos outros membros).

---

### NC-TAP-02 — Auditoria/log como entrega sem indicação de sprint no escopo
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR RAP 1 — escopo claramente definido
**Localização:** Seção 2.1 — Incluído, item 4
**Problema:** A entrega "Auditoria e log de operações" na tabela de escopo é seguida da nota "(planejado — Sprint 2)", mas esta nota não está presente na própria célula — está documentada de forma inconsistente. Mais grave: no REQ-AASP01-001 (RF-07) e no PCP-AASP01-001, a auditoria é claramente marcada como "Planejado — Sprint 2 (ainda não implementado)". O TAP apresenta a auditoria como entrega plena no escopo sem qualificá-la adequadamente como futura, podendo gerar expectativas incorretas no cliente.
**Evidência:** > "4 | Auditoria e log de operações (planejado — Sprint 2)"
**Referência normativa:** GPR RAP 1 — o escopo deve ser claro e não ambíguo.
**Ação corretiva:** Mover a nota "(planejado — Sprint 2)" para dentro da célula da tabela, tornando explícito que a auditoria ainda não foi implementada na data do TAP v1.1 (24/06/2026).

---

### NC-TAP-03 — Data do documento (24/06/2026) é a data da versão 1.1, não a data de aprovação do TAP
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR RAP 1 — rastreabilidade do documento
**Localização:** Cabeçalho — campo Data
**Problema:** O cabeçalho registra Data = 24/06/2026, que é a data da revisão 1.1 (reconciliação), mas o TAP foi aprovado em 19/05/2026 (versão 1.0). Um TAP é um documento de abertura cujo valor temporal é a data de aprovação. Registrar a data da última revisão no campo "Data" do cabeçalho oculta a data de aprovação original e pode induzir o avaliador a acreditar que o TAP foi aprovado apenas em 24/06/2026 — após o início do projeto.
**Evidência:** > "Versão | 1.1 | Data | 24/06/2026 | Status | Aprovado"
**Referência normativa:** GPR RAP 1 — data de aprovação deve ser rastreável. O histórico de revisões documenta versões; o campo Data do cabeçalho deve refletir a data de criação/aprovação original (ou ambas devem ser claramente distinguidas).
**Ação corretiva:** Adicionar campo "Data de Aprovação: 19/05/2026" no cabeçalho, distinguindo-o da data da última revisão.

---

### NC-TAP-04 — Ausência de assinatura ou evidência formal de aprovação
**Severidade:** 🟢 Leve
**RAP impactado:** GPR RAP 1 — aprovação formal registrada
**Localização:** Cabeçalho — campo Status; ausência de seção de assinaturas
**Problema:** O TAP declara "Status: Aprovado", mas não há seção de assinaturas, nem referência a e-mail, ata ou qualquer evidência que documente quem aprovou e quando. A ATA-AASP01-001 confirma a realização do Kickoff mas não menciona aprovação explícita do TAP como item de pauta.
**Evidência:** > "Status | Aprovado"
**Referência normativa:** GPR RAP 1 — aprovação formal com identificação dos aprovadores é evidência obrigatória.
**Ação corretiva:** Adicionar seção de aprovação ao TAP com: nome do aprovador (Marcos Turnes — PO AASP), data (19/05/2026) e canal de aprovação (Teams/e-mail). Ou referenciar o item da ATA-AASP01-001 onde o TAP foi formalmente aprovado.

---

### NC-TAP-05 — "Time de Melhoria Contínua" como autor sem identificação nominal
**Severidade:** 🟢 Leve
**RAP impactado:** GCO RAP 2 — rastreabilidade de alterações
**Localização:** Histórico de Revisões — versão 1.1
**Problema:** Mesmo problema sistêmico identificado em todos os documentos com revisão 1.1: o autor "Time de Melhoria Contínua" não identifica nominalmente o responsável pela alteração.
**Evidência:** > "1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab"
**Referência normativa:** GCO RAP 2 — responsável pela alteração deve ser identificado nominalmente.
**Ação corretiva:** Identificar o responsável nominal pela alteração da v1.1.

---

### NC-TAP-06 — GQA não auditou o TAP explicitamente
**Severidade:** 🔵 Obs
**RAP impactado:** GQA RAP 1 — produtos de trabalho verificados
**Localização:** GQA-AASP01-001 §3 (lista de produtos verificados)
**Problema:** O GQA-AASP01-001 lista o TAP como "✅ Conforme" na tabela de verificação de produtos de trabalho, mas não há evidência de que o auditor Silvio Baroni revisou o TAP com os critérios estruturais do processo GQA. A marcação "✅" sem observações específicas pode indicar verificação superficial.
**Evidência:** GQA-AASP01-001 §3: > "Termo de Abertura | TAP-AASP01-001 | ✅"
**Referência normativa:** GQA RAP 2 — verificação deve ser baseada em critérios definidos, não apenas em presença do documento.
**Ação corretiva:** Observação para a próxima auditoria GQA: documentar os critérios verificados para cada produto de trabalho, não apenas o status binário.
