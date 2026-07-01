# Registro de Verificação de GQA — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | GQA-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Marco / tipo de verificação** | Verificação intermediária — pós-Sprint 1 e meio da Sprint 2 |
| **Data** | 15/06/2026 |
| **Auditor (GQA)** | Silvio Baroni — Time de Melhoria Contínua / SEPG (auditor independente) |
| **Gerente de Projeto** | Abraão Oliveira |
| **Versão** | 1.2 |
| **Processo MPS-SW** | GQA — Garantia da Qualidade do Processo e do Produto (evidência de projeto) |

---

## 1. Escopo da verificação

Verificação independente da aderência do projeto AASP01 — Grupos de Usuários ao Processo-Padrão Organizacional (PRO-GPC-001) e às adaptações registradas (ADAP-AASP01-001), conforme a Estratégia de Garantia da Qualidade (EST-GPC-001). Esta é a auditoria intermediária prevista para projetos de Nível 2 de adaptação (GUIA-GPC-001, §5.2); a auditoria de encerramento ocorrerá na Sprint 3.

A verificação cobre os marcos já concluídos: Abertura, Discovery/Requisitos, Concepção/Design, Planejamento e a Sprint 1 (desenvolvimento, homologação e aceite). A independência é assegurada: o auditor não integra a equipe de execução (Gerente de Projeto, Tech Lead e desenvolvedores) nem a função de QA do produto.

---

## 2. Verificação de aderência ao processo

Legenda: ✅ Conforme · ⚠ Observação · N/A não aplicável no momento.

| # | Ponto de controle (GUIA-GPC-001 §3) | Evidência | Situação |
|---|---|---|---|
| 1 | Abertura formal do projeto | TAP-AASP01-001 aprovado (19/05/2026) e Ata de Kickoff (ATA-AASP01-001) | ✅ |
| 2 | Requisitos especificados e validados com o cliente | REQ-AASP01-001 (RF-01 a RF-09, RNF-01 a RNF-05) com critérios de aceite; validação por sprint registrada | ✅ |
| 3 | Design técnico avaliado antes da construção | PCP-AASP01-001 (v1.0, 26/05/2026) com arquitetura, modelo de dados e decisões (GDE-AASP01-001) revisados antes da Sprint 1 | ✅ |
| 4 | Definição de Pronto a cada entrega (critérios de aceite, code review, verificação, homologação) | REV-AASP01-001 (code review por PR), VV-AASP01-001, CTQ-AASP01-001 e gate de CI obrigatório | ✅ |
| 5 | Aprovação do cliente antes da promoção para produção | Aceite formal da Sprint 1 por Marcos Turnes (ATA-AASP01-002, 06/06/2026); homologação e produção final pendentes (projeto em curso) | ✅ |
| 6 | Encerramento formal (Termo de Aceite e lições aprendidas) | Previsto para a Sprint 3 (TAE e LI) | N/A |

**Gerência de Configuração (GCO 1–3):**

| Resultado | Evidência | Situação |
|---|---|---|
| GCO 1 — itens de configuração identificados | GCO-AASP01-001 §3 (IC-01 a IC-06) | ✅ |
| GCO 2 — controle de versões e baselines | Baselines BL-01 (19/05) e BL-02 (06/06) com tags imutáveis; Git Flow | ✅ |
| GCO 3 — controle de mudanças | CR-AASP01-001 (registro de change requests; sem CR no período — escopo estável) | ✅ |

---

## 3. Verificação de produtos de trabalho

Legenda: ✅ Conforme (critérios verificados) · ⚠ NC identificada (ver §4) · ⏳ Pendente (Sprint futura) · N/A Não aplicável.

