# Sistema de Processos MPS-SW Nível C — TIMEWARE

Repositório dos ativos de processo da **Timeware Brasil Softwares e Serviços LTDA**, estruturados para a avaliação oficial do **MR-MPS-SW:2024 — Nível C**.

---

## 1. Sobre este repositório

Este repositório contém a **camada de definição** dos processos da Timeware: políticas, processos, estratégias, planos, guias e templates que descrevem como a organização desenvolve software sob medida, de forma alinhada ao modelo MPS-SW.

- **Escopo da avaliação:** desenvolvimento de **software sob medida para clientes** (modelo fábrica de software). Produto próprio e sustentação não fazem parte do escopo desta versão.
- **Modelo de referência:** MR-MPS-SW:2024, Nível C.
- **Avaliadora:** ASR Consultoria.

> **Estado atual:** a camada de **definição** dos 12 processos está completa. A camada de **evidências** (preenchimento dos templates com dados de 4 projetos reais) é a etapa seguinte.

## 2. Organização do repositório

```
/
├── oficial/                     ← evidência MPS (auditada pela ASR)
│   ├── 00_governanca/           ← política, processo-padrão, GQA, riscos, OSW, diagrama
│   ├── 01_apoio/                ← MED, CAP, GDE, GCO, AQU
│   ├── 02_processos_projeto/    ← GPR, REQ, PCP, ITP, VV
│   ├── 03_templates/            ← TPL-* (modelos preenchidos por projeto)
│   └── 04_capacidade/           ← mapa de capacidade
│
└── _interno/                    ← apoio à gestão (NÃO vai para a avaliação)
    ├── MAPA-ORG-001             ← mapa de artefatos (índice-mestre)
    ├── GUIA-ORG-001             ← guia de estrutura do Confluence
    └── GUIA-GPR-001             ← roteiro de kickoff
```

**Duas categorias de documento:**
- **[OFICIAL]** — evidência MPS, auditada pela ASR, pasta `oficial/`.
- **[INTERNO]** — apoio/gestão, não vai para a avaliação, pasta `_interno/`.

## 3. Convenção de nomenclatura

Os documentos seguem o padrão **`TIPO-PROCESSO-NÚMERO`** (definido em CONV-ORG-001):

- **Tipos:** `POL` (política), `CONV` (convenção), `PRO` (processo), `EST` (estratégia), `PLA` (plano), `TPL` (template), `GUIA`, `MAPA`, `DIAG` (diagrama).
- **Processo:** sigla MPS (GPR, REQ, GPC...) ou `ORG` (organizacional).
- **Versão:** `MAIOR.MENOR`, sem data no nome (o histórico de versões fica no rodapé de cada documento e no Git).

## 4. Os 12 processos (camada de definição — completa)

### Governança
| Código | Documento | Versão | Resultados MPS |
|---|---|---|---|
| POL-ORG-001 | Política Organizacional de Processos | 1.0 | OSW 1 |
| CONV-ORG-001 | Convenção de Nomenclatura e Versionamento | 1.0 | GCO 1, 4 |
| PRO-GPC-001 | Processo-Padrão Organizacional | 2.1 | GPC 2 |
| GUIA-GPC-001 | Guia de Adaptação do Processo-Padrão | 1.2 | GPC 2 |
| EST-GPC-001 | Estratégia de Garantia da Qualidade | 1.2 | GPC 3 |
| EST-GPC-002 | Estratégia de Gerência de Riscos | 1.1 | GPC 7 |
| PRO-GPC-002 | Definição do Time de Melhoria Contínua | 1.1 | GPC 6 |
| PLA-GPC-001 | Plano de Gestão e Melhoria de Processos | 1.2 | GPC 1, 4, 5, 8, 10, 11 |
| PRO-OSW-001 | Governança Organizacional de Processos | 1.1 | OSW 2-7 |
| PRO-OSW-002 | Gestão de Portfólio de Projetos | 1.1 | OSW 8-10 |

### Apoio
| Código | Documento | Versão | Resultados MPS |
|---|---|---|---|
| PLA-MED-001 | Plano de Medição | 1.1 | MED 1-7; GPC 9; OSW 6 |
| PLA-CAP-001 | Plano de Capacitação | 1.0 | CAP 1-4 |
| PRO-GDE-001 | Processo de Gerência de Decisões | 1.0 | GDE 1-6 |
| PLA-GCO-001 | Plano de Gerência de Configuração | 1.0 | GCO 1-5 |
| PRO-AQU-001 | Processo de Aquisição | 1.0 | AQU 1-4 |

### Processos de Projeto
| Código | Documento | Versão | Resultados MPS |
|---|---|---|---|
| PRO-GPR-001 | Processo de Gerência de Projetos | 1.2 | GPR 1-20 |
| PRO-REQ-001 | Processo de Engenharia de Requisitos | 1.1 | REQ 1-7 |
| PRO-PCP-001 | Processo de Projeto e Construção do Produto | 1.1 | PCP 1-3 |
| PRO-ITP-001 | Processo de Integração do Produto | 1.0 | ITP 1-6 |
| PRO-VV-001 | Processo de Verificação e Validação | 1.2 | VV 1-5 |

