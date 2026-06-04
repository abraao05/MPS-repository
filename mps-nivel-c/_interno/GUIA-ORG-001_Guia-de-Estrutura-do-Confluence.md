# Guia de Estrutura do Confluence — MPS-SW Nível C (TIMEWARE)

| Campo | Valor |
|---|---|
| **Documento** | GUIA-ORG-001 — Guia de Estrutura do Confluence |
| **Versão** | 1.0 |
| **Data** | 12/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Classificação** | Interno (apoio à organização da documentação) |
| **Finalidade** | Orientar a montagem dos espaços e páginas do Confluence para a avaliação MPS-SW Nível C |

---

## 1. Objetivo

Este guia descreve **como organizar o Confluence** para a documentação do MPS-SW Nível C da Timeware. Ele serve para que a pessoa responsável crie a estrutura de espaços e páginas de forma padronizada.

A organização separa o que é **organizacional** (a biblioteca de processos, estável) do que é **evidência de projeto** (muda a cada projeto). São, portanto, **dois espaços** distintos.

## 2. Visão geral

```
Confluence
├── Espaço 1 — PROCESSOS   (biblioteca de ativos organizacionais)
└── Espaço 2 — PROJETOS    (evidências dos projetos + consolidado organizacional)
```

- **Espaço PROCESSOS:** contém os documentos de definição (políticas, processos, estratégias, templates, mapa de capacidade). É estável; a edição deve ser **restrita ao Time de Melhoria Contínua**.
- **Espaço PROJETOS:** contém uma árvore por projeto (evidências) e uma seção de consolidado organizacional. As equipes de projeto alimentam suas árvores.

A "cola" entre os espaços: cada documento de projeto **referencia o processo organizacional que segue** (ex.: "elaborado conforme PRO-GPR-001").

## 3. Espaço 1 — PROCESSOS

Estrutura de páginas sugerida:

```
PROCESSOS
├── 00 - Governança
│     ├── POL-ORG-001  — Política Organizacional de Processos
│     ├── CONV-ORG-001 — Convenção de Nomenclatura e Versionamento
│     ├── PRO-GPC-001  — Processo-Padrão Organizacional
│     ├── GUIA-GPC-001 — Guia de Adaptação do Processo-Padrão
│     ├── EST-GPC-001  — Estratégia de Garantia da Qualidade
│     ├── EST-GPC-002  — Estratégia de Gerência de Riscos
│     ├── PRO-GPC-002  — Definição do Time de Melhoria Contínua
│     ├── PLA-GPC-001  — Plano de Gestão e Melhoria de Processos
│     ├── PRO-OSW-001  — Governança Organizacional de Processos
│     └── PRO-OSW-002  — Gestão de Portfólio de Projetos
├── 01 - Apoio
│     ├── PLA-MED-001  — Plano de Medição
│     ├── PLA-CAP-001  — Plano de Capacitação
│     ├── PRO-GDE-001  — Processo de Gerência de Decisões
│     ├── PLA-GCO-001  — Plano de Gerência de Configuração
│     └── PRO-AQU-001  — Processo de Aquisição
├── 02 - Processos de Projeto
│     ├── PRO-GPR-001  — Processo de Gerência de Projetos
│     ├── PRO-REQ-001  — Processo de Engenharia de Requisitos
│     ├── PRO-PCP-001  — Processo de Projeto e Construção do Produto
│     ├── PRO-ITP-001  — Processo de Integração do Produto
│     └── PRO-VV-001   — Processo de Verificação e Validação
├── 03 - Templates
│     ├── TPL-GPR-001  — Template de Plano de Projeto
│     ├── TPL-REQ-001  — Template de Documento de Requisitos
│     ├── TPL-REQ-002  — Template de Matriz de Rastreabilidade
│     ├── TPL-PCP-001  — Template de Documento de Design
│     ├── TPL-ITP-001  — Template de Estratégia de Integração
│     ├── TPL-VV-001   — Template de Plano de V&V
│     └── TPL-VV-002   — Template de Registro de Revisão por Pares
└── 04 - Capacidade
      └── MAPA-CAP-001 — Mapa de Capacidade dos Processos
```

