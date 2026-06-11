# Registro de Garantia da Qualidade — GASMIG Governança de APIs

| Campo | Valor |
|---|---|
| **Documento** | GQA-GASMIG02-001 — Registro de Garantia da Qualidade |
| **Versão** | 1.4 |
| **Data** | 11/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Fundação Tecnológica GASMIG — Governança de APIs |
| **Auditor** | COO (Operações) |

---

## 1. Objetivo

Registrar as auditorias de qualidade realizadas ao longo do projeto, verificando a aderência ao processo definido e a conformidade dos artefatos produzidos com os padrões estabelecidos.

---

## 2. Auditoria de aderência ao processo

### 2.1 OS-001 — Configuração Base do Gateway

**Data da auditoria:** 07/05/2026
**Auditado por:** COO (Operações)
**Período auditado:** 10/04/2026 – 07/05/2026

| Item verificado | Conforme? | Observação |
|---|---|---|
| Termo de abertura elaborado antes do início das atividades | ✅ Sim | TAP-GASMIG02-001 v1.0, assinado em 10/04/2026 |
| Requisitos documentados e rastreáveis antes da configuração | ✅ Sim | REQ-GASMIG02-001 v1.0 |
| Design técnico documentado e aprovado antes do deploy | ✅ Sim | PCP-GASMIG02-001 v1.0, elaborado em 15/04/2026 |
| Adaptações ao processo formalizadas | ✅ Sim | ADAP-GASMIG02-001: testes substituídos por checklists de verificação |
| Plano de verificação executado com resultados registrados | ✅ Sim | VV-GASMIG02-001 com checklist e evidências |
| Rastreabilidade mantida entre requisitos, design e verificação | ✅ Sim | RASTR-GASMIG02-001 v1.0 |
| Papéis e responsabilidades seguidos conforme planejado | ✅ Sim | Conforme PLA-GASMIG02-001, seção 6 |
| Encerramento formal realizado com aceite do cliente | ✅ Sim | ATA-GASMIG02-002 + TAE-GASMIG02-001 |
| **GCO-1** — ICs identificados e controlados com convenção de versão adotada | ✅ Sim | Azure DevOps com Git Flow e naming convention de IaC/policies documentados em GCO-GASMIG02-001 |
| **GCO-2** — Baseline estabelecida ao encerramento da OS-001 | ✅ Sim | Tag `v1.0.0-os001` e snapshot dos Named Values + policies exportados (GCO-GASMIG02-001 §3) |
| **GCO-3** — Auditoria de configuração realizada: ICs íntegros e consistentes | ✅ Sim | GCO-GASMIG02-001 §4 — auditoria ao encerramento da OS-001; ICs verificados, nenhuma inconsistência |

**Resultado OS-001:** Sem não conformidades.

---

### 2.2 OS-002 — Integração e Homologação (auditoria parcial — sprint em andamento)

**Data da auditoria:** 04/06/2026
**Auditado por:** COO (Operações)
**Período auditado:** 26/05/2026 – 04/06/2026

| Item verificado | Conforme? | Observação |
|---|---|---|
| Termo de abertura elaborado antes do início | ✅ Sim | TAP-GASMIG02-002 v1.0 |
| Requisitos documentados e rastreáveis | ✅ Sim | REQ-GASMIG02-002 v1.0 |
| Design técnico documentado | ✅ Sim | PCP-GASMIG02-002 v1.0 |
| Adaptações ao processo formalizadas | ✅ Sim | ADAP-GASMIG02-002 v1.0 |
| Cronograma sendo seguido conforme planejado | ✅ Sim | Sprint encerrada 06/06/2026 conforme planejado |
| Verificação técnica e encerramento formal | ✅ Sim | REV executada 09/06/2026; aceite em 09/06/2026; TAE-GASMIG02-002 emitido |
| **GCO-1** — ICs identificados e controlados com convenção de versão adotada | ✅ Sim | Reutiliza repositório e convenção da OS-001; novos recursos OS-002 controlados sob tag `v1.0.0-os002` |
| **GCO-2** — Baseline de sprint estabelecida | ✅ Sim | Baseline intermediária documentada antes do deploy do lote OS-002 (GCO-GASMIG02-001 §3) |
| **GCO-3** — Auditoria de configuração realizada | ✅ Sim | Checklist técnico REV-GASMIG02-001 inclui verificação de ICs (Named Values, policies) — 0 inconsistências |

**Resultado OS-002 (parcial):** Sem não conformidades.

---

### 2.3 OS-002 — Auditoria de encerramento

**Data da auditoria:** 10/06/2026
**Auditado por:** COO (Operações)
**Período auditado:** 04/06/2026 – 09/06/2026

