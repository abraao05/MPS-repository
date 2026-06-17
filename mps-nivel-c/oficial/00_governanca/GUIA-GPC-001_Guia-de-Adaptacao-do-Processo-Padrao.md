# Guia de Adaptação do Processo-Padrão — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | GUIA-GPC-001 — Guia de Adaptação do Processo-Padrão (Tailoring) |
| **Versão** | 2.1 |
| **Data** | 10/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Responsável** | Silvio Baroni |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |
| **Documento de referência** | PRO-GPC-001 — Processo-Padrão Organizacional |

---

## 1. Propósito

Este guia define como a Timeware adapta o Processo-Padrão Organizacional (PRO-GPC-001) ao contexto de cada projeto e, quando aplicável, como os próprios processos organizacionais são calibrados. A adaptação assegura que o processo seja aplicado de forma proporcional ao porte, ao tipo e à criticidade de cada iniciativa, sem comprometer os controles essenciais de qualidade nem a rastreabilidade exigida pelo modelo de referência.

O guia cobre dois planos de adaptação:

- **Adaptação de projeto:** o Gerente de Projeto decide, no início da iniciativa, quais atividades e produtos de trabalho serão realizados em profundidade plena, simplificados ou dispensados — dentro das diretrizes aqui estabelecidas.
- **Adaptação organizacional:** o COO decide, com base em avaliação periódica ou necessidade específica, quando um processo organizacional pode ser aplicado em configuração reduzida para um contexto ou período determinado.

## 2. Princípio da adaptação (regra de ouro)

Adaptar o processo significa ajustar **como** e **com que profundidade** cada atividade é realizada — nunca eliminar arbitrariamente um ponto de controle obrigatório.

- **É permitido:** ajustar a profundidade e a formalidade dos produtos de trabalho; combinar papéis; encurtar ou simplificar atividades; dispensar atividades que genuinamente não se aplicam ao projeto.
- **Não é permitido:** suprimir um ponto de controle obrigatório (abertura, requisitos, design, verificação, homologação, encerramento) sob a justificativa de que o projeto é pequeno ou urgente.

Uma atividade só pode ser dispensada quando **não se aplica de fato** ao projeto — por exemplo, design de interface em um projeto sem front-end —, não por conveniência de prazo. Toda dispensa é registrada com justificativa explícita.

## 3. Pontos de controle obrigatórios (não adaptáveis)

Independentemente do nível de adaptação, todo projeto sob medida mantém:

1. Abertura formal do projeto (Termo de Abertura).
2. Requisitos identificados, especificados e validados com o cliente.
3. Design técnico (arquitetura) avaliado antes da construção.
4. Definição de Pronto aplicada a cada entrega (critérios de aceite, code review, verificação, homologação).
5. Aprovação do cliente antes da promoção para produção.
6. Encerramento formal (Termo de Aceite e registro de lições aprendidas).

Estes controles variam em profundidade, mas existem em todos os projetos.

## 4. Eixos de adaptação de projeto

A adaptação de cada projeto considera os eixos a seguir.

### 4.1. Tipo de produto

| Situação | Adaptação |
|---|---|
| Projeto **com interface de usuário** | Inclui design de UX/UI (wireframe → validação → design contínuo antecipado). |
| Projeto **sem front-end** (API, serviço, backend) | Dispensa o design de UX/UI. Mantém o design técnico (arquitetura, modelo de dados, contratos de integração). |
| Projeto de **integração** entre sistemas existentes | Ênfase no design de interfaces e contratos. UX/UI normalmente não se aplica. |
| Projeto de **configuração de plataforma / infraestrutura** | Atividades de desenvolvimento substituídas por configuração; verificação por checklists técnicos em vez de testes de software. |
| Projeto de **migração / modernização** de legado | Inclui análise do sistema atual; o design foca em compatibilidade e estratégia de migração. |

### 4.2. Origem dos requisitos e do design

| Situação | Adaptação |
|---|---|
| Cliente **não traz** design pronto | A Timeware conduz a criação do design (wireframe, protótipo, validação). |
| Cliente **traz** design/UX pronto | Criação de UX/UI dispensada; o design é validado e implementado. |
| Cliente **traz requisitos já detalhados** (ex.: RFP fechado) | Discovery mais curto, focado em confirmar entendimento e rastreabilidade. |

