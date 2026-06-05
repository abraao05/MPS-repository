# Cenários de Teste de Homologação — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | CTQ-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | VV (evidência de projeto — cenários de teste de homologação) |

---

## 1. Contexto

Este documento registra os cenários de teste executados durante a fase de homologação do projeto Cadastro de Clientes — Rede D1000, cobrindo os canais PDV, Balcão, Call Center, Omni (VTEX) e Conveniados, além da integração Propz CRM.

Os cenários foram definidos em conjunto entre as equipes Timeware (QA: Lucas Batista) e D1000 (QA: Julielle Santos / Fagner Pereira) e executados principalmente no período de outubro a janeiro/2026 no ambiente de homologação `d1000_homologacao`.

**Base de dados:** os status reports de 08/10, 14/10 e 17/10/2025 registraram formalmente o progresso e os defeitos identificados.

---

## 2. Resumo de cobertura por canal (snapshot 17/10/2025)

| Canal | Cenários totais | OK | Não OK | Não testados | % Testados |
|---|---|---|---|---|---|
| Balcão | 31 | 17 | 6 | 10 | 74% |
| PDV | 6 | 0 | 0 | 6 | 0% (na data) |
| Call Center | 8 | 0 | 0 | 8 | 0% (desbloqueado em 16/10) |
| Omni | 2 | 0 | 0 | 2 | 0% (URL webhook ajustada 16/10) |
| Conveniados | 4 | 4 | 0 | 0 | **100%** |

---

## 3. Cenários — Canal Balcão (31 cenários)

### 3.1 Cadastro de cliente

| ID | Cenário | Pré-condição | Passos | Resultado esperado | Status (17/10) |
|---|---|---|---|---|---|
| BAL-01 | Cadastro de novo cliente com todos os dados obrigatórios | CPF não existe na base | Informar CPF, nome, data de nascimento, telefone, e-mail no terminal Balcão; confirmar | Cliente cadastrado; código do cliente retornado pelo Balcão = código retornado pela API | OK |
| BAL-02 | Cadastro de cliente sem e-mail (campo opcional) | CPF não existe na base | Informar apenas campos obrigatórios (sem e-mail) | Cliente cadastrado com sucesso | OK |
| BAL-03 | Tentativa de cadastro com CPF já existente | CPF já cadastrado na base | Informar mesmo CPF na tela de cadastro | Sistema exibe mensagem de CPF já cadastrado; não duplica | OK |
| BAL-04 | Cadastro com CPF inválido (dígito verificador errado) | — | Informar CPF com formato inválido | Sistema rejeita antes de enviar; mensagem de validação exibida | OK |
| BAL-05 | Código do cliente no Balcão = código na API | Cliente recém-cadastrado | Cadastrar via Balcão; consultar o mesmo CPF via API | `id_cliente` retornado pelo Balcão deve coincidir com `id_cliente` da API | **Não OK** — Bug BAL-B01 |
| BAL-06 | Cadastro com endereço completo | CPF não existe na base | Informar todos os campos de endereço (CEP, logradouro, número, complemento, bairro, cidade, UF) | Endereço salvo corretamente; retornado na consulta | OK |

### 3.2 Consulta de cliente

| ID | Cenário | Pré-condição | Passos | Resultado esperado | Status (17/10) |
|---|---|---|---|---|---|
| BAL-07 | Consulta de cliente existente por CPF | Cliente cadastrado na base | Digitar CPF na tela de consulta do Balcão | Dados do cliente exibidos corretamente; sem atualização de registro | OK |
| BAL-08 | Consulta após truncate da base — comportamento de leitura pura | Base truncada (cenário de teste de migration) | Consultar cliente que existe na base saneada | Dados retornados sem nenhuma escrita no banco (sem UPDATE gerado) | **Não OK** — Bug BAL-B02 |
| BAL-09 | Consulta de CPF inexistente | CPF não cadastrado | Digitar CPF inexistente | Mensagem de "cliente não encontrado"; sem erro de sistema | OK |
| BAL-10 | Consulta com fallback: cloud indisponível → base local | API cloud simulada como indisponível (timeout) | Realizar consulta com API cloud fora | Sistema faz fallback para base local; resultado retornado | Não testado |

