# Mapa de Artefatos — MPS-SW Nível C — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | MAPA-ORG-001 — Mapa de Artefatos / Plano de Implantação |
| **Versão** | 0.18 (rascunho) |
| **Data** | 02/06/2026 |
| **Modelo de referência** | MR-MPS-SW:2024 — Nível C |
| **Avaliadora (IA)** | ASR Consultoria e Assessoria em Qualidade Ltda. |
| **Fonte de escopo** | PlanilhaIndicadores_SW_2024__NivelC.xlsx |
| **Nº de projetos na avaliação** | 4 (a definir quais — Fase 3) |
| **Responsável (ponto focal)** | Abraão Oliveira |

> **Alterações v0.2 (02/06/2026):** resolução das 5 pendências de escopo. OSW 8/9/10 confirmados no escopo (há gestão de portfólio). AQU mantido, mas movido para o fim da fila (candidato a não-aplicável, a confirmar com a ASR). Ferramentas definidas (Jira, Git, Azure DevOps, Azure Test Plans/Xray, Confluence). Papel de GQA confirmado. Ver seção 3 para detalhes.

> **Como usar este mapa:** é o painel de controle da implantação. Cada processo tem seus resultados esperados (o que a avaliação verifica) e os artefatos que servem de evidência. A coluna **Status** é atualizada conforme avançamos. A coluna **Local** indica onde o artefato vai viver (Confluence, template, ferramenta, registro por projeto).
>
> **Legenda de Status:** ⬜ A fazer · 🟨 Em andamento · ✅ Pronto · 🔵 Revisar
>
> **Legenda de Tipo:** `ORG` = artefato organizacional (faz 1 vez) · `PROJ` = artefato de projeto (preenche por projeto, x4) · `TPL` = template/modelo · `DEF` = documento de definição/política

> **Nota importante sobre os processos de PROJETO (GPR, REQ, PCP, ITP, VV):** o status ✅ nesses processos indica que a **definição do processo e os templates** estão prontos (camada organizacional). A **evidência de uso** — os templates preenchidos em cada um dos 4 projetos da avaliação — é uma etapa posterior (camada de evidência), ainda a ser produzida quando os 4 projetos forem selecionados e documentados. Definição pronta ≠ evidência nos projetos.


---

## 1. Visão geral — ordem de construção

A implantação segue do macro (governança organizacional) para o granular (execução de projeto), terminando pela camada de capacidade que atravessa tudo. Esta é a ordem recomendada de trabalho:

| Fase | Camada | Processos | Por quê primeiro |
|---|---|---|---|
| **1** | Governança | OSW, GPC | Definem a estrutura, a política e a *biblioteca de processos* que todo o resto usa |
| **2** | Apoio organizacional | MED, CAP, GDE, GCO, AQU | Serviços organizacionais que os projetos consomem |
| **3** | Execução de projeto | GPR, REQ, PCP, ITP, VV | O ciclo de vida do projeto, adaptado do processo-padrão |
| **4** | Capacidade (transversal) | CP_Projeto, CP_Organizacional | Institucionalização — aplica-se a TODOS os processos acima |

---

## 2. Estrutura de pastas / organização proposta

```
MPS-Nivel-C/
├── 00_Governanca/          (OSW, GPC) — DEF/ORG → Confluence
├── 01_Apoio/               (MED, CAP, GDE, GCO, AQU) — DEF/ORG + TPL
├── 02_Projeto/             (GPR, REQ, PCP, ITP, VV) — DEF/ORG + TPL
├── 03_Templates/           (todos os TPL em branco) → modelos Confluence/Word
├── 04_Registros/           (TPL preenchidos por projeto)
│   ├── Projeto-1/
│   ├── Projeto-2/
│   ├── Projeto-3/
│   └── Projeto-4/
└── 05_Capacidade/          (evidências de institucionalização — garantia da qualidade, melhoria)
```

---

## 2.1 Documentos já produzidos

