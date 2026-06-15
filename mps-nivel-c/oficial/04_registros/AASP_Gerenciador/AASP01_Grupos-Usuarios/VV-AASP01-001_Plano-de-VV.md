# Plano de Verificacao e Validacao — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | VV-AASP01-001 |
| **Projeto** | Grupos de Usuarios — AASP Gerenciador |
| **Cliente** | AASP — Associacao dos Advogados de Sao Paulo |
| **Versao** | 1.0 |
| **Data** | 26/05/2026 |
| **Gerente de Projeto** | Henry Komatsu |
| **Processo MPS-SW** | VER / VAL — Verificacao e Validacao (evidencia de projeto) |

---

## 1. Objetivo

Definir a estrategia e as atividades de Verificacao e Validacao (V&V) do microservico `ms.auxo.gruposusuarios`, garantindo que o produto:

- **Verificacao**: atende aos requisitos especificados nos documentos REQ-AASP01-001 e PCP-AASP01-001 (design tecnico)
- **Validacao**: atende as necessidades reais do negocio AASP, conforme acordado com o Product Owner Marcos Ferreira e validado por Renata Souza

Este plano e aplicado a todos os sprints do projeto (S1 a S4) e constitui evidencia obrigatoria dos processos VER e VAL do MPS-SW nivel C.

---

## 2. Escopo do Plano

Este documento cobre todas as atividades de V&V desde:

- Testes unitarios realizados durante o desenvolvimento (nivel de metodo e classe)
- Testes de integracao com banco de dados e com o microservico `ms.temis.vinculos`
- Code review tecnico (peer review) em Pull Requests no Azure DevOps
- Testes de sistema via Swagger UI e Postman
- Testes de homologacao (UAT) executados por Renata Souza em ambiente AASP
- Aceite formal por sprint realizado por Marcos Ferreira

O escopo funcional cobre todos os requisitos funcionais AG-20 a AG-25 definidos em REQ-AASP01-001, distribuidos nas sprints S1 a S4.

---

## 3. Estrategia de Verificacao e Validacao

### 3.1 Niveis de Teste

| Nivel | Tipo | Responsavel | Ferramenta | Criterio de Entrada | Criterio de Saida |
|---|---|---|---|---|---|
| 1 | Testes Unitarios | Henry Komatsu + Bruno Almeida (Timeware) | xUnit (.NET FW 4.7.2) + Moq | Feature implementada em branch de feature; build local verde | Cobertura >= 80% nas camadas de servico (GruposService, PermissoesService) e repositorio (GruposRepository); todos os testes passando sem falha |
| 2 | Testes de Integracao | Henry Komatsu (Timeware) | xUnit + SQL Server local (scripts de setup de banco de teste) | Testes unitarios passando; banco de teste configurado | Todos os fluxos criticos (CRUD de grupos, associacao de permissoes, vinculo usuario-grupo, integracao com ms.temis.vinculos) executados sem falha |
| 3 | Code Review (peer review) | Henry Komatsu como revisor principal | Azure DevOps Pull Requests + checklist de revisao | PR aberto; pipeline CI verde (build + testes unitarios passando) | PR aprovado formalmente por Henry Komatsu (Tech Lead); todos os achados P1 e P2 resolvidos antes da aprovacao |
| 4 | Testes de Sistema | Henry Komatsu via Swagger UI / Postman | Swagger UI (gerado automaticamente) + Postman | Feature integrada em ambiente dev; PR mergeado em develop | Todos os endpoints respondem com status HTTP correto; payloads de resposta conformes ao contrato de API; autenticacao JWT funcionando |
| 5 | Testes de Homologacao (UAT) | Renata Souza (AASP) + Henry Komatsu (suporte) | Roteiros CTQ-AASP01-001 + ambiente de homologacao AASP | Ambiente de homologacao disponivel; roteiros de teste aprovados por Henry; build deployado em homolag. | >= 95% dos cenarios criticos aprovados; todos os cenarios P1 (criticos) aprovados sem ressalvas |
| 6 | Aceite Formal | Marcos Ferreira (AASP, Product Owner) | Ata de aceite documentada (ATA-AASP01-00X) | Testes de homologacao com >= 95% aprovacao; relatorio de execucao emitido | Aceite formal registrado em ata e assinado por Marcos Ferreira; versao do entregavel congelada no repositorio |

