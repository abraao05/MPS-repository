# Mini-manual — Revisão por Pares

**O que é.** A verificação de um produto de trabalho (código, design, documento) por alguém diferente do autor, com o objetivo de encontrar problemas antes que avancem para a próxima etapa. Cada revisão produz um registro rastreável.

**O que ele garante.** Que (1) o item revisado passou por um segundo par de olhos com registro do resultado; (2) os apontamentos encontrados têm severidade, tratamento e situação acompanhados; (3) há uma decisão explícita de aprovação ou rejeição; e (4) problemas de segurança, qualidade e performance são detectados antes de chegarem ao cliente.

**Por que fazer.** Defeitos encontrados em revisão custam em média 10 vezes menos para corrigir do que defeitos encontrados em produção. A revisão por pares é a atividade de menor custo-benefício em qualidade de software — e também é evidência direta do resultado VV 2 do MPS.

**Como usar no dia a dia.**
1. Ao abrir um Pull Request, acione o revisor definido para o tipo de item (código → tech lead ou par designado; documento → PO ou gestor).
2. O revisor examina os itens listados na seção 2 e registra apontamentos na seção 3 — um por linha, com severidade.
3. O autor trata os apontamentos e registra o tratamento na mesma linha.
4. O revisor confirma os tratamentos e emite o resultado (seção 4).
5. O Pull Request pode usar este registro como evidência formal — basta referenciar o ID aqui no PR e vice-versa.

**Erro comum a evitar.** Revisar "para constar" — aprovar sem apontamentos reais quando há problemas visíveis. Uma revisão vazia aprovada gera falsa confiança e inutiliza a evidência. A regra prática: se você leu o código e não pensou em nada, você não leu o código. Uma revisão honesta com zero apontamentos é válida — uma revisão protocolar que encobre problemas, não.
