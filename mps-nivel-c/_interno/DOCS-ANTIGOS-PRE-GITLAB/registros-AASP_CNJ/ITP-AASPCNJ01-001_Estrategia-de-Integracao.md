# Estratégia de Integração — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | ITP-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |

---

## 1. Componentes a integrar

| Componente | Descrição |
|---|---|
| CapturaServer | Serviço Windows que identifica NUPs pendentes e os enfileira no RabbitMQ |
| WorkerAndamentos | Workers que consomem a fila, consultam as fontes e enviam resultados via webhook |
| API AndamentosProcessuais | API REST interna que serializa para `IModelElastic` e indexa no Elasticsearch |

## 2. Interfaces

| Interface | Entre | Tipo/contrato |
|---|---|---|
| Enfileiramento | CapturaServer ↔ RabbitMQ | Mensagem com NUP (fila unificada) |
| Captura CNJ | WorkerAndamentos ↔ API DataJud/CNJ | REST, autenticação Bearer (token em `PonteAPI`) |
| Captura TJSP | WorkerAndamentos ↔ Portais EPROC/ESAJ | Crawler Puppeteer (navegador headless) |
| Fallback parceiras | WorkerAndamentos ↔ APIs Solucionário/Botmax | REST (por ordem de prioridade) |
| Gravação | WorkerAndamentos ↔ API AndamentosProcessuais | Webhook → indexação no Elasticsearch |

## 3. Estratégia e ordem de integração

A integração foi entregue de forma incremental:
1. **EPROC/ESAJ (TJSP)** — primeira integração (Fase 2), cobrindo o tribunal de maior volume.
2. **DataJud/CNJ** — fonte primária universal (Fase 4), com roteamento por `CodigoFonteAPI` e fila unificada.
3. **Fallback e desligamento de parceiras** — integração das parceiras como fallback final e rotina de desligamento de NUP após captura via CNJ.

Cada mensagem da fila contém o NUP e as informações para o worker determinar a fonte. Em retorno vazio/aguardando das parceiras, o worker publica um novo item ao final da fila para revisita posterior.

## 4. Ambiente de integração

Azure DevOps (controle de versão e pipeline CI/CD); hospedagem dos workers e APIs internas em AWS; RabbitMQ como broker de mensagens. Ver GCO-AASPCNJ01-001.

## 5. Critérios de prontidão para integração

- Code review aprovado (mínimo 1 revisor além do autor) antes do merge em `develop` (ver REV-AASPCNJ01-001).
- Testes de fluxo executados para o cenário integrado.
- Tratamento de erro por instância implementado e registrado nas tabelas de controle.

## 6. Testes do produto integrado

O fluxo integrado (consulta → autenticação → recebimento do JSON → webhook → indexação) foi validado por testes de integração e de fluxo (E2E), incluindo cenários de sucesso, fallback e erro parcial por instância. Detalhes em VV-AASPCNJ01-001 e REL-VV-AASPCNJ01-001. Mecanismo de retry no envio ao webhook implementado na Fase 5 para aumentar a resiliência.

## 7. Entrega e material de apoio

A entrega em produção segue o rito de GMUD: montagem de pacote de publicação, validação em homologação e agendamento com a Infraestrutura. Material de apoio: coleções Postman da API CNJ e scripts de banco, versionados no Azure DevOps (pasta `/docs` e `/db`).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Estratégia de integração consolidada a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
