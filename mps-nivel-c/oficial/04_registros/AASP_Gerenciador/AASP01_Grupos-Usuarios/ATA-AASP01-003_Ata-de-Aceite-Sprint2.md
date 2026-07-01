# Ata de Aceite — Sprint 2 — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASP01-003 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Reunião** | Sprint Review + Aceite Formal — Sprint 2 |
| **Data** | 20/06/2026 |
| **Horário** | 14h00 – 15h20 |
| **Canal** | Microsoft Teams |
| **Facilitador** | Abraão Oliveira (Timeware) |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Processo MPS-SW** | VV / GPR (evidência de validação formal e aceite de fase) |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão Oliveira | Timeware | Gerente de Projeto · Facilitador |
| Cezar Hiraki Velázquez | Timeware | Arquiteto / Tech Lead |
| Renan Kiyoshi | Timeware | Desenvolvedor (AG-23) |
| Mateus Veloso | Timeware | Desenvolvedor (AG-24) |
| Marcos Turnes | AASP | Product Owner / Representante do Cliente / Aprovador |
| Leonardo Francisco Pereira | AASP | QA / Homologador |

---

## 2. Objetivo da Reunião

Apresentar os entregáveis da Sprint 2 (AG-23 e AG-24) ao cliente AASP, demonstrar o funcionamento da trilha de auditoria e da integração com ms.temis.vinculos via Swagger UI, apresentar os resultados dos testes de homologação executados por Leonardo Francisco Pereira e obter o aceite formal de Marcos Turnes (AASP, PO), encerrando oficialmente a Sprint 2.

---

## 3. Itens Apresentados

| História | Requisitos Cobertos | Funcionalidade Demonstrada | Cenários de Aceite | Resultado |
|---|---|---|---|---|
| **AG-23** — Auditoria de Operações de Grupos | RF-07 | Interceptor de auditoria registrando operações Create/Update/Delete na tabela `auditoria_grupos`; consulta de trilha por `usuario_acao`; imutabilidade dos registros (append-only); índice `IX_auditoria_grupos_usuario_acao` para performance | AUD-01 (auditoria de criação), AUD-02 (auditoria de exclusão) — 2/2 OK | Aprovado por Marcos Turnes |
| **AG-24** — Integração ms.temis.vinculos | RF-08 | Cliente HTTP sincronizando vínculos com ms.temis.vinculos (endpoint `api/gerenciar/grupos/vinculados`); comportamento fault-tolerant (timeout 5s + retry 2x); fallback sem interrupção do negócio | INT-01 (happy path — sincronização bem-sucedida), INT-02 (fallback — ms.temis.vinculos indisponível, operação não interrompida) — 2/2 OK | Aprovado por Marcos Turnes |

---

## 4. Demonstração Técnica

Renan Kiyoshi demonstrou a **trilha de auditoria (AG-23)** via Swagger UI (`http://homologacao.aasp/swagger`), executando operações de inclusão, alteração e exclusão de grupos e verificando os registros gerados na tabela `auditoria_grupos`. Demonstrou também a consulta de auditoria filtrando por `usuario_acao` com uso do índice de performance.

Mateus Veloso demonstrou a **integração com ms.temis.vinculos (AG-24)**, incluindo o cenário de disponibilidade normal (INT-01) e o cenário de fallback com ms.temis.vinculos indisponível (INT-02), confirmando que a operação de negócio não é interrompida em caso de falha da integração. O timeout de 5s e o retry de 2 tentativas foram validados em ambiente de homologação.

Cezar Hiraki apresentou o **resumo do code review** das MRs !6 e !7: 3 achados identificados (RV-006-01 P2, RV-006-02 P2, RV-007-01 P3), todos resolvidos antes do merge. Apresentou também a cobertura de testes: 14 novos métodos adicionados na Sprint 2, totalizando 36 métodos com cobertura cumulativa de 70,1% (meta: ≥ 60% — atingida).

Leonardo Francisco Pereira confirmou que os **4 cenários de aceite** (AUD-01, AUD-02, INT-01, INT-02) foram executados por ele no ambiente de homologação AASP em 20/06/2026 e aprovados sem ressalvas, conforme evidências registradas no CTQ-AASP01-001.

---

## 5. Resultados dos Testes de Homologação — Sprint 2

