# Estratégia de Gerência de Riscos e Oportunidades — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | EST-GPC-002 — Estratégia de Gerência de Riscos e Oportunidades |
| **Versão** | 1.1 |
| **Data** | 25/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Processo MPS-SW relacionado** | GPC 7 (estratégia de gerência de riscos) |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Esta estratégia define como a Timeware identifica, analisa, trata e monitora riscos e oportunidades, tanto no âmbito dos projetos quanto no âmbito organizacional. O objetivo é antecipar ameaças e oportunidades, permitindo decisões informadas que protejam os compromissos da organização e dos seus projetos.

Esta estratégia organizacional é a base para o tratamento de riscos nos projetos, conduzido conforme o processo de Gerência de Projetos (GPR).

## 2. Conceitos

- **Risco:** evento incerto que, se ocorrer, tem efeito negativo sobre objetivos (prazo, custo, qualidade, escopo).
- **Oportunidade:** evento incerto que, se ocorrer, tem efeito positivo sobre objetivos.

Ambos são geridos pelo mesmo ciclo descrito nesta estratégia.

## 3. Categorias de risco

Os riscos são classificados em categorias, para facilitar identificação e análise:

| Categoria | Exemplos |
|---|---|
| **Técnico** | Complexidade, arquitetura, integrações, dependências tecnológicas. |
| **Prazo** | Estimativas otimistas, atrasos de dependências, mudanças de escopo. |
| **Custo** | Estouro de orçamento, esforço subestimado. |
| **Recursos** | Indisponibilidade de pessoas-chave, concorrência de recursos entre projetos. |
| **Externo / Cliente** | Dependência de terceiros, mudanças do cliente, fatores regulatórios. |

## 4. Ciclo de gerência de riscos

### 4.1. Identificação
Riscos e oportunidades são identificados ao longo do projeto, a partir de: planejamento, reuniões da equipe, lições aprendidas de projetos anteriores e análise das categorias acima.

### 4.2. Análise e priorização
Cada risco é avaliado segundo dois fatores, em escala de 1 (baixo) a 3 (alto):

- **Probabilidade:** chance de o risco ocorrer.
- **Impacto:** severidade do efeito caso ocorra.

A **exposição ao risco** é o produto Probabilidade × Impacto, resultando na priorização:

| Exposição (P × I) | Prioridade |
|---|---|
| 6 a 9 | Alta — tratamento imediato |
| 3 a 4 | Média — tratamento planejado |
| 1 a 2 | Baixa — monitoramento |

### 4.3. Tratamento
Para cada risco priorizado, define-se uma estratégia de resposta:

| Estratégia | Aplicação |
|---|---|
| **Mitigar** | Reduzir probabilidade e/ou impacto. |
| **Evitar** | Eliminar a causa do risco. |
| **Transferir** | Repassar o risco a terceiro (ex.: contrato, seguro). |
| **Aceitar** | Conviver com o risco, com plano de contingência se necessário. |

Para oportunidades, aplicam-se respostas análogas (explorar, potencializar, compartilhar, aceitar).

### 4.4. Monitoramento
Os riscos são monitorados continuamente e revisados em três momentos:

- **A cada sprint:** revisão dos riscos ativos do projeto.
- **Nos marcos do projeto:** revisão estruturada, incluindo novos riscos e reavaliação dos existentes.
- **Organizacional (periódico):** o Time de Melhoria Contínua revisa os riscos de natureza organizacional (que afetam a empresa além de um projeto).

## 5. Registro

Os riscos e oportunidades são registrados e acompanhados no **Jira**, contendo no mínimo: identificação, categoria, descrição, probabilidade, impacto, exposição, estratégia de resposta, responsável e situação.

## 6. Riscos organizacionais

Além dos riscos de projeto, a Timeware acompanha riscos de natureza organizacional — por exemplo, concorrência de recursos entre projetos do portfólio, dependência de pessoas-chave e riscos de negócio. Esses riscos são tratados pela gerência e pelo Time de Melhoria Contínua, conforme a Gerência Organizacional de Software (OSW).

## 7. Papéis

| Papel | Responsabilidade |
|---|---|
| **Gerente de Projeto** | Conduz a gerência de riscos no projeto; mantém o registro atualizado. |
| **Equipe do Projeto** | Identifica riscos e executa as respostas planejadas. |
| **Time de Melhoria Contínua** | Mantém esta estratégia; acompanha riscos organizacionais. |
| **COO (Operações)** | Trata os riscos organizacionais; decide respostas no nível operacional; reporta ao CEO os de maior exposição. |
| **Founder e CEO** | Decide sobre riscos organizacionais que exigem autoridade estratégica. |

## 8. Documentos relacionados

- POL-ORG-001 — Política Organizacional de Processos
- PRO-GPC-001 — Processo-Padrão Organizacional
- Processo de Gerência de Projetos (GPR)
- Gerência Organizacional de Software (OSW)
- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 20/08/2025 | Time de Melhoria Contínua | Definição inicial da estratégia de gerência de riscos e oportunidades |
| 1.1 | 25/11/2025 | Time de Melhoria Contínua | Inclusão da camada COO no tratamento de riscos organizacionais |
