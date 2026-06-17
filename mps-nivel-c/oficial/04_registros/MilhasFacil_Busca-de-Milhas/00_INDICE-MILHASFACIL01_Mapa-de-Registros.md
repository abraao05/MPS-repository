# Índice de Registros do Projeto — MilhasFacil

| Campo | Valor |
|---|---|
| **Documento** | INDICE-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Natureza** | Documento de controle / índice — apoio interno. Organiza a produção das evidências do projeto; **não é, ele próprio, evidência auditável pela ASR**. |
| **Fonte consolidada** | Planilha de Gestão `GEST-MILHASFACIL01-001` (fonte da verdade de gestão) + código real dos três repositórios + APIs Azure DevOps/Jira (coleta 15/06/2026) |

> **Como usar:** este índice mapeia todos os registros MPS a produzir para o projeto MILHASFACIL01, o status de cada um e o processo MPS-SW que evidenciam. Conforme cada artefato for gerado ou atualizado, ajustar a coluna **Status** e registrar no histórico ao final.

---

## 1. Contexto e momento do projeto

- **Início:** 09/02/2026 · **Encerramento previsto:** 26/07/2026.
- **Status atual (15/06/2026):** **Sprint 9 de 12 em andamento** (01–14/06/2026); projeto **ABERTO**.
- **Consequência para a documentação:** todo o conjunto de **execução** (Ondas 1 e 2) já pode ser produzido com base no realizado em S1–S9; os artefatos de **encerramento** (Onda 3: Termo de Encerramento, Lições Aprendidas, Ata de Aceite Final) **aguardam o aceite formal** previsto para o fim do projeto (~26/07/2026) e ainda não se aplicam.
- **Equipe (time atual):** Abraão (GP — gestão, fora do DevOps), Cézar Velazquez (Tech Lead / Arquiteto / DevOps — revisor de PR), Jonathan Alves (QA — teste manual), Carol/Caroline (GQA independente — fora do DevOps), Felipe Santos · Lucas Batista · Henry Oliveira (Devs). **DevOps (Azure) = 5:** Cézar + 3 devs + Jonathan. Mapa de identidade no tooling (contas legadas): aprovação de PR sob `Mateus Veloso` = Cézar; commits de infra sob `Raony Chagas`/`Mateus Sousa` = Cézar; `Felipe Siqueira`/`Henry Komatsu`/`Lucas Batista de Sousa` = os devs. Reatribuição no Jira ✅: **Cézar** (`cezar.hiraki`) → MF-4/6/12/40/52/73; **Abraão** (`abraao.oliveira`) → MF-72; **Jonathan Alves** (`jonathan@timeware.com.br`) → MF-7/20/27/71. **Cézar** é revisor do **PR #29** no Azure (conta própria, Approved/vote 10). **Raony** fora do projeto.

---

## 2. Plano de produção (ondas)

**Legenda de status:** ✅ gerado (15/06/2026) · 🔵 aguardando encerramento (projeto aberto) · ⚪ insumo externo já existente.

### Onda 1 — Núcleo de execução

| # | Código do artefato | Documento | Processo | Status |
|---|---|---|---|---|
| 1 | TAP-MILHASFACIL01-001 | Termo de Abertura | GPR | ✅ |
| 2 | PLA-MILHASFACIL01-001 | Plano de Projeto | GPR | ✅ |
| 3 | REQ-MILHASFACIL01-001 | Documento de Requisitos | REQ | ✅ |
| 4 | PCP-MILHASFACIL01-001 | Documento de Design | PCP | ✅ |

### Onda 2 — Restante da execução

| # | Código do artefato | Documento | Processo | Status |
|---|---|---|---|---|
| 5 | ADAP-MILHASFACIL01-001 | Registro de Adaptação do Processo | GPR | ✅ |
| 6 | ITP-MILHASFACIL01-001 | Estratégia de Integração | ITP | ✅ |
| 7 | VV-MILHASFACIL01-001 | Plano de Verificação e Validação | VV | ✅ |
| 8 | REL-VV-MILHASFACIL01-001 | Relatório de Execução de Testes | VV | ✅ |
| 9 | GCO-MILHASFACIL01-001 | Registro de Gerência de Configuração | GCO | ✅ |
| 10 | GDE-MILHASFACIL01-001 | Registro de Análise de Decisão | GDE | ✅ |
| 11 | MED-MILHASFACIL01-001 | Registro de Medição | MED | ✅ |
| 12 | RASTR-MILHASFACIL01-001 | Matriz de Rastreabilidade | REQ | ✅ |
| 13 | RAC-MILHASFACIL01-001 | Relatório de Acompanhamento | GPR | ✅ |
| 14 | CR-MILHASFACIL01-001 | Change Request (CR-MF-001 — filtros antecipados S10→S9) | GPR | ✅ |
| 15 | ATA-MILHASFACIL01-001 | Ata de Kickoff | ORG | ✅ |
| 16 | ATA-MILHASFACIL01-002 | Ata de Aprovação de Arquitetura (Design Review — PO + Tech Lead) | ORG | ✅ |
| 17 | GQA-MILHASFACIL01-001 | Registro de GQA | GPC | ✅ |
| 18 | CAP-MILHASFACIL01-001 | Registro de Capacitação da Equipe | CAP | ✅ |
| 19 | REV-MILHASFACIL01-001 | Registro de Revisão por Pares | VV | ✅ |
| 20 | CTQ-MILHASFACIL01-001 | Cenários de Teste por card (Gherkin + critério + aprovação) | VV | ✅ |
| 21 | GEST-MILHASFACIL01-001 | Planilha de Gestão do Projeto (xlsx, 10 abas) — fonte da verdade de gestão | GPR | ✅ |

> Nota: não há registro de aprovação de **design de UI/UX** porque o **layout é fornecido pelo cliente** (Hub de Milhas); a aprovação de design restringe-se à **arquitetura técnica** (ATA-MILHASFACIL01-002, PO + Tech Lead).

### Onda 3 — Encerramento (aguardar aceite formal ~26/07/2026)

| # | Código do artefato | Documento | Processo | Status |
|---|---|---|---|---|
| 22 | ATA-MILHASFACIL01-003 | Ata de Aceite Final | ORG | 🔵 |
| 23 | TAE-MILHASFACIL01-001 | Termo de Encerramento e Aceite | GPR | 🔵 |
| 24 | LI-MILHASFACIL01-001 | Lições Aprendidas | GPR | 🔵 |

### Fora de escopo

| Item | Decisão |
|---|---|
| AQU — Aquisição | 🔴 **Não gerar registro de projeto.** A equipe é própria da Timeware; não há subcontratação de desenvolvimento. Z-API e as cias aéreas são dependências de serviço/insumo, tratadas em ITP e na seção de Riscos do PLA, não em um registro AQU. |

---

## 3. Evidências em imagem a capturar

Os registros referenciam capturas de tela que devem ser anexadas na subpasta `evidencias/`. Lista consolidada:

| Código | O que capturar | Fonte | Usado em |
|---|---|---|---|
| IMG-JIRA-01 | Board 614 e burndown da sprint | Jira | RAC |
| IMG-DEVOPS-01 | Pull Request com aprovação (vote 10) | Azure DevOps | REV |
| IMG-DEVOPS-02 | Lista dos 29 Pull Requests (28 concluídos + #29 ativo) | Azure DevOps | GCO |
| IMG-DEVOPS-03 | Tags/baselines (v0.1.0–v0.9.0) | Azure DevOps | GCO |
| IMG-CI-01 | Builds/pipelines (execução) | Azure Pipelines | RAC, REL-VV |
| IMG-CI-02 | Builds #52–#60 succeeded | Azure Pipelines | REL-VV |
| IMG-CI-03 | Relatório de cobertura JaCoCo | Azure Pipelines | MED |
| IMG-CI-04 | Estágios do pipeline (Test→Build) | Azure Pipelines | ITP |
| IMG-SWAGGER-01 | Swagger UI da API | API (springdoc) | PCP |
| IMG-ARQ-01 | Diagrama de arquitetura da solução (3 serviços) | Design Review / doc de arquitetura | ATA-002 |
| IMG-QA-01 | Evidência de teste manual — auth (register/login) | QA (homologação) | CTQ |
| IMG-QA-02 | Evidência de teste manual — busca de voos | QA (homologação) | CTQ |
| IMG-QA-03 | Evidência de teste manual — logout/blacklist | QA (homologação) | CTQ |
| IMG-QA-04 | Evidência de teste manual — filtros avançados (S9) | QA (homologação) | CTQ |
| IMG-QA-05 | Evidência de teste manual — airport ILIKE (S9) | QA (homologação) | CTQ |
| IMG-QA-06 | Evidência de teste manual — export CSV (S9) | QA (homologação) | CTQ |

---

## 4. Observações de classificação

- **Formato:** registros produzidos em Markdown (`.md`); conversão para Word (`.docx`) gerada em paralelo na mesma pasta.
- **Release v0.9.0 (15/06/2026):** `develop` foi promovido `develop→homolog→main` nos 3 repositórios, com **tag v0.9.0** em `main`. Os filtros avançados (RF13), export CSV (RF14) e airport ILIKE (MF-64) estão **Entregues (released em `main`)**, como os demais RFs. `main` passou a abranger **Flyway V1–V5 + V9 (`airport_search_index`)**; a migration **V10** (padronização de nomenclatura de BD, MF-73) está no **PR #29 ativo**, ainda não mergeada.
- **Revisão de PR:** registrada em GCO, GQA e REV — os **6 PRs da S9** (#11/#12/#28/#21/#22/#27) estão **concluídos COM revisor** — Tech Lead **Cézar Velazquez** (no Azure sob a conta legada `Mateus Veloso`, Approved/vote 10); os **22 PRs históricos S1–S8** não têm revisor registrado na API (integração retroativa, imutáveis, ressalva); o **PR #29 (MF-73)** está ativo, **aprovado pelo Tech Lead Cézar Velazquez na conta própria dele no Azure DevOps (Approved/vote 10)**, aguardando merge. Em 15/06/2026 foi ativada **branch policy** exigindo ≥1 revisor em `develop` nos 3 repositórios. Jira: MF-64/MF-65/MF-69 = Concluído; **MF-73** criado (padronização de BD). MF-45 corrigido (V7→V4). Intake MF-72 alinhado à fonte da verdade.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Criação do índice-mestre dos registros do projeto MILHASFACIL01. Ondas 1 e 2 geradas (18 registros .md + planilha GEST existente); Onda 3 (encerramento) marcada como aguardando aceite formal. |
