# Análise de Adequação por Processo — Projeto FTFRUKI (SuperApp Força de Vendas)

| Campo | Valor |
|---|---|
| **Projeto** | FTFRUKI — SuperApp Força de Vendas (cliente: Fruki Bebidas) |
| **Pasta** | `mps-nivel-c/oficial/04_registros/FTFRUKI_SuperApp-Forca-de-Vendas` (branch `claude/gallant-hamilton-T0gPb`) |
| **Modelo de referência** | MR-MPS-SW:2024 — Nível C |
| **Base da avaliação** | Checklist de projetos (Bloco 2) + templates/políticas Timeware como referência de completude |
| **Iterações avaliadas** | Pacote 1 (sufixo -001) e PacoteFinal24 (sufixo -002) |
| **Data** | 05/06/2026 |

> **Legenda:** ✅ OK = existe e completo · 🟨 PARCIAL = existe com lacuna · ❌ FALTA = não há · NA = não se aplica.
> Cada item foi comparado com a seção exigida pelo template Timeware correspondente para julgar a completude.

**Resultado geral: 28 ✅ OK · 11 🟨 PARCIAL · 1 ❌ FALTA (40 itens).** Conformidade estrutural alta; as lacunas são de evidência operacional (acompanhamento contínuo, controle formal de mudanças, formalização de revisão por pares e evidências "vivas" de CI/integridade).

---

## GPR — Gerência de Projetos (ref. TPL-GPR-001/002/005)

| Item | Evidência | Status |
|---|---|---|
| R42 Ficha do projeto (cliente, período, escopo, equipe, papéis) | TAP-FRUKI01-001/002 | ✅ OK |
| R43 Plano / cronograma / sprints / marcos | PLA-FRUKI01-001/002 §1–11 | ✅ OK |
| R44 Status reports / atas de acompanhamento | RAC-FRUKI01-001; ATA-001/002/003 | 🟨 PARCIAL |
| R45 Lista/registro de riscos | PLA-FRUKI01-001/002 §9 | ✅ OK |
| R46 Acompanhamento planejado × realizado | PLA §4–5; RAC-FRUKI01-001 | 🟨 PARCIAL |
| R47 Análise de causa de resultados significativos | TAE-FRUKI01-001/002 §6 | ✅ OK |

**Lacunas:** o acompanhamento contínuo só existe para o PacoteFinal24 (RAC parcial até 27/12) — o Pacote 1 não tem status report periódico nem plan×real de esforço/prazo. As atas cobrem marcos formais, não o monitoramento de desvio sprint a sprint.

---

## REQ — Engenharia de Requisitos (ref. TPL-REQ-001/002, TPL-GPR-006)

| Item | Evidência | Status |
|---|---|---|
| R48 Backlog / requisitos (épicos, histórias) | REQ-FRUKI01-001/002 §4–5 | ✅ OK |
| R49 Critérios de aceite + envolvimento de stakeholders | REQ §4/5/7 | ✅ OK |
| R50 Confirmação/aprovação do entendimento | REQ §8; ATA-002/003 | ✅ OK |
| R51 Change requests / controle de mudança | — | ❌ FALTA |
| R52 Matriz de rastreabilidade | RASTR-FRUKI01-001/002 (cobertura 100%) | ✅ OK |
| R53 Registro de validação dos requisitos | REQ §7; PCP §5 | 🟨 PARCIAL |

**Lacunas:** **único FALTA do projeto** — não há Change Request formal (TPL-GPR-006). Os TAE declaram "sem CR", mas o atraso da API Rota PDV e a renomeação "Caixa Preta → Regra de Ouro" foram tratados ad-hoc (GDE/atas), sem evidência de que o controle de mudanças do GPR esteja em operação. A validação dos requisitos é narrativa, sem métricas (% validado, defeitos pós-validação).

---

## PCP — Projeto e Construção do Produto (ref. TPL-PCP-001, TPL-GDE-001)

| Item | Evidência | Status |
|---|---|---|
| R54 Design/arquitetura + rastreabilidade design↔requisitos | PCP-FRUKI01-001/002 | ✅ OK |
| R55 Alternativas, critérios e justificativa de design | PCP §2.4; GDE-FRUKI01-001 | ✅ OK |
| R56 Implementação (código/baseline) conforme design | RASTR; TAE §2 (PRs Azure DevOps) | ✅ OK |
| R57 Documentação técnica mantida (interfaces, sustentação) | PCP §2.1–2.3; TAE §5 | 🟨 PARCIAL |

**Lacunas:** o design cobre arquitetura, modelo de dados e integrações, mas não há manual de sustentação/operação separado — o código fica sob custódia da Fruki sem artefato de manutenção formalizado.

---

## ITP — Integração do Produto (ref. TPL-ITP-001)

| Item | Evidência | Status |
|---|---|---|
| R58 Estratégia de integração + interfaces | ITP-FRUKI01-001/002 §1–2 | ✅ OK |
| R59 Ambiente de integração/homologação | ITP §4 | ✅ OK |
| R60 Avaliação de prontidão de componentes | ITP §5 | ✅ OK |
| R61 Registros de integração (logs build/CI) | PRs Azure DevOps (implícito) | 🟨 PARCIAL |
| R62 Relatório de teste de integração | VV §6 (Gherkin) | ✅ OK |
| R63 Release notes + material de apoio + entrega | TAE; ATA-003; AAB v2.0 | ✅ OK |

