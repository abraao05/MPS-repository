# Plano de Verificação e Validação — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | VV-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 26/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | VV — Verificação e Validação (evidência de projeto) |

---

## 1. Objetivo

Definir a estratégia e as atividades de Verificação e Validação (V&V) do microserviço `ms.auxo.gruposusuarios`, garantindo que o produto:

- **Verificação**: atende aos requisitos especificados nos documentos REQ-AASP01-001 e PCP-AASP01-001 (design técnico)
- **Validação**: atende as necessidades reais do negócio AASP, conforme acordado com o Product Owner Marcos Turnes e validado por Leonardo Francisco Pereira

Este plano e aplicado a todos os sprints do projeto (S1 a S4) e constitui evidência obrigatória do processo VV do MPS-SW nível C.

---

## 2. Escopo do Plano

Este documento cobre todas as atividades de V&V desde:

- Testes unitários realizados durante o desenvolvimento (nível de método e classe)
- Testes de integração com banco de dados e com o microserviço `ms.temis.vinculos`
- Code review técnico (peer review) em Pull Requests no Azure DevOps
- Testes de sistema via Swagger UI e Postman
- Testes de homologação (UAT) executados por Leonardo Francisco Pereira em ambiente AASP
- Aceite formal por sprint realizado por Marcos Turnes

O escopo funcional cobre todos os requisitos funcionais AG-20 a AG-25 definidos em REQ-AASP01-001, distribuidos nas sprints S1 a S4.

---

## 3. Estratégia de Verificação e Validação

### 3.1 Níveis de Teste

| Nível | Tipo | Responsável | Ferramenta | Critério de Entrada | Critério de Saída |
|---|---|---|---|---|---|
| 1 | Testes Unitários | Cézar Velázquez + Renan Kioshi (Timeware) | xUnit (.NET FW 4.7.2) + Moq | Feature implementada em branch de feature; build local verde | Cobertura >= 80% nas camadas de serviço (GruposService, PermissoesService) e repositório (GruposRepository); todos os testes passando sem falha |
| 2 | Testes de Integração | Cézar Velázquez (Timeware) | xUnit + SQL Server local (scripts de setup de banco de teste) | Testes unitários passando; banco de teste configurado | Todos os fluxos críticos (CRUD de grupos, associação de permissões, vínculo usuário-grupo, integração com ms.temis.vinculos) executados sem falha |
| 3 | Code Review (peer review) | Cézar Velázquez como revisor principal | Azure DevOps Pull Requests + checklist de revisão | PR aberto; pipeline CI verde (build + testes unitários passando) | PR aprovado formalmente por Cézar Velázquez (Tech Lead); todos os achados P1 e P2 resolvidos antes da aprovação |
| 4 | Testes de Sistema | Cézar Velázquez via Swagger UI / Postman | Swagger UI (gerado automaticamente) + Postman | Feature integrada em ambiente dev; PR mergeado em develop | Todos os endpoints respondem com status HTTP correto; payloads de resposta conformes ao contrato de API; autenticação JWT funcionando |
| 5 | Testes de Homologação (UAT) | Leonardo Francisco Pereira (AASP) + Cézar Velázquez (suporte) | Roteiros CTQ-AASP01-001 + ambiente de homologação AASP | Ambiente de homologação disponível; roteiros de teste aprovados em conjunto (Abraão Oliveira e Leonardo Francisco Pereira); build deployado em homologação. | >= 95% dos cenários críticos aprovados; todos os cenários P1 (críticos) aprovados sem ressalvas |
| 6 | Aceite Formal | Marcos Turnes (AASP, Product Owner) | Ata de aceite documentada (ATA-AASP01-00X) | Testes de homologação com >= 95% aprovação; relatório de execução emitido | Aceite formal registrado em ata e assinado por Marcos Turnes; versão do entregável congelada no repositório |

### 3.2 Critérios de Qualidade do Projeto

