# Mapa de Artefatos — MPS-SW Nível C — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | MAPA-ORG-001 — Mapa de Artefatos / Plano de Implantação |
| **Versão** | 0.38 (rascunho) |
| **Data** | 05/06/2026 |
| **Modelo de referência** | MR-MPS-SW:2024 — Nível C |
| **Avaliadora (IA)** | ASR Consultoria e Assessoria em Qualidade Ltda. |
| **Fonte de escopo** | PlanilhaIndicadores_SW_2024__NivelC.xlsx |
| **Nº de projetos na avaliação** | 4+ (4 documentados: FTGASMIG, FTFRUKI, PROFARMA/D1000, MILHASFACIL/Hub de Milhas · AASP a documentar) |
| **Responsável (ponto focal)** | Abraão Oliveira |

> **Alterações v0.2 (02/06/2026):** resolução das 5 pendências de escopo. OSW 8/9/10 confirmados no escopo (há gestão de portfólio). AQU mantido, mas movido para o fim da fila (candidato a não-aplicável, a confirmar com a ASR). Ferramentas definidas (Jira, Git, Azure DevOps, Azure Test Plans/Xray, Confluence). Papel de GQA confirmado. Ver seção 3 para detalhes.

> **Alterações v0.30 (05/06/2026):** criado TPL-GPC-001 (Template de Registro de Verificação de GQA); PLA-GPC-001 atualizado para v1.3 com inventário completo de ativos (§2). Ambas as lacunas identificadas na análise de cobertura da camada de definição.

> **Alterações v0.33 (05/06/2026):** §2.1 reescrito como inventário completo e organizado por categoria — versão única de referência de todos os documentos existentes.

> **Alterações v0.38 (11/06/2026):** §2.1 Registros de projetos atualizado com inventário completo de MILHASFACIL_Plataforma-Milhas3 (17 docs — projeto Milhas3, cliente Hub de Milhas, encerrado 16/11/2025). Quarto projeto real documentado; mínimo de 4 projetos da avaliação atingido. Pendência 3 e próximos passos atualizados.
>
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

*Atualizado em 05/06/2026 — versão de referência de todos os ativos de processo produzidos.*

### Governança organizacional (`oficial/00_governanca/`)

| Código | Documento | Versão | Atende |
|---|---|---|---|
| POL-ORG-001 | Política Organizacional de Processos | 1.0 | OSW 1 |
| CONV-ORG-001 | Convenção de Nomenclatura e Versionamento | 1.1 | GCO 1, 4 |
| PRO-GPC-001 | Processo-Padrão Organizacional | 2.2 | GPC 2 |
| GUIA-GPC-001 | Guia de Adaptação do Processo-Padrão | 1.2 | GPC 2 |
| PRO-GPC-002 | Definição do Time de Melhoria Contínua | 1.2 | GPC 6 |
| EST-GPC-001 | Estratégia de Garantia da Qualidade | 1.3 | GPC 3; CP (iv, v, vi) |
| EST-GPC-002 | Estratégia de Gerência de Riscos e Oportunidades | 1.2 | GPC 7 |
| PLA-GPC-001 | Plano de Gestão e Melhoria de Processos | 1.4 | GPC 1, 4, 5, 8, 10, 11 |
| PRO-OSW-001 | Governança Organizacional de Processos | 1.2 | OSW 2, 3, 4, 5, 6, 7 |
| PRO-OSW-002 | Gestão de Portfólio de Projetos | 1.2 | OSW 8, 9, 10 |

### Apoio organizacional (`oficial/01_apoio/`)

