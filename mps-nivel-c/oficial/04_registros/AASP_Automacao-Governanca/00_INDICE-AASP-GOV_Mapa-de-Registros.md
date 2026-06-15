# Índice de Registros do Projeto — AASP_Automacao-Governanca

| Campo | Valor |
|---|---|
| **Documento** | INDICE-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Código do projeto** | AASP-GOV |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Natureza** | Documento de controle / índice — apoio interno. Organiza os registros do projeto; **não é, ele próprio, evidência auditável pela ASR**. |
| **Fonte consolidada** | `AASP_AutomacaoGovernanca_Registro_de_Projeto` v2.0 (08/06/2026) |

> **Como usar:** este índice mapeia todos os registros MPS produzidos para o projeto AASP-GOV, a área de processo de cada um e a seção do documento-fonte que o alimenta. O projeto está **encerrado** (02/06/2026), portanto todos os registros de execução e de encerramento foram produzidos.

---

## 1. Contexto e momento do projeto

- **Início:** 14/04/2026 · **Encerramento:** 02/06/2026 · **Duração:** ~7 semanas.
- **Status atual:** Encerrado — desenvolvimento concluído, homologado e aceite emitido.
- **Auditoria GQA:** realizada em 08/06/2026 (Jonathan Barbosa, independente) — 10 de 10 itens conformes, 0 desvios.
- **Equipe:** Cezar Hiraki Velazquez (GP / Tech Lead), Raony Chagas (Dev Sênior), Allan Barbosa Patrocínio Alves (Dev). Patrocinador/cliente: Marcos Correa Fernandez Turnes (AASP).

---

## 2. Registros produzidos

**Legenda de status:** ✅ gerado (15/06/2026).

| # | Código do artefato | Documento | Processo | Seção-fonte | Status |
|---|---|---|---|---|---|
| 1 | TAP-AASP-GOV-001 | Termo de Abertura | GPR | 2 | ✅ |
| 2 | ADAP-AASP-GOV-001 | Registro de Adaptação do Processo | GPR | 3 | ✅ |
| 3 | PLA-AASP-GOV-001 | Plano de Projeto | GPR | 6 | ✅ |
| 4 | REQ-AASP-GOV-001 | Documento de Requisitos | REQ | 4 | ✅ |
| 5 | RASTR-AASP-GOV-001 | Matriz de Rastreabilidade | REQ | 5 | ✅ |
| 6 | PCP-AASP-GOV-001 | Documento de Design | PCP | 7 | ✅ |
| 7 | ITP-AASP-GOV-001 | Estratégia de Integração | ITP | 9 | ✅ |
| 8 | VV-AASP-GOV-001 | Plano de Verificação e Validação | VV | 10.1–10.4 | ✅ |
| 9 | REL-VV-AASP-GOV-001 | Relatório de Execução de Testes | VV | 10.2, 10.3, 10.5 | ✅ |
| 10 | GCO-AASP-GOV-001 | Registro de Gerência de Configuração | GCO | 8 | ✅ |
| 11 | GDE-AASP-GOV-001 | Registro de Análise de Decisão | GDE | 15 | ✅ |
| 12 | MED-AASP-GOV-001 | Registro de Medição | MED | 11 | ✅ |
| 13 | AQU-AASP-GOV-001 | Registro de Aquisição | AQU | 13 | ✅ |
| 14 | CAP-AASP-GOV-001 | Registro de Capacitação da Equipe | CAP | 14 | ✅ |
| 15 | RAC-AASP-GOV-001 | Relatório de Acompanhamento | GPR | 6, 10.5 | ✅ |
| 16 | REV-AASP-GOV-001 | Registro de Revisão por Pares | VV | 8.2, 14 | ✅ |
| 17 | GQA-AASP-GOV-001 | Registro de GQA | GPC | 12 | ✅ |
| 18 | ATA-AASP-GOV-001 | Ata de Reunião de Abertura (Kickoff) | ORG | 1.3, 3.3, 15 | ✅ |
| 19 | LI-AASP-GOV-001 | Lições Aprendidas | GPR | 16.5 | ✅ |
| 20 | TAE-AASP-GOV-001 | Termo de Encerramento | GPR | 16 | ✅ |
| 21 | GEST-AASP-GOV | Planilha de Gestão do Projeto (xlsx) | GPR | 5, 6, 11 | ✅ |

---

## 3. Cobertura de processos MPS-SW Nível C

O documento-fonte lista os processos cobertos: **GPR · REQ · OSW · ITP · VV · GPC · MED · GDE · GCO · CAP · AQU**. Mapeamento para os registros:

| Processo | Registro(s) |
|---|---|
| GPR — Gerência de Projetos | TAP, ADAP, PLA, RAC, LI, TAE, GEST |
| REQ — Engenharia de Requisitos | REQ, RASTR |
| OSW / PCP — Projeto e Construção do Produto | PCP (seção rotulada "OSW" na fonte, reclassificada como PCP — OSW é processo organizacional, não de projeto) |
| ITP — Integração do Produto | ITP |
| VV — Verificação e Validação | VV, REL-VV, REV |
| GPC — Gerência de Processos (GQA) | GQA |
| MED — Medição | MED |
| GDE — Gerência de Decisões | GDE |
| GCO — Gerência de Configuração | GCO |
| CAP — Capacitação | CAP |
| AQU — Aquisição | AQU |
| ORG — Governança Organizacional | ATA |

---

## 4. Observações de classificação

- **Seção 7 do doc-fonte está rotulada "(OSW)"**, mas o conteúdo (arquitetura, camadas, fluxo, mapeamento de entidades) é de **PCP**. Gerado como PCP-AASP-GOV-001.
- **Change Request (CR):** não se aplica — o escopo foi fixo desde a abertura; ocorreram apenas correções de defeitos na homologação (Fase 4), não mudanças de escopo.
- **AQU:** diferentemente de projetos sem subcontratação, este registro foi produzido porque o doc-fonte lista AQU como processo coberto e detalha as dependências de terceiros (APIs externas + pacotes NuGet); o registro é "leve" (sem subcontratação de desenvolvimento).
- **Formato:** registros produzidos em Markdown (`.md`) com conversão para Word (`.docx`) no padrão Timeware.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Criação do índice-mestre e geração dos 21 registros do projeto AASP-GOV a partir do documento-fonte consolidado v2.0 (08/06/2026), em `.md` e `.docx`. |