| Item verificado | Conforme? | Observação |
|---|---|---|
| Verificação técnica executada com resultados registrados | ✅ Sim | REV-GASMIG02-001 executada por Cézar Hiraki em 09/06/2026; 0 não conformidades |
| Aceite formal do cliente obtido | ✅ Sim | E-mail Sérgio Villaça 09/06/2026 11:30 — "a entrega da fase 2 está aprovada" |
| Encerramento formal documentado | ✅ Sim | TAE-GASMIG02-002 emitido em 09/06/2026 |
| Lições aprendidas registradas | ✅ Sim | LI-GASMIG02-001 atualizado com seção OS-002 |
| Medição finalizada | ✅ Sim | MED-GASMIG02-001 atualizado — todos os indicadores M1–M9 OS-002 confirmados |
| **GCO-3** — Auditoria de configuração de encerramento realizada | ✅ Sim | GCO-GASMIG02-001 §4 — todos os ICs auditados ao encerramento da OS-002; baseline final `v1.0.0-os002` intacta e rastreável |

**Resultado encerramento OS-002:** Sem não conformidades. Projeto encerrado com 100% dos artefatos de processo em conformidade.

---

## 3. Revisão dos artefatos produzidos

### 3.1 OS-001

| Artefato | Padrão esperado | Conforme? | Observação |
|---|---|---|---|
| TAP-GASMIG02-001 | Cabeçalho completo, escopo, stakeholders, cronograma, assinaturas | ✅ Sim | |
| PLA-GASMIG02-001 | Planejamento detalhado, riscos, recursos, marcos | ✅ Sim | |
| REQ-GASMIG02-001 | Requisitos numerados, rastreáveis, com critério de aceite | ✅ Sim | |
| PCP-GASMIG02-001 | Arquitetura documentada, decisões técnicas registradas | ✅ Sim | |
| VV-GASMIG02-001 | Checklist de verificação com resultados e evidências | ✅ Sim | |
| RASTR-GASMIG02-001 | Cobertura total dos RFs em artefatos e atividades | ✅ Sim | |
| ADAP-GASMIG02-001 | Adaptações justificadas e aprovadas | ✅ Sim | |
| ATA-GASMIG02-002 | Assinatura do cliente, itens aceitos, ressalvas | ✅ Sim | |
| TAE-GASMIG02-001 | Encerramento formal, lições aprendidas, pendências | ✅ Sim | |

### 3.2 OS-002

| Artefato | Padrão esperado | Conforme? | Observação |
|---|---|---|---|
| TAP-GASMIG02-002 | Cabeçalho completo, escopo, stakeholders, cronograma, assinaturas | ✅ Sim | |
| PLA-GASMIG02-002 | Planejamento detalhado, riscos, recursos, marcos | ✅ Sim | v1.1 com equipe e datas atualizadas |
| REQ-GASMIG02-002 | Requisitos numerados, rastreáveis, com critério de aceite | ✅ Sim | |
| PCP-GASMIG02-002 | Arquitetura documentada, decisões técnicas registradas | ✅ Sim | |
| VV-GASMIG02-002 | Checklist de verificação com resultados e evidências | ✅ Sim | |
| RASTR-GASMIG02-002 | Cobertura total dos RFs em artefatos e atividades | ✅ Sim | |
| ADAP-GASMIG02-002 | Adaptações justificadas e aprovadas | ✅ Sim | |
| REV-GASMIG02-001 | Registro de verificação técnica pós-deploy | ✅ Sim | Executada por Cézar Hiraki em 09/06/2026; 0 não conformidades |
| ATA-GASMIG02-003 | Ata de apresentação e aceite | ✅ Sim | Reunião 08/06/2026; aceite registrado em 09/06/2026 |
| TAE-GASMIG02-002 | Encerramento formal | ✅ Sim | Emitido em 09/06/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 07/05/2026 | COO (Operações) | Auditoria de encerramento da OS-001 |
| 1.1 | 04/06/2026 | COO (Operações) | Inclusão de auditoria parcial da OS-002 em andamento |
| 1.2 | 05/06/2026 | Time de Melhoria Contínua | Correção do papel do auditor para COO (Operações), garantindo independência da GQA em relação à equipe de projeto |
| 1.3 | 10/06/2026 | COO (Operações) | Fechamento da auditoria parcial OS-002; adição da auditoria de encerramento (§2.3); artefatos ⏳ atualizados para ✅ |
| 1.4 | 11/06/2026 | Time de Melhoria Contínua | Adição de itens GCO-1 a GCO-3 nas três auditorias (OS-001, OS-002 parcial e OS-002 encerramento) — GCO 5 |
