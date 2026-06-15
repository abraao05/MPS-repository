# Mapa de Artefatos — MPS-SW Nível C — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | MAPA-ORG-001 — Mapa de Artefatos / Plano de Implantação |
| **Versão** | 0.40 (rascunho) |
| **Data** | 13/06/2026 |
| **Modelo de referência** | MR-MPS-SW:2024 — Nível C |
| **Avaliadora (IA)** | ASR Consultoria e Assessoria em Qualidade Ltda. |
| **Fonte de escopo** | PlanilhaIndicadores_SW_2024__NivelC.xlsx |
| **Nº de projetos na avaliação** | 3 selecionados (PROFARMA/D1000, FTGASMIG, FTFRUKI) · AASP_CNJ documentado como 4º projeto (reserva) |
| **Responsável (ponto focal)** | Abraão Oliveira |

> **Alterações v0.40 (13/06/2026):** revisão geral do inventário (§2.1) a partir da varredura completa do repositório — sincronização de todos os documentos e versões existentes hoje. Novos artefatos de governança incorporados: ATA-GPC-001 (ata de análise crítica), GQA-ORG-001 (auditoria organizacional), REG-GPC-001 (registro de melhorias), REG-GPC-002 (plano de implementação de melhorias), REG-OSW-001 (painel de portfólio) e REG-OSW-002 (comunicação da política). Novos processos de apoio: PRO-CAP-001, PRO-GCO-001, PRO-MED-001 e REG-MED-001 (repositório de medidas). Capacitação ampliada para 47 ativos (incl. MAT-CAP-023 e TPL-CAP-002). Registros de projeto atualizados: PROFARMA (21), FTGASMIG (28 — OS-001 e OS-002 encerradas), FTFRUKI (34), e **AASP_CNJ agora documentado (19 docs)** como 4º projeto de reserva. Escopo da avaliação fixado em **3 projetos** (PROFARMA, GASMIG, FRUKI). AQU confirmado como **Não Aplicável**.

> **Alterações v0.2 (02/06/2026):** resolução das 5 pendências de escopo. OSW 8/9/10 confirmados no escopo (há gestão de portfólio). AQU mantido, mas movido para o fim da fila (candidato a não-aplicável, a confirmar com a ASR). Ferramentas definidas (Jira, Git, Azure DevOps, Azure Test Plans/Xray, Confluence). Papel de GQA confirmado. Ver seção 3 para detalhes.

> **Alterações v0.30 (05/06/2026):** criado TPL-GPC-001 (Template de Registro de Verificação de GQA); PLA-GPC-001 atualizado para v1.3 com inventário completo de ativos (§2). Ambas as lacunas identificadas na análise de cobertura da camada de definição.

> **Alterações v0.33 (05/06/2026):** §2.1 reescrito como inventário completo e organizado por categoria — versão única de referência de todos os documentos existentes.

> **Alterações v0.37 (05/06/2026):** §2.1 Registros de projetos atualizado com inventário completo de FTFRUKI_SuperApp-Forca-de-Vendas (32 docs — Pacote 1 encerrado Set/2025 e Pacote Final 24 encerrado Jan/2026) e PROFARMA_Cadastro-de-Clientes (18 docs — encerrado 29/01/2026, cliente Rede D1000). Pendência 3 e próximos passos atualizados.

> **Alterações v0.36 (05/06/2026):** versões atualizadas no §2.1 conforme ajustes de compliance MPS: PRO-GPC-002 v1.2, EST-GPC-001 v1.3, EST-GPC-002 v1.2, PRO-GDE-001 v1.2, PRO-GPR-001 v1.4 (seções de rastreabilidade com nomenclatura equivalente ASR); TPL-GPR-001 v1.1 (+coluna Exposição); TPL-GPC-001 v1.1 (+% conformidade).

> **Alterações v0.35 (05/06/2026):** inclusão dos 28 materiais de capacitação oficiais (`oficial/01_apoio/cap/`) no inventário §2.1: 12 mini-manuais por processo (GUIA-CAP-001~012), 10 trilhas de treinamento por papel (MAT-CAP-013~022), 5 avaliações de capacitação (AVA-CAP-001~005) e 1 template de registro de sessão (TPL-CAP-001).

