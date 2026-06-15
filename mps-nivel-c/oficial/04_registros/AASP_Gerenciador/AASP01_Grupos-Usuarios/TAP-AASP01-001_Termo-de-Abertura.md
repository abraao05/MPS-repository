# TAP-AASP01-001 — Termo de Abertura do Projeto

| Campo         | Valor                                                                 |
|---------------|-----------------------------------------------------------------------|
| Documento     | TAP-AASP01-001                                                        |
| Projeto       | AASP01 — Grupos de Usuários (Feature AG)                              |
| Cliente       | AASP — Associação dos Advogados de São Paulo                          |
| Produto       | ms.auxo.gruposusuarios                                                |
| Versão        | 1.0                                                                   |
| Data          | 19/05/2026                                                            |
| Autor         | Abraão                                                         |
| Status        | Aprovado                                                              |

---

## 1. Objetivo do Projeto

Desenvolver o microsserviço **ms.auxo.gruposusuarios** para o sistema Gerenciador da AASP, permitindo a criação e gestão de grupos de usuários com controle de permissões RBAC e vínculos usuário↔grupo, integrado ao ecossistema existente da AASP.

## 2. Escopo

### 2.1 Incluído

| # | Entrega |
|---|---------|
| 1 | CRUD completo de grupos de usuários |
| 2 | Permissões por grupo (modelo RBAC) |
| 3 | Vinculação usuário↔grupo (inclusão e remoção) |
| 4 | Auditoria e log de operações em tabela `AuditoriaGrupos` |
| 5 | Integração com `ms.temis.vinculos` via HTTP |
| 6 | Relatórios consolidados com exportação CSV |
| 7 | Endpoints RESTful documentados (Swagger) |
| 8 | Testes unitários e de integração por sprint |

### 2.2 Não Incluído

- Modernização ou refatoração de outros módulos do sistema Gerenciador
- Sustentação e manutenção pós-entrega do microsserviço
- Desenvolvimento de frontend ou interface gráfica para o módulo

## 3. Partes Interessadas

| Papel                   | Nome             | Organização | Contato                          |
|-------------------------|------------------|-------------|----------------------------------|
| PO / Patrocinador        | Marcos Turnes  | AASP        | —                                |
| QA                      | Leonardo Francisco Pereira     | AASP        | —                                |
| Gerente de Projeto / TL | Abraão (GP) · Cezar Hiraki (TL)    | Timeware    | Abraão (a confirmar) · contato@cezarvelazquez.com.br |
| Desenvolvedor           | Renan Kiyoshi    | Timeware    | renan.kiyoshi.timeware@outlook.com |
| Desenvolvedor           | Henry Komatsu    | Timeware    | henry.komatsu.timeware@outlook.com |
| Desenvolvedor           | Mateus Veloso           | Timeware    | mateus.veloso.timeware@outlook.com |

## 4. Macroplanejamento

| Marco                | Data                  | Observação                              |
|----------------------|-----------------------|-----------------------------------------|
| Kickoff              | 19/05/2026            | Realizado — ver ATA-AASP01-001          |
| Sprint 1 — início    | 26/05/2026            | —                                       |
| Sprint 1 — fim       | 06/06/2026            | ✅ Concluída — aceite Marcos Turnes   |
| Sprint 2 — início    | 09/06/2026            | Em andamento                            |
| Sprint 2 — fim       | 20/06/2026            | —                                       |
| Sprint 3 — início    | 23/06/2026            | Planejada                               |
| Sprint 3 — fim       | 04/07/2026            | —                                       |
| Sprint 4 — início    | 07/07/2026            | Encerramento                            |
| Sprint 4 — fim       | 11/07/2026            | —                                       |
| Encerramento         | ~11/07/2026           | —                                       |

## 5. Premissas

- Ambiente SQL Server disponível e acessível para as equipes durante o projeto
- Acesso ao repositório Azure DevOps (`komatsuhenry67/gerenciador-aasp/ms.auxo.gruposusuarios`) concedido a todos os membros da equipe antes do início da Sprint 1
- Banco de dados `auxo3` acessível e com schema atualizado
- Schema e contrato de integração do `ms.temis.vinculos` documentados e disponibilizados pela AASP antes da Sprint 2

## 6. Restrições

- Stack obrigatória: **.NET Framework 4.7.2** — migração para .NET 8 ou superior fora do escopo
- ORM: **Dapper** — uso de Entity Framework Core não autorizado
- Escopo limitado à feature AG (Grupos de Usuários); quaisquer outras demandas devem ser tratadas como novo projeto ou change request formal

## 7. Referências

| Documento        | Descrição                          |
|------------------|------------------------------------|
| ATA-AASP01-001   | Ata de Reunião de Kickoff          |
| REQ-AASP01-001   | Documento de Requisitos            |
| PLA-AASP01-001   | Plano de Projeto                   |

---

## Histórico de Revisões

| Versão | Data       | Autor          | Descrição             |
|--------|------------|----------------|-----------------------|
| 1.0    | 19/05/2026 | Abraão  | Criação do documento  |
