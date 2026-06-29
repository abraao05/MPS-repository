# Ata de Kickoff — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Reunião** | Kickoff — Inicio formal do projeto |
| **Data** | 24/06/2026 |
| **Horario** | 09h30 – 11h00 |
| **Canal** | Microsoft Teams |
| **Facilitador** | Abraão (Timeware) |
| **Versão** | 1.1 |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | GPR — Gerência de Projetos (evidência de projeto) |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão · Cezar Hiraki | Timeware | GP (Abraão) · Arquiteto/Tech Lead (Cezar) · Facilitador |
| Renan Kiyoshi | Timeware | Desenvolvedor |
| Henry Komatsu | Timeware | Desenvolvedor |
| Mateus Veloso | Timeware | Desenvolvedor |
| Marcos Turnes | AASP | Product Owner / Representante do Cliente |
| Caroline Sousa | AASP | QA / Homologadora |

---

## 2. Pauta

1. Apresentação da equipe Timeware ao time AASP
2. Revisão do escopo e objetivos — Feature AG (Grupos de Usuários)
3. Arquitetura técnica da solução (stack, banco de dados, integrações)
4. Cadência de trabalho (sprints, cerimonias, canais de comunicação)
5. Gestão de acessos: GitLab, banco auxo3, ambiente de homologação
6. Alinhamentos sobre o banco auxo3 (schema existente, restrições)
7. Proximos passos e ações imediatas

---

## 3. Resumo das Discussões

### 3.1 Apresentação da Equipe e Alinhamento de Papeis

Abraão abriu a reunião apresentando a equipe Timeware responsável pela entrega da Feature AG: Abraão como Gerente de Projeto, Cezar Hiraki como Arquiteto e Tech Lead, e Renan Kiyoshi, Henry Komatsu e Mateus Veloso como desenvolvedores. Marcos Turnes foi apresentado como Product Owner da AASP e principal tomador de decisões de negocio para o projeto. Caroline Sousa ficou estabelecida como responsável pela execução dos testes de homologação e pelo aceite técnico dos entregaveis. Ficou acordado que Abraão e Marcos Turnes seriam os pontos focais primarios de comunicação entre Timeware e AASP.

### 3.2 Revisão do Escopo

Abraão apresentou o escopo completo da Feature AG — Grupos de Usuários, que compreende:

- **CRUD de Grupos**: criação, leitura, atualização e exclusão (soft delete) de grupos de usuários
- **Função do usuário no grupo**: definição do papel de cada usuário no grupo (Usuario ou Administrador)
- **Vinculação Usuario-Grupo**: endpoints para adicionar e remover usuários de grupos
- **Auditoria** (planejada): registro de ações sobre grupos e membros
- **Integração com ms.temis.vinculos**: consumo do microserviço de vinculos para validações de acesso
- **Relatórios**: listagens e consultas de grupos e seus membros

Marcos Turnes confirmou os objetivos de negocio e reafirmou a criticidade do controle de acesso por grupo para a operação do sistema Gerenciador pela AASP. O microserviço será entregue como `ms.auxo.usuarios`, consumido internamente pelo Gerenciador.

### 3.3 Arquitetura Técnica

Cezar Hiraki apresentou a proposta de arquitetura técnica:

- **Framework**: ASP.NET Core Web API (.NET 5.0 (net5.0))
- **ORM**: Dapper (decisão tomada na reunião — ver D-01 e GDE-001)
- **Banco de dados**: SQL Server — banco `auxo3` (banco existente do Gerenciador AASP)
- **Branching**: Git Flow no repositório GitLab (`ms.auxo.usuarios`)
- **Autenticação**: JWT Bearer Token em todos os endpoints (D-05)
- **Configuração**: connection strings via variáveis de ambiente, sem hardcode (D-06)

Marcos Turnes confirmou que o banco `auxo3` e o repositório GitLab estão disponíveis e serão compartilhados com a equipe Timeware até 23/05/2026. Renan Kiyoshi levantou a questao sobre soft delete versus hard delete para grupos. Após discussão sobre integridade referencial e rastreabilidade auditavel exigida pelo MPS-SW, ficou decidido pelo soft delete via campo `Ativo = false` (D-02 — GDE-002).

### 3.4 Cadência de Trabalho

Ficou estabelecida a seguinte cadência de trabalho para todo o projeto:

- **Daily Standup**: todos os dias úteis as 09h30 via Microsoft Teams (todas as partes — Abraão, Cezar e os desenvolvedores; quando necessário Marcos Turnes e Caroline)
- **Sprint**: duração de 2 semanas; Sprint 1 com inicio em 26/05/2026
- **Sprint Planning**: segunda-feira de abertura do sprint (Abraão e a equipe de desenvolvimento, com alinhamento previo com Marcos Turnes)
- **Sprint Review / Demo**: sexta-feira de encerramento do sprint, as 14h00 via Teams, com participação obrigatória de Marcos Turnes e Caroline Sousa
- **Relatório de Status Semanal**: Abraão envia email de status a Marcos Turnes toda sexta-feira, cobrindo progresso, impedimentos e proximos passos
- **Canal de comunicação assincronico**: Microsoft Teams (canal do projeto) para duvidas e alinhamentos não urgentes; urgências por telefone direto Abraão–Marcos

### 3.5 Gestão de Acessos

Marcos Turnes confirmou que os seguintes acessos seriam providenciados até **23/05/2026**:

