# Registro de Change Requests — Cadastro de Clientes · Rede D1000

| Campo | Valor |
|---|---|
| **Documento** | CR-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Contexto

O projeto foi contratado como squad mensalizado (3 Dev Pleno), modelo que permite a absorção incremental de mudanças de escopo sem recontratação formal, desde que aprovadas pelo patrocinador e registradas. Ao longo dos 19 sprints (abril/2025–janeiro/2026), foram aprovados e absorvidos **12 change requests**, todos gerenciados dentro do mesmo squad sem acréscimo de custo de mão de obra — os CRs impactaram principalmente o cronograma e contribuíram para a extensão do prazo original de setembro/2025 para janeiro/2026.

---

## 2. Registro consolidado de Change Requests

| CR | Fase / Sprints | Descrição da mudança | Escopo afetado | Impacto no prazo | Aprovado por | Status |
|---|---|---|---|---|---|---|
| CR-01 | Fase 2 · Sprints 6–8 | Integração BlueSoft (score de crédito e dados de perfil) — inclusão da integração com o sistema de crédito BlueSoft, não prevista no escopo original | RF-15 — novo endpoint e integração | +2 sprints estimados | Armando Junior / Abraão Oliveira | ✅ Absorvido |
| CR-02 | Fase 2 · Sprints 6–8 | Integração CloseUp (dados de consumo) — inclusão da integração com o sistema de análise de consumo CloseUp | RF-16 — novo endpoint e integração | Incluído no mesmo bloco do CR-01 | Armando Junior / Abraão Oliveira | ✅ Absorvido |
| CR-03 | Fase 2 · Sprints 8–10 | Ajustes de implementação na integração BlueSoft — refinamentos de contrato de API e tratamento de casos extremos identificados na implementação do CR-01 | RF-15 — ajustes pós-integração | Dentro do bloco de sprints realocados | Armando Junior | ✅ Absorvido |
| CR-04 | Fase 2 · Sprints 8–10 | Ajustes de implementação na integração CloseUp — refinamentos de contrato de API e tratamento de casos extremos identificados na implementação do CR-02 | RF-16 — ajustes pós-integração | Dentro do bloco de sprints realocados | Armando Junior | ✅ Absorvido |
| CR-05 | Fase 2 · Sprint 8 | Worker de anonimização LGPD — desenvolvimento do worker de expurgo de dados pessoais sensíveis conforme exigência legal, não previsto no escopo original | Novo componente: worker batch de anonimização | +1 sprint estimado | Pedro Costa / Abraão Oliveira | ✅ Absorvido |
| CR-06 | Fase 4 · Sprint 11 | Backup PITR explicitado nos requisitos de infraestrutura — inclusão formal do requisito de Point-in-Time Recovery para o banco PostgreSQL Azure no escopo do projeto | RNF — requisito de infraestrutura | Sem impacto de prazo | Humberto Erler | ✅ Absorvido |
| CR-07 | Fase 2 · Sprint 13–14 | Aceleração do prazo da integração Propz CRM — antecipação do deadline da integração Propz de "sem prazo definido" para 04/12/2025, com compromisso formal de entrega | RF-14 (Propz CRM) — deadline fixado em 04/12/2025 | Criou prazo rígido; absorvido dentro do cronograma já revisado | Abraão Oliveira / Helena Moreira | ✅ Absorvido |
| CR-08 | Fase 4 · Sprint 8 | Adição de métricas Prometheus ao serviço — inclusão de endpoint `/metrics` com métricas de performance e negócio para observabilidade interna | Novo componente: endpoint de métricas Prometheus | Sem impacto de prazo | Armando Junior | ✅ Absorvido |
| CR-09 | Fase 4 · Sprint 12–13 | Ajuste no contrato de API VTEX — campo de endereço não previsto na especificação original identificado nos testes de integração VTEX; inclusão do campo no modelo de dados e no contrato de API | RF-12 (VTEX) — ajuste de contrato e modelo | Sem impacto de prazo | Armando Junior | ✅ Absorvido |
| CR-10 | Fase 4 · Sprint 12–13 | Campo `score_credito` na integração BlueSoft — campo adicional solicitado pelo negócio para enriquecer o perfil de cliente com dados de crédito BlueSoft, não previsto na especificação original do CR-01 | RF-15 (BlueSoft) — campo adicional no modelo | Sem impacto de prazo | Pedro Costa / Armando Junior | ✅ Absorvido |
| CR-11 | Fase 5 · Sprint 16–17 | Ajuste no fluxo de opt-out Propz CRM — redefinição do comportamento de opt-out de marketing após validação conjunta com o time Propz; mudança de lógica de propagação do sinal de opt-out | RF-14 (Propz CRM) — ajuste de lógica de negócio | Sem impacto de prazo | Pedro Costa / Helena Moreira | ✅ Absorvido |
| CR-12 | Fase 5 · Sprint 17 | Suporte a campo adicional de conveniado no canal Call Center — campo de identificação de programa de conveniado solicitado pela equipe de Call Center durante os testes de homologação | RF-13 (Call Center) — campo adicional | Sem impacto de prazo | Humberto Erler | ✅ Absorvido |

---

## 3. Impacto consolidado

| Dimensão | Impacto |
|---|---|
| **Prazo** | Extensão de ~4 meses (setembro/2025 → janeiro/2026); principal fator: CRs de integrações BlueSoft e CloseUp (CR-01 a CR-04) somados ao risco de ambiente e GMUD |
| **Custo** | Sem acréscimo de custo de mão de obra (modelo mensalizado); custo adicional indireto: viagens presenciais para resolução de blockers (média R$ 5.000 por deslocamento) |
| **Escopo** | +2 integrações completas (BlueSoft e CloseUp), +1 worker LGPD, +1 componente de observabilidade (Prometheus), múltiplos ajustes de contrato de API e modelo de dados |
| **Qualidade** | Todos os CRs foram implementados com testes unitários e cenários de homologação correspondentes; 0 defeitos S1 ou S2 abertos no aceite |

---

## 4. CRs que impactaram o cronograma

| CR | Impacto no prazo | Sprint(s) afetadas |
|---|---|---|
| CR-01 / CR-02 | Principal fator de extensão — adição de 2 integrações completas | Sprints 6–10 realocados |
| CR-05 | Acréscimo de 1 sprint de desenvolvimento | Sprint 8 replanejado |
| CR-07 | Criou prazo rígido (04/12/2025) que condicionou os Sprints 13–16 | Sprints 13–16 |

Os demais CRs (CR-03, CR-04, CR-06, CR-08, CR-09, CR-10, CR-11, CR-12) foram absorvidos sem impacto adicional no cronograma por serem refinamentos implementados dentro dos sprints afetados ou por não consumirem esforço significativo além do já alocado.

---

## 5. Rastreabilidade

| Referência | Relação |
|---|---|
| RAC-PROFARMA01-001 | Desvios e CRs por fase do projeto |
| TAE-PROFARMA01-001 §4 | Indicadores finais — 12 CRs formais absorvidos |
| REQ-PROFARMA01-001 | Requisitos originais; RF-12 a RF-17 correspondem a entregas expandidas por CRs |
| GQA-PROFARMA01-001 | Conformidade do processo de controle de mudanças |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — reconstituído com base no RAC-PROFARMA01-001 e TAE-PROFARMA01-001 |
