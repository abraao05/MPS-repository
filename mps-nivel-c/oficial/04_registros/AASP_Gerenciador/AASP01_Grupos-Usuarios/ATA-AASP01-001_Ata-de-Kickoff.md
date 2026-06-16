# Ata de Kickoff — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Reuniao** | Kickoff — Início formal do projeto |
| **Data** | 19/05/2026 |
| **Horário** | 09h30 – 11h00 |
| **Canal** | Microsoft Teams |
| **Facilitador** | Abraão Oliveira (Timeware) |
| **Versão** | 1.0 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR — Gerência de Projetos (evidência de projeto) |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão Oliveira · Cézar Velázquez | Timeware | GP (Abraão Oliveira) · Arquiteto/Tech Lead (Cézar) · Facilitador |
| Renan Kioshi | Timeware | Desenvolvedor |
| Henry Komatsu | Timeware | Desenvolvedor |
| Mateus Veloso | Timeware | Desenvolvedor |
| Marcos Turnes | AASP | Product Owner / Representante do Cliente |
| Leonardo Francisco Pereira | AASP | QA / Homologadora |

---

## 2. Pauta

1. Apresentação da equipe Timeware ao time AASP
2. Revisão do escopo e objetivos — Feature AG (Grupos de Usuários)
3. Arquitetura técnica da solução (stack, banco de dados, integrações)
4. Cadência de trabalho (sprints, cerimonias, canais de comunicação)
5. Gestao de acessos: Azure DevOps, banco auxo3, ambiente de homologação
6. Alinhamentos sobre o banco auxo3 (schema existente, restrições)
7. Próximos passos e acoes imediatas

---

## 3. Resumo das Discussões

### 3.1 Apresentação da Equipe e Alinhamento de Papeis

Abraão Oliveira abriu a reuniao apresentando a equipe Timeware responsável pela entrega da Feature AG: Abraão Oliveira como Gerente de Projeto, Cézar Velázquez como Arquiteto e Tech Lead, e Renan Kioshi, Henry Komatsu e Mateus Veloso como desenvolvedores. Marcos Turnes foi apresentado como Product Owner da AASP e principal tomador de decisões de negócio para o projeto. Leonardo Francisco Pereira ficou estabelecida como responsável pela execução dos testes de homologação e pelo aceite técnico dos entregáveis. Ficou acordado que Abraão Oliveira e Marcos Turnes seriam os pontos focais primários de comunicação entre Timeware e AASP.

### 3.2 Revisão do Escopo

Abraão Oliveira apresentou o escopo completo da Feature AG — Grupos de Usuários, que compreende:

- **CRUD de Grupos**: criação, leitura, atualização e exclusão (soft delete) de grupos de usuários
- **Controle de Permissões RBAC**: vinculação de permissões a grupos, habilitando controle de acesso baseado em funções
- **Vinculação Usuário-Grupo**: endpoints para adicionar e remover usuários de grupos
- **Auditoria**: registro de acoes sobre grupos e permissões
- **Integração com ms.temis.vinculos**: consumo do microserviço de vínculos para validações de acesso
- **Relatórios**: listagens e consultas de grupos e seus membros

Marcos Turnes confirmou os objetivos de negócio e reafirmou a criticidade do controle de acesso por grupo para a operação do sistema Gerenciador pela AASP. O microserviço será entregue como `ms.auxo.gruposusuarios`, consumido internamente pelo Gerenciador.

### 3.3 Arquitetura Técnica

Cézar Velázquez apresentou a proposta de arquitetura técnica:

- **Framework**: ASP.NET Web API (.NET Framework 4.7.2)
- **ORM**: Dapper (decisão tomada na reuniao — ver D-01 e GDE-001)
- **Banco de dados**: SQL Server — banco `auxo3` (banco existente do Gerenciador AASP)
- **Branching**: Git Flow no repositório Azure DevOps (`ms.auxo.gruposusuarios`)
- **Autenticação**: JWT Bearer Token em todos os endpoints (D-05)
- **Configuração**: connection strings via variáveis de ambiente, sem hardcode (D-06)

Marcos Turnes confirmou que o banco `auxo3` e o repositório Azure DevOps estao disponíveis e serao compartilhados com a equipe Timeware até 23/05/2026. Renan Kioshi levantou a questao sobre soft delete versus hard delete para grupos. Após discussão sobre integridade referencial e rastreabilidade auditável exigida pelo MPS-SW, ficou decidido pelo soft delete via campo `Ativo = false` (D-02 — GDE-002).

### 3.4 Cadência de Trabalho

Ficou estabelecida a seguinte cadência de trabalho para todo o projeto:

- **Daily Standup**: todos os dias úteis as 09h30 via Microsoft Teams (todas as partes — Abraão Oliveira, Cézar e os desenvolvedores; quando necessário Marcos Turnes e Leonardo)
- **Sprint**: duração de 2 semanas; Sprint 1 com início em 26/05/2026
- **Sprint Planning**: segunda-feira de abertura do sprint (Abraão Oliveira e a equipe de desenvolvimento, com alinhamento prévio com Marcos Turnes)
- **Sprint Review / Demo**: sexta-feira de encerramento do sprint, as 14h00 via Teams, com participação obrigatória de Marcos Turnes e Leonardo Francisco Pereira
- **Relatório de Status Semanal**: Abraão Oliveira envia email de status a Marcos Turnes toda sexta-feira, cobrindo progresso, impedimentos e próximos passos
- **Canal de comunicação assincronico**: Microsoft Teams (canal do projeto) para dúvidas e alinhamentos não urgentes; urgências por telefone direto Abraão Oliveira–Marcos

