# Registro de Capacitação da Equipe — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | CAP-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.1 |
| **Data** | 24/06/2026 |
| **Responsável** | Abraão Oliveira (Gerente de Projeto) |
| **Processo MPS-SW** | CAP — Capacitação (evidência de projeto) |

---

## 1. Objetivo

Registrar a identificação das competências necessárias à execução do projeto AASP01 — Grupos de Usuários e a situação de cada papel da equipe frente a essas competências, conforme o Plano de Capacitação organizacional (PLA-CAP-001). A avaliação foi conduzida no início do projeto, junto à definição da equipe.

---

## 2. Competências necessárias ao projeto

| # | Competência | Justificativa no projeto |
|---|---|---|
| C-01 | .NET 5.0 (net5.0) / ASP.NET Web API | Stack obrigatória do sistema Gerenciador AASP |
| C-02 | Dapper e SQL Server (T-SQL, migrations) | Acesso a dados sobre o banco legado auxo3 |
| C-03 | Arquitetura de microsserviços REST e RBAC | Design do ms.auxo.usuarios e controle de permissões |
| C-04 | Integração HTTP entre serviços (contratos, retry) | Integração com o ms.temis.vinculos |
| C-05 | Git Flow e GitLab (Merge Request, pipeline CI/CD) | Versionamento, code review e gate de qualidade |
| C-06 | Testes automatizados (xUnit, Moq) | Cobertura de testes unitários e de integração |
| C-07 | Segurança de aplicação (JWT, prevenção de SQL Injection) | Autenticação dos endpoints e queries parametrizadas |

---

## 3. Matriz de competências da equipe

Legenda: ✅ competência atendida.

| Papel | Colaborador | Competências | Situação |
|---|---|---|---|
| Gerente de Projeto | Abraão Oliveira | Gestão ágil, GPR, comunicação com o cliente | ✅ |
| Tech Lead / Arquiteto / GCO | Cezar Hiraki | C-01, C-02, C-03, C-04, C-05, C-07 | ✅ |
| Desenvolvedor | Renan Kiyoshi | C-01, C-02, C-05, C-06 | ✅ |
| Desenvolvedor | Henry Komatsu | C-01, C-02, C-05, C-06 | ✅ |
| Desenvolvedor | Mateus Veloso | C-01, C-02, C-05, C-06 | ✅ |

---

## 4. Ações de capacitação

A equipe alocada já possuía as competências necessárias à stack e ao domínio do projeto, evidenciadas pela experiência prévia em módulos do sistema Gerenciador AASP (Dapper e .NET 5.0 (net5.0) como padrão estabelecido — ver GDE-AASP01-001). Não foi identificada necessidade de treinamento formal específico para o início do projeto.

| Necessidade | Ação | Situação |
|---|---|---|
| Alinhamento do contrato de API do ms.temis.vinculos (C-04) | Sessão técnica de alinhamento no início da Sprint 2, com o time do cliente | Realizada (09/06/2026) |

> A avaliação de eficácia das ações de capacitação, quando aplicável, é consolidada no encerramento do projeto (conforme PLA-CAP-001). Para ações de curta duração e baixo impacto, a avaliação formal de eficácia é dispensável (GUIA-GPC-001, §7.2).

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 19/05/2026 | Abraão Oliveira | Identificação das competências do projeto e situação da equipe (início do projeto) |
| 1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
