# Registro de Adaptação do Processo — Milhas3

| Campo | Valor |
|---|---|
| **Documento** | ADAP-MILHASFACIL01-001 — Registro de Adaptação |
| **Versão** | 1.0 |
| **Data** | 16/05/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR — Gerência de Projeto |

---

## 1. Objetivo

Registrar as adaptações ao Processo Padrão Organizacional (PRO-GPC-001) aplicadas a este projeto, em conformidade com o Guia de Adaptação do Processo Padrão (GUIA-GPC-001).

## 2. Caracterização do projeto

| Atributo | Valor |
|---|---|
| Tipo de projeto | Desenvolvimento de produto web novo (greenfield) |
| Porte | Médio (~650 SP, 13 sprints, equipe de 7 pessoas) |
| Complexidade técnica | Alta — motor de rastreamento com bypass de proteção anti-bot Akamai via Selenium |
| Metodologia | Scrum — sprints de 2 semanas |
| Tipo de entrega | Incremental (entregas parciais por sprint com Sprint Reviews com cliente) |

## 3. Adaptações aplicadas

| ID | Elemento do processo | Decisão | Justificativa |
|---|---|---|---|
| AD-01 | Design UX/UI | Aplicável | Produto web com interface para usuário final; protótipos Angular validados pelo cliente a cada sprint antes do desenvolvimento do respectivo módulo |
| AD-02 | Estratégia de integração (ITP) | Aplicável com ajuste | Integrações realizadas por scraping automatizado (Selenium WebDriver), não por APIs REST convencionais; ITP-MILHASFACIL01-001 documenta a estratégia específica por programa de fidelidade e abordagem de bypass Akamai |
| AD-03 | Nível de documentação | Padrão | Projeto de médio porte com escopo bem delimitado; documentação completa de todos os processos MPS-SW se justifica pelo contexto de auditoria |
| AD-04 | Combinação de papéis | GP acumula PO; UX acumula Analista de Negócio | Equipe enxuta; Abraão Oliveira (GP + PO) e Igor Santana (UX + Analista de Negócio); papéis complementares sem conflito de interesse |
| AD-05 | Cadência de entrega | Incremental com Sprint Reviews quinzenais | Natureza SaaS do produto permite e exige feedback contínuo do cliente; Sprint Reviews com Felipe (Hub de Milhas) a cada sprint |
| AD-06 | Ambiente de staging | Único ambiente de homologação em VM Linux | Sem Kubernetes ou múltiplos ambientes cloud; homologação isolada por branch Git e variáveis de ambiente na mesma VM |
| AD-07 | Termo de Encerramento parcial | Não aplicável | Projeto único sem divisão em pacotes ou OS-PARCELAS; há apenas um TAE ao final do projeto |

## 4. Elementos não adaptados (processo padrão aplicado na íntegra)

- Gestão de riscos (GPR 10) — tabela completa com probabilidade, impacto, exposição e resposta
- Controle de mudanças — via Change Request formal
- Rastreabilidade de requisitos (RASTR-MILHASFACIL01-001)
- Verificação e validação (VV-MILHASFACIL01-001)
- Medição (MED-MILHASFACIL01-001)
- Garantia da qualidade independente (GQA-MILHASFACIL01-001)
- Gerência de configuração (GCO-MILHASFACIL01-001)
- Gerência de decisões (GDE-MILHASFACIL01-001)

## 5. Aprovação

Adaptações revisadas e aprovadas pelo Gerente de Projeto (Abraão Oliveira) em 16/05/2025, conforme ATA-MILHASFACIL01-001.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/05/2025 | Time de Melhoria Contínua | Documento inicial |
