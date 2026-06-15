# Índice de Registros do Projeto — AASP_Automacao-Governanca

| Campo | Valor |
|---|---|
| **Documento** | INDICE-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Natureza** | Documento de controle / índice — apoio interno. Organiza os registros do projeto; **não é, ele próprio, evidência auditável pela ASR**. |
| **Fonte** | INTAKE-AASPGOV01_Formulario-de-Levantamento (14/06/2026) · RDP-AASPGOV01-001 v3.0 |

> **Como usar:** este índice mapeia todos os registros MPS produzidos para o projeto AASPGOV01, a área de processo de cada um e a seção do formulário de levantamento (intake) que o alimenta. O projeto está **encerrado** (02/06/2026); todos os registros de execução e de encerramento foram produzidos.

---

## 1. Contexto do projeto

- **Início:** 14/04/2026 · **Encerramento:** 02/06/2026 · **Duração:** ~7 semanas (49 dias).
- **Status:** Encerrado — desenvolvimento concluído, homologado e aceite formal emitido.
- **Tecnologia:** .NET 8 LTS (C#) — Azure Scheduled Job · Azure DevOps (GitFlow) · Azure Key Vault.
- **Esforço:** 216 h estimadas → 236 h realizadas (+9,3%) · 59 SP em 4 sprints (S0–S3).
- **Auditoria GQA:** 02/06/2026, Jonathan Alves (independente) — 16/16 itens conformes, 0 NCs.

**Equipe:** Abraão Oliveira (GP) · Cezar Hiraki Velazquez (Tech Lead/Arquiteto) · Raony Chagas (Dev Sênior) · Allan Alves (Dev) · Caroline Sousa (QA) · Lucas Batista (DevOps). Patrocinador: Marcos Correa Fernandez Turnes (AASP).

---

## 2. Registros produzidos

**Legenda:** ✅ gerado (15/06/2026).

| # | Código | Documento | Processo | Bloco-fonte | Status |
|---|---|---|---|---|---|
| 1 | TAP-AASPGOV01-001 | Termo de Abertura | GPR | 1, 2, 3, 8 | ✅ |
| 2 | ADAP-AASPGOV01-001 | Registro de Adaptação | GPR | 4 | ✅ |
| 3 | PLA-AASPGOV01-001 | Plano de Projeto | GPR | 5, 8, 2 | ✅ |
| 4 | RAC-AASPGOV01-001 | Relatório de Acompanhamento (RAG-4D) | GPR | 10.2 | ✅ |
| 5 | TAE-AASPGOV01-001 | Termo de Aceite e Encerramento | GPR | 13 | ✅ |
| 6 | LI-AASPGOV01-001 | Lições Aprendidas (7 lições) | GPR | 13.1 | ✅ |
| 7 | REQ-AASPGOV01-001 | Documento de Requisitos (11 RF + 6 RNF) | REQ | 3 | ✅ |
| 8 | RASTR-AASPGOV01-001 | Matriz de Rastreabilidade (RF×CT×CA) | REQ | 3, 9 | ✅ |
| 9 | PCP-AASPGOV01-001 | Documento de Design | PCP | 6, 7 | ✅ |
| 10 | ITP-AASPGOV01-001 | Estratégia de Integração | ITP | 6, 9 | ✅ |
| 11 | VV-AASPGOV01-001 | Plano de V&V (12 CT) | VV | 9 | ✅ |
| 12 | REL-VV-AASPGOV01-001 | Relatório de Execução de Testes (12 CT, 5 bugs) | VV | 9 | ✅ |
| 13 | REV-AASPGOV01-001 | Registro de Revisão por Pares (23 PRs) | VV | 11 | ✅ |
| 14 | GCO-AASPGOV01-001 | Registro de Configuração (6 IC, 3 baselines) | GCO | 6 | ✅ |
| 15 | GDE-AASPGOV01-001 | Registro de Análise de Decisão (D01–D07) | GDE | 7 | ✅ |
| 16 | MED-AASPGOV01-001 | Registro de Medição (M1–M7) | MED | 12 | ✅ |
| 17 | CAP-AASPGOV01-001 | Registro de Capacitação da Equipe | CAP | 2, 4.2 | ✅ |
| 18 | GQA-AASPGOV01-001 | Registro de GQA (16 itens) | GPC | 11 | ✅ |
| 19 | ATA-AASPGOV01-001 | Ata de Kickoff (14/04) | ORG | 10.1 | ✅ |
| 20 | ATA-AASPGOV01-002 | Ata de Alinhamento de APIs (23/04) | ORG | 10.1 | ✅ |
| 21 | ATA-AASPGOV01-003 | Ata de Validação da Homologação (29/05) | ORG | 9.2, 10.1 | ✅ |
| 22 | ATA-AASPGOV01-004 | Ata de Aceite e Encerramento (02/06) | ORG | 13 | ✅ |
| 23 | GEST-AASPGOV01 | Planilha de Gestão do Projeto (`.xlsx`, 9 abas) | GPR | 5, 6, 9, 12 | ✅ |

> Os itens 1–23 correspondem aos **23 produtos de trabalho** verificados na auditoria de GQA (GQA-AASPGOV01-001). Este índice (item de controle) não é contado como produto auditável.

---

## 3. Cobertura de processos MPS-SW Nível C

| Processo | Registro(s) |
|---|---|
| GPR — Gerência de Projetos | TAP, ADAP, PLA, RAC, LI, TAE, GEST |
| REQ — Engenharia de Requisitos | REQ, RASTR |
| PCP — Projeto e Construção do Produto | PCP (seção "OSW/arquitetura" do intake reclassificada como PCP) |
| ITP — Integração do Produto | ITP |
| VV — Verificação e Validação | VV, REL-VV, REV |
| GPC — Gerência de Processos (GQA) | GQA |
| MED — Medição | MED |
| GDE — Gerência de Decisões | GDE |
| GCO — Gerência de Configuração | GCO |
| CAP — Capacitação | CAP |
| ORG — Governança Organizacional | ATA-001 a ATA-004 |
| AQU — Aquisição | Não aplicável (sem subcontratação; padrão `MAPA-ORG-001`). Dependências de terceiros tratadas em ITP/PCP e nota no ADAP §4 |

---

## 4. Observações de classificação

- **Change Request (CR):** não se aplica — escopo fixo desde o TAP; apenas correções de defeitos na homologação (BUG-01 a BUG-05), sem mudança de escopo.
- **PRs e commits:** os Pull Requests de tudo que foi entregue estão registrados em REV-AASPGOV01-001 (23 PRs, por branch/item/autor/revisor/sprint/baseline). Os identificadores internos e os commits residem no Azure DevOps (consultáveis pela ASR).
- **Formato:** registros em Markdown (`.md`) com conversão para Word (`.docx`) no padrão Timeware; a planilha de gestão em `.xlsx`.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Criação do índice-mestre e geração dos 23 registros do projeto AASPGOV01 a partir do INTAKE-AASPGOV01 (14/06/2026), em `.md` + `.docx` e a planilha `.xlsx`. |
