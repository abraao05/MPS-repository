# Processo de Capacitação — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-CAP-001 — Processo de Capacitação |
| **Versão** | 1.1 |
| **Data** | 10/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Responsável** | Silvio Baroni |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware garante que as pessoas que executam os processos organizacionais e de projeto possuem as competências necessárias para fazê-lo — identificando necessidades de capacitação, planejando e realizando ações de desenvolvimento, registrando as evidências de competência e avaliando a efetividade das ações.

O processo de Capacitação (CAP) é um processo de apoio organizacional: garante que os atributos de capacidade relacionados às pessoas (preparo para os processos) sejam sistematicamente atendidos em toda a organização.

## 2. Princípio

A competência de quem executa um processo é condição necessária para que o processo produza resultados consistentes. Portanto, antes de colocar uma pessoa em um papel, a organização deve assegurar que ela está preparada — seja por formação/experiência pré-existente, seja por capacitação interna realizada. Ambas as formas são evidência válida de competência.

## 3. Entradas do processo

- Matriz de papéis e responsabilidades (MAPA-ORG-001): define os papéis dos 12 processos e as competências exigidas por papel.
- Necessidades dos projetos: tecnologias, ferramentas e competências exigidas pelos projetos em andamento ou previstos.
- Lacunas de competência: identificadas em avaliações de desempenho, achados de GQA e observação de líderes técnicos.
- Revisão de processos: adoção ou revisão de processos organizacionais exige capacitação prévia das equipes.
- Evidências existentes: currículos, certificados e registros de treinamentos anteriores (REG-CAP-*, CVs em `cap/curriculos/`).

## 4. Atividades do processo

### 4.1 Identificação das necessidades de capacitação

As necessidades de capacitação são identificadas a partir de três fontes:

| Fonte | Como se manifesta | Responsável |
|---|---|---|
| **Necessidades dos projetos** | Tecnologias ou competências novas exigidas por projetos previstos | Gerente de Projeto + Tech Lead |
| **Necessidades dos processos** | Adoção, revisão ou implantação de processos organizacionais | Time de Melhoria Contínua |
| **Lacunas de competência** | Avaliações de desempenho; achados de GQA; observação dos líderes | Líderes / Tech Leads |

As necessidades identificadas são consolidadas em um **mapa de necessidades de capacitação** (planilha no Confluence), revisado semestralmente pelo Time de Melhoria Contínua com apoio da área de Cultura e Pessoas (RH).

### 4.2 Planejamento das ações de capacitação

A partir das necessidades identificadas, é elaborado um plano de capacitação que:

- prioriza as ações pela relevância para os projetos e para os objetivos da organização;
- define modalidade (treinamento interno, workshop, trilha, code dojo, mentoria, certificação externa);
- designa instrutores ou facilitadores, datas e participantes esperados;
- aloca recursos necessários (carga horária, material, orçamento para certificações).

A abordagem combina as modalidades conforme o tipo de competência: competências de processo são desenvolvidas por trilhas internas e workshops conduzidos pelo Time de Melhoria Contínua; competências técnicas são desenvolvidas por workshops técnicos conduzidos pelos líderes técnicos ou consultores especializados; competências pré-existentes são evidenciadas por currículo.

O detalhamento operacional das trilhas por papel está nos materiais de capacitação (MAT-CAP-*) e o plano vigente é mantido em PLA-CAP-001.

### 4.3 Realização das ações de capacitação

As ações planejadas são realizadas e registradas. Cada sessão ou workshop gera um **Registro de Capacitação (REG-CAP-*)** que documenta:

- data, tema e modalidade da ação;
- facilitador/instrutor;
- participantes e confirmação de presença;
- conteúdo abordado;
- evidência de realização (lista de presença, material produzido, avaliação aplicada).

Para certificações externas, o certificado obtido pelo colaborador é anexado ao registro de competência.

### 4.4 Evidenciação de competência

A competência de cada colaborador em cada papel é evidenciada de duas formas:

- **Competência pré-existente:** formação acadêmica, certificações profissionais e experiência relevante, evidenciadas por currículo arquivado em `cap/curriculos/` e indexado no REG-CAP-CV-001.
- **Competência desenvolvida internamente:** trilhas, workshops e sessions conduzidos pela organização, evidenciados pelos registros de capacitação (REG-CAP-*).

