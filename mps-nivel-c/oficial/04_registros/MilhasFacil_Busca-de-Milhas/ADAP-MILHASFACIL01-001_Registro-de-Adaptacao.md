# Registro de Adaptação do Processo — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | ADAP-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.1 |
| **Data** | 15/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Tech Lead / Arquiteto / DevOps** | Cézar Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto — adaptação do processo padrão) |

---

## 1. Objetivo

Registrar as adaptações aplicadas ao processo-padrão de desenvolvimento Timeware para a execução do projeto MilhasFacil — Busca de Milhas, justificando cada decisão de tailoring e seus impactos no planejamento e na operação do ciclo de vida.

---

## 2. Nível de adaptação do projeto (calibração)

Conforme o Guia de Adaptação do Processo-Padrão (GUIA-GPC-001 §5), o projeto é classificado pela regra do **nível mais alto atingido em qualquer critério**.

| Critério (GUIA-GPC-001 §5.1) | Situação do MilhasFacil | Nível |
|---|---|---|
| Duração | 09/02/2026 a 26/07/2026 (~5,5 meses) | Nível 2 |
| Tamanho da equipe | 7 pessoas no projeto (GP; Tech Lead/Arquiteto/DevOps; QA; GQA; 3 desenvolvedores — DevOps = 5) | Nível 3 |
| Complexidade técnica | Três serviços (API Spring Boot, Web Angular, Crawler Python); múltiplas integrações externas (Smiles, Azul, Latam e Z-API/WhatsApp); busca paralela; autenticação JWT com refresh e blacklist | Nível 2–3 |
| Criticidade / SLA contratual | Sem SLA contratual rígido; impacto operacional moderado | Nível 2 |
| Regulação / compliance | Tratamento de dados pessoais de usuário (LGPD básico); sem regulação setorial | Nível 2 |

**Nível de adaptação resultante: Nível 3 — Aprofundado**, determinado pelo tamanho da equipe e pela complexidade técnica multi-serviço com múltiplas integrações.

Coerente com o Nível 3, o projeto mantém os produtos de trabalho mais formais previstos no GUIA-GPC-001 §5.2: documento de requisitos completo com **rastreabilidade bidirecional explícita** (RASTR §2 e §3), **automação de testes com métrica de cobertura** (JaCoCo; gate de 80% a partir da S4), **plano de integração independente** (ITP) e **GQA por ciclo/sprint** (auditorias GQA-A01/A02/A03). As adaptações registradas na seção seguinte ajustam a *profundidade e a forma* de execução, sem suprimir nenhum ponto de controle obrigatório (GUIA-GPC-001 §3).

---

## 3. Adaptações aplicadas