### 4.3. Porte do projeto

| Situação | Adaptação |
|---|---|
| Projeto **pequeno / curto** (≤ 3 meses) | Documentação mais enxuta: requisitos podem ser registrados como histórias no Jira. Os pontos de controle obrigatórios (§3) são mantidos. |
| Projeto **médio** (3–12 meses) | Profundidade padrão conforme PRO-GPC-001. |
| Projeto **grande / longo / crítico** (> 12 meses ou alto risco) | Maior formalidade e rastreabilidade; mais rigor nos produtos de trabalho e nos registros. |

### 4.4. Equipe e papéis

| Situação | Adaptação |
|---|---|
| Equipe pequena | Papéis podem ser acumulados (ex.: Tech Lead acumula Arquiteto). A responsabilidade por cada papel permanece atribuída. |
| Equipe grande | Papéis tendem a ser exercidos por pessoas distintas; segregação de funções críticas. |

### 4.5. Criticidade e regulação

| Situação | Adaptação |
|---|---|
| Projeto com requisitos **regulatórios ou de alta criticidade** | Maior rigor nas atividades de verificação, validação e registro; controles reforçados conforme a exigência aplicável. |
| Projeto sem requisitos regulatórios | Verificação proporcional ao porte e complexidade. |

### 4.6. Cadência de entrega e ambientes

| Situação | Adaptação |
|---|---|
| **Cadência de entrega ao cliente** | A cadência é definida por projeto e acordada na Apresentação e Aprovação do Plano. A Timeware pode consolidar incrementos internamente em stage e entregar na cadência combinada. |
| **Ambiente de stage** | Recomendado, mas não obrigatório. Sua ausência aumenta o risco de instabilidade nas apresentações ao cliente, que passariam a ocorrer em homologação. |

## 5. Calibração do nível de adaptação

Para tornar a decisão de adaptação objetiva e rastreável, cada projeto é classificado em um dos três níveis abaixo, com base nos critérios de calibração.

### 5.1. Critérios de calibração

| Critério | Nível 1 — Essencial | Nível 2 — Padrão | Nível 3 — Aprofundado |
|---|---|---|---|
| **Duração** | ≤ 3 meses | 3 a 12 meses | > 12 meses |
| **Tamanho da equipe** | 1 a 2 pessoas | 3 a 5 pessoas | ≥ 6 pessoas |
| **Complexidade técnica** | Baixa (CRUD, integração simples, configuração de plataforma) | Média (múltiplos módulos, 2–3 integrações) | Alta (arquitetura distribuída, múltiplas integrações críticas, algoritmos complexos) |
| **Criticidade / SLA contratual** | Sem SLA formalizado | SLA informal ou baixo impacto financeiro | SLA contratual rígido ou alto impacto financeiro/operacional |
| **Regulação / compliance** | Sem requisito regulatório | Dados sensíveis / LGPD básico | Regulação setorial, auditoria externa ou requisito contratual de conformidade |

**Regra de classificação:** o projeto assume o nível mais alto atingido em **qualquer** critério. Exemplo: um projeto pequeno (Nível 1 por duração) com requisito regulatório forte é classificado como Nível 3.

### 5.2. O que cada nível define

| Aspecto | Nível 1 — Essencial | Nível 2 — Padrão | Nível 3 — Aprofundado |
|---|---|---|---|
| **Requisitos** | Histórias no Jira com critério de aceite | Documento de requisitos completo | Documento completo + rastreabilidade bidirecional explícita |
| **Design técnico** | ADR simplificado ou registro em PCP | PCP completo | PCP completo + diagramas formais de arquitetura e modelo de dados |
| **Verificação / Validação** | Checklist + smoke checks | Plano de VV + execução registrada | Plano de VV + automação de testes + métricas de cobertura |
| **Integração** | Validação informal de contratos | Plano de integração + registro | Plano de integração + testes de contrato + ambiente dedicado |
| **Gestão de Projetos** | Kanban / backlog no Jira | PLA completo + RAC periódico | PLA completo + RAC periódico + gestão formal de riscos |
| **GQA** | 1 auditoria de encerramento | 1 auditoria intermediária + encerramento | Auditorias por sprint/fase + encerramento |
| **Lições aprendidas** | Registro simplificado no TAE | Documento LI estruturado | Documento LI + análise de causa-raiz + OMs formais |

