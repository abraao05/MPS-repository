# Registro de Análise de Decisão — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | GDE-AASP01-001 |
| **Versão** | 1.3 |
| **Data** | 01/07/2026 |
| **Projeto** | AG — ms.auxo.usuarios |
| **Cliente** | AASP |
| **GP/TL** | Abraão (GP) · Cezar Hiraki (TL) (Timeware) |
| **Dev** | Renan Kiyoshi (Timeware) |
| **PO** | Marcos Turnes (AASP) |
| **QA** | Leonardo Francisco Pereira (AASP) |

---

## Decisão GDE-001 — ORM para acesso ao banco SQL Server (Dapper vs Entity Framework Core)

### 1. Contexto / problema

O ms.auxo.usuarios precisa de uma camada de acesso ao banco SQL Server (auxo3). O projeto Gerenciador da AASP usa .NET 5.0 (net5.0) como target framework. A escolha do ORM e uma decisão arquitetural com impacto em toda a camada de dados do microsserviço, afetando performance, manutenção, compatibilidade e consistência com o restante do projeto.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Dapper | Micro-ORM open-source; queries SQL explicitas escritas pelo desenvolvedor; suporte pleno e oficial ao .NET 5.0 (net5.0); alto desempenho em operações de leitura e escrita; baixo overhead de memória e CPU; já utilizado em outros módulos do Gerenciador AASP como padrão estabelecido |
| B | Entity Framework Core 6.x | ORM completo da Microsoft com abstração via LINQ e DbContext; suporte oficial ao .NET 5.0 (net5.0); porém introduziria um segundo padrão de acesso a dados no projeto; curva de aprendizado de migrations e DbContext; overhead maior em queries simples comparado ao Dapper; geração de SQL pode ser opaca |
| C | ADO.NET puro | Acesso ao banco sem ORM; máximo controle sobre as queries; verboso e com alto custo de manutenção para operações CRUD; requer muito código boilerplate para cada operação; não oferece vantagem real sobre Dapper para este cenário |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Compatibilidade plena com .NET 5.0 (net5.0) | Alto |
| Consistência com o padrão existente do projeto Gerenciador AASP | Alto |
| Performance em operações de leitura (listagem de grupos, relatórios) | Alto |
| Facilidade de manutenção e debugging de queries SQL | Medio |
| Curva de aprendizado da equipe atual | Medio |

### 4. Avaliação — Matriz de decisão

| Critério | Peso | A — Dapper | B — EF Core 6.x | C — ADO.NET puro |
|---|---|---|---|---|
| Compatibilidade com .NET 5.0 | Alto | Plena — suporte oficial e estável ao .NET 5.0 (net5.0) | Plena — EF Core 6 suporta net5.0 oficialmente, mas seria um novo padrão no projeto | Plena — ADO.NET é nativo do .NET em qualquer versão |
| Consistência com o projeto | Alto | Excelente — Dapper já e o padrão adotado nos outros módulos do Gerenciador AASP; equipe conhece o padrão | Baixa — EF Core seria uma exceção no projeto, introduzindo um segundo padrão de acesso a dados sem justificativa técnica suficiente | Media — possível de usar, mas introduz verbosidade e diferenca de estilo em relação ao restante |
| Performance em leitura | Alto | Excelente — queries SQL otimizadas escritas diretamente pelo desenvolvedor; sem overhead de tradução LINQ para SQL | Boa — pode gerar SQL ineficiente via LINQ para queries complexas; otimizações exigem conhecimento avancado do EF Core | Excelente — controle total sobre o SQL; sem overhead de ORM |
| Manutenção e debugging | Medio | Bom — SQL explicito e legivel no código; fácil de debugar e otimizar queries diretamente | Bom — mas o SQL gerado pelo EF Core pode ser opaco e difícil de debugar sem ferramentas adicionais | Ruim — código muito verboso para CRUD básico; alto custo de manutenção para operações simples |
| Curva de aprendizado | Medio | Baixa — equipe já trabalha com Dapper nos outros módulos; sem necessidade de treinamento adicional | Media — EF Core tem curva de aprendizado significativa com migrations, DbContext, fluent API e comportamentos de tracking | Baixa — ADO.NET e simples conceitualmente, mas verbose |

### 5. Decisão

**Escolhido: Alternativa A — Dapper**

Justificativa: a consistência com o padrão já adotado nos demais módulos do Gerenciador AASP e a performance em leitura foram os fatores determinantes. Embora o EF Core 6 também suporte o .NET 5.0, adotá-lo introduziria um segundo padrão de acesso a dados sem justificativa técnica suficiente, divergindo do restante do projeto. O Dapper oferece performance superior em queries de leitura, e a equipe já possui experiência consolidada com o micro-ORM nos outros módulos do projeto, eliminando curva de aprendizado e garantindo consistência arquitetural. A alternativa C (ADO.NET puro) foi descartada por não oferecer vantagem real sobre o Dapper para este cenário, com custo de manutenção significativamente maior.

### 6. Impacto e riscos da decisão

