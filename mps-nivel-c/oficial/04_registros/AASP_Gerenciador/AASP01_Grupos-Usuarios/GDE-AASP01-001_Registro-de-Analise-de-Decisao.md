# Registro de Analise de Decisao — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | GDE-AASP01-001 |
| **Versao** | 1.0 |
| **Data** | 19/05/2026 |
| **Projeto** | AG — ms.auxo.gruposusuarios |
| **Cliente** | AASP |
| **GP/TL** | Henry Komatsu (Timeware) |
| **Dev** | Bruno Almeida (Timeware) |
| **PO** | Marcos Ferreira (AASP) |
| **QA** | Renata Souza (AASP) |

---

## Decisao GDE-001 — ORM para acesso ao banco SQL Server (Dapper vs Entity Framework Core)

### 1. Contexto / problema

O ms.auxo.gruposusuarios precisa de uma camada de acesso ao banco SQL Server (auxo3). O projeto Gerenciador da AASP usa .NET Framework 4.7.2 como target framework. A escolha do ORM e uma decisao arquitetural com impacto em toda a camada de dados do microsservico, afetando performance, manutencao, compatibilidade e consistencia com o restante do projeto.

### 2. Alternativas avaliadas

| # | Alternativa | Descricao |
|---|---|---|
| A | Dapper | Micro-ORM open-source; queries SQL explicitas escritas pelo desenvolvedor; suporte pleno e oficial ao .NET Framework 4.7.2; alto desempenho em operacoes de leitura e escrita; baixo overhead de memoria e CPU; ja utilizado em outros modulos do Gerenciador AASP como padrao estabelecido |
| B | Entity Framework Core 6.x | ORM completo da Microsoft com abstracao via LINQ e DbContext; suporte ao .NET Framework 4.7.2 e apenas experimental via netstandard2.0, podendo apresentar comportamentos inesperados; curva de aprendizado de migrations e DbContext; overhead maior em queries simples comparado ao Dapper; geracao de SQL pode ser opaca |
| C | ADO.NET puro | Acesso ao banco sem ORM; maximo controle sobre as queries; verboso e com alto custo de manutencao para operacoes CRUD; requer muito codigo boilerplate para cada operacao; nao oferece vantagem real sobre Dapper para este cenario |

### 3. Criterios de decisao

| Criterio | Peso |
|---|---|
| Compatibilidade plena com .NET Framework 4.7.2 | Alto |
| Consistencia com o padrao existente do projeto Gerenciador AASP | Alto |
| Performance em operacoes de leitura (listagem de grupos, relatorios) | Alto |
| Facilidade de manutencao e debugging de queries SQL | Medio |
| Curva de aprendizado da equipe atual | Medio |

### 4. Avaliacao — Matriz de decisao

| Criterio | Peso | A — Dapper | B — EF Core 6.x | C — ADO.NET puro |
|---|---|---|---|---|
| Compatibilidade .NET FW 4.7.2 | Alto | Plena — suporte oficial e estavel para .NET Framework 4.7.2 | Parcial — suporte apenas via netstandard2.0; pode apresentar comportamentos inesperados em runtime com .NET FW legado | Plena — ADO.NET e nativo do .NET Framework em qualquer versao |
| Consistencia com o projeto | Alto | Excelente — Dapper ja e o padrao adotado nos outros modulos do Gerenciador AASP; equipe conhece o padrao | Baixa — EF Core seria uma excecao no projeto, introduzindo um segundo padrao de acesso a dados sem justificativa tecnica suficiente | Media — possivel de usar, mas introduz verbosidade e diferenca de estilo em relacao ao restante |
| Performance em leitura | Alto | Excelente — queries SQL otimizadas escritas diretamente pelo desenvolvedor; sem overhead de traducao LINQ para SQL | Boa — pode gerar SQL ineficiente via LINQ para queries complexas; otimizacoes exigem conhecimento avancado do EF Core | Excelente — controle total sobre o SQL; sem overhead de ORM |
| Manutencao e debugging | Medio | Bom — SQL explicito e legivel no codigo; facil de debugar e otimizar queries diretamente | Bom — mas o SQL gerado pelo EF Core pode ser opaco e dificil de debugar sem ferramentas adicionais | Ruim — codigo muito verboso para CRUD basico; alto custo de manutencao para operacoes simples |
| Curva de aprendizado | Medio | Baixa — equipe ja trabalha com Dapper nos outros modulos; sem necessidade de treinamento adicional | Media — EF Core tem curva de aprendizado significativa com migrations, DbContext, fluent API e comportamentos de tracking | Baixa — ADO.NET e simples conceitualmente, mas verbose |

### 5. Decisao

**Escolhido: Alternativa A — Dapper**

Justificativa: A compatibilidade plena com .NET Framework 4.7.2 e a consistencia com o padrao existente do Gerenciador AASP foram os fatores determinantes. O suporte do EF Core ao .NET Framework e apenas via netstandard2.0, introduzindo risco tecnico desnecessario em um projeto de producao. O Dapper oferece performance superior em queries de leitura, e a equipe ja possui experiencia consolidada com o micro-ORM nos outros modulos do projeto, eliminando curva de aprendizado e garantindo consistencia arquitetural. A alternativa C (ADO.NET puro) foi descartada por nao oferecer vantagem real sobre o Dapper para este cenario, com custo de manutencao significativamente maior.

### 6. Impacto e riscos da decisao

