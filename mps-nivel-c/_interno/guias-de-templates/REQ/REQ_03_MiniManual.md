# Mini-manual — Especificação de Requisitos

**O que é.** O processo que define, organiza e mantém os requisitos do produto — desde a necessidade crua da parte interessada até o requisito especificado, priorizado e rastreável à implementação.

**O que ele garante (o que "mede").** Que (1) as necessidades certas foram ouvidas das pessoas certas, (2) viraram requisitos claros e priorizados, (3) há rastreabilidade nos dois sentidos entre requisito e implementação, e (4) inconsistências entre requisitos, planos e produto são detectadas e tratadas. Não é uma métrica numérica — é cobertura e consistência: todo requisito tem origem, e toda implementação tem requisito.

**Por que fazer.** Requisito mal levantado ou perdido é a causa mais cara de retrabalho: descobre-se tarde, quando já se construiu a coisa errada. A rastreabilidade bidirecional é o que permite, a qualquer momento, perguntar "por que isto existe?" (do código ao requisito) e "isto foi construído?" (do requisito ao código) — e detectar órfãos antes que virem problema.

**Como usar no dia a dia.**
1. Levante necessidades das partes interessadas (seção 1–2 do documento).
2. Transforme em requisitos com ID, prioridade e alocação (seção 3).
3. Obtenha o compromisso de quem vai construir (seção 4).
4. Mantenha a rastreabilidade viva: cada implementação cita o ID do requisito (seção 5).
5. A cada mudança de requisito, gere nova versão e registre o que mudou.
6. Periodicamente, rode a verificação de órfãos — é o que mantém o documento honesto.

**Erro comum a evitar.** Tratar a rastreabilidade como burocracia preenchida no fim. Ela só funciona se for mantida durante a construção (o ID do requisito viaja com a tarefa e o commit), não reconstruída depois.