| Código | Documento | Versão | Atende | Situação |
|---|---|---|---|---|
| MAPA-ORG-001 | Mapa de Artefatos / Plano de Implantação | 0.18 | GPC 1 (rastreabilidade) | Rascunho |
| CONV-ORG-001 | Convenção de Nomenclatura e Versionamento | 1.0 | GCO 1, GCO 4 | Aprovado |
| POL-ORG-001 | Política Organizacional de Processos | 1.0 | OSW 1 | Aprovado |
| PRO-GPC-001 | Processo-Padrão Organizacional | 1.0 | GPC 2 | Aprovado |
| GUIA-GPC-001 | Guia de Adaptação do Processo-Padrão | 1.0 | GPC 2 | Aprovado |
| EST-GPC-001 | Estratégia de Garantia da Qualidade | 1.1 | GPC 3; CP (iv,v,vi) | Aprovado |
| PRO-GPC-002 | Definição do Time de Melhoria Contínua | 1.1 | GPC 6 | Aprovado |
| EST-GPC-002 | Estratégia de Gerência de Riscos e Oportunidades | 1.1 | GPC 7 | Aprovado |
| PLA-GPC-001 | Plano de Gestão e Melhoria de Processos | 1.2 | GPC 1, 4, 5, 8, 10, 11 | Aprovado |
| PRO-OSW-001 | Governança Organizacional de Processos | 1.1 | OSW 2, 3, 4, 5, 6, 7 | Aprovado |
| PRO-OSW-002 | Gestão de Portfólio de Projetos | 1.1 | OSW 8, 9, 10 | Aprovado |
| PLA-MED-001 | Plano de Medição | 1.0 | MED 1-7; GPC 9; OSW 6 | Aprovado |
| PLA-GCO-001 | Plano de Gerência de Configuração | 1.0 | GCO 1-5 | Aprovado |
| PRO-GDE-001 | Processo de Gerência de Decisões | 1.0 | GDE 1-6 | Aprovado |
| PLA-CAP-001 | Plano de Capacitação | 1.0 | CAP 1-4 | Aprovado |
| PRO-AQU-001 | Processo de Aquisição | 1.0 | AQU 1-4 | Aprovado (a confirmar aplicabilidade c/ ASR) |
| PRO-GPR-001 | Processo de Gerência de Projetos | 1.0 | GPR 1-20 | Aprovado |
| TPL-GPR-001 | Template de Plano de Projeto | 1.0 | GPR (template) | Aprovado |
| PRO-REQ-001 | Processo de Engenharia de Requisitos | 1.0 | REQ 1-7 | Aprovado |
| TPL-REQ-001 | Template de Documento de Requisitos | 1.0 | REQ (template) | Aprovado |
| TPL-REQ-002 | Template de Matriz de Rastreabilidade | 1.0 | REQ 4 (template) | Aprovado |

---

## FASE 1 — GOVERNANÇA

### OSW — Gerência Organizacional de Software
*Propósito: dar à gerência instrumentos para apoiar os processos e alinhar objetivos de negócio, processos, recursos e projetos.*

| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| OSW 1 | Diretrizes de definição/melhoria de desempenho definidas e comunicadas | **POL-ORG-001 — Política Organizacional de Processos** | DEF/ORG | Confluence | ✅ |
| OSW 2 | Recursos e treinamento garantidos pela gerência | **PRO-OSW-001 §3** | ORG | Confluence | ✅ |
| OSW 3 | Informações de governança identificadas e usadas | **PRO-OSW-001 §6** | ORG | Jira/Confluence | ✅ |
| OSW 4+ | Autoridade, competências e colaboradores alinhados aos objetivos | **PRO-OSW-001 §4** | DEF/ORG | Confluence | ✅ |
| OSW 5+ | Riscos/oportunidades organizacionais geridos | **PRO-OSW-001 §5** + EST-GPC-002 | ORG | Jira | ✅ |
| OSW 6 | Coleta/análise/uso de medidas organizacionais garantidos | **PRO-OSW-001 §6 + PLA-MED-001 §5** | ORG | Jira | ✅ |
| OSW 7 | Alinhamento dos processos aos objetivos garantido | **PRO-OSW-001 §7** — análise crítica trimestral | ORG | Confluence | ✅ |
| OSW 8 | Oportunidades de negócio/investimentos priorizados (portfólio) | **PRO-OSW-002 §3** | DEF/ORG | Confluence | ✅ |
| OSW 9 | Recursos/orçamento/autoridade do portfólio estabelecidos | **PRO-OSW-002 §4** + quadro de capacity | ORG | Confluence | ✅ |
| OSW 10 | Projetos do portfólio mantidos/tratados conforme acordos | **PRO-OSW-002 §5** | ORG | Confluence | ✅ |

