# PLA-AASP01-001 — Plano de Projeto

| Campo         | Valor                                                                 |
|---------------|-----------------------------------------------------------------------|
| Documento     | PLA-AASP01-001                                                        |
| Projeto       | AASP01 — Grupos de Usuários (Feature AG)                              |
| Cliente       | AASP — Associação dos Advogados de São Paulo                          |
| Produto       | ms.auxo.usuarios                                                |
| Versão        | 1.2                                                                   |
| Data          | 01/07/2026                                                            |
| Autor         | Abraão Oliveira                                                       |
| Status        | Vigente                                                               |

---

## 1. Objetivo do Plano

Este documento define o planejamento executivo do projeto AASP01, estabelecendo cronograma, papéis, plano de comunicação, gestão de riscos, verificação & validação e métricas de sucesso para o desenvolvimento do microsserviço **ms.auxo.usuarios**.

## 2. Escopo e Premissas

O escopo deste plano abrange as Sprints 1 a 3 do projeto, conforme detalhado no TAP-AASP01-001 e nos requisitos RF-01 a RF-09 do REQ-AASP01-001.

**Premissas:**

- Ambiente SQL Server (`auxo3`) disponível e acessível durante todo o projeto
- Acesso ao repositório GitLab concedido antes do início da Sprint 1
- Schema e contrato de integração do `ms.temis.vinculos` disponibilizados antes da Sprint 2
- Dedicação mínima acordada com as partes para reviews e homologação em cada sprint

## 3. Cronograma

| Sprint   | Período               | SP   | Principais Entregas                                              | Status         |
|----------|-----------------------|------|------------------------------------------------------------------|----------------|
| Sprint 1 | 26/05/2026–06/06/2026 | 34   | CRUD grupos (RF-01 a RF-04), Função do usuário (RF-05), Vínculos (RF-06) — MRs !1–!5 | ✅ Concluída — aceite Marcos Turnes 06/06/2026 |
| Sprint 2 | 09/06/2026–20/06/2026 | 28   | Auditoria/Log (RF-07), Integração ms.temis.vinculos (RF-08)      | ✅ Concluída — aceite Marcos Turnes 20/06/2026 |
| Sprint 3 | 23/06/2026–04/07/2026 | 20   | Relatórios e CSV export (RF-09), homologação QA                  | 📋 Planejada   |
| **Total** | **19/05–04/07/2026** | **82** | —                                                             | —              |

### 3.1 Git Flow

| Branch           | Finalidade                                      |
|------------------|-------------------------------------------------|
| `main`           | Código em produção — merge apenas via release   |
| `develop`        | Integração contínua de features                 |
| `feature/ag-{id}`| Desenvolvimento de cada requisito AG            |
| `release/*`      | Preparação de entrega ao final de cada sprint   |

## 4. Papéis e Responsabilidades

| Papel                        | Responsável      | Organização | Responsabilidades                                                                           |
|------------------------------|------------------|-------------|----------------------------------------------------------------------------------------------|
| Product Owner                | Marcos Turnes  | AASP        | Priorização do backlog, aceite de entrega, aprovação de change requests                      |
| QA / Homologação             | Leonardo Francisco Pereira     | AASP        | Execução de testes de homologação, emissão de parecer de aceite por sprint                   |
| Gerente de Projeto / Tech Lead | Abraão (GP) · Cezar Hiraki (TL)  | Timeware    | Coordenação do projeto, arquitetura técnica, code review, relatório de status, gestão de riscos |
| Desenvolvedor                | Renan Kiyoshi    | Timeware    | Implementação das features, testes unitários, atualização da documentação técnica            |
| Desenvolvedor                | Henry Komatsu    | Timeware    | Implementação das features e testes unitários                                                |
| Desenvolvedor                | Mateus Veloso           | Timeware    | Implementação das features e testes unitários                                                |

## 5. Plano de Comunicação

