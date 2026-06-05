# Análise de Adequação — Projeto PROFARMA (Cadastro de Clientes · Rede D1000)

| Campo | Valor |
|---|---|
| **Projeto** | Cadastro de Clientes — Rede D1000 (cliente: Profarma S.A. / Rede D1000) |
| **Pasta** | `mps-nivel-c/oficial/04_registros/PROFARMA_Cadastro-de-Clientes` (branch `claude/gallant-hamilton-T0gPb`) |
| **Modelo** | MR-MPS-SW:2024 — Nível C |
| **Base** | Checklist de projetos (Bloco 2) + templates/políticas Timeware como referência de completude |
| **Data** | 05/06/2026 |
| **Resultado** | **28 OK · 10 PARCIAL · 2 FALTA** (40 itens) |

> Avaliação conservadora: cada item foi confrontado com o conteúdo real dos 18 documentos e com a seção exigida pelo template correspondente. Evidência que vive em ferramenta (Azure DevOps, Jira, Datadog) e não está nos `.md` foi avaliada pelo que o documento efetivamente contém — não como OK por presunção.

---

## Visão geral

Tecnicamente é o projeto **mais maduro** dos avaliados: GQA com não conformidades formais e ações corretivas, GDE com cinco decisões arquiteturais rigorosas (matriz de critérios + aprovador), MED com SPI (0,91) e análise de causa-raiz, REL-VV consolidando 7 níveis de teste, REV com três revisões por pares formais, e RAC consolidando seis fases com planejado×realizado. A camada de **gerência (GPR), requisitos (REQ), design (PCP), V&V e qualidade (GQA/MED/GDE)** está sólida.

As deficiências concentram-se em **três frentes**: (1) ausência total da **Gerência de Configuração de projeto (GCO)**; (2) ausência do artefato de **Integração do Produto (ITP)**; (3) lacunas pontuais de formalização em REQ e nas evidências "vivas". Há também **uma inconsistência interna nos registros de defeito** que um avaliador apontaria.

---

## Deficiências em relação à metodologia

### 1. Gerência de Configuração (GCO) — a lacuna mais grave [R70 FALTA, R73 FALTA, R71/R72/R74 PARCIAL]

Não existe documento de GCO no dossiê. O `ADAP-PROFARMA01-001` (A-08) declara que o Gerente de Projeto "acumulou o papel de GCO", mas **nenhum registro de configuração foi produzido**. Em concreto, falta:

- **Lista de itens de configuração (R70 — REQUERIDO):** não há inventário de ICs com ID, tipo, situação e relações. Existem menções a repositórios (`loja-backend`, `loja-balcao-frontend`) e versões, mas não um registro de ICs.
- **Relatório de auditoria de configuração (R73 — REQUERIDO):** inexistente. A `GQA-P03` audita a *completude de artefatos e a aderência ao processo*, não as *baselines/integridade de ICs* — não substitui a auditoria de configuração.
- **Baselines/tags (R71):** versões e GMUD aparecem dispersas (`25.12.1.1`, `26.1.1.1`, GMUD 2624117, PR 10684), sem um *baseline register* formal.
- **Histórico de modificações dos ICs (R72):** coberto parcialmente pelo log de CRs (RASTR §5) e pela numeração de versões; sem changelog/git log consolidado.
- **Pacote de entrega / checksum (R74):** o pacote de encerramento foi entregue (TAE §8, ATA-002 D-04), mas sem hash/checksum de integridade.

**Impacto MPS:** o processo GCO (resultados GCO 1–5) e o atributo de capacidade CP "produtos sob controle" ficam sem evidência de projeto. **Observação relevante:** os outros projetos da amostra (FTGASMIG, FTFRUKI) possuem um registro de GCO — o PROFARMA é o único sem. É a prioridade de correção.

### 2. Integração do Produto (ITP) — artefato ausente [R58/R60/R61/R63 PARCIAL, R59/R62 OK]

Não há documento de Estratégia de Integração (equivalente ao `TPL-ITP-001`). As **interfaces internas/externas estão muito bem descritas** — `REQ §5` (ITEC, VTEX, Propz, PBM, BlueSoft, CloseUp com padrão/direção/schema) e `PCP §5` (fluxos) — e os **testes de integração existem** (`REL-VV` Nível 2, 11 cenários). Por isso não é FALTA. O que falta é o artefato consolidado:

- Estratégia/ordem de integração e ambiente de integração formalizados (R58/R59 cobertos só parcialmente fora de um doc ITP).
- **Avaliação de prontidão de componentes (R60):** há critérios de entrada/saída por nível de teste (VV §3.1) e de piloto (VV §7.2), mas não uma avaliação de prontidão por componente.
- **Logs de build/CI (R61):** o pipeline está descrito (RNF-12), mas nenhum log/registro de execução de CI está anexado.
- **Release notes (R63):** versões e material de apoio (doc Propz) existem; falta um documento de release notes.

