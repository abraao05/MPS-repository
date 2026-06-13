# Repositório Organizacional de Medidas

> **O que é este documento.** O repositório consolidado das medidas da organização: para cada medida, sua definição operacional completa, os valores de referência (de mercado, no início; próprios, conforme amadurece) e os dados coletados ao longo do tempo. É a fonte única contra a qual o desempenho é analisado e contra a qual projetos estimam.
>
> **Como usar.** As definições operacionais (seção 2) são estáveis. Os dados coletados (seção 3) crescem a cada projeto/período. Os valores de referência (seção 2, coluna "Referência") começam com benchmark de mercado e são **substituídos** pelos dados próprios da organização assim que houver histórico suficiente.

---

## 1. Aviso sobre os valores de referência *(ler antes de usar)*

Os valores de referência abaixo vêm de benchmarks de mercado publicados e servem como **ponto de partida provisório** enquanto a Timeware não tem histórico próprio. Três ressalvas honestas, para não tirar conclusão errada:

1. **Benchmark de mercado não é meta nem nota.** É um ponto de orientação. A referência verdadeira da Timeware nasce dos seus próprios dados (seção 3), acumulados projeto a projeto.
2. **Velocidade (story points) NÃO tem benchmark de mercado válido.** Story points são relativos a cada equipe — "X pontos por período" não significa nada fora do time que pontuou. Por isso a velocidade entra **sem referência externa**; sua referência só pode vir dos dados próprios.
3. **As referências de entrega (lead time, taxa de falha) seguem o DORA**, que é explícito: esses números servem para acompanhar a **própria evolução** ao longo do tempo, não para comparar equipes entre si nem como ranking. Os limiares do DORA mudam ano a ano (são derivados por análise de cluster), então são orientação, não lei.

---

## 2. Medidas e definições operacionais

> **Definição operacional (item requerido)** deve conter, para cada medida: nome; objetivo relacionado; fórmula de cálculo; medidas básicas (se derivada); forma/momento/responsável da coleta; forma de armazenamento; procedimento/responsável da análise.

### Medida 1 — Velocidade da equipe

| Campo | Conteúdo |
|---|---|
| **Nome** | Velocidade (pontos entregues por período) |
| **Objetivo relacionado** | Apoiar a estimativa de prazo e a alocação (derivar esforço/duração da dimensão) |
| **Fórmula** | soma dos story points das histórias concluídas ÷ duração do período (ex.: por sprint) |
| **Medidas básicas** | story points concluídos; duração do período |
| **Coleta** | ao fim de cada período/fase; responsável: gestor do projeto; fonte: rastreador de tarefas |
| **Armazenamento** | seção 3 deste repositório, por projeto e período |
| **Análise** | tendência da própria equipe ao longo do tempo; responsável: gestor |
| **Referência** | **Sem benchmark de mercado** (medida relativa à equipe — ver aviso 2). Referência = média móvel dos próprios dados da Timeware |

### Medida 2 — Lead time (duração commit → produção)

| Campo | Conteúdo |
|---|---|
| **Nome** | Lead time de mudança |
| **Objetivo relacionado** | Medir a agilidade de entrega de valor ao usuário |
| **Fórmula** | tempo decorrido do primeiro commit de uma mudança até ela estar em produção |
| **Medidas básicas** | data/hora do commit; data/hora do deploy em produção |
| **Coleta** | por mudança/entrega; responsável: automatizável a partir do histórico Git + deploy |
| **Armazenamento** | seção 3, por projeto |
| **Análise** | distribuição e tendência; responsável: gestor |
| **Referência (DORA, orientação)** | Elite: menos de 1 dia · Alto: entre 1 dia e 1 semana · Médio: 1 semana a 1 mês · Baixo: acima de 1 mês. *Usar para acompanhar a própria evolução, não para ranking.* |

### Medida 3 — Cobertura de testes

| Campo | Conteúdo |
|---|---|
| **Nome** | Cobertura de testes |
| **Objetivo relacionado** | Indicar o grau de exercício do código pelos testes (apoio à qualidade) |
| **Fórmula** | linhas/branches de código exercitadas pelos testes ÷ total, em % |
| **Medidas básicas** | linhas cobertas; linhas totais |
| **Coleta** | a cada build; responsável: automatizável pela ferramenta de cobertura |
| **Armazenamento** | seção 3, por projeto |
| **Análise** | nível atual e tendência; responsável: dev/gestor |
| **Referência (mercado)** | ~80% é o consenso de mercado. Referências citadas: Google trata 60% aceitável, 75% bom, 90% exemplar; 70–80% é meta razoável para a maioria dos projetos. *Cobertura alta não garante teste bom — é indicador, não prova de qualidade.* |

### Medida 4 — Taxa de defeitos / falhas

| Campo | Conteúdo |
|---|---|
| **Nome** | Taxa de falha de mudança (proxy de defeitos) |
| **Objetivo relacionado** | Indicar a estabilidade das entregas |
| **Fórmula** | nº de mudanças que causaram falha/necessitaram correção ÷ total de mudanças, em % |
| **Medidas básicas** | mudanças com falha; total de mudanças |
| **Coleta** | por período; responsável: gestor; fonte: registros de correção/regressão |
| **Armazenamento** | seção 3, por projeto |
| **Análise** | tendência; responsável: gestor |
| **Referência (DORA, orientação)** | Elite: menos de 5% · Alto: menos de 15%. **Ressalva:** a "taxa de regressões por fase" que se coleta hoje é uma definição *próxima*, não idêntica, ao change failure rate do DORA — ao consolidar, padronizar a definição. |

---

## 3. Dados coletados *(cresce a cada projeto/período)*

> Aqui ficam os dados reais. Conforme preenche, a média própria da Timeware substitui o benchmark de mercado como referência.

| Projeto | Período | Velocidade | Lead time | Cobertura | Taxa de falha |
|---|---|---|---|---|---|
| `[preencher]` | | | | | |

---

## 4. Garantia de qualidade das medidas *(nível C — MED 3, MED 7)*

> As medidas coletadas precisam ser verificadas (acurácia, precisão, completeza) antes de usar, e o repositório é avaliado periodicamente.

- **Como cada medida é verificada antes de entrar:** `[preencher — ex.: conferência de que o dado está completo e veio da fonte correta]`
- **Procedimento de avaliação periódica do repositório:** `[preencher — quando e como se confere a qualidade dos dados acumulados]`
- **Automação como garantia de qualidade:** coleta automatizada (Git, ferramenta de cobertura, deploy) reduz erro de coleta e é a forma recomendada de assegurar qualidade — priorizar onde possível.