| Evento                  | Frequência                              | Canal          | Participantes              | Responsável    |
|-------------------------|-----------------------------------------|----------------|----------------------------|----------------|
| Daily Stand-up          | Diária — 09h30                          | Microsoft Teams | Equipe Timeware            | Abraão  |
| Sprint Review           | Sexta-feira da semana de fechamento     | Microsoft Teams | Equipe completa + PO + QA  | Abraão  |
| Sprint Retrospectiva    | Sexta-feira da semana de fechamento     | Microsoft Teams | Equipe Timeware            | Abraão  |
| Relatório de Status     | Semanal — toda segunda-feira            | E-mail         | Marcos Turnes, Leonardo Francisco Pereira | Abraão |
| Comunicações urgentes   | Sob demanda                             | Microsoft Teams | Partes envolvidas          | Qualquer membro |
| Relatório GQA           | Por auditoria (intermediária + encerramento) | E-mail | Silvio Baroni (SEPG) | Abraão |

## 6. Plano de Gestão de Riscos

### 6.1 Escala de Probabilidade e Impacto

- **Probabilidade:** P1 = Baixa | P2 = Média | P3 = Alta
- **Impacto:** I1 = Baixo | I2 = Médio | I3 = Alto
- **Exposição:** P × I (escala 1–9)

### 6.2 Registro de Riscos

| ID   | Risco                                             | Prob | Impacto | Exposição | Resposta / Mitigação                                                        | Status atual (01/07/2026) | Última atualização |
|------|---------------------------------------------------|------|---------|-----------|-----------------------------------------------------------------------------|---|---|
| R-01 | Indisponibilidade do ambiente de homologação AASP | P2   | I2      | 4         | Agendamento prévio de janelas de homologação com a equipe AASP              | ✅ Encerrado — ambiente disponível e utilizado nas Sprints 1 e 2 | 20/06/2026 |
| R-02 | Schema do banco `auxo3` com inconsistências       | P2   | I3      | 6         | Análise do schema antes de cada sprint; scripts de migração com rollback     | ✅ Encerrado — schema analisado; migrations aplicadas sem regressões | 06/06/2026 |
| R-03 | Mudança de escopo solicitada pelo PO              | P1   | I2      | 2         | Escopo congelado após assinatura do TAP; novas demandas tratadas via CR formal | ✅ Encerrado — zero CRs registrados; escopo estável | 01/07/2026 |
| R-04 | Falha na integração com `ms.temis.vinculos`       | P2   | I3      | 6         | Contrato de API definido em ITP antes da Sprint 2; ambiente de mock para testes | 🟡 Monitoramento ativo — integração implementada e aceita na Sprint 2; validação final em Sprint 3 | 20/06/2026 |
| R-05 | Indisponibilidade do desenvolvedor                | P1   | I3      | 3         | Pair programming documentado; documentação técnica sempre atualizada         | ✅ Encerrado — sem indisponibilidade registrada em nenhuma sprint | 01/07/2026 |

## 7. Plano de Verificação e Validação (V&V)

| Atividade                   | Quando             | Responsável       | Critério de Conclusão                                        |
|-----------------------------|--------------------|-------------------|--------------------------------------------------------------|
| Testes unitários            | A cada sprint      | Renan Kiyoshi, Henry Komatsu e Mateus Veloso (cada dev responsável pelo próprio código) | Cobertura ≥ 60% nos módulos entregues na sprint |
| Code review                 | A cada MR          | Cezar Hiraki     | Aprovação formal no GitLab antes do merge              |
| Testes de integração        | Sprint 2           | Cezar Hiraki     | Endpoints integrados validados em ambiente de desenvolvimento |
| Homologação QA              | Sprint 3            | Leonardo Francisco Pereira     | Parecer de aceite emitido pela QA da AASP                    |
| Aceite formal               | Fim de cada sprint  | Marcos Turnes  | Confirmação escrita do PO (e-mail ou Teams)                  |

## 8. Métricas de Sucesso

| ID  | Métrica                                                             |
|-----|---------------------------------------------------------------------|
| M1  | 100% dos requisitos funcionais (RF-01 a RF-09) entregues e aceitos  |
| M2  | Cobertura de testes unitários ≥ 60% em todos os módulos             |
| M3  | Tempo de resposta ≤ 500 ms para 95% das requisições (RNF-01)        |
| M4  | Zero defeitos críticos abertos na entrega final                     |
| M5  | Aceite formal de sprint em 100% das sprints pelo PO                 |
| M6  | Integração com `ms.temis.vinculos` validada em homologação          |
| M7  | Número de Change Requests aprovados: 0 (escopo estável conforme TAP) — qualquer CR aprovado deve ter impacto em prazo e custo documentado |
| M8  | Entrega dentro do prazo definido no TAP (até 04/07/2026)            |