## 6. Guia de adaptação por processo

Esta seção detalha, para cada processo de projeto, quais atividades e produtos de trabalho são obrigatórios, adaptáveis ou dispensáveis — e os critérios que autorizam cada decisão.

**Legenda:**
- **Obrigatório:** deve ser realizado em todo projeto, independentemente do nível de adaptação.
- **Adaptável:** a profundidade ou a forma de execução pode ser reduzida; a atividade não é eliminada.
- **Dispensável com justificativa:** pode ser suprimido quando o critério de dispensa se aplica; a decisão é registrada.

---

### 6.1. Engenharia de Requisitos (REQ)

| Atividade / Produto de trabalho | Status | Condição de adaptação / dispensa | Resultado MPS |
|---|---|---|---|
| Identificação e especificação de requisitos funcionais | Obrigatório | — | REQ 1, REQ 2 |
| Critérios de aceite por requisito | Obrigatório | — | REQ 2, REQ 5 |
| Validação dos requisitos com o cliente | Obrigatório | — | REQ 5 |
| Rastreabilidade requisito → entrega | Obrigatório | — | REQ 4 |
| Documento de Requisitos formal (REQ-*) | Adaptável | Nível 1: histórias detalhadas no Jira com critério de aceite são aceitas como substituto | REQ 1 |
| Workshop / sessões de elicitação formal | Adaptável | Dispensado quando cliente já entrega RFP ou backlog detalhado; substituído por sessão de confirmação | REQ 1 |
| Protótipo de UX / wireframe | Dispensável com justificativa | Dispensado em projetos sem interface de usuário | REQ 3 |
| Modelagem de domínio (diagrama de entidades de negócio) | Dispensável com justificativa | Dispensado em projetos de porte Nível 1 ou sem modelo de dados complexo | REQ 2 |
| Rastreabilidade bidirecional explícita (requisito ↔ caso de teste) | Adaptável | Nível 1–2: rastreabilidade via tags no Jira; Nível 3: matriz de rastreabilidade formal | REQ 4 |

---

### 6.2. Projeto e Construção do Produto (PCP)

| Atividade / Produto de trabalho | Status | Condição de adaptação / dispensa | Resultado MPS |
|---|---|---|---|
| Design técnico avaliado antes da construção | Obrigatório | — | PCP 1 |
| Definição de contratos de interface / API | Obrigatório | — | PCP 2 |
| Code review antes de merge para develop | Obrigatório | — | PCP 4 |
| Definição de Pronto aplicada a cada entrega | Obrigatório | — | PCP 5 |
| Documento de Design (PCP-*) | Adaptável | Nível 1: registro técnico simplificado no Jira ou ADR aceito como substituto | PCP 1 |
| Diagrama de componentes / arquitetura formal | Adaptável | Nível 1–2: diagrama informal suficiente; Nível 3: diagramas C4 ou equivalente | PCP 1 |
| Modelo de dados formal (diagrama ER) | Adaptável | Dispensado em projetos sem modelo relacional próprio (ex.: configuração de plataforma) | PCP 2 |
| Design de UX/UI (wireframe, protótipo) | Dispensável com justificativa | Dispensado em projetos sem interface de usuário | PCP 3 |
| ADR (Architecture Decision Records) | Adaptável | Nível 1: decisões registradas no documento de design; Nível 3: ADRs individuais por decisão relevante | PCP 1 |
| Análise de impacto formal para mudanças de design | Adaptável | Nível 1–2: registro no Jira suficiente; Nível 3: documento de impacto formal | PCP 6 |

---

### 6.3. Integração do Produto (ITP)

| Atividade / Produto de trabalho | Status | Condição de adaptação / dispensa | Resultado MPS |
|---|---|---|---|
| Estratégia de integração definida antes da execução | Obrigatório | — | ITP 1 |
| Validação de contratos de interface entre componentes | Obrigatório | — | ITP 2 |
| Critérios de aceite de integração definidos | Obrigatório | — | ITP 3 |
| Registro dos resultados de integração | Obrigatório | — | ITP 4 |
| Plano de Integração formal (ITP-*) | Adaptável | Nível 1–2: estratégia de integração registrada no PCP ou no PLA; Nível 3: documento ITP independente | ITP 1 |
| Ambiente de integração dedicado | Adaptável | Nível 1–2: ambiente de homologação usado para integração; Nível 3: ambiente de integração separado | ITP 2 |
| Testes de contrato automatizados | Adaptável | Nível 1: validação manual de contrato aceita; Nível 3: testes de contrato automatizados recomendados | ITP 2 |
| Plano de integração formal | Dispensável com justificativa | Dispensado em projetos sem integrações externas ou com integração de interface única e baixo risco | ITP 1 |

