# Registro de Verificação de GQA — [NOME DO PROJETO]

> **TEMPLATE (TPL-GPC-001).** Preencher um registro por verificação realizada. Cada verificação corresponde a um marco do processo-padrão ou a uma amostragem, conforme EST-GPC-001 §4. O auditor de GQA deve ser independente da equipe verificada (EST-GPC-001 §3). Arquivar na seção "Registros de GQA" do projeto no Confluence.

| Campo | Valor |
|---|---|
| **Projeto** | [Nome do projeto] |
| **Marco / tipo de verificação** | [Abertura · Discovery/Requisitos · Concepção · Aprovação do Plano · Desenvolvimento — sprint N · Homologação/Entrega · Encerramento · Amostragem] |
| **Data** | [dd/mm/aaaa] |
| **Auditor (GQA)** | [Nome/papel] |
| **Gerente de Projeto** | [Nome/papel] |

---

## 1. Escopo da verificação

*[Descrever o que foi verificado: quais produtos de trabalho foram examinados e quais atividades do processo foram observadas.]*

## 2. Verificação de aderência ao processo

*Marcar cada item: ✅ Conforme | ⚠ Desvio | N/A Não se aplica. Para cada ⚠, registrar o achado na seção 4.*

| # | Item verificado | Resultado | Referência ao processo |
|---|---|---|---|
| 1 | [...] | [...] | [...] |
| 2 | [...] | [...] | [...] |
| 3 | [...] | [...] | [...] |
| 4 | [...] | [...] | [...] |
| 5 | [...] | [...] | [...] |
| GCO-1 | Itens de configuração identificados e controlados em repositório com convenção de versão adotada | [...] | PRO-GCO-001 §2; PLA-GCO-001 |
| GCO-2 | Baseline estabelecida no marco verificado (ou equivalente documentado) | [...] | PRO-GCO-001 §3; GCO-[PROJ]-001 |
| GCO-3 | Auditoria de configuração realizada: ICs confirmados íntegros e consistentes com os documentos de projeto | [...] | PRO-GCO-001 §4 |

## 3. Verificação de produtos de trabalho

*Verificar existência, completude e conformidade com o padrão (template correto, versionamento, campos obrigatórios preenchidos).*

| # | Produto de trabalho | Existe? | Completo? | Segue padrão? | Observação |
|---|---|---|---|---|---|
| 1 | [...] | [...] | [...] | [...] | [...] |
| 2 | [...] | [...] | [...] | [...] | [...] |
| 3 | [...] | [...] | [...] | [...] | [...] |
| 4 | [...] | [...] | [...] | [...] | [...] |

## 4. Achados

*Registrar cada desvio das seções 2 e 3. Se nenhum, registrar "Nenhum desvio identificado".*

| # | Desvio | Severidade | Recomendação | Responsável | Prazo | Status |
|---|---|---|---|---|---|---|
| 1 | [...] | [Alta · Média · Baixa] | [...] | [...] | [dd/mm/aaaa] | [Aberto · Em andamento · Resolvido] |

## 5. Resultado

| Campo | Valor |
|---|---|
| **Resultado geral** | [Conforme · Conforme com ressalvas · Não conforme] |
| **% de conformidade** | [itens conformes ÷ itens aplicáveis × 100] |
| **Achados abertos** | [N] |
| **Oportunidades de melhoria identificadas** | [...] *(ou "Nenhuma")* |

---

## Histórico de revisões do template

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 12/08/2025 | Time de Melhoria Contínua | Versão inicial do template |
| 1.1 | 11/06/2026 | Time de Melhoria Contínua | Adição de itens GCO-1 a GCO-3 na seção 2 (verificação de aderência à gerência de configuração — GCO 5) |
