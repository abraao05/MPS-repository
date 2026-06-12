# Guia de Auditorias de GQA — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | GUIA-GPC-002 — Guia de Auditorias de GQA |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este guia apresenta o conjunto de padrões a serem observados na realização das auditorias de **Garantia da Qualidade de Processo (GQA)** dos projetos de software e dos processos organizacionais da Timeware.

Ele **complementa a `EST-GPC-001` (Estratégia de Garantia da Qualidade)**, detalhando a operação das auditorias: os tipos de auditoria, a periodicidade, as ferramentas, a estratégia de execução e os critérios de escalonamento e resolução de não conformidades (NCs).

## 2. Equipe e independência

A GQA é exercida por **membros do Time de Melhoria Contínua, em regime de rodízio**, assegurando a **independência entre quem audita e quem executa**, conforme `EST-GPC-001 §3`:

- Os envolvidos na auditoria de um projeto constam no **plano do projeto**; o auditor designado **não pode ter atuado na execução** daquele projeto.
- A designação do auditor de projeto é feita pelo **Gerente de Projeto** em conjunto com o Time de Melhoria Contínua, respeitada a independência.
- As auditorias de processos **organizacionais** são designadas pela **direção** da Timeware.
- Na verificação dos ativos produzidos pelo próprio Time de Melhoria Contínua, o auditor **não deve ser o autor** do ativo avaliado.
- **Consultores externos** contratados para apoio ao programa de melhoria (por exemplo, a ASR Consultoria) podem conduzir atividades de GQA — em especial a auditoria de **"QA do QA"**.

## 3. Tipos de auditoria de GQA

### 3.1. GQA de projetos de software

As auditorias de GQA são realizadas nos projetos de desenvolvimento sob a metodologia ágil, nas fases e marcos definidos no plano do projeto. Devem ocorrer **conforme os marcos do processo e por amostragem**, com periodicidade **mínima mensal** (ver `EST-GPC-001 §4`).

- O **Auditor de GQA** é responsável por **registrar e agendar** as auditorias no **Jira** (no projeto ou em um quadro específico de tarefas de auditoria).
- As auditorias usam os **checklists de GQA** com critérios pré-definidos do processo-padrão (registro em `TPL-GPC-001 — Registro de Verificação de GQA`; equivalente nos templates do consultor: `CHK-Auditoria de Projetos`, por fase).
- O Auditor de GQA **acompanha as não conformidades** identificadas até o devido encerramento (verificar, reabrir e escalar quando necessário).

### 3.2. GQA de atividades organizacionais

As auditorias dos **processos organizacionais** devem ser executadas no **mínimo a cada 60 dias**.

- O Auditor de GQA designado é responsável por **registrar e agendar** as auditorias organizacionais no **Jira**, em um quadro criado para esse fim.
- O registro segue o `TPL-GPC-001` adaptado ao escopo organizacional (equivalente do consultor: `CHK-Auditoria Organizacional`, por área de processo, com percentual de aderência).

### 3.3. Auditoria de "QA do QA"

Sempre que a Timeware estiver executando um **projeto de melhoria com objetivo de (re)certificação MPS-SW**, o **"QA do QA"** — a verificação da própria função de garantia da qualidade — é realizado por **consultores da empresa contratada** (ASR).

- Nesse caso, a consultoria utiliza o **checklist de QA do QA** da Timeware, mantido no repositório de ativos de processo (Confluence / repositório MPS).

## 4. Atividades de GQA e periodicidade

| Tarefa | Periodicidade | Participantes | Registro |
|---|---|---|---|
| Executar auditorias de GQA de projetos | Conforme os marcos e as sprints do projeto (mínimo mensal) | Auditor de GQA · Gerente de Projeto | Jira + `TPL-GPC-001` |
| Executar auditorias de GQA organizacionais | No mínimo a cada 60 dias | Auditor de GQA · Responsável pelo processo | Jira + `TPL-GPC-001` (organizacional) |
| Executar auditoria de "QA do QA" | Quando houver projeto de (re)certificação | Consultor externo (ASR) | Checklist de QA do QA |

O Auditor de GQA é responsável pelo **encerramento das não conformidades (NCs)** no Jira — nos projetos, nas operações ou no quadro organizacional aberto para manter as atividades de GQA organizacional.

> Uma **não conformidade (NC)** é o não cumprimento de um requisito do modelo de referência **MR-MPS-SW:2024**, em processos, produtos (software) ou serviços.

## 5. Ferramentas e recursos