| Produto de trabalho | Documento | Critérios verificados | Situação |
|---|---|---|---|
| Termo de Abertura | TAP-AASP01-001 | Escopo definido; partes interessadas com contatos; macroplanejamento com datas; referências documentais; aprovação registrada | ⚠ NC-GQA-01: campo contato do GP vazio ("a confirmar") |
| Plano de Projeto | PLA-AASP01-001 | Cronograma com milestones; papéis e responsabilidades; plano de V&V; registro de riscos; plano de comunicação | ⚠ NC-GQA-02: ausência de seção de encerramento (GPR RAP 7) |
| Registro de Adaptação | ADAP-AASP01-001 | Adaptações com justificativa e mitigação; A-08 com aprovação registrada | ✅ |
| Documento de Requisitos | REQ-AASP01-001 | RFs com critérios de aceite testáveis; RNFs mensuráveis; rastreabilidade ao backlog | ✅ |
| Matriz de Rastreabilidade | RASTR-AASP01-001 | Cobertura RF→endpoint→teste; bidirecionalidade verificada para Sprint 1 | ✅ |
| Documento de Design | PCP-AASP01-001 | Modelo de dados com tabelas; decisões arquiteturais referenciadas no GDE; padrões de implementação definidos | ✅ |
| Registro de Análise de Decisão | GDE-AASP01-001 | Alternativas avaliadas com critérios ponderados; decisão registrada com responsável | ✅ |
| Estratégia de Integração | ITP-AASP01-001 | Interfaces identificadas; contrato INT-01 com ms.temis.vinculos em definição (Sprint 2) | ✅ |
| Plano de Verificação e Validação | VV-AASP01-001 | Níveis de teste definidos; critérios de qualidade; atividades por sprint | ✅ |
| Cenários de Teste e Homologação | CTQ-AASP01-001 | 10 cenários Sprint 1 com pré-condição, passos e resultado esperado; todos executados 100% na Sprint 1 | ✅ |
| Relatório de Execução de Testes | REL-VV-AASP01-001 | Sprint 1 com testes unitários (22/22), code review (5 achados resolvidos), UAT (10/10 aprovados); aceite formal registrado | ✅ |
| Registro de Revisão Técnica | REV-AASP01-001 | 4 sessões de code review; achados com severidade, resolução e MR correspondente | ✅ |
| Registro de Gerência de Configuração | GCO-AASP01-001 | ICs identificados; BL-01 e BL-02 com tags imutáveis; Git Flow; auditorias registradas | ⚠ NC-GQA-03: IC-05 declara 19 artefatos mas índice lista 21 |
| Registro de Medição | MED-AASP01-001 | Métricas M1–M8 definidas com meta; Sprint 1 coletada | ✅ |
| Relatório de Acompanhamento | RAC-AASP01-001 | Sprint 1 concluída; Sprint 2 com 7 dias decorridos e AG-23/AG-24 não iniciados — risco registrado em §3.2 | ⚠ NC-GQA-04 (OM): ações corretivas para o atraso de AG-23/AG-24 não documentadas |
| Registro de Change Requests | CR-AASP01-001 | Processo de CR definido; zero CRs registrados — escopo estável | ⚠ NC-GQA-05: processo MPS-SW classificado como GRE (incorreto — deve ser GMUDS) |
| Registro de Capacitação da Equipe | CAP-AASP01-001 | Competências identificadas; matriz de situação por papel | ✅ |
| Planilha de Gestão do Projeto | GEST-AASP01 | Acompanhamento de SP por sprint; backlog com prioridades | ✅ |
| Atas de Reunião | ATA-AASP01-001, ATA-AASP01-002 | Participantes, pauta, decisões e próximos passos documentados; aceite Sprint 1 formal | ⚠ NC-GQA-06: processo MPS-SW nas atas classificado como AQU/GRE (deve ser GPR/ORG e VV/GPR) |
| Índice de Registros | 00_INDICE-AASP01 | 21 documentos listados com status; rastreabilidade ao processo MPS | ✅ |
| Termo de Encerramento e Aceite | TAE-AASP01-001 | — | ⏳ Sprint 3 |
| Lições Aprendidas | LI-AASP01-001 | — | ⏳ Sprint 3 |

---

## 4. Achados

