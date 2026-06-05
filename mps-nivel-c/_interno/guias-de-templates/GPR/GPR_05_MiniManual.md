# Mini-manual — Gerência de Projetos (GPR)

**O que é o GPR.** Processo que define e acompanha o trabalho comprometido: o que será entregue, com quais recursos, em que prazo, com quais riscos — e como o andamento real é comparado ao que foi combinado. O GPR não é sobre preencher formulários; é sobre ter um plano real, medir o desvio e agir antes que o problema se instale.

**O que ele garante.** Que (1) existe um plano com baseline documentada, (2) o andamento é monitorado sistematicamente com base nessa baseline, (3) desvios são tratados com ação — não ignorados ou explicados depois —, (4) mudanças de escopo passam por decisão formal em vez de se acumular silenciosamente, e (5) o encerramento é formal, com aceite do cliente e registro das lições aprendidas.

**Por que fazer.** Projetos sem plano terminam atrasados e com escopo diferente do combinado — e ninguém sabe exatamente quando as coisas saíram dos trilhos. O GPR cria o espelho: a baseline permite enxergar o desvio enquanto ainda há tempo de agir.

---

## Os 6 artefatos e quando cada um é usado

| Artefato | Código | Quando produzir | Quem preenche |
|---|---|---|---|
| Termo de Abertura | TPL-GPR-002 | Antes de qualquer estimativa — ao confirmar que o projeto será iniciado | Gerente de Projeto, com patrocinador |
| Registro de Adaptação | TPL-GPR-003 | Logo após o Termo de Abertura, antes do planejamento detalhado | Gerente de Projeto |
| Plano do Projeto | TPL-GPR-001 | Na fase de planejamento, depois da adaptação — é a baseline | Gerente de Projeto, com a equipe |
| Relatório de Acompanhamento | TPL-GPR-005 | A cada ciclo de acompanhamento (por fase, milestone ou período definido) | Gerente de Projeto |
| Change Request | TPL-GPR-006 | A cada mudança que afeta escopo, prazo ou custo — antes de executá-la | Gerente de Projeto / solicitante |
| Termo de Encerramento | TPL-GPR-004 | Ao final do projeto, após a última entrega validada e aceita | Gerente de Projeto, com cliente |

---

## Sequência típica de uso

1. **Abertura formal (TAP).** O Gerente de Projeto emite o Termo de Abertura com o patrocinador/cliente: objetivo, escopo macro, equipe inicial, marcos estimados. O projeto tem início oficializado.
2. **Adaptação consciente.** Antes do planejamento detalhado, registra-se o Registro de Adaptação: quais eixos do processo-padrão se aplicam, quais não se aplicam, e por quê. A adaptação é uma decisão deliberada, não um esquecimento.
3. **Planejamento e baseline.** O Plano do Projeto é elaborado: histórias, estimativas, orçamento, cronograma, recursos, riscos. Quando aprovado, torna-se a baseline — o ponto de referência contra o qual tudo será medido.
4. **Execução com acompanhamento.** A cada ciclo, o Relatório de Acompanhamento compara o planejado ao realizado em todas as dimensões (escopo, esforço, prazo, recursos, riscos). Desvios geram ações; ações são acompanhadas até fechar.
5. **Mudanças formais (CR).** Qualquer mudança que afeta a baseline (escopo, prazo, custo) passa por um Change Request. O CR analisa o impacto, define o tipo de tratamento e produz uma decisão documentada. Se aprovado, reflete na baseline e no backlog.
6. **Encerramento formal (TEN).** Ao fim do projeto, o Termo de Encerramento registra o que foi entregue, como o escopo se realizou, o aceite do cliente, a estratégia de sustentação e as lições aprendidas. Encerra as obrigações formais da equipe com o projeto.

---

**Erro comum a evitar.** Dois erros frequentes, e opostos:

- **Confundir baseline com realização.** O Plano é o baseline — o comprometimento feito. O Relatório é o espelho da realidade. Atualizar o Plano para "refletir o que aconteceu" sem um CR formal destrói o histórico: perde-se a capacidade de enxergar desvios e aprender com eles.

- **Tratar o CR como exceção informal.** Mudanças pequenas que "não precisam de CR" se acumulam e fazem o escopo real divergir silenciosamente do combinado. A regra deve ser simples: se a mudança tem impacto que seria difícil reverter, ela precisa de CR. O CR não é burocracia — é o mecanismo que mantém o plano honesto.
