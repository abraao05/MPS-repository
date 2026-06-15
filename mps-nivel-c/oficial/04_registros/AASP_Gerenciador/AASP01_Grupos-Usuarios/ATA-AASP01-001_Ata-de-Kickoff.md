# Ata de Kickoff — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASP01-001 |
| **Projeto** | Grupos de Usuarios — AASP Gerenciador |
| **Cliente** | AASP — Associacao dos Advogados de Sao Paulo |
| **Reuniao** | Kickoff — Inicio formal do projeto |
| **Data** | 19/05/2026 |
| **Horario** | 09h30 – 11h00 |
| **Canal** | Microsoft Teams |
| **Facilitador** | Henry Komatsu (Timeware) |
| **Versao** | 1.0 |
| **Gerente de Projeto** | Henry Komatsu |
| **Processo MPS-SW** | GPR — Gerencia de Projetos (evidencia de projeto) |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Henry Komatsu | Timeware | Gerente de Projeto / Tech Lead / Facilitador |
| Bruno Almeida | Timeware | Desenvolvedor Junior |
| Marcos Ferreira | AASP | Product Owner / Representante do Cliente |
| Renata Souza | AASP | QA / Homologadora |

---

## 2. Pauta

1. Apresentacao da equipe Timeware ao time AASP
2. Revisao do escopo e objetivos — Feature AG (Grupos de Usuarios)
3. Arquitetura tecnica da solucao (stack, banco de dados, integracoes)
4. Cadencia de trabalho (sprints, cerimonias, canais de comunicacao)
5. Gestao de acessos: Azure DevOps, banco auxo3, ambiente de homologacao
6. Alinhamentos sobre o banco auxo3 (schema existente, restricoes)
7. Proximos passos e acoes imediatas

---

## 3. Resumo das Discussoes

### 3.1 Apresentacao da Equipe e Alinhamento de Papeis

Henry Komatsu abriu a reuniao apresentando a equipe Timeware responsavel pela entrega da Feature AG: Henry como Gerente de Projeto e Tech Lead, e Bruno Almeida como Desenvolvedor Junior. Marcos Ferreira foi apresentado como Product Owner da AASP e principal tomador de decisoes de negocio para o projeto. Renata Souza ficou estabelecida como responsavel pela execucao dos testes de homologacao e pelo aceite tecnico dos entregaveis. Ficou acordado que Henry Komatsu e Marcos Ferreira seriam os pontos focais primarios de comunicacao entre Timeware e AASP.

### 3.2 Revisao do Escopo

Henry Komatsu apresentou o escopo completo da Feature AG — Grupos de Usuarios, que compreende:

- **CRUD de Grupos**: criacao, leitura, atualizacao e exclusao (soft delete) de grupos de usuarios
- **Controle de Permissoes RBAC**: vinculacao de permissoes a grupos, habilitando controle de acesso baseado em funcoes
- **Vinculacao Usuario-Grupo**: endpoints para adicionar e remover usuarios de grupos
- **Auditoria**: registro de acoes sobre grupos e permissoes
- **Integracao com ms.temis.vinculos**: consumo do microservico de vinculos para validacoes de acesso
- **Relatorios**: listagens e consultas de grupos e seus membros

Marcos Ferreira confirmou os objetivos de negocio e reafirmou a criticidade do controle de acesso por grupo para a operacao do sistema Gerenciador pela AASP. O microservico sera entregue como `ms.auxo.gruposusuarios`, consumido internamente pelo Gerenciador.

### 3.3 Arquitetura Tecnica

Henry Komatsu apresentou a proposta de arquitetura tecnica:

- **Framework**: ASP.NET Core Web API (.NET Framework 4.7.2)
- **ORM**: Dapper (decisao tomada na reuniao — ver D-01 e GDE-001)
- **Banco de dados**: SQL Server — banco `auxo3` (banco existente do Gerenciador AASP)
- **Branching**: Git Flow no repositorio Azure DevOps (`ms.auxo.gruposusuarios`)
- **Autenticacao**: JWT Bearer Token em todos os endpoints (D-05)
- **Configuracao**: connection strings via variaveis de ambiente, sem hardcode (D-06)

Marcos Ferreira confirmou que o banco `auxo3` e o repositorio Azure DevOps estao disponiveis e serao compartilhados com a equipe Timeware ate 23/05/2026. Bruno Almeida levantou a questao sobre soft delete versus hard delete para grupos. Apos discussao sobre integridade referencial e rastreabilidade auditavel exigida pelo MPS-SW, ficou decidido pelo soft delete via campo `Ativo = false` (D-02 — GDE-002).

### 3.4 Cadencia de Trabalho

Ficou estabelecida a seguinte cadencia de trabalho para todo o projeto:

- **Daily Standup**: todos os dias uteis as 09h30 via Microsoft Teams (todas as partes — Henry, Bruno, quando necessario Marcos e Renata)
- **Sprint**: duracao de 2 semanas; Sprint 1 com inicio em 26/05/2026
- **Sprint Planning**: segunda-feira de abertura do sprint (Henry + Bruno, com alinhamento previo com Marcos)
- **Sprint Review / Demo**: sexta-feira de encerramento do sprint, as 14h00 via Teams, com participacao obrigatoria de Marcos Ferreira e Renata Souza
- **Relatorio de Status Semanal**: Henry Komatsu envia email de status a Marcos Ferreira toda sexta-feira, cobrindo progresso, impedimentos e proximos passos
- **Canal de comunicacao assincronico**: Microsoft Teams (canal do projeto) para duvidas e alinhamentos nao urgentes; urgencias por telefone direto Henry–Marcos

