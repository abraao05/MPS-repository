# Registro de Capacitação da Equipe — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | CAP-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.2 |
| **Data** | 01/07/2026 |
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

| Papel | Colaborador | Competências | Situação | Critério de Avaliação |
|---|---|---|---|---|
| Gerente de Projeto | Abraão Oliveira | Gestão ágil, GPR, comunicação com o cliente | ✅ | Experiência comprovada em projetos anteriores Timeware (ms.auxo.notificacoes, ms.auxo.relatorios) + histórico de entregas no sistema Gerenciador AASP |
| Tech Lead / Arquiteto / GCO | Cezar Hiraki | C-01, C-02, C-03, C-04, C-05, C-07 | ✅ | Avaliação técnica na contratação; experiência demonstrada em projetos Timeware com stack .NET + Dapper + SQL Server; certificação em arquitetura de microsserviços |
| Desenvolvedor | Renan Kiyoshi | C-01, C-02, C-05, C-06 | ✅ | Trabalho anterior no Gerenciador AASP (ms.auxo.usuarios — módulo legado); experiência comprovada com .NET 5.0, Dapper e xUnit |
| Desenvolvedor | Henry Komatsu | C-01, C-02, C-05, C-06 | ✅ | Experiência comprovada em projetos .NET 5.0 Timeware; participação em revisão técnica de código do Gerenciador AASP |
| Desenvolvedor | Mateus Veloso | C-01, C-02, C-05, C-06 | ✅ | Experiência comprovada em projetos .NET 5.0 Timeware; participação em módulos Dapper + SQL Server no ecossistema Gerenciador AASP |

---

## 4. Ações de capacitação

A equipe alocada já possuía as competências necessárias à stack e ao domínio do projeto, evidenciadas pela experiência prévia em módulos do sistema Gerenciador AASP (Dapper e .NET 5.0 (net5.0) como padrão estabelecido — ver GDE-AASP01-001). Não foi identificada necessidade de treinamento formal específico para o início do projeto.

| Necessidade | Ação | Situação | Evidência |
|---|---|---|---|
| Alinhamento do contrato de API do ms.temis.vinculos (C-04) | Sessão técnica de alinhamento no início da Sprint 2 (09/06/2026), com Cezar Hiraki (Timeware) e time do cliente AASP; duração: 1h30; resultado: contrato de API do ms.temis.vinculos recebido e entendido; payload de integração definido; ver ADAP A-03 e ITP-AASP01-001 §4.1 | Realizada (09/06/2026) | Registro interno: contrato de API disponibilizado pelo cliente conforme ADAP A-03; implementação realizada nos MRs !6 e !7 (Sprint 2). |

> A avaliação de eficácia das ações de capacitação é consolidada no encerramento do projeto. Para ações de curta duração e baixo impacto (como alinhamentos técnicos de sessão única), a avaliação formal de eficácia é dispensável quando o resultado pode ser verificado pela entrega (AG-24 implementado e aceito na Sprint 2).

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 19/05/2026 | Abraão Oliveira | Identificação das competências do projeto e situação da equipe (início do projeto) |
| 1.1 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
| 1.2 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: coluna "Critério de avaliação" adicionada à matriz de competências; evidência da ação C-04 detalhada (participantes, duração, resultado); justificativa de dispensa de eficácia substituída por critério interno verificável. |