A visão consolidada papel → titular → evidência está na Matriz de Papéis e Responsabilidades (MAPA-ORG-001 §5).

### 4.5 Avaliação da efetividade

Após cada ciclo de capacitação, a efetividade das ações é avaliada verificando se o aprendizado foi aplicado nos projetos. A avaliação considera o retorno dos participantes, a observação dos líderes e os indicadores de desempenho dos processos.

Os resultados da avaliação são registrados (AVA-CAP-* e REL-CAP-*) e realimentam o planejamento das próximas ações. Lacunas persistentes geram novas ações de capacitação ou reforço.

### 4.6 Manutenção dos recursos de capacitação

A organização mantém os recursos necessários ao programa de capacitação: instrutores internos identificados e disponíveis, materiais e trilhas atualizados (MAT-CAP-*), orçamento para certificações externas. A manutenção desses recursos é responsabilidade do COO e da área de Cultura e Pessoas.

## 5. Saídas do processo

- Mapa de necessidades de capacitação atualizado (Confluence).
- Registros de sessões e workshops (REG-CAP-*).
- Currículos e certificados arquivados (`cap/curriculos/`).
- Índice de evidências de competência (REG-CAP-CV-001).
- Matriz de papéis com titulares e evidências de competência (MAPA-ORG-001 §5).
- Avaliações de efetividade (AVA-CAP-* e REL-CAP-*).

## 6. Papéis

| Papel | Responsabilidade no processo |
|---|---|
| **COO (Operações)** | Garante recursos e orçamento para a capacitação; autoriza o plano de capacitação. |
| **Cultura e Pessoas / RH** | Mantém o controle de capacitação, os registros e os recursos; apoia na identificação de necessidades. |
| **Time de Melhoria Contínua** | Identifica necessidades relacionadas aos processos organizacionais; planeja e conduz as trilhas de processo; mantém o mapa de necessidades; avalia a efetividade. |
| **Líderes / Tech Leads** | Identificam lacunas técnicas nas equipes; atuam como instrutores e mentores em workshops técnicos. |
| **Consultores externos (quando aplicável)** | Conduzem capacitações especializadas (ex.: processo, arquitetura, qualidade) contratadas como PJ. |
| **Colaboradores** | Participam das ações de capacitação e aplicam o aprendizado nos projetos. |

## 7. Documentos relacionados

- PLA-CAP-001 — Plano Operacional de Capacitação (abordagem, modalidades, frequência de revisão do mapa de necessidades)
- MAPA-ORG-001 — Matriz de Papéis e Responsabilidades (papel × competências × titulares × evidências)
- REG-CAP-CV-001 — Índice de Currículos e Evidências de Competência
- MAT-CAP-* — Materiais e trilhas de capacitação por papel
- POL-ORG-001 — Política Organizacional de Processos
- PRO-GPC-002 — Definição do Time de Melhoria Contínua
- PRO-GPC-001 — Processo-Padrão Organizacional

## 8. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados do processo **Capacitação (CAP)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| CAP 1 — necessidades de capacitação identificadas | Seção 4.1; PLA-CAP-001 §3 |
| CAP 2 — estratégia/plano de capacitação estabelecido | Seção 4.2; PLA-CAP-001 §2 e §3 |
| CAP 3 — capacitação conduzida e registrada | Seções 4.3 e 4.4; REG-CAP-001 a REG-CAP-013; curriculos arquivados |
| CAP 4 — eficácia da capacitação avaliada; recursos/instrutores mantidos | Seções 4.5 e 4.6; AVA-CAP-*; REL-CAP-001 |

Este processo apoia diretamente os **atributos de capacidade CP-ii e CP-iii** do MR-MPS-SW — responsáveis pelos processos definidos e pessoas preparadas — para todos os 12 processos no escopo da avaliação.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Silvio Baroni |
| 1.0 | 10/06/2026 | Time de Melhoria Contínua | Versão inicial — definição formal do processo de capacitação, complementando o plano operacional PLA-CAP-001 e integrando a camada de evidências de competência (MAPA-ORG-001, REG-CAP-CV-001) |
