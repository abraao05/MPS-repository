# Análise de Adequação — Projeto FTGASMIG (Fundação Tecnológica de Governança de APIs)

| Campo | Valor |
|---|---|
| **Projeto** | Fundação Tecnológica GASMIG — Governança de APIs (cliente: GASMIG — Cia. de Gás de Minas Gerais) |
| **Pasta** | `mps-nivel-c/oficial/04_registros/FTGASMIG_Governanca-APIs` (branch `claude/gallant-hamilton-T0gPb`) |
| **Modelo** | MR-MPS-SW:2024 — Nível C |
| **Base** | Checklist de projetos (Bloco 2) + templates/políticas Timeware como referência de completude |
| **Natureza** | Projeto de **configuração de ferramenta** (Azure API Management), sem desenvolvimento de software — adaptações formalizadas em ADAP |
| **Estrutura** | Duas Ordens de Serviço: **OS-001 encerrada** (aceite 26/05/2026) e **OS-002 em andamento** (verificação/aceite previstos para 09–10/06/2026) |
| **Data** | 05/06/2026 |
| **Resultado** | **27 OK · 11 PARCIAL · 1 FALTA · 1 NA** (40 itens) |

> Avaliação conservadora: cada item foi confrontado com o conteúdo real dos 22 documentos das duas OS e com a seção exigida pelo template. Por ser projeto de **configuração** (não desenvolvimento), várias adaptações (V&V por checklist, revisão técnica no lugar de revisão de código, ITP de componentes não aplicável) são legítimas e estão formalizadas em `ADAP-GASMIG02-001/002` — foram consideradas como tal, sem penalizar.

---

## Visão geral

A OS-001 apresenta um ciclo completo e coerente: `TAP → REQ (com critérios de aceite, validação e confirmação) → PCP (design + decisões) → GDE → VV → REV (verificação executada) → ATA de aceite → TAE → GQA`. As adaptações ao tipo de projeto (configuração de APIM) são bem justificadas. Os pontos fortes incluem requisitos com critérios de aceite explícitos, decisão arquitetural rigorosa (GDE), verificação técnica registrada (REV) e GQA independente (COO) sem não conformidades.

As deficiências concentram-se em: (1) **Gerência de Configuração (GCO)** sem registro formal/auditoria; (2) ausência de **registro de medição (MED)** e de **relatório de acompanhamento (RAC)**; (3) **artefatos de planejamento não atualizados pós-execução** (inconsistência interna); e (4) a **OS-002 ainda aberta**.

---

## Deficiências em relação à metodologia

### 1. Gerência de Configuração (GCO) [R70/R71/R72/R74 PARCIAL, R73 FALTA]

Não há documento de GCO. O papel de GCO foi atribuído a Cézar Hiraki (TAP/PLA), e **os itens de configuração estão enumerados** — no `PCP §2.2` (named values, produtos, grupos, workspaces, policy fragments, com relações) e na coluna "Item de configuração" da `RASTR`. Isso é mais do que o projeto PROFARMA tinha, por isso **R70 é PARCIAL** (não FALTA). Mas falta:

- Um **registro formal de GCO** com situação e nível de controle por IC (R70).
- **Baseline/tags** formalizadas — o IaC (Bicep/ARM) está versionado no Azure DevOps GASMIG, mas sem *baseline register* (R71); histórico de modificações dos ICs só por referência a commits (R72); sem hash/checksum no pacote de entrega (R74).
- **Relatório de auditoria de configuração (R73 — REQUERIDO): inexistente.** A `GQA-001` audita aderência ao processo e completude de artefatos, **não** as baselines/integridade dos itens de configuração. É a única FALTA do projeto.

### 2. Medição (MED) e Acompanhamento (RAC) [R78 PARCIAL, R44 PARCIAL, R46 PARCIAL]

- **Sem registro de medição do projeto (R78):** o `VV §5` afirma que os indicadores "alimentam a medição conforme PLA-MED-001", mas **não existe um documento MED**. Há dados dispersos (prazo planejado×realizado no `TAE §3`; "nenhuma pendência" no REV), sem indicadores consolidados (lead time, defeitos, retrabalho, SLA).
- **Sem relatório de acompanhamento consolidado (R44):** existem `ATA-001` (kickoff) e `ATA-002` (aceite), e o `PLA §7` cita status semanal por e-mail/Teams, mas não há um RAC consolidando o acompanhamento.
- **Plan×real parcial (R46):** o `TAE §3` cobre prazo (15 dias planejados; entrega 18/05, 4 dias além, sem impacto) e escopo (100%), mas não o esforço realizado.

### 3. Inconsistência interna — artefatos de planejamento não atualizados pós-execução

Vários artefatos de **planejamento** permaneceram no estado pré-execução, enquanto os **resultados reais** foram consolidados em outros documentos (REV, ATA, TAE, GQA):

