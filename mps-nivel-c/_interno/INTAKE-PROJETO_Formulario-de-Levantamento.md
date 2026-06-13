# Formulário de Levantamento de Projeto — MPS-SW Nível C

| Campo | Valor |
|---|---|
| **Documento** | INTAKE-PROJETO (interno) |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Uso** | Preencher antes de solicitar a geração dos documentos MPS do projeto |

> **Como usar:** preencha todos os blocos abaixo e entregue ao responsável pela geração dos documentos. Campos marcados com **\*** são obrigatórios para gerar o conjunto mínimo. Os demais enriquecem documentos específicos. Deixe em branco o que genuinamente não se aplica — não invente dados.

---

## BLOCO 1 — Identificação do projeto

*Alimenta: TAP, PLA, cabeçalhos de todos os documentos*

| Campo | Sua resposta |
|---|---|
| **\* Nome do projeto** | |
| **\* Código do projeto** | *(ex.: FTXXXXXX — prefixo do cliente + código interno)* |
| **\* Cliente / organização** | |
| **\* Produto ou sistema** | *(ex.: app mobile Android, plataforma web, API, etc.)* |
| **\* Objetivo principal** | *(1–3 frases: o que o projeto entrega e qual problema resolve)* |
| **\* Data de início** | |
| **\* Data de encerramento** | |
| **O projeto tem pacotes / fases distintas?** | *(sim/não — se sim, liste os nomes e períodos de cada um)* |
| **Código do pacote 1** | |
| **Código do pacote 2 (se houver)** | |

---

## BLOCO 2 — Equipe

*Alimenta: TAP, PLA §6, GQA, VV, ATAs*

### Equipe Timeware

| Papel | Nome |
|---|---|
| **\* Gerente de Projeto** | |
| **\* Tech Lead / Arquiteto** | |
| **Desenvolvedor(es)** | *(um por linha)* |
| **QA / Testes** | |
| **Designer UX/UI** | *(se aplicável)* |
| **\* Auditor GQA** | *(deve ser independente da equipe — normalmente COO)* |

### Stakeholders do cliente

| Papel | Nome | Responsabilidade |
|---|---|---|
| **\* Sponsor / responsável pelo aceite** | | |
| **PO / contato técnico** | | |
| **Revisor de código (se fizer code review)** | | |
| **Outros** | | |

---

## BLOCO 3 — Escopo e requisitos

*Alimenta: TAP, PLA §2, REQ, RASTR*

### Escopo

| Campo | Sua resposta |
|---|---|
| **\* O que está incluído** | *(liste os módulos / funcionalidades / entregas)* |
| **\* O que está fora do escopo** | |
| **Produto de entrada** | *(o que o cliente fornece: APIs, dados, protótipos, etc.)* |

### Requisitos funcionais

> Liste cada RF com: código, nome curto e descrição. Mínimo 1.

| Código | Nome | Descrição |
|---|---|---|
| RF-01 | | |
| RF-02 | | |
| RF-03 | | |
| *(adicione linhas conforme necessário)* | | |

### Requisitos não funcionais

| Código | Categoria | Descrição |
|---|---|---|
| RNF-01 | *(Performance / Segurança / Compatibilidade / Disponibilidade…)* | |
| RNF-02 | | |
| *(adicione linhas conforme necessário)* | | |

---

## BLOCO 4 — Adaptação do processo-padrão

*Alimenta: ADAP, PLA §3*

| Item | Decisão | Justificativa |
|---|---|---|
| **Design UX/UI** | *(aplicável / não aplicável)* | |
| **Nível de documentação** | *(enxuto / padrão / reforçado)* | |
| **Combinação de papéis** | *(ex.: Tech Lead acumula Arquiteto)* | |
| **Processo de revisão de código** | *(ex.: PR no Azure DevOps revisada por X)* | |
| **Processo de entrega** | *(ex.: APK via Expo / deploy em homologação / publicação na Play Store)* | |
| **Outras adaptações** | | |

---

## BLOCO 5 — Estimativas e cronograma

