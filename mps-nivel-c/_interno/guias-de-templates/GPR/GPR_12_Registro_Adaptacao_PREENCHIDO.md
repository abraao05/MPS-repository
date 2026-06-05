# Registro de Adaptação do Processo — Trainer Connect

> **Modelo de preenchimento** com base no projeto *Trainer Connect* — plataforma web para personal trainers gerenciarem alunos e prescreverem treinos. Dados sem equivalente direto no repositório (gestor, cliente formal) marcados com *(exemplo)*. O objetivo é mostrar como o registro fica preenchido para um projeto de porte médio com equipe enxuta.

---

## Identificação

| Campo | Valor |
|---|---|
| Documento | ADAP-TCON-001 |
| Projeto | Trainer Connect — plataforma de gestão para personal trainers |
| Versão | v1 |
| Data | 06/01/2025 |
| Responsável pela adaptação | *(exemplo: Gestor Timeware — Gerente de Projeto)* |

---

## 1. Decisões de adaptação

| Eixo | Decisão para este projeto | Justificativa |
|---|---|---|
| Tipo de produto | Produto web com front-end em React (SPA) e back-end gerenciado (banco com regras de acesso por linha) | Produto digital de uso contínuo, não um projeto de serviço pontual; a natureza web influencia os requisitos de ambiente de stage e a cadência de entrega |
| Origem dos requisitos | A Timeware elabora os requisitos em colaboração com o cliente/PO, baseada em pesquisa de problema e validação contínua com o usuário real (trainer) | O cliente define o problema e valida o resultado, mas a especificação técnica e a priorização detalhada são responsabilidade da equipe Timeware |
| Porte | Médio — aproximadamente 120 pontos de história, ~150 h de esforço estimado, duração de ~10 semanas, equipe de 2 a 3 pessoas *(exemplo)* | Acima do porte pequeno (projeto solo simples), abaixo do porte grande (equipe dedicada de 5+); requer plano documentado e acompanhamento formal, mas sem necessidade de estrutura de PMO |
| Equipe / papéis | Dev full-stack acumula o papel de arquiteto de software; GP acumula o papel de analista de negócio | Equipe enxuta justifica o acúmulo; decisões de arquitetura são documentadas nos registros de design (PCP); a acumulação de papéis é explícita e não implica ausência de governança |
| Criticidade / regulação | Produto sem regulação específica (não é sistema de saúde regulado, não processa dados financeiros diretos na v1.0) | Módulo de comércio (gateway de pagamento) está explicitamente fora do escopo desta versão; privacidade de dados (LGPD) deve ser considerada no design, mas não gera requisito regulatório formal no escopo atual |
| Cadência de entrega | Entrega por milestone (v1.0, v1.5, v1.8) — cada milestone é uma entrega funcional em produção com aceite do usuário | Cadência de milestone permite entregas de valor frequentes e validação real antes de avançar; evita o risco de entregar tudo no final |
| Ambiente de stage / homologação | Preview automático a cada alteração na branch de desenvolvimento (deploy automático via plataforma de hospedagem) | O preview automático cobre a necessidade de homologação para um produto deste porte; não é necessário ambiente dedicado de QA separado |

---

## 2. Etapas aplicáveis e não aplicáveis

| Etapa do processo-padrão | Aplicável? | Observação / justificativa |
|---|---|---|
| Levantamento de contexto e pesquisa | Sim | Aplicada em cada fase; registrada nos artefatos GSD (RESEARCH, CONTEXT) |
| Planejamento detalhado da fase | Sim | Aplicada a cada milestone antes do início; registrada no PLAN de cada fase |
| Execução e construção | Sim | Aplicada integralmente |
| Revisão técnica (verificação) | Sim | Revisão por pares via pull request com revisor humano antes do merge; suíte de testes automatizados |
| Validação com usuário / UAT | Sim | Aplicada ao fim de cada milestone com o trainer (usuário real) em produção |
| Aceite formal do cliente por milestone | Sim | Aceite registrado na ata de encerramento de cada milestone *(exemplo)* |
| Registro de lições aprendidas | Sim | Registrado na fase de retrospectiva de cada milestone (artefato RETROSPECTIVE) |
| Especificação de UI antes da execução | Sim (adaptação adicional) | Como o produto tem forte componente visual, cada fase inclui especificação de UI (UI-SPEC) antes da execução — adição ao processo-padrão, não redução |

---

## 3. Pontos de controle obrigatórios (checklist)

- [x] Termo de Abertura emitido antes do início do planejamento detalhado
- [x] Registro de Adaptação aprovado antes do Plano do Projeto
- [ ] Plano do Projeto com baseline estabelecida e aprovada *(a verificar no marco de aprovação do plano)*
- [ ] Relatório de Acompanhamento emitido a cada milestone (v1.0, v1.5, v1.8)
- [ ] Change Requests formalizados para toda mudança de escopo, prazo ou custo (ex.: módulo de comércio → CR-TCON-001)
- [ ] Revisão por pares realizada nos produtos de trabalho selecionados (via PR com revisor humano)
- [ ] Verificação GQA no marco de aprovação do Plano do Projeto
- [ ] Termo de Encerramento emitido com aceite formal do cliente ao final da v1.8
- [ ] Especificação de UI produzida antes da fase de execução em cada milestone com componente visual
