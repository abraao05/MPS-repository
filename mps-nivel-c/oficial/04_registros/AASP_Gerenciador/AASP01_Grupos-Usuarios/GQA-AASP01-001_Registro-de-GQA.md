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
| **Versão** | 1.0 |
| **Processo MPS-SW** | GPC — Garantia da Qualidade do Processo (evidência de projeto) |

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

| Produto de trabalho | Documento | Situação |
|---|---|---|
| Termo de Abertura | TAP-AASP01-001 | ✅ |
| Plano de Projeto | PLA-AASP01-001 | ✅ |
| Registro de Adaptação | ADAP-AASP01-001 | ✅ |
| Documento de Requisitos | REQ-AASP01-001 | ✅ |
| Matriz de Rastreabilidade | RASTR-AASP01-001 | ✅ |
| Documento de Design | PCP-AASP01-001 | ✅ |
| Registro de Análise de Decisão | GDE-AASP01-001 | ✅ |
| Estratégia de Integração | ITP-AASP01-001 | ✅ |
| Plano de Verificação e Validação | VV-AASP01-001 | ✅ |
| Cenários de Teste e Homologação | CTQ-AASP01-001 | ✅ |
| Relatório de Execução de Testes | REL-VV-AASP01-001 | ✅ |
| Registro de Revisão Técnica | REV-AASP01-001 | ✅ |
| Registro de Gerência de Configuração | GCO-AASP01-001 | ✅ |
| Registro de Medição | MED-AASP01-001 | ✅ |
| Relatório de Acompanhamento | RAC-AASP01-001 | ✅ |
| Registro de Change Requests | CR-AASP01-001 | ✅ |
| Registro de Capacitação da Equipe | CAP-AASP01-001 | ✅ |
| Planilha de Gestão do Projeto | GEST-AASP01 | ✅ |
| Atas de Reunião | ATA-AASP01-001, ATA-AASP01-002 | ✅ |
| Índice de Registros | 00_INDICE-AASP01 | ✅ |
| Termo de Encerramento e Aceite | TAE-AASP01-001 | ⏳ Sprint 3 |
| Lições Aprendidas | LI-AASP01-001 | ⏳ Sprint 3 |

---

## 4. Achados

Nenhuma não-conformidade bloqueante identificada. Registram-se as oportunidades de melhoria abaixo:

| ID | Tipo | Descrição | Recomendação |
|---|---|---|---|
| OM-01 | Oportunidade de melhoria | A adaptação A-02 (ADAP-AASP01-001) previu formalização do Sprint Planning a partir da Sprint 3. | Garantir o registro do planejamento das sprints restantes (S3 e S4) na Planilha de Gestão. |
| OM-02 | Oportunidade de melhoria | Avaliação de eficácia da capacitação e Lições Aprendidas ainda não aplicáveis (projeto em curso). | Concluir, no encerramento (Sprint 3), a avaliação de eficácia (CAP) e o registro de Lições Aprendidas (LI). |

---

## 5. Resultado

**Conforme.** A aderência ao processo-padrão e às adaptações registradas está confirmada para todos os marcos verificados. Os pontos de controle obrigatórios foram mantidos, os produtos de trabalho previstos para o estágio atual estão presentes e consistentes, e a gerência de configuração opera com baselines controladas. As observações registradas são oportunidades de melhoria, sem impacto na conformidade.

**Próxima verificação:** auditoria de encerramento, na Sprint 3, cobrindo a homologação final, o Termo de Encerramento e Aceite e as Lições Aprendidas.

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Silvio Baroni (Time de Melhoria Contínua) | Verificação intermediária de GQA do projeto AASP01 — pós-Sprint 1 e meio da Sprint 2 |
