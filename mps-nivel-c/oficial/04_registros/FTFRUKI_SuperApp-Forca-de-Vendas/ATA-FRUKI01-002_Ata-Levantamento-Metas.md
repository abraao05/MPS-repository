# Ata de Reunião — Levantamento de Demanda — Módulo Metas e RV

| Campo | Valor |
|---|---|
| **Reunião** | Levantamento demanda Metas — SuperApp Fruki |
| **Projeto / contexto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Data** | 25/06/2025 |
| **Local / meio** | Videoconferência (Google Meet) |
| **Responsável pela ata** | Abraão Oliveira |

---

## 1. Participantes

| Nome | Papel | Organização |
|---|---|---|
| Abraão Oliveira | Gerente de Projeto / PO | Timeware |
| Brenda Chrystie | UX/UI Designer / Analista de Negócio | Timeware |
| Leandro Lottermann | Coordenador de Sistemas | Fruki Bebidas |
| Cecília Ribeiro | Analista Digital / PO Cliente | Fruki Bebidas |

---

*Reunião referenciada em Fireflies ID: mo3xiqhyv46qvkkb — "Levantamento demanda Metas"*

## 2. Pauta

- Levantamento das regras de negócio do Módulo de Metas e RV
- Definição dos indicadores a serem exibidos para cada perfil de vendedor
- Acesso ao repositório Azure DevOps e às APIs de metas

## 3. Discussões e definições

**Escopo do módulo Metas/RV:**
- A Fruki possui múltiplos perfis de representantes comerciais com composições de RV distintas; a tela de metas precisa adaptar os indicadores exibidos conforme o perfil do usuário logado
- Indicadores prioritários: volume por família de produtos, cobertura, drop size, positivação e acompanhamento de visitas
- Cecília Ribeiro confirmou as regras de cálculo de RV por perfil e os critérios de atingimento

**APIs disponíveis:**
- `GET /acompanhamentoMetasFamilias/{representante}/{periodo}/{tipo}` — metas e atingimento por família de produtos
- `GET /acompanhamentoMetasItens/{representante}/{periodo}/{tipo}` — metas e atingimento por item (SKU)
- `GET /acompanhamentoForaDeRota/{representante}/{data}` — acompanhamento de representantes fora de rota
- `GET /acompanhamentoVisitas/{representante}/{data}` — visitas realizadas no dia
- Autenticação via headers `client-id` e `client-secret`; Jardel envia as credenciais e documentação Swagger após a reunião

**Acesso ao repositório:**
- Leandro confirmará acesso ao Azure DevOps (`https://dev.azure.com/fruki`) para o usuário `timeware`
- A equipe Timeware trabalha em branch separada (`feature/novos-recursos-superapp`) e entrega via Pull Request revisada pelo Jardel antes do merge

**Protótipos e validação:**
- Brenda será responsável pelo design das telas de metas; protótipos serão compartilhados com Cecília para validação antes do desenvolvimento
- Supervisores de vendas também utilizarão o módulo; suas necessidades de visualização (acompanhamento da equipe) devem ser consideradas no design

## 4. Decisões e aceites

| Decisão / aceite | Responsável | Data |
|---|---|---|
| Indicadores confirmados para o MVP: volume, cobertura, drop size, positivação, visitas | Cecília Ribeiro | 25/06/2025 |
| Autenticação via client-id/client-secret para todas as APIs | Jardel Dargas Silva | 25/06/2025 |
| Branch separada + PR revisada pelo Jardel antes do merge | Abraão Oliveira | 25/06/2025 |
| Protótipos enviados para validação antes de cada sprint | Brenda Chrystie | 25/06/2025 |

## 5. Ações (follow-up)

| Ação | Responsável | Prazo |
|---|---|---|
| Enviar credenciais (client-id/client-secret) e documentação Swagger das APIs | Jardel Dargas Silva | 26/06/2025 |
| Criar usuário `timeware` no Azure DevOps e conceder acesso ao repositório | Leandro Lottermann / Renan | 26/06/2025 |
| Elaborar protótipos iniciais das telas de indicadores de metas | Brenda Chrystie | 02/07/2025 |
| Iniciar desenvolvimento do Módulo Metas/RV após recebimento dos acessos | Luca Watson / Thiago Gomes | 26/06/2025 |

## 6. Próximos passos

- Recebimento dos acessos ao repositório e às APIs (26/06/2025 — e-mail Leandro: "ENC: Instruções para Acesso ao Repositório...")
- Desenvolvimento integrado às APIs com validação contínua de regras de negócio com Cecília
- Geração de APK de teste para piloto com vendedores selecionados (previsão: 05/08/2025)

---

## Controle de atualizações

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (reunião realizada em 25/06/2025) |
