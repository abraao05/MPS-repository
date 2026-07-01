# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Registro de Gerência de Configuração
**Código:** GCO-AASP01-001
**Versão auditada:** 1.2
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 1 | 2 | 1 | 0 |
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 1 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 1 | 0 | 0 | 0 |
| **TOTAL** | **2** | **5** | **1** | **0** |

**Veredicto:** NÃO-CONFORME CRÍTICO

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-GCO-01 — BL-03 prevista para 20/06/2026 não foi registrada (data atual 30/06/2026)
**Severidade:** 🔴 Grave
**RAP impactado:** GCO RAP 3 — baselines estabelecidas conforme planejado
**Localização:** Seção 4 — Baselines estabelecidas; seção 5 — Auditoria de configuração
**Problema:** O documento prevê "BL-03 — após aceite formal da Sprint 2 (previsto para 20/06/2026)". Na data de auditoria (30/06/2026), a Sprint 2 deveria ter encerrado há 10 dias. A BL-03 não está registrada na seção 4 — se o aceite da Sprint 2 ocorreu, a baseline não foi documentada. Se não ocorreu, isso indica desvio de prazo não registrado. Em ambos os casos, o GCO está desatualizado.
**Evidência:** > "Próxima baseline prevista: BL-03 — após aceite formal da Sprint 2 (previsto para 20/06/2026)..."
**Referência normativa:** GCO RAP 3 — baselines devem ser estabelecidas nos marcos planejados. GCO RAP 4 — registro de baselines deve ser mantido.
**Ação corretiva:** Atualizar o GCO com o resultado da Sprint 2: (a) se aceite ocorreu em 20/06/2026, registrar BL-03 com todos os ICs, aprovador e data; (b) se o aceite foi adiado, registrar o desvio e nova data prevista.

---

### NC-GCO-02 — Inventário de ICs tem contagem inconsistente com o índice (19 vs 21 artefatos)
**Severidade:** 🔴 Grave
**RAP impactado:** GCO RAP 1 — todos os ICs identificados
**Localização:** Seção 3, IC-05; comparado com 00_INDICE-AASP01
**Problema:** O IC-05 registra "19 artefatos (18 .docx + 1 .xlsx)" como itens de configuração no pacote MPS-SW. O índice lista 21 artefatos entregues (mais 2 previstos). Os dois documentos faltantes no IC-05 são provavelmente o GQA-AASP01-001 e o CAP-AASP01-001. Itens de configuração não inventariados estão fora do controle de configuração — qualquer alteração nesses documentos não será rastreada pela GCO.
**Evidência:** > "IC-05 | Documentação MPS-SW | [...] Total: 19 artefatos (18 .docx + 1 .xlsx)."
**Referência normativa:** GCO RAP 1 — todos os itens de configuração identificados e sob controle.
**Ação corretiva:** Atualizar IC-05 para 21 artefatos, listando nominalmente todos os documentos incluídos. Verificar se GQA e CAP estão na baseline BL-02.

---

### NC-GCO-03 — Auditoria de acompanhamento de 15/06 é o único registro de auditoria pós-baseline e não verifica conteúdo
**Severidade:** 🟡 Moderada
**RAP impactado:** GCO RAP 5 — auditorias de configuração realizadas
**Localização:** Seção 5 — Auditoria de configuração, linha 15/06/2026
**Problema:** A auditoria de acompanhamento de 15/06/2026 verifica apenas aspectos de processo (branches corretos, pipeline ativo, histórico limpo) sem verificar a consistência de conteúdo dos ICs — por exemplo, verificar que os documentos MPS-SW versionados estão consistentes entre si ou que os scripts SQL estão aplicados no ambiente de homologação. Uma auditoria de configuração completa deve incluir verificação de integridade dos conteúdos, não apenas da estrutura.
**Evidência:** > "15/06/2026 | Auditoria de acompanhamento [...] | Verificação de que feature branches estão derivados de develop pós-BL-02; nenhum commit direto em main ou develop; pipeline CI executando..."
**Referência normativa:** GCO RAP 5 — auditoria de configuração deve verificar integridade dos ICs, não apenas a estrutura de versionamento.
**Ação corretiva:** Expandir a auditoria de acompanhamento para incluir: (a) verificação de que todos os documentos da BL-02 estão consistentes entre si; (b) confirmação de que as 3 migrations SQL estão aplicadas no ambiente de homologação; (c) verificação do Swagger contra os requisitos.