> **Alterações v0.34 (05/06/2026):** adição do inventário de registros de projetos ao §2.1 — FTGASMIG (24 documentos, OS-001 encerrada + OS-002 em andamento) confirmado como primeiro projeto da avaliação; estrutura dos demais projetos criada (AASP ×3, PROFARMA). Correção da independência da GQA no FTGASMIG (auditor: COO). Criação do GDE-GASMIG02-001 (registro de decisão arquitetural). Pendência 3 (seleção dos 4 projetos) atualizada.

> **Alterações v0.32 (05/06/2026):** criado GUIA-GCO-001 (Guia de Nomenclaturas Técnicas v1.0) com padrões técnicos de nomenclatura para repositórios, código, BD, recursos Azure, pipelines e Key Vault. PLA-GPC-001 atualizado para v1.4 (adição ao inventário). PLA-GCO-001 v1.1 referencia o novo guia.

> **Alterações v0.31 (05/06/2026):** fechamento de lacunas de definição identificadas no diagnóstico MPS. Grupo 1 (conteúdo): PRO-OSW-001 v1.2 (+RACI e competências §4); PRO-OSW-002 v1.2 (+estrutura do quadro de capacity §4.1); PLA-MED-001 v1.3 (+estrutura do repositório organizacional §4.1); PLA-GCO-001 v1.1 (+lista mínima de ICs por projeto §3.1); PLA-CAP-001 v1.1 (+tabela de fontes e responsáveis §3). Grupo 2 (maturidade): PRO-GDE-001 v1.1 (+limiar orientativo de alto impacto); PRO-AQU-001 v1.1 (+critérios mínimos de qualificação); PRO-ITP-001 v1.1 (+critérios de conclusão da integração); MAPA-CAP-001 v1.1 (+revisão de correspondência pós-primeiro ciclo).

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

## 2.1 Inventário completo de documentos

*Atualizado em 13/06/2026 (v0.40) — gerado a partir da varredura direta do repositório (`oficial/`). Total: 199 documentos `.md` + 6 currículos (`.pdf`), 1 diagrama (`.svg`) e planilhas de gestão de projeto (`.xlsx`).*

### Governança organizacional (`oficial/00_governanca/`)

| Código | Documento | Versão | Atende |
|---|---|---|---|
| ATA-GPC-001 | Reuniao Analise Critica de Processos | 1.0 | GPC 6,7; OSW 3 |
| CONV-ORG-001 | Convencao de Nomenclatura e Versionamento | 1.1 | GCO 1, 4 |
| EST-GPC-001 | Estrategia de Garantia da Qualidade | 1.3 | GPC 3; CP (iv,v,vi) |
| EST-GPC-002 | Estrategia de Gerencia de Riscos | 1.2 | GPC 7; OSW 5 |
| GQA-ORG-001 | Auditoria Organizacional | 1.1 | GPC 3; CP (iv,v) |
| GUIA-GPC-001 | Guia de Adaptacao do Processo Padrao | 2.0 | GPC 2 |
| PLA-GPC-001 | Plano de Gestao e Melhoria de Processos | 1.7 | GPC 1,4,5,8,10,11 |
| POL-ORG-001 | Politica Organizacional de Processos | 1.0 | OSW 1 |
| PRO-GPC-001 | Processo Padrao Organizacional | 2.3 | GPC 2 |
| PRO-GPC-002 | Definicao do Time de Melhoria Continua | 1.2 | GPC 6 |
| PRO-OSW-001 | Governanca Organizacional de Processos | 1.2 | OSW 2,3,4,5,6,7 |
| PRO-OSW-002 | Gestao de Portfolio de Projetos | 1.3 | OSW 8,9,10 |
| REG-GPC-001 | Registro de Melhorias de Processo | 1.0 | GPC 4 |
| REG-GPC-002 | Plano de Implementacao de Melhorias | 1.0 | GPC 5,6,11 |
| REG-OSW-001 | Painel de Portfolio | 1.0 | OSW 8,9,10; MED 6 |
| REG-OSW-002 | Comunicacao da Politica Organizacional | 1.0 | OSW 1,7 |

### Apoio organizacional (`oficial/01_apoio/`)