- **Impacto arquitetural:** toda a camada de repositório do ms.auxo.usuarios usara Dapper com queries SQL explicitas; migrations e alterações de schema serão gerenciadas por scripts .sql versionados no repositório (sem EF Core migrations)
- **Risco aceito:** maior verbosidade no repositório em comparação com EF Core para operações simples; mitigado pela consistência com o padrão do projeto e pela experiência da equipe com Dapper
- **Decisão validada por:** Cezar Hiraki (TL) e Marcos Turnes (PO) no Kickoff em 19/05/2026

---

## Decisão GDE-002 — Estratégia de exclusão de grupos (Soft Delete vs Hard Delete)

### 1. Contexto / problema

Ao excluir um grupo de usuários, e necessário decidir se o registro e removido fisicamente do banco (hard delete via DELETE SQL) ou apenas marcado como excluido (soft delete via campo `excluido`). A decisão impacta integridade referencial das tabelas relacionadas (`grupos_usuarios_vinculos`, `grupos_usuarios_funcao`), auditabilidade do sistema e conformidade com os requisitos do processo MPS-SW de rastreabilidade.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Soft Delete (campo `excluido`) | Registro permanece fisicamente no banco; o campo `excluido` e definido como 1 na operação de exclusão; todas as queries de listagem filtram `WHERE excluido = 0`; histórico de dados preservado; integridade referencial com as tabelas relacionadas mantida sem cascata de deleções |
| B | Hard Delete (exclusão física) | Registro removido do banco via DELETE SQL; implementação mais simples; perde o histórico do grupo; pode causar registros orfaos nas tabelas relacionadas (`grupos_usuarios_vinculos`, `grupos_usuarios_funcao`), a menos que se implemente CASCADE DELETE ou exclusão manual em cascata |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Integridade referencial e preservação do histórico de dados | Alto |
| Rastreabilidade para fins de auditoria e conformidade MPS-SW | Alto |
| Comportamento esperado e validado pelo PO (AASP) | Medio |
| Simplicidade de implementação | Baixo |

### 4. Avaliação — Matriz de decisão

| Critério | Peso | A — Soft Delete | B — Hard Delete |
|---|---|---|---|
| Integridade referencial e histórico | Alto | Excelente — os registros de `grupos_usuarios_vinculos` e `grupos_usuarios_funcao` permanecem integros; histórico completo preservado | Ruim — exige CASCADE DELETE nas tabelas relacionadas ou exclusão manual em cascata; histórico perdido |
| Rastreabilidade e auditoria | Alto | Excelente — grupos excluidos podem ser consultados para auditoria | Ruim — registros relacionados ficam orfaos após hard delete; rastreabilidade comprometida |
| Comportamento validado pelo PO | Medio | Aprovado — Marcos Turnes validou a abordagem de soft delete no Kickoff | Não validado — não e a expectativa do PO |
| Simplicidade de implementação | Baixo | Media — requer o campo `excluido` e o filtro `WHERE excluido = 0` em todas as queries de listagem | Alta — DELETE SQL simples; porém exige tratamento de cascata |

### 5. Decisão

**Escolhido: Alternativa A — Soft Delete**

Justificativa: A integridade referencial e critica para o ms.auxo.usuarios — grupos possuem histórico de vinculos (`grupos_usuarios_vinculos`) e de funções (`grupos_usuarios_funcao`) que não devem ser perdidos. O hard delete exigiria cascata de exclusões ou geraria registros orfaos nas tabelas relacionadas, comprometendo a rastreabilidade exigida pelo processo MPS-SW. O soft delete preserva o histórico completo, e compativel com o requisito de auditoria (AG-23 — planejado para a Sprint 2) e alinhado com a rastreabilidade exigida pelo MPS-SW nível C. Decisão validada com o PO Marcos Turnes no Kickoff em 19/05/2026 (referenciado como D-02 na ATA-AASP01-001).

### 6. Impacto da decisão

- **Tabela `grupos_usuarios`:** campo `excluido` (0 = ativo, 1 = excluido) e `data_exclusao` usados para o soft delete
- **Endpoint `excluirgrupo`:** executa `UPDATE grupos_usuarios SET excluido = 1, data_exclusao = GETDATE() WHERE id = @id` — não executa DELETE SQL
- **Queries de listagem:** todas as queries de SELECT em `grupos_usuarios` filtram `WHERE excluido = 0`
- **Hard delete:** nunca executado via API; apenas o time de DBA pode remover registros diretamente no banco em casos excepcionais e documentados
- **Soft delete de vinculos:** a mesma estratégia se aplica a `grupos_usuarios_vinculos` — `removerusuario` faz `UPDATE ... SET excluido = 1`, não DELETE do registro

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 19/05/2026 | Abraão | Criação do documento; decisões GDE-001 (Dapper) e GDE-002 (Soft Delete) tomadas no Kickoff |
| 1.1 | 15/06/2026 | Abraão | GDE-002 alinhado ao schema real (soft delete via `excluido`; tabelas `grupos_usuarios`, `_vinculos`, `_funcao`; endpoint `excluirgrupo`) |
| 1.2 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
| 1.3 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: autor de v1.2 corrigido (Time de Melhoria Contínua → Silvio Baroni SEPG); versão e data do cabeçalho atualizadas. |
