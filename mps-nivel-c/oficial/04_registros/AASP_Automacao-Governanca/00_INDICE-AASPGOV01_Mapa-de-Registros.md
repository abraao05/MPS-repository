# Índice de Registros do Projeto — AASP_Automacao-Governanca

| Campo | Valor |
|---|---|
| **Documento** | INDICE-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Código do projeto** | AASPGOV01 |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.2 |
| **Data** | 15/06/2026 |
| **Natureza** | Documento de controle / índice — apoio interno. Organiza a produção das evidências do projeto; não é, ele próprio, evidência auditável pela ASR. |
| **Fonte consolidada** | `AASP_AutomacaoGovernanca_Registro_de_Projeto` v2.0 (08/06/2026) |

> **Como usar:** este índice mapeia todos os registros MPS a produzir para o projeto AASPGOV01, o status de cada um e a seção do documento-fonte que o alimenta. Conforme cada artefato for gerado, atualizar a coluna **Status** e registrar no histórico ao final.

---

## 1. Contexto e momento do projeto

- **Início:** 14/04/2026 · **Encerramento:** 02/06/2026.
- **Status atual (02/06/2026):** projeto encerrado — desenvolvimento concluído, homologado e aceite emitido.
- **Fases do processo-padrão (PRO-GPC-001):** todas concluídas.
- **Modelo agile retroativo:** execução real em 4 fases (waterfall) modelada retroativamente em 4 sprints de 2 semanas (~59 SP) para evidência e carga no Jira — ver ADAP-AASPGOV01-001.

---

## 2. Plano de produção (ondas)

A produção segue três ondas, da maior para a menor prontidão de insumo.

**Legenda de status:** ✅ gerado e no repositório · ⏳ pendente.

### Onda 1 — Núcleo de execução

| # | Código do artefato | Documento | Processo | Seção-fonte | Status |
|---|---|---|---|---|---|
| 1 | TAP-AASPGOV01-001 | Termo de Abertura | GPR | v2.0 §2 | ✅ |
| 2 | PLA-AASPGOV01-001 | Plano de Projeto | GPR | v2.0 §6 | ✅ |
| 3 | REQ-AASPGOV01-001 | Documento de Requisitos | REQ | v2.0 §4 | ✅ |
| 4 | PCP-AASPGOV01-001 | Documento de Design | PCP | v2.0 §7 | ✅ |

### Onda 2 — Restante da execução

| # | Código do artefato | Documento | Processo | Seção-fonte | Status |
|---|---|---|---|---|---|
| 5 | ADAP-AASPGOV01-001 | Registro de Adaptação do Processo | GPR | — | ✅ |
| 6 | ITP-AASPGOV01-001 | Estratégia de Integração | ITP | v2.0 §9 | ✅ |
| 7 | VV-AASPGOV01-001 | Plano de Verificação e Validação | VV | v2.0 §10 | ✅ |
| 8 | REL-VV-AASPGOV01-001 | Relatório de Execução de Testes | VV | v2.0 §10 | ✅ |
| 9 | REV-AASPGOV01-001 | Registro de Revisão por Pares | VV | v2.0 §8 | ✅ |
| 10 | GCO-AASPGOV01-001 | Registro de Gerência de Configuração | GCO | v2.0 §8 | ✅ |
| 11 | GDE-AASPGOV01-001 | Registro de Análise de Decisão | GDE | v2.0 §15 | ✅ |
| 12 | MED-AASPGOV01-001 | Registro de Medição | MED | v2.0 §11 | ✅ |
| 13 | RASTR-AASPGOV01-001 | Matriz de Rastreabilidade | REQ | v2.0 §5 | ✅ |
| 14 | RAC-AASPGOV01-001 | Relatório de Acompanhamento | GPR | v2.0 §6 | ✅ |
| 15 | ATA-AASPGOV01-001 | Ata de Kickoff (14/04/2026) | ORG | — | ✅ |
| 16 | ATA-AASPGOV01-002 | Ata de Alinhamento Mapeamento de APIs (23/04/2026) | ORG | — | ✅ |
| 17 | ATA-AASPGOV01-003 | Ata de Validação de Homologação (29/05/2026) | ORG | — | ✅ |
| 18 | GQA-AASPGOV01-001 | Registro de GQA | GPC | v2.0 §12 | ✅ |
| 19 | GEST-AASPGOV01 | Planilha de Gestão do Projeto (xlsx) | GPR | v2.0 §6, §11 | ✅ |
| 20 | CAP-AASPGOV01-001 | Registro de Capacitação da Equipe | CAP | v2.0 §14 | ✅ |