| ID | Tipo | Severidade | Documento afetado | Descrição | Prazo para correção | Status |
|---|---|---|---|---|---|---|
| NC-GQA-01 | Não-Conformidade | Moderada | TAP-AASP01-001 | Campo de contato do GP Abraão está como "a confirmar" em documento já aprovado. Deve ser preenchido com e-mail real. | 24/06/2026 | ✅ Corrigido em v1.2 (01/07/2026) |
| NC-GQA-02 | Não-Conformidade | Grave | PLA-AASP01-001 | Plano de projeto sem seção de encerramento — critérios de aceite final, responsável pelo TAE e prazo não planejados. GPR RAP 7 não atendido. | 24/06/2026 | ✅ Corrigido em v1.2 (01/07/2026) |
| NC-GQA-03 | Não-Conformidade | Moderada | GCO-AASP01-001 | IC-05 declara 19 artefatos MPS-SW mas o índice lista 21 (CAP e GQA não contabilizados na baseline BL-02). | 24/06/2026 | ✅ Corrigido em GCO v1.3 (01/07/2026) |
| NC-GQA-04 | Observação | Leve | RAC-AASP01-001 | AG-23 e AG-24 não iniciados no 7º dia útil da Sprint 2 — desvio de cronograma sem ação corretiva documentada. | 20/06/2026 | ✅ Resolvido — AG-23 e AG-24 entregues na Sprint 2 |
| NC-GQA-05 | Não-Conformidade | Grave | CR-AASP01-001 | Processo MPS-SW classificado como GRE (Gerência de Riscos) — incorreto. O registro de CRs é evidência de GMUDS (Gerência de Mudanças). | 24/06/2026 | ✅ Corrigido em CR v1.1 (01/07/2026) |
| NC-GQA-06 | Não-Conformidade | Grave | ATA-AASP01-001, ATA-AASP01-002 | Processo MPS-SW classificado como AQU/GRE — incorreto. ATA-001 deve ser GPR/ORG; ATA-002 deve ser VV/GPR. Classificação incorreta impede localização das evidências de GPR RAP 1 e VV RAP 3. | 24/06/2026 | ✅ Corrigido nas versões 1.2 (01/07/2026) |
| OM-01 | Oportunidade de melhoria | — | ADAP-AASP01-001 | Adaptação A-02 previu formalização do Sprint Planning a partir da Sprint 3. Registrar encerramento formal da adaptação após início da Sprint 3 (23/06/2026). | 30/06/2026 | ✅ Corrigido em ADAP v1.2: A-02 declarada encerrada em 23/06/2026 |
| OM-02 | Oportunidade de melhoria | — | CAP-AASP01-001 | Avaliação de eficácia da capacitação e Lições Aprendidas a concluir no encerramento da Sprint 3. | ~04/07/2026 | ⏳ Pendente — Sprint 3 em andamento |

---

## 5. Resultado

**Conforme com Não-Conformidades Identificadas.** O projeto AASP01 apresenta aderência geral ao Processo-Padrão Organizacional e às adaptações registradas. Os pontos de controle obrigatórios foram mantidos e os produtos de trabalho previstos estão presentes. Foram identificadas 5 não-conformidades de classificação e conteúdo, com nenhuma de severidade bloqueante para a Sprint 2, e 2 oportunidades de melhoria — todos registrados com prazo de correção e tratamento documentado neste relatório.

As NCs identificadas foram corrigidas nas respectivas versões dos documentos afetados (v1.2 de 01/07/2026). A verificação de conformidade pós-correção foi realizada pelo auditor GQA em 01/07/2026.

**Próxima verificação:** auditoria de encerramento, na Sprint 3, cobrindo: (a) homologação final AG-25 + regressão AG-20 a AG-25; (b) Termo de Encerramento e Aceite; (c) Lições Aprendidas; (d) verificação das NCs identificadas nesta auditoria; (e) avaliação de eficácia da capacitação (CAP).

**Critérios de auditoria de encerramento:** para cada produto de trabalho verificar: (i) conteúdo consistente com a realidade do projeto; (ii) métricas Sprint 3 coletadas; (iii) aceite formal de Marcos Turnes com evidência rastreável; (iv) baseline BL-04 estabelecida; (v) todas as NCs desta auditoria intermediária resolvidas.

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Silvio Baroni (SEPG) | Verificação intermediária de GQA do projeto AASP01 — pós-Sprint 1 e meio da Sprint 2 |
| 1.1 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do projeto; processo MPS-SW corrigido para GQA. |
| 1.2 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: seção 3 reescrita com critérios de verificação explícitos; seção 4 atualizada com 6 NCs e 2 OMs identificados; seção 5 resultado revisado para "Conforme com NCs Identificadas"; processo MPS-SW corrigido (GPC → GQA). |