---

### 6.4. Verificação e Validação (VV)

| Atividade / Produto de trabalho | Status | Condição de adaptação / dispensa | Resultado MPS |
|---|---|---|---|
| Verificação técnica dos entregáveis antes da entrega | Obrigatório | — | VV 1, VV 2 |
| Validação com o cliente antes da aceitação | Obrigatório | — | VV 4 |
| Registro dos resultados de verificação e validação | Obrigatório | — | VV 5 |
| Plano de Verificação e Validação (VV-*) | Obrigatório | A forma varia: checklist de configuração é aceito para projetos de infraestrutura/plataforma; plano com casos de teste para projetos de software | VV 1 |
| Testes automatizados (unitários, integração) | Adaptável | Obrigatório em Nível 3; recomendado em Nível 2; dispensável em Nível 1 ou em projetos de configuração de plataforma (sem código desenvolvido) | VV 2 |
| Testes de performance / carga | Dispensável com justificativa | Dispensado quando não há SLA de performance contratual definido | VV 2 |
| Smoke checks como método de verificação | Adaptável | Aceito como método principal em projetos de Nível 1 ou projetos de configuração de infraestrutura; complementar em Nível 2–3 | VV 2 |
| Revisão por pares formal (peer review registrado) | Adaptável | Nível 1: code review no PR aceito como evidência; Nível 3: revisão por pares formal com registro separado | VV 3 |
| Métricas de cobertura de testes | Adaptável | Nível 1–2: não obrigatório; Nível 3: cobertura mínima definida e monitorada | VV 2 |

---

### 6.5. Gerência de Projetos (GPR)

| Atividade / Produto de trabalho | Status | Condição de adaptação / dispensa | Resultado MPS |
|---|---|---|---|
| Termo de Abertura de Projeto | Obrigatório | — | GPR 1 |
| Plano de Projeto (PLA-*) | Obrigatório | — | GPR 2, GPR 3, GPR 4 |
| Cronograma de marcos e entregas | Obrigatório | — | GPR 6 |
| Controle de mudanças de escopo | Obrigatório | — | GPR 9 |
| Encerramento formal (Termo de Encerramento) | Obrigatório | — | GPR 10 |
| Relatório de Acompanhamento (RAC-*) | Adaptável | Nível 1: resumo no Jira aceito como acompanhamento; Nível 2–3: documento RAC formal periódico | GPR 7 |
| Registro de Adaptação do Processo | Adaptável | Pode estar embutido no PLA em projetos de Nível 1; documento separado em Nível 2–3 | GPR 2 |
| Gestão de riscos com registro formal | Adaptável | Nível 1: riscos registrados no PLA; Nível 2–3: registro e monitoramento de riscos ao longo do projeto | GPR 5 |
| Estratégia de transição para produção | Obrigatório | A profundidade varia: Nível 1 pode registrar no PLA; Nível 3 requer plano de deploy com rollback e comunicação ao cliente | GPR 8 |
| Reuniões de status formais com o cliente | Adaptável | Dispensado quando há comunicação contínua e o cliente acompanha o Jira; substituído por update assíncrono acordado | GPR 7 |

## 7. Adaptação de processos organizacionais

Esta seção define quando e como os próprios processos organizacionais da Timeware podem ser aplicados em configuração reduzida. A adaptação organizacional é mais restrita do que a adaptação de projeto: requer decisão do COO e registro explícito.

### 7.1. Princípio

Os processos organizacionais (GCO, MED, CAP, AQU, GDE e GPC) são o "nível estável" da operação e, por isso, são adaptados com critério mais conservador do que os processos de projeto. A redução de escopo de um processo organizacional é sempre temporária ou contextual — não representa abandono do processo.

### 7.2. Processos organizacionais e suas possibilidades de adaptação

