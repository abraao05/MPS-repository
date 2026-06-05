# Diagnóstico do Checklist de Evidências — MPS-SW Nível C — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | DIAG-ORG-001 — Diagnóstico do Checklist de Documentação e Evidências [INTERNO] |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Modelo de referência** | MR-MPS-SW:2024 — Nível C |
| **Base de comparação** | Checklist_MPS_SW_NivelC_Timeware.xlsx (avaliadora ASR) × repositório de processos (git) |
| **Saída** | `Checklist_MPS_SW_NivelC_Timeware_preenchido.xlsx` |

> **Nota:** documento de apoio interno (não é evidência MPS, não auditável pela ASR). Compara o set mínimo do checklist com o que existe hoje no repositório e aponta o que falta. Nenhum status foi inventado: cada classificação aponta o artefato de origem no git ou registra a ausência.

---

## 1. Como ler

Legenda usada (conforme o checklist): **OK** = temos e localizado · **PARCIAL** = existe mas com lacuna · **FALTA** = não temos · **NA** = não se aplica (justificar).

O diagnóstico separa **camada de definição** (políticas, processos, planos, templates — o "como fazer") da **camada de evidência** (registros reais de uso, por projeto — o "fizemos"). Este é o eixo central do resultado.

---

## 2. Conclusão em uma frase

A **camada de definição organizacional está madura** (a maioria dos itens corporativos é OK ou PARCIAL); a **camada de evidência é o gargalo**: nenhum dos 4 projetos da amostra foi selecionado, então **todo o Bloco 2 (por projeto) está FALTA**, e vários itens corporativos que são *registros de uso* (relatórios, dashboards, auditorias) ainda não foram produzidos.

---

## 3. Bloco 1 — Corporativo / Unidade Organizacional

Resumo: **8 OK · 16 PARCIAL · 10 FALTA · 1 NA** (35 itens).

### OK (8) — temos e está localizado
- Política/diretrizes organizacionais → **POL-ORG-001**
- Inventário de ativos de processo → **PLA-GPC-001 §2** + **MAPA-ORG-001**
- Lista de ativos reutilizáveis → inventário + lista de templates (**README §5**)
- Definição de indicadores (fonte/periodicidade/responsável) → **PLA-MED-001 §3**
- Critérios de avaliação de fornecedores → **PRO-AQU-001 §3** *(candidato a NA — confirmar com a ASR)*
- Procedimento/critérios de decisão estruturada → **PRO-GDE-001**
- Procedimento de GC e controle de mudanças → **PLA-GCO-001 §4** + **TPL-GPR-006**
- Plano/programa de treinamento organizacional → **PLA-CAP-001**

### PARCIAL (16) — existe a definição, falta a evidência de uso ou um artefato consolidado
| Item | O que existe | Lacuna |
|---|---|---|
| Definição da unidade/escopo | README + MAPA-ORG-001 ([INTERNO]) | Documento oficial único para a ASR |
| Matriz RACI | Papéis em PRO-OSW-001 §4 e seções "Papéis" | Matriz RACI consolidada |
| Cola/roteiro de entrevista por papel | Materiais TREINO-A..K | Roteiro de entrevista da avaliação |
| Registro de alocação de recursos/orçamento | PRO-OSW-001 §3 (define) | Registro/evidência efetiva |
| Relatórios gerenciais de desempenho | PRO-OSW-001 §7 (define análise crítica) | Relatórios efetivos |
| Biblioteca de processos | 12 processos + capacidade no git | Publicação/confirmação no Confluence |
| Registro de melhorias/lições aprendidas | PLA-GPC-001 §5.1 (define) | Registros efetivos (retrospectivas) |
| Procedimento de análise de causa | Previsto em GPR19/PLA-GPC-001 | Procedimento organizacional dedicado |
| Matriz de competências | PLA-CAP-001 §3 (necessidades/lacunas) | Matriz formal por papel |
| Registros de treinamentos realizados | PLA-CAP-001 §4 + TREINO-* | Presença/conclusão |
| Avaliação de efetividade dos treinamentos | PLA-CAP-001 §5 (define) | Avaliações efetivas |
| Decision log organizacional | TPL-GDE-001 (RAD) | Log populado |
| Política de arquivamento e retenção | CONV-ORG-001 + Git/Confluence | Política explícita de retenção |
| Plano/checklist de auditoria de configuração | PLA-GCO-001 §7 (define) | Checklist/plano dedicado |
| Matriz de evidências consolidada | MAPA-ORG-001 (resultado→artefato) | Matriz com links (Confluence/Jira/Git) |
| Matriz de rastreabilidade organizacional | MAPA-ORG-001 | Consolidar + links |