| Artefato | Estado encontrado | Onde está o resultado real |
|---|---|---|
| `VV-GASMIG02-001 §4` (checklist) | Todas as caixas `☐` vazias, evidência "—" | `REV-GASMIG02-001` — todos os itens ✅ com evidência |
| `RASTR-GASMIG02-001` (coluna Situação) | Todas as linhas "Pendente" | REV confirma todos verificados/aprovados |
| `ADAP-GASMIG02-001 §3` (pontos de controle) | Itens de V&V/encerramento `[ ]` desmarcados | TAE/REV/ATA confirmam concluídos |
| `PCP-GASMIG02-001 §5` (verificação) | "A verificar — 13/05/2026" | REV (18/05) confirma aprovado |

**Impacto:** um avaliador da ASR apontaria a **contradição** entre os documentos de planejamento ("pendente/vazio") e os de encerramento ("concluído/aprovado"). A evidência de execução existe (REV/ATA/TAE/GQA são robustos), mas os artefatos-fonte deveriam ter sido atualizados. **Recomendação:** atualizar VV §4, RASTR (Situação→Verificado), ADAP §3 e PCP §5 para refletir o resultado, ou referenciar explicitamente o REV como registro de execução.

### 4. OS-002 em andamento (evidência de encerramento pendente)

A `GQA-001 §2.2` indica que **REV-002, ATA-003 e TAE-002 estão pendentes** (previstos para 09–10/06/2026). O `VV-GASMIG02-002 §4` está com o checklist em branco (verificação 09/06 a realizar). Portanto, a segunda metade do projeto ainda **não tem evidência de verificação/aceite**. A avaliação acima apoia-se na **OS-001 (encerrada)**; quando a OS-002 fechar, os itens de V&V/aceite/GCO devem ser reconfirmados para ela.

### 5. Itens menores

- **Documentação de sustentação (R57):** o PCP é completo e o IaC é entregue, mas não há manual de sustentação separado (o ambiente passa ao TI da GASMIG).
- **E-mail de aceite (R76):** os e-mails de aceite/entrega estão **referenciados com data/hora** na `ATA-002`/`TAE` (Abraão→Sérgio 18/05 18:37; Sérgio 26/05 11:39), mas o artefato original (domínio externo) não está anexado.
- **Release notes / logs de CI (R63/R61):** material de evidência (PDF) e IaC foram entregues; faltam release notes formais e logs de build/CI (este último pouco aplicável a projeto de configuração).

---

## Sobre o item R51 (Change Requests) — NA, não FALTA

Marquei **NA (não se aplica)**, não FALTA: o `TAE §3` declara explicitamente **"nenhum change request durante a execução"** e o mecanismo de controle de mudanças **está definido** (PLA risco R-04 e `ADAP §2`: mudança de escopo segue `TPL-GPR-006`), apenas não foi acionado porque não houve mudança de escopo. Importante: a **OS-002 é uma parcela separada já prevista** (escopo listado como "não incluído" na OS-001), não uma mudança da OS-001. Como não houve mudança de requisitos a controlar, NA com justificativa é o correto.

---

## Pontos fortes (para não enviesar a leitura)

- **REQ completo:** critérios de aceite por requisito, seção de validação (§7) e de confirmação de entendimento (§8) — supera FTFRUKI e PROFARMA neste ponto.
- **Verificação executada e registrada (REV-001):** todos os itens verificados com evidência, demo ao vivo ao cliente, sem pendências.
- **Decisão arquitetural rigorosa (GDE-001 + PCP §2.4):** workspaces vs. produtos com matriz de critérios, riscos e premissas.
- **GQA independente (COO):** auditoria de aderência das duas OS, sem não conformidades; revisão de artefatos documentada.
- **Adaptações coerentes e formalizadas (ADAP):** V&V por checklist, revisão técnica no lugar de revisão de código e ITP de componentes NA — adequado ao projeto de configuração.

---

## Recomendações priorizadas

1. **Produzir o registro de GCO e a auditoria de configuração** (fecha a única FALTA, R73 REQUERIDO; e eleva R70/R71/R72/R74) — formalizar IC list (a partir do PCP §2.2/RASTR), baselines/tags do IaC e auditoria de baselines.
2. **Atualizar os artefatos de planejamento** (VV §4, RASTR Situação, ADAP §3, PCP §5) para refletir a execução — elimina a inconsistência planejamento×encerramento.
3. **Criar o registro de Medição (MED)** do projeto e um relatório de acompanhamento (RAC) consolidando o status semanal.
4. **Encerrar a OS-002** (REV-002, ATA-003, TAE-002) e reconfirmar os itens de V&V/aceite/GCO para ela.
5. **Anexar** o e-mail de aceite (R76) e um manual mínimo de sustentação (R57).