### 3. Requisitos — formalização incompleta [R50 PARCIAL; R49 OK com ressalva]

- **Confirmação de entendimento dos requisitos (R50):** o `REQ` não tem a seção de confirmação/compromisso (prevista no `TPL-REQ-001 §8`). A aprovação existe de forma indireta (aprovação do plano em PLA §11, sprint reviews, UAT). Reforçando a lacuna, a própria **`GQA-P01` registrou a NC-01: requisitos documentados retroativamente nos sprints 1–3** (desenvolvimento começou sem requisitos formais). A NC foi resolvida, mas evidencia que o entendimento não foi confirmado *antes* da construção inicial.
- **Critérios de aceite (R49 — OK com ressalva):** a tabela de RF **não traz critérios de aceite por requisito**; eles existem como "resultado esperado" nos cenários de teste (`CTQ`, `VV §5`) e estão rastreados (RASTR). Está coberto, mas a localização não é a usual — vale embutir os critérios no próprio REQ.

### 4. Documentação técnica para sustentação [R57 PARCIAL]

O `PCP` é forte em arquitetura, modelo de dados, fluxos e segurança, mas **não há manual de sustentação**. A `ADAP A-06` formaliza que a documentação de baixo nível ficou nos PRs do Azure DevOps; a sustentação é objeto de contrato futuro. É uma adaptação justificada, mas o item permanece parcial para fins de "manuais para sustentação".

### 5. Evidências de aceite [R76 PARCIAL]

O aceite formal está bem documentado (TAE §9 + ATA-002 §8, declaração de Humberto Erler). Falta apenas **anexar o e-mail/registro externo original** do aceite/entrega (R76) — hoje é referenciado, não anexado.

---

## Inconsistência a corrigir (não altera status, mas um avaliador apontaria)

Os **registros de defeito do CTQ e do REL-VV divergem para os mesmos IDs de bug**:

| ID | `CTQ §9` | `REL-VV §5` |
|---|---|---|
| BAL-B01 | "código do cliente diverge do `id_cliente` na API" | "código de **opt-in** diverge do registrado no banco" (S2) |
| BAL-B02 | "consulta após truncate envia UPDATE" | "**opt-out não reseta pontos de fidelidade** no Propz" (S2) |
| BAL-B03 | "opt-out não atualiza flag fidelidade" | "**consulta após truncate gera UPDATE**" (S1) |
| PDV-B01 | "cadastro persiste com `opt_in=true`, cliente não encontrado" | "cadastro via PDV **persiste parcialmente — endereço não salvo**" (S1) |

As descrições/severidades estão **trocadas entre os dois documentos**. O conteúdo de teste é forte e a reconciliação para 100% está clara no `REL-VV §4`, mas a rastreabilidade de defeito fica comprometida. **Recomendação:** unificar a tabela de defeitos (uma fonte única — preferencialmente o REL-VV) e referenciá-la no CTQ. Menor: `REQ §7` chama o controle de mudanças de "change request conforme GMUD", conflando CR (mudança de requisito) com GMUD (autorização de deploy) — convém separar os termos.

---

## Pontos fortes (para não enviesar a leitura)

- **GPR:** TAP/PLA/RAC/TAE completos; 6 fases com planejado×realizado, riscos materializados e ações corretivas; SPI 0,91 com causa-raiz (MED §5).
- **Controle de mudanças (R51 OK):** registro CR-01 a CR-12 auditado pela GQA-P02 e reconhecido no TAE — consistente (sem a contradição vista no FTFRUKI).
- **V&V:** 273 testes unitários (84% cobertura), REL-VV com 7 níveis, REV com 3 revisões por pares formais, homologação 100% por canal, piloto sem incidentes S1.
- **GQA (R80/R81 OK):** três auditorias e **registro de NC formal com ação corretiva** (NC-01/NC-02) — supera os demais projetos da amostra neste ponto.
- **GDE/MED:** cinco decisões arquiteturais rigorosas e medição com índice de desempenho e análise de variância.

---

## Recomendações priorizadas

1. **Produzir o registro de GCO do projeto** (lista de ICs, baselines/tags, histórico de mudanças, **auditoria de configuração**) — fecha os dois únicos FALTA, ambos REQUERIDO.
2. **Criar a Estratégia de Integração (ITP)** consolidando interfaces (já descritas em REQ/PCP), ordem de integração, ambiente, prontidão de componentes e release notes.
3. **Unificar os registros de defeito** (CTQ × REL-VV) e corrigir a inconsistência de IDs/severidade.
4. **Embutir critérios de aceite no REQ** e acrescentar a seção de confirmação de entendimento dos requisitos.
5. **Anexar** o e-mail/registro externo de aceite (R76) e um **manual mínimo de sustentação** (R57).