| Critério | Meta | Referência |
|---|---|---|
| Cobertura de testes unitários | >= 80% nas camadas de serviço e repositório | REQ RNF-05 (REQ-AASP01-001) |
| Cenários de homologação aprovados (críticos) | 100% dos cenários P1 aprovados; >= 95% do total | Acordo formalizado com AASP no Kickoff (ATA-AASP01-001) |
| Defeitos críticos (P1) em produção ou homologação | 0 antes do aceite formal | Meta de qualidade do projeto |
| Defeitos P2 em homologação | 0 não resolvidos antes do aceite | Meta de qualidade do projeto |
| Tempo de resposta API (percentil 95) | <= 500 ms para todos os endpoints | REQ RNF-01 (REQ-AASP01-001) |
| Rastreabilidade requisito para teste | 100% para todos os RFs entregues na sprint | RASTR-AASP01-001 |
| Desvio de SP por sprint | <= 10% | PLA-AASP01-001 |

---

## 4. Atividades de V&V por Sprint

| Sprint | Escopo Funcional | Atividades de V&V | Responsável | Status |
|---|---|---|---|---|
| Sprint 1 (26/05–06/06) | AG-20: CRUD base de grupos; AG-21: controle de permissões RBAC; AG-22: vinculação usuário-grupo | Testes unitários AG-20, AG-21, AG-22 (meta >= 80% cobertura); code review PRs #11, #12, #13, #14, #15; testes de sistema via Swagger (GET, POST, PUT, DELETE /grupos e endpoints de permissões e vínculos); UAT Leonardo Francisco Pereira (10 cenários CTQ); aceite formal Marcos Turnes | Renan Kioshi, Henry Komatsu e Mateus Veloso + Leonardo Francisco Pereira + Marcos Turnes | Concluido (aceite 06/06/2026) |
| Sprint 2 (09/06–20/06) | AG-23: auditoria de acoes; AG-24: integração com ms.temis.vinculos | Testes unitários AG-23, AG-24; testes de integração ms.temis.vinculos (mock + real); code review PRs #16, #17 (previstos); testes de sistema em ambiente dev; UAT Leonardo Francisco Pereira; aceite formal Marcos Turnes | Renan Kioshi, Henry Komatsu e Mateus Veloso + Leonardo Francisco Pereira + Marcos Turnes | Em andamento |
| Sprint 3 (23/06–04/07) | AG-25: relatórios e listagens avançadas | Testes unitários AG-25; testes de sistema (Swagger + Postman); UAT completo (Leonardo Francisco Pereira) com roteiros de regressão de AG-20 a AG-25; preparação para aceite final | Renan Kioshi, Henry Komatsu e Mateus Veloso + Leonardo Francisco Pereira | Planejado |
| Sprint 4 (07/07–11/07) | Encerramento, estabilização, documentação final | Homologação final completa; regressão completa de todos os endpoints (AG-20 a AG-25); correção de eventuais defeitos remanescentes; aceite formal de encerramento | Cézar Velázquez + Leonardo Francisco Pereira + Marcos Turnes | Planejado |

---

## 5. Critérios de Entrada e Saída por Sprint

### Critérios de Entrada (para início das atividades de V&V da sprint)

1. Feature funcional implementada no branch de feature correspondente
2. Pipeline CI verde: build sem erros + todos os testes unitários passando
3. Pull Request aberto no Azure DevOps com descrição das mudanças
4. Scripts de migration (quando aplicável) validados em banco local

### Critérios de Saída (para encerramento e aceite da sprint)

1. Todos os testes unitários passando; cobertura >= 80%
2. Todos os testes de integração passando sem falha
3. Code review aprovado por Cézar Velázquez (Tech Lead); achados P1 e P2 resolvidos
4. Testes de sistema (Swagger / Postman) sem anomalias nos contratos de API
5. UAT executado por Leonardo Francisco Pereira com >= 95% de aprovação (100% dos cenários P1)
6. Aceite formal documentado em ata por Marcos Turnes

