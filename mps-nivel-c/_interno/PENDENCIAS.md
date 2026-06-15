# Pendências em Aberto — Implantação MPS-SW Nível C

> **Nota:** este é um documento de apoio interno (não é evidência MPS, não auditável pela ASR).
> Lista de pontos a retomar, registrados ao longo da produção dos artefatos.

---

## Pendências ativas

| # | Data registro | Pendência | Contexto / origem | Status |
|---|---|---|---|---|
| 1 | 2026-06-03 | **Alinhar POL-ORG-001 à camada COO** | O COO (Operações) foi introduzido em vários documentos de governança (PRO-OSW-001, PRO-GPC-002, EST-GPC-001, EST-GPC-002, PLA-GPC-001), estabelecendo a estrutura CEO estratégico / COO operacional. A POL-ORG-001 (Política Organizacional de Processos), porém, ainda cita apenas "Founder e CEO" na seção de responsabilidades. Verificar se a Política deve ser revisada (provável v1.1) para refletir essa camada e manter consistência com os demais ativos. | ✅ Resolvido (2026-06-15) — POL-ORG-001 atualizado para v1.1 com adição do papel COO (Operações) na seção 5 (Responsabilidades), cobrindo atribuições operacionais, coordenação de portfólio, GQA e aprovação de adaptações de processo. Consistência com PRO-GPC-002, PRO-OSW-001, EST-GPC-001, EST-GPC-002 e PLA-GPC-001 restaurada. |
| 2 | 2026-06-03 | **GPR não está no repositório** | O MAPA-ORG-001 v0.18 lista `PRO-GPR-001` (Processo de Gerência de Projetos) e `TPL-GPR-001` (Template de Plano de Projeto) como produzidos/aprovados e marca GPR 1-20 como ✅, mas esses dois arquivos **não foram enviados** e **não existem em `oficial/02_projeto/` nem `oficial/03_templates/`**. O lote que pulou de v0.16 → v0.18 sugere um conjunto intermediário (GPR) não recebido. Reenviar PRO-GPR-001 e TPL-GPR-001 para fechar a lacuna. | ✅ Resolvido (2026-06-03) — PRO-GPR-001 e TPL-GPR-001 recebidos e adicionados ao repositório no lote v0.19. |

---

## Pendências herdadas do MAPA-ORG-001 (ações abertas de escopo)

Estas já constam na seção 3 do MAPA-ORG-001, replicadas aqui para acompanhamento:

- Confirmar **não-aplicabilidade do AQU** (Aquisição) com o avaliador líder da ASR.
- Definir os **4 projetos** da avaliação antes da Fase 3.
- **MED:** definir camada de consolidação de indicadores (dashboard Jira ou planilha organizacional). Bloqueia o fechamento de OSW 6 (🟨) e GPC 9 (⬜).