> **OSW 8/9/10 — CONFIRMADOS NO ESCOPO (v0.2).** A TIMEWARE gerencia portfólio: recursos compartilhados entre projetos (tech lead, arquiteto, PO) com gestão de capacity; quando necessário, puxa recursos de fora da unidade ou contrata. Já existe um quadro/registro de capacity informal — será formalizado como evidência principal de OSW 9/10.

### GPC — Gerência de Processos
*Propósito: estabelecer e melhorar a biblioteca de ativos de processo da organização; definir estratégias de qualidade e de risco.*

| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| GPC 1 | Ativos de processo necessários identificados | **PLA-GPC-001 §2** — Inventário de ativos | DEF/ORG | Confluence | ✅ |
| GPC 2+ | Estratégia de arquitetura de processos + biblioteca + diretrizes de adaptação | **PRO-GPC-001 Processo-Padrão Organizacional** (✅) + **GUIA-GPC-001 Guia de Adaptação** (✅) | DEF/ORG | Confluence | ✅ |
| GPC 3 | Estratégia e plano(s) de garantia da qualidade | **EST-GPC-001 — Estratégia de Garantia da Qualidade** | DEF/ORG | Confluence | ✅ |
| GPC 4+ | Oportunidades de melhoria identificadas e mantidas | **PLA-GPC-001 §5.1** — Registro de Oportunidades de Melhoria | ORG | Jira | ✅ |
| GPC 5+ | Plano de implementação de melhorias | **PLA-GPC-001 §5** | ORG | Confluence | ✅ |
| GPC 6 | Estrutura de apoio (SEPG/grupo de processos) estabelecida | **PRO-GPC-002 — Definição do Time de Melhoria Contínua** | DEF/ORG | Confluence | ✅ |
| GPC 7 | Estratégia de gerência de riscos e oportunidades | **EST-GPC-002 — Estratégia de Gerência de Riscos** | DEF/ORG | Confluence | ✅ |
| GPC 8 | Ambientes padrão de trabalho estabelecidos | **PLA-GPC-001 §3** | DEF/ORG | Confluence | ✅ |
| GPC 9 | Repositório organizacional de medidas + garantia da qualidade de medidas | **PLA-MED-001 §4 e §8** | DEF/ORG | Jira | ✅ |
| GPC 10 | Processos-padrão implantados na organização | **PLA-GPC-001 §4** | ORG | Confluence | ✅ |
| GPC 11 | Efetividade das melhorias avaliada e relatada | **PLA-GPC-001 §6** | ORG | Confluence | ✅ |

---

## FASE 2 — APOIO ORGANIZACIONAL

### MED — Medição
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| MED 1 | Objetivos de medição derivados dos objetivos de negócio | **PLA-MED-001 §2** | DEF/ORG | Confluence | ✅ |
| MED 2 | Medidas com definições operacionais | **PLA-MED-001 §3** — Catálogo de Medidas | DEF/ORG | Confluence | ✅ |
| MED 3+ | Medidas coletadas, verificadas e armazenadas | **PLA-MED-001 §4** | ORG | Jira | ✅ |
| MED 4+ | Desempenho organizacional analisado | **PLA-MED-001 §5** | ORG | Jira | ✅ |
| MED 5 | Ações corretivas a partir das medidas | **PLA-MED-001 §6** | ORG | Jira | ✅ |
| MED 6 | Resultados comunicados periodicamente | **PLA-MED-001 §7** | ORG | Confluence | ✅ |
| MED 7 | Repositório avaliado periodicamente (qualidade de medidas) | **PLA-MED-001 §8** | DEF/ORG | Confluence | ✅ |

> **MED — nota de ferramenta (v0.2):** o Jira é o repositório de medidas. Atenção na produção: o avaliador exige que os indicadores sejam **consolidados e analisados ao longo do tempo** (não números soltos por projeto). Provável necessidade de uma camada de consolidação — dashboard do Jira ou planilha de indicadores organizacional. Definir no Plano de Medição.

### CAP — Capacitação
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| CAP 1+ | Necessidades de capacitação identificadas + planos | **PLA-CAP-001 §3** | DEF/ORG | Confluence | ✅ |
| CAP 2 | Treinamentos realizados e registrados | **PLA-CAP-001 §4** (controle de capacitação) | ORG | Confluence | ✅ |
| CAP 3 | Efetividade do programa avaliada e comunicada | **PLA-CAP-001 §5** | ORG | Confluence | ✅ |
| CAP 4 | Habilidades de instrutores e recursos mantidos | **PLA-CAP-001 §6** | ORG | Confluence | ✅ |