### 3.3 Opt-in / Opt-out e fidelidade

| ID | Cenário | Pré-condição | Passos | Resultado esperado | Status (17/10) |
|---|---|---|---|---|---|
| BAL-11 | Realizar opt-in de cliente | Cliente com opt-in = false | Marcar opt-in na tela do Balcão; salvar | `opt_in = true` na base; flag de fidelidade atualizado corretamente | OK |
| BAL-12 | Realizar opt-out de cliente com fidelidade ativa | Cliente com opt-in = true e fidelidade = true | Desmarcar opt-in (opt-out) na tela do Balcão; salvar | `opt_in = false`; `fidelidade = false` na base | **Não OK** — Bug BAL-B03 |
| BAL-13 | Opt-out de cliente sem programa de fidelidade | Cliente com opt-in = true e fidelidade = false | Desmarcar opt-in; salvar | `opt_in = false`; sem alteração na flag de fidelidade | Não testado |
| BAL-14 | Verificar tipo de opt-in retornado na consulta | Cliente com opt-in ativo | Consultar cliente via Balcão | Campo tipo de opt-in deve ser retornado com valor correto (ex.: "SMS", "EMAIL") | Não testado (pendência levantada em 08/10) |
| BAL-15 | Consulta de cliente com fidelidade — exibição do programa | Cliente com fidelidade = true | Consultar cliente | Programa de fidelidade exibido no Balcão com pontos e validade | Não testado |

### 3.4 Atualização de dados

| ID | Cenário | Pré-condição | Passos | Resultado esperado | Status (17/10) |
|---|---|---|---|---|---|
| BAL-16 | Atualização de telefone principal | Cliente cadastrado | Alterar telefone na tela do Balcão; salvar | Novo telefone salvo; auditoria registrada | OK |
| BAL-17 | Atualização de endereço | Cliente com endereço cadastrado | Alterar endereço; salvar | Endereço atualizado; endereço anterior preservado no log de auditoria | OK |
| BAL-18 | Atualização de e-mail | Cliente sem e-mail cadastrado | Incluir e-mail; salvar | E-mail adicionado com sucesso | OK |
| BAL-19 | Tentativa de atualização com CPF em uso por outro cliente | — | Alterar CPF (se campo habilitado) para CPF já cadastrado | Sistema rejeita; mensagem de conflito | OK |

### 3.5 Conveniados (via Balcão)

| ID | Cenário | Pré-condição | Passos | Resultado esperado | Status (17/10) |
|---|---|---|---|---|---|
| BAL-20 | Consulta de cliente conveniado | Cliente com convênio ativo | Consultar por CPF | Dados do convênio exibidos corretamente | OK |
| BAL-21 | Cadastro de conveniado | Cliente sem convênio | Selecionar convênio; preencher dados; salvar | Convênio associado ao cliente; retornado na próxima consulta | OK |

### 3.6 Cenários de erro e resiliência

| ID | Cenário | Pré-condição | Passos | Resultado esperado | Status (17/10) |
|---|---|---|---|---|---|
| BAL-22 | Timeout na chamada à API | API lenta (simular latência > 30s) | Executar qualquer operação | Exibição de mensagem de timeout; sem travamento de terminal | Não testado |
| BAL-23 | Erro 500 da API tratado no front | Simular erro interno na API | Executar operação de cadastro | Front exibe mensagem amigável; não expõe stack trace | Não testado |

---

## 4. Cenários — Canal PDV (6 cenários)