### Capacidade
| Código | Documento | Versão | Resultados MPS |
|---|---|---|---|
| MAPA-CAP-001 | Mapa de Capacidade dos Processos | 1.0 | CP-E/D/C (rastreabilidade) |

## 5. Templates (preenchidos por projeto)

| Código | Documento | Processo |
|---|---|---|
| TPL-GPR-001 | Plano de Projeto | GPR |
| TPL-GPR-002 | Termo de Abertura do Projeto | GPR |
| TPL-GPR-003 | Registro de Adaptação do Processo | GPR 2 / CP-C |
| TPL-GPR-004 | Termo de Encerramento e Aceite | GPR |
| TPL-GPR-005 | Relatório de Acompanhamento (Status Report) | GPR 14 |
| TPL-GPR-006 | Change Request | GPR / GCO |
| TPL-REQ-001 | Documento de Requisitos | REQ |
| TPL-REQ-002 | Matriz de Rastreabilidade | REQ 4 |
| TPL-PCP-001 | Documento de Design | PCP |
| TPL-ITP-001 | Estratégia de Integração | ITP |
| TPL-VV-001 | Plano de Verificação e Validação | VV |
| TPL-VV-002 | Registro de Revisão por Pares | VV 2 |
| TPL-GDE-001 | Registro de Análise de Decisão (RAD) | GDE |
| TPL-ORG-001 | Ata de Reunião (multiuso) | — |

## 6. O fluxo do processo-padrão

O desenvolvimento de software sob medida segue **sete fases** (detalhadas em PRO-GPC-001):

1. **Originação** — Comercial fecha o contrato (escopo macro) e faz a passagem de bastão ao Escritório de Projetos.
2. **Abertura (Kickoff gerencial)** — marco gerencial de início; gera o Termo de Abertura.
3. **Discovery e Requisitos** — Tech Lead + PO levantam e especificam; produz o Documento de Requisitos (funcional + técnico).
4. **Concepção (trilhas paralelas)** — trilha de projeto (escopo, marcos) e trilha de produto (arquitetura, design, estimativa) geram os insumos do plano.
5. **Planejamento e Aprovação do Plano** — plano fechado e aprovado pelo cliente (baseline; aceite em ata).
6. **Desenvolvimento (Sprints)** — Scrum, backlog incremental, design adiantado, Definição de Pronto.
7. **Homologação, Entrega e Encerramento** — validação, aprovação do cliente, produção e encerramento formal.

**Ambientes:** Desenvolvimento → QA → Homologação → Stage (réplica de produção) → Produção. O stage é recomendado, mas adaptável por projeto.

**Encerramento em dois níveis:** aceite de produto (review de sprint, incremental) e encerramento de projeto (Termo de Encerramento).

## 7. Ferramentas

| Ferramenta | Uso |
|---|---|
| **Jira** | Gestão de projeto, backlog, riscos, ações, casos de teste, medidas. |
| **Git + Azure DevOps** | Código-fonte, baselines (tags/releases), integração contínua, Pull Requests. |
| **Azure Test Plans / Xray** | Casos e resultados de teste. |
| **Confluence** | Biblioteca de processos e documentação de projetos. |

## 8. Documentação no Confluence

A documentação é mantida em **dois espaços** (ver GUIA-ORG-001):
- **Espaço PROCESSOS** — biblioteca de ativos organizacionais (este repositório), edição restrita ao Time de Melhoria Contínua.
- **Espaço PROJETOS** — evidências dos projetos, cada um em árvore idêntica, com links para Jira e Git.

## 9. Estrutura de qualidade (papéis)

A garantia da qualidade opera em três funções separadas, assegurando independência:
- **Time de Melhoria Contínua** — define e mantém os processos.
- **Equipes de Engenharia** — executam os processos.
- **GQA de Processo** — verifica a aderência (auditor independente da equipe avaliada).

> A "garantia da qualidade" de **processo** (GQA) é distinta da qualidade de **software** (QA/V&V). São funções diferentes.

## 10. Estado e próximos passos

**Concluído:** camada de definição completa (12 processos + templates + mapa de capacidade).

**Próximas etapas:**
- Definir os 4 projetos da avaliação (modelo fábrica de software).
- Preencher os templates com as evidências dos projetos (Confluence, Jira, Git).
- Validar pendências com a ASR e com as equipes (ver MAPA-ORG-001).
- Converter os documentos aprovados para Word (formato auditado pela ASR), após revisão.

---

*Para o índice completo e o status de rastreabilidade de cada resultado MPS, ver `_interno/MAPA-ORG-001`.*
