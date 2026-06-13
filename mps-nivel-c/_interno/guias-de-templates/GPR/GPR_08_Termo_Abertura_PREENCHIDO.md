# Termo de Abertura do Projeto — Trainer Connect

> **Modelo de preenchimento** com base no projeto real *Trainer Connect* — plataforma web para personal trainers gerenciarem alunos e prescreverem treinos. Dados sem equivalente real no repositório (orçamento, nome do gestor, cliente formal) marcados com *(exemplo)*. O objetivo é mostrar como o template fica preenchido, não servir de registro oficial.

---

## Identificação

| Campo | Valor |
|---|---|
| Documento | TAP-TCON-001 |
| Projeto | Trainer Connect — plataforma de gestão para personal trainers |
| Cliente / patrocinador | *(exemplo: cliente Timeware)* |
| Versão | v1 |
| Data de abertura | 06/01/2025 |
| Gerente de Projeto | *(exemplo: Gestor Timeware)* |

---

## 1. Objetivo do projeto

Permitir que personal trainers gerenciem sua base de alunos, montem e prescrevam treinos personalizados e acompanhem a execução pelo aluno — tudo em uma plataforma web de acesso fácil, sem necessidade de planilhas ou ferramentas desconexas. O resultado esperado é que o trainer ganhe produtividade na gestão do dia a dia e o aluno tenha maior adesão ao programa por ter o treino acessível e organizado.

---

## 2. Escopo macro

### 2.1 Incluído

- Cadastro e gestão de alunos (perfil, histórico, vínculo trainer↔aluno)
- Biblioteca de exercícios (com exercícios públicos reutilizáveis entre trainers)
- Montagem e prescrição de treinos a partir da biblioteca
- Acompanhamento de execução pelo aluno (visualização e registro de progresso)
- Autenticação e perfis diferenciados (trainer e aluno)

### 2.2 Não incluído (explicitamente excluído)

- Cobrança, pagamentos in-app ou integração com gateway de pagamento (parqueado para v2.0 — dependência de integração com gateway ainda imatura)
- Confirmação de e-mail (excluída por limitação do plano de infraestrutura adotado)
- Aplicativo móvel nativo (produto web responsivo; app nativo fora do escopo atual)

---

## 3. Partes interessadas

| Parte interessada | Papel / interesse no projeto |
|---|---|
| Personal trainer (usuário primário) | Usa o produto para gerenciar alunos e prescrever treinos; valida as entregas |
| Aluno do trainer | Usuário final; acessa e executa o treino recebido |
| Cliente / patrocinador *(exemplo)* | Define escopo e aprova orçamento; recebe o produto entregue |
| Equipe Timeware (dev + gestão) | Constrói, entrega e dá suporte ao produto |

---

## 4. Equipe do projeto

| Papel | Pessoa | Responsabilidade no projeto |
|---|---|---|
| Gerente de Projeto | *(exemplo: Gestor Timeware)* | Planejamento, acompanhamento e encerramento |
| Desenvolvedor full-stack | *(exemplo: Dev Timeware)* | Implementação, arquitetura e decisões técnicas |
| Product Owner / Referência de negócio | *(exemplo: PO / cliente)* | Priorização do backlog, aceite de entregas por milestone |

---

## 5. Macroplanejamento (marcos com datas-alvo)

> Datas-alvo da abertura do projeto — o planejamento detalhado será feito no Plano do Projeto.

| Marco | Descrição | Data-alvo |
|---|---|---|
| v1.0 — Fundação | Autenticação + cadastro de alunos em produção | 31/01/2025 |
| v1.5 — Treinos | Trainer monta e prescreve treino ao aluno | 28/02/2025 |
| v1.8 — Execução pelo aluno | Aluno visualiza e executa o treino prescrito; fluxos validados com usuário real | 30/04/2025 |

---

## 6. Agenda das próximas atividades

| Atividade | Responsável | Prazo |
|---|---|---|
| Elaborar Registro de Adaptação do processo | Gerente de Projeto | 10/01/2025 |
| Elaborar Plano do Projeto (baseline v1) | Gerente de Projeto + Dev | 13/01/2025 |
| Configurar ambiente de desenvolvimento e repositório | Dev full-stack | 10/01/2025 |
| Iniciar fase Fundação (histórias OWN-01…) | Dev full-stack | 13/01/2025 |

---

## 7. Premissas e restrições iniciais

### 7.1 Premissas

- Cliente / PO disponível para validações ao fim de cada milestone.
- Infraestrutura de hospedagem com publicação automática já disponível.
- A biblioteca de exercícios públicos pode ser populada ao longo da construção (não é pré-requisito bloqueante).
- Cada fase pode ser entregue em produção de forma incremental, sem dependência de completar o produto inteiro primeiro.

### 7.2 Restrições

- Prazo máximo para v1.8 (milestone final do escopo atual): 30/04/2025.
- Orçamento aprovado: R$ 45.000 *(exemplo)*.
- Plano de infraestrutura adotado não suporta confirmação de e-mail — funcionalidade excluída do escopo.
- Módulo de comércio (integração com gateway) não pode entrar neste escopo por dependência imatura — registrado formalmente como exclusão.

---

## Registro de abertura

| Campo | Valor |
|---|---|
| Data do kickoff | 06/01/2025 |
| Referência à ata de kickoff | ATA-TCON-001 *(exemplo)* |
| Aprovado por | *(exemplo: Gestor Timeware — Gerente de Projeto)* |
