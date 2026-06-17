# Relatório de Acompanhamento — SuperApp Fruki · Pacote 1

## 0. Identificação do ciclo

| Campo | Valor |
|---|---|
| **Documento** | RAC-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Plano de referência** | PLA-FRUKI01-001 v1.3 |
| **Período / ciclo** | 05/06/2025 – Set/2025 (encerramento do Pacote 1) |
| **Data do relatório** | Set/2025 |
| **Responsável** | Abraão Oliveira |

---

## 1. Monitoramento do planejado vs. realizado

### 1.1 Progresso de escopo e tarefas

| Módulo / Entregável | Planejado | Realizado | Desvio | Comentário |
|---|---|---|---|---|
| RF-01 — Tela de metas por família de produtos | Jun–Jul/2025 | Concluído — Jul/2025 | 0 | Integração com `/acompanhamentoMetasFamilias` funcional |
| RF-02 — Indicadores de cobertura, drop size e positivação | Jul/2025 | Concluído — Jul/2025 | 0 | Reutilizou padrão de integração da RF-01 |
| RF-03 — Composição de RV estimada por perfil | Jul–Ago/2025 | Concluído — Ago/2025 | 0 | |
| RF-04 — Adaptação de telas por perfil (representante / supervisor) | Ago/2025 | Concluído — Ago/2025 | 0 | |
| Piloto com vendedores selecionados | 05/08/2025 | Realizado — 05/08/2025 | 0 | Defeitos P-01 e P-02 identificados; corrigidos antes do aceite |
| Ajustes pós-piloto (normalização, cálculo de positivação) | Ago/2025 | Concluído — Ago/Set/2025 | +2 semanas | Identificação de P-01 (duplicação de famílias) e P-02 (cálculo de positivação); ver ATA-FRUKI01-007 |
| PR e aceite final | Set/2025 | Concluído — Set/2025 | 0 | PR revisada e mergeada por Jardel; aceite de Leandro Lottermann |

**Escopo entregue:** 4/4 RFs (100%)
**Aceite formal:** Set/2025 — Leandro Lottermann (Fruki)

### 1.2 Estimado vs. realizado (esforço)

| Sprint | SP estimados | SP entregues | Comentário |
|---|---|---|---|
| Sprint 1 — RF-01 e RF-02 | 32 SP | 34 SP | +2 SP — tratamento de latência e deduplicação de dados da API não previsto no planejamento inicial |
| Sprint 2 — RF-03, RF-04 e piloto | 28 SP | 30 SP | +2 SP — ajustes pós-piloto (P-01: deduplicação de famílias; P-02: cálculo de positivação) |
| **Total** | **60 SP** | **64 SP** | **+4 SP (+6,7%)** — absorvido sem impacto no prazo de aceite |

- **Velocity Sprint 1:** ~34 SP / 4 semanas
- **Velocity Sprint 2:** ~30 SP / 4–5 semanas (inclui ajustes pós-piloto)
- **Velocity média observada:** ~32 SP/sprint (compatível com estimativa de 30–35 SP do PLA-FRUKI01-001)

**Horas estimadas × realizadas:**

| Dimensão | Estimado | Realizado | Desvio |
|---|---|---|---|
| Esforço total (horas) | 784 h | ~847 h | +8% |

*Base: orçamento de horas por papel em PLA-FRUKI01-001 §4 (784 h para 4 sprints de 2 semanas). Desvio alinhado ao desvio de SP (+8%).*

### 1.3 Cronograma

| Marco | Planejado | Realizado | Desvio |
|---|---|---|---|
| Kickoff | 05/06/2025 | 05/06/2025 | 0 |
| Levantamento de requisitos | 25/06/2025 | 25/06/2025 | 0 |
| Acesso ao repositório Azure DevOps | 26/06/2025 | 26/06/2025 | 0 |
| Piloto com vendedores selecionados | Ago/2025 | 05/08/2025 | 0 |
| Correções pós-piloto | Ago/Set/2025 | Ago/Set/2025 | 0 |
| Aceite formal | Set/2025 | Set/2025 | 0 |

### 1.4 Recursos

| Dimensão | Planejado | Realizado | Desvio |
|---|---|---|---|
| Equipe Timeware | Abraão (GP/PO), Brenda (UX/analista), Luca + Thiago (devs) | Conforme planejado | 0 |
| APIs Fruki | Disponíveis antes do desenvolvimento | Credenciais fornecidas em 26/06/2025; APIs com latência elevada (~3,10s) e retorno de dados duplicados | Normalização e deduplicação implementadas no front-end — sem impacto de prazo |