### Onda 3 — Encerramento

| # | Código do artefato | Documento | Processo | Seção-fonte | Status |
|---|---|---|---|---|---|
| 21 | ATA-AASPGOV01-004 | Ata de Aceite Final (02/06/2026) | ORG | — | ✅ |
| 22 | TAE-AASPGOV01-001 | Termo de Encerramento e Aceite | GPR | v2.0 §16 | ✅ |
| 23 | LI-AASPGOV01-001 | Lições Aprendidas | GPR | v2.0 §16.5 | ✅ |

> **Nota sobre Change Request:** não houve CR durante o projeto — escopo estável do Kickoff ao encerramento. Confirmado no INTAKE-AASPGOV01 (Bloco 10).

### Fora de escopo

| Item | Decisão |
|---|---|
| AQU — Aquisição | **Não gerar registro de projeto.** Não houve subcontratação de desenvolvimento; APIs Sensr/Jira e Azure Scheduler são insumos de serviço, tratados em ITP-AASPGOV01-001 e nos riscos do PLA, não em um registro AQU. |

---

## 3. Dados base (decisões da Fase 1)

### Equipe Timeware

| Papel | Nome |
|---|---|
| Gerente de Projeto (GP) | Abraão Oliveira |
| Tech Lead / Arquiteto (acumula 2 papéis) | Cezar Hiraki |
| Desenvolvedor Sênior | Raony Chagas |
| Desenvolvedor (Suporte) | Allan Alves |
| Analista de Testes (QA) | Caroline Sousa |
| Infraestrutura / DevOps | Lucas Batista |
| Auditor GQA (independente) | Jonathan Alves |

### Cliente

- **Sponsor / Patrocinador:** Marcos Correa Fernandez Turnes
- **Organização:** AASP — Associação dos Advogados de São Paulo

### Período e esforço

- **Período:** 14/04/2026 – 02/06/2026 (~7 semanas)
- **Esforço estimado:** 216 h
- **Esforço realizado:** 236 h
- **Desvio:** +9,3%

### Modelo agile retroativo

- **Conversão:** 1 SP = 4 h
- **Backlog total:** ~59 SP em 4 sprints
- **Velocity média:** ~15 SP/sprint
- **Distribuição:** Sprint 0 (15 SP) · Sprint 1 (16 SP) · Sprint 2 (16 SP) · Sprint 3 (12 SP)

---

## 4. Observações de classificação

- **Formato:** registros produzidos em Markdown (`.md`); conversão para Word apenas quando solicitado.
- **Modelagem retroativa em sprints:** os requisitos foram organizados em sprints e story points retroativamente, com base nas fases reais executadas — conforme ADAP-AASPGOV01-001 e GEST-AASPGOV01.
- **Nomes reais nos registros de projeto:** seguindo o padrão do AASP_CNJ, registros de identificação (TAP, PLA, ATAs, GQA, TAE) usam os nomes reais da equipe.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Criação do índice-mestre de registros do projeto AASPGOV01 a partir do documento-fonte consolidado v2.0 (08/06/2026). Onda 1 parcial gerada (INDICE + TAP + PLA + ADAP); demais artefatos delegados ou em produção. |
| 1.1 | 13/06/2026 | Time de Melhoria Contínua | Todos os 23 artefatos confirmados no repositório. CR removido do índice — INTAKE-AASPGOV01 (Bloco 10) confirma ausência de Change Request. Status geral atualizado para ✅. |
| 1.2 | 15/06/2026 | Time de Melhoria Contínua | Passo de consistência interna: padronização do nome do projeto (AASP_Automacao-Governanca) em todos os registros; correções pontuais em TAE (contagem de cenários), ATA-002/GDE (data de D04), RASTR (critério RNF-05) e CAP (fases de Lucas Batista). Sem alteração de fatos do projeto. |
