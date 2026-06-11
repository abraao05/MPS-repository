# Termo de Encerramento — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | TAE-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Versão** | 1.0 |
| **Data de encerramento** | 26/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Resumo do projeto

A OS-PARCELA-001 configurou a Fundação Tecnológica de Integração da GASMIG no Azure API Management, estabelecendo a base reutilizável para todas as futuras integrações da empresa. O projeto foi executado em 15 dias corridos (29/04 – 14/05/2026, com aceite formal em 26/05/2026), pela equipe Timeware, dentro do escopo contratado sem change requests.

## 2. Entregas realizadas

| Entrega | Situação | Observação |
|---|---|---|
| Governança corporativa do Azure API Management | ✅ Concluída | Políticas globais, named values, policy fragments, estrutura de produtos e grupos |
| Controle de acesso com políticas de expiração de credenciais | ✅ Concluída | TTL configurado; fluxo de renovação documentado |
| Barreiras de segurança para acesso interno (rede GASMIG) | ✅ Concluída | IP restriction ativa no produto interno |
| Barreiras de segurança para acesso externo (parceiros e clientes) | ✅ Concluída | Políticas de validação de credenciais no produto externo |
| Ambiente de sandbox para testes pré-produção | ✅ Concluída | Produto sandbox com API de exemplo publicado e isolado |
| Catálogo corporativo com identidade visual GASMIG | ✅ Concluída | Portal do desenvolvedor ativo, com branding GASMIG e SSO Entra ID |
| Workspace dedicado ArcelorMittal | ✅ Concluída | `ws-arcelormittal` — produtos, assinaturas e políticas isoladas |
| Workspace dedicado Usiminas | ✅ Concluída | `ws-usiminas` — produtos, assinaturas e políticas isoladas |
| Rate limiting por workspace | ✅ Concluída | Named values e policy fragments configurados |
| Throttling por workspace | ✅ Concluída | Named values e policy fragments configurados |
| SSO SAML / Entra ID no portal | ✅ Concluída | Login via conta corporativa GASMIG funcional |
| Scripts IaC (Bicep/ARM) no Azure DevOps | ✅ Concluída | Configuração versionada no repositório GASMIG |
| Mocks de API (valor agregado sem custo) | ✅ Concluída | Adicionado pela Timeware para demonstrar a fundação em funcionamento |

## 3. Escopo: planejado × realizado

| Dimensão | Planejado | Realizado |
|---|---|---|
| Escopo | 10 RF + 5 RNF conforme REQ-GASMIG02-001 | 100% entregue conforme planejado; sem itens removidos |
| Prazo | 15 dias corridos (até 14/05/2026) | Entregue e aceite em 18/05/2026 (demonstração) / 26/05/2026 (confirmação pagamento) — 4 dias além do marco, sem impacto contratual |
| Change requests | — | Nenhum change request durante a execução |
| Itens adicionais | — | Mocks de API incluídos sem custo como suporte à demonstração |

## 4. Aceite do cliente

| Cliente / responsável | Aceite | Data | Ref. da ata |
|---|---|---|---|
| Sérgio Guimarães Villaça — GASMIG | ✅ Aprovado | 26/05/2026 | ATA-GASMIG02-002 + e-mail Sérgio 26/05/2026 11:39 |

## 5. Transição / sustentação

O ambiente Azure API Management configurado passa ao controle da GASMIG (TI — Sérgio Villaça) a partir do aceite. A documentação técnica entregue (design, IaC, plano de V&V, registro de verificação) está disponível no repositório Azure DevOps da GASMIG e no repositório MPS da Timeware.

Não há transição para sustentação separada — a fundação é o ponto de partida das próximas entregas (OS-PARCELA-002 e projetos de API subsequentes).

## 6. Lições aprendidas

| Tema | O que ocorreu | Lição / recomendação |
|---|---|---|
| Acesso ao ambiente Azure | O provisionamento de acesso ao tenant GASMIG ocorreu sem atraso significativo, não impactando o prazo | Manter o padrão: solicitar acesso no dia 1 e acompanhar ativamente |
| Parâmetros de rede | IPs da rede interna e configurações de firewall foram fornecidos durante a execução, sem bloquear entregas paralelas | Trabalhar com named values parametrizáveis desde o início permitiu avançar sem os valores definitivos |
| Demonstração com mocks | Adicionar mocks de API à demonstração foi percebido positivamente pelo cliente — tornou a entrega mais concreta e compreensível | Para projetos de infraestrutura/configuração, incluir um mock ou caso real na demonstração facilita o aceite |
| Agenda do aceite | A sessão de demonstração ocorreu ao final de uma reunião com pauta diferente (especificação de APIs), o que funcionou mas deixou pouco tempo dedicado | Recomendar sessão exclusiva para aceite em projetos futuros, mesmo que curta |
| Documentação adaptada ao tipo de projeto | A adaptação de V&V e revisão por pares para checklist de configuração (em vez de testes de software) foi adequada e coerente | Manter essa adaptação para projetos de configuração de ferramentas — registrar no ADAP desde o início |

---

## Registro de encerramento

| Aceite formal em | Ref. |
|---|---|
| 26/05/2026 | E-mail Sérgio Villaça 26/05/2026 11:39 — NF encaminhada ao processo de pagamento; ATA-GASMIG02-002 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Versão inicial — encerramento formal da OS-PARCELA-001 |