### 3.2 Criterios de Qualidade do Projeto

| Criterio | Meta | Referencia |
|---|---|---|
| Cobertura de testes unitarios | >= 80% nas camadas de servico e repositorio | REQ RNF-02 (REQ-AASP01-001) |
| Cenarios de homologacao aprovados (criticos) | 100% dos cenarios P1 aprovados; >= 95% do total | Acordo formalizado com AASP no Kickoff (ATA-AASP01-001) |
| Defeitos criticos (P1) em producao ou homologacao | 0 antes do aceite formal | Meta de qualidade do projeto |
| Defeitos P2 em homologacao | 0 nao resolvidos antes do aceite | Meta de qualidade do projeto |
| Tempo de resposta API (percentil 95) | <= 500 ms para todos os endpoints | REQ RNF-01 (REQ-AASP01-001) |
| Rastreabilidade requisito para teste | 100% para todos os RFs entregues na sprint | RASTR-AASP01-001 |
| Desvio de SP por sprint | <= 10% | PLA-AASP01-001 |

---

## 4. Atividades de V&V por Sprint

| Sprint | Escopo Funcional | Atividades de V&V | Responsavel | Status |
|---|---|---|---|---|
| Sprint 1 (26/05–06/06) | AG-20: CRUD base de grupos; AG-21: controle de permissoes RBAC; AG-22: vinculacao usuario-grupo | Testes unitarios AG-20, AG-21, AG-22 (meta >= 80% cobertura); code review PRs #11, #12, #13, #14, #15; testes de sistema via Swagger (GET, POST, PUT, DELETE /grupos e endpoints de permissoes e vinculos); UAT Renata Souza (10 cenarios CTQ); aceite formal Marcos Ferreira | Henry Komatsu + Bruno Almeida + Renata Souza + Marcos Ferreira | Concluido (aceite 06/06/2026) |
| Sprint 2 (09/06–20/06) | AG-23: auditoria de acoes; AG-24: integracao com ms.temis.vinculos | Testes unitarios AG-23, AG-24; testes de integracao ms.temis.vinculos (mock + real); code review PRs #16, #17 (previstos); testes de sistema em ambiente dev; UAT Renata Souza; aceite formal Marcos Ferreira | Henry Komatsu + Bruno Almeida + Renata Souza + Marcos Ferreira | Em andamento |
| Sprint 3 (23/06–04/07) | AG-25: relatorios e listagens avancadas | Testes unitarios AG-25; testes de sistema (Swagger + Postman); UAT completo (Renata Souza) com roteiros de regressao de AG-20 a AG-25; preparacao para aceite final | Henry Komatsu + Bruno Almeida + Renata Souza | Planejado |
| Sprint 4 (07/07–11/07) | Encerramento, estabilizacao, documentacao final | Homologacao final completa; regressao completa de todos os endpoints (AG-20 a AG-25); correcao de eventuais defeitos remanescentes; aceite formal de encerramento | Henry Komatsu + Renata Souza + Marcos Ferreira | Planejado |

---

## 5. Criterios de Entrada e Saida por Sprint

### Criterios de Entrada (para inicio das atividades de V&V da sprint)

1. Feature funcional implementada no branch de feature correspondente
2. Pipeline CI verde: build sem erros + todos os testes unitarios passando
3. Pull Request aberto no Azure DevOps com descricao das mudancas
4. Scripts de migration (quando aplicavel) validados em banco local

### Criterios de Saida (para encerramento e aceite da sprint)

