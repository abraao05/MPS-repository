# Registro de Medição — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | MED-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | MED (evidência de projeto) |

---

## 1. Objetivo

Registrar as medidas coletadas ao longo do projeto, conforme o PLA-MED-001, para apoiar a análise de custo, prazo, qualidade e estabilidade da operação de captura. As medidas abrangem os projetos correlatos id 213 (EPROC/ESAJ) e id 256 (CNJ).

## 2. Indicadores do projeto

| Indicador | Meta | Resultado |
|---|---|---|
| Redução de custo mensal de captura | ≥ R$ 12.500/mês | Economia estimada de ~R$ 15.000/mês após migração completa para a API CNJ |
| Economia anual projetada | ≥ R$ 150.000/ano | ~R$ 180.000/ano (base: volume atual de 550 mil instâncias) |
| Cobertura de tribunais | Todos os cobertos pelo CNJ | Cobertura universal via DataJud para processos de consulta pública |
| Estabilidade da fila | Zero travamentos manuais/mês | Travamento corrigido na Fase 4; monitoramento ativo implantado |
| Aderência ao prazo de desenvolvimento | Entrega até 02/05/2026 | Desenvolvimento concluído em 01/06/2026 (atraso de ~30 dias por escopo adicional acordado) |

## 3. Medidas de esforço (prazo/progresso)

| Fase | Esforço estimado (h) | Esforço realizado (h) | Responsável principal |
|---|---|---|---|
| Fase 1 — Análise e Arquitetura | 60 | ~80 | Cézar / Abraão Oliveira |
| Fase 2 — Desenvolvimento EPROC/ESAJ | 120 | ~124 | Raony |
| Fase 3 — Estabilização EPROC/ESAJ | 80 | ~93 | Raony |
| Fase 4 — Desenvolvimento CNJ | 200 | ~195 | Raony / Levi |
| Fase 5 — Testes e Validação | 80 | ~109 | Raony / Jonatan |
| Fase 6 — Implantação (parcial) | 46 | Em apuração (~23 h) | Raony / Abraão Oliveira |
| **Total** | **586** | **~624 (parcial)** | |

## 4. Resultado financeiro da migração

| Modelo | Custo unitário | Volume (instâncias/mês) | Custo mensal |
|---|---|---|---|
| API Solucionário (anterior) | R$ 0,03 / instância | 550.000 instâncias | R$ 16.500 |
| API DataJud/CNJ (novo) | R$ 0,01 / processo | ~183.000 processos | R$ 1.830 |
| **Economia mensal projetada** | — | — | **R$ 14.670** |
| **Economia anual projetada** | — | — | **R$ 176.040** |

> Nota: a diferença entre os ~R$ 180.000 citados nos alinhamentos e o valor calculado decorre do modelo de cobrança — a Solucionário cobra por instância (uma por grau), enquanto a CNJ cobra por processo. Para ~183 mil processos com média de 3 instâncias, o custo anterior seria 550 mil × R$ 0,03 = R$ 16.500/mês.

## 5. Análise de variâncias

| Variância | Magnitude | Causa-raiz |
|---|---|---|
| Esforço realizado acima do estimado em Fases 1, 3 e 5 | Média | Estudo do captcha Cloudflare mais longo (Fase 1); estabilização e testes além do previsto |
| Atraso de ~30 dias na conclusão do desenvolvimento | Média | Escopo adicional acordado (segredo de justiça por instância, ajustes de fallback e de cadastro nas parceiras) |

O atraso é explicado por escopo adicional acordado com o cliente, não por desvio de produtividade. As metas de custo, cobertura e estabilidade foram atingidas.

## 6. Comunicação dos resultados

Conforme PLA-MED-001 §7, os resultados foram comunicados nas reuniões de alinhamento (ver ATA-AASPCNJ01-001 e GQA-AASPCNJ01-001) e nas devolutivas aos associados sobre o resultado da solução EPROC/ESAJ em produção (jan–fev/2026). A consolidação de encerramento será registrada no fechamento do projeto.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de medição consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
