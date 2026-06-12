# Registro de Adaptação do Processo — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | ADAP-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Responsável pela adaptação** | Abraão Oliveira |

---

## 1. Decisões de adaptação

Adaptação do processo-padrão (PRO-GPC-001) a este projeto, conforme o GUIA-GPC-001.

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto (com/sem front-end) | Sem UX/UI — apenas back-end/worker e arquitetura | A solução é um agente de captura e serviços de retaguarda; não há interface de usuário |
| Origem dos requisitos e do design | Timeware elabora; AASP valida e homologa | Os requisitos derivam de problemas operacionais da captura; o cliente valida resultados e aceita as entregas |
| Porte do projeto | Médio → formalidade padrão | ~586 h estimadas, ~9 meses, dois projetos correlatos (id 213 EPROC e id 256 CNJ) |
| Equipe e papéis (acúmulo) | Dev Sênior acumulou execução de testes nas fases iniciais; GP acumulou responsável por GCO | Equipe enxuta; Analista de Testes dedicado a partir da Fase 5 |
| Estimativa e cadência | Estimativa e acompanhamento por horas e cards no ClickUp (não por story points/Scrum) | Modelo de gestão por atividades adotado para este projeto |
| Cadência de entrega ao cliente | Por marco/fase, com devolutivas ao cliente | Acordada com a AASP; resultados comunicados por fase |
| Ambiente de stage | Não adotado — homologação por amostragem | Não havia ambiente de Elasticsearch dedicado para testes; validação por repetição do mesmo processo na fila sem impacto no índice de produção |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | Não | Projeto sem front-end |
| Mapa de teste por história (story) | Não | Projeto não usa histórias/SP; testes organizados por fluxo e fase (ver VV-AASPCNJ01-001) |
| Documento de Design (arquitetura) | Sim | PCP-AASPCNJ01-001 |
| Estratégia de Integração | Sim | ITP-AASPCNJ01-001 |
| Plano e execução de V&V | Sim | VV-AASPCNJ01-001 e REL-VV-AASPCNJ01-001 |
| Gerência de Configuração | Sim | GCO-AASPCNJ01-001 (GitFlow + GMUD) |
| Registro de decisões (GDE) | Sim | GDE-AASPCNJ01-001 |
| Aquisição (AQU) | Não | Não há subcontratação de desenvolvimento; APIs/infra de terceiros são insumos de serviço, tratados em ITP/PCP e Riscos |

## 3. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados (REQ-AASPCNJ01-001)
- [ ] Plano de Projeto aprovado pelo cliente (baseline) — a registrar no encerramento (projeto em execução)
- [x] Definição de Pronto aplicada (critérios de aceite CA01–CA07, ver VV)
- [x] Verificação e validação realizadas (VV / REL-VV)
- [ ] Encerramento formal com aceite — Onda 3 (encerramento previsto 30/06/2026)

Os dois pontos em aberto referem-se a marcos de encerramento e serão registrados ao final do projeto (TAE-AASPCNJ01-001 e a ata de aceite), conforme o estágio atual.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de adaptação consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