- Acesso ao repositório GitLab (`ms.auxo.usuarios`) para Renan Kiyoshi, Henry Komatsu e Mateus Veloso
- Acesso ao banco `auxo3` (ambiente dev) para Renan Kiyoshi, Henry Komatsu e Mateus Veloso
- Documentação do contrato de API do `ms.temis.vinculos` (microserviço de vinculos)

Caroline Sousa ficou responsável por preparar o ambiente de homologação AASP (banco de dados de homologação e servidor de aplicação) para estar disponível no inicio da Sprint 2, em **09/06/2026**, data em que os primeiros testes de homologação estão previstos.

### 3.6 Schema do Banco auxo3

Cezar Hiraki levantou a necessidade de analisar o schema existente do banco `auxo3` para identificar tabelas relevantes e evitar conflitos de nomenclatura ou redundancia. Marcos Turnes informou que há uma tabela `Usuarios` no banco, com `UsuarioId` como chave primaria utilizada em todo o sistema Gerenciador. As novas tabelas necessárias para a Feature AG (`grupos_usuarios`, `grupos_usuarios_vinculos`, `grupos_usuarios_funcao`) serão criadas via scripts de migration versionados no repositório, garantindo rastreabilidade e reproducibilidade dos ambientes (dev, homologação, produção). Ficou acordado que Cezar Hiraki elaboraria os scripts de migration até 28/05/2026.

---

## 4. Decisões Tomadas

| # | Decisão | Responsável | Referência |
|---|---|---|---|
| D-01 | Dapper como ORM — escolhido em detrimento do Entity Framework Core por compatibilidade com .NET FW 5.0 e por ser o padrão de acesso a dados adotado no projeto Gerenciador AASP | Cezar Hiraki | GDE-001 |
| D-02 | Soft Delete para grupos — campo `Ativo = false` ao inves de exclusão física; garante integridade referencial e rastreabilidade auditavel conforme requisitos MPS | Cezar Hiraki | GDE-002 |
| D-03 | Git Flow como modelo de branching — padrão: `feature/ag-{id}` -> `develop` -> `release` -> `main`; nenhum commit direto em `main` ou `develop` | Cezar Hiraki | GCO-AASP01-001 |
| D-04 | Sprint de 2 semanas com daily as 09h30 no Teams; Sprint Review na sexta-feira de encerramento as 14h | Abraão + Marcos Turnes | PLA-AASP01-001 |
| D-05 | JWT Bearer Token para autenticação em todos os endpoints do ms.auxo.usuarios, sem exceção | Cezar Hiraki | PCP-AASP01-001 |
| D-06 | Connection strings via variáveis de ambiente — proibido hardcode de strings de conexão no código-fonte ou em arquivos commitados | Cezar Hiraki | GCO-AASP01-001 |
| D-07 | Aceite formal por sprint realizado por Marcos Turnes, com participação de Caroline Sousa na execução dos testes de homologação; aceite documentado em ata | Marcos Turnes | VV-AASP01-001 |

---

## 5. Ações Imediatas

| Ação | Responsável | Prazo |
|---|---|---|
| Providenciar acesso ao repositório GitLab (ms.auxo.usuarios) para Renan Kiyoshi, Henry Komatsu e Mateus Veloso | Marcos Turnes | 23/05/2026 |
| Compartilhar schema do banco auxo3 (tabelas existentes, PKs, FKs relevantes) | Marcos Turnes | 23/05/2026 |
| Compartilhar contrato de API do ms.temis.vinculos (swagger ou documento de especificação) | Marcos Turnes | 23/05/2026 |
| Preparar ambiente de homologação AASP (banco de dados e servidor de aplicação) para testes de homologação | Caroline Sousa | 09/06/2026 (inicio Sprint 2) |
| Configurar pipeline CI/CD no GitLab (build automático, execução de testes unitarios no MR) | Cezar Hiraki | 26/05/2026 |
| Criar branches de feature no repositório: feature/ag-20, feature/ag-21, feature/ag-22 | Renan Kiyoshi | 26/05/2026 |
| Elaborar scripts de migration para criação das tabelas grupos_usuarios, grupos_usuarios_vinculos e grupos_usuarios_funcao no banco auxo3 | Cezar Hiraki | 28/05/2026 |
| Enviar convite recorrente do Teams para daily 09h30 (equipe Timeware e AASP) | Abraão | 19/05/2026 (neste dia) |
| Enviar convite do Teams para Sprint Review Sprint 1 — 06/06/2026 as 14h00 | Abraão | 19/05/2026 (neste dia) |

---

## 6. Proximos Passos

- **Sprint 1** inicia em **26/05/2026**, com foco na implementação de AG-20 (CRUD base de grupos: incluirgrupo, listargrupo, buscargrupoporid, alterargrupo, excluirgrupo, ativardesativar)
- **Próxima reunião formal**: Sprint Review Sprint 1 — **06/06/2026 as 14h00** via Microsoft Teams, com Marcos Turnes e Caroline Sousa
- Equipe Timeware iniciara o setup do projeto (.NET FW 5.0, Dapper, estrutura de pastas, pipeline CI) imediatamente após recebimento dos acessos (previsto 23/05/2026)

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 19/05/2026 | Abraão | Versão inicial — registro da reunião de kickoff realizada em 19/05/2026 |
| 1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
