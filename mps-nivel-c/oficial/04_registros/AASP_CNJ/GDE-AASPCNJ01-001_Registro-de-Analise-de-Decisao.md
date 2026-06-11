# Registro de Análise de Decisão (RAD) — AASP_CNJ · Fonte primária de captura

| Campo | Valor |
|---|---|
| **Documento** | GDE-AASPCNJ01-001 |
| **Projeto / contexto** | AASP_CNJ — WorkerAndamentos |
| **Data** | 06/04/2026 |
| **Responsável pela decisão** | Gerente de Projeto / Tech Lead (com o time de desenvolvimento) |

---

## 1. Problema / decisão a tomar

Definir a fonte primária de captura de andamentos processuais que substituiria o modelo anterior (web scrapers frágeis e APIs privadas pagas, com custo de ~R$ 16.500/mês e cobertura incompleta).

## 2. Gatilho

Escolha de tecnologia/fornecedor de alto impacto financeiro e operacional, com efeito na arquitetura de captura — atinge os gatilhos do PRO-GDE-001 (tecnologia/fornecedor e alto impacto).

## 3. Alternativas consideradas

| # | Alternativa | Descrição |
|---|---|---|
| A | Manter APIs privadas (Solucionário/Botmax) | Continuar a captura por fornecedores pagos, com custo por instância e cobertura parcial |
| B | Crawler próprio universal | Estender o engine EPROC/ESAJ para todos os tribunais |
| C | API DataJud/CNJ como fonte primária | Fonte oficial, gratuita por baixo custo, padronizada e de cobertura nacional |

## 4. Critérios de avaliação

| Critério | Peso |
|---|---|
| Custo por captura | 3 |
| Cobertura de tribunais | 3 |
| Padronização do modelo de dados | 2 |
| Manutenibilidade / estabilidade | 2 |
| Risco de indisponibilidade | 2 |

## 5. Avaliação (matriz de decisão)

Escala 1–3 por critério (3 = melhor atende). Pontuação ponderada pelo peso.

| Critério | Peso | Alt. A (privadas) | Alt. B (crawler universal) | Alt. C (CNJ) |
|---|---|---|---|---|
| Custo por captura | 3 | 1 | 2 | 3 |
| Cobertura de tribunais | 3 | 2 | 2 | 3 |
| Padronização | 2 | 2 | 1 | 3 |
| Manutenibilidade | 2 | 2 | 1 | 3 |
| Risco de indisponibilidade | 2 | 2 | 2 | 2 |
| **Total ponderado** | | **20** | **19** | **35** |

## 6. Decisão e justificativa

Escolhida a **Alternativa C — API DataJud/CNJ como fonte primária universal**. Reúne cobertura nacional com um único endpoint padronizado, custo de R$ 0,01/processo (vs. R$ 0,03/instância da principal privada) e modelo de dados uniforme, simplificando a serialização para o Elasticsearch. Economia projetada de ~R$ 180 mil anuais. As fontes EPROC/ESAJ e parceiras permanecem como fallback configurável por `CodigoFonteAPI`.

## 7. Riscos associados à decisão

| Risco | Resposta |
|---|---|
| Indisponibilidade/alteração da API CNJ | Manter EPROC/ESAJ e parceiras como fallback configurável |
| CNJ não cobre processos em segredo de justiça | Fallback obrigatório por instância (EPROC/ESAJ ou parceiras com credencial) |

## 8. Premissas (para revisão futura)

- A API DataJud/CNJ permanece disponível com a cobertura declarada.
- O custo de R$ 0,01/processo se mantém conforme contratado.

---

## Anexo — Registro consolidado de decisões do projeto

| # | Data | Decisão | Justificativa |
|---|---|---|---|
| D01 | Out/2025 | Desenvolver engine nativo EPROC/ESAJ para o TJSP | Eliminar dependência de APIs privadas no maior tribunal e reduzir custo no maior volume |
| D02 | Abr/2026 | Adotar a API DataJud/CNJ como fonte primária universal | Cobertura universal, custo reduzido e padronização (RAD detalhado acima) |
| D03 | Abr/2026 | Unificar a fila RabbitMQ para todos os tribunais | Elimina código duplicado e simplifica o roteamento e o escalonamento |
| D04 | Abr/2026 | Armazenar o token Bearer CNJ de forma compartilhada (`PonteAPI`) | Evitar renovações paralelas e condições de corrida entre workers |
| D05 | Abr/2026 | Tratar o JSON da API CNJ no worker (não na API) | Worker entrega `IModelElastic` pronto, simplificando a API AndamentosProcessuais |
| D06 | Mai/2026 | Pausar o desenvolvimento da captura de 2ª instância EPROC | Priorização acordada com o cliente para focar na integração CNJ (ver CR-AASPCNJ01-001) |
| D07 | Mai/2026 | Controlar segredo de justiça por instância (campo `Segredo`) | Um processo pode estar em segredo em uma instância e não em outra |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | RAD da fonte primária de captura (D02) + registro consolidado de decisões, a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