| Código | Documento | Versão | Atende |
|---|---|---|---|
| GUIA-GCO-001 | Guia de Nomenclaturas Tecnicas | 1.0 | GCO 1,2; GPC 8 |
| PLA-CAP-001 | Plano de Capacitacao | 1.2 | CAP 1-4; OSW 2 |
| PLA-GCO-001 | Plano de Gerencia de Configuracao | 1.1 | GCO 1-5 |
| PLA-MED-001 | Plano de Medicao | 1.3 | MED 1-7; GPC 9; OSW 6 |
| PRO-AQU-001 | Processo de Aquisicao | 1.1 | AQU 1-4 (NA) |
| PRO-CAP-001 | Processo de Capacitacao | 1.0 | CAP 1-4 |
| PRO-GCO-001 | Processo de Gerencia de Configuracao | 1.0 | GCO 1-5 |
| PRO-GDE-001 | Processo de Gerencia de Decisoes | 1.2 | GDE 1-6 |
| PRO-MED-001 | Processo de Medicao | 1.0 | MED 1-7 |
| REG-MED-001 | Repositorio Organizacional de Medicao | 1.0 | MED 3,7; GPC 9 |

### Capacitação (`oficial/01_apoio/cap/`)

| Código | Documento | Versão |
|---|---|---|
| AVA-CAP-001 | Avaliacao Processo Padrao Geral | 1.2 |
| AVA-CAP-002 | Avaliacao GPR | 1.1 |
| AVA-CAP-003 | Avaliacao Tecnico REQ PCP VV | 1.1 |
| AVA-CAP-004 | Avaliacao GCO ITP | 1.1 |
| AVA-CAP-005 | Avaliacao GPC MED CAP | 1.0 |
| GUIA-CAP-001 | MiniManual GPR | 1.3 |
| GUIA-CAP-002 | MiniManual REQ | 1.2 |
| GUIA-CAP-003 | MiniManual PCP | 1.2 |
| GUIA-CAP-004 | MiniManual VV | 1.2 |
| GUIA-CAP-005 | MiniManual GCO | 1.2 |
| GUIA-CAP-006 | MiniManual ITP | 1.1 |
| GUIA-CAP-007 | MiniManual GDE | 1.1 |
| GUIA-CAP-008 | MiniManual MED | 1.1 |
| GUIA-CAP-009 | MiniManual GPC | 1.1 |
| GUIA-CAP-010 | MiniManual OSW | 1.0 |
| GUIA-CAP-011 | MiniManual CAP | 1.0 |
| GUIA-CAP-012 | MiniManual AQU | 1.0 |
| MAT-CAP-013 | Trilha COO Portfolio | 1.1 |
| MAT-CAP-014 | Trilha Time Melhoria SEPG | 1.1 |
| MAT-CAP-015 | Trilha RH Pessoas | 1.0 |
| MAT-CAP-016 | Trilha Tech Lead Arquiteto | 1.2 |
| MAT-CAP-017 | Trilha PO PM | 1.2 |
| MAT-CAP-018 | Trilha Devs | 1.2 |
| MAT-CAP-019 | Trilha DevOps | 1.1 |
| MAT-CAP-020 | Trilha QA | 1.2 |
| MAT-CAP-021 | Trilha GCO Baseline | 1.1 |
| MAT-CAP-022 | Trilha Responsavel Medicao | 1.1 |
| MAT-CAP-023 | Trilha Tecnica Onboarding | 1.0 |
| REG-CAP-001B | Sessao Reforco Jan2025 | 1.0 |
| REG-CAP-001 | Sessao Treinamento Dez2024 | 1.0 |
| REG-CAP-002B | Sessao Reforco Set2025 | 1.0 |
| REG-CAP-002 | Sessao Treinamento Mar2025 | 1.0 |
| REG-CAP-003 | Sessao Treinamento Ago2025 | 1.0 |
| REG-CAP-004 | Sessao Treinamento Jan2026 | 1.0 |
| REG-CAP-005 | Sessao Treinamento Mai2026 | 1.0 |
| REG-CAP-006 | Sessao Gestao Out2025 | 1.0 |
| REG-CAP-007 | Sessao Tecnico Jan2026 | 1.0 |
| REG-CAP-008 | Sessao Tecnico Fev2026 | 1.0 |
| REG-CAP-009 | Reciclagem Mar2026 | 1.0 |
| REG-CAP-010 | Onboarding Tecnico Jan2026 | 1.0 |
| REG-CAP-011 | Workshop Azure APIM Mar2026 | 1.0 |
| REG-CAP-012 | Workshop Automacao Testes Fev2026 | 1.0 |
| REG-CAP-013 | Consultoria Desenho Processos Jun2025 | 1.0 |
| REG-CAP-CV-001 | Indice de Curriculos | 1.0 |
| REL-CAP-001 | Relatorio de Eficacia 2025 | 1.0 |
| TPL-CAP-001 | Registro de Sessao de Treinamento | 1.0 |
| TPL-CAP-002 | Relatorio de Eficacia de Treinamento | 1.0 |

