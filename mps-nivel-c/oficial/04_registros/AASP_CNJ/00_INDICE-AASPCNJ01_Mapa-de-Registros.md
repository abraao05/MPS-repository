# Índice de Registros do Projeto — AASP_CNJ

| Campo | Valor |
|---|---|
| **Documento** | INDICE-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Código do projeto** | AASPCNJ01 |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.1 |
| **Data** | 11/06/2026 |
| **Natureza** | Documento de controle / índice — apoio interno. Organiza a produção das evidências do projeto; **não é, ele próprio, evidência auditável pela ASR**. |
| **Fonte consolidada** | `AASP_CNJ_Registro_de_Projeto` v1.0 (08/06/2026) |

> **Como usar:** este índice mapeia todos os registros MPS a produzir para o projeto AASPCNJ01, o status de cada um, a seção do documento-fonte que o alimenta e o dado ainda pendente. Conforme cada artefato for gerado, atualizar a coluna **Status** e registrar no histórico ao final.

---

## 1. Contexto e momento do projeto

- **Início:** 01/10/2025 · **Encerramento previsto:** 30/06/2026.
- **Status atual (08/06/2026):** desenvolvimento concluído; implantação em produção em andamento.
- **Fases do processo-padrão (PRO-GPC-001):** 1 a 6 concluídas; **Fase 7 (Homologação, Entrega e Encerramento) em andamento**.
- **Consequência para a documentação:** todo o conjunto de **execução** pode ser produzido agora; os artefatos de **encerramento** (TAE, Lições Aprendidas, Ata de Aceite Final) aguardam o aceite formal (~30/06/2026).

---

## 2. Plano de produção (ondas)

A produção segue três ondas, da maior para a menor prontidão de insumo.

**Legenda de status:** ✅ gerado (11/06/2026) · 🔵 aguardando encerramento · 🔴 não se aplica.

> **Atualização v1.1 (11/06/2026):** Ondas 1 e 2 geradas — **18 registros** em `.md` na pasta do projeto. Pendente: Onda 3 (encerramento) e a planilha de gestão (GEST). Os documentos usam **papéis genéricos** (sem nomes) — substituição por nomes reais pendente do envio do roster.

### Onda 1 — Núcleo de execução (insumo forte)

| # | Código do artefato | Documento | Processo | Seção-fonte | Status |
|---|---|---|---|---|---|
| 1 | TAP-AASPCNJ01-001 | Termo de Abertura | GPR | 1 | ✅ |
| 2 | PLA-AASPCNJ01-001 | Plano de Projeto | GPR | 1, 3 | ✅ |
| 3 | REQ-AASPCNJ01-001 | Documento de Requisitos | REQ | 2 | ✅ |
| 4 | PCP-AASPCNJ01-001 | Documento de Design | PCP | 4 | ✅ |

### Onda 2 — Restante da execução

| # | Código do artefato | Documento | Processo | Seção-fonte | Status |
|---|---|---|---|---|---|
| 5 | ADAP-AASPCNJ01-001 | Registro de Adaptação do Processo | GPR | — | ✅ |
| 6 | ITP-AASPCNJ01-001 | Estratégia de Integração | ITP | 6 | ✅ |
| 7 | VV-AASPCNJ01-001 | Plano de Verificação e Validação | VV | 7.1–7.3 | ✅ |
| 8 | REL-VV-AASPCNJ01-001 | Relatório de Execução de Testes | VV | 7.2, 7.4 | ✅ |
| 9 | GCO-AASPCNJ01-001 | Registro de Gerência de Configuração | GCO | 5 | ✅ |
| 10 | GDE-AASPCNJ01-001 | Registro de Análise de Decisão | GDE | 12 | ✅ |
| 11 | MED-AASPCNJ01-001 | Registro de Medição | MED | 8 | ✅ |
| 12 | RASTR-AASPCNJ01-001 | Matriz de Rastreabilidade | REQ | 2.3 + 4 + 7 | ✅ |
| 13 | RAC-AASPCNJ01-001 | Relatório de Acompanhamento | GPR | 3.2, 8.2 | ✅ |
| 14 | CR-AASPCNJ01-001 | Change Request (pausa da 2ª instância EPROC) | GPR | 5.3, D06 | ✅ |
| 15 | ATA-AASPCNJ01-001 | Ata de Alinhamento — Fluxo API CNJ (07/04/2026) | ORG | 9.1 | ✅ |
| 16 | GQA-AASPCNJ01-001 | Registro de GQA | GPC | 9 | ✅ |
| 17 | GEST-AASPCNJ01 | Planilha de Gestão do Projeto (xlsx) | GPR | 3.2, 3.4, 8 | 🔵 a produzir |
| 18 | CAP-AASPCNJ01-001 | Registro de Capacitação da Equipe | CAP | 11 | ✅ |
| 19 | REV-AASPCNJ01-001 | Registro de Revisão por Pares | VV | 9.1, 11 | ✅ |