*Alimenta: PLA §4 e §5, RAC, planilha de gestão*

### Estimativas

| Campo | Valor |
|---|---|
| **\* Tamanho estimado (story points)** | |
| **\* Velocity de referência (pontos/sprint)** | |
| **\* Base histórica usada** | *(projetos ou sprints de referência)* |
| **Esforço/prazo estimado** | *(nº de sprints ou meses)* |
| **Duração de cada sprint** | *(ex.: 2 semanas)* |

### Marcos

| Marco | Data planejada | Data realizada |
|---|---|---|
| Kickoff | | |
| Fim do Discovery / Requisitos | | |
| Aprovação do Plano (baseline) | | |
| Fim Sprint 1 | | |
| Fim Sprint 2 | | |
| Fim Sprint 3 | | |
| *(adicione sprints)* | | |
| Piloto / Homologação | | |
| Aceite final / Encerramento | | |

---

## BLOCO 6 — Ambiente e configuração

*Alimenta: PLA §6, GCO*

| Campo | Valor |
|---|---|
| **\* Repositório de código** | *(ex.: Azure DevOps — org/projeto/repo)* |
| **\* Branch strategy** | *(ex.: main + feature branches; PR obrigatório para merge)* |
| **Ambiente de desenvolvimento** | |
| **Ambiente de homologação / staging** | |
| **Ambiente de produção** | |
| **\* Tecnologias principais** | *(ex.: React Native, Node.js, PostgreSQL)* |
| **Ferramentas de gestão** | *(ex.: Jira, Confluence, Teams, WhatsApp)* |
| **Baseline de configuração (versão entregue)** | *(ex.: tag v1.0.0 — APK / build de produção)* |

---

## BLOCO 7 — Decisões arquiteturais e de design

*Alimenta: PCP, GDE, ITP*

### Arquitetura

| Campo | Valor |
|---|---|
| **Padrão arquitetural** | *(ex.: MVC, Clean Architecture, BFF…)* |
| **Integrações externas** | *(APIs do cliente, serviços de terceiros — liste com nome e responsável)* |
| **Estratégia de build e entrega** | *(ex.: APK para homologação, AAB para Play Store)* |

### Decisões formais (GDE) — uma linha por decisão relevante

| Contexto / Problema | Alternativas consideradas | Decisão tomada | Justificativa |
|---|---|---|---|
| | | | |
| | | | |

---

## BLOCO 8 — Riscos

*Alimenta: PLA §9, planilha de gestão*

> Probabilidade e Impacto: escala 1–3. Exposição = P × I (resultado 1–9).

| Risco | Prob. (1–3) | Impacto (1–3) | Exposição | Resposta | Status final |
|---|---|---|---|---|---|
| | | | | *(mitigar / evitar / aceitar / transferir)* | *(realizado / não ocorreu)* |
| | | | | | |

---

## BLOCO 9 — Verificação e Validação (V&V / Testes)

*Alimenta: VV, planilha de gestão — aba V&V*

### Ciclos de execução

| Ciclo / Sprint | Módulo | O que foi testado | Defeitos encontrados | Como foi resolvido | Data |
|---|---|---|---|---|---|
| | | | | | |

### Cenários de teste

> Um bloco por cenário. Copie o bloco quantas vezes precisar.

---

**Cenário CT-XX — [nome do cenário]**
- **Módulo:** 
- **Tipo:** *(Happy / Sad)*
- **Dado que:** 
- **Quando:** 
- **Então:** 
- **E:** *(repetir se houver mais de um step "E")*
- **Evidência:** *(ex.: APK testado em dd/mm/aaaa, validado por X)*
- **Resultado:** *(Aprovado / Reprovado)*

---

---

## BLOCO 10 — Reuniões e acompanhamento

*Alimenta: ATAs, RAC, CR*

### Reuniões realizadas

