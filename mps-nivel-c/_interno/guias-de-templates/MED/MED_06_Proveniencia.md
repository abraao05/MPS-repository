# Tabela de Proveniência — Medição

> Origens: **[GSD]** / **[Jira]** / **[Manual]** / **[Derivado]**. **(confirmado)** comprovado no diagnóstico; **(hipótese)** depende da Timeware.

## Plano de Medição
| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| 1. Objetivos de medição | [Manual] | gatilho à liderança (derivam de objetivos de NEGÓCIO — não existem em ferramenta) | confirmado |
| 2. Medidas selecionadas | [Manual] | ligação objetivo→medida, definida no processo | confirmado |
| 3. Análise de desempenho | [Derivado] | calculada sobre os dados do Repositório | confirmado |
| 4. Ações corretivas | [GSD]+[Manual] | `RETROSPECTIVE` (lições) + decisão gerencial | confirmado |
| 5. Comunicação | [Manual] | gatilho (definição de público/frequência/meio) | confirmado |

## Repositório de Medidas
| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| 2. Definições operacionais | [Manual] | texto-padrão (definido uma vez por medida) | confirmado |
| 2. Referências de mercado | [Manual] | benchmarks pesquisados (DORA, consenso de cobertura) — embutidos no documento | confirmado |
| 3. Dado: velocidade | [Jira]+[Derivado] | pontos concluídos (Jira) ÷ período | hipótese (depende do Jira) |
| 3. Dado: lead time | [GSD] | timestamps de commit (Git) → deploy | confirmado |
| 3. Dado: cobertura | [GSD] | ferramenta de cobertura no build | confirmado |
| 3. Dado: taxa de falha | [GSD] | regressões/correções nos registros de fase + commits de fix | confirmado |
| 4. Garantia de qualidade | [Manual]+[GSD] | procedimento manual + automação de coleta | confirmado |