| Ferramenta | Uso |
|---|---|
| **Jira** | Registro, agendamento e acompanhamento das auditorias e das NCs (tarefas) |
| **Confluence / repositório MPS** | Checklists de GQA, registros de verificação (`TPL-GPC-001`), checklist de QA do QA e evidências |
| **Azure DevOps / Git** | Verificação de itens de configuração e baselines, quando aplicável à auditoria |

A organização dos artefatos e a retenção seguem o `PLA-GCO-001` (Gerência de Configuração) e a `CONV-ORG-001` (nomenclatura e versionamento).

## 6. Estratégia de execução das auditorias

As auditorias seguem o modelo **híbrido (marcos + amostragem)** definido na `EST-GPC-001 §4`, com **frequência intermitente conforme o histórico de aderência** dos processos:

- **Projetos:** as auditorias não precisam ocorrer em todas as sprints; podem ser executadas em **fases específicas** (Planejamento, Análise, Desenvolvimento, Configuração, Entrega) ou em **sprints amostrais**, conforme o percentual de aderência observado.
- **Operações de serviço e processos organizacionais:** podem ser executadas em **janelas maiores** (por exemplo, a cada seis ou doze meses) quando o histórico de aderência for consistentemente alto, respeitado o mínimo de 60 dias para o nível organizacional.

O dimensionamento da amostra e da frequência é decisão do Time de Melhoria Contínua, registrada no planejamento das verificações.

## 7. Critérios de escalonamento e resolução de NCs

**Resolução.** A resolução das NCs é feita no **Jira**, na tarefa referente à própria NC, com **ação corretiva, responsável e prazo**, acompanhada pelo Auditor de GQA até o encerramento.

**Gatilhos de escalonamento.** Uma NC é escalada quando:

- o **prazo-limite** de resolução informado pelo auditor na tarefa for ultrapassado;
- o **auditado se recusar** a realizar a correção;
- o **auditado estiver ausente** da organização no vencimento do prazo de resolução.

**Procedimento.** No escalonamento, atribui-se a tarefa da NC ao **nível hierárquico imediatamente superior** e, persistindo o impasse, à **direção**, para que as ações cabíveis sejam tomadas (ver `EST-GPC-001 §6`).

## 8. Documentos relacionados

- `EST-GPC-001` — Estratégia de Garantia da Qualidade (GQA)
- `PRO-GPC-001` — Processo-Padrão Organizacional
- `GUIA-GPC-001` — Guia de Adaptação do Processo-Padrão
- `TPL-GPC-001` — Registro de Verificação de GQA
- `PLA-GPC-001` — Plano de Gestão e Melhoria de Processos
- `PRO-OSW-001` — Governança Organizacional de Processos (análise crítica e escalonamento)
- `PLA-GCO-001` — Plano de Gerência de Configuração
- `CONV-ORG-001` — Convenção de Nomenclatura e Versionamento

## 9. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este guia apoia o resultado **GPC 3** do processo **Gerência de Processos (GPC)** e os **atributos de capacidade CP-C (iv) e (v)** — verificação objetiva da aderência ao processo e avaliação objetiva dos produtos de trabalho por função independente.

| Resultado / atributo | Onde é atendido neste documento |
|---|---|
| GPC 3 — estratégia e plano de garantia da qualidade (operação das auditorias) | Seções 1 a 7 |
| CP-C (iv) — verificação objetiva de que o processo é seguido | Seções 3 e 6 |
| CP-C (v) — produtos de trabalho avaliados objetivamente | Seções 3 e 4 |

**Nomenclatura equivalente — templates MPS do consultor de avaliação**

| Artefato Timeware | Código Timeware | Equivalente nos templates MPS (consultor) |
|---|---|---|
| Registro de Verificação de GQA — projetos | `TPL-GPC-001` | `CHK-Auditoria de Projetos` — checklists por fase, com `% de Aderência` por fase |
| Registro de Verificação de GQA — organização | `TPL-GPC-001` (adaptado) | `CHK-Auditoria Organizacional` — checklist por área de processo, com `Percentual de Aderência` |
| Auditoria da função de qualidade | (conduzida pela ASR) | `CHK-Auditoria de QA do QA` |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Versão inicial — adaptada do "Guia de Auditorias de GQA" fornecido por consultoria externa ao padrão de documentação Timeware (terminologia Timeware/SEPG; ferramentas Jira/Confluence/repositório MPS no lugar de Webmaster/Google Drive; referência ao MR-MPS-SW:2024; vínculo a EST-GPC-001 e TPL-GPC-001). |
