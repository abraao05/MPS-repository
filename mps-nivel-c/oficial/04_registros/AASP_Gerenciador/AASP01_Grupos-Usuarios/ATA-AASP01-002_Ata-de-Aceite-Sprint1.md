# Ata de Aceite — Sprint 1 — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASP01-002 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Reunião** | Sprint Review + Aceite Formal — Sprint 1 |
| **Data** | 06/06/2026 |
| **Horário** | 14h00 – 15h30 |
| **Canal** | Microsoft Teams |
| **Facilitador** | Abraão (Timeware) |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Processo MPS-SW** | AQU / GRE (evidência de projeto) |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão · Cezar Hiraki | Timeware | GP (Abraão) · Arquiteto/Tech Lead (Cezar) · Facilitador |
| Renan Kiyoshi | Timeware | Desenvolvedor |
| Henry Komatsu | Timeware | Desenvolvedor |
| Mateus Veloso | Timeware | Desenvolvedor |
| Marcos Turnes | AASP | Product Owner / Representante do Cliente / Aprovador |
| Caroline Sousa | AASP | QA / Homologadora |

---

## 2. Objetivo da Reunião

Apresentar os entregáveis da Sprint 1 (AG-20, AG-21, AG-22) ao cliente AASP, demonstrar o funcionamento dos endpoints via Swagger UI, apresentar os resultados dos testes de homologação executados por Caroline Sousa e obter o aceite formal de Marcos Turnes (AASP, PO), encerrando oficialmente a Sprint 1.

---

## 3. Itens Apresentados

| História | Requisitos Cobertos | Endpoints Demonstrados | Status dos Testes | Resultado do Aceite |
|---|---|---|---|---|
| **AG-20** — CRUD de Grupos | RF-01 a RF-04 | incluirgrupo (criação com validação de nome único); listargrupo (listagem paginada); buscargrupoporid (usuários do grupo); alterargrupo (alteração); excluirgrupo (soft delete — campo excluido=1); ativardesativar (ativa/desativa) | 7 cenários: GRP-01 a GRP-07 — todos OK (100%) | Aprovado por Marcos Turnes |
| **AG-21** — Função do Usuário no Grupo | RF-05 | alterarfuncaodousuario (função: Usuario/Administrador) | 1 cenário: FUNC-01 — OK (100%) | Aprovado por Marcos Turnes |
| **AG-22** — Vínculo Usuário-Grupo | RF-06 | vínculo de usuários via GrupoDeUsuarios em incluirgrupo/alterargrupo; removerusuario (soft delete do vínculo) | 2 cenários: VINC-01, VINC-02 — todos OK (100%) | Aprovado por Marcos Turnes |

---

## 4. Demonstração Técnica

Cezar Hiraki demonstrou todos os endpoints via **Swagger UI** (`http://localhost:5000/swagger`) com banco `auxo3` de homologação, cobrindo os fluxos happy path e sad path de cada história. As validações de negócio (nome único de grupo e função do usuário) foram demonstradas em tempo real com payloads de teste preparados previamente.

Renan Kiyoshi demonstrou os **scripts de migration** do banco de dados (estrutura das tabelas grupos_usuarios, grupos_usuarios_vinculos e grupos_usuarios_funcao) e a organização do repositório no GitLab, incluindo as branches de feature, MRs aprovados e histórico de commits por história.

Caroline Sousa confirmou que todos os **10 cenários de aceite** (GRP-01 a GRP-07, FUNC-01, VINC-01 e VINC-02) foram executados por ela no ambiente de homologação AASP em 06/06/2026 e aprovados sem ressalvas, conforme evidências registradas no CTQ-AASP01-001.

---

## 5. Resultados dos Testes de Homologação — Sprint 1

| Tipo de Teste | Quantidade | Resultado |
|---|---|---|
| Testes unitários | 22 métodos | 100% passando; cobertura estimada 85% (meta: ≥80% — atingida) |
| Testes de integração | 3 | 100% passando (round-trip banco auxo3 validado) |
| Cenários de aceite (CTQ) | 10 | 10/10 (100%) aprovados por Caroline Sousa em 06/06/2026 |
| Achados code review (REV) | 5 (P2: 3; P3: 2) | Todos resolvidos antes do merge — nenhum defeito aberto |

---

## 6. Pontos Levantados pelo Cliente

- **Marcos Turnes (AASP — PO):** Confirmou que os endpoints atendem ao que foi especificado no REQ-AASP01-001. Nenhuma ressalva técnica ou de negócio foi identificada. Solicitou que a Sprint Review da Sprint 2 seja realizada em 20/06/2026 no mesmo horário (14h00, Teams).

- **Caroline Sousa (AASP — QA):** Validou todos os 10 cenários de aceite no ambiente de homologação AASP. Solicitou que o ambiente de homologação para a Sprint 2 seja preparado pela equipe Timeware até 11/06/2026, incluindo os scripts de migration das novas tabelas (AuditoriaGrupos).

- **Abraão (Timeware — GP):** Informou que a Sprint 2 inicia em 09/06/2026 com as histórias AG-23 (Auditoria de Grupos) e AG-24 (Integração com ms.temis.vinculos). Confirmou que o ambiente de homologação será preparado até 11/06/2026 conforme solicitado por Caroline Sousa.

---

## 7. Aceite Formal

**Marcos Turnes (AASP) concedeu aceite formal da Sprint 1 SEM RESSALVAS em 06/06/2026.**

A Sprint 1 é considerada oficialmente encerrada e entregue. Todas as histórias (AG-20, AG-21, AG-22) estão em status **Done** e os entregáveis foram aceitos pelo representante do cliente.

**Declaração de aceite (registrada em reunião via Microsoft Teams em 06/06/2026):**

> "Confirmo o aceite formal dos entregáveis da Sprint 1 (AG-20, AG-21 e AG-22) do projeto Grupos de Usuários — AASP Gerenciador. Os endpoints foram demonstrados e validados conforme os critérios de aceite definidos. Nenhuma ressalva ou pendência identificada."
>
> — **Marcos Turnes**, AASP, 06/06/2026

---

## 8. Próximos Passos

| Ação | Responsável | Prazo |
|---|---|---|
| Iniciar Sprint 2 — AG-23 (Auditoria) + AG-24 (Integração ms.temis.vinculos) | Renan Kiyoshi, Henry Komatsu e Mateus Veloso | 09/06/2026 |
| Preparar ambiente de homologação AASP para Sprint 2 (migrations AuditoriaGrupos) | Renan Kiyoshi, Henry Komatsu e Mateus Veloso | 11/06/2026 |
| Confirmar ambiente de homologação Sprint 2 recebido e validado | Caroline Sousa (AASP) | 11/06/2026 |
| Atualizar GEST-AASP01, RAC-AASP01-001 e MED-AASP01-001 com resultados finais Sprint 1 | Abraão | 09/06/2026 |
| Sprint Review Sprint 2 agendada — apresentação de AG-23 e AG-24 | Abraão + Marcos Turnes | 20/06/2026 — 14h00 Teams |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 06/06/2026 | Abraão | Versão inicial — ata de aceite formal da Sprint 1 (AG-20, AG-21, AG-22); aceite concedido por Marcos Turnes sem ressalvas |
