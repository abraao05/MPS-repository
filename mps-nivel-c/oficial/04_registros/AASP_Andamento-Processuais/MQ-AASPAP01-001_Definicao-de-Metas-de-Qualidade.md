# DEFINIÇÃO DE METAS DE QUALIDADE — AASP_ANDAMENTOSPROCESSUAIS

MQ-AASPAP01-001 · Versão 1.0 · 15/12/2025 · Timeware Brasil

| Campo | Valor |
|---|---|
| **Documento** | MQ-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Gerente de Projeto** | Abraão Oliveira |
| **Versão** | 1.0 |
| **Data** | 15/12/2025 |
| **Processo MPS-SW** | GPC/MED (evidência de projeto) |
| **Momento** | Início do projeto (kickoff) |

## 1. Objetivo
Definir, no início do projeto, as metas de qualidade que orientam a Medição (MED-AASPAP01-001), a Garantia da Qualidade de Processo (GQA-AASPAP01-001) e a Verificação & Validação (VV-AASPAP01-001) da refatoração da solução legada AndamentosProcessuais para o modelo DataJud/CNJ + WorkerAndamentos.

## 2. Metas de qualidade do projeto
| Código | Meta de qualidade | Alvo | Forma de verificação |
|---|---|---|---|
| MQ-1 | Aderência ao cronograma | ≥ 85% das entregas no prazo | MED (M1) / RAC |
| MQ-2 | Desvio de esforço | ≤ 20% | MED (M2) |
| MQ-3 | Defeitos escapados para produção | 0 | REL-VV / MED (M4) |
| MQ-4 | Taxa de contenção de defeitos (corrigidos antes da implantação) | ≥ 95% | REL-VV / MED (M5) |
| MQ-5 | Retrabalho | ≤ 5% do esforço | MED (M6) |
| MQ-6 | Conformidade de processo (auditoria de GQA) | 100% dos itens conformes | GQA-AASPAP01-001 |
| MQ-7 | Cobertura de requisitos por teste | 100% (RF01–RF12 com cenário de teste) | RASTR / VV / REL-VV |

## 3. Critérios de qualidade funcionais (refatoração cirúrgica)
- Zero regressão no fluxo EPROC/ESAJ em produção durante a transição (verificado pelo CT-12).

- Rastreabilidade: todo estado de processamento registrado com data, status e observação de erro (RNF02).

- Idempotência/resiliência: reenvio (retry) do webhook sem perda nem duplicidade (RNF04).

- Histórico de movimentações por instância sem sobrescrita (inativação + criação).

- Tratamento de erro e de segredo de justiça por instância, sem afetar instâncias não restritas.

## 4. Definição de Pronto (DoD)
Uma entrega é considerada pronta quando: (i) o código foi revisado por Merge Request com ao menos 1 revisor além do autor (ver REV); (ii) os cenários de teste da fase foram aprovados (ver VV/REL-VV); (iii) não há defeito aberto de severidade alta; (iv) a baseline de configuração foi registrada no GitLab (ver GCO).

## 5. Governança das metas
As metas são medidas e reportadas na Medição (MED-AASPAP01-001), verificadas na auditoria de GQA (GQA-AASPAP01-001) e acompanhadas nas atas de acompanhamento por fase. Desvios e ações corretivas são tratados via Change Request (CR) e registrados no RAC.

## Histórico de revisões
| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/12/2025 | Gerente de Projeto | Definição das metas de qualidade do projeto no kickoff (alvos de prazo, esforço, defeitos, contenção, retrabalho, conformidade de processo e cobertura de testes). |