| Código | Documento | Versão | Atende |
|---|---|---|---|
| PLA-MED-001 | Plano de Medição | 1.3 | MED 1–7; GPC 9; OSW 6 |
| PLA-GCO-001 | Plano de Gerência de Configuração | 1.1 | GCO 1–5 |
| GUIA-GCO-001 | Guia de Nomenclaturas Técnicas | 1.0 | GCO 1, 2; GPC 8 |
| PRO-GDE-001 | Processo de Gerência de Decisões | 1.2 | GDE 1–6 |
| PLA-CAP-001 | Plano de Capacitação | 1.1 | CAP 1–4 |
| GUIA-CAP-001 | Mini-manual — Gerência de Projetos | — | CAP 2 (material de apoio) |
| GUIA-CAP-002 | Mini-manual — Especificação de Requisitos | — | CAP 2 |
| GUIA-CAP-003 | Mini-manual — Projeto e Construção do Produto | — | CAP 2 |
| GUIA-CAP-004 | Mini-manual — Verificação e Validação | — | CAP 2 |
| GUIA-CAP-005 | Mini-manual — Gerência de Configuração | — | CAP 2 |
| GUIA-CAP-006 | Mini-manual — Integração do Produto | — | CAP 2 |
| GUIA-CAP-007 | Mini-manual — Gerência de Decisões | — | CAP 2 |
| GUIA-CAP-008 | Mini-manual — Medição | — | CAP 2 |
| GUIA-CAP-009 | Mini-manual — Gerência de Processos | — | CAP 2 |
| GUIA-CAP-010 | Mini-manual — Gerência Organizacional de Software | — | CAP 2 |
| GUIA-CAP-011 | Mini-manual — Capacitação | — | CAP 2 |
| GUIA-CAP-012 | Mini-manual — Aquisição | — | CAP 2 |
| MAT-CAP-013 | Trilha COO / Portfólio | 1.0 | CAP 1–2 |
| MAT-CAP-014 | Trilha Time de Melhoria Contínua / SEPG | 1.0 | CAP 1–2 |
| MAT-CAP-015 | Trilha RH / Pessoas | 1.0 | CAP 1–2 |
| MAT-CAP-016 | Trilha Tech Lead / Arquiteto | 1.0 | CAP 1–2 |
| MAT-CAP-017 | Trilha PO / PM | 1.0 | CAP 1–2 |
| MAT-CAP-018 | Trilha Desenvolvedores | 1.0 | CAP 1–2 |
| MAT-CAP-019 | Trilha DevOps | 1.0 | CAP 1–2 |
| MAT-CAP-020 | Trilha QA | 1.0 | CAP 1–2 |
| MAT-CAP-021 | Trilha GCO Baseline / Auditoria de Configuração | 1.0 | CAP 1–2 |
| MAT-CAP-022 | Trilha Responsável de Medição | 1.0 | CAP 1–2 |
| AVA-CAP-001 | Avaliação — Processo-Padrão Geral | 1.0 | CAP 3 |
| AVA-CAP-002 | Avaliação — Trilha GP / PO | 1.0 | CAP 3 |
| AVA-CAP-003 | Avaliação — Trilha Técnica (Tech Lead / Devs / QA) | 1.0 | CAP 3 |
| AVA-CAP-004 | Avaliação — Trilha GCO / ITP | 1.0 | CAP 3 |
| AVA-CAP-005 | Avaliação — Trilha GPC / MED / CAP | 1.0 | CAP 3 |
| TPL-CAP-001 | Template de Registro de Sessão de Treinamento | 1.0 | CAP 2 (template) |
| PRO-AQU-001 | Processo de Aquisição | 1.1 | AQU 1–4 *(aplicabilidade a confirmar com ASR)* |

### Processos de projeto (`oficial/02_projeto/`)

| Código | Documento | Versão | Atende |
|---|---|---|---|
| PRO-GPR-001 | Processo de Gerência de Projetos | 1.4 | GPR 1–20 |
| GUIA-GPR-001 | Roteiro de Apresentação de Kickoff | 1.0 | apoio ao GPR |
| PRO-REQ-001 | Processo de Engenharia de Requisitos | 1.1 | REQ 1–7 |
| PRO-PCP-001 | Processo de Projeto e Construção do Produto | 1.1 | PCP 1–3 |
| PRO-ITP-001 | Processo de Integração do Produto | 1.1 | ITP 1–6 |
| PRO-VV-001 | Processo de Verificação e Validação | 1.2 | VV 1–5 |

### Templates (`oficial/03_templates/`)