| ID | Cenário | Pré-condição | Passos | Resultado esperado | Status (17/10) |
|---|---|---|---|---|---|
| PDV-01 | Identificação de cliente por CPF no PDV | Cliente cadastrado | Digitar CPF no terminal PDV | Dados do cliente recuperados; nome exibido na tela | Não testado (pendente) |
| PDV-02 | Cadastro de novo cliente pelo PDV | CPF não existe | Informar CPF + dados mínimos no terminal PDV | Cliente cadastrado; retorno de opt-in = false por padrão | **Não OK** — Bug PDV-B01 |
| PDV-03 | Tentativa de cadastro no PDV — cliente fica com opt-in = true mesmo com falha | CPF não existe | Iniciar cadastro; simular falha (ex.: timeout); consultar CPF depois | Se falhou, cliente NÃO deve estar na base (ou deve estar com opt-in = false) | **Não OK** — Bug PDV-B01 |
| PDV-04 | Consulta de cliente preferencial por UF (fallback local) | Base de clientes preferenciais por UF carregada | Consultar CPF de cliente preferencial | Cliente retornado da base local de clientes preferenciais | Não testado |
| PDV-05 | PDV em modo offline — fallback para base local | API cloud indisponível | Realizar venda com identificação de cliente | PDV consulta base local; venda não bloqueada | Não testado |
| PDV-06 | Sincronização de transação offline ao retornar online | PDV estava offline; transações pendentes | API cloud restaurada | Transações offline sincronizadas sem duplicação | Não testado |

---

## 5. Cenários — Canal Call Center (8 cenários)

| ID | Cenário | PBI Azure DevOps | Resultado esperado | Status (17/10) |
|---|---|---|---|---|
| CC-01 | Cadastrar novo cliente via Call Center | PBI-26 | Cliente cadastrado; sem erro de integração com Gestão | **Não OK** — Bug CC-B01 |
| CC-02 | Consultar cliente por CPF via Call Center | — | Dados completos do cliente retornados em ≤ 500ms | Não testado |
| CC-03 | Atualizar telefone do cliente via Call Center | — | Novo telefone salvo; confirmação exibida ao atendente | Não testado |
| CC-04 | Atualizar endereço do cliente via Call Center | — | Endereço atualizado; auditoria registrada | Não testado |
| CC-05 | Consultar histórico de compras do cliente | — | Histórico retornado (via integração CloseUp) | Não testado |
| CC-06 | Registrar opt-in via Call Center | — | `opt_in = true` salvo; flag de canal = CALLCENTER | Não testado |
| CC-07 | Cliente não encontrado — comportamento do sistema | — | Mensagem clara de "cliente não encontrado"; opção de cadastro | Não testado |
| CC-08 | Autenticação do atendente expirada | — | Sistema solicita nova autenticação; sessão do cliente não perdida | Não testado |

---

## 6. Cenários — Canal Omni / VTEX (2 cenários)

| ID | Cenário | Pré-condição | Passos | Resultado esperado | Status (17/10) |
|---|---|---|---|---|---|
| OMNI-01 | Cadastro de cliente via VTEX (compra e-commerce) | CPF não existe na base | Realizar checkout no e-commerce VTEX com CPF novo | Cliente criado via endpoint POST /clientes/vtex; webhook de confirmação recebido | Não testado (desbloqueado em 16/10 com nova URL) |
| OMNI-02 | Integração de pedidos — fluxo legado vs. atual | Pedidos do legado e novo sistema coexistindo | Fazer pedido via VTEX; verificar consolidação no ITEC | Pedido consolidado corretamente sem duplicação; fluxo validado pelo Ethierre | Não testado (Ethierre finalizando análise em 17/10) |

---

## 7. Cenários — Conveniados (4 cenários — 100% OK)

