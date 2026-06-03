# MPS-SW Nível C — TIMEWARE

Repositório de documentação da implantação do modelo **MR-MPS-SW:2024 — Nível C** na TIMEWARE, conduzida com apoio da avaliadora **ASR Consultoria e Assessoria em Qualidade Ltda.**

---

## Estrutura do repositório

```
mps-nivel-c/
├── _interno/          ← documentos de apoio (NÃO auditáveis pela ASR)
└── oficial/           ← evidências MPS (auditadas pela ASR)
    ├── 00_governanca/
    ├── 01_apoio/
    ├── 02_projeto/
    ├── 03_templates/
    ├── 04_registros/
    │   ├── projeto-1/
    │   ├── projeto-2/
    │   ├── projeto-3/
    │   └── projeto-4/
    └── 05_capacidade/
```

---

## `_interno/` — Documentos de apoio (não auditáveis)

Contém documentos de gestão interna do projeto de implantação. **Não fazem parte do conjunto de evidências avaliado pela ASR.** Use esta pasta para planos de trabalho, mapas de artefatos, anotações de reunião e qualquer material de apoio que oriente a equipe interna, mas que não precisa ser entregue à avaliadora.

Exemplo: `MAPA-ORG-001_Mapa-de-Artefatos-Nivel-C.md` — painel de controle da implantação, com status de cada artefato por processo.

---

## `oficial/` — Evidências MPS (auditadas pela ASR)

Tudo dentro de `oficial/` **pode ser solicitado e analisado pela ASR** durante a avaliação. Mantenha apenas documentos finalizados e aprovados aqui. As subpastas seguem as fases de implantação definidas no MAPA-ORG-001:

| Pasta | Fase | Processos | Conteúdo |
|---|---|---|---|
| `00_governanca/` | Fase 1 | OSW, GPC | Políticas organizacionais, processo-padrão, biblioteca de processos |
| `01_apoio/` | Fase 2 | MED, CAP, GDE, GCO, AQU | Planos e definições dos processos de apoio organizacional |
| `02_projeto/` | Fase 3 | GPR, REQ, PCP, ITP, VV | Definições e templates do ciclo de vida de projeto |
| `03_templates/` | — | Todos | Templates em branco (modelos Confluence/Word prontos para uso) |
| `04_registros/` | — | Todos | Templates preenchidos por projeto (um subdiretório por projeto) |
| `05_capacidade/` | Fase 4 | Transversal | Evidências de institucionalização: registros de GQA, auditorias, melhoria |

---

## Convenções

- Nomenclatura e versionamento de arquivos: ver `oficial/00_governanca/CONV-ORG-001_Convencao-de-Nomenclatura-e-Versionamento.md`
- Ponto focal da implantação: **Abraão Oliveira**
- Modelo de referência: **MR-MPS-SW:2024 — Nível C**
- Avaliadora: **ASR Consultoria e Assessoria em Qualidade Ltda.**