**Lacunas:** os logs de build/CI (pipelines) não estão documentados/anexados — a evidência vive nos PRs do Azure DevOps. Recomenda-se referenciar links de CI com hash de commit.

---

## VV — Verificação e Validação (ref. TPL-VV-001/002)

| Item | Evidência | Status |
|---|---|---|
| R64 Lista de produtos de trabalho para V&V | VV §1 | ✅ OK |
| R65 Evidência de revisão por pares (PR review) | VV §3; GCO §; PRs | 🟨 PARCIAL |
| R66 Evidência de testes + registro de defeitos | VV §4–6; ATA-007 (P-01..P-03) | ✅ OK |
| R67 Checklist/procedimento de revisão por pares | VV §3 | 🟨 PARCIAL |
| R68 Relatório de V&V analisado e comunicado | VV §5 | ✅ OK |
| R69 Evidência de homologação | TAE; ATA-003/007 | ✅ OK |

**Lacunas:** a revisão por pares existe (Jardel revisa PRs) e os critérios estão descritos, mas **não há registro formal por PR no padrão TPL-VV-002** (tabela de apontamentos com severidade/situação). É a lacuna mais repetida do bloco de qualidade.

---

## GCO — Gerência de Configuração (projeto) (ref. PLA-GCO-001)

| Item | Evidência | Status |
|---|---|---|
| R70 Lista de itens de configuração | GCO-FRUKI01-001 §1 | ✅ OK |
| R71 Baseline final / tags / releases | GCO §3 (BL-01..BL-05) | ✅ OK |
| R72 Histórico de modificações dos ICs | GCO §4 (CM-01..CM-03) | 🟨 PARCIAL |
| R73 Relatório de auditoria de configuração | GCO §5 (05/06/2026 — Conforme) | ✅ OK |
| R74 Pacote de entrega final / hash-checksum | TAE-002; GCO | 🟨 PARCIAL |

**Lacunas:** o changelog/git log não está anexado (só referência nominal a PRs) e não há hash/checksum de integridade do pacote final (AAB v2.0).

---

## Aceite & Homologação

| Item | Evidência | Status |
|---|---|---|
| R75 Termo de aceite assinado | TAE-001/002; ATA-003 | ✅ OK |
| R76 E-mail de aceite/entrega do cliente | TAE/ATA (citado) | 🟨 PARCIAL |
| R77 Ata de homologação | ATA-FRUKI01-003 | ✅ OK |

**Lacunas:** o aceite via e-mail/Teams é citado mas o **artefato original (domínio externo) não está anexado** — recomenda-se anexar PDF/print do e-mail ou ID da reunião.

---

## MED — Medição (projeto)

| Item | Evidência | Status |
|---|---|---|
| R78 Indicadores do projeto (prazo, defeitos, retrabalho, plan×real) | MED-FRUKI01-001 (M1–M6) | ✅ OK |

**Observação:** indicadores bem cobertos — aderência a prazo, desvio de esforço, velocity, densidade e taxa de contenção de defeitos (100%, 0 defeitos em produção).

---

## GDE — Decisões / Qualidade (projeto)

| Item | Evidência | Status |
|---|---|---|
| R79 Decision log do projeto | GDE-FRUKI01-001 | ✅ OK |
| R80 Checklist de qualidade / aderência ao processo | GQA-FRUKI01-001 | ✅ OK |
| R81 Registro de não conformidades e ações corretivas | GQA; MED | 🟨 PARCIAL |

**Lacunas:** a GQA reporta "sem não conformidades"; os problemas reais (atraso da API Rota PDV, defeitos do piloto) foram geridos como risco/defeito, não como **NC + ação corretiva** formal (TPL-GPC-001 §4). Note-se que a Timeware não possui template dedicado de NC — lacuna organizacional já identificada em análises anteriores.

---

## Síntese e recomendações

**Pontos fortes**
- Conjunto documental completo nos dois pacotes (TAP, PLA, REQ, RASTR, PCP, ITP, VV, GCO, GQA, MED, GDE, TAE) — nenhum documento estrutural ausente.
- Rastreabilidade necessidade → requisito → design → PR → teste com cobertura 100%.
- Decisões técnicas registradas com alternativas/critérios (GDE) e GQA auditada sem achados.
- Ciclo de qualidade efetivo: testes Gherkin, piloto com vendedores reais, contenção de 100% dos defeitos.

**Lacunas priorizadas**
1. **Controle formal de mudanças (R51 — FALTA):** adotar Change Request (TPL-GPR-006) mesmo para registrar atraso de API e renomeações, evidenciando o processo em operação.
2. **Acompanhamento contínuo (R44/R46):** produzir status report por sprint/mês também para o Pacote 1; hoje só o PacoteFinal24 tem RAC parcial.
3. **Formalizar revisão por pares (R65/R67):** registrar cada PR no padrão TPL-VV-002 (apontamentos, severidade, situação).
4. **Evidências "vivas" (R61/R72/R74):** referenciar logs de CI/commit, git log e hash/checksum do pacote de entrega.
5. **Documentação de sustentação (R57)** e **anexo do aceite externo (R76)**.
6. **Registro de NC + ação corretiva (R81):** depende de um template organizacional de NC que a Timeware ainda não possui.