| ID | Cenário | Resultado | Status final |
|---|---|---|---|
| CONV-01 | Importação de conveniados via API de integração | Importação concluída sem erro | **OK** (validado pelo time de Suporte) |
| CONV-02 | Consulta de conveniado por CPF | Dados do convênio retornados corretamente | **OK** |
| CONV-03 | Conveniado com múltiplos convênios ativos | Todos os convênios listados corretamente | **OK** |
| CONV-04 | Inativação de convênio de cliente | Convênio inativado; cliente permanece ativo | **OK** |

---

## 8. Cenários — Integração Propz CRM (endpoints reais)

Documentação da integração entregue em 04/12/2025. Defeito de documentação identificado por Julielle Santos (QA D1000) em 05/12/2025.

### 8.1 Health check e listagem

| ID | Cenário | Endpoint | Resultado esperado | Status |
|---|---|---|---|---|
| PROPZ-01 | Health check da integração | GET /api/Propz/health | HTTP 200; status de conexão com a Propz = healthy | OK |
| PROPZ-02 | Listar redes disponíveis | GET /api/Propz/redes | Lista retorna: 1=Drogasmil, 2=Farmalife, 3=Tamoio, 4=Rosário | **Não OK** na documentação inicial — Bug PROPZ-B01 (códigos invertidos: 3=Rosário, 4=Tamoio estava incorreto) |

### 8.2 Verificação e sincronização individual

| ID | Cenário | Endpoint | Body | Resultado esperado | Status |
|---|---|---|---|---|---|
| PROPZ-03 | Verificar existência de cliente na Propz — Drogasmil | GET /api/Propz/existe/{cpf}?codigoRede=1 | — | HTTP 200; body `{"existe": true/false}` | OK |
| PROPZ-04 | Verificar existência de cliente não cadastrado | GET /api/Propz/existe/{cpf}?codigoRede=1 (CPF sem cadastro na Propz) | — | HTTP 200; `{"existe": false}` | OK |
| PROPZ-05 | Sincronizar cliente individual — Rede Rosário (codigoRede=4) | POST /api/Propz | `{"cpf": "12345678901", "codigoRede": 4}` | HTTP 200; cliente criado/atualizado na Propz; resposta da Propz retornada | OK (após correção da inversão de código) |
| PROPZ-06 | Sincronizar cliente individual — Rede Tamoio (codigoRede=3) | POST /api/Propz | `{"cpf": "12345678901", "codigoRede": 3}` | HTTP 200; cliente criado/atualizado na Propz | OK (após correção) |
| PROPZ-07 | Sincronizar cliente com CPF inválido | POST /api/Propz | `{"cpf": "00000000000", "codigoRede": 1}` | HTTP 422; validação rejeitada antes de chamar a Propz | OK |
| PROPZ-08 | Sincronizar cliente com codigoRede inexistente | POST /api/Propz | `{"cpf": "12345678901", "codigoRede": 99}` | HTTP 400; mensagem de rede inválida | OK |

### 8.3 Sincronização em lote

| ID | Cenário | Endpoint | Payload | Resultado esperado | Status |
|---|---|---|---|---|---|
| PROPZ-09 | Sincronizar lote de 1 cliente | POST /api/Propz/lote | Array com 1 registro | HTTP 200; 1 sincronizado com sucesso | OK |
| PROPZ-10 | Sincronizar lote de 50 clientes (máximo) | POST /api/Propz/lote | Array com 50 registros | HTTP 200; todos processados | OK |
| PROPZ-11 | Sincronizar lote com 51 clientes (acima do limite) | POST /api/Propz/lote | Array com 51 registros | HTTP 400; mensagem de limite excedido | OK |
| PROPZ-12 | Lote com clientes de redes diferentes | POST /api/Propz/lote | Array com registros de codigoRede 1, 2, 3 e 4 | HTTP 200; cada cliente sincronizado na rede correta | OK |
| PROPZ-13 | Lote com CPF duplicado no mesmo payload | POST /api/Propz/lote | Array com mesmo CPF duas vezes | HTTP 400 ou deduplicação automática; sem duplicata na Propz | Não testado |