*Subtotal capacitação: 47 documentos (5 avaliações, 12 mini-manuais, 11 trilhas/materiais, 15 registros de sessão, índice de currículos, relatório de eficácia, 2 templates).*

### Processos de projeto (`oficial/02_projeto/`)

| Código | Documento | Versão | Atende |
|---|---|---|---|
| GUIA-GPR-001 | Roteiro de Kickoff | 1.0 | apoio GPR |
| PRO-GPR-001 | Processo de Gerencia de Projetos | 1.4 | GPR 1-20 |
| PRO-ITP-001 | Processo de Integracao do Produto | 1.1 | ITP 1-6 |
| PRO-PCP-001 | Processo de Projeto e Construcao do Produto | 1.1 | PCP 1-3 |
| PRO-REQ-001 | Processo de Engenharia de Requisitos | 1.1 | REQ 1-7 |
| PRO-VV-001 | Processo de Verificacao e Validacao | 1.2 | VV 1-5 |

### Templates (`oficial/03_templates/`)

| Código | Documento | Versão |
|---|---|---|
| EXEMPLO-GPR-005 | Status Report Exemplo Preenchido | — |
| TPL-GDE-001 | Template Registro de Analise de Decisao | — |
| TPL-GPC-001 | Template Registro de Verificacao de GQA | — |
| TPL-GPR-001 | Template Plano de Projeto | [versão] |
| TPL-GPR-002 | Template Termo de Abertura | [versão] |
| TPL-GPR-003 | Template Registro de Adaptacao | [versão] |
| TPL-GPR-004 | Template Termo de Encerramento | [versão] |
| TPL-GPR-005 | Template Relatorio de Acompanhamento | — |
| TPL-GPR-006 | Template Change Request | — |
| TPL-ITP-001 | Template Estrategia de Integracao | [versão] |
| TPL-ORG-001 | Template Ata de Reuniao | — |
| TPL-PCP-001 | Template Documento de Design | [versão] |
| TPL-REQ-001 | Template Documento de Requisitos | [versão] |
| TPL-REQ-002 | Template Matriz de Rastreabilidade | [versão] |
| TPL-VV-001 | Template Plano de Verificacao e Validacao | [versão] |
| TPL-VV-002 | Template Registro de Revisao por Pares | — |

### Capacidade (`oficial/05_capacidade/`)

| Código | Documento | Versão | Atende |
|---|---|---|---|
| MAPA-CAP-001 | Mapa de Capacidade dos Processos | 1.1 | CP-E/D/C |
| MAPA-ORG-001 | Matriz de Papeis e Responsabilidades | 1.0 | OSW 4; CP (iii) |

### Registros de projeto — PROFARMA (`04_registros/PROFARMA_Cadastro-de-Clientes/`)

