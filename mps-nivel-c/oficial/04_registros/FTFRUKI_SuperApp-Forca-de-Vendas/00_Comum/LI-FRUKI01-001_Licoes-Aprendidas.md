# Lições Aprendidas e Oportunidades de Melhoria — SuperApp Fruki · Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | LI-FRUKI01-001 — Lições Aprendidas e Oportunidades de Melhoria |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | SuperApp Fruki — Força de Vendas (Pacote 1 + Pacote Final 24) |
| **Aprovação** | Gerente de Projeto |

---

## 1. Objetivo

Consolidar as lições aprendidas ao longo dos dois pacotes do SuperApp Fruki (jun/2025–jan/2026) e identificar oportunidades de melhoria para projetos futuros de desenvolvimento mobile e integração com APIs de clientes.

---

## 2. O que funcionou bem

| # | Lição | Impacto |
|---|---|---|
| LE-01 | A cadência de entrega incremental por módulo (um módulo por sprint mensal) permitiu validação contínua com o cliente e identificação antecipada de ajustes de regras de negócio, sem acumular retrabalho no final | Alto — três módulos entregues e aceitos sem retorno de escopo |
| LE-02 | O processo de prototipagem e validação com Cecília Ribeiro antes de cada sprint de desenvolvimento eliminou ambiguidades de regras de negócio e evitou retrabalho de interface | Alto — todos os módulos aceitos sem revisão estrutural de UX |
| LE-03 | A decisão de normalizar dados e tratar problemas de API no front-end (em vez de solicitar correções ao time de TI da Fruki) foi acertada no contexto de um cliente com capacidade técnica limitada: permitiu continuar o desenvolvimento sem dependências externas | Médio — zero atraso por aguardar correção de API |
| LE-04 | A reunião de levantamento de demanda com Cecília (25/06/2025) estruturada antes do início do desenvolvimento foi suficiente para documentar todos os requisitos do Pacote 1; o mesmo modelo foi replicado no Pacote Final 24 | Alto — requisitos estáveis ao longo de todo o projeto |
| LE-05 | A revisão de código (PR) pelo Jardel Dargas Silva antes do merge no repositório Fruki funcionou como gate de qualidade técnica e garantia de compatibilidade com o codebase existente; nenhum problema pós-merge identificado em produção | Alto — zero defeitos em produção |
| LE-06 | O piloto com vendedores selecionados (05/08/2025 no Pacote 1) revelou problemas reais de dados (duplicação de famílias, cálculos inconsistentes) que não foram identificados com mocks; a antecipação do piloto permitiu correção antes do aceite formal | Médio — defeitos corrigidos antes do aceite |

---

## 3. O que pode melhorar

| # | Lição | Causa-raiz | Impacto |
|---|---|---|---|
| LE-07 | A API de Rota PDV foi disponibilizada por Jardel apenas em 08/01/2026 (Sprint 3), cerca de 3 semanas após o previsto; a dependência foi gerenciada sem impacto no prazo final, mas gerou pressão na equipe | Ausência de cláusula formal de comprometimento de data de API no plano de projeto | Baixo (absorvido) |
| LE-08 | A lista de perguntas do formulário de PDV foi recebida de Alexsandro apenas em 04/12/2025, no início da Sprint 3; o desenvolvimento da tela dependia dessa lista | Pré-requisito de conteúdo (perguntas do formulário) não foi incluído formalmente no plano de projeto como bloqueador da sprint | Baixo (absorvido com antecipação parcial da tela) |
| LE-09 | A duplicação de famílias na API de Metas e o cálculo inconsistente de positivação foram identificados apenas no piloto com vendedores reais (05/08/2025), não durante o desenvolvimento | Ausência de cenários de teste com dados reais de API antes do piloto; uso exclusivo de mocks no desenvolvimento | Médio — exigiu sprint adicional de ajustes |
| LE-10 | O onboarding no codebase existente do SuperApp Fruki (assumindo de fornecedor anterior) levou mais tempo que o estimado; a documentação técnica do projeto anterior não estava disponível | Em projetos de substituição de fornecedor, não há checklist para solicitação de documentação técnica do projeto existente | Baixo (absorvido no prazo de início) |

---

## 4. Oportunidades de melhoria para processos organizacionais

| # | Oportunidade | Área afetada | Prioridade |
|---|---|---|---|
| OM-01 | Incluir no template de Plano de Projeto uma seção explícita de "Pré-requisitos do cliente" com responsável e data de comprometimento (APIs, credenciais, conteúdo de formulários, acesso a repositórios) | Planejamento de projetos | Alta |
| OM-02 | Incluir no checklist de início de sprint de desenvolvimento um item de validação de dados reais da API (ou mock que simule casos extremos como duplicados, valores nulos, formato não padronizado) antes de avançar para desenvolvimento de interface | V&V / processo de desenvolvimento | Alta |
| OM-03 | Criar checklist de onboarding para projetos de substituição de fornecedor: lista de documentação técnica, acesso a repositórios, credenciais de APIs e histórico do projeto a solicitar ao cliente antes do kickoff | Planejamento de projetos | Média |
| OM-04 | Incluir na reunião de levantamento de requisitos para módulos com formulários (ex.: PDV) uma seção explícita de confirmação da lista completa de campos/perguntas, com documento de aceite assinado pelo responsável do cliente | Levantamento de requisitos | Média |
| OM-05 | Para projetos mobile com integração a APIs de clientes, incluir no plano de risco padrão o risco "API não disponibilizada no prazo" com resposta pré-definida (mock + desenvolvimento paralelo + escalonamento via gestor do contrato) | Gestão de riscos | Baixa |

---

## 5. Aplicação em projetos futuros

As lições LE-07 e OM-01 foram identificadas durante o Pacote Final 24 e devem ser incorporadas imediatamente ao template PLA-GPR nas próximas revisões. O modelo de validação de protótipos antes de cada sprint (LE-02) e de entrega incremental mensal (LE-01) devem ser mantidos como práticas padrão em projetos mobile de múltiplos módulos.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/01/2026 | Gerente de Projeto | Lições aprendidas dos dois pacotes do SuperApp Fruki; oportunidades de melhoria identificadas |