| Processo | Sempre obrigatório | Adaptável / contextual | Dispensável com justificativa |
|---|---|---|---|
| **GPC** (Gerência de Processos) | Manter e disseminar o processo-padrão; conduzir melhorias identificadas | Frequência de revisão do processo-padrão (mínimo: anual) | — |
| **GCO** (Gerência de Configuração) | Controle de versão de código (Git); baseline de entregáveis; auditoria de configuração | Nível de detalhe dos ICs para projetos muito pequenos (registros simplificados aceitos) | — |
| **MED** (Medição) | Coleta das medidas obrigatórias (M1–M7 do PLA-MED-001); consolidação no repositório organizacional | Frequência de coleta (mensal em projetos curtos aceita em vez de por sprint) | Medidas específicas não aplicáveis ao tipo de projeto (ex.: cobertura de testes em projetos de configuração) |
| **CAP** (Capacitação) | Identificação de necessidades de competências; registro de treinamentos concluídos | Formato do plano (simplificado para contratados de curto prazo) | Avaliação de eficácia formal (dispensável para treinamentos de curta duração e baixo impacto) |
| **AQU** (Aquisição) | Critérios mínimos de qualificação de fornecedores; avaliação técnica antes de contratar | — | Todo o processo AQU é dispensável em projetos sem aquisição de terceiros |
| **GDE** (Gerência de Decisões) | Registro de decisões de alto impacto técnico ou de negócio | Profundidade da análise (tabela simplificada aceita para decisões de menor impacto) | Análise formal de alternativas (dispensável para decisões com única alternativa viável) |

### 7.3. Critérios e autoridade de aprovação

| Tipo de adaptação | Autoridade de aprovação | Como registrar |
|---|---|---|
| Adaptação de projeto (processos GPR, REQ, PCP, ITP, VV) | Gerente de Projeto, registrado no Registro de Adaptação do Projeto | ADAP-* do projeto, referenciado no PLA |
| Adaptação de processo organizacional (GCO, MED, CAP, AQU, GDE, GPC) | COO | Atualização do documento de processo (PRO-*/PLA-*) ou registro em ata de análise crítica (PRO-OSW-001) |
| Suspensão temporária de processo organizacional | COO com ciência do CEO | Registro em ata de análise crítica com prazo de retomada definido |

### 7.4. Ciclo de revisão das adaptações organizacionais

As adaptações de processos organizacionais são revisadas:
- **Anualmente**, na análise crítica conduzida pelo COO (conforme PRO-OSW-001).
- **A qualquer momento**, quando uma mudança no contexto da organização (porte, portfólio, regulação) tornar a adaptação obsoleta ou insuficiente.

## 8. Como registrar e revisar a adaptação de projeto

### 8.1. Momento de decisão

A adaptação é decidida entre o kickoff gerencial e o fechamento do Plano de Projeto, antes do início das atividades técnicas. O Gerente de Projeto preenche o Registro de Adaptação do Processo (TPL-GPR-003) indicando, para cada eixo aplicável: a decisão, a justificativa e o nível de adaptação resultante (§5).

### 8.2. Conteúdo mínimo do registro

- Nível de adaptação definido (1, 2 ou 3) e os critérios que o determinaram.
- Lista de atividades/produtos dispensados, com justificativa para cada dispensa.
- Lista de atividades/produtos simplificados, com descrição da simplificação.
- Responsável pela aprovação e data.

### 8.3. Revisão durante a execução

A adaptação pode ser revisada se o contexto do projeto mudar significativamente. Gatilhos típicos de revisão:

- Mudança de escopo que eleve a complexidade técnica ou o risco.
- Alteração de requisitos regulatórios após o início do projeto.
- Mudança de equipe que elimine um papel originalmente acumulado.

A revisão é registrada no mesmo documento de adaptação, com nova versão e justificativa da mudança.

## 9. Exemplos de aplicação

### 9.1. Projeto de desenvolvimento de API (sem front-end) — Nível 2

**Contexto:** Desenvolvimento de API REST de integração entre dois sistemas, duração 4 meses, equipe de 3 pessoas, sem SLA regulatório.

**Calibração:** Duração → Nível 2; Complexidade → Nível 2; Regulação → Nível 1. Resultado: **Nível 2 — Padrão**.

