# Registro de Gerência de Configuração — SuperApp Fruki · Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | GCO-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Força de Vendas (Pacote 1 + Pacote Final 24) |
| **Versão** | 1.4 |
| **Data** | 05/06/2026 |
| **Responsável** | Abraão Oliveira |
| **Referência organizacional** | PLA-GCO-001 — Plano de Gerência de Configuração |

---

## 1. Itens de configuração do projeto

Conforme PLA-GCO-001 seção 3.1, os seguintes itens de configuração foram identificados e colocados sob controle para este projeto:

| IC | Repositório / localização | Nível de controle |
|---|---|---|
| Código-fonte do SuperApp Fruki (Pacote 1 + Pacote Final 24) | Azure DevOps Fruki — `https://dev.azure.com/fruki/superapp/_git/fruki-app.git` | Controle de versão Git + Pull Request com revisão pelo Jardel antes do merge |
| TAP-FRUKI01-001 e TAP-FRUKI01-002 | Repositório MPS Timeware (`mps-nivel-c/oficial/04_registros/FTFRUKI_SuperApp-Forca-de-Vendas/`) | Versionamento conforme CONV-ORG-001 |
| PLA-FRUKI01-001 e PLA-FRUKI01-002 | Idem | Idem — documentos baseline aprovados pelo cliente |
| REQ-FRUKI01-001 e REQ-FRUKI01-002 | Idem | Idem |
| ADAP-FRUKI01-001 e ADAP-FRUKI01-002 | Idem | Idem |
| PCP-FRUKI01-001 e PCP-FRUKI01-002 | Idem | Idem |
| ITP-FRUKI01-001 e ITP-FRUKI01-002 | Idem | Idem |
| VV-FRUKI01-001 e VV-FRUKI01-002 | Idem | Idem |
| RASTR-FRUKI01-001 e RASTR-FRUKI01-002 | Idem | Idem |
| TAE-FRUKI01-001 e TAE-FRUKI01-002 | Idem | Idem |
| ATAs (ATA-FRUKI01-001 a ATA-FRUKI01-008) | Idem | Idem |
| RAC-FRUKI01-001 e RAC-FRUKI01-002 | Idem | Idem |
| GQA-FRUKI01-001 | Idem | Idem |
| GDE-FRUKI01-001 | Idem | Idem |
| CR-FRUKI01-001 | Idem | Idem — mudança de escopo aprovada antes do início da execução |
| MED-FRUKI01-001 | Idem | Idem |
| LI-FRUKI01-001 | Idem | Idem |
| RAC-FRUKI01-001 | Idem | Idem |
| Build APK de homologação (por entrega) | Expo — link compartilhado com cliente antes de cada sprint | Distribuição controlada — link único por build |
| Build AAB v2.0 (produção) | Entregue ao time Fruki para publicação na Play Store | Imutável após entrega — versionamento 2.0 |

---

## 2. Estrutura de branches (repositório Fruki)

| Branch | Descrição | Criado por |
|---|---|---|
| `main` | Branch principal do repositório Fruki; código estável em produção | Fruki (pré-existente) |
| `feature/novos-recursos-superapp` | Branch do Pacote 1 (Metas/RV) | Timeware — Jun/2025 |
| `feature/nao-alocados` | Branch Sprint 1 Pacote Final 24 (Pedidos Não Alocados) | Timeware — Out/2025 |
| `feature/regra-de-ouro` | Branch Sprint 2 Pacote Final 24 (Regra de Ouro) | Timeware — Nov/2025 |
| `feature/pdv-rota` | Branch Sprint 3 Pacote Final 24 (PDV / Rota PDV) | Timeware — Dez/2025 |

**Política de merge:** nenhuma branch é mergeada na `main` sem revisão e aprovação explícita de Jardel Dargas Silva via Pull Request no Azure DevOps.

---

## 3. Baselines estabelecidas

| Baseline | Evento | Data | Identificador |
|---|---|---|---|
| **BL-01** — Módulo Metas/RV | Merge da branch `feature/novos-recursos-superapp` após revisão de Jardel; aceite do Pacote 1 | Set/2025 | PR Pacote 1 — Azure DevOps Fruki |
| **BL-02** — Módulo Pedidos Não Alocados | Merge PR #57 após revisão de Jardel | 25/10/2025 | PR #57 — Azure DevOps Fruki |
| **BL-03** — Módulo Regra de Ouro | Merge da branch `feature/regra-de-ouro` após revisão de Jardel | Nov/2025 | PR Regra de Ouro — Azure DevOps Fruki |
| **BL-04** — Módulo PDV / Rota PDV | Merge da branch `feature/pdv-rota` após revisão de Jardel | Jan/2026 | PR PDV — Azure DevOps Fruki |
| **BL-05** — Release v2.0 (AAB) | Build AAB versionado 2.0 gerado e entregue para publicação na Play Store | Jan/2026 | `app.json` / `package.json` v2.0 — Azure DevOps Fruki |

---

## 4. Controle de mudanças

| # | Mudança | Tipo | Solicitante | Aprovada por | Data | Ref. |
|---|---|---|---|---|---|---|
| CM-01 | Renomeação da funcionalidade "Caixa Preta" para "Regra de Ouro" em toda a interface | Mudança de nomenclatura de UX (sem impacto no escopo técnico) | Cecília Ribeiro | Abraão Oliveira | 22/10/2025 | GDE-FRUKI01-001 — Decisão 2 |
| CM-02 | Normalização de dados de pedidos não alocados implementada no front-end (em vez de solicitar correção da API) | Decisão técnica de implementação | Abraão Oliveira / Luca Watson | Abraão Oliveira | Out/2025 | GDE-FRUKI01-001 — Decisão 1 |
| CM-03 | Adição do módulo Regra de Ouro sem custo adicional (estava fora do escopo original da proposta) | Ampliação de escopo sem impacto comercial | Leandro Lottermann | Abraão Oliveira / Tiago Nascimento | 09/10/2025 | CR-FRUKI01-001; TAP-FRUKI01-002; Fireflies ID: HWwWGbMe3glWfXgl |

---

## 5. Auditoria de configuração

| Item auditado | Data | Resultado |
|---|---|---|
| Todos os documentos do Pacote 1 versionados conforme CONV-ORG-001 | 05/06/2026 | Conforme — versões 1.0 e 1.1 aplicadas corretamente |
| Todos os documentos do Pacote Final 24 versionados conforme CONV-ORG-001 | 05/06/2026 | Conforme — versão 1.0 em todos |
| Código-fonte entregue via PR revisada por Jardel em todas as branches | 05/06/2026 | Conforme — PRs #57, Regra de Ouro e PDV aprovadas antes do merge |
| Build AAB v2.0 entregue e versionado corretamente | 05/06/2026 | Conforme — `app.json` / `package.json` com versão 2.0 |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — Pacote 1 (ICs, branches, baselines, mudanças) |
| 1.1 | 05/06/2026 | Abraão Oliveira | Inclusão do Pacote Final 24 — branches, baselines BL-02 a BL-05, mudanças CM-01 a CM-03 |
| 1.2 | 05/06/2026 | Abraão Oliveira | Atualização da lista de ICs: ATAs expandidas de ATA-003 para ATA-007 (atas de validação de sprint e piloto) |
| 1.3 | 05/06/2026 | Abraão Oliveira | CR-FRUKI01-001 adicionado à lista de ICs; CM-03 atualizado com referência ao CR formal |
| 1.4 | 05/06/2026 | Abraão Oliveira | ICs expandidos: ATAs até ATA-008, RAC-001 e RAC-002 adicionados |