| Código | Documento | Atende |
|---|---|---|
| TPL-GPR-001 | Template de Plano de Projeto | GPR 12 |
| TPL-GPR-002 | Template de Termo de Abertura do Projeto | GPR 1 |
| TPL-GPR-003 | Template de Registro de Adaptação do Processo | GPR 2 / CP-C |
| TPL-GPR-004 | Template de Termo de Encerramento e Aceite | GPR |
| TPL-GPR-005 | Template de Relatório de Acompanhamento | GPR 14 |
| TPL-GPR-006 | Template de Change Request | GPR / GCO |
| TPL-REQ-001 | Template de Documento de Requisitos | REQ 1–2 |
| TPL-REQ-002 | Template de Matriz de Rastreabilidade | REQ 4 |
| TPL-PCP-001 | Template de Documento de Design | PCP 1–2 |
| TPL-ITP-001 | Template de Estratégia de Integração | ITP 1 |
| TPL-VV-001 | Template de Plano de V&V | VV 1, 3 |
| TPL-VV-002 | Template de Registro de Revisão por Pares | VV 2 |
| TPL-GPC-001 | Template de Registro de Verificação de GQA | GPC 3 / CP (iv, v) |
| TPL-GDE-001 | Template de Registro de Análise de Decisão (RAD) | GDE 6 |
| TPL-ORG-001 | Template de Ata de Reunião | multiuso |

### Registros de projetos (`oficial/04_registros/`)

**FTGASMIG — Governança de APIs** · Cliente: GASMIG · GP: Abraão Oliveira

*OS-001 encerrada (aceite 26/05/2026) · OS-002 em andamento (encerramento previsto 10/06/2026)*

| Código | Documento | Versão | Evidência |
|---|---|---|---|
| TAP-GASMIG02-001 | Termo de Abertura — OS-001 | 1.0 | GPR 1, 13 |
| PLA-GASMIG02-001 | Plano de Projeto — OS-001 | 1.1 | GPR 3–12 |
| REQ-GASMIG02-001 | Documento de Requisitos — OS-001 | 1.0 | REQ 1–7 |
| PCP-GASMIG02-001 | Documento de Design — OS-001 | 1.1 | PCP 1–3 |
| VV-GASMIG02-001 | Plano de V&V — OS-001 | 1.0 | VV 1–5 |
| RASTR-GASMIG02-001 | Matriz de Rastreabilidade — OS-001 | 1.0 | REQ 4 |
| ADAP-GASMIG02-001 | Registro de Adaptação — OS-001 | 1.2 | GPR 2 / CP-C |
| GDE-GASMIG02-001 | Registro de Análise de Decisão | 1.0 | GDE 2–6 |
| REV-GASMIG02-001 | Registro de Verificação Técnica — OS-001 | 1.0 | PCP 2 / VV 4 |
| ATA-GASMIG02-001 | Ata de Kickoff | 1.0 | GPR 13 |
| ATA-GASMIG02-002 | Ata de Aceite — OS-001 | 1.0 | GPR (aceite) |
| TAE-GASMIG02-001 | Termo de Encerramento — OS-001 | 1.0 | GPR (encerramento) |
| LI-GASMIG02-001 | Lições Aprendidas | 1.0 | GPR 20 / GPC 4 |
| CAP-GASMIG02-001 | Registro de Capacitação da Equipe | 1.0 | CAP 2 |
| GQA-GASMIG02-001 | Registro de GQA (OS-001 + OS-002 parcial) | 1.2 | GPC 3 / CP (iv, v) |
| TAP-GASMIG02-002 | Termo de Abertura — OS-002 | 1.0 | GPR 1, 13 |
| PLA-GASMIG02-002 | Plano de Projeto — OS-002 | 1.1 | GPR 3–12 |
| REQ-GASMIG02-002 | Documento de Requisitos — OS-002 | 1.0 | REQ 1–7 |
| PCP-GASMIG02-002 | Documento de Design — OS-002 | 1.0 | PCP 1–3 |
| VV-GASMIG02-002 | Plano de V&V — OS-002 | 1.0 | VV 1–5 |
| RASTR-GASMIG02-002 | Matriz de Rastreabilidade — OS-002 | 1.0 | REQ 4 |
| ADAP-GASMIG02-002 | Registro de Adaptação — OS-002 | 1.0 | GPR 2 / CP-C |