---

## 9. Registro de defeitos identificados na homologação

### 9.1 Bugs confirmados (com referência nos status reports)

| ID Bug | Canal | Descrição | Identificado por | Data | Status final |
|---|---|---|---|---|---|
| BAL-B01 | Balcão | Código do cliente retornado pelo Balcão diverge do `id_cliente` na API | Fagner Pereira | 15/10/2025 | Corrigido (deploy sprint final) |
| BAL-B02 | Balcão | Consulta após truncate da base envia UPDATE para todos os clientes consultados (comportamento incorreto — deveria ser somente leitura) | Fagner Pereira | 15/10/2025 | Corrigido |
| BAL-B03 | Balcão | Realizar opt-out não atualiza a flag `fidelidade` para false; cliente permanece com fidelidade = true | Fagner Pereira | 15/10/2025 | Corrigido |
| PDV-B01 | PDV | Tentativa de cadastro falhou, mas cliente foi persistido com `opt_in = true`; ao consultar o CPF, cliente não é encontrado (inconsistência: registro parcial "fantasma") | Fagner Pereira | 15/10/2025 | Corrigido |
| CC-B01 | Call Center | Erro ao cadastrar cliente: "Ocorreu um erro ao tentar cadastrar ou atualizar o registro na base do Gestão" (PBI-26) | Equipe D1000 | 21/10/2025 | Corrigido |
| API-B01 | API | Erro no front ao cadastrar cliente via PDV/Balcão (erro exibido no front, mas cadastro é concluído no banco) — comportamento silencioso | Equipe Timeware | 14/10/2025 | Corrigido (deploy 14/10) |
| PROPZ-B01 | Propz CRM | Códigos das bandeiras Tamoio e Rosário invertidos na documentação (correto: 3=Tamoio, 4=Rosário) | Julielle Santos | 05/12/2025 | Corrigido na documentação |

### 9.2 Itens de melhoria identificados (não bugs)

| ID | Descrição | Canal | Decisão |
|---|---|---|---|
| MEL-01 | Campo "tipo de opt-in" não retornado na consulta do Balcão (ex.: "SMS", "EMAIL") — necessário para regras de negócio de fidelidade | Balcão | Implementado no sprint seguinte |
| MEL-02 | Fallback cloud → local → preferencial: regra definida, scripts de clientes preferenciais por UF precisam ser carregados | PDV | Scripts de insert preparados e carregados |
| MEL-03 | Versão do Call Center confirmada em 25721 — necessário merge antes de liberar ambiente de testes | Call Center | Merge realizado por Renan em 14/10 |

---

## 10. Processo de aceite por canal

O processo de aceite seguiu o fluxo estabelecido no PLA-PROFARMA01-001:

1. **Timeware** executa correções e faz deploy no ambiente `d1000_homologacao`
2. **Fagner Pereira / Equipe D1000** valida no ambiente com dados reais de homologação
3. **Julielle Santos (QA D1000)** executa os cenários formais e registra resultado
4. **Pedro Costa (Patrocinador)** emite autorização para início do piloto após aceite técnico
5. **Piloto loja 9** executado como validação final em condições reais de operação

Sequência de liberação final (janeiro/2026):
- 21/01/2026: Timeware finaliza novo pacote de backend; PR enviado para merge pela Profarma
- 22/01/2026: Timeware comunica formalmente a liberação para testes (e-mail Abraão → Armando)
- 23/01/2026: Pedro Costa confirma início do processo de atualização do ambiente
- 26/01/2026: Fagner Pereira confirma versão atualizada no ambiente
- 29/01/2026: Aceite formal emitido por Humberto Erler

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — reconstituída com base nos status reports de 08/10, 14/10 e 17/10/2025, documentação da integração Propz (04/12/2025) e e-mails de liberação para testes (jan/2026) |
