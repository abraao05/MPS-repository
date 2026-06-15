# Registro de Aquisição — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | AQU-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsável** | Cezar Hiraki Velazquez (Gerente de Projeto / Tech Lead) |
| **Processo MPS-SW** | AQU (evidência de projeto) |

---

## 1. Natureza das aquisições

O projeto não subcontratou desenvolvimento de software. As "aquisições" deste projeto correspondem a **serviços de terceiros (APIs externas e serviço de nuvem)** e a **componentes de software de prateleira (pacotes NuGet)** incorporados à solução. Este registro documenta a identificação dessas dependências e os critérios objetivos para sua adoção.

## 2. Serviços e dependências de terceiros

| Fornecedor / Dependência | Tipo | Papel no projeto |
|---|---|---|
| API Sensr | API REST externa | Fonte de dados da migração — fornece autenticação, atividades, detalhes e sub-atividades |
| API Jira v3 (Atlassian) | API REST externa | Destino da migração — recebe criação de Epics, Tasks, Subtasks, transições e comentários |
| Azure Scheduler | Serviço de nuvem | Agendamento e execução periódica do serviço |
| HtmlAgilityPack | Pacote NuGet | Parsing de HTML dos campos do Sensr |
| Newtonsoft.Json | Pacote NuGet | Serialização e desserialização JSON |
| Microsoft.Extensions.* | Framework .NET | Injeção de dependências, configuração e logging |
| Azure DevOps | Controle de versão / CI-CD | Repositório e pipeline de publicação |

## 3. Critérios de adoção de dependências

Dependências selecionadas com base em três critérios objetivos: **maturidade do pacote**, **compatibilidade com .NET 8** e **necessidade técnica objetiva**.

| Dependência | Justificativa da escolha |
|---|---|
| HtmlAgilityPack | Referência para parsing de HTML em .NET; maturidade e compatibilidade com .NET 8 |
| Newtonsoft.Json | Preferido ao `System.Text.Json` pela flexibilidade no mapeamento de propriedades com nomes diferentes entre o JSON das APIs e os modelos C# |
| Microsoft.Extensions.* | Parte do ecossistema .NET 8 (DI, configuração e logging) |

## 4. Gestão e riscos das dependências

- As APIs do Sensr e do Jira são premissas de disponibilidade do projeto (ver REQ-AASP-GOV-001). O risco de comportamento inconsistente da API Jira para transições de status (R-04) foi tratado com consulta prévia das transições disponíveis (ver PLA-AASP-GOV-001 §9).
- Não há contrato de subcontratação de desenvolvimento a gerir; não se aplicam critérios de seleção de fornecedor de mão de obra.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de aquisição consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