---

## 2. Envolvimento das partes interessadas

- **Cecília Ribeiro:** validou os protótipos antes do desenvolvimento; participou do feedback do piloto (ago/2025); aprovou os ajustes pós-piloto antes do aceite.
- **Leandro Lottermann:** acompanhou o progresso via e-mail; concedeu acesso ao repositório Azure DevOps em 26/06/2025; emitiu o aceite formal em set/2025.
- **Jardel Dargas Silva:** disponibilizou as credenciais de API (26/06/2025); revisou e aprovou a Pull Request antes do merge.

---

## 3. Transição para operação e suporte

Concluída via merge da Pull Request no repositório Azure DevOps da Fruki. O código foi integrado ao codebase do SuperApp Fruki e passou a ser mantido pelo time técnico da Fruki. A Timeware não mantém ambiente de sustentação — novas demandas seguem nova proposta comercial.

Sequência natural: encerramento do Pacote 1 → abertura do Pacote Final 24 (09/10/2025), com continuidade na mesma base de código.

---

## 4. Riscos e oportunidades

| ID | Risco | Situação final | Ocorrência | Comunicado a |
|---|---|---|---|---|
| R-01 | APIs da Fruki com latência elevada ou formato não padronizado | **Encerrado** — normalização e deduplicação implementadas no front-end; ver GDE-FRUKI01-001 Decisão 1 | Parcialmente materializado (latência + dados duplicados); tratado sem impacto de prazo | Leandro Lottermann (via e-mail de status) |
| R-02 | Atraso na validação de protótipos por Cecília | **Encerrado** | Não ocorreu; validações dentro do prazo | — |
| R-03 | Mudança de escopo durante o desenvolvimento | **Encerrado** | Não ocorreu durante o Pacote 1; mudança de escopo (Regra de Ouro) tratada no Pacote Final 24 via CR-FRUKI01-001 | — |
| R-04 | Dificuldade de agenda para validação de protótipos com Cecília | **Encerrado** | Não ocorreu; protótipos validados antes de cada sprint sem bloqueio de agenda | — |

---

## 5. Ações corretivas e questões

| ID | Questão / desvio | Ação tomada | Tratada com | Responsável | Situação |
|---|---|---|---|---|---|
| AC-01 | Duplicação de famílias de produtos na tela de metas (detectada no piloto) | Deduplicação implementada em `metasService.ts` antes do aceite | Jardel (revisão de PR) | Luca Watson | Resolvida — Ago/2025 |
| AC-02 | Cálculo de positivação inconsistente com o sistema Fruki (detectado no piloto) | Fórmula alinhada com Jardel; cálculo corrigido no serviço front-end | Jardel / Cecília | Luca Watson | Resolvida — Ago/Set/2025 |

---

## 6. Análise de resultados significativos

| Resultado | Análise de causa | Encaminhamento |
|---|---|---|
| Piloto revelou dois defeitos de negócio (P-01 e P-02) não detectados durante o desenvolvimento | APIs da Fruki com dados reais apresentaram casos que os mocks de desenvolvimento não simulavam (duplicatas, fórmula de positivação) | Incluir casos extremos da API nos cenários de teste antes do piloto; usar mocks que simulem duplicados e valores não padronizados — ver LI-FRUKI01-001 LE-02 |
| Prazo mantido apesar dos +4 SP de esforço pós-piloto | Ajustes foram localizados em `metasService.ts`; arquitetura bem isolada facilitou correções rápidas | Manter separação de responsabilidades (service layer para normalização, tela para apresentação) como padrão arquitetural |
| Zero retrabalho de UX | Protótipos validados por Cecília antes do desenvolvimento eliminaram retrabalho de interface | Manter validação de protótipo com PO do cliente antes de cada sprint — ver LI-FRUKI01-001 LE-01 |

---

## 7. Melhorias de processo propostas

| O que funcionou | Por que propor como melhoria | Encaminhado para |
|---|---|---|
| Validação de protótipos com Cecília antes de cada sprint | Eliminou retrabalho de UX; aumentou previsibilidade de sprint | LI-FRUKI01-001 — LE-01 / processo organizacional GPR |
| Normalização de dados no front-end (`metasService.ts`) | Desacoplou a entrega do time Timeware da qualidade dos dados da API do cliente | LI-FRUKI01-001 — OM-05 / processo organizacional GPR |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun–set/2025) |
| 1.1 | 17/06/2026 | Abraão Oliveira | §1.2 ampliado: adição de tabela de horas estimadas × realizadas (784 h → ~847 h; desvio +8%) |
