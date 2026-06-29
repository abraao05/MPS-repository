# Índice de Registros do Projeto — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | INDICE-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador (Feature AG) |
| **Código do projeto** | AASP01 |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Produto** | ms.auxo.usuarios |
| **Versão** | 1.1 |
| **Data** | 24/06/2026 |
| **Natureza** | Documento de controle / índice — apoio interno. Organiza a produção das evidências do projeto; não é, ele próprio, evidência auditável pela ASR. |

> **Como usar:** este índice mapeia os registros MPS-SW do projeto AASP01, o processo de origem e o status de cada um. Conforme cada artefato evolui, atualizar a coluna **Status** e registrar no histórico ao final.

---

## 1. Contexto e momento do projeto

- **Início:** 19/05/2026 (Kickoff) · **Encerramento previsto:** 11/07/2026.
- **Status atual (15/06/2026):** em execução — Sprint 1 concluída e aceita (06/06/2026); Sprint 2 em andamento; Sprints 3 e 4 planejadas.
- **Nível de adaptação:** 2 — Padrão (ver ADAP-AASP01-001).
- **Fases do processo-padrão (PRO-GPC-001):** Abertura, Discovery/Requisitos, Concepção e Planejamento concluídas; Desenvolvimento em curso; Homologação e Encerramento previstos para a Sprint 3.

---

## 2. Registros do projeto

**Legenda de status:** ✅ gerado e no repositório · ⏳ previsto (encerramento).

| # | Código | Documento | Processo | Status |
|---|---|---|---|---|
| 1 | TAP-AASP01-001 | Termo de Abertura | GPR | ✅ |
| 2 | PLA-AASP01-001 | Plano de Projeto | GPR | ✅ |
| 3 | ADAP-AASP01-001 | Registro de Adaptação | GPR | ✅ |
| 4 | RAC-AASP01-001 | Relatório de Acompanhamento | GPR | ✅ |
| 5 | CR-AASP01-001 | Registro de Change Requests | GPR / GCO | ✅ |
| 6 | REQ-AASP01-001 | Documento de Requisitos | REQ | ✅ |
| 7 | RASTR-AASP01-001 | Matriz de Rastreabilidade | REQ | ✅ |
| 8 | PCP-AASP01-001 | Documento de Design | PCP | ✅ |
| 9 | GDE-AASP01-001 | Registro de Análise de Decisão | GDE | ✅ |
| 10 | ITP-AASP01-001 | Estratégia de Integração | ITP | ✅ |
| 11 | VV-AASP01-001 | Plano de Verificação e Validação | VV | ✅ |
| 12 | CTQ-AASP01-001 | Cenários de Teste e Homologação | VV | ✅ |
| 13 | REL-VV-AASP01-001 | Relatório de Execução de Testes | VV | ✅ |
| 14 | REV-AASP01-001 | Registro de Revisão Técnica | VV | ✅ |
| 15 | GCO-AASP01-001 | Registro de Gerência de Configuração | GCO | ✅ |
| 16 | MED-AASP01-001 | Registro de Medição | MED | ✅ |
| 17 | CAP-AASP01-001 | Registro de Capacitação da Equipe | CAP | ✅ |
| 18 | GQA-AASP01-001 | Registro de Verificação de GQA | GPC | ✅ |
| 19 | GEST-AASP01 | Planilha de Gestão do Projeto (xlsx) | GPR | ✅ |
| 20 | ATA-AASP01-001 | Ata de Kickoff (19/05/2026) | ORG | ✅ |
| 21 | ATA-AASP01-002 | Ata de Aceite — Sprint 1 (06/06/2026) | ORG | ✅ |
| 22 | TAE-AASP01-001 | Termo de Encerramento e Aceite | GPR | ⏳ Sprint 3 |
| 23 | LI-AASP01-001 | Lições Aprendidas | GPR | ⏳ Sprint 3 |

> **Aquisição (AQU):** não aplicável — não houve subcontratação de desenvolvimento (equipe própria Timeware). Insumos de serviço (APIs e ambientes do cliente) são tratados em ITP-AASP01-001 e nos riscos do PLA-AASP01-001.

---

## 3. Observações de classificação

- **Formato:** registros produzidos em Markdown (`.md`) e convertidos para Word (`.docx`); planilha de gestão em `.xlsx`.
- **Nomes reais nos registros:** os registros de identificação e de capacidade (TAP, PLA, ATAs, GQA, CAP) nominam a equipe real, conforme a camada de capacidade do modelo.

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Abraão Oliveira | Criação do índice de registros do projeto AASP01 (Sprint 2 em andamento) |
| 1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
