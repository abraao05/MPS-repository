# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Registro de Capacitação da Equipe
**Código:** CAP-AASP01-001
**Versão auditada:** 1.1
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 0 | 2 | 1 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 1 | 0 | 0 |
| Coerência (CON) | 0 | 0 | 0 | 0 |
| MPS.BR (MPS) | 0 | 1 | 0 | 0 |
| **TOTAL** | **0** | **2** | **2** | **1** |

**Veredicto:** NÃO-CONFORME

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-CAP-01 — Avaliação de competências é binária (✅/ausente) sem critério de avaliação documentado
**Severidade:** 🟡 Moderada
**RAP impactado:** CAP RAP 2 — avaliação de necessidades de capacitação com critério definido
**Localização:** Seção 3 — Matriz de competências da equipe
**Problema:** A matriz de competências usa apenas "✅ competência atendida" sem descrever como a competência foi avaliada (entrevista, prova, experiência prévia verificada, certificado). O MPS.BR CAP exige que a identificação de necessidades de treinamento seja baseada em avaliação com critério, não apenas autodeclaração ou avaliação do GP.
**Evidência:** > "Desenvolvedor | Renan Kiyoshi | C-01, C-02, C-05, C-06 | ✅"
**Referência normativa:** CAP RAP 2 — as necessidades de treinamento devem ser identificadas com base em avaliação das competências existentes vs. requeridas.
**Ação corretiva:** Adicionar coluna "Critério de avaliação" à matriz: ex. "Experiência comprovada em projetos anteriores (ms.auxo.notificacoes)", "Avaliação técnica na contratação", "Trabalho anterior no Gerenciador AASP".

---

### NC-CAP-02 — Ação de capacitação C-04 ("sessão técnica de alinhamento") sem evidência de realização
**Severidade:** 🟡 Moderada
**RAP impactado:** CAP RAP 3 — ações de capacitação realizadas e eficácia avaliada
**Localização:** Seção 4 — Ações de capacitação
**Problema:** A única ação de capacitação registrada é uma "Sessão técnica de alinhamento no início da Sprint 2 (09/06/2026)". O status é "Realizada (09/06/2026)", mas não há evidência desta realização (ata, registro de presença, material apresentado). O ADAP-AASP01-001 menciona que "o contrato de API do ms.temis.vinculos foi disponibilizado pelo time do cliente somente no início da Sprint 2", o que é consistente, mas a sessão técnica em si não tem documentação.
**Evidência:** > "Alinhamento do contrato de API do ms.temis.vinculos (C-04) | Sessão técnica de alinhamento no início da Sprint 2, com o time do cliente | Realizada (09/06/2026)"
**Referência normativa:** CAP RAP 3 — execução das ações de treinamento deve ser registrada com evidência.
**Ação corretiva:** Registrar evidência da sessão de alinhamento: participantes, duração, resultado (contrato de API recebido e entendido). Pode ser um parágrafo na própria seção 4 ou referência a uma ata de reunião.

---

### NC-CAP-03 — Abraão Oliveira aparece com nome completo mas nos outros documentos apenas como "Abraão"
**Severidade:** 🟢 Leve
**RAP impactado:** Coerência interna
**Localização:** Cabeçalho — Responsável; Seção 3 — Matriz
**Problema:** Este é o único documento que registra "Abraão Oliveira" como nome completo do GP. Todos os demais documentos usam apenas "Abraão". A inconsistência de nomenclatura é leve mas cria ambiguidade na identificação do responsável.
**Evidência:** > "Responsável | Abraão Oliveira (Gerente de Projeto)"
**Referência normativa:** Consistência de identificação de partes em documentos.
**Ação corretiva:** Padronizar o nome do GP como "Abraão Oliveira" em todos os documentos do projeto (ou usar apenas o prenome por decisão da equipe — mas de forma consistente).

---

### NC-CAP-04 — Avaliação de eficácia diferida sem critério de dispensa claro
**Severidade:** 🟢 Leve
**RAP impactado:** CAP RAP 4 — eficácia avaliada
**Localização:** Seção 4 — nota final
**Problema:** O documento dispensa a avaliação de eficácia citando "GUIA-GPC-001, §7.2". Esta referência não está disponível para verificação no pacote documental auditado. A dispensa de avaliação de eficácia é aceitável para treinamentos de curta duração, mas a referência normativa interna deve estar acessível ao avaliador.
**Evidência:** > "Para ações de curta duração e baixo impacto, a avaliação formal de eficácia é dispensável (GUIA-GPC-001, §7.2)."
**Referência normativa:** CAP RAP 4 — avaliação de eficácia requerida.
**Ação corretiva:** Incluir o GUIA-GPC-001 no pacote documental de referência do projeto, ou transcrever o critério de dispensa diretamente no documento CAP.

---

### NC-CAP-05 — "Time de Melhoria Contínua" sem identificação nominal
**Severidade:** 🔵 Obs
**RAP impactado:** GCO RAP 2
**Localização:** Histórico de Revisões — versão 1.1
**Problema:** Problema sistêmico de todos os documentos com revisão v1.1.
**Evidência:** > "1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação..."
**Referência normativa:** GCO RAP 2.
**Ação corretiva:** Identificar o responsável nominal.
