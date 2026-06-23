# Plano de Verificação e Validação — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | VV-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.2 |
| **Data** | 23/06/2026 |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | VER / VAL — Verificação e Validação (evidência de projeto) |

---

## 1. Objetivo

Definir a estratégia e as atividades de Verificação e Validação (V&V) do microserviço `ms.auxo.gruposusuarios`, garantindo que o produto:

- **Verificação**: atende aos requisitos especificados nos documentos REQ-AASP01-001 e PCP-AASP01-001 (design técnico)
- **Validação**: atende as necessidades reais do negocio AASP, conforme acordado com o Product Owner Marcos Turnes e validado por Leonardo Francisco Pereira

Este plano e aplicado a todos os sprints do projeto (S1 a S3) e constitui evidência obrigatória dos processos VER e VAL do MPS-SW nível C.

---

## 2. Escopo do Plano

Este documento cobre todas as atividades de V&V desde:

- Code review técnico (peer review) em Merge Requests no GitLab
- Testes de sistema via Swagger UI e Postman
- Testes de homologação (UAT) executados por Leonardo Francisco Pereira em ambiente AASP
- Aceite formal por sprint realizado por Marcos Turnes

> **Nota:** Testes unitários e de integração automatizados **não se aplicam** a este projeto — o projeto não possui testes automatizados.

O escopo funcional cobre todos os requisitos funcionais AG-20 a AG-25 definidos em REQ-AASP01-001, distribuidos nas sprints S1 a S3.

---

## 3. Estratégia de Verificação e Validação

### 3.1 Níveis de Teste

| Nível | Tipo | Responsável | Ferramenta | Critério de Entrada | Critério de Saida |
|---|---|---|---|---|---|
| 1 | Testes Unitários | N/A | N/A | N/A | **Não se aplica** — o projeto não possui testes unitários automatizados. |
| 2 | Testes de Integração | N/A | N/A | N/A | **Não se aplica** — o projeto não possui testes de integração automatizados. |
| 3 | Code Review (peer review) | Cezar Hiraki como revisor principal | GitLab Merge Requests + checklist de revisão | MR aberto; build verde | MR aprovado formalmente por Cezar Hiraki (Tech Lead); todos os achados P1 e P2 resolvidos antes da aprovação |
| 4 | Testes de Sistema | Cezar Hiraki via Swagger UI / Postman | Swagger UI (gerado automaticamente) + Postman | Feature integrada em ambiente dev; MR mergeado em develop | Todos os endpoints respondem com status HTTP correto (200/400) e envelope padrão; autenticação JWT funcionando |
| 5 | Testes de Homologação (UAT) | Leonardo Francisco Pereira (AASP) + Cezar Hiraki (suporte) | Roteiros CTQ-AASP01-001 + ambiente de homologação AASP | Ambiente de homologação disponível; roteiros de teste aprovados; build deployado em homolog. | >= 95% dos cenários criticos aprovados; todos os cenários P1 (criticos) aprovados sem ressalvas |
| 6 | Aceite Formal | Marcos Turnes (AASP, Product Owner) | Ata de aceite documentada (ATA-AASP01-00X) | Testes de homologação com >= 95% aprovação; relatório de execução emitido | Aceite formal registrado em ata por Marcos Turnes; versão do entregavel congelada no repositório |

### 3.2 Critérios de Qualidade do Projeto

| Critério | Meta | Referência |
|---|---|---|
| Testes unitários automatizados | **Não se aplica** — o projeto não possui testes unitários automatizados | — |
| Cenários de homologação aprovados (criticos) | 100% dos cenários P1 aprovados; >= 95% do total | Acordo formalizado com AASP no Kickoff (ATA-AASP01-001) |
| Defeitos criticos (P1) em produção ou homologação | 0 antes do aceite formal | Meta de qualidade do projeto |
| Defeitos P2 em homologação | 0 não resolvidos antes do aceite | Meta de qualidade do projeto |
| Tempo de resposta API (percentil 95) | <= 500 ms para todos os endpoints | REQ RNF-01 (REQ-AASP01-001) |
| Rastreabilidade requisito para teste | 100% para todos os RFs entregues na sprint | RASTR-AASP01-001 |
| Desvio de SP por sprint | <= 10% | PLA-AASP01-001 |

---

## 4. Atividades de V&V por Sprint

| Sprint | Escopo Funcional | Atividades de V&V | Responsável | Status |
|---|---|---|---|---|
| Sprint 1 (26/05–06/06) | AG-20: CRUD de grupos; AG-21: função do usuário no grupo; AG-22: vinculo usuário-grupo | Code review MRs !1, !2, !3, !4, !5; testes de sistema via Swagger (endpoints GET/POST de `api/gerenciar/grupos`); UAT Leonardo Francisco Pereira (10 cenários CTQ); aceite formal Marcos Turnes | Renan Kiyoshi, Henry Komatsu e Mateus Veloso + Leonardo Francisco Pereira + Marcos Turnes | Concluido (aceite 06/06/2026) |
| Sprint 2 (09/06–20/06) | AG-23: auditoria de ações; AG-24: integração com ms.temis.vinculos | Code review MRs; testes de sistema em ambiente dev; UAT Leonardo Francisco Pereira; aceite formal Marcos Turnes | Renan Kiyoshi, Henry Komatsu e Mateus Veloso + Leonardo Francisco Pereira + Marcos Turnes | Em andamento |
| Sprint 3 (23/06–04/07) | AG-25: relatório consolidado de grupos | Testes de sistema (Swagger + Postman); UAT (Leonardo Francisco Pereira) com regressão de AG-20 a AG-25; preparação para aceite final | Renan Kiyoshi, Henry Komatsu e Mateus Veloso + Leonardo Francisco Pereira | Planejado |