- **Impacto arquitetural:** toda a camada de repositorio do ms.auxo.gruposusuarios usara Dapper com queries SQL explicitas; migrations e alteracoes de schema serao gerenciadas por scripts .sql versionados no repositorio (sem EF Core migrations)
- **Risco aceito:** maior verbosidade no repositorio em comparacao com EF Core para operacoes simples; mitigado pela consistencia com o padrao do projeto e pela experiencia da equipe com Dapper
- **Decisao validada por:** Henry Komatsu (TL) e Marcos Ferreira (PO) no Kickoff em 19/05/2026

---

## Decisao GDE-002 — Estrategia de exclusao de grupos (Soft Delete vs Hard Delete)

### 1. Contexto / problema

Ao excluir um grupo de usuarios, e necessario decidir se o registro e removido fisicamente do banco (hard delete via DELETE SQL) ou apenas marcado como inativo (soft delete via campo Ativo=false). A decisao impacta integridade referencial das tabelas relacionadas (PermissoesGrupo, UsuariosGrupo, AuditoriaGrupos), auditabilidade do sistema e conformidade com os requisitos do processo MPS-SW de rastreabilidade.

### 2. Alternativas avaliadas

| # | Alternativa | Descricao |
|---|---|---|
| A | Soft Delete (campo Ativo=false) | Registro permanece fisicamente no banco; campo Ativo bit e definido como false na operacao de exclusao; todas as queries de listagem filtram WHERE Ativo=1; historico de dados preservado; integridade referencial com tabelas filhas mantida sem cascata de delecoes; compativel com auditoria |
| B | Hard Delete (exclusao fisica) | Registro removido do banco via DELETE SQL; implementacao mais simples; perde o historico do grupo; pode causar registros orfaos em tabelas relacionadas como PermissoesGrupo, UsuariosGrupo e AuditoriaGrupos, a menos que se implemente CASCADE DELETE ou exclusao manual em cascata |

### 3. Criterios de decisao

| Criterio | Peso |
|---|---|
| Integridade referencial e preservacao do historico de dados | Alto |
| Rastreabilidade para fins de auditoria e conformidade MPS-SW | Alto |
| Comportamento esperado e validado pelo PO (AASP) | Medio |
| Simplicidade de implementacao | Baixo |

### 4. Avaliacao — Matriz de decisao

| Criterio | Peso | A — Soft Delete | B — Hard Delete |
|---|---|---|---|
| Integridade referencial e historico | Alto | Excelente — registros de PermissoesGrupo, UsuariosGrupo e AuditoriaGrupos permanecem integros com FK valida; historico completo preservado | Ruim — exige CASCADE DELETE em todas as tabelas filhas ou exclusao manual em cascata; historico de AuditoriaGrupos perdido |
| Rastreabilidade e auditoria | Alto | Excelente — grupos inativos podem ser consultados para auditoria; AuditoriaGrupos mantem GrupoId valido mesmo apos inativacao | Ruim — registros de AuditoriaGrupos ficam orfaos apos hard delete do grupo; rastreabilidade comprometida |
| Comportamento validado pelo PO | Medio | Aprovado — Marcos Ferreira validou a abordagem de soft delete no Kickoff; comportamento alinhado com expectativa do AASP | Nao validado — nao e a expectativa do PO |
| Simplicidade de implementacao | Baixo | Media — requer adicao do campo Ativo e filtro WHERE Ativo=1 em todas as queries de listagem | Alta — DELETE SQL simples, sem necessidade de campo adicional; porem exige tratamento de cascata |

### 5. Decisao

**Escolhido: Alternativa A — Soft Delete**

Justificativa: A integridade referencial e critica para o ms.auxo.gruposusuarios — grupos possuem historico de vinculos (UsuariosGrupo), permissoes (PermissoesGrupo) e registros de auditoria (AuditoriaGrupos) que nao devem ser perdidos. O hard delete exigiria cascata de exclusoes ou geraria registros orfaos em tabelas filhas, comprometendo a rastreabilidade exigida pelo processo MPS-SW. O soft delete preserva o historico completo, e compativel com o requisito de auditoria (AG-23 — implementado na Sprint 2) e alinhado com a rastreabilidade exigida pelo MPS-SW nivel C. Decisao validada com o PO Marcos Ferreira no Kickoff em 19/05/2026 (referenciado como D-02 na ATA-AASP01-001).

### 6. Impacto da decisao

- **Tabela Grupos:** campo Ativo bit NOT NULL DEFAULT 1 incluido na definicao da tabela
- **Endpoint DELETE /grupos/{id}:** executa UPDATE Grupos SET Ativo=0, DataAtualizacao=GETDATE() WHERE Id={id} — nao executa DELETE SQL
- **Queries de listagem:** todas as queries de SELECT em Grupos, PermissoesGrupo e UsuariosGrupo filtram WHERE Ativo=1
- **Regra de negocio:** grupos com Ativo=false nao podem receber novos vinculos de usuarios nem novas permissoes — validacao implementada no GrupoService
- **Hard delete:** nunca executado via API; apenas o time de DBA pode remover registros diretamente no banco em casos excepcionais e documentados
- **Soft delete de vinculos:** a mesma estrategia se aplica a UsuariosGrupo — desvinculo de usuario faz UPDATE Ativo=0, nao DELETE do registro

---

## Historico de revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 19/05/2026 | Henry Komatsu | Criacao do documento; decisoes GDE-001 (Dapper) e GDE-002 (Soft Delete) tomadas no Kickoff e formalizadas com base nas discussoes com Marcos Ferreira (PO) e Bruno Almeida (Dev) |