*3 artefatos pendentes (encerramento OS-002): REV-GASMIG02-002, ATA-GASMIG02-003, TAE-GASMIG02-002 — previstos para 09–10/06/2026.*

**FTFRUKI — SuperApp Fruki · Força de Vendas** · Cliente: Fruki Bebidas S.A. · GP: Abraão Oliveira

*Pacote 1 (Módulo Metas e RV) encerrado Set/2025 · Pacote Final 24 encerrado 15/01/2026 · 32 documentos*

*Pacote 1 — Módulo Metas e Remuneração Variável*

| Código | Documento | Versão | Evidência |
|---|---|---|---|
| TAP-FRUKI01-001 | Termo de Abertura — Pacote 1 | 1.1 | GPR 1, 13 |
| PLA-FRUKI01-001 | Plano de Projeto — Pacote 1 | 1.1 | GPR 3–12 |
| REQ-FRUKI01-001 | Documento de Requisitos — Pacote 1 | 1.1 | REQ 1–7 |
| PCP-FRUKI01-001 | Documento de Design — Pacote 1 | 1.0 | PCP 1–3 |
| VV-FRUKI01-001 | Plano de V&V — Pacote 1 | 1.0 | VV 1–5 |
| ITP-FRUKI01-001 | Estratégia de Integração — Pacote 1 | 1.0 | ITP 1 |
| RASTR-FRUKI01-001 | Matriz de Rastreabilidade — Pacote 1 | 1.0 | REQ 4 |
| ADAP-FRUKI01-001 | Registro de Adaptação — Pacote 1 | 1.1 | GPR 2 / CP-C |
| ATA-FRUKI01-001 | Ata de Kickoff | 1.0 | GPR 13 |
| ATA-FRUKI01-002 | Ata de Levantamento de Metas | 1.0 | REQ 1 |
| ATA-FRUKI01-007 | Ata de Piloto — Módulo Metas e RV | 1.0 | VV 5 |
| TAE-FRUKI01-001 | Termo de Encerramento — Pacote 1 | 1.0 | GPR (encerramento) |

*Pacote Final 24*

| Código | Documento | Versão | Evidência |
|---|---|---|---|
| TAP-FRUKI01-002 | Termo de Abertura — Pacote Final 24 | 1.1 | GPR 1, 13 |
| PLA-FRUKI01-002 | Plano de Projeto — Pacote Final 24 | 1.0 | GPR 3–12 |
| REQ-FRUKI01-002 | Documento de Requisitos — Pacote Final 24 | 1.0 | REQ 1–7 |
| PCP-FRUKI01-002 | Documento de Design — Pacote Final 24 | 1.0 | PCP 1–3 |
| VV-FRUKI01-002 | Plano de V&V — Pacote Final 24 | 1.0 | VV 1–5 |
| ITP-FRUKI01-002 | Estratégia de Integração — Pacote Final 24 | 1.0 | ITP 1 |
| RASTR-FRUKI01-002 | Matriz de Rastreabilidade — Pacote Final 24 | 1.0 | REQ 4 |
| ADAP-FRUKI01-002 | Registro de Adaptação — Pacote Final 24 | 1.1 | GPR 2 / CP-C |
| CR-FRUKI01-001 | Solicitação de Mudança — Regra de Ouro | 1.0 | GPR / GCO |
| RAC-FRUKI01-001 | Relatório de Acompanhamento | 1.0 | GPR 14 |
| ATA-FRUKI01-003 | Ata de Aceite Final | 1.0 | GPR (aceite) |
| ATA-FRUKI01-004 | Ata de Validação Sprint 1 | 1.0 | VV 5 |
| ATA-FRUKI01-005 | Ata de Validação Sprint 2 | 1.0 | VV 5 |
| ATA-FRUKI01-006 | Ata de Validação Sprint 3 | 1.0 | VV 5 |
| TAE-FRUKI01-002 | Termo de Encerramento — Pacote Final 24 | 1.1 | GPR (encerramento) |

