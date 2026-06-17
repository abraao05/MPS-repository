# Registro de Análise de Decisão — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | GDE-AASP01-001 |
| **Versão** | 1.0 |
| **Data** | 19/05/2026 |
| **Projeto** | AG — ms.auxo.gruposusuarios |
| **Cliente** | AASP |
| **GP/TL** | Abraão Oliveira (GP) · Cézar Velázquez (TL) (Timeware) |
| **Dev** | Renan Kioshi (Timeware) |
| **PO** | Marcos Turnes (AASP) |
| **QA** | Leonardo Francisco Pereira (AASP) |

---

## Decisão GDE-001 — ORM para acesso ao banco SQL Server (Dapper vs Entity Framework Core)

### 1. Contexto / problema

O ms.auxo.gruposusuarios precisa de uma camada de acesso ao banco SQL Server (auxo3). O projeto Gerenciador da AASP usa .NET Framework 4.7.2 como target framework. A escolha do ORM é uma decisão arquitetural com impacto em toda a camada de dados do microsserviço, afetando performance, manutenção, compatibilidade e consistência com o restante do projeto.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Dapper | Micro-ORM open-source; queries SQL explícitas escritas pelo desenvolvedor; suporte pleno e oficial ao .NET Framework 4.7.2; alto desempenho em operações de leitura e escrita; baixo overhead de memória e CPU; já utilizado em outros módulos do Gerenciador AASP como padrão estabelecido |
| B | Entity Framework Core 6.x | ORM completo da Microsoft com abstração via LINQ e DbContext; suporte ao .NET Framework 4.7.2 e apenas experimental via netstandard2.0, podendo apresentar comportamentos inesperados; curva de aprendizado de migrations e DbContext; overhead maior em queries simples comparado ao Dapper; geração de SQL pode ser opaca |
| C | ADO.NET puro | Acesso ao banco sem ORM; máximo controle sobre as queries; verboso e com alto custo de manutenção para operações CRUD; requer muito código boilerplate para cada operação; não oferece vantagem real sobre Dapper para este cenário |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Compatibilidade plena com .NET Framework 4.7.2 | Alto |
| Consistência com o padrão existente do projeto Gerenciador AASP | Alto |
| Performance em operações de leitura (listagem de grupos, relatórios) | Alto |
| Facilidade de manutenção e debugging de queries SQL | Médio |
| Curva de aprendizado da equipe atual | Médio |

### 4. Avaliação — Matriz de decisão

| Critério | Peso | A — Dapper | B — EF Core 6.x | C — ADO.NET puro |
|---|---|---|---|---|
| Compatibilidade .NET FW 4.7.2 | Alto | Plena — suporte oficial e estável para .NET Framework 4.7.2 | Parcial — suporte apenas via netstandard2.0; pode apresentar comportamentos inesperados em runtime com .NET FW legado | Plena — ADO.NET e nativo do .NET Framework em qualquer versão |
| Consistência com o projeto | Alto | Excelente — Dapper já é o padrão adotado nos outros módulos do Gerenciador AASP; equipe conhece o padrão | Baixa — EF Core seria uma exceção no projeto, introduzindo um segundo padrão de acesso a dados sem justificativa técnica suficiente | Média — possível de usar, mas introduz verbosidade e diferença de estilo em relação ao restante |
| Performance em leitura | Alto | Excelente — queries SQL otimizadas escritas diretamente pelo desenvolvedor; sem overhead de tradução LINQ para SQL | Boa — pode gerar SQL ineficiente via LINQ para queries complexas; otimizações exigem conhecimento avançado do EF Core | Excelente — controle total sobre o SQL; sem overhead de ORM |
| Manutenção e debugging | Médio | Bom — SQL explícito e legível no código; fácil de debugar e otimizar queries diretamente | Bom — mas o SQL gerado pelo EF Core pode ser opaco e difícil de debugar sem ferramentas adicionais | Ruim — código muito verboso para CRUD básico; alto custo de manutenção para operações simples |
| Curva de aprendizado | Médio | Baixa — equipe já trabalha com Dapper nos outros módulos; sem necessidade de treinamento adicional | Média — EF Core tem curva de aprendizado significativa com migrations, DbContext, fluent API e comportamentos de tracking | Baixa — ADO.NET e simples conceitualmente, mas verbose |

### 5. Decisão

**Escolhido: Alternativa A — Dapper**

Justificativa: A compatibilidade plena com .NET Framework 4.7.2 e a consistência com o padrão existente do Gerenciador AASP foram os fatores determinantes. O suporte do EF Core ao .NET Framework e apenas via netstandard2.0, introduzindo risco técnico desnecessário em um projeto de produção. O Dapper oferece performance superior em queries de leitura, e a equipe já possui experiência consolidada com o micro-ORM nos outros módulos do projeto, eliminando curva de aprendizado e garantindo consistência arquitetural. A alternativa C (ADO.NET puro) foi descartada por não oferecer vantagem real sobre o Dapper para este cenário, com custo de manutenção significativamente maior.

### 6. Impacto e riscos da decisão