---

## 5. Critérios de Entrada e Saida por Sprint

### Critérios de Entrada (para inicio das atividades de V&V da sprint)

1. Feature funcional implementada no branch de feature correspondente
2. Build sem erros
3. Merge Request aberto no GitLab com descrição das mudanças
4. Scripts de banco de dados (quando aplicável) validados em ambiente local

### Critérios de Saida (para encerramento e aceite da sprint)

1. Testes unitários automatizados: **Não se aplica** — o projeto não possui testes unitários automatizados
2. Testes de integração automatizados: **Não se aplica** — o projeto não possui testes de integração automatizados
3. Code review aprovado por Cezar Hiraki (Tech Lead); achados P1 e P2 resolvidos
4. Testes de sistema (Swagger / Postman) sem anomalias nos contratos de API
5. UAT executado por Leonardo Francisco Pereira com >= 95% de aprovação (100% dos cenários P1)
6. Aceite formal documentado em ata por Marcos Turnes

---

## 6. Gestão de Defeitos Encontrados

### 6.1 Classificação de Severidade

| Severidade | Descrição | Impacto | Bloqueio de merge |
|---|---|---|---|
| P1 — Critico | Defeito que impede o funcionamento do fluxo principal ou causa perda de dados | Alto — bloqueia entrega | Sim |
| P2 — Alto | Defeito que afeta funcionalidade importante sem workaround simples | Medio-alto | Sim |
| P3 — Medio | Defeito com workaround disponível ou impacto limitado a cenário específico | Medio | Não (deve ser resolvido antes do aceite) |
| P4 — Baixo | Inconsistência menor, problema estetico ou melhoria | Baixo | Não |

### 6.2 Fluxo de Gestão de Defeitos

1. Defeito identificado em code review: registrado como comentário no MR com severidade e descrição
2. Defeito identificado em UAT: registrado por Leonardo Francisco Pereira no GitLab Issues com ID, descrição, severidade e evidência
3. Desenvolvedor (Renan / Henry / Mateus Veloso) corrige e registra a resolução no item de trabalho
4. Cezar Hiraki verifica a correção antes de re-aprovar o MR ou liberar para novo ciclo de UAT
5. Defeitos P1 e P2 devem ser resolvidos e re-validados antes de qualquer merge em `develop`

### 6.3 Histórico de Defeitos

| Sprint | ID Defeito | Tipo | Severidade | Descrição | Resolvido | MR / Referência |
|---|---|---|---|---|---|---|
| Sprint 1 | REV-S1-01 | Code Review | P2 | Conforme REV-AASP01-001 (RV-001-01) | Sim (antes do merge) | MR !1 |
| Sprint 1 | REV-S1-02 | Code Review | P3 | Conforme REV-AASP01-001 (RV-001-02) | Sim (antes do merge) | MR !1 |
| Sprint 1 | REV-S1-03 | Code Review | P2 | Conforme REV-AASP01-001 (RV-002-01) | Sim (antes do merge) | MR !3 |
| Sprint 1 | REV-S1-04 | Code Review | P2 | Conforme REV-AASP01-001 (RV-003-01) | Sim (antes do merge) | MR !4 |
| Sprint 1 | REV-S1-05 | Code Review | P3 | Conforme REV-AASP01-001 (RV-003-02) | Sim (antes do merge) | MR !5 |

> Detalhes completos de cada achado disponível em REV-AASP01-001 (Registro de Revisão Técnica). Nenhum defeito aberto em produção ou homologação ao termino da Sprint 1.

---

## 7. Ferramentas e Ambientes

| Ferramenta / Ambiente | Uso | Responsável pela Manutenção |
|---|---|---|
| Testes automatizados (xUnit/Moq) | **Não se aplica** — o projeto não possui testes automatizados | — |
| Swagger UI (Swashbuckle) | Testes de sistema manuais; documentação automática da API | Cezar Hiraki |
| Postman | Testes de sistema e contratuais; coleção de endpoints exportavel | Cezar Hiraki |
| GitLab Merge Requests | Code review, gate de qualidade, rastreabilidade de mudanças | Cezar Hiraki |
| SQL Server (ambiente dev local) | Banco de dados utilizado durante o desenvolvimento | Renan Kiyoshi, Henry Komatsu e Mateus Veloso |
| Ambiente de homologação AASP (banco + servidor) | UAT e aceite formal por sprint; ambiente espelhado da produção | Leonardo Francisco Pereira (AASP) |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão | Versão inicial — plano de V&V elaborado no inicio da Sprint 1 |
| 1.1 | 15/06/2026 | Abraão | Alinhado a API real (endpoints GET/POST 200/400; função do usuário), 3 sprints, nomes reais de service/repositorio |
| 1.2 | 23/06/2026 | Abraão | Testes unitários e de integração marcados como Não se aplica (projeto sem testes automatizados) |