| Código | Documento | Versão |
|---|---|---|
| ADAP-PROFARMA01-001 | Registro de Adaptacao | 1.1 |
| ATA-PROFARMA01-001 | Ata de Kickoff | 1.0 |
| ATA-PROFARMA01-002 | Ata de Aceite Final | 1.0 |
| CR-PROFARMA01-001 | Registro de Change Requests | 1.0 |
| CTQ-PROFARMA01-001 | Cenarios de Teste Homologacao | 1.0 |
| GCO-PROFARMA01-001 | Registro de Gerencia de Configuracao | 1.0 |
| GDE-PROFARMA01-001 | Registro de Analise de Decisao | 1.0 |
| GQA-PROFARMA01-001 | Registro de GQA | 1.1 |
| ITP-PROFARMA01-001 | Estrategia de Integracao | 1.0 |
| LI-PROFARMA01-001 | Licoes Aprendidas | 1.2 |
| MED-PROFARMA01-001 | Registro de Medicao | 1.2 |
| PCP-PROFARMA01-001 | Documento de Design | 1.5 |
| PLA-PROFARMA01-001 | Plano de Projeto | 1.3 |
| RAC-PROFARMA01-001 | Relatorio de Acompanhamento | 1.0 |
| RASTR-PROFARMA01-001 | Matriz de Rastreabilidade | 1.1 |
| REL-VV-PROFARMA01-001 | Relatorio de Execucao de Testes | 1.0 |
| REQ-PROFARMA01-001 | Documento de Requisitos | 1.4 |
| REV-PROFARMA01-001 | Registro de Revisao Tecnica | 1.0 |
| TAE-PROFARMA01-001 | Termo de Encerramento | 1.0 |
| TAP-PROFARMA01-001 | Termo de Abertura | 1.0 |
| VV-PROFARMA01-001 | Plano de VV | 1.2 |

### Registros de projeto — GASMIG (`04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica/`)

| Código | Documento | Versão |
|---|---|---|
| ADAP-GASMIG02-001 | Registro de Adaptacao | 1.4 |
| ADAP-GASMIG02-002 | Registro de Adaptacao OS002 | 1.2 |
| ATA-GASMIG02-001 | Ata de Kickoff | — |
| ATA-GASMIG02-002 | Ata de Aceite OS001 | — |
| ATA-GASMIG02-003 | Apresentacao Entrega OS002 | 1.0 |
| CAP-GASMIG02-001 | Registro de Capacitacao da Equipe | 1.1 |
| GCO-GASMIG02-001 | Gerencia de Configuracao | 1.0 |
| GDE-GASMIG02-001 | Registro de Analise de Decisao | 1.1 |
| GQA-GASMIG02-001 | Registro de GQA | 1.5 |
| ITP-GASMIG02-002 | Estrategia de Integracao OS002 | 1.0 |
| LI-GASMIG02-001 | Licoes Aprendidas | 1.2 |
| MED-GASMIG02-001 | Registro de Medicao | 1.2 |
| PCP-GASMIG02-001 | Documento de Design | 1.1 |
| PCP-GASMIG02-002 | Documento de Design OS002 | 1.0 |
| PLA-GASMIG02-001 | Plano de Projeto | 1.3 |
| PLA-GASMIG02-002 | Plano de Projeto OS002 | 1.3 |
| RAC-GASMIG02-001 | Relatorio de Acompanhamento | 1.1 |
| RASTR-GASMIG02-001 | Matriz de Rastreabilidade | 1.0 |
| RASTR-GASMIG02-002 | Matriz de Rastreabilidade OS002 | 1.0 |
| REQ-GASMIG02-001 | Documento de Requisitos | 1.0 |
| REQ-GASMIG02-002 | Documento de Requisitos OS002 | 1.0 |
| REV-GASMIG02-001 | Registro de Verificacao Tecnica | 1.0 |
| TAE-GASMIG02-001 | Termo de Encerramento OS001 | 1.0 |
| TAE-GASMIG02-002 | Termo de Encerramento OS002 | 1.0 |
| TAP-GASMIG02-001 | Termo de Abertura | 1.0 |
| TAP-GASMIG02-002 | Termo de Abertura OS002 | 1.0 |
| VV-GASMIG02-001 | Plano de VV | 1.2 |
| VV-GASMIG02-002 | Plano de VV OS002 | 1.1 |

### Registros de projeto — FRUKI (`04_registros/FTFRUKI_SuperApp-Forca-de-Vendas/`)

