# Relatório de Acompanhamento do Projeto

> **Nota sobre este exemplo.** Modelo de preenchimento usando o *Trainer Connect* como base, a partir da evidência real do diagnóstico (durações de fase, commits, retrospectivas, auditorias de milestone). Onde o dado dependia de estrutura inexistente no projeto solo (orçamento, comunicação a stakeholders), usamos valor plausível marcado *(exemplo)*. Serve de orientação de "como preencher".

---

## 0. Identificação do ciclo

| Campo | Valor |
|---|---|
| Projeto | Trainer Connect |
| Plano de referência (versão) | v3 do Plano do Projeto |
| Período / ciclo deste relatório | Fechamento do milestone v1.8 (Execução) |
| Data do relatório | 2026-06-02 |
| Responsável pelo relatório | *(exemplo: gestor Timeware)* |

---

## 1. Monitoramento do planejado vs. realizado

### 1.1 Progresso de escopo e tarefas

| Dimensão | Planejado (baseline) | Realizado | Desvio | Comentário |
|---|---|---|---|---|
| Histórias concluídas | 9 histórias no milestone v1.8 | 9/9 concluídas | 0 | Auditoria de milestone confirmou cobertura completa de requisitos, sem requisito órfão |
| Fases concluídas | 24 fases planejadas no acumulado | 24 concluídas | 0 | Pipeline aplicado de forma idêntica em todas |

### 1.2 Estimado vs. realizado (dimensão e esforço)

| Item | Pontos estimados | Pontos entregues | Esforço estimado | Esforço real | Comentário |
|---|---|---|---|---|---|
| Fase Fundação | 24 | 24 | ~30 h | ~28 h | Abaixo do estimado |
| Fase Treinos | 45 | 45 | ~55 h | ~60 h | Acima: complexidade da biblioteca subestimada |
| Fase Execução | 30 | 30 | ~45 h | ~44 h | Dentro do estimado |

- **Velocidade real observada neste ciclo:** ~11 pontos/semana *(exemplo; planejado era ~12)*
- **Esforço real por ponto observado:** ~1,3 h/ponto — *ligeiramente acima do 1,25 h/ponto usado na estimativa; valor atualizado para a referência das próximas estimativas.*

### 1.3 Orçamento e cronograma

| Dimensão | Planejado (baseline) | Realizado | Desvio | Comentário |
|---|---|---|---|---|
| Orçamento total | R$ 45.000 *(exemplo)* | R$ 45.000 (sem estouro) | 0 | Custo comercial fixo; sem aditivo |
| Marco v1.8 | 2025-04 | 2025-04 | 0 | Entregue no prazo; validado por usuário real em produção |

### 1.4 Recursos

| Dimensão | Planejado | Realizado | Desvio | Comentário |
|---|---|---|---|---|
| Recursos humanos | Equipe prevista | Mantida | 0 | — |
| Ambiente | Dev/homolog/produção | Operando | 0 | Publicação automática funcionando |

---

## 2. Envolvimento das partes interessadas

- Usuário primário (personal trainer) participou da validação de aceite ao fim do milestone, com registro de sign-off. Alunos testaram os fluxos de execução.
- Não houve parte interessada omitida no ciclo. *(Na Timeware, o plano de comunicação a stakeholders é o mecanismo que garante isso de forma sistemática — no projeto solo original esse era um ponto fraco identificado.)*

---

## 3. Transição para operação e suporte

- Produto publicado em produção e em uso por usuário real. Migrações de banco aplicadas de forma versionada e ordenada. Monitoramento dos primeiros acessos sem incidentes relevantes.

---

## 4. Riscos e oportunidades

| ID | Risco / Oportunidade | Situação atual | Mudança desde o último ciclo | Comunicado a quem |
|---|---|---|---|---|
| R-02 | Dependência de gateway de pagamento (módulo comércio) | Mantida — módulo segue parqueado | Sem mudança; prereqs ainda não atendidos | Patrocinador |
| O-01 | Exercícios públicos como diferencial | Implementado e em uso | Oportunidade concretizada | Patrocinador, usuário |

---

## 5. Ações corretivas e questões

| ID | Questão / desvio | Ação tomada | Tratada com | Responsável | Situação |
|---|---|---|---|---|---|
| A-01 | Divergência entre duas tabelas do banco (drift) detectada na retrospectiva | Padrão adotado: atualizar ambas as tabelas no mesmo commit | Equipe de desenvolvimento | Dev | Concluída |
| A-02 | Uma fase ficou sem registro de validação (detectado na auditoria) | Marcado como débito técnico e validação executada antes do fechamento | Gestor | Dev | Concluída |
| A-03 | Esforço da fase Treinos acima do estimado | Causa registrada; referência de esforço por ponto ajustada | Gestor | Gestor | Concluída |

---

## 6. Análise de resultados significativos

| Resultado | Análise de causa | Encaminhamento |
|---|---|---|
| Drift recorrente entre tabelas do banco (v1.0 e v1.1) | Causa-raiz: o executor atualizava só um dos dois lugares que precisavam mudar juntos | Virou prática padrão (ação A-01); recorrência cessou |
| Milestone v1.8 entregue completo e validado em produção | Pipeline consistente + rastreabilidade de requisitos (zero órfãos na auditoria) | Manter a prática; propor como padrão (seção 7) |

---

## 7. Melhorias de processo propostas

| O que funcionou | Por que propor como melhoria de processo | Encaminhado para |
|---|---|---|
| Auditoria de milestone com detecção de requisito órfão (cruzamento de 3 fontes) | Garante que nenhum requisito fica sem implementação/verificação; replicável em qualquer projeto | Processo organizacional (gestão de processos) |
| Atualizar tabelas dependentes no mesmo commit | Elimina classe inteira de bug de drift; baixo custo, alto retorno | Padrões de engenharia da organização |