1. Todos os testes unitarios passando; cobertura >= 80%
2. Todos os testes de integracao passando sem falha
3. Code review aprovado por Henry Komatsu (Tech Lead); achados P1 e P2 resolvidos
4. Testes de sistema (Swagger / Postman) sem anomalias nos contratos de API
5. UAT executado por Renata Souza com >= 95% de aprovacao (100% dos cenarios P1)
6. Aceite formal documentado em ata por Marcos Ferreira

---

## 6. Gestao de Defeitos Encontrados

### 6.1 Classificacao de Severidade

| Severidade | Descricao | Impacto | Bloqueio de merge |
|---|---|---|---|
| P1 — Critico | Defeito que impede o funcionamento do fluxo principal ou causa perda de dados | Alto — bloqueia entrega | Sim |
| P2 — Alto | Defeito que afeta funcionalidade importante sem workaround simples | Medio-alto | Sim |
| P3 — Medio | Defeito com workaround disponivel ou impacto limitado a cenario especifico | Medio | Nao (deve ser resolvido antes do aceite) |
| P4 — Baixo | Inconsistencia menor, problema estetico ou melhoria | Baixo | Nao |

### 6.2 Fluxo de Gestao de Defeitos

1. Defeito identificado em code review: registrado como comentario no PR com severidade e descricao
2. Defeito identificado em UAT: registrado por Renata Souza no Azure DevOps Boards com ID, descricao, severidade e evidencia
3. Desenvolvedor (Bruno / Henry) corrige e registra a resolucao no item de trabalho
4. Henry Komatsu verifica a correcao antes de re-aprovar o PR ou liberar para novo ciclo de UAT
5. Defeitos P1 e P2 devem ser resolvidos e re-validados antes de qualquer merge em `develop`

### 6.3 Historico de Defeitos

| Sprint | ID Defeito | Tipo | Severidade | Descricao | Resolvido | PR / Referencia |
|---|---|---|---|---|---|---|
| Sprint 1 | REV-S1-01 | Code Review | P2 | A apurar — conforme REV-AASP01-001 | Sim (antes do merge) | PR #11 |
| Sprint 1 | REV-S1-02 | Code Review | P2 | A apurar — conforme REV-AASP01-001 | Sim (antes do merge) | PR #12 |
| Sprint 1 | REV-S1-03 | Code Review | P2 | A apurar — conforme REV-AASP01-001 | Sim (antes do merge) | PR #13 |
| Sprint 1 | REV-S1-04 | Code Review | P3 | A apurar — conforme REV-AASP01-001 | Sim (antes do merge) | PR #14 |
| Sprint 1 | REV-S1-05 | Code Review | P3 | A apurar — conforme REV-AASP01-001 | Sim (antes do merge) | PR #15 |

> Detalhes completos de cada achado disponivel em REV-AASP01-001 (Registro de Revisao Tecnica). Nenhum defeito aberto em producao ou homologacao ao termino da Sprint 1.

---

## 7. Ferramentas e Ambientes

| Ferramenta / Ambiente | Uso | Responsavel pela Manutencao |
|---|---|---|
| xUnit (.NET FW 4.7.2) + Moq | Testes unitarios e de integracao automatizados | Henry Komatsu |
| Swagger UI (Swashbuckle) | Testes de sistema manuais; documentacao automatica da API | Henry Komatsu |
| Postman | Testes de sistema e contratuais; colecao de endpoints exportavel | Henry Komatsu |
| Azure DevOps Pull Requests + pipeline CI | Code review, gate de qualidade (build + testes), rastreabilidade de mudancas | Henry Komatsu (configuracao do pipeline) |
| SQL Server Express (ambiente dev local) | Banco de dados para testes unitarios e de integracao em ambiente local | Henry Komatsu + Bruno Almeida |
| Ambiente de homologacao AASP (banco + servidor) | UAT e aceite formal por sprint; ambiente espelhado da producao | Renata Souza (AASP) |

---

## Historico de Revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 26/05/2026 | Henry Komatsu | Versao inicial — plano de V&V elaborado no inicio da Sprint 1, cobrindo estrategia, niveis de teste e criterios para todas as sprints do projeto |
