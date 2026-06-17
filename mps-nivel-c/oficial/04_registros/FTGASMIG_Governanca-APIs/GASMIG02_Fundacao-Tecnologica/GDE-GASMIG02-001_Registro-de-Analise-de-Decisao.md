# Registro de Análise de Decisão — Isolamento de Clientes no Azure APIM

| Campo | Valor |
|---|---|
| **Documento** | GDE-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — Governança de APIs |
| **Versão** | 1.1 |
| **Data** | 11/06/2026 |
| **Responsável pela decisão** | Cézar Hiraki (Tech Lead / Arquiteto) / Abraão Oliveira (GP/PO) |
| **Processo de referência** | PRO-GDE-001 v1.2 |

---

## 1. Problema / decisão a tomar

A GASMIG precisa servir dois clientes industriais distintos (ArcelorMittal e Usiminas) a partir de uma única instância do Azure API Management, com isolamento completo de APIs, políticas e assinaturas por cliente. É necessário definir a **estratégia de isolamento** que será adotada como padrão na fundação — uma decisão arquitetural que impacta toda a estrutura da plataforma e é praticamente irreversível após a configuração.

## 2. Gatilho

Decisão de arquitetura/técnica relevante e irreversível: a estrutura escolhida determina como novos clientes serão integrados no futuro e não pode ser alterada sem reconfiguração completa da instância APIM.

## 3. Alternativas consideradas

| # | Alternativa | Descrição |
|---|---|---|
| A | Produtos/Assinaturas por cliente | Criar produtos APIM separados por cliente (`prod-arcelormittal`, `prod-usiminas`) com assinaturas individuais. Políticas de isolamento implementadas por produto, sem separação de plano de administração. |
| B | Workspaces APIM dedicados por cliente | Criar um workspace APIM por cliente (`ws-arcelormittal`, `ws-usiminas`), cada um com seu próprio plano de administração, APIs, políticas e assinaturas completamente isolados da instância principal. |

## 4. Critérios de avaliação

| Critério | Peso |
|---|---|
| Isolamento e segurança (dados e políticas de um cliente não acessíveis ao outro) | Alto |
| Escalabilidade (facilidade de adicionar novos clientes no futuro) | Alto |
| Delegação de administração (possibilidade de dar acesso administrativo limitado por cliente) | Médio |
| Complexidade de configuração inicial | Baixo |

## 5. Avaliação (matriz de decisão)

| Critério | Peso | Alt. A — Produtos/Assinaturas | Alt. B — Workspaces dedicados |
|---|---|---|---|
| Isolamento e segurança | Alto | Parcial — dados isolados, mas plano de administração compartilhado; risco de cross-contamination em políticas globais | Total — cada workspace é um domínio isolado de administração e dados; políticas de um workspace não afetam o outro |
| Escalabilidade | Alto | Baixa — novos clientes aumentam a complexidade do plano de produtos compartilhado; difícil de governar com muitos clientes | Alta — cada novo cliente = novo workspace independente; padrão replicável sem reconfiguração da base |
| Delegação de administração | Médio | Não suportado nativamente — acesso administrativo é all-or-nothing na instância | Suportado — cada workspace pode ter seus próprios administradores, sem acesso aos demais |
| Complexidade de configuração inicial | Baixo | Menor — configuração mais simples, familiar para equipes com experiência em APIM básico | Maior — requer provisionamento de workspace e configuração de permissões por workspace |
| **Avaliação geral** | | Adequada para casos simples; insuficiente para fundação corporativa multi-cliente de longo prazo | Solução de referência para governança corporativa multi-tenant no Azure APIM |

## 6. Decisão e justificativa

**Decisão: Alternativa B — Workspaces APIM dedicados por cliente.**

A fundação GASMIG é explicitamente projetada para ser reutilizável em projetos futuros de API. Com dois clientes na primeira OS e expansão prevista, o modelo de workspaces é o único que oferece isolamento completo (dados + administração) sem reconfiguração da base a cada novo cliente. A complexidade adicional na configuração inicial é compensada pela simplicidade operacional ao longo do tempo. O modelo de Produtos/Assinaturas adequaria-se a um cenário de cliente único ou com necessidade de isolamento apenas lógico, o que não é o caso da GASMIG.

## 7. Riscos associados à decisão

| Risco | Resposta |
|---|---|
| A funcionalidade de Workspaces pode exigir tier Premium ou determinada versão do APIM, não disponível no tenant GASMIG | Verificar o tier atual da instância APIM GASMIG antes da configuração; escalar para Sérgio Villaça se necessário (risco R-02 do PLA-GASMIG02-001) |
| Equipe de execução sem experiência prévia com Workspaces APIM (recurso mais recente) | Cézar Hiraki conduz o provisionamento inicial e revisão; documentação Microsoft como referência; reservar tempo de validação antes do deploy final |

## 8. Premissas (para revisão futura)

- O tenant GASMIG possui instância APIM em tier compatível com Workspaces (Standard v2 ou Premium).
- O modelo de dois clientes industriais (ArcelorMittal e Usiminas) permanece; se o modelo de negócio mudar para acesso totalmente compartilhado sem isolamento, a decisão deve ser reavaliada.
- Não há restrições regulatórias ou contratuais que impeçam o uso de uma instância APIM compartilhada com isolamento por workspace.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 14/04/2026 | Cézar Hiraki / Abraão Oliveira | Registro inicial da decisão de arquitetura de isolamento de clientes |
| 1.1 | 11/06/2026 | Time de Melhoria Contínua | Adicionada referência ao processo de decisão de referência (PRO-GDE-001 v1.2) |