### FALTA (10) — não existe no repositório
1. Organograma da unidade
2. Lista de projetos da amostra (4+1) — **pendência-chave** (MAPA-ORG-001 §3)
3. Lista de entrevistados por papel
4. Registro de aderência/auditoria dos processos nos projetos (evidência de GQA)
5. Registros de onboarding
6. Currículos/resumos dos entrevistados
7. Dashboard consolidado de indicadores — pendência MED (consolidação)
8. Registro de análise dos indicadores e decisão tomada
9. Contratos/pedidos + evidência de uso (AQU) — candidato a NA
10. Explicação de arquivamento e uso do Jira importado (data room)

### NA (1)
- Avaliação do fornecedor → sem aquisição/subcontratação nos projetos da amostra (**confirmar NA com a ASR**).

---

## 4. Bloco 2 — Por Projeto

**Todos os 40 itens × 5 projetos = FALTA.**

Motivo: a definição e os **templates estão prontos** (camada organizacional), mas a **evidência de uso não foi produzida** porque os 4 projetos da avaliação ainda não foram selecionados (pendência MAPA-ORG-001 §3). Cada linha da planilha aponta, na coluna de observação, o template/ferramenta de origem que deverá gerar a evidência (ex.: Ficha → TPL-GPR-002; Plano → TPL-GPR-001; Design → TPL-PCP-001; Rastreabilidade → TPL-REQ-002; Revisão por pares → TPL-VV-002/PR; Auditoria de config. → PLA-GCO-001 §7).

Itens marcados **REQUERIDO** no checklist que precisam de atenção especial por projeto:
- Evidência de revisão por pares (PR review) — junto com testes (VV)
- Relatório de auditoria de configuração (GCO projeto)

---

## 5. O que ainda falta do MPS-SW (lista priorizada)

**Bloqueador (destrava o resto):**
1. **Selecionar os 4 projetos da amostra** + 1 reserva. Sem isso, todo o Bloco 2 fica parado.

**Camada de evidência por projeto (depois da seleção):** preencher os templates já prontos em cada projeto — Ficha, Plano, Requisitos, Design, Integração, V&V, Configuração, Aceite, Indicadores, Decision log, GQA.

**Itens corporativos a produzir:**
2. Camada de **consolidação de indicadores** (dashboard) — também destrava OSW 6 e GPC 9.
3. **Registros de GQA** (auditoria de aderência) — sustenta os atributos de capacidade CP (iv/v/vi).
4. **Organograma**, **matriz RACI** consolidada, **matriz de competências** formal.
5. Registros de **treinamento realizado/onboarding** e **avaliação de efetividade**.
6. **Decision log organizacional** populado e **registros de melhoria/retrospectivas**.
7. **Matriz de evidências com links** (data room) + explicação do Jira importado.
8. Artefatos enxutos: política de **arquivamento/retenção** e **checklist de auditoria de config.**

**Decisões a confirmar com a ASR:**
9. **Aplicabilidade do AQU** (candidato a NA — nenhum dos 4 projetos tem aquisição).

---

## 6. Saída

A planilha `Checklist_MPS_SW_NivelC_Timeware_preenchido.xlsx` foi preenchida com:
- **Bloco 1:** status na coluna *Unidade Avaliada* (verde/amarelo/vermelho/cinza).
- **Bloco 2:** status FALTA nas 5 colunas de projeto.
- **Coluna I (nova):** *Observação / Diagnóstico* apontando o artefato de origem no git ou a ausência, por item.

---

## Histórico de revisões
| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Criação do diagnóstico a partir da comparação checklist × repositório. |