### Onda 3 — Encerramento (aguardar aceite formal ~30/06/2026)

| # | Código do artefato | Documento | Processo | Seção-fonte | Status |
|---|---|---|---|---|---|
| 20 | ATA-AASPCNJ01-002 | Ata de Aceite Final | ORG | — | 🔵 |
| 21 | TAE-AASPCNJ01-001 | Termo de Encerramento e Aceite | GPR | — | 🔵 |
| 22 | LI-AASPCNJ01-001 | Lições Aprendidas | GPR | (implícito) | 🔵 |

### Fora de escopo

| Item | Decisão |
|---|---|
| AQU — Aquisição (seção 10 do doc-fonte) | 🔴 **Não gerar registro de projeto.** No `MAPA-ORG-001`, AQU é candidato a não-aplicável (nenhum projeto subcontrata desenvolvimento). DataJud/Solucionário/Botmax/AWS/Azure são dependências/insumos de serviço — o conteúdo é reaproveitado em ITP, PCP e na seção de Riscos do PLA, não em um registro AQU. |

---

## 3. Dados pendentes (necessários antes de gerar)

> Como a opção escolhida foi **nomes reais**, os registros de identificação (TAP, PLA, GQA, ATAs) dependem dos dados abaixo. Nada será inventado — onde faltar, o campo fica em aberto e é sinalizado.

**Pessoas (papéis → nomes reais):**
- Gerente de Projeto / Tech Lead
- Arquiteto de Software
- Desenvolvedor Sênior (Principal)
- Desenvolvedor (Suporte)
- Analista de Testes
- Representante / sponsor da AASP (quem concede o aceite)
- **Auditor de GQA** — deve ser independente da equipe (padrão organizacional: COO)

**Outros dados:**
- Contrato / forma de contratação com a AASP (TAP) — ex.: alocação de squad, OS, contrato fechado.
- GQA (seção 9 está rasa): marcos auditados, datas, itens verificados, % de conformidade e desvios.
- Baseline de configuração entregue (GCO) — confirmar a tag de versão (o doc cita "v240").
- MED: confirmar se mapeamos os indicadores da seção 8 para o conjunto padrão M1–M9 do `PLA-MED-001` ou mantemos os indicadores próprios do projeto.

**Decisões de adaptação (ADAP)** — proponho a partir do doc, para sua validação:
- Ausência de ambiente de Elasticsearch dedicado → homologação por amostragem (restrição 2.5).
- Acúmulo de papéis (Dev Sênior atuando também em testes nas fases iniciais).
- Nível de documentação e rito de GMUD para implantação.

---

## 4. Observações de classificação

- **Seção 4 do doc-fonte está rotulada "(OSW)"**, mas o conteúdo (arquitetura, componentes, fallback) é de **PCP**. O registro será gerado como PCP-AASPCNJ01-001. OSW é processo organizacional, não de projeto.
- **Formato:** registros produzidos em Markdown (`.md`); conversão para Word apenas quando solicitado.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Criação do índice-mestre de registros do projeto AASPCNJ01 a partir do documento-fonte consolidado v1.0. Estrutura definida; conteúdo dos registros a produzir. |
| 1.1 | 11/06/2026 | Time de Melhoria Contínua | Ondas 1 e 2 geradas (18 registros .md). Status atualizado para ✅. Pendentes: planilha de gestão (GEST) e Onda 3 (encerramento). Documentos com papéis genéricos — substituição por nomes reais pendente. |