## 4. Espaço 2 — PROJETOS

### 4.1. Árvore-padrão de cada projeto

**Todos os projetos seguem a mesma árvore** (mesma ordem e mesmos itens). A ordem reflete o fluxo do processo-padrão (PRO-GPC-001), da abertura ao encerramento.

```
[NN] - [Nome do Projeto]
├── 1. Termo de Abertura                         (marco: Kickoff gerencial)
├── 2. Registro de Adaptação do Processo
├── 3. Documento de Requisitos                   (+ Matriz de Rastreabilidade)
├── 4. Documento de Design                       (Concepção: arquitetura + UX/UI quando aplicável)
├── 5. Plano de Projeto                          (fechado na concepção)
├── 6. Plano de V&V + cenários (Gherkin)
├── 7. Registros de GQA (verificações do projeto)
├── 8. Atas
│      ├── Ata de Kickoff (abertura gerencial)
│      ├── Ata de Aprovação do Plano             (aceite do cliente / baseline)
│      ├── Atas de revisão / sprint review
│      └── Ata de Encerramento
├── 9. Relatório de Encerramento + Lições Aprendidas
├── 10. Change Requests                          (mudanças sobre a baseline, quando houver)
└── Links externos
       ├── Jira  → backlog, riscos, casos de teste, medidas
       └── Git/Azure → repositório, baselines (tags), Pull Requests
```

### 4.2. Observações importantes

- **Aceite do plano é por reunião:** o aceite do cliente sobre o Plano de Projeto é registrado na **Ata de Aprovação do Plano** (item 8), não em documento assinado separado. Essa ata estabelece a baseline.
- **Design e Plano vêm antes da execução:** são produtos da concepção/planejamento; por isso aparecem antes na árvore.
- **UX/UI é condicional:** projetos sem front-end (APIs, serviços) não têm design de UX/UI — apenas arquitetura. Registrar isso no Registro de Adaptação (item 2).
- **Evidências em três lugares:** nem tudo é página no Confluence. Documentos ficam aqui; backlog/riscos/testes/medidas ficam no **Jira**; código/baselines/PRs ficam no **Git/Azure**. Os links (item "Links externos") conectam tudo.
- **Cada documento referencia o processo:** ex.: o Plano de Projeto cita "conforme PRO-GPR-001"; o Documento de Requisitos cita "conforme PRO-REQ-001".

### 4.3. Projetos da avaliação

```
PROJETOS
├── 01 - [Projeto A]      (a definir)
├── 02 - [Projeto B]      (a definir)
├── 03 - [Projeto C]      (a definir)
├── 04 - [Projeto D]      (a definir)
└── 99 - Consolidado Organizacional
       ├── Verificações de GQA (consolidado)
       ├── Indicadores consolidados (MED)
       └── Atas de Análise Crítica (trimestral)
```

> Os quatro projetos devem seguir o modelo de **fábrica de software** (recebem requisitos, passam pela esteira de desenvolvimento), e não o modelo squad-as-service.

## 5. Permissões sugeridas

| Espaço | Quem edita | Quem visualiza |
|---|---|---|
| PROCESSOS | Time de Melhoria Contínua | Toda a organização |
| PROJETOS | Equipes de projeto + Time de Melhoria Contínua | Conforme política interna |

## 6. Passo a passo para montagem

1. Criar o **Espaço PROCESSOS** e as páginas-seção (00 a 04) conforme a seção 3.
2. Migrar os documentos de definição (do repositório Git) para as páginas correspondentes.
3. Restringir a edição do espaço ao Time de Melhoria Contínua.
4. Criar o **Espaço PROJETOS**.
5. Criar **uma página-modelo** com a árvore-padrão da seção 4.1 e usá-la como template (duplicar) para cada projeto.
6. Criar a seção **99 - Consolidado Organizacional**.
7. Em cada projeto, preencher os documentos a partir dos templates do espaço PROCESSOS e inserir os links para Jira e Git.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 12/11/2025 | Time de Melhoria Contínua | Definição inicial do guia de estrutura do Confluence |