### GDE — Gerência de Decisões
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| GDE 1 | Diretrizes de quando usar decisão formal | **PRO-GDE-001 §3** (gatilhos) | DEF/ORG | Confluence | ✅ |
| GDE 2–6 | Problema, alternativas, critérios, métodos, avaliação e decisão registrados | **PRO-GDE-001 §4-5** (processo + RAD) | DEF/ORG + PROJ | Confluence | ✅ |

### GCO — Gerência de Configuração
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| GCO 1 | Itens de configuração identificados + níveis de controle | **PLA-GCO-001 §3** | DEF/ORG | Confluence | ✅ |
| GCO 2 | Sistema de GC e controle de mudanças | **PLA-GCO-001 §4** | DEF/ORG | Git/Azure DevOps | ✅ |
| GCO 3 | Baselines estabelecidas | **PLA-GCO-001 §5** (tags/releases) | PROJ | Git/Azure DevOps | ✅ |
| GCO 4 | Registros de itens e modificações | **PLA-GCO-001 §6** | PROJ | Git/Azure DevOps | ✅ |
| GCO 5 | Auditorias de configuração executadas | **PLA-GCO-001 §7** (auditoria via GQA) | DEF/ORG | Confluence | ✅ |

### AQU — Aquisição
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| AQU 1 | Critérios de avaliação de fornecedores + pedidos de proposta | **PRO-AQU-001 §3** | DEF/ORG | Confluence | ✅ |
| AQU 2 | Respostas avaliadas e fornecedor selecionado | **PRO-AQU-001 §4** | DEF/ORG + PROJ | Confluence | ✅ |
| AQU 3+ | Desempenho do fornecedor monitorado (acordo) | **PRO-AQU-001 §5** | DEF/ORG + PROJ | Confluence | ✅ |
| AQU 4+ | Revisão técnica das entregas do fornecedor documentada | **PRO-AQU-001 §6** | DEF/ORG + PROJ | Confluence | ✅ |

> **AQU — DECISÃO v0.2: ÚLTIMO A PRODUZIR / CANDIDATO A NÃO-APLICÁVEL.** A TIMEWARE confirmou que **nenhum dos 4 projetos** da avaliação tem aquisição/subcontratação de desenvolvimento (todo o desenvolvimento é feito por colaboradores próprios sob gestão da TIMEWARE). Ação: (1) confirmar a não-aplicabilidade com o **avaliador líder da ASR**; (2) se a ASR exigir, produzir apenas a versão organizacional enxuta (Critérios de Seleção + Template de Acordo/Monitoramento) "na prateleira". **Não bloqueia o restante da implantação.**

---

## FASE 3 — EXECUÇÃO DE PROJETO

### GPR — Gerência de Projetos
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| GPR 1 | Escopo estabelecido e mantido | Termo de Abertura / Escopo (no Plano de Projeto) | PROJ | Registros | ✅ |
| GPR 2+ | Processo definido para o projeto (adaptado do padrão) | **Registro de Adaptação do Processo (Tailoring)** | TPL + PROJ | Template→Registros | ✅ |
| GPR 3+ | Estimativas de dimensão | Registro de estimativa de dimensão | PROJ | Registros | ✅ |
| GPR 4+ | Estimativas de esforço, duração, custo (baseadas no repositório) | Registro de estimativas | PROJ | Registros | ✅ |
| GPR 5 | Orçamento e cronograma com marcos | Cronograma + orçamento | PROJ | Jira | ✅ |
| GPR 6 | Recursos humanos planejados | Plano de recursos humanos (no Plano) | PROJ | Registros | ✅ |
| GPR 7+ | Recursos materiais e ambiente de trabalho | Plano de recursos materiais/ambiente | PROJ | Registros | ✅ |
| GPR 8 | Estratégia de transição p/ operação e suporte | Plano de transição | PROJ | Registros | ✅ |
| GPR 9 | Envolvimento das partes interessadas planejado | Plano de comunicação/partes interessadas | PROJ | Registros | ✅ |
| GPR 10+ | Riscos/oportunidades do projeto tratados | Registro de riscos do projeto | PROJ | Jira | ✅ |
| GPR 11 | Viabilidade do projeto avaliada | Registro de análise de viabilidade | PROJ | Registros | ✅ |
| GPR 12+ | Plano geral integrado e mantido | **Template de Plano de Projeto** | TPL + PROJ | Template→Registros | ✅ |
| GPR 13+ | Plano revisado com interessados + compromisso obtido | Ata de revisão/compromisso do plano | PROJ | Registros | ✅ |
| GPR 14+ | Monitoramento do planejado vs. realizado | **Template de Relatório de Acompanhamento** | TPL + PROJ | Template→Registros | ✅ |
| GPR 15 | Envolvimento das partes interessadas monitorado | (no relatório de acompanhamento) | PROJ | Registros | ✅ |
| GPR 16 | Transição monitorada | (no relatório de acompanhamento) | PROJ | Registros | ✅ |
| GPR 17+ | Riscos monitorados e comunicados | (no registro de riscos) | PROJ | Jira | ✅ |
| GPR 18+ | Ações corretivas identificadas e acompanhadas | Registro de ações/issues | PROJ | Jira | ✅ |
| GPR 19+ | Resultados significativos analisados (causas) | Registro de análise de causas | PROJ | Registros | ✅ |
| GPR 20 | Mudanças eficazes propostas como melhoria | (alimenta GPC 4) | PROJ | Confluence | ✅ |

