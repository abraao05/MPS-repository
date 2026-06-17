# Ata de Piloto — Módulo Metas e RV — SuperApp Fruki · Pacote 1

| Campo | Valor |
|---|---|
| **Documento** | ATA-FRUKI01-007 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Versão** | 1.0 |
| **Data** | 05/08/2025 |
| **Tipo** | Sessão de piloto com vendedores selecionados + reunião de revisão de resultados |
| **Canal** | Presencial (campo) + Microsoft Teams (revisão) |
| **Fireflies** | Não registrado — piloto em campo; feedback coletado por formulário e WhatsApp |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão Oliveira | Timeware | GP / Product Owner |
| Brenda Chrystie | Timeware | UX / Analista de negócio |
| Luca Watson | Timeware | Desenvolvedor |
| Cecília Ribeiro | Fruki | Responsável pelo produto (cliente) |
| Jardel Dargas Silva | Fruki | Tech lead / revisor de PR |
| Representantes de vendas selecionados | Fruki | Usuários finais do piloto |

---

## 2. Objetivo do piloto

Validar o Módulo Metas e Remuneração Variável com dados reais de campo antes do aceite formal do Pacote 1. O piloto foi realizado com um grupo de representantes de vendas selecionados pela Fruki, utilizando o APK de homologação em dispositivos Android pessoais em suas rotinas normais de trabalho.

---

## 3. Escopo do piloto

| Funcionalidade | RF | Incluída no piloto |
|---|---|---|
| Acompanhamento de metas por família de produtos | RF-01 | Sim |
| Acompanhamento de metas por item / SKU | RF-02 | Sim |
| Acompanhamento de visitas do dia | RF-03 | Sim |
| Acompanhamento de representantes fora de rota | RF-04 | Sim (supervisores) |

---

## 4. Configuração do piloto

- **Data de início:** 05/08/2025
- **Duração:** ~2 semanas (até aceite formal em Set/2025)
- **APK distribuído via:** link Expo compartilhado por Cecília Ribeiro com representantes selecionados
- **Dispositivos:** Android (versões variadas; mínimo Android 8.0)
- **Dados:** dados reais de produção da Fruki (APIs em ambiente de produção)

---

## 5. Defeitos e ajustes identificados no piloto

| # | Problema identificado | RF afetado | Ação tomada | Responsável | Data resolução |
|---|---|---|---|---|---|
| P-01 | Duplicação de famílias de produtos na listagem de metas por família | RF-01 | Implementação de deduplicação em `metasService.ts` — famílias ordenadas e deduplicadas antes do repasse ao estado | Luca Watson | Ago/2025 |
| P-02 | Cálculo inconsistente de positivação: percentual exibido diferente do sistema Fruki | RF-01 / RF-02 | Revisão da fórmula de cálculo com Jardel; alinhamento do cálculo com regra de negócio fornecida por Cecília; correção no serviço front-end | Luca Watson / Jardel Dargas Silva | Ago/2025 |
| P-03 | Latência perceptível na abertura da tela de metas por família (>3s em 4G) | RF-01 | Otimização da chamada à API; implementação de cache local para sessão | Luca Watson | Ago/2025 |

---

## 6. Feedback qualitativo dos representantes

| Aspecto | Avaliação | Observação |
|---|---|---|
| Clareza das informações de meta | Positiva | Representantes consideraram mais fácil acompanhar o progresso do que no sistema anterior |
| Velocidade de carregamento (após correção) | Satisfatória | Melhora percebida após otimização de latência (P-03) |
| Usabilidade geral | Positiva | Nenhum pedido de alteração estrutural de tela ou fluxo de navegação |
| Informação de positivação | Inicialmente confusa | Resolvida após correção de cálculo (P-02) e explicação pela Cecília aos representantes |

---

## 7. Decisões tomadas

| Decisão | Responsável |
|---|---|
| Corrigir duplicação e cálculo de positivação antes de encaminhar para aceite formal | Abraão Oliveira |
| Manter normalização no front-end (deduplicação, ordenação) sem solicitar correção da API Fruki | Abraão Oliveira (ver GDE-FRUKI01-001 — Decisão 1) |
| Encaminhar PR para revisão de Jardel após correções | Abraão Oliveira |

---

## 8. Encaminhamentos

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| 1 | Corrigir deduplicação de famílias em `metasService.ts` | Luca Watson | Ago/2025 |
| 2 | Corrigir cálculo de positivação alinhado com regra de Cecília | Luca Watson | Ago/2025 |
| 3 | Gerar novo APK pós-correções e redistribuir para Cecília | Abraão Oliveira | Ago/2025 |
| 4 | Revisão técnica da PR pelo Jardel após correções | Jardel Dargas Silva | Set/2025 |
| 5 | Aceite formal do Pacote 1 após validação pós-correções | Cecília Ribeiro / Leandro Lottermann | Set/2025 |

---

## 9. Resultado do piloto

- **Status:** Concluído com sucesso após correções
- **Defeitos críticos:** 0 (os defeitos P-01 e P-02 foram corrigidos antes do aceite)
- **Aceite formal:** Pacote 1 aceito em Set/2025 — ver `TAE-FRUKI01-001_Termo-de-Encerramento.md`
- **Lição aprendida:** Validação de protótipo antes da sprint e piloto com dados reais antes do aceite formam um ciclo de qualidade eficaz para detecção de problemas de negócio — registrado em `LI-FRUKI01-001` (LE-01)

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (piloto realizado em ago/2025) |