### 3.5 Gestao de Acessos

Marcos Ferreira confirmou que os seguintes acessos seriam providenciados ate **23/05/2026**:

- Acesso ao repositorio Azure DevOps (`ms.auxo.gruposusuarios`) para Henry Komatsu e Bruno Almeida
- Acesso ao banco `auxo3` (ambiente dev) para Henry Komatsu e Bruno Almeida
- Documentacao do contrato de API do `ms.temis.vinculos` (microservico de vinculos)

Renata Souza ficou responsavel por preparar o ambiente de homologacao AASP (banco de dados de homologacao e servidor de aplicacao) para estar disponivel no inicio da Sprint 2, em **09/06/2026**, data em que os primeiros testes de homologacao estao previstos.

### 3.6 Schema do Banco auxo3

Henry Komatsu levantou a necessidade de analisar o schema existente do banco `auxo3` para identificar tabelas relevantes e evitar conflitos de nomenclatura ou redundancia. Marcos Ferreira informou que ha uma tabela `Usuarios` no banco, com `UsuarioId` como chave primaria utilizada em todo o sistema Gerenciador. As novas tabelas necessarias para a Feature AG (`Grupos`, `PermissoesGrupo`, `UsuariosGrupo`) serao criadas via scripts de migration versionados no repositorio, garantindo rastreabilidade e reproducibilidade dos ambientes (dev, homologacao, producao). Ficou acordado que Henry Komatsu elaboraria os scripts de migration ate 28/05/2026.

---

## 4. Decisoes Tomadas

| # | Decisao | Responsavel | Referencia |
|---|---|---|---|
| D-01 | Dapper como ORM — escolhido em detrimento do Entity Framework Core por compatibilidade com .NET FW 4.7.2 e por ser o padrao de acesso a dados adotado no projeto Gerenciador AASP | Henry Komatsu | GDE-001 |
| D-02 | Soft Delete para grupos — campo `Ativo = false` ao inves de exclusao fisica; garante integridade referencial e rastreabilidade auditavel conforme requisitos MPS | Henry Komatsu | GDE-002 |
| D-03 | Git Flow como modelo de branching — padrao: `feature/ag-{id}` -> `develop` -> `release` -> `main`; nenhum commit direto em `main` ou `develop` | Henry Komatsu | GCO-AASP01-001 |
| D-04 | Sprint de 2 semanas com daily as 09h30 no Teams; Sprint Review na sexta-feira de encerramento as 14h | Henry Komatsu + Marcos Ferreira | PLA-AASP01-001 |
| D-05 | JWT Bearer Token para autenticacao em todos os endpoints do ms.auxo.gruposusuarios, sem excecao | Henry Komatsu | PCP-AASP01-001 |
| D-06 | Connection strings via variaveis de ambiente — proibido hardcode de strings de conexao no codigo-fonte ou em arquivos commitados | Henry Komatsu | GCO-AASP01-001 |
| D-07 | Aceite formal por sprint realizado por Marcos Ferreira, com participacao de Renata Souza na execucao dos testes de homologacao; aceite documentado em ata | Marcos Ferreira | VV-AASP01-001 |

---

## 5. Acoes Imediatas

| Acao | Responsavel | Prazo |
|---|---|---|
| Providenciar acesso ao repositorio Azure DevOps (ms.auxo.gruposusuarios) para Henry Komatsu e Bruno Almeida | Marcos Ferreira | 23/05/2026 |
| Compartilhar schema do banco auxo3 (tabelas existentes, PKs, FKs relevantes) | Marcos Ferreira | 23/05/2026 |
| Compartilhar contrato de API do ms.temis.vinculos (swagger ou documento de especificacao) | Marcos Ferreira | 23/05/2026 |
| Preparar ambiente de homologacao AASP (banco de dados e servidor de aplicacao) para testes de homologacao | Renata Souza | 09/06/2026 (inicio Sprint 2) |
| Configurar pipeline CI/CD no Azure DevOps (build automatico, execucao de testes unitarios no PR) | Henry Komatsu | 26/05/2026 |
| Criar branches de feature no repositorio: feature/ag-20, feature/ag-21, feature/ag-22 | Bruno Almeida | 26/05/2026 |
| Elaborar scripts de migration para criacao das tabelas Grupos, PermissoesGrupo e UsuariosGrupo no banco auxo3 | Henry Komatsu | 28/05/2026 |
| Enviar convite recorrente do Teams para daily 09h30 (Henry, Bruno, Marcos, Renata) | Henry Komatsu | 19/05/2026 (neste dia) |
| Enviar convite do Teams para Sprint Review Sprint 1 — 06/06/2026 as 14h00 | Henry Komatsu | 19/05/2026 (neste dia) |

---

## 6. Proximos Passos

- **Sprint 1** inicia em **26/05/2026**, com foco na implementacao de AG-20 (CRUD base de grupos: POST /grupos, GET /grupos, GET /grupos/{id}, PUT /grupos/{id}, DELETE /grupos/{id})
- **Proxima reuniao formal**: Sprint Review Sprint 1 — **06/06/2026 as 14h00** via Microsoft Teams, com Marcos Ferreira e Renata Souza
- Equipe Timeware iniciara o setup do projeto (.NET FW 4.7.2, Dapper, estrutura de pastas, pipeline CI) imediatamente apos recebimento dos acessos (previsto 23/05/2026)

---

## Historico de Revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 19/05/2026 | Henry Komatsu | Versao inicial — registro da reuniao de kickoff realizada em 19/05/2026 |