### REQ — Engenharia de Requisitos
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| REQ 1 | Necessidades das partes interessadas identificadas + entendimento confirmado | **Documento de Requisitos** | TPL + PROJ | Template→Registros | ✅ |
| REQ 2+ | Requisitos especificados, priorizados, alocados | (no Documento de Requisitos) | PROJ | Registros | ✅ |
| REQ 3 | Compromisso da equipe técnica obtido | Ata/registro de compromisso | PROJ | Registros | ✅ |
| REQ 4 | Rastreabilidade bidirecional | **Matriz de Rastreabilidade** | TPL + PROJ | Template→Registros | ✅ |
| REQ 5 | Planos/produtos revisados vs. requisitos | Registro de revisão de consistência | PROJ | Registros | ✅ |
| REQ 6 | Requisitos analisados (necessários e suficientes) | Registro de análise de requisitos | PROJ | Registros | ✅ |
| REQ 7 | Requisitos validados | Registro de validação de requisitos | PROJ | Registros | ✅ |

### PCP — Projeto e Construção do Produto
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| PCP 1+ | Design desenvolvido com solução baseada em critérios + rastreável | **Documento de Design / Arquitetura** | TPL + PROJ | Template→Registros | ⬜ |
| PCP 2 | Design avaliado e problemas tratados | Registro de revisão de design | PROJ | Registros | ⬜ |
| PCP 3+ | Produto implementado conforme design + informações mantidas | Código/build + documentação técnica | PROJ | Git/Azure DevOps | ⬜ |

### ITP — Integração do Produto
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| ITP 1+ | Estratégia de integração + interfaces | **Estratégia/Plano de Integração** | TPL + PROJ | Template→Registros | ⬜ |
| ITP 2 | Ambiente de integração estabelecido | Definição do ambiente de integração | PROJ | Azure DevOps | ⬜ |
| ITP 3+ | Componentes avaliados antes de integrar | Registro de prontidão de componente | PROJ | Registros | ⬜ |
| ITP 4 | Componentes integrados conforme estratégia | Registro de integração | PROJ | Azure DevOps | ⬜ |
| ITP 5+ | Produto integrado testado | Registro de testes de integração | PROJ | Registros | ⬜ |
| ITP 6 | Produto e material de apoio entregues | Registro de entrega + material de apoio | PROJ | Registros | ⬜ |

### VV — Verificação e Validação
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| VV 1 | Produtos a verificar/validar selecionados (testes + revisão por pares) | **Plano de V&V** | TPL + PROJ | Template→Registros | ⬜ |
| VV 2 | Procedimentos e material p/ revisão por pares | **Template de Revisão por Pares** | TPL + PROJ | Template→Registros | ⬜ |
| VV 3+ | Métodos, critérios e ambientes de V&V | (no Plano de V&V) | PROJ | Registros | ⬜ |
| VV 4 | Atividades de V&V realizadas + problemas tratados | Registros de teste + revisão por pares | PROJ | Registros | ⬜ |
| VV 5 | Resultados analisados, registrados e comunicados | Relatório de V&V | PROJ | Registros | ⬜ |