| # | Item do processo-padrão | Decisão de adaptação | Justificativa |
|---|---|---|---|
| A-01 | Pipeline de CI executado em agente Linux padrão | Pipelines executadas em agente Windows (Default) com tasks **PowerShell@2** nas três pipelines ("MilhasFacil API/Web/Crawler - Pipeline") | Agente Windows é o recurso disponível na organização; padronização das tasks em PowerShell@2 reduz divergência entre as três pipelines. Mitiga o risco R-05 (pipeline de CI em agente Windows) |
| A-02 | Histórico de repositório construído incrementalmente desde a primeira sprint | Histórico dos repositórios (MilhasFacil_api, MilhasFacil_web, MilhasFacil_crawler) **inicializado de forma consolidada** (retroativa); saneamento prospectivo a partir da S9 | A integração ao Azure DevOps ocorreu de forma retroativa; datas reais de PR e build concentram-se em 13–15/06/2026. Os **22 PRs históricos (S1–S8)** permanecem **sem revisor registrado** por serem fruto da consolidação histórica (PR concluído é imutável). A partir da S9 a revisão de PR está **evidenciada**: os **6 PRs da S9** (API #11/#12/#28, Web #21/#22, Crawler #27) foram **concluídos em 15/06 com revisor Cézar Velazquez (TL) — Approved (vote 10)**, registrado no Azure DevOps sob a conta legada `Mateus Veloso`, e mergeados em develop; foi ativada a **branch policy** de revisor (≥1 revisor) em develop nos três repositórios, impedindo recorrência |
| A-03 | Gate de cobertura de testes ativo desde o Sprint 1 | Gate de cobertura (JaCoCo 80% na API) **ativado a partir da Sprint 4** | A NC-001 (cobertura <80%, JaCoCo 74% na S2) motivou a priorização de testes unitários e a introdução do gate de CI a partir da S4; a NC foi encerrada na S5 (JaCoCo 82%) |
| A-04 | Revisão de PR com dois revisores independentes | Revisão com **um revisor** — o Tech Lead/Arquiteto **Cézar Velazquez** aprova os PRs (Approved, vote 10); no Azure DevOps a aprovação aparece sob a conta legada `Mateus Veloso` (= Cézar) | Equipe enxuta com três desenvolvedores efetivos; o Tech Lead concentra a aprovação técnica dos PRs, mantendo o gate de aprovação sem ampliar o lead time. A branch policy de revisor em develop (S9) torna o revisor obrigatório nos três repositórios. A aprovação de escopo/CR é responsabilidade do GP (Abraão) |
| A-05 | Cadastro de dados de referência em banco de dados | Lista de aeroportos (IATA) mantida **fixa em código** (`SearchService`) na linha principal até a release v0.9.0; a partir de v0.9.0, busca de aeroportos atendida por **AirportController/AirportRepository** com índice `V9__airport_search_index.sql` (MF-64) | Volume estável e pequeno de aeroportos; a lista em código simplificou o deploy nas primeiras sprints. Na S9 a busca passou a ser servida por consulta paginada case-insensitive (ILIKE + extensão `unaccent`), released em main na v0.9.0 |
| A-06 | Combinação de papéis | O **GP (Abraão)** faz gestão e **não codifica** (fora do DevOps); o **Tech Lead Cézar Velazquez** acumula os papéis de **Arquiteto e DevOps** e é o revisor de PR; a **GQA (Carol/Caroline)** é **independente** (auditoria de processo), não codifica e fica fora do DevOps; o QA de teste manual é Jonathan Alves | Equipe contratada enxuta; concentração dos papéis técnicos (TL/Arquiteto/DevOps) em Cézar para viabilidade operacional, preservando a **independência da GQA (Carol)** em relação ao desenvolvimento e a separação do GP (gestão) da execução técnica |
| A-07 | Notificação síncrona obrigatória ao usuário | Envio de WhatsApp via Z-API (`WhatsAppClient`) tratado como **best-effort**: falha no envio não interrompe o fluxo de alerta | Disponibilidade da Z-API é externa (risco R-03); o serviço de alerta (`ScheduledAlertService`) prossegue mesmo em caso de falha de notificação, com dedupe por origem-destino-milhas |
| A-08 | Prefixo de branch de funcionalidade `feature/...` (PLA-GCO-001 §4.1) | Adotados os prefixos **`feat/`** e **`fix/`** seguidos da chave Jira (`feat/MF-XX-...`, `fix/MF-XX-...`), no padrão Conventional Branches/Commits | Alinhamento com os tipos de Conventional Commits usados no projeto (feat/fix/test/chore/ci) e com a chave de rastreabilidade MF-XX (RNF04); estratégia main/develop/feature do PLA-GCO-001 mantida na essência. O saneamento da política de branch foi concluído na S9 com a ativação da branch policy de revisor em develop nos três repositórios |
| A-09 | Nomenclatura de scripts SQL `0001-create-…-table.sql` (GUIA-GCO-001 §4) | Migrations versionadas pela convenção do **Flyway** (`V1__create_users.sql` … `V5__…`; `V9__airport_search_index.sql`); padronização de nomenclatura de BD em curso via **PR #29 (MF-73)** com `V10__fix_naming_conventions.sql` | A ferramenta Flyway exige o prefixo `V<n>__`; a numeração sequencial e o controle de versão do schema (objetivo do guia) são plenamente atendidos pela convenção nativa. O PR #29 (MF-73, chore — padronização de nomenclatura de BD conforme GUIA-GCO-001) introduz a migration V10 (padronização de índices + coluna `is_active`) e foi **aprovado pelo Tech Lead Cézar Velazquez na conta própria dele no Azure DevOps (vote 10)**, aguardando merge |
| A-10 | Histórico de fluxo dos cards no Jira transitando pelas colunas em tempo real desde a S1 | Status dos cards das sprints **S1–S8 registrado de forma consolidada** (transições em 13–15/06); a **Sprint 9 transita pelas colunas em tempo real** (To Do → Doing → Code Review → To Test → Done) | Mesma causa-raiz de A-02 (tooling Azure/Jira montado retroativamente). O **desenvolvimento em si — os commits — seguiu a linha do tempo real das sprints** (fev–jun), assim como as **tags v0.1.0–v0.9.0** (criadas no fim de cada sprint). A evidência de teste e aprovação **por card** é registrada no **CTQ-MILHASFACIL01-001** (cenário Gherkin + critério + resultado + aprovador), independentemente do carimbo das transições |

---

## 4. Itens sem adaptação (processo-padrão mantido)

- Controle de versão de código no Azure DevOps (Git), com branch padrão main nos três repositórios.
- PR obrigatório para develop antes do merge, com aprovação do Tech Lead (Cézar Velazquez).
- Execução de testes (JUnit5+Mockito+AssertJ, SpringBootTest+Testcontainers, Karma, pytest) como gate no pipeline de CI.
- Registro de riscos com probabilidade, impacto, exposição e plano de resposta.
- Rastreabilidade de requisitos (RF → Jira → branch → PR → build).
- Nomenclatura de branches `feat/`|`fix/` + `MF-XX` (política de branch — RNF04).
- Formalização de mudanças de escopo via change request antes da implementação (CR-MF-001).

---

## 5. Impacto das adaptações no projeto

| Adaptação | Impacto observado |
|---|---|
| A-01 (CI Windows / PowerShell@2) | Padronização das três pipelines; builds reais #41–#60 quase todos `succeeded` (apenas #42 `canceled`). Risco R-05 mantido sob controle |
| A-02 (histórico consolidado) | 22 PRs históricos (S1–S8) sem revisor registrado, representados fielmente como integração retroativa (ressalva com causa-raiz), sem afirmar revisor onde não há; a partir da S9, 6 PRs com revisor Cézar Velazquez (TL; conta legada `Mateus Veloso`, Approved) e branch policy de revisor ativa em develop (saneamento prospectivo). Meta "PRs sem revisor = 0" cumprida pelos 6 PRs da S9 |
| A-03 (gate de cobertura na S4) | Cobertura JaCoCo elevada de 74% (S2) para 82% (S5); NC-001 encerrada; meta de ≥80% atendida a partir da S4 |
| A-05 (aeroportos em código → ILIKE) | Deploy simplificado nas primeiras sprints; na S9, busca de aeroportos migrada para consulta paginada (ILIKE + `unaccent`) com índice V9, released em main na v0.9.0 |
| A-08 / A-09 (saneamento de BD e branch) | Branch policy de revisor ativada em develop (saneamento da política de branch); padronização de nomenclatura de BD em curso via PR #29 (MF-73), migration V10 aprovada pelo Tech Lead Cézar Velazquez (conta própria, vote 10), aguardando merge |

---

## 6. Processos não aplicáveis ao projeto

| Processo | Aplicável? | Justificativa |
|---|---|---|
| Aquisição (AQU) | **Não aplicável** | Squad próprio Timeware; não há subcontratação de terceiro responsável por entrega. Os serviços externos (Z-API, portais das companhias raspados pelo crawler) são insumos/integrações, tratados em ITP e Riscos, fora do escopo de AQU. |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Inclusão da seção 2 (Nível de adaptação / calibração conforme GUIA-GPC-001 §5): projeto classificado como Nível 3 — Aprofundado; renumeração das seções seguintes. |
