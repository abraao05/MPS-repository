# Plano de Projeto — [NOME DO PROJETO]

> **TEMPLATE (TPL-GPR-001).** Modelo a ser preenchido por projeto. Os campos entre colchetes `[ ]` devem ser substituídos pelas informações do projeto. As instruções em itálico orientam o preenchimento e podem ser removidas na versão final do projeto.

| Campo | Valor |
|---|---|
| **Documento** | [CÓDIGO DO PLANO — ex.: PLA-PROJ-XXX] |
| **Projeto** | [Nome do projeto] |
| **Cliente** | [Cliente] |
| **Versão** | [versão] |
| **Data** | [dd/mm/aaaa] |
| **Gerente de Projeto** | [responsável] |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

*[Descreva o objetivo do projeto, o problema que resolve e o resultado esperado para o cliente.]*

## 2. Escopo (GPR 1)

*[Descreva o escopo do projeto — o que está incluído e o que está fora. Referencie o Documento de Requisitos quando existir.]*

- **Incluído:** [...]
- **Não incluído:** [...]

## 3. Adaptação do processo (GPR 2)

*[Registre como o processo-padrão foi adaptado a este projeto, conforme o Guia de Adaptação (GUIA-GPC-001).]*

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Design UX/UI | [aplicável / não aplicável] | [ex.: projeto sem front-end] |
| Nível de documentação | [enxuto / padrão / reforçado] | [porte do projeto] |
| Combinação de papéis | [ex.: Tech Lead acumula Arquiteto] | [...] |

## 4. Estimativas (GPR 3, 4)

*[Registre as estimativas de tamanho (story points), a derivação de esforço/prazo e o orçamento de horas por papel. Indique a base histórica usada.]*

**Tamanho e prazo**

- **Tamanho estimado:** [pontos]
- **Velocity de referência:** [pontos/sprint]
- **Número de sprints estimado:** [nº]
- **Duração estimada:** [período — ex.: 4 meses / jul–out/2026]
- **Base histórica utilizada:** [projetos/velocity de referência]

**Orçamento de horas por papel**

*[Calcule as horas por papel usando a referência: 168 h/mês disponíveis por pessoa (21 dias × 8 h); deduzindo ~28 h de cerimônias ágeis e reuniões internas (~15%), a capacidade efetiva de projeto é de **140 h/mês por FTE** ou **70 h por sprint de 2 semanas por FTE**. Ajuste pela % de dedicação ao projeto.]*

| Papel | Pessoas | Dedicação | h efetivas/sprint | Nº sprints | **h estimadas** |
|---|---|---|---|---|---|
| Gerente de Projeto / PO | [n] | [ex.: 60%] | [ex.: 42 h] | [n] | [total] |
| Tech Lead / Arquiteto | [n] | [ex.: 80%] | [ex.: 56 h] | [n] | [total] |
| Desenvolvedor | [n] | [ex.: 100%] | [ex.: 70 h] | [n] | [total] |
| QA | [n] | [ex.: 80%] | [ex.: 56 h] | [n] | [total] |
| DevOps | [n] | [ex.: 40%] | [ex.: 28 h] | [n] | [total] |
| **Total** | | | | | **[soma]** |

> *Referência de cálculo:* h efetivas/sprint = 70 h × (% dedicação). Ex.: Dev 100% = 70 h/sprint; GP 60% = 42 h/sprint. Papéis não aplicáveis ao projeto devem ser removidos da tabela.

## 5. Cronograma, marcos e orçamento (GPR 5)

*[Liste os marcos do projeto e as sprints previstas. O orçamento total de horas é derivado da tabela acima.]*

**Marcos**

| Marco | Data prevista |
|---|---|
| [Kickoff gerencial (abertura)] | [data] |
| [Fim do Discovery / Requisitos] | [data] |
| [Fim da Concepção (design + estimativas)] | [data] |
| [Aprovação do Plano (baseline)] | [data] |
| [Entregas / releases] | [datas] |
| [Encerramento] | [data] |

**Orçamento total do projeto**

| Item | Valor |
|---|---|
| Horas totais estimadas | [soma da tabela §4] |
| Período (início–fim) | [data] a [data] |
| Sprints | [nº] sprints de 2 semanas |

## 6. Recursos (GPR 6, 7)

- **Equipe:** *[papéis e alocação; indicar recursos compartilhados conforme portfólio]*
- **Ambiente e ferramentas:** *[ambientes-padrão e específicos do projeto]*

## 7. Partes interessadas e comunicação (GPR 9)

*[Liste as partes interessadas e o plano de comunicação — o que, para quem, com que frequência.]*

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| [Cliente] | [...] | [reuniões, reviews] |

## 8. Transição (GPR 8)

*[Quando aplicável, descreva a estratégia de transição para operação/sustentação. Caso não se aplique, registre "não aplicável".]*

## 9. Riscos (GPR 10)

*[Registre os principais riscos identificados. O acompanhamento detalhado é feito no Jira conforme EST-GPC-002. Exposição = Probabilidade × Impacto; escala 1–3 em cada dimensão (resultado 1–9). Ver faixas de criticidade em EST-GPC-002 §4.]*

| Risco | Prob. (1–3) | Impacto (1–3) | Exposição (P×I) | Resposta |
|---|---|---|---|---|
| [risco] | [1–3] | [1–3] | [1–9] | [mitigar / evitar / aceitar / transferir] |

## 10. Viabilidade (GPR 11)

*[Registre a avaliação de viabilidade do projeto considerando escopo, estimativas, recursos e riscos.]*

## 11. Aprovação do Plano (GPR 13)

*[O plano é apresentado ao cliente na reunião de Apresentação e Aprovação do Plano. O aceite é registrado na ata dessa reunião (não há documento de assinatura separado). Registre abaixo a referência da reunião/ata e os envolvidos.]*

| Envolvido | Papel | Aceite | Data | Ref. da ata |
|---|---|---|---|---|
| [nome/papel] | [...] | [aprovado] | [data] | [link/ata] |

> A aprovação registrada aqui estabelece a **baseline** do projeto. A partir dela, mudanças de escopo seguem o fluxo de change request.

---

## Controle de atualizações do plano

*[O Plano de Projeto é vivo. Registre aqui as atualizações relevantes ao longo do projeto.]*

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| [v] | [data] | [autor] | [o que mudou] |

---

## Histórico de revisões do template

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/09/2025 | Time de Melhoria Contínua | Versão inicial do template de plano de projeto |
| 1.1 | 10/06/2026 | Time de Melhoria Contínua | Adição de tabela de orçamento de horas por papel em §4 (GPR 4) e seção de orçamento total em §5 (GPR 5), com referência de capacidade 168 h/mês → 70 h efetivas/sprint/FTE |