> **V&V — nota de ferramenta (v0.2):** testes registrados em **Azure Test Plans + Jira/Xray**. Fluxo aceito: casos de teste começam em planilha e depois são importados para a ferramenta — documentar isso explicitamente no Plano de V&V para o avaliador entender que é intencional. Revisão por pares pode ser evidenciada via pull request (Git/Azure) + registro de revisão.

---

## FASE 4 — CAPACIDADE (TRANSVERSAL A TODOS OS 13 PROCESSOS)

> **Atenção:** os atributos CP-E/D/C **não são um processo separado**. São exigências de *institucionalização* que o avaliador verifica para **cada um** dos 13 processos. É o que diferencia o Nível C de níveis iniciais.

| Atributo (CP-E/D/C) | O que exige | Como evidenciamos (transversal) | Status |
|---|---|---|---|
| (i) Processo produz resultados definidos | O processo realmente funciona | Registros de uso em cada processo | ⬜ |
| (ii) Processo-padrão + diretrizes de adaptação usados | Planejar/executar/monitorar com papéis, infra, produtos | Tailoring (GPR 2+) + processo-padrão (GPC 2+) | ⬜ |
| (iii) Pessoas preparadas para o processo | Capacitação adequada | Plano de Capacitação (CAP) + registros | ⬜ |
| (iv) Verificação objetiva de que o processo é seguido | Auditoria de aderência ao processo | **Registros de Garantia da Qualidade (GQA)** | ⬜ |
| (v) Produtos de trabalho avaliados objetivamente | Revisão de produtos vs. padrão | Registros de GQA de produtos | ⬜ |
| (vi) Oportunidades de melhoria identificadas | Durante a garantia da qualidade | Alimenta GPC 4 (oport. de melhoria) | ⬜ |
| (vii) Informações disponibilizadas à organização | Compartilhar ativos/medidas | Biblioteca de processos + repositório de medidas | ⬜ |

---

## 3. Pendências de escopo — status (resolvidas em 02/06/2026)

| # | Pendência | Status | Decisão |
|---|---|---|---|
| 1 | **Portfólio (OSW 8/9/10)** | ✅ Resolvido | **No escopo.** TIMEWARE gerencia portfólio: recursos compartilhados (tech lead, arquiteto, PO) + gestão de capacity. Há quadro de capacity informal a formalizar. |
| 2 | **Aquisição (AQU)** | ✅ Resolvido (com ação) | **Último a produzir / candidato a não-aplicável.** Nenhum dos 4 projetos tem aquisição. Confirmar não-aplicabilidade com o avaliador líder da ASR. |
| 3 | **Os 4 projetos** | 🟨 Adiado p/ Fase 3 | Ainda não definidos. Não bloqueia a produção organizacional (Fases 1 e 2). Definir antes da Fase 3. Precisam permitir evidenciar o ciclo completo (requisito → design → construção → integração → V&V). |
| 4 | **Ferramentas** | ✅ Resolvido | Jira (gestão de projeto, riscos, ações, repositório de medidas) · Git + Azure DevOps (código, baselines, integração/CI-CD) · Azure Test Plans + Jira/Xray (testes) · Confluence (definições/registros). |
| 5 | **Garantia da Qualidade (GQA)** | ✅ Resolvido | Pessoa/área de GQA existe na TIMEWARE. Detalhar nome/papel ao produzir a Estratégia de GQA (GPC 3). |

**Itens que seguem como ação aberta (não bloqueiam a produção):**
- Confirmar não-aplicabilidade do AQU com a ASR (ponto 2).
- Definir os 4 projetos antes da Fase 3 (ponto 3).
- MED: definir camada de consolidação de indicadores (dashboard Jira ou planilha organizacional).

---

## 4. Próximos passos sugeridos

1. ✅ **Mapa de Artefatos** (este documento) — v0.2, pendências de escopo resolvidas
2. ⬜ Iniciar **FASE 1**: começar pelo **GPC 2+ (Processo-Padrão Organizacional + Guia de Adaptação)** — espinha dorsal que tudo referencia
3. ⬜ Em seguida: **Política Organizacional (OSW 1)** e **Estratégia de Garantia da Qualidade (GPC 3)**
4. ⬜ Ao chegar na Fase 3: definir os 4 projetos e confirmar AQU com a ASR

> **Observação de auditoria:** este mapa também serve de evidência para GPC 1 (identificação de ativos de processo) e como rastreabilidade entre resultados esperados e artefatos — algo que a ASR vai querer ver logo no início.
