# Processo de Gerência de Decisões — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-GDE-001 — Processo de Gerência de Decisões |
| **Versão** | 1.0 |
| **Data** | `<dd/mm/aaaa>` |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Processos MPS-SW relacionados** | GDE 1 a GDE 6 |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware conduz **decisões relevantes** de forma estruturada — com análise de alternativas e critérios objetivos —, garantindo que escolhas de alto impacto sejam fundamentadas, registradas e rastreáveis, em vez de tomadas apenas por intuição ou conveniência do momento.

> **Mapa de resultados atendidos neste documento:**
> - Seção 3 → **GDE 1** (diretrizes de quando aplicar decisão formal)
> - Seção 4 → **GDE 2 a GDE 6** (problema, alternativas, critérios, avaliação e decisão)
> - Seção 5 → registro e rastreabilidade da decisão

## 2. Princípio

Nem toda decisão exige análise formal. Aplicar o processo a escolhas triviais geraria burocracia desnecessária. Por isso, a Timeware define **gatilhos** (seção 3) que determinam quando uma decisão merece o tratamento formal descrito neste documento. Decisões fora desses gatilhos seguem o curso normal do trabalho.

## 3. Quando aplicar decisão formal — gatilhos (GDE 1)

Uma decisão deve seguir o processo formal quando atende a **pelo menos um** dos gatilhos abaixo:

| Gatilho | Exemplos |
|---|---|
| **Decisão de arquitetura ou técnica relevante** | Escolha de padrão arquitetural, estrutura de dados estruturante, estratégia de integração. |
| **Escolha de tecnologia, ferramenta ou fornecedor** | Adoção de framework, linguagem, serviço de terceiro, plataforma. |
| **Alto impacto, risco ou custo** | Decisão que afeta significativamente prazo, custo, qualidade ou que carrega risco elevado. |
| **Irreversibilidade** | Decisão difícil ou custosa de reverter depois de tomada. |

Quando uma decisão **não** atende a nenhum gatilho, ela é tomada no fluxo normal, sem necessidade de registro formal — cabendo ao Gerente de Projeto ou Tech Lead o bom senso de elevar ao processo formal um caso limítrofe.

## 4. Como conduzir a decisão formal (GDE 2 a GDE 6)

O processo formal segue seis passos:

1. **Definir o problema/decisão (GDE 2):** descrever claramente o que precisa ser decidido e o contexto.
2. **Levantar alternativas (GDE 3):** identificar as opções viáveis (no mínimo duas), evitando decidir sobre uma única opção.
3. **Definir critérios de avaliação (GDE 4):** estabelecer os critérios e seus pesos (por exemplo: custo, prazo, complexidade, risco, aderência ao requisito, manutenibilidade).
4. **Definir o método de avaliação (GDE 5):** como as alternativas serão comparadas (por exemplo, matriz de decisão pontuando cada alternativa em cada critério).
5. **Avaliar as alternativas (GDE 6):** aplicar o método, comparar os resultados e identificar a alternativa recomendada.
6. **Decidir e registrar:** tomar a decisão, registrar a justificativa e comunicar aos envolvidos.

## 5. Registro de Análise de Decisão (RAD)

Cada decisão formal é documentada em um **Registro de Análise de Decisão (RAD)**, mantido no Confluence, contendo:

- identificação e data da decisão;
- problema/decisão e contexto;
- gatilho que motivou a análise formal;
- alternativas consideradas;
- critérios de avaliação e pesos;
- método e resultado da avaliação (matriz de decisão);
- decisão tomada e justificativa;
- responsável pela decisão.

### Diferenciais adotados pela Timeware

Além do registro padrão, a Timeware incorpora dois elementos que aumentam o valor do RAD:

- **Vínculo com riscos:** cada decisão formal identifica os riscos associados à alternativa escolhida, que são registrados e tratados conforme a Estratégia de Gerência de Riscos (EST-GPC-002). Assim, a decisão não termina na escolha — ela alimenta a gestão de riscos.
- **Revisão da decisão:** o RAD registra as premissas que sustentaram a decisão. Quando o contexto do projeto muda de forma que invalide uma premissa relevante, a decisão é reaberta e reavaliada, evitando que escolhas baseadas em premissas superadas permaneçam vigentes.

## 6. Papéis

| Papel | Responsabilidade |
|---|---|
| **Tech Lead / Arquiteto** | Conduzem decisões técnicas e de arquitetura formais. |
| **Gerente de Projeto** | Identifica decisões que atingem os gatilhos; garante o registro. |
| **Product Owner** | Participa de decisões que afetam escopo e produto. |
| **COO (Operações)** | Participa de decisões de alto impacto organizacional. |

## 7. Documentos relacionados

- PRO-GPC-001 — Processo-Padrão Organizacional
- EST-GPC-002 — Estratégia de Gerência de Riscos e Oportunidades
- Processo de Projeto e Construção do Produto (PCP)
- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Definição inicial do processo de gerência de decisões |