| Tipo | Data | Participantes (nomes/papéis) | Pautas / Decisões principais |
|---|---|---|---|
| Kickoff | | | |
| Levantamento de requisitos | | | |
| Validação Sprint 1 | | | |
| Validação Sprint 2 | | | |
| Validação Sprint 3 | | | |
| Aceite final | | | |
| *(outras)* | | | |

### Change Requests (se houver mudança de escopo)

| Código | Data | Descrição da mudança | Impacto em prazo/escopo | Aprovado por |
|---|---|---|---|---|
| CR-XXXXXX-001 | | | | |

### Acompanhamento de sprints

| Sprint | Planejado (SP) | Realizado (SP) | Desvio | Observação |
|---|---|---|---|---|
| Sprint 1 | | | | |
| Sprint 2 | | | | |
| Sprint 3 | | | | |

---

## BLOCO 11 — GQA (Garantia da Qualidade)

*Alimenta: GQA*

| Marco auditado | Data | Auditor | Itens verificados | Desvios encontrados | % Conformidade |
|---|---|---|---|---|---|
| Abertura | | | | | |
| Aprovação do Plano | | | | | |
| Desenvolvimento | | | | | |
| Homologação/Entrega | | | | | |
| Encerramento | | | | | |

---

## BLOCO 12 — Medição (KPIs)

*Alimenta: MED*

> Preencha o que foi medido. Baseline e meta vêm do PLA-MED-001.

| Código | Indicador | Resultado medido |
|---|---|---|
| M1 | % Entregas no prazo | |
| M2 | Desvio de esforço (%) | |
| M3 | Story points entregues vs. planejados | |
| M4 | Velocity média realizada | |
| M5 | Taxa de defeitos em homologação | |
| M6 | Defeitos escapados para produção | |
| M7 | % Requisitos com rastreabilidade completa | |
| M8 | % Conformidade GQA | |
| M9 | NPS do cliente / satisfação | |

---

## BLOCO 13 — Encerramento

*Alimenta: TAE, LI*

| Campo | Valor |
|---|---|
| **\* Data do aceite formal** | |
| **\* Forma do aceite** | *(ex.: reunião via Teams, e-mail, assinatura de ata)* |
| **\* Quem concedeu o aceite** | |
| **Entregas finais** | *(liste o que foi entregue: build, código, documentação)* |
| **O projeto foi encerrado conforme planejado?** | *(sim / não — se não, explique brevemente)* |

### Lições aprendidas

| Categoria | O que funcionou bem | O que melhorar |
|---|---|---|
| Processo / gestão | | |
| Técnico | | |
| Comunicação com o cliente | | |
| Estimativas | | |
| Outros | | |

---

## Checklist antes de entregar este formulário

- [ ] Todos os campos **\*** preenchidos
- [ ] Pelo menos 1 requisito funcional listado (Bloco 3)
- [ ] Pelo menos 1 cenário de teste descrito (Bloco 9)
- [ ] Datas de início e encerramento confirmadas (Bloco 1)
- [ ] Auditor GQA identificado e diferente da equipe do projeto (Bloco 2)
- [ ] Aceite formal documentado (Bloco 13)

---

## Documentos gerados a partir deste formulário

| Documento | Blocos usados |
|---|---|
| TAP — Termo de Abertura | 1, 2 |
| PLA — Plano de Projeto | 1, 2, 3, 4, 5, 6, 8 |
| ADAP — Registro de Adaptação | 4 |
| REQ — Documento de Requisitos | 3 |
| PCP — Documento de Design | 6, 7 |
| ITP — Estratégia de Integração | 6, 7 |
| VV — Plano de V&V | 9 |
| GCO — Registro de Configuração | 6 |
| GDE — Registro de Decisão | 7 |
| GQA — Registro de GQA | 11 |
| MED — Registro de Medição | 12 |
| RASTR — Matriz de Rastreabilidade | 3, 9 |
| ATAs | 10 |
| CR — Change Request | 10 |
| RAC — Relatório de Acompanhamento | 5, 10 |
| TAE — Termo de Encerramento | 13 |
| LI — Lições Aprendidas | 13 |
| Planilha de Gestão (Excel) | todos |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial |
