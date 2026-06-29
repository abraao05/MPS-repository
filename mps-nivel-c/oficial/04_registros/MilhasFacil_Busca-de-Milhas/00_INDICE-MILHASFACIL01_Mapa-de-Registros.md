# Índice de Registros do Projeto — MilhasFacil

| Campo | Valor |
|---|---|
| **Documento** | INDICE-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 3.0 |
| **Data** | 26/06/2026 |
| **Natureza** | Documento de controle / índice — apoio interno. Organiza a produção das evidências do projeto; **não é, ele próprio, evidência auditável pela ASR**. |
| **Fonte consolidada** | Planilha de Gestão `GEST-MILHASFACIL01-001` (fonte da verdade de gestão) + código real dos três repositórios + APIs GitLab/Jira (coleta 15/06/2026) |

> **Como usar:** este índice mapeia todos os registros MPS a produzir para o projeto MILHASFACIL01, o status de cada um e o processo MPS-SW que evidenciam. Conforme cada artefato for gerado ou atualizado, ajustar a coluna **Status** e registrar no histórico ao final.

---

## 1. Contexto e momento do projeto

- **Início:** 09/02/2026 · **Encerramento previsto:** 26/07/2026.
- **Status atual (26/06/2026):** **Sprint 10 de 12 em andamento** (15–28/06/2026); projeto **ABERTO**.
- **Consequência para a documentação:** todo o conjunto de **execução** (Ondas 1 e 2) já pode ser produzido com base no realizado em S1–S10; os artefatos de **encerramento** (Onda 3: Termo de Encerramento, Lições Aprendidas, Ata de Aceite Final) **aguardam o aceite formal** previsto para o fim do projeto (~26/07/2026) e ainda não se aplicam.
- **Equipe (time atual):** Abraão (GP — gestão, fora do DevOps), Cézar Velazquez (Tech Lead / Arquiteto / DevOps — revisor de MR, GitLab: cezar.velazquez), Jonathan Alves (QA — teste manual, GitLab: jonathan.barbosa), Carol/Caroline (GQA independente — fora do DevOps, GitLab: caroline.sousa), Felipe Santos (GitLab: felipe.siqueira) · Lucas Batista (GitLab: lucas.batista) · Henry Oliveira (GitLab: henry.komatsu) (Devs).

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
| IMG-GITLAB-01 | Merge Requests com 2 revisores aprovados; api !15 ativo | GitLab | REV |
| IMG-GITLAB-02 | Lista dos 39 MRs (38 concluídos + api !15 ativo) | GitLab | GCO |
| IMG-GITLAB-03 | Tags/baselines (v0.1.0–v0.9.0) + branches protegidas | GitLab | GCO |
| IMG-CI-01 | Pipelines GitLab CI (success) + gate JaCoCo 80% | GitLab CI/CD | RAC, REL-VV |
| IMG-CI-02 | Pipelines recentes succeeded (S9) | GitLab CI/CD | REL-VV |
| IMG-CI-03 | Relatório de cobertura JaCoCo | GitLab CI/CD artifacts | MED |
| IMG-CI-04 | Estágios do pipeline (Test→Build) | GitLab CI/CD | ITP |
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
- **Release v0.9.0 (15/06/2026):** `develop` foi promovido `develop→homolog→main` nos 3 repositórios, com **tag v0.9.0** em `main`. Os filtros avançados (RF13), export CSV (RF14) e airport ILIKE (MF-64) estão **Entregues (released em `main`)**. `main` passou a abranger **Flyway V1–V5 + V9 (`airport_search_index`)**; a migration **V10** (padronização de nomenclatura de BD, MF-73) está no **api !15 ativo**, ainda não mergeada.
- **Revisão de MR (26/06/2026):** todos os **39 MRs** possuem **exatamente 2 revisores aprovados** (verificado via SQL `merge_request_reviewers` — 0 linhas com contagem ≠ 2). Meta "MRs sem revisor = 0" — **Cumprida**. O **api !15 (MF-73)** está ativo, aprovado por cezar.velazquez + lucas.batista, aguardando merge. Proteção de branch (`push=No one`) ativa em `main`/`homolog`/`develop` nos 3 repositórios. Jira: MF-64/MF-65/MF-69 = Concluído; **MF-73** em andamento.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Criação do índice-mestre dos registros do projeto MILHASFACIL01. Ondas 1 e 2 geradas (18 registros .md + planilha GEST existente); Onda 3 (encerramento) marcada como aguardando aceite formal. |
| 2.0 | 25/06/2026 | Auditoria MPS.BR Nível C | Reconciliação: status S10, plataforma GitLab, remoção de mapa de aliases Azure DevOps. |
| 3.0 | 26/06/2026 | Time de Melhoria Contínua | Reconciliação final MPS.BR Nível C — remoção de "Mateus Veloso" e aliases legados; contagem 29→37 MRs; api !15 substitui "MR #29"; referências IMG-DEVOPS-* atualizadas para IMG-GITLAB-*; meta "MRs sem revisor=0" confirmada (todos os 37 MRs com 2 revisores via SQL). |
| 4.0 | 29/06/2026 | Auditoria MPS.BR Nível C | Contagem de MRs atualizada 37 → 39 (inclusão de api !20/!21 — correção de build develop/homolog) em §3 (IMG-GITLAB-02) e §4. |