---

### NC-GCO-04 — Cezar Hiraki é simultaneamente responsável pelo GCO e revisor principal dos MRs — conflito de interesse não mitigado
**Severidade:** 🟡 Moderada
**RAP impactado:** GCO RAP 5 — independência nas auditorias de configuração
**Localização:** Seção 2 — Estratégia; ADAP-AASP01-001 A-08
**Problema:** A adaptação A-08 permite que Cezar Hiraki acumule GCO, revisor de MRs e arquiteto. O GCO é responsável por auditar os próprios artefatos que Cezar Hiraki produziu ou aprovou. Embora o ADAP-AASP01-001 registre esta adaptação, a mitigação ("Renan Kiyoshi preparado para assumir GCO em caso de indisponibilidade") não resolve o conflito de interesse estrutural — o problema não é indisponibilidade, é independência.
**Evidência:** GCO-AASP01-001 §2: "Responsável de GCO (Cezar Hiraki)"; ADAP A-08: "Cezar Hiraki acumula os papeis de Arquiteto, Tech Lead, DevOps, Revisor e GCO"
**Referência normativa:** GCO RAP 5 — auditoria de configuração deve ter independência suficiente. MPS.BR Guia de Avaliação — acumulação de papéis conflitantes deve ser mitigada com procedimentos compensatórios.
**Ação corretiva:** Designar Silvio Baroni (SEPG) ou outro membro independente para realizar a auditoria formal de configuração nas baselines, mesmo que Cezar Hiraki mantenha as operações diárias do GCO.

---

### NC-GCO-05 — Auditoria da BL-01 realizada pelo próprio responsável de GCO (Cezar Hiraki)
**Severidade:** 🟡 Moderada
**RAP impactado:** GCO RAP 5 — independência
**Localização:** Seção 5 — Auditoria de configuração, linha 19/05/2026
**Problema:** A auditoria da baseline BL-01 foi realizada por "Cezar Hiraki" — o mesmo responsável pela criação do repositório e da estrutura auditada. Autoavaliação não constitui auditoria independente de configuração.
**Evidência:** > "19/05/2026 | Auditoria de baseline inicial (BL-01) | [...] | Aprovado | Cezar Hiraki"
**Referência normativa:** GCO RAP 5 — auditoria de configuração deve ser independente.
**Ação corretiva:** Registrar quem validou o trabalho de Cezar Hiraki na BL-01 (ex.: Abraão validou como GP, ou Silvio Baroni verificou no GQA). Ou definir que a auditoria de baseline é realizada pelo GQA (Silvio Baroni).

---

### NC-GCO-06 — Pipeline CI em containers não evidenciado — _DOSSIE confirma lacuna
**Severidade:** 🟢 Leve
**RAP impactado:** GCO RAP 2 — mecanismos de controle implementados
**Localização:** Seção 2 — Gate de merge (CI); IC-03
**Problema:** O documento descreve um "Pipeline GitLab CI obrigatório" com etapas de build, testes unitários e análise estática. O _DOSSIE-EVIDENCIAS_AASP01.md classifica esta evidência como "furo — criar .gitlab-ci.yml + testes (build real no GitLab) OU abrandar docs", indicando que o pipeline CI não tem evidência verificável externa ao sistema GitLab.
**Evidência:** _DOSSIE: > "4 | Pipeline CI/CD (build verde, 22 testes, cobertura) | GCO, MED, VV, REL-VV | furo | criar .gitlab-ci.yml+testes..."
**Referência normativa:** GCO RAP 2 — mecanismos de controle devem ser evidenciáveis.
**Ação corretiva:** Exportar e arquivar captura de tela do pipeline GitLab CI em execução (build verde, testes passando) como evidência no pacote documental, conforme identificado no dossiê de evidências.