| Código | Documento | Versão |
|---|---|---|
| ADAP-FRUKI01-001 | Registro de Adaptacao | 1.2 |
| ADAP-FRUKI01-002 | Registro de Adaptacao PacoteFinal24 | 1.2 |
| ATA-FRUKI01-001 | Ata de Kickoff | — |
| ATA-FRUKI01-002 | Ata Levantamento Metas | — |
| ATA-FRUKI01-003 | Ata de Aceite Final | — |
| ATA-FRUKI01-004 | Ata Validacao Sprint1 NaoAlocados | 1.0 |
| ATA-FRUKI01-005 | Ata Validacao Sprint2 RegraDeOuro | 1.0 |
| ATA-FRUKI01-006 | Ata Validacao Sprint3 PDV | 1.0 |
| ATA-FRUKI01-007 | Ata Piloto Pacote1 | 1.0 |
| ATA-FRUKI01-008 | Ata Kickoff PacoteFinal24 | 1.0 |
| CR-FRUKI01-001 | Solicitacao de Mudanca RegraDeOuro | 1.0 |
| GCO-FRUKI01-001 | Registro de Configuracao | 1.4 |
| GDE-FRUKI01-001 | Registro de Decisao | — |
| GQA-FRUKI01-001 | Registro de GQA | 1.2 |
| ITP-FRUKI01-001 | Estrategia de Integracao | 1.0 |
| ITP-FRUKI01-002 | Estrategia de Integracao PacoteFinal24 | 1.0 |
| LI-FRUKI01-001 | Licoes Aprendidas | 1.0 |
| MED-FRUKI01-001 | Registro de Medicao | 1.0 |
| PCP-FRUKI01-001 | Documento de Design | 1.0 |
| PCP-FRUKI01-002 | Documento de Design PacoteFinal24 | 1.0 |
| PLA-FRUKI01-001 | Plano de Projeto | 1.1 |
| PLA-FRUKI01-002 | Plano de Projeto PacoteFinal24 | 1.0 |
| RAC-FRUKI01-001 | Relatorio de Acompanhamento | — |
| RAC-FRUKI01-002 | Relatorio de Acompanhamento Pacote1 | — |
| RASTR-FRUKI01-001 | Matriz de Rastreabilidade | 1.0 |
| RASTR-FRUKI01-002 | Matriz de Rastreabilidade PacoteFinal24 | 1.0 |
| REQ-FRUKI01-001 | Documento de Requisitos | 1.1 |
| REQ-FRUKI01-002 | Documento de Requisitos PacoteFinal24 | 1.0 |
| TAE-FRUKI01-001 | Termo de Encerramento | 1.0 |
| TAE-FRUKI01-002 | Termo de Encerramento PacoteFinal24 | 1.1 |
| TAP-FRUKI01-001 | Termo de Abertura | 1.1 |
| TAP-FRUKI01-002 | Termo de Abertura PacoteFinal24 | 1.1 |
| VV-FRUKI01-001 | Plano VeV | 1.0 |
| VV-FRUKI01-002 | Plano VeV PacoteFinal24 | 1.0 |

### Registros de projeto — AASP_CNJ (`04_registros/AASP_CNJ/`)

| Código | Documento | Versão |
|---|---|---|
| 00 | INDICE AASPCNJ01_Mapa de Registros | 1.5 |
| ADAP-AASPCNJ01-001 | Registro de Adaptacao | 1.0 |
| ATA-AASPCNJ01-001 | Ata Alinhamento Fluxo CNJ | — |
| CAP-AASPCNJ01-001 | Registro de Capacitacao da Equipe | 1.0 |
| CR-AASPCNJ01-001 | Change Request | — |
| GCO-AASPCNJ01-001 | Registro de Configuracao | 1.0 |
| GDE-AASPCNJ01-001 | Registro de Analise de Decisao | — |
| GQA-AASPCNJ01-001 | Registro de GQA | — |
| ITP-AASPCNJ01-001 | Estrategia de Integracao | 1.0 |
| MED-AASPCNJ01-001 | Registro de Medicao | 1.0 |
| PCP-AASPCNJ01-001 | Documento de Design | 1.0 |
| PLA-AASPCNJ01-001 | Plano de Projeto | 1.0 |
| RAC-AASPCNJ01-001 | Relatorio de Acompanhamento | — |
| RASTR-AASPCNJ01-001 | Matriz de Rastreabilidade | 1.0 |
| REL-VV-AASPCNJ01-001 | Relatorio de Execucao de Testes | 1.0 |
| REQ-AASPCNJ01-001 | Documento de Requisitos | 1.0 |
| REV-AASPCNJ01-001 | Registro de Revisao por Pares | — |
| TAP-AASPCNJ01-001 | Termo de Abertura | 1.0 |
| VV-AASPCNJ01-001 | Plano de VV | 1.0 |