*Compartilhados (ambos os pacotes)*

| Código | Documento | Versão | Evidência |
|---|---|---|---|
| GDE-FRUKI01-001 | Registro de Análise de Decisão | 1.0 | GDE 2–6 |
| GQA-FRUKI01-001 | Registro de GQA | 1.1 | GPC 3 / CP (iv, v) |
| GCO-FRUKI01-001 | Registro de Configuração | 1.3 | GCO 4 |
| LI-FRUKI01-001 | Lições Aprendidas | 1.0 | GPR 20 / GPC 4 |
| MED-FRUKI01-001 | Registro de Medição | 1.0 | MED 3–4 |

---

**PROFARMA — Cadastro de Clientes · Rede D1000** · Cliente: Profarma S.A. / Rede D1000 · GP: Abraão Oliveira

*Encerrado 29/01/2026 · 18 documentos*

| Código | Documento | Versão | Evidência |
|---|---|---|---|
| TAP-PROFARMA01-001 | Termo de Abertura | 1.0 | GPR 1, 13 |
| PLA-PROFARMA01-001 | Plano de Projeto | 1.0 | GPR 3–12 |
| REQ-PROFARMA01-001 | Documento de Requisitos | 1.2 | REQ 1–7 |
| PCP-PROFARMA01-001 | Documento de Design | 1.3 | PCP 1–3 |
| VV-PROFARMA01-001 | Plano de V&V | 1.1 | VV 1–5 |
| RASTR-PROFARMA01-001 | Matriz de Rastreabilidade | 1.1 | REQ 4 |
| ADAP-PROFARMA01-001 | Registro de Adaptação | 1.0 | GPR 2 / CP-C |
| GDE-PROFARMA01-001 | Registro de Análise de Decisão | 1.0 | GDE 2–6 |
| CTQ-PROFARMA01-001 | Cenários de Teste de Homologação | 1.0 | VV 3 |
| REV-PROFARMA01-001 | Registro de Revisão Técnica | 1.0 | PCP 2 / VV 4 |
| REL-VV-PROFARMA01-001 | Relatório de Execução de Testes | 1.0 | VV 4–5 |
| RAC-PROFARMA01-001 | Relatório de Acompanhamento | 1.0 | GPR 14 |
| ATA-PROFARMA01-001 | Ata de Kickoff | 1.0 | GPR 13 |
| ATA-PROFARMA01-002 | Ata de Aceite Final | 1.0 | GPR (aceite) |
| GQA-PROFARMA01-001 | Registro de GQA | 1.0 | GPC 3 / CP (iv, v) |
| MED-PROFARMA01-001 | Registro de Medição | 1.0 | MED 3–4 |
| LI-PROFARMA01-001 | Lições Aprendidas | 1.0 | GPR 20 / GPC 4 |
| TAE-PROFARMA01-001 | Termo de Encerramento | 1.0 | GPR (encerramento) |

---

**MILHASFACIL — Plataforma Milhas3 · Busca e Monitoramento de Milhas** · Cliente: Hub de Milhas (Felipe) · GP: Abraão Oliveira

*Encerrado 16/11/2025 · 17 documentos · projeto único (sem pacotes/OS) · aceite formal em ATA-MILHASFACIL01-002*

