# Plano de Medição

> **Modelo de preenchimento** com base no Trainer Connect. **Importante:** os objetivos de medição (seção 1) são *exemplos plausíveis* — na Timeware, devem ser substituídos pelos objetivos de negócio reais definidos pela liderança. A medição não tem valor se os objetivos forem fictícios.

---

## 0. Identificação

| Campo | Valor |
|---|---|
| Organização | Timeware *(exemplo)* |
| Versão | v1 |
| Data | 2026-06-02 |
| Responsável | *(exemplo: liderança)* |

---

## 1. Objetivos de medição e de desempenho *(exemplos — substituir pelos reais)*

| Objetivo de negócio | Necessidade de informação | Objetivo de medição | Medida(s) |
|---|---|---|---|
| Entregar projetos no prazo acordado com o cliente | Quão previsível é nossa entrega? | Acompanhar prazo estimado vs. real e a estabilidade da velocidade | velocidade, lead time |
| Reduzir retrabalho e defeitos em produção | Quanto retrabalho geramos? | Acompanhar taxa de falha e cobertura de testes | taxa de defeitos, cobertura |

---

## 2. Medidas selecionadas
(as quatro medidas do Repositório, ligadas aos objetivos acima.)

| Medida | Objetivo que atende | Definição em |
|---|---|---|
| Velocidade | previsibilidade | Repositório, Medida 1 |
| Lead time | agilidade | Repositório, Medida 2 |
| Cobertura | qualidade | Repositório, Medida 3 |
| Taxa de defeitos | estabilidade | Repositório, Medida 4 |

---

## 3. Análise de desempenho organizacional

- **Quando:** ao fechamento de cada milestone e consolidação trimestral.
- **Como:** comparar a velocidade e a taxa de falha do Trainer Connect ao longo das fases; identificar que a fase Treinos teve esforço acima do estimado (subestimação da complexidade da biblioteca).
- **Necessidades de melhoria:** melhorar a estimativa de fases com componente de biblioteca; medir a cobertura formalmente (hoje não é registrada como %).

---

## 4. Ações corretivas

| Achado | Ação | Responsável | Situação |
|---|---|---|---|
| Esforço da fase Treinos acima do estimado | Ajustar esforço-por-ponto na referência; revisar estimativa de fases similares | Gestor | Concluída |
| Cobertura não medida formalmente | Passar a registrar a % de cobertura a cada build | Dev | Aberta |

---

## 5. Comunicação dos resultados

- **Para quem:** equipe e liderança.
- **Frequência:** a cada fechamento de milestone (resumo) e consolidação trimestral.
- **Meio:** página no espaço da organização (Confluence) com o painel das quatro medidas.
