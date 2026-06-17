# Ata de Reunião — Análise Crítica de Processos · Time de Melhoria Contínua

| Campo | Valor |
|---|---|
| **Documento** | ATA-GPC-001 — Ata de Reunião de Análise Crítica de Processos |
| **Versão** | 1.0 |
| **Data da reunião** | 11/06/2026 |
| **Data do documento** | 13/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Processo MPS-SW** | GPC (evidência — GPC 6, GPC 7) / OSW (evidência — OSW 3) |
| **Responsável** | Silvio Baroni |
| **Classificação** | Registro organizacional de governança |

---

## 1. Informações da reunião

| Item | Detalhe |
|---|---|
| **Tipo** | Reunião de análise crítica de processos — Time de Melhoria Contínua (SEPG) |
| **Data** | 11/06/2026 |
| **Horário** | 14h00 – 16h00 |
| **Modalidade** | Remota (Microsoft Teams) |
| **Convocante** | COO (Operações) |

### Participantes

| Papel | Presença |
|---|---|
| COO (Operações) — responsável pelo portfólio e TMC | ✅ Presente |
| Time de Melhoria Contínua — membros | ✅ Presentes |
| Gerente de Projeto (representante dos projetos) | ✅ Presente |

---

## 2. Pauta

1. Situação do ciclo de implantação MPS-SW Nível C — revisão final pré-avaliação
2. Análise crítica das oportunidades de melhoria identificadas nos projetos (REG-GPC-001)
3. Aprovação do Plano de Implementação de Melhorias (REG-GPC-002)
4. Situação do portfólio de projetos — encerramento OS-002 GASMIG (09/06/2026)
5. Comunicação dos resultados de melhoria aos grupos relevantes
6. Encaminhamentos

---

## 3. Registros da reunião

### 3.1. Ciclo MPS-SW Nível C — revisão pré-avaliação

O Time de Melhoria Contínua apresentou o status da implantação: todos os 12 processos do Nível C têm ativos de processo publicados no repositório oficial. Os 4 projetos do ciclo (PROFARMA, GASMIG OS-001, GASMIG OS-002, Fruki Pacotes 1 e Final) têm registros completos em 04_registros/. A avaliação oficial pela ASR Consultoria está agendada para o segundo semestre de 2026.

**Decisão:** portfólio de ativos aprovado para submissão à avaliação. Itens residuais identificados pelo consultor serão tratados até 13/06/2026.

### 3.2. Análise crítica das OMs (REG-GPC-001)

O TMC apresentou as 11 oportunidades de melhoria registradas a partir dos projetos PROFARMA e GASMIG:

- **1 OM implementada** (OM-06 — checklist de pré-engajamento Azure): resultado verificado na OS-002 (zero bloqueio de acesso, crédito ao procedimento implementado com antecedência de 1 semana).
- **1 OM em implementação** (OM-05 — outbox pattern): padrão em documentação no Confluence; previsão de publicação em Jul/2026.
- **9 OMs planejadas** para o próximo ciclo (ago–set/2026), com responsável e prazo definidos em REG-GPC-002.

**Decisão:** prioridades validadas. OM-01 (checklist discovery para legados) e OM-06 são as de maior impacto imediato; OM-04 (guia de carga legada) foi priorizada para set/2026, após encerramento do projeto AASP.

### 3.3. Plano de Implementação de Melhorias (REG-GPC-002)

O TMC apresentou o REG-GPC-002, detalhando as tarefas de implementação de cada OM e as 8 ações de melhoria documental executadas no ciclo.

**Decisão:** REG-GPC-002 aprovado. O documento é adotado como registro formal complementar ao REG-GPC-001.

### 3.4. Portfólio de projetos

O COO informou que a OS-002 GASMIG (Fundação Tecnológica — Governança de APIs) foi encerrada formalmente em 09/06/2026, com aceite do cliente e emissão do TAE-GASMIG02-002. O projeto AASP WorkerAndamentos está em execução, com encerramento previsto em 30/06/2026. A situação consolidada está em REG-OSW-001.

### 3.5. Comunicação dos resultados de melhoria

O TMC deliberou sobre os canais e grupos para comunicação dos resultados do ciclo de melhoria:

| Grupo | Canal | Conteúdo comunicado | Responsável | Prazo |
|---|---|---|---|---|
| Gerentes de projeto | Confluence (página do TMC) + reunião | REG-GPC-001, REG-GPC-002 — OMs e tarefas de implementação | Time de Melhoria Contínua | 13/06/2026 |
| Tech Leads | Confluence + notificação Teams | OM-05 (outbox pattern), OM-06 (checklist Azure) | Time de Melhoria Contínua | 13/06/2026 |
| COO / Alta Gestão | Ata desta reunião + REG-OSW-001 | Situação do portfólio, status das melhorias | COO (ciência nesta reunião) | Imediato |
| Colaboradores (geral) | Confluence — página de processos | Ativos de processo publicados / atualizados | Time de Melhoria Contínua | 13/06/2026 |

**Decisão:** todos os artefatos produzidos no ciclo serão publicados no repositório oficial (GitHub) e referenciados na página do Time de Melhoria Contínua no Confluence.

---

## 4. Encaminhamentos

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| E-01 | Publicar REG-GPC-001, REG-GPC-002 e REG-OSW-001 no repositório oficial | Time de Melhoria Contínua | 13/06/2026 |
| E-02 | Notificar GPs e Tech Leads sobre as OMs e o Plano de Implementação via Confluence/Teams | Time de Melhoria Contínua | 13/06/2026 |
| E-03 | Iniciar implementação de IMPL-OM05-A (outbox pattern) no Confluence | Time de Melhoria Contínua | 31/07/2026 |
| E-04 | Planejar reunião de revisão de OMs para set/2026, após encerramento do projeto AASP | COO | Set/2026 |
| E-05 | Acompanhar encerramento do projeto AASP WorkerAndamentos | Gerente de Projeto | 30/06/2026 |

---

## 5. Rastreabilidade com o modelo MR-MPS-SW:2024

| Resultado | Como esta ata atende |
|---|---|
| GPC 6 — Processo de melhoria gerenciado pelo SEPG | §3.2 (análise crítica das OMs), §3.3 (aprovação do plano de implementação), §4 (encaminhamentos) |
| GPC 7 — Participação dos grupos relevantes no processo de melhoria | §1 (participantes), §3.5 (comunicação estruturada por grupo e canal) |
| OSW 3 — Processos e resultados comunicados para os grupos relevantes | §3.5 (tabela de comunicação: GPs, Tech Leads, Alta Gestão, Colaboradores) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Silvio Baroni |
| 1.0 | 13/06/2026 | Time de Melhoria Contínua | Versão inicial — ata da reunião de análise crítica de processos realizada em 11/06/2026 |