## 9. Processo de Change Request

Toda solicitação de alteração de escopo, prazo ou custo deve:

1. Ser formalizada por escrito (e-mail ou formulário CR) pelo solicitante
2. Ser avaliada pelo Gerente de Projeto (Abraão) quanto a impacto em prazo, esforço e riscos
3. Ser aprovada formalmente por **Marcos Turnes (AASP)** e **Abraão (Timeware)**
4. Ser registrada no documento de Change Requests (CR-AASP01) com número sequencial
5. Ter o plano atualizado antes da implementação

Mudanças não aprovadas por ambas as partes não serão implementadas.

## 10. Plano de Encerramento

O encerramento formal do projeto ocorrerá ao final da Sprint 3, aproximadamente em 04/07/2026.

### 10.1 Critérios de Aceite Final

| Critério | Responsável pela verificação | Meta |
|---|---|---|
| 100% dos RFs entregues (RF-01 a RF-09) e aceitos formalmente | Marcos Turnes (PO AASP) | Obrigatório |
| Cobertura de testes unitários ≥ 60% (todas as sprints) | Cezar Hiraki | Obrigatório |
| Zero defeitos P1 (críticos) abertos | Cezar Hiraki | Obrigatório |
| Regressão completa (AG-20 a AG-25) aprovada por Leonardo Francisco Pereira | Leonardo Francisco Pereira (QA AASP) | Obrigatório |
| Todos os artefatos MPS-SW em versão final entregues | Silvio Baroni (SEPG) | Obrigatório |
| BL-04 (baseline de encerramento) estabelecida e auditada | Cezar Hiraki + Silvio Baroni | Obrigatório |

### 10.2 Artefatos de Encerramento

| Artefato | Responsável | Prazo |
|---|---|---|
| Termo de Encerramento e Aceite (TAE-AASP01-001) | Abraão Oliveira | ~04/07/2026 |
| Lições Aprendidas (LI-AASP01-001) | Abraão Oliveira | ~04/07/2026 |
| RAC v1.4 (status final Sprint 3) | Abraão Oliveira | ~04/07/2026 |
| MED v1.4 (métricas finais) | Abraão Oliveira | ~04/07/2026 |
| REL-VV v1.5 (resultados finais + regressão) | Cezar Hiraki | ~04/07/2026 |
| Auditoria de encerramento GQA | Silvio Baroni (SEPG) | ~04/07/2026 |

### 10.3 Responsabilidades de Encerramento

- **Abraão Oliveira (GP):** emissão do TAE, convocação da Sprint Review final, encerramento dos riscos ativos, produção das Lições Aprendidas
- **Cezar Hiraki (TL/GCO):** estabelecimento da BL-04 (tag sprint-3-aceite), auditoria de baseline com supervisão do SEPG, atualização do REL-VV com resultados da Sprint 3
- **Silvio Baroni (SEPG):** auditoria GQA de encerramento, verificação das NCs da auditoria intermediária resolvidas, validação da BL-04

---

## 11. Referências

| Documento      | Descrição                     |
|----------------|-------------------------------|
| TAP-AASP01-001 | Termo de Abertura do Projeto  |
| REQ-AASP01-001 | Documento de Requisitos       |
| ATA-AASP01-001 | Ata de Reunião de Kickoff     |

---

## Histórico de Revisões

| Versão | Data       | Autor          | Descrição             |
|--------|------------|----------------|-----------------------|
| 1.0 | 19/05/2026 | Abraão Oliveira | Criação do documento |
| 1.1 | 06/06/2026 | Abraão Oliveira | Atualização pós-aceite Sprint 1: status Sprint 1 → ✅ Concluída; Sprint 2 → 🔄 Em andamento |
| 1.2 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: status Sprint 2 → ✅ Concluída; riscos com colunas "Status atual" e "Última atualização"; testes unitários com responsabilidade compartilhada (3 devs); M7 reformulado como métrica quantitativa; seção 10 (Plano de Encerramento) adicionada; SEPG incluído no plano de comunicação. |
