# Processo de Verificação e Validação — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-VV-001 — Processo de Verificação e Validação |
| **Versão** | 1.1 |
| **Data** | `<dd/mm/aaaa>` |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Processos MPS-SW relacionados** | VV 1 a VV 5 |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware verifica e valida seus produtos de software, assegurando que sejam construídos corretamente (verificação) e que atendam às necessidades do cliente (validação), por meio de testes e revisão por pares.

> **Mapa de resultados atendidos neste documento:**
> - Seção 3 → **VV 1** (produtos a verificar/validar e métodos)
> - Seção 4 → **VV 2** (revisão por pares)
> - Seção 5 → **VV 3** (métodos, critérios e ambientes)
> - Seção 6 → **VV 4** (atividades realizadas e problemas tratados)
> - Seção 7 → **VV 5** (resultados analisados e comunicados)

## 2. Conceitos

- **Verificação:** o produto está sendo construído **corretamente**, conforme requisitos e padrões (testes, revisão por pares).
- **Validação:** o produto **atende à necessidade real** do cliente (validação de requisitos, homologação com o cliente).

## 3. Seleção e planejamento (VV 1)

- Para cada projeto, define-se **o que** será verificado e validado e por **quais métodos**, registrado no **Plano de V&V** (TPL-VV-001).
- Os métodos combinam, no mínimo: **testes** (executados por QA e desenvolvimento) e **revisão por pares** (code review).

## 4. Revisão por pares (VV 2)

- O código passa por **revisão por pares (code review)** antes do merge, via Pull Request (Git/Azure DevOps), conforme a Definição de Pronto e a Gerência de Configuração (PLA-GCO-001).
- A revisão verifica aderência aos padrões, aos requisitos e à qualidade técnica; os apontamentos são tratados antes da aprovação.
- O registro da revisão é o próprio Pull Request (revisores, comentários, aprovação) e/ou o template TPL-VV-002.

## 5. Métodos, critérios e ambientes (VV 3)

- **Desenvolvimento:** o desenvolvedor testa o que produziu conforme os **critérios de aceite** definidos.
- **QA:** aplica metodologias de teste sobre o produto (teste exploratório guiado pelos requisitos, testes funcionais, de integração e outros aplicáveis), documentando os cenários com evidências e formalizando-os em **Gherkin** (`Dado/Quando/Então`) para reúso e eventual automação.
- **Ferramentas e ambientes:** os casos e resultados de teste são mantidos em **Azure Test Plans** e/ou **Jira/Xray**. Os casos podem iniciar em planilha e ser importados para a ferramenta — fluxo aceito e documentado.
- A homologação ocorre em ambiente de **homologação/staging**.

## 6. Execução e tratamento de problemas (VV 4)

As atividades de verificação e validação são **executadas** conforme o plano. O fluxo de teste conduzido pelo QA é:

1. **Recebimento da demanda:** o QA recebe a task já disponibilizada no ambiente de **homologação**, com os critérios de aceite e o escopo definidos.
2. **Teste exploratório guiado pelos requisitos:** o QA testa a funcionalidade de forma exploratória, orientado pelos requisitos e critérios de aceite.
3. **Documentação dos cenários e evidências:** os cenários testados são documentados, com as respectivas **evidências** (capturas de tela, vídeos, logs).
4. **Aprovação:** atendidos os critérios, a task é aprovada.
5. **Formalização em Gherkin:** os cenários são formalizados em **Gherkin** (`Dado / Quando / Então`), contemplando o caminho de sucesso (*happy path*) e os de exceção (*sad path*). Esses cenários ficam prontos para as **rodadas futuras de teste (regressão)** e para **automação**, quando a equipe decidir automatizá-los.

Os **defeitos** identificados são registrados (Jira/Xray), priorizados e **tratados** até a resolução. A validação final com o cliente ocorre na **homologação**, antes da promoção para produção.

> A automação de testes não é obrigatória em todos os projetos: os cenários Gherkin mantêm o conhecimento de teste documentado e reaproveitável, e a automação é adotada quando a equipe avalia que compensa.

## 7. Análise e comunicação dos resultados (VV 5)

- Os resultados de V&V são **analisados** (cobertura, defeitos encontrados, defeitos que escaparam para produção) e **registrados**.
- São **comunicados** aos envolvidos e alimentam os indicadores de qualidade da Medição (PLA-MED-001): densidade de defeitos, defeitos homologação × produção, retrabalho.

## 8. Papéis

| Papel | Responsabilidade |
|---|---|
| **Desenvolvedor** | Testa o que produz conforme critérios de aceite; participa do code review. |
| **QA** | Planeja e aplica metodologias de teste; registra casos e resultados. |
| **Tech Lead** | Conduz/garante a revisão por pares. |
| **Product Owner / Cliente** | Valida o produto na homologação. |

## 9. Documentos e artefatos relacionados

- PRO-GPC-001 — Processo-Padrão Organizacional
- TPL-VV-001 — Template de Plano de Verificação e Validação
- TPL-VV-002 — Template de Registro de Revisão por Pares
- PLA-GCO-001 — Plano de Gerência de Configuração
- PLA-MED-001 — Plano de Medição
- PRO-REQ-001 — Processo de Engenharia de Requisitos

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Definição inicial do processo de verificação e validação |
| 1.1 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Detalhamento do fluxo do QA (teste exploratório, evidências, cenários Gherkin) |
