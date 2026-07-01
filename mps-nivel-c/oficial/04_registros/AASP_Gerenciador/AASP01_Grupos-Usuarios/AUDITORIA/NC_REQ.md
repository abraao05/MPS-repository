# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Documento de Requisitos
**Código:** REQ-AASP01-001
**Versão auditada:** 1.3
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 2 | 1 | 1 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **3** | **1** | **1** |

**Veredicto:** NÃO-CONFORME

---

## OBSERVAÇÕES POSITIVAS

O REQ-AASP01-001 é bem estruturado, com glossário, requisitos funcionais e não funcionais, regras de negócio e critérios de aceite. A separação entre requisitos entregues (Sprint 1) e planejados (Sprints 2 e 3) é clara e honesta. A rastreabilidade aos itens do backlog (AG-20 a AG-25) é completa para a Sprint 1.

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-REQ-01 — Critério de aceite RF-09 é vago: "Relatório consolidado de grupos disponível para consulta"
**Severidade:** 🟡 Moderada
**RAP impactado:** REQ RAP 2 — requisitos testáveis com critérios de aceite verificáveis
**Localização:** Seção 6 — Critérios de Aceite, RF-09
**Problema:** O critério de aceite do RF-09 ("Relatório consolidado de grupos disponível para consulta") não define o que o relatório deve conter, qual o formato da resposta, se há paginação, quais campos são obrigatórios, ou qual é o critério de "disponível". Para um requisito planejado para a Sprint 3 (próxima sprint), critérios de aceite vagos impedem a execução de testes adequados.
**Evidência:** > "RF-09 | *(Planejado — Sprint 3)* Relatório consolidado de grupos disponível para consulta"
**Referência normativa:** REQ RAP 2 — requisitos devem ser verificáveis; critérios de aceite devem ser específicos e mensuráveis.
**Ação corretiva:** Refinar o critério de aceite do RF-09 antes do início da Sprint 3: especificar o endpoint (ex.: `GET listargrupo` com parâmetros de agrupamento), os campos obrigatórios na resposta, se inclui exportação CSV (mencionada no TAP), e o critério de aprovação pelo QA.

---

### NC-REQ-02 — RF-07 e RF-08 marcados como "Planejado — Sprint 2" mas a Sprint 2 encerrou (30/06/2026)
**Severidade:** 🟡 Moderada
**RAP impactado:** REQ RAP 3 — rastreabilidade do estado atual dos requisitos
**Localização:** Seção 3 — Requisitos Funcionais, RF-07 e RF-08
**Problema:** Na data de auditoria (30/06/2026), a Sprint 2 encerrou em 20/06/2026. Os RF-07 e RF-08 permanecem marcados como "Planejado — Sprint 2" no documento v1.3 de 24/06/2026. Se foram implementados e aceitos, o status deve ser atualizado para "Entregue". Se não foram, é um desvio de escopo que deve ser registrado. O documento deixa o estado desses requisitos indefinido.
**Evidência:** > "RF-07 | *(Planejado — Sprint 2)* Registro automático de auditoria em tabela `AuditoriaGrupos`..."
**Referência normativa:** REQ RAP 3 — o estado de cada requisito deve ser rastreável e atualizado.
**Ação corretiva:** Atualizar RF-07 e RF-08 com o status pós-Sprint 2: "Entregue (aceite XX/06/2026)" ou "Postergado para Sprint 3 — registrar CR de prazo".

---

### NC-REQ-03 — Ausência de requisito de exportação CSV no REQ, apesar de estar no TAP
**Severidade:** 🟡 Moderada
**RAP impactado:** REQ RAP 1 — requisitos completos e consistentes com o TAP
**Localização:** Comparação TAP §2.1 item 6 vs REQ §3 RF-09
**Problema:** O TAP-AASP01-001 lista como entrega do escopo "Relatórios consolidados com exportação CSV". O REQ-AASP01-001 registra RF-09 como "Geração de relatório consolidado de grupos" sem mencionar a exportação CSV. Os cenários de teste CTQ-AASP01-001 planejam "REL-02 — Exportação do relatório em formato CSV" na Sprint 3. Há inconsistência entre o TAP e o REQ sobre se o CSV é um requisito formal ou apenas um cenário de teste adicional.
**Evidência:** TAP §2.1: > "6 | Relatórios consolidados com exportação CSV"; REQ RF-09: > "Geração de relatório consolidado de grupos" (sem CSV).
**Referência normativa:** REQ RAP 1 — todos os requisitos identificados nas partes interessadas devem ser capturados no documento de requisitos.
**Ação corretiva:** Adicionar RF-09b (ou incluir no RF-09): exportação do relatório em formato CSV, com critério de aceite correspondente. Ou registrar formalmente que o CSV foi excluído do escopo com justificativa.

---

### NC-REQ-04 — Aprovação do documento registrada em campo "Status: Aprovado" sem identificação do aprovador
**Severidade:** 🟢 Leve
**RAP impactado:** REQ RAP 1 — requisitos aprovados formalmente pelo cliente
**Localização:** Cabeçalho — campo Status
**Problema:** O campo "Status: Aprovado" não identifica quem aprovou, quando aprovou e por qual mecanismo. Para o REQ, o aprovador deve ser o PO (Marcos Turnes) pois os requisitos representam as necessidades do negócio do cliente.
**Evidência:** > "Status | Aprovado"
**Referência normativa:** REQ RAP 1 — requisitos aprovados pelo representante do cliente.
**Ação corretiva:** Adicionar campo "Aprovado por: Marcos Turnes (PO AASP) — data: XX/XX/2026" ou referenciar a ata de kickoff como evidência de aprovação dos requisitos iniciais.

---

### NC-REQ-05 — Documento bem estruturado com glossário útil
**Severidade:** 🔵 Obs
**RAP impactado:** —
**Localização:** Seção 2 — Glossário
**Problema:** —
**Evidência:** O glossário define claramente os termos "Grupo", "Membro", "Função", "Envelope", "Soft Delete", "auxo3" e "temis3" com precisão técnica adequada.
**Referência normativa:** —
**Ação corretiva:** Manter o padrão de glossário em todos os documentos técnicos futuros.
