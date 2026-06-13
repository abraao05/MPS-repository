# Mini-manual — Verificação e Validação

**O que é.** O processo que confirma duas coisas distintas: **verificação** — o produto atende à especificação (construímos certo)? — feita por testes **e** revisão por pares; e **validação** — o produto serve ao uso real pretendido (construímos a coisa certa)?

**O que ele garante.** Que os entregáveis selecionados foram testados e revisados por um par (pessoa com conhecimento equivalente ou superior), que métodos/critérios/ambientes estão definidos, que problemas encontrados foram tratados, e que os resultados foram analisados, registrados e comunicados.

**Por que fazer.** Teste sozinho pega o que você pensou em testar; revisão por pares pega o que você não pensou. Validação pega o caso em que tudo "passa" mas o produto não resolve o problema real do usuário. Os três juntos cobrem ângulos que individualmente escapam.

**Como usar no dia a dia.**
1. Selecione os produtos de trabalho a verificar/validar (seção 1).
2. Tenha um procedimento de revisão por pares com material de apoio (seção 2). **Na Timeware, a revisão por pares é humana, no pull request, antes do merge** — é o mecanismo padrão que satisfaz o requisito de "par".
3. Defina métodos, critérios e ambientes (seção 3).
4. Execute e trate os problemas até resolver (seção 4).
5. Analise, registre e comunique os resultados às partes interessadas (seção 5).

**Erro comum a evitar.** Confundir verificação automatizada (testes) com revisão por pares. O requisito pede as **duas**. Uma revisão feita só por ferramenta não substitui o olhar de outra pessoa qualificada — por isso o PR com revisor humano é o padrão.