| Decisão de adaptação | Justificativa |
|---|---|
| Design de UX/UI dispensado | Projeto sem interface de usuário |
| Plano de integração registrado no PCP (não documento separado) | Nível 2; integração entre 2 sistemas bem definidos |
| Testes automatizados de unidade e integração realizados | Nível 2; código desenvolvido |
| Documento de Requisitos completo (não só histórias no Jira) | Duração e complexidade Nível 2 |
| RAC emitido mensalmente | Cadência adequada para 4 meses |

### 9.2. Projeto de configuração de plataforma Azure API Management — Nível 1

**Contexto:** Configuração de gateway de APIs em plataforma cloud existente, duração 6 semanas, equipe de 2 pessoas, sem desenvolvimento de software.

**Calibração:** Duração → Nível 1; Complexidade → Nível 1 (configuração, não desenvolvimento); Regulação → Nível 1. Resultado: **Nível 1 — Essencial**.

| Decisão de adaptação | Justificativa |
|---|---|
| Testes automatizados dispensados | Sem código desenvolvido; verificação por checklists de configuração e smoke checks HTTP |
| Plano de VV como checklist de configuração | Tipo de projeto — configuração de plataforma, não software |
| Plano de integração dispensado como documento separado | Integrações são configurações de roteamento na plataforma; documentadas no design técnico |
| Requisitos registrados no documento REQ | Projeto com cliente externo; rastreabilidade necessária independente do porte |
| Lições aprendidas registradas em documento LI | Boa prática mantida mesmo em Nível 1 |

## 10. Documentos relacionados

- PRO-GPC-001 — Processo-Padrão Organizacional
- POL-ORG-001 — Política Organizacional de Processos
- PRO-OSW-001 — Governança Organizacional de Processos
- TPL-GPR-003 — Template do Registro de Adaptação do Processo
- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento
- EST-GPC-001 — Estratégia de Garantia da Qualidade

## 11. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW:2024. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

| Processo MPS | Resultado | Onde é atendido neste documento |
|---|---|---|
| GPC | GPC 2 — Diretrizes de adaptação do processo-padrão organizacional | Seções 2 (princípio), 3 (controles obrigatórios), 4 (eixos), 5 (calibração), 7 (adaptação organizacional), 8 (registro) |
| REQ | REQ 1–5 — Identificação, especificação, rastreabilidade, validação | Seção 6.1 — define quais resultados REQ são obrigatórios e quais são adaptáveis por nível |
| PCP | PCP 1–6 — Design, construção, code review, DoD | Seção 6.2 — define quais atividades PCP são obrigatórias e quais admitem simplificação |
| ITP | ITP 1–4 — Estratégia, contratos, critérios, registro de integração | Seção 6.3 — define quais produtos ITP são obrigatórios e quais dispensáveis |
| VV | VV 1–5 — Verificação, validação, métodos, registro de resultados | Seção 6.4 — define quais atividades VV são obrigatórias e quais são adaptáveis por tipo de projeto |
| GPR | GPR 1–10 — Planejamento, acompanhamento, controle | Seção 6.5 — define quais produtos GPR são obrigatórios e quais admitem simplificação por nível |
| GCO, MED, CAP, AQU, GDE | Adaptabilidade de processos organizacionais | Seção 7 — define quando processos organizacionais podem ser aplicados em configuração reduzida, com autoridade e registro |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 2.1 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Silvio Baroni |
| 1.0 | 08/08/2025 | Time de Melhoria Contínua | Definição inicial do guia de adaptação do processo-padrão |
| 1.1 | 16/12/2025 | Time de Melhoria Contínua | Ajuste de nomenclatura de fase conforme o novo fluxo |
| 1.2 | 19/01/2026 | Time de Melhoria Contínua | Inclusão do eixo de adaptação de cadência de entrega e ambiente de stage |
| 2.0 | 10/06/2026 | Time de Melhoria Contínua | Reestruturação completa: adição de matriz de calibração por nível (§5); guias de adaptação específicos por processo — REQ, PCP, ITP, VV, GPR (§6); capítulo de adaptação de processos organizacionais com autoridade e ciclo de revisão (§7); expansão do registro e revisão de adaptações (§8); exemplos ampliados (§9); rastreabilidade expandida para todos os processos MPS impactados (§11) |