### Internos (`_interno/`) — não auditados pela ASR

| Código | Documento | Observação |
|---|---|---|
| MAPA-ORG-001 | Mapa de Artefatos / Plano de Implantação (este doc) | Rascunho de gestão (v0.40) |
| GUIA-ORG-001 | Guia de Estrutura do Confluence | Apoio à navegação no Confluence |
| PlanilhaIndicadores...PREENCHIDA | Planilha de evidências para a ASR | Submissão da avaliação (links Drive) |

### Lacunas de upload (existem no repositório, ainda sem link no Drive)

| Código | Pasta | Observação |
|---|---|---|
| REG-MED-001 | 01_apoio | Repositório de medidas — subir `.docx` ao Drive (reforça MED 3/7 e GPC 9) |
| EXEMPLO-GPR-005 | 03_templates | Exemplo preenchido de status report — apoio, não é evidência obrigatória |
| ATA-FRUKI01-008 | 04_registros/FTFRUKI | Ata de kickoff do Pacote Final 24 — subir ao Drive (reforça GPR 13 do FRUKI) |
| 00_INDICE-AASPCNJ01 | 04_registros/AASP_CNJ | Índice do projeto AASP (reserva) |

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
| PCP 1+ | Design desenvolvido com solução baseada em critérios + rastreável | **Documento de Design / Arquitetura** | TPL + PROJ | Template→Registros | ✅ |
| PCP 2 | Design avaliado e problemas tratados | Registro de revisão de design | PROJ | Registros | ✅ |
| PCP 3+ | Produto implementado conforme design + informações mantidas | Código/build + documentação técnica | PROJ | Git/Azure DevOps | ✅ |

### ITP — Integração do Produto
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| ITP 1+ | Estratégia de integração + interfaces | **Estratégia/Plano de Integração** | TPL + PROJ | Template→Registros | ✅ |
| ITP 2 | Ambiente de integração estabelecido | Definição do ambiente de integração | PROJ | Azure DevOps | ✅ |
| ITP 3+ | Componentes avaliados antes de integrar | Registro de prontidão de componente | PROJ | Registros | ✅ |
| ITP 4 | Componentes integrados conforme estratégia | Registro de integração | PROJ | Azure DevOps | ✅ |
| ITP 5+ | Produto integrado testado | Registro de testes de integração | PROJ | Registros | ✅ |
| ITP 6 | Produto e material de apoio entregues | Registro de entrega + material de apoio | PROJ | Registros | ✅ |

### VV — Verificação e Validação
| Resultado | Exigência (resumo) | Artefato de evidência | Tipo | Local | Status |
|---|---|---|---|---|---|
| VV 1 | Produtos a verificar/validar selecionados (testes + revisão por pares) | **Plano de V&V** | TPL + PROJ | Template→Registros | ✅ |
| VV 2 | Procedimentos e material p/ revisão por pares | **Template de Revisão por Pares** | TPL + PROJ | Template→Registros | ✅ |
| VV 3+ | Métodos, critérios e ambientes de V&V | (no Plano de V&V) | PROJ | Registros | ✅ |
| VV 4 | Atividades de V&V realizadas + problemas tratados | Registros de teste + revisão por pares | PROJ | Registros | ✅ |
| VV 5 | Resultados analisados, registrados e comunicados | Relatório de V&V | PROJ | Registros | ✅ |

> **V&V — nota de ferramenta (v0.2):** testes registrados em **Azure Test Plans + Jira/Xray**. Fluxo aceito: casos de teste começam em planilha e depois são importados para a ferramenta — documentar isso explicitamente no Plano de V&V para o avaliador entender que é intencional. Revisão por pares pode ser evidenciada via pull request (Git/Azure) + registro de revisão.

---

## FASE 4 — CAPACIDADE (TRANSVERSAL A TODOS OS 13 PROCESSOS)

> **Atenção:** os atributos CP-E/D/C **não são um processo separado**. São exigências de *institucionalização* que o avaliador verifica para **cada um** dos 13 processos. É o que diferencia o Nível C de níveis iniciais.

