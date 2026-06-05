# Mini-manual — Matriz de Rastreabilidade (TPL-REQ-002)

**O que é.** A Matriz de Rastreabilidade é o documento que conecta, em uma cadeia contínua, a necessidade da parte interessada ao requisito especificado, ao item de design, ao item no backlog, ao caso de teste e à situação final. Ela permite navegar nos dois sentidos: do requisito ao código (para verificar que foi construído) e do código ao requisito (para verificar que havia justificativa). É a ferramenta que torna a pergunta "tudo que prometemos foi construído?" respondível de forma objetiva.

**O que garante.** Que (1) todo requisito tem um caminho rastreável desde a necessidade que o originou até o caso de teste que o verifica, (2) não há itens implementados sem requisito — o chamado "escopo fantasma" —, (3) não há requisitos sem cobertura de teste — o "risco invisível" —, e (4) é possível, a qualquer momento do projeto, saber qual é a situação de cada compromisso. A seção de cobertura é o termômetro de saúde da rastreabilidade.

**Por que fazer.** Projetos sem rastreabilidade chegam ao final sem saber se entregaram tudo que prometeram. E sem saber se tudo que construíram tinha razão de existir. Esses dois diagnósticos — requisito sem teste e código sem requisito — costumam aparecer juntos e sempre indicam risco: ou o produto está incompleto, ou está inflado com funcionalidades que ninguém solicitou. A Matriz é o que torna esses riscos visíveis antes que se tornem problemas.

**Como usar no dia a dia.**

1. **Quando começar?** Na fase de planejamento — assim que os primeiros requisitos são especificados. Não espere o projeto terminar.
2. A cada requisito especificado, crie uma linha na Matriz com o ID do requisito e a necessidade que o origina.
3. Quando a história for para o backlog/Jira, preencha a coluna "Item no backlog" com o ID da issue. O ID do requisito viaja com a tarefa — não começa a rastreabilidade retroativamente.
4. Quando a história for implementada, registre o componente ou serviço na coluna "Item de design".
5. Quando o caso de teste for escrito e executado, preencha o ID do caso de teste e a situação (Verificado / Atendido).
6. A cada milestone, rode a verificação de órfãos: itens sem requisito e requisitos sem cobertura. Corrija antes de avançar.
7. A seção de Cobertura deve estar vazia (nenhum órfão) ao final do projeto — se não estiver, é risco a tratar antes do encerramento.

**Erro comum a evitar.** Preencher a Matriz apenas no final do projeto, quando os órfãos já foram construídos e não há mais como corrigi-los facilmente. A rastreabilidade só funciona se for mantida durante a construção — o ID do requisito precisa viajar com a tarefa desde o momento em que entra no backlog, não ser reconectado depois. Construir a rastreabilidade retroativamente é um exercício de memória falível que produz uma matriz de aparência correta, mas sem valor real de auditoria.
