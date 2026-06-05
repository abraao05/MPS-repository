# Repositório Organizacional de Medidas

> **Modelo de preenchimento** com base no Trainer Connect. Os dados da seção 3 vêm do diagnóstico (durações de fase, ~63 arquivos de teste / ~600 casos, regressões corrigidas, velocidade da retrospectiva). Onde o dado exato não estava no diagnóstico, marcamos *(exemplo)*. Os valores de referência são os benchmarks pesquisados.

---

## 1. Aviso sobre os valores de referência
(idêntico ao template — benchmark é ponto de partida; velocidade não tem benchmark externo; referências DORA servem para acompanhar a própria evolução, não para ranking.)

---

## 2. Medidas e definições operacionais
(as quatro definições operacionais são as mesmas do template; abaixo, os valores observados no Trainer Connect.)

| Medida | Definição (resumo) | Referência | Observado no Trainer Connect |
|---|---|---|---|
| Velocidade | pontos concluídos ÷ período | sem benchmark externo | ~11 pontos/semana (retrospectiva); planejado ~12 |
| Lead time | commit → produção | DORA elite < 1 dia | deploy automático a cada push aprovado — lead time tipicamente < 1 dia *(consistente com faixa elite)* |
| Cobertura | linhas cobertas ÷ total | mercado ~80% | ~63 arquivos de teste / ~600 casos; % exata não medida formalmente no projeto solo *(lacuna: medir e registrar a %)* |
| Taxa de falha | mudanças com falha ÷ total | DORA elite < 5%, alto < 15% | 11 regressões numa fase, corrigidas antes do release *(exemplo de cálculo: 11 ÷ total de mudanças da fase)* |

---

## 3. Dados coletados

| Projeto | Período | Velocidade | Lead time | Cobertura | Taxa de falha |
|---|---|---|---|---|---|
| Trainer Connect | Fase Fundação | ~12 pts/sem | < 1 dia | não medida | baixa |
| Trainer Connect | Fase Treinos | ~10 pts/sem | < 1 dia | não medida | regressões pontuais |
| Trainer Connect | Fase Execução | ~11 pts/sem | < 1 dia | ~78% *(exemplo)* | ~3% *(exemplo)* |

> *Observação honesta: o projeto solo coletava esses dados de forma descritiva (durações, contagem de testes), não como medidas com definição operacional. Este repositório é justamente o passo que faltava — transformar dados soltos em medidas definidas e consolidadas.*

---

## 4. Garantia de qualidade das medidas

- **Verificação antes de entrar:** conferir que o dado de velocidade corresponde às histórias realmente concluídas (não em andamento); que a cobertura veio da ferramenta no build da versão entregue; que a taxa de falha conta só mudanças que foram a produção.
- **Avaliação periódica:** a cada fechamento de milestone, revisar a consistência dos dados acumulados.
- **Automação:** lead time, cobertura e contagem de mudanças são coletáveis automaticamente (Git, ferramenta de cobertura, deploy) — priorizar a automação como garantia de qualidade.