- **Impacto arquitetural:** toda a camada de repositório do ms.auxo.gruposusuarios usará Dapper com queries SQL explícitas; migrations e alterações de schema serao gerenciadas por scripts .sql versionados no repositório (sem EF Core migrations)
- **Risco aceito:** maior verbosidade no repositório em comparação com EF Core para operações simples; mitigado pela consistência com o padrão do projeto e pela experiência da equipe com Dapper
- **Decisão validada por:** Cézar Velázquez (TL) e Marcos Turnes (PO) no Kickoff em 19/05/2026

---

## Decisão GDE-002 — Estratégia de exclusão de grupos (Soft Delete vs Hard Delete)

### 1. Contexto / problema

Ao excluir um grupo de usuários, é necessário decidir se o registro é removido fisicamente do banco (hard delete via DELETE SQL) ou apenas marcado como inativo (soft delete via campo Ativo=false). A decisão impacta integridade referencial das tabelas relacionadas (PermissoesGrupo, UsuariosGrupo, AuditoriaGrupos), auditabilidade do sistema e conformidade com os requisitos do processo MPS-SW de rastreabilidade.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Soft Delete (campo Ativo=false) | Registro permanece fisicamente no banco; campo Ativo bit e definido como false na operação de exclusão; todas as queries de listagem filtram WHERE Ativo=1; histórico de dados preservado; integridade referencial com tabelas filhas mantida sem cascata de deleções; compatível com auditoria |
| B | Hard Delete (exclusão física) | Registro removido do banco via DELETE SQL; implementação mais simples; perde o histórico do grupo; pode causar registros orfaos em tabelas relacionadas como PermissoesGrupo, UsuariosGrupo e AuditoriaGrupos, a menos que se implemente CASCADE DELETE ou exclusão manual em cascata |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Integridade referencial e preservação do histórico de dados | Alto |
| Rastreabilidade para fins de auditoria e conformidade MPS-SW | Alto |
| Comportamento esperado e validado pelo PO (AASP) | Médio |
| Simplicidade de implementação | Baixo |

### 4. Avaliação — Matriz de decisão

| Critério | Peso | A — Soft Delete | B — Hard Delete |
|---|---|---|---|
| Integridade referencial e histórico | Alto | Excelente — registros de PermissoesGrupo, UsuariosGrupo e AuditoriaGrupos permanecem integros com FK valida; histórico completo preservado | Ruim — exige CASCADE DELETE em todas as tabelas filhas ou exclusão manual em cascata; histórico de AuditoriaGrupos perdido |
| Rastreabilidade e auditoria | Alto | Excelente — grupos inativos podem ser consultados para auditoria; AuditoriaGrupos mantém GrupoId válido mesmo após inativação | Ruim — registros de AuditoriaGrupos ficam orfaos após hard delete do grupo; rastreabilidade comprometida |
| Comportamento validado pelo PO | Médio | Aprovado — Marcos Turnes validou a abordagem de soft delete no Kickoff; comportamento alinhado com expectativa do AASP | Não validado — não é a expectativa do PO |
| Simplicidade de implementação | Baixo | Média — requer adição do campo Ativo e filtro WHERE Ativo=1 em todas as queries de listagem | Alta — DELETE SQL simples, sem necessidade de campo adicional; porém exige tratamento de cascata |

### 5. Decisão

**Escolhido: Alternativa A — Soft Delete**

Justificativa: A integridade referencial é crítica para o ms.auxo.gruposusuarios — grupos possuem histórico de vínculos (UsuariosGrupo), permissões (PermissoesGrupo) e registros de auditoria (AuditoriaGrupos) que não devem ser perdidos. O hard delete exigiria cascata de exclusões ou geraria registros orfaos em tabelas filhas, comprometendo a rastreabilidade exigida pelo processo MPS-SW. O soft delete preserva o histórico completo, é compatível com o requisito de auditoria (AG-23 — implementado na Sprint 2) e alinhado com a rastreabilidade exigida pelo MPS-SW nível C. Decisão validada com o PO Marcos Turnes no Kickoff em 19/05/2026 (referenciado como D-02 na ATA-AASP01-001).

### 6. Impacto da decisão

- **Tabela Grupos:** campo Ativo bit NOT NULL DEFAULT 1 incluido na definição da tabela
- **Endpoint DELETE /grupos/{id}:** executa UPDATE Grupos SET Ativo=0, DataAtualizacao=GETDATE() WHERE Id={id} — não executa DELETE SQL
- **Queries de listagem:** todas as queries de SELECT em Grupos, PermissoesGrupo e UsuariosGrupo filtram WHERE Ativo=1
- **Regra de negócio:** grupos com Ativo=false não podem receber novos vínculos de usuários nem novas permissões — validação implementada no GrupoService
- **Hard delete:** nunca executado via API; apenas o time de DBA pode remover registros diretamente no banco em casos excepcionais e documentados
- **Soft delete de vínculos:** a mesma estratégia se aplica a UsuariosGrupo — desvínculo de usuário faz UPDATE Ativo=0, não DELETE do registro

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 19/05/2026 | Abraão Oliveira | Criação do documento; decisões GDE-001 (Dapper) e GDE-002 (Soft Delete) tomadas no Kickoff e formalizadas com base nas discussões com Marcos Turnes (PO) e Renan Kioshi (Dev) |
