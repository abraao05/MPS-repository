# Avaliação de Capacitação — Trilha GCO / ITP (DevOps / GCO Baseline)

| Campo | Valor |
|---|---|
| **Documento** | AVA-CAP-004 — Avaliação Trilha GCO / ITP |
| **Versão** | 1.1 |
| **Data** | 22/09/2025 |
| **Aplicação** | DevOps, GCO Baseline/Auditoria |
| **Pré-requisito** | AVA-CAP-001 aprovado |
| **Referência** | PLA-CAP-001 §4; MAT-CAP-019, MAT-CAP-021; GUIA-CAP-005, GUIA-CAP-006 |

---

## Instruções

Responda com suas próprias palavras. Questões marcadas com **(DevOps)** são obrigatórias para DevOps; questões **(GCO)** são obrigatórias para o papel GCO Baseline/Auditoria. As demais são comuns. Pontuação de corte: **70%**.

---

## Bloco 1 — GCO (Gerência de Configuração)

**1.** O que é um item de configuração? Cite três exemplos de itens de configuração em um projeto Timeware.

> _Resposta esperada: Item de configuração é qualquer artefato ou componente sujeito a controle e versionamento formal. Exemplos: código-fonte, documentos de requisitos, planos de projeto, scripts de banco de dados, arquivos de configuração de ambiente._

**2.** Qual é a diferença entre o papel do DevOps e o papel do GCO Baseline no processo GCO?

> _Resposta esperada: O DevOps opera a configuração (cria tags, baselines, releases no pipeline). O GCO Baseline define os níveis de controle e audita se a operação está em conformidade com o plano. Um executa; o outro governa._

**3.** O que é controle de mudanças e por que é necessário no GCO?

> _Resposta esperada: O controle de mudanças garante que qualquer alteração em um item de configuração já baselineado seja formalizada (Change Request), aprovada e registrada antes de ser implementada. Sem controle, não é possível garantir a integridade das baselines._

**4.** Onde ficam registradas as baselines e os releases na Timeware?

> _Resposta esperada: No Git (tags de versão) e no Azure DevOps (pipelines, releases). A convenção de nomenclatura segue CONV-ORG-001._

---

## Bloco 2 — ITP (Integração do Produto)

**5. (DevOps)** Quais são os ambientes de integração utilizados pela Timeware? Descreva o fluxo de promoção.

> _Resposta esperada: Dev → QA → Homologação → Stage (réplica de produção para o cliente) → Produção. A promoção ocorre após validação em cada etapa: o cliente aprova na homologação antes de ir para produção._

**6. (DevOps)** O DevOps contribui com qual indicador de qualidade do PLA-MED-001? Como?

> _Resposta esperada: Defeitos homologação × produção. O DevOps opera a promoção entre ambientes, portanto registra (ou viabiliza o registro) dos defeitos encontrados em cada ambiente. Esse dado informa se os defeitos estão sendo capturados antes de chegarem à produção._

**7. (DevOps)** O que é o TPL-ITP-001 e qual é a participação do DevOps na sua produção?

> _Resposta esperada: É o template de Estratégia/Plano de Integração. O DevOps contribui com a definição dos ambientes, do pipeline de CI/CD e do caminho de promoção. A condução é do Tech Lead, mas o DevOps co-produz a parte de infraestrutura e pipeline._

---

## Bloco 3 — Auditoria de Configuração (GCO Baseline)

**8. (GCO)** O que verifica uma auditoria de configuração? Cite dois itens verificados.

> _Resposta esperada: A auditoria verifica a integridade das baselines (o que está no repositório bate com o que deveria estar) e se os registros de itens e modificações estão completos e corretos. Exemplos: todas as tags de release existem; os Change Requests foram registrados para todas as mudanças._

**9. (GCO)** Como a auditoria de configuração pode ser conduzida via GQA?

> _Resposta esperada: O GQA (auditoria de processo e produto) pode incluir a auditoria de configuração como um dos itens verificados — confirmando se os procedimentos de GCO estão sendo seguidos e se os registros de configuração estão em ordem. GCO 5 pode ser atendido dentro de uma auditoria GQA mais ampla._

**10. (GCO)** Onde fica o registro de uma auditoria de configuração?

> _Resposta esperada: No Confluence (PLA-GCO-001 §7 — Registro de Auditoria de Configuração)._

---

## Bloco 4 — Configuração no dia a dia (todos os papéis técnicos)

**11.** O que é a CONV-ORG-001 e quando ela é consultada?

> _Resposta esperada: É a convenção de nomenclatura e versionamento da Timeware. Define como nomear documentos, artefatos, branches, tags e releases. É consultada toda vez que um novo artefato é criado ou versionado._

**12.** Um desenvolvedor precisa criar uma nova branch para implementar uma funcionalidade. Como deve nomeá-la segundo a convenção da Timeware?

> _Resposta esperada: Conforme CONV-ORG-001 — padrão: feature/TICKET-descricao-curta (ex.: feature/GASFT-12-autenticacao-jwt). Sem acentos, sem espaços._

---

## Gabarito e Pontuação

| Questão | Papel | Pontos |
|---|---|---|
| 1 | Todos | 8 |
| 2 | Todos | 10 |
| 3 | Todos | 8 |
| 4 | Todos | 8 |
| 5 | DevOps (obrigatória) | 10 |
| 6 | DevOps (obrigatória) | 8 |
| 7 | DevOps (obrigatória) | 8 |
| 8 | GCO (obrigatória) | 10 |
| 9 | GCO (obrigatória) | 8 |
| 10 | GCO (obrigatória) | 8 |
| 11 | Todos | 8 |
| 12 | Todos | 6 |

A pontuação é normalizada para 100 com base nas questões aplicáveis ao papel. Corte de aprovação: **70 pontos**.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/03/2025 | Time de Melhoria Contínua | Versão inicial |
| 1.1 | 22/09/2025 | Time de Melhoria Contínua | Revisão após resultados da segunda turma: maior detalhamento nas questões de auditoria |