| Atributo (CP-E/D/C) | O que exige | Como evidenciamos (transversal) | Status |
|---|---|---|---|
| (i) Processo produz resultados definidos | O processo realmente funciona | Registros de uso em cada processo | 🟨 |
| (ii) Processo-padrão + diretrizes de adaptação usados | Planejar/executar/monitorar com papéis, infra, produtos | Tailoring (GPR 2+) + processo-padrão (GPC 2+) | 🟨 |
| (iii) Pessoas preparadas para o processo | Capacitação adequada | Plano de Capacitação (CAP) + registros | 🟨 |
| (iv) Verificação objetiva de que o processo é seguido | Auditoria de aderência ao processo | **Registros de Garantia da Qualidade (GQA)** | 🟨 |
| (v) Produtos de trabalho avaliados objetivamente | Revisão de produtos vs. padrão | Registros de GQA de produtos | 🟨 |
| (vi) Oportunidades de melhoria identificadas | Durante a garantia da qualidade | Alimenta GPC 4 (oport. de melhoria) | 🟨 |
| (vii) Informações disponibilizadas à organização | Compartilhar ativos/medidas | Biblioteca de processos + repositório de medidas | 🟨 |

---

## 3. Pendências de escopo — status (resolvidas em 02/06/2026)

| # | Pendência | Status | Decisão |
|---|---|---|---|
| 1 | **Portfólio (OSW 8/9/10)** | ✅ Resolvido | **No escopo.** TIMEWARE gerencia portfólio: recursos compartilhados (tech lead, arquiteto, PO) + gestão de capacity. Há quadro de capacity informal a formalizar. |
| 2 | **Aquisição (AQU)** | ✅ Resolvido (com ação) | **Último a produzir / candidato a não-aplicável.** Nenhum dos 4 projetos tem aquisição. Confirmar não-aplicabilidade com o avaliador líder da ASR. |
| 3 | **Os 4 projetos** | 🟨 Em andamento | 3 projetos documentados: FTGASMIG (22 docs — OS-001 encerrada, OS-002 em andamento), FTFRUKI (32 docs — Pacote 1 encerrado Set/2025 + Pacote Final 24 encerrado Jan/2026), PROFARMA/Rede D1000 (18 docs — encerrado Jan/2026). AASP (3 projetos) ainda a documentar. |
| 4 | **Ferramentas** | ✅ Resolvido | Jira (gestão de projeto, riscos, ações, repositório de medidas) · Git + Azure DevOps (código, baselines, integração/CI-CD) · Azure Test Plans + Jira/Xray (testes) · Confluence (definições/registros). |
| 5 | **Garantia da Qualidade (GQA)** | ✅ Resolvido | Pessoa/área de GQA existe na TIMEWARE. Detalhar nome/papel ao produzir a Estratégia de GQA (GPC 3). |

**Itens que seguem como ação aberta (não bloqueiam a produção):**
- Confirmar não-aplicabilidade do AQU com a ASR (ponto 2).
- Definir os 4 projetos antes da Fase 3 (ponto 3).
- MED: definir camada de consolidação de indicadores (dashboard Jira ou planilha organizacional).

---

## 4. Próximos passos sugeridos

1. ✅ **Fase 1 — Governança:** todos os documentos prontos (OSW, GPC)
2. ✅ **Fase 2 — Apoio organizacional:** todos os documentos prontos (MED, CAP, GDE, GCO, AQU)
3. ✅ **Fase 3 — Processos de projeto (camada organizacional):** definições e templates prontos
4. 🟨 **Fase 3 — Evidências de projeto:** 3 projetos documentados (FTGASMIG, FTFRUKI, PROFARMA/D1000); faltam 3 projetos AASP
5. ⬜ **Documentar projetos AASP** (Andamento-Processuais, Automacao-Governanca, CNJ) para fechar os 4+ projetos exigidos pela avaliação
6. ⬜ **Confirmar AQU** com o avaliador líder da ASR (não-aplicabilidade ou versão enxuta)
7. ⬜ **Planilha-mestre de evidências** para entrega à ASR antes da avaliação inicial

> **Observação de auditoria:** este mapa também serve de evidência para GPC 1 (identificação de ativos de processo) e como rastreabilidade entre resultados esperados e artefatos — algo que a ASR vai querer ver logo no início.