| Tipo de Teste | Sprint 2 | Cumulativo (S1+S2) | Resultado |
|---|---|---|---|
| Testes unitários | 14 novos métodos | 36 métodos | 100% passando; cobertura 70,1% (meta: ≥ 60% — atingida) |
| Testes de integração | INT-01 + INT-02 | — | 2/2 aprovados (ms.temis.vinculos) |
| Cenários de aceite (CTQ) | 4 (AUD-01, AUD-02, INT-01, INT-02) | 14 (S1: 10 + S2: 4) | 4/4 (100%) aprovados por Leonardo Francisco Pereira em 20/06/2026 |
| Achados code review (REV) | 3 (P2: 2 — !6; P3: 1 — !7) | 8 (S1: 5 + S2: 3) | Todos resolvidos antes do merge — nenhum defeito aberto |

---

## 6. Pontos Levantados pelo Cliente

- **Marcos Turnes (AASP — PO):** Confirmou que as funcionalidades AG-23 e AG-24 atendem aos requisitos RF-07 e RF-08 especificados no REQ-AASP01-001. Validou o comportamento fault-tolerant da integração (INT-02): o sistema de negócio não pode ficar indisponível por falha de um serviço externo — o comportamento demonstrado está correto. Nenhuma ressalva técnica ou de negócio identificada. Confirmou o aceite formal da Sprint 2 via e-mail encaminhado à equipe Timeware em 20/06/2026 (arquivado).

- **Leonardo Francisco Pereira (AASP — QA):** Validou os 4 cenários de aceite no ambiente de homologação AASP. Confirmou que o ambiente de homologação com temis3 foi disponibilizado conforme acordado na Sprint Review da Sprint 1. Solicitou que o ambiente seja mantido disponível para os testes de regressão da Sprint 3 (AG-25).

- **Abraão Oliveira (Timeware — GP):** Informou que a Sprint 3 inicia em 23/06/2026 com a história AG-25 (Relatório Consolidado de Grupos). Confirmou que os documentos MPS-SW serão atualizados com os resultados da Sprint 2 (RAC, MED, REL-VV, GCO, RASTR, CTQ) na semana seguinte ao aceite.

---

## 7. Aceite Formal

**Marcos Turnes (AASP) concedeu aceite formal da Sprint 2 SEM RESSALVAS em 20/06/2026.**

A Sprint 2 é considerada oficialmente encerrada e entregue. Todas as histórias (AG-23, AG-24) estão em status **Done** e os entregáveis foram aceitos pelo representante do cliente. A baseline BL-03 foi estabelecida com a tag `sprint-2-aceite` no repositório GitLab após o aceite formal.

**Declaração de aceite (registrada em reunião via Microsoft Teams em 20/06/2026 e confirmada por e-mail arquivado de 20/06/2026):**

> "Confirmo o aceite formal dos entregáveis da Sprint 2 (AG-23 e AG-24) do projeto Grupos de Usuários — AASP Gerenciador. A trilha de auditoria e a integração com ms.temis.vinculos foram demonstradas e validadas conforme os critérios de aceite definidos. O comportamento fault-tolerant da integração atende aos requisitos de disponibilidade do sistema. Nenhuma ressalva ou pendência identificada."
>
> — **Marcos Turnes**, AASP, 20/06/2026

---

## 8. Próximos Passos

| Ação | Responsável | Prazo | Status |
|---|---|---|---|
| Iniciar Sprint 3 — AG-25 (Relatório Consolidado de Grupos) | Renan Kiyoshi, Henry Komatsu e Mateus Veloso | 23/06/2026 | ✅ Cumprida — Sprint 3 iniciada em 23/06/2026 |
| Atualizar documentos MPS-SW com resultados Sprint 2 (RAC, MED, REL-VV, GCO, RASTR, CTQ) | Abraão Oliveira | 27/06/2026 | ✅ Cumprida — documentos atualizados |
| Registrar baseline BL-03 no GCO-AASP01-001 com tag sprint-2-aceite | Cezar Hiraki (GCO) + Silvio Baroni (SEPG — verificação independente) | 23/06/2026 | ✅ Cumprida — BL-03 registrada; tag sprint-2-aceite criada no GitLab |
| Manter ambiente de homologação AASP disponível para regressão Sprint 3 | Leonardo Francisco Pereira (AASP) | Duração da Sprint 3 | ✅ Em andamento |
| Sprint Review Sprint 3 agendada — apresentação de AG-25 | Abraão Oliveira + Marcos Turnes | ~04/07/2026 — 14h00 Teams | ⏳ Agendada |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 20/06/2026 | Abraão Oliveira | Versão inicial — ata de aceite formal da Sprint 2 (AG-23, AG-24); aceite concedido por Marcos Turnes sem ressalvas; e-mail de confirmação arquivado em 20/06/2026 |