### 3.5 Gestao de Acessos

Marcos Turnes confirmou que os seguintes acessos seriam providenciados até **23/05/2026**:

- Acesso ao repositório Azure DevOps (`ms.auxo.gruposusuarios`) para Renan Kioshi, Henry Komatsu e Mateus Veloso
- Acesso ao banco `auxo3` (ambiente dev) para Renan Kioshi, Henry Komatsu e Mateus Veloso
- Documentação do contrato de API do `ms.temis.vinculos` (microserviço de vínculos)

Leonardo Francisco Pereira ficou responsável por preparar o ambiente de homologação AASP (banco de dados de homologação e servidor de aplicação) para estar disponível no início da Sprint 2, em **09/06/2026**, data em que os primeiros testes de homologação estao previstos.

### 3.6 Schema do Banco auxo3

Cézar Velázquez levantou a necessidade de analisar o schema existente do banco `auxo3` para identificar tabelas relevantes e evitar conflitos de nomenclatura ou redundância. Marcos Turnes informou que ha uma tabela `Usuarios` no banco, com `UsuarioId` como chave primária utilizada em todo o sistema Gerenciador. As novas tabelas necessárias para a Feature AG (`Grupos`, `PermissoesGrupo`, `UsuariosGrupo`) serao criadas via scripts de migration versionados no repositório, garantindo rastreabilidade e reproducibilidade dos ambientes (dev, homologação, produção). Ficou acordado que Cézar Velázquez elaboraria os scripts de migration até 28/05/2026.

---

## 4. Decisões Tomadas

| # | Decisão | Responsável | Referência |
|---|---|---|---|
| D-01 | Dapper como ORM — escolhido em detrimento do Entity Framework Core por compatibilidade com .NET FW 4.7.2 e por ser o padrão de acesso a dados adotado no projeto Gerenciador AASP | Cézar Velázquez | GDE-001 |
| D-02 | Soft Delete para grupos — campo `Ativo = false` ao inves de exclusão física; garante integridade referencial e rastreabilidade auditável conforme requisitos MPS | Cézar Velázquez | GDE-002 |
| D-03 | Git Flow como modelo de branching — padrão: `feature/ag-{id}` -> `develop` -> `release` -> `main`; nenhum commit direto em `main` ou `develop` | Cézar Velázquez | GCO-AASP01-001 |
| D-04 | Sprint de 2 semanas com daily as 09h30 no Teams; Sprint Review na sexta-feira de encerramento as 14h | Abraão Oliveira + Marcos Turnes | PLA-AASP01-001 |
| D-05 | JWT Bearer Token para autenticação em todos os endpoints do ms.auxo.gruposusuarios, sem exceção | Cézar Velázquez | PCP-AASP01-001 |
| D-06 | Connection strings via variáveis de ambiente — proibido hardcode de strings de conexao no código-fonte ou em arquivos commitados | Cézar Velázquez | GCO-AASP01-001 |
| D-07 | Aceite formal por sprint realizado por Marcos Turnes, com participação de Leonardo Francisco Pereira na execução dos testes de homologação; aceite documentado em ata | Marcos Turnes | VV-AASP01-001 |

---

## 5. Acoes Imediatas

| Acao | Responsável | Prazo |
|---|---|---|
| Providenciar acesso ao repositório Azure DevOps (ms.auxo.gruposusuarios) para Renan Kioshi, Henry Komatsu e Mateus Veloso | Marcos Turnes | 23/05/2026 |
| Compartilhar schema do banco auxo3 (tabelas existentes, PKs, FKs relevantes) | Marcos Turnes | 23/05/2026 |
| Compartilhar contrato de API do ms.temis.vinculos (swagger ou documento de especificação) | Marcos Turnes | 23/05/2026 |
| Preparar ambiente de homologação AASP (banco de dados e servidor de aplicação) para testes de homologação | Leonardo Francisco Pereira | 09/06/2026 (início Sprint 2) |
| Configurar pipeline CI/CD no Azure DevOps (build automático, execução de testes unitários no PR) | Cézar Velázquez | 26/05/2026 |
| Criar branches de feature no repositório: feature/ag-20, feature/ag-21, feature/ag-22 | Renan Kioshi | 26/05/2026 |
| Elaborar scripts de migration para criação das tabelas Grupos, PermissoesGrupo e UsuariosGrupo no banco auxo3 | Cézar Velázquez | 28/05/2026 |
| Enviar convite recorrente do Teams para daily 09h30 (equipe Timeware e AASP) | Abraão Oliveira | 19/05/2026 (neste dia) |
| Enviar convite do Teams para Sprint Review Sprint 1 — 06/06/2026 as 14h00 | Abraão Oliveira | 19/05/2026 (neste dia) |

---

## 6. Próximos Passos

- **Sprint 1** inicia em **26/05/2026**, com foco na implementação de AG-20 (CRUD base de grupos: POST /grupos, GET /grupos, GET /grupos/{id}, PUT /grupos/{id}, DELETE /grupos/{id})
- **Próxima reuniao formal**: Sprint Review Sprint 1 — **06/06/2026 as 14h00** via Microsoft Teams, com Marcos Turnes e Leonardo Francisco Pereira
- Equipe Timeware iniciará o setup do projeto (.NET FW 4.7.2, Dapper, estrutura de pastas, pipeline CI) imediatamente após recebimento dos acessos (previsto 23/05/2026)

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 19/05/2026 | Abraão Oliveira | Versão inicial — registro da reuniao de kickoff realizada em 19/05/2026 |