---

## 6. Gestao de Defeitos Encontrados

### 6.1 Classificação de Severidade

| Severidade | Descrição | Impacto | Bloqueio de merge |
|---|---|---|---|
| P1 — Crítico | Defeito que impede o funcionamento do fluxo principal ou causa perda de dados | Alto — bloqueia entrega | Sim |
| P2 — Alto | Defeito que afeta funcionalidade importante sem workaround simples | Médio-alto | Sim |
| P3 — Médio | Defeito com workaround disponível ou impacto limitado a cenário específico | Médio | Não (deve ser resolvido antes do aceite) |
| P4 — Baixo | Inconsistência menor, problema estetico ou melhoria | Baixo | Não |

### 6.2 Fluxo de Gestao de Defeitos

1. Defeito identificado em code review: registrado como comentário no PR com severidade e descrição
2. Defeito identificado em UAT: registrado por Leonardo Francisco Pereira no Azure DevOps Boards com ID, descrição, severidade e evidência
3. Desenvolvedor (Renan / Henry / Mateus Veloso) corrige e registra a resolução no item de trabalho
4. Cézar Velázquez verifica a correção antes de re-aprovar o PR ou liberar para novo ciclo de UAT
5. Defeitos P1 e P2 devem ser resolvidos e re-validados antes de qualquer merge em `develop`

### 6.3 Histórico de Defeitos

| Sprint | ID Defeito | Tipo | Severidade | Descrição | Resolvido | PR / Referência |
|---|---|---|---|---|---|---|
| Sprint 1 | RV-001-01 | Code Review | P2 | Validação de nome duplicado ausente no POST /grupos (retornava exceção do banco em vez de HTTP 409) | Sim (antes do merge) | PR #11 |
| Sprint 1 | RV-001-02 | Code Review | P3 | GET /grupos/{id} retornava HTTP 500 em vez de HTTP 404 para id inexistente | Sim (antes do merge) | PR #12 |
| Sprint 1 | RV-002-01 | Code Review | P2 | Enum de permissão validado apenas no banco; valores inválidos lançavam exceção SQL em vez de HTTP 400 | Sim (antes do merge) | PR #13 |
| Sprint 1 | RV-003-01 | Code Review | P2 | Falta de validação de usuário ativo antes de vincular (permitia vincular usuário inativo) | Sim (antes do merge) | PR #14 |
| Sprint 1 | RV-003-02 | Code Review | P3 | DELETE de vínculo não retornava HTTP 404 amigável quando o vínculo não existia | Sim (antes do merge) | PR #15 |

> Detalhes completos de cada achado disponível em REV-AASP01-001 (Registro de Revisão Técnica). Nenhum defeito aberto em produção ou homologação ao termino da Sprint 1.

---

## 7. Ferramentas e Ambientes

| Ferramenta / Ambiente | Uso | Responsável pela Manutenção |
|---|---|---|
| xUnit (.NET FW 4.7.2) + Moq | Testes unitários e de integração automatizados | Cézar Velázquez |
| Swagger UI (Swashbuckle) | Testes de sistema manuais; documentação automática da API | Cézar Velázquez |
| Postman | Testes de sistema e contratuais; coleção de endpoints exportável | Cézar Velázquez |
| Azure DevOps Pull Requests + pipeline CI | Code review, gate de qualidade (build + testes), rastreabilidade de mudanças | Cézar Velázquez (configuração do pipeline) |
| SQL Server Express (ambiente dev local) | Banco de dados para testes unitários e de integração em ambiente local | Renan Kioshi, Henry Komatsu e Mateus Veloso |
| Ambiente de homologação AASP (banco + servidor) | UAT e aceite formal por sprint; ambiente espelhado da produção | Leonardo Francisco Pereira (AASP) |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Versão inicial — plano de V&V elaborado no início da Sprint 1, cobrindo estratégia, níveis de teste e critérios para todas as sprints do projeto |
