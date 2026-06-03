# Convenção de Nomenclatura e Versionamento de Documentos — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | CONV-ORG-001 — Convenção de Nomenclatura e Versionamento |
| **Versão** | 1.0 |
| **Data** | `<dd/mm/aaaa>` |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Processo MPS-SW relacionado** | GCO 1, GCO 4 — Gerência de Configuração |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Esta convenção define como os documentos e ativos de processo da Timeware são identificados, nomeados e versionados. O objetivo é garantir que todo item tenha identificação única e rastreável, que sua versão e situação sejam sempre conhecidas, e que a organização mantenha controle sobre seus ativos de processo.

Os documentos da Timeware são tratados como **itens de configuração**: cada um possui um código único, um tipo, uma descrição e uma situação controlada.

## 2. Código de identificação

Todo documento recebe um código no formato:

```
TIPO-PROCESSO-NÚMERO
```

- **TIPO** — natureza do documento (ver tabela 3).
- **PROCESSO** — sigla do processo MPS-SW ao qual o documento pertence; ou `ORG` quando o documento é de abrangência organizacional (não vinculado a um único processo).
- **NÚMERO** — sequencial de três dígitos dentro daquela combinação tipo+processo, iniciando em `001`.

**Exemplos:**

| Código | Leitura |
|---|---|
| `POL-ORG-001` | Política organizacional nº 001 |
| `CONV-ORG-001` | Convenção organizacional nº 001 (este documento) |
| `PRO-GPC-001` | Descrição de processo do GPC nº 001 |
| `TPL-GPR-001` | Template do processo GPR nº 001 |
| `PLA-MED-001` | Plano do processo MED nº 001 |
| `EST-GPC-001` | Estratégia do processo GPC nº 001 |

## 3. Tipos de documento

| TIPO | Significado | Exemplos de uso |
|---|---|---|
| `POL` | Política | Política Organizacional de Processos |
| `CONV` | Convenção | Esta convenção; convenções de codificação |
| `PRO` | Processo / Procedimento | Descrição de processo-padrão, procedimentos operacionais |
| `EST` | Estratégia | Estratégia de garantia da qualidade; estratégia de riscos |
| `PLA` | Plano | Plano de medição; plano de capacitação; plano de projeto |
| `TPL` | Template / Modelo | Modelos em branco a serem preenchidos por projeto |
| `REG` | Registro | Templates preenchidos; atas; relatórios; evidências |
| `GUIA` | Guia / Diretriz | Guia de adaptação (tailoring); diretrizes |
| `MAPA` | Índice / Mapa | Mapa de artefatos; índices-mestre |
| `CAT` | Catálogo | Catálogo de medidas; catálogo de ativos |

## 4. Siglas de processo (MPS-SW Nível C)

| Sigla | Processo |
|---|---|
| `GPR` | Gerência de Projetos |
| `REQ` | Engenharia de Requisitos |
| `PCP` | Projeto e Construção do Produto |
| `ITP` | Integração do Produto |
| `VV` | Verificação e Validação |
| `GCO` | Gerência de Configuração |
| `CAP` | Capacitação |
| `OSW` | Gerência Organizacional de Software |
| `GPC` | Gerência de Processos |
| `MED` | Medição |
| `AQU` | Aquisição |
| `GDE` | Gerência de Decisões |
| `ORG` | Organizacional (sem vínculo a um processo único) |

## 5. Nome do arquivo

O nome do arquivo combina o código com uma descrição curta, separados por underline, sem datas e sem espaços:

```
CÓDIGO_Descricao-Curta.extensao
```

**Exemplos:**
- `POL-ORG-001_Politica-Organizacional-de-Processos.md`
- `TPL-GPR-001_Plano-de-Projeto.md`
- `PRO-GPC-001_Processo-Padrao-Organizacional.md`

Regras:
- Sem datas no nome do arquivo. As datas ficam apenas no cabeçalho e no histórico de revisões internos ao documento.
- Sem acentos e sem espaços no nome do arquivo (usar hífen na descrição).
- O código nunca muda ao longo da vida do documento, mesmo entre versões.

## 6. Versionamento

A versão segue o formato `MAIOR.MENOR`, sem data:

| Situação | Versão | Quando aplicar |
|---|---|---|
| Rascunho | `0.1`, `0.2`, ... | Documento em elaboração, ainda não aprovado. |
| Aprovado | `1.0` | Primeira versão aprovada e oficializada. |
| Ajuste menor | `1.1`, `1.2`, ... | Correções, ajustes de texto, complementos que não alteram a estrutura. |
| Revisão maior | `2.0`, `3.0`, ... | Mudança estrutural, de escopo ou de conteúdo significativa. |

Regras:
- A versão fica registrada no cabeçalho do documento e na tabela de histórico de revisões.
- A data associada a cada versão é registrada no histórico de revisões, podendo refletir a data real de formalização do conteúdo.

## 7. Situação (estado do documento)

Todo documento tem uma situação, registrada quando aplicável:

| Situação | Significado |
|---|---|
| **Rascunho** | Em elaboração; versão `0.x`. |
| **Em revisão** | Submetido à revisão/aprovação. |
| **Aprovado** | Oficializado; versão `1.0` ou superior. |
| **Obsoleto** | Substituído por versão mais recente ou descontinuado. |

## 8. Estrutura mínima de cabeçalho

Todo documento da Timeware inicia com um cabeçalho de identificação contendo, no mínimo: código do documento, versão, data, organização, aprovação e processo MPS-SW relacionado. Documentos de definição encerram com uma tabela de **Histórico de revisões** (versão, data, autor, descrição).

## 9. Documentos relacionados

- POL-ORG-001 — Política Organizacional de Processos
- Plano de Gerência de Configuração (GCO)
- Mapa de Artefatos MPS-SW Nível C

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Definição da convenção de nomenclatura e versionamento |