| Código | Documento | Versão | Evidência |
|---|---|---|---|
| TAP-MILHASFACIL01-001 | Termo de Abertura | 1.0 | GPR 1, 13 |
| PLA-MILHASFACIL01-001 | Plano de Projeto | 1.0 | GPR 3–12 |
| ADAP-MILHASFACIL01-001 | Registro de Adaptação | 1.0 | GPR 2 / CP-C |
| REQ-MILHASFACIL01-001 | Documento de Requisitos | 1.0 | REQ 1–7 |
| PCP-MILHASFACIL01-001 | Documento de Design | 1.0 | PCP 1–3 |
| ITP-MILHASFACIL01-001 | Estratégia de Integração | 1.0 | ITP 1–6 |
| RASTR-MILHASFACIL01-001 | Matriz de Rastreabilidade | 1.0 | REQ 4 |
| VV-MILHASFACIL01-001 | Plano de V&V | 1.0 | VV 1–5 |
| GDE-MILHASFACIL01-001 | Registro de Análise de Decisão | 1.0 | GDE 2–6 |
| GCO-MILHASFACIL01-001 | Registro de Configuração | 1.0 | GCO 1–5 |
| GQA-MILHASFACIL01-001 | Registro de GQA | 1.0 | GPC 3 / CP (iv, v) |
| MED-MILHASFACIL01-001 | Registro de Medição | 1.0 | MED 3–4 |
| ATA-MILHASFACIL01-001 | Ata de Kickoff | 1.0 | GPR 13 |
| ATA-MILHASFACIL01-002 | Ata de Aceite Final | 1.0 | GPR (aceite) |
| RAC-MILHASFACIL01-001 | Relatório de Acompanhamento | 1.0 | GPR 14 |
| LI-MILHASFACIL01-001 | Lições Aprendidas | 1.0 | GPR 20 / GPC 4 |
| TAE-MILHASFACIL01-001 | Termo de Encerramento | 1.0 | GPR (encerramento) |

---

**Projetos AASP — estrutura criada, documentação a produzir**

| Pasta | Cliente | Status |
|---|---|---|
| AASP_Andamento-Processuais | AASP | ⬜ A documentar |
| AASP_Automacao-Governanca | AASP | ⬜ A documentar |
| AASP_CNJ | AASP | ⬜ A documentar |

---

### Capacidade (`oficial/05_capacidade/`)

| Código | Documento | Versão | Atende |
|---|---|---|---|
| MAPA-CAP-001 | Mapa de Capacidade dos Processos (CP-E/D/C) | 1.1 | CP-E, CP-D, CP-C (rastreabilidade) |

### Internos (`_interno/`) — não auditados pela ASR

| Código | Documento | Versão | Observação |
|---|---|---|---|
| MAPA-ORG-001 | Mapa de Artefatos / Plano de Implantação (este doc) | 0.38 | Rascunho de gestão |
| GUIA-ORG-001 | Guia de Estrutura do Confluence | 1.0 | Apoio à navegação no Confluence |

### Pendentes / A produzir

| Código | Documento | Prioridade | Observação |
|---|---|---|---|
| DIAG-GPC-001 | Diagrama do Fluxo do Processo-Padrão (figura) | Média | Ilustra PRO-GPC-001; a atualizar com ambientes |
| TREINO-* | Apostilas de treinamento por papel | Baixa | Apoio à preparação da equipe — não é evidência MPS |

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
| 3 | **Os 4 projetos** | 🟨 Em andamento | 4 projetos documentados: FTGASMIG (22 docs — OS-001 encerrada, OS-002 em andamento), FTFRUKI (32 docs — Pacote 1 encerrado Set/2025 + Pacote Final 24 encerrado Jan/2026), PROFARMA/Rede D1000 (18 docs — encerrado Jan/2026), MILHASFACIL/Hub de Milhas (17 docs — encerrado 16/11/2025). Mínimo de 4 projetos atingido; AASP (3 projetos) segue como adicional/opcional. |
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
4. 🟨 **Fase 3 — Evidências de projeto:** 4 projetos documentados (FTGASMIG, FTFRUKI, PROFARMA/D1000, MILHASFACIL/Hub de Milhas) — mínimo de 4 da avaliação atingido
5. ⬜ **Documentar projetos AASP** (Andamento-Processuais, Automacao-Governanca, CNJ) — adicional/opcional; o mínimo de 4 projetos já é atendido (FTGASMIG, FTFRUKI, PROFARMA, MILHASFACIL)
6. ⬜ **Confirmar AQU** com o avaliador líder da ASR (não-aplicabilidade ou versão enxuta)
7. ⬜ **Planilha-mestre de evidências** para entrega à ASR antes da avaliação inicial

> **Observação de auditoria:** este mapa também serve de evidência para GPC 1 (identificação de ativos de processo) e como rastreabilidade entre resultados esperados e artefatos — algo que a ASR vai querer ver logo no início.
