# Estratégia de Garantia da Qualidade de Processo — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | EST-GPC-001 — Estratégia de Garantia da Qualidade (GQA) |
| **Versão** | 1.2 |
| **Data** | 17/12/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Esta estratégia define como a Timeware garante, de forma objetiva e independente, que seus processos estão sendo seguidos e que os produtos de trabalho atendem aos padrões estabelecidos. A Garantia da Qualidade de Processo (GQA) é a função que verifica a aderência aos processos definidos, registra os desvios encontrados, acompanha sua correção e identifica oportunidades de melhoria.

## 2. Escopo da garantia da qualidade

A GQA da Timeware verifica:

- **Aderência ao processo:** se os projetos e atividades seguem o Processo-Padrão Organizacional (PRO-GPC-001) e suas adaptações (GUIA-GPC-001).
- **Conformidade da documentação:** se os produtos de trabalho documentais exigidos pelo processo existem, estão completos e seguem os padrões da organização.

A GQA **não avalia a qualidade técnica interna do código-fonte** — essa responsabilidade pertence às atividades de Verificação e Validação (revisão por pares e testes do QA). Como insumo para a melhoria de processos, a GQA pode observar indicadores como número de defeitos e retrabalho, utilizando-os para identificar ajustes necessários no processo, e não como auditoria técnica do produto.

## 3. Responsável e independência

A GQA é exercida por **membros do Time de Melhoria Contínua, em regime de rodízio**.

A objetividade da verificação é assegurada pela **independência entre quem audita e quem executa**:

- o responsável pela verificação de um projeto **não pode ter atuado na execução** daquele projeto;
- a verificação é conduzida por **auditor externo à equipe avaliada**;
- o rodízio entre os membros do Time de Melhoria Contínua distribui as verificações e evita que a mesma pessoa audite continuamente o mesmo time.

No caso específico da verificação dos ativos produzidos pelo próprio Time de Melhoria Contínua, o responsável pela auditoria não deve ser o autor do ativo avaliado.

## 4. Momentos e frequência das verificações

A verificação segue um modelo **híbrido**, combinando verificação por marcos e verificação por amostragem.

### 4.1. Verificação por marcos do processo

A cada ponto de controle do processo-padrão, verifica-se a aderência correspondente:

| Marco | O que é verificado |
|---|---|
| Abertura (Kickoff gerencial) | Termo de Abertura registrado; equipe designada; ata de kickoff. |
| Discovery / Requisitos | Requisitos especificados e validados; rastreabilidade estabelecida. |
| Concepção | Design avaliado; quando aplicável, protótipo aceito pelo cliente; estimativas concluídas. |
| Aprovação do Plano | Plano de Projeto aprovado pelo cliente; aceite registrado em ata; baseline estabelecida. |
| Desenvolvimento | Definição de Pronto sendo aplicada (critérios de aceite, code review, testes do QA); change requests tratados. |
| Homologação / Entrega | Aprovação do cliente registrada antes da promoção para produção. |
| Encerramento | Termo de Aceite e lições aprendidas registrados. |

### 4.2. Verificação por amostragem

Periodicamente, ao longo das sprints, a GQA verifica uma **amostra** de produtos de trabalho (por exemplo, histórias quanto a critérios de aceite, evidência de revisão por pares e de testes), de forma a acompanhar a aderência continuamente sem auditar a totalidade dos itens.

### 4.3. Planejamento

As verificações são planejadas no início do projeto (como parte do planejamento do projeto) e os registros são produzidos nas ocasiões planejadas, evidenciando o acompanhamento ao longo de todo o ciclo de vida — e não apenas ao final.

## 5. Registro, comunicação e tratamento dos achados

- Os achados das verificações são registrados em **documento de verificação da qualidade**, mantido no Confluence.
- Cada achado indica: o que foi verificado, o desvio encontrado (se houver), a severidade e a recomendação.
- Os achados são comunicados aos responsáveis pela atividade verificada.
- Quando um achado demanda correção, a ação corretiva é acompanhada como **item rastreável** (registrada no Jira quando se torna tarefa), até sua conclusão.

## 6. Escalonamento de impasses

Quando um desvio identificado pela GQA **não é corrigido** pelos responsáveis, ou quando há **desacordo** sobre o achado, aplica-se o escalonamento:

1. **Nível 1 — Equipe do projeto:** a GQA trata o achado diretamente com a equipe e o gerente do projeto.
2. **Nível 2 — Time de Melhoria Contínua:** desvios não resolvidos no projeto são levados ao Time de Melhoria Contínua.
3. **Nível 3 — COO (Operações):** impasses que permanecem sem resolução são escalados ao COO, responsável operacional pelos processos, que decide. Casos de natureza estratégica são reportados pelo COO ao CEO.

Este caminho garante que a GQA tenha autoridade efetiva, independentemente de quem é auditado.

## 7. Contribuição para a melhoria de processos

A GQA é uma fonte de oportunidades de melhoria. Desvios recorrentes, dificuldades de aderência e indicadores de defeitos e retrabalho observados durante as verificações são encaminhados ao Time de Melhoria Contínua como insumo para o aprimoramento do processo-padrão (alimentando a Gerência de Processos — GPC — e a Medição — MED).

## 8. Documentos relacionados

- POL-ORG-001 — Política Organizacional de Processos
- PRO-GPC-001 — Processo-Padrão Organizacional
- GUIA-GPC-001 — Guia de Adaptação do Processo-Padrão
- Processo de Verificação e Validação (VV)
- Plano de Medição (MED)
- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento

## 9. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde ao resultado **GPC 3** do processo **Gerência de Processos (GPC)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| GPC 3 — estratégia e plano de garantia da qualidade, com verificação de aderência ao processo e avaliação de produtos de trabalho por função independente | Seções 1 a 7 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 12/08/2025 | Time de Melhoria Contínua | Definição inicial da estratégia de garantia da qualidade de processo |
| 1.1 | 21/11/2025 | Time de Melhoria Contínua | Ajuste do escalonamento de impasses para o COO (estrutura organizacional) |
| 1.2 | 17/12/2025 | Time de Melhoria Contínua | Atualização dos marcos de verificação conforme o novo fluxo (kickoff gerencial, concepção, aprovação do plano) |
