#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera o mapa de links do Google Drive (acervo oficial Timeware) para a planilha
de indicadores da ASR.

Saida: MAPA-DRIVE_Indice-de-Links.csv  (colunas: Pasta | Documento | Tipo | Link)
       MAPA-DRIVE_Indice-de-Links.xlsx (se openpyxl estiver disponivel)

Os dados (pasta, nome do arquivo, id) foram coletados via search_files do
conector Google Drive, pasta por pasta (parentId), em 13/06/2026.
O link e' montado pelo template oficial do Drive a partir do id.
"""
import csv
import os
import sys

LINK_TPL = "https://drive.google.com/file/d/{id}/view?usp=drivesdk"

# Cada linha: pasta ||| nome_do_arquivo_com_extensao ||| id_do_drive
DATA = r"""
00_governanca|||ATA-GPC-001_Reuniao-Analise-Critica-de-Processos.docx|||1s9RPnB6u6YPiKqHsOoyV3sM4jk8waSQ6
00_governanca|||REG-OSW-002_Comunicacao-da-Politica-Organizacional.docx|||1nJCJ4U3BnvuCSpMTp5w9K5IgSFF-_0X-
00_governanca|||REG-GPC-002_Plano-de-Implementacao-de-Melhorias.docx|||10CueJB2QqzBsWk0c5xw9g-SMlhLe6aCq
00_governanca|||REG-OSW-001_Painel-de-Portfolio.docx|||16GzPsr1B98jKvGynRIZbGMIuB3-xgBNX
00_governanca|||PRO-OSW-002_Gestao-de-Portfolio-de-Projetos.docx|||1dh_076oGwPXwRO50M1MTXkldD0x2jn34
00_governanca|||GQA-ORG-001_Auditoria-Organizacional.docx|||13ypkmhks1HUEva1c1WNgZWom0H1NRndJ
00_governanca|||REG-GPC-001_Registro-de-Melhorias-de-Processo.docx|||12mK6HP6TI01uERtCD5cowZ59frP8MITS
00_governanca|||PLA-GPC-001_Plano-de-Gestao-e-Melhoria-de-Processos.docx|||1Lw-0QgXqeLuTy6iWmVjVmiXtaVdBtqcj
00_governanca|||PRO-GPC-001_Processo-Padrao-Organizacional.docx|||15z2lvvglDk45Eh6jA-mzJbaYCuTnLEsa
00_governanca|||GUIA-GPC-001_Guia-de-Adaptacao-do-Processo-Padrao.docx|||1s7X2zQ0vnCUHx3Jzm3m8eliwIIpX9Zcc
00_governanca|||EST-GPC-002_Estrategia-de-Gerencia-de-Riscos.docx|||1WFa93nIx6l-4It8LE8jSdtbGLqneOXPs
00_governanca|||POL-ORG-001_Politica-Organizacional-de-Processos.docx|||1KBJHr12DQ0TM51UqpNkQiMlsOKsZNdHS
00_governanca|||EST-GPC-001_Estrategia-de-Garantia-da-Qualidade.docx|||1PcLyYQbGTpNvDjGdDvV7Csshp6DRAEKQ
00_governanca|||PRO-GPC-002_Definicao-do-Time-de-Melhoria-Continua.docx|||1SQNp-nJBm5anlx8cMGkrzZokborcrgav
00_governanca|||CONV-ORG-001_Convencao-de-Nomenclatura-e-Versionamento.docx|||1yKI99GViOo-a1ADKW4vs6yG4raqzyxXL
00_governanca|||PRO-OSW-001_Governanca-Organizacional-de-Processos.docx|||1oClWBy8t0wSsbqu6c1WeAVBkLizpN9Cp
00_governanca|||ATA-GPC-001_Reuniao-Analise-Critica-de-Processos.md|||1EEuTIt9ISGnUeoNd7Lt7DD9vNFJlB59u
00_governanca|||REG-OSW-002_Comunicacao-da-Politica-Organizacional.md|||1uJSd2QS0Zx_M3FSSIWiYQ6YGd_GbK-_0
00_governanca|||REG-GPC-002_Plano-de-Implementacao-de-Melhorias.md|||1Y7EUeDcEsFcccvzUAngHWSyyh6yfBudU
00_governanca|||REG-OSW-001_Painel-de-Portfolio.md|||1_KlCtM-JtsNP7nfXJ-amWm_W-RNRQR2T
00_governanca|||GQA-ORG-001_Auditoria-Organizacional.md|||1g6vfBg9quFs8q5ORxAXmvd7gCa_vKjX6
00_governanca|||PRO-OSW-002_Gestao-de-Portfolio-de-Projetos.md|||1J9FGVXCdeNnpRGualWPacksTPwIIZsoB
00_governanca|||PLA-GPC-001_Plano-de-Gestao-e-Melhoria-de-Processos.md|||1xcLwP7ixzwYPLjkZGzmuTKLRVC9URm3F
00_governanca|||REG-GPC-001_Registro-de-Melhorias-de-Processo.md|||1NhvbapiCkmSZduNELja-urzuNU_rJZmx
00_governanca|||PRO-GPC-001_Processo-Padrao-Organizacional.md|||13J3dcvr__Vs5_XIzyjVt-wlG3VxWIric
00_governanca|||GUIA-GPC-001_Guia-de-Adaptacao-do-Processo-Padrao.md|||1I0lk9tEWdpP_DW_eqSOXbmpOobbMvuK_
00_governanca|||EST-GPC-002_Estrategia-de-Gerencia-de-Riscos.md|||1MllGYXnjqDoA_xHcSpMnljQFAnxBCMCr
00_governanca|||EST-GPC-001_Estrategia-de-Garantia-da-Qualidade.md|||1aT-otYaoxJ83fFgBmnO_1XNfaZshZ5a8
00_governanca|||PRO-GPC-002_Definicao-do-Time-de-Melhoria-Continua.md|||1ZMItgBSAAiuUyTxp_5M5ENp6QC4qYrWe
00_governanca|||PRO-OSW-001_Governanca-Organizacional-de-Processos.md|||1jOjPRa6GiU7fW8xrIvx8oeRfke0fyYvd
00_governanca|||CONV-ORG-001_Convencao-de-Nomenclatura-e-Versionamento.md|||17HJQfMjPnEOk_ZAYsaufEELNizZREYM6
00_governanca|||POL-ORG-001_Politica-Organizacional-de-Processos.md|||19p6sKCbL0INg_e5ccIT_qYegWID3mH7d
01_apoio|||PLA-CAP-001_Plano-de-Capacitacao.docx|||15f8l5cLRx2GUtPtEOgB5YMr_B8wLzUyX
01_apoio|||PLA-CAP-001_Plano-de-Capacitacao.md|||1SNg3LxGK2LzuGArQi4Y6ZnshmsaL1k8V
01_apoio|||REG-MED-001_Repositorio-Organizacional-de-Medicao.md|||1y9d_Tifq5ymLZi471yNVKwhp2oIbkxeM
01_apoio|||PRO-GCO-001_Processo-de-Gerencia-de-Configuracao.docx|||14nFj1LZ8Ua49h8KWxHzERS2-7zXtXgGq
01_apoio|||PRO-CAP-001_Processo-de-Capacitacao.md|||1FCGW2TBeSVry2MaWPkzx8oF0oh6P2x7b
01_apoio|||PRO-MED-001_Processo-de-Medicao.docx|||1Z2FhoHfN_g3Wvgqd6OmWooBY-gT0fFvW
01_apoio|||PRO-MED-001_Processo-de-Medicao.md|||14bS2beLkw_RodEHv_m2d_jKOXkpYITxl
01_apoio|||PRO-CAP-001_Processo-de-Capacitacao.docx|||1-R1f0avcdbEkKxwPDvBlJF5RqJlUI4bK
01_apoio|||PRO-GCO-001_Processo-de-Gerencia-de-Configuracao.md|||1YOiurj5y8HJEMKovAMxawzEpvR-ycQty
01_apoio|||PRO-GDE-001_Processo-de-Gerencia-de-Decisoes.docx|||1_NACA9i2s6L-ZwzbonY6mDbNK84z_bc8
01_apoio|||PRO-AQU-001_Processo-de-Aquisicao.docx|||11QhxjcAqXMJqQ5JRPC3uRorX8htrC0Gv
01_apoio|||GUIA-GCO-001_Guia-de-Nomenclaturas-Tecnicas.docx|||1RdyMfVvNDDoMRVoEDgg9XqrGPw0xZfvP
01_apoio|||PLA-MED-001_Plano-de-Medicao.docx|||1OIs1jn8y5vbVwuATrGkxl8k8lufjArMd
01_apoio|||PLA-GCO-001_Plano-de-Gerencia-de-Configuracao.docx|||1EByQS4N7fnjNayOj6xD9FIic8lY2dVWk
01_apoio|||PRO-GDE-001_Processo-de-Gerencia-de-Decisoes.md|||1ZgPCPbKCTJxmI0de7UCEMaNMsWMwhlOB
01_apoio|||DIAG-GPC-001_Fluxo-do-Processo-Padrao.svg|||1VcE5l4Q3ZKn1xnD22cW6oGtMI0ZGcoaq
01_apoio|||PLA-GCO-001_Plano-de-Gerencia-de-Configuracao.md|||1GAXEf-Rgw6FUAl1GJsabUA75uoGycy0y
01_apoio|||GUIA-GCO-001_Guia-de-Nomenclaturas-Tecnicas.md|||1hNRZy_3-cU8McKmBLSWs9PuGwbMftoUY
01_apoio|||PRO-AQU-001_Processo-de-Aquisicao.md|||1fr64cQA9CxVUTdpaaEaliRkY-USP8gfu
01_apoio|||PLA-MED-001_Plano-de-Medicao.md|||1V6NiR6exNC6XMpHqGNWw9GAoS704bjEr
01_apoio/cap|||MAT-CAP-023_Trilha-Tecnica-Onboarding.docx|||1sKQLlANRH_jIB6WIy0v6ko5XemKojdC-
01_apoio/cap|||REG-CAP-CV-001_Indice-de-Curriculos.docx|||1K0cu6iTTt70jGgGBXDo9pRWwPj3sGva4
01_apoio/cap|||REG-CAP-CV-001_Indice-de-Curriculos.md|||14INGstsvVIz7rsXaOxlfArjNflLSFd5x
01_apoio/cap|||REG-CAP-010_Onboarding-Tecnico-Jan2026.docx|||1pWjwFRZgCCd2D4MIN9AEhMIX176WACAg
01_apoio/cap|||REG-CAP-011_Workshop-Azure-APIM-Mar2026.docx|||11KTzVFyJCNcVZHItsY2HZwL8YX2CHk7r
01_apoio/cap|||MAT-CAP-023_Trilha-Tecnica-Onboarding.md|||1oHF_OtwhrXzCkBYJnrTDkTjNhey3vmk_
01_apoio/cap|||REG-CAP-013_Consultoria-Desenho-Processos-Jun2025.md|||1sgqmkafBuD0gJ_EPNluW16VXUquFp24v
01_apoio/cap|||REG-CAP-013_Consultoria-Desenho-Processos-Jun2025.docx|||1FpzpCSb3W1th24HWN5iUTN_O17YSW1NZ
01_apoio/cap|||REG-CAP-012_Workshop-Automacao-Testes-Fev2026.docx|||10RHw3_QQb3-yF4aCqLMMk7vNzROKhbXH
01_apoio/cap|||REG-CAP-012_Workshop-Automacao-Testes-Fev2026.md|||13aw-J5V35sDlLWbE4MMCvt06qA8p-InU
01_apoio/cap|||REG-CAP-010_Onboarding-Tecnico-Jan2026.md|||1jt5GFjbCsNurYrDdCoW-Pjmdr5BanLwK
01_apoio/cap|||REG-CAP-011_Workshop-Azure-APIM-Mar2026.md|||1qu5roDPPeKIxp3C-DCMHOtkuavzA6DX_
01_apoio/cap|||REG-CAP-007_Sessao-Tecnico-Jan2026.docx|||16Lpc4ZfSV0HGifzpJwfeEjIgidwCo2pR
01_apoio/cap|||TPL-CAP-002_Relatorio-de-Eficacia-de-Treinamento.docx|||1m3HpIJ0JgLVQM9LaEDxMUgidJhkg6RJO
01_apoio/cap|||GUIA-CAP-007_MiniManual-GDE.docx|||1MgTl2w9fZz3aHeHW0ZSdEKN9TmEHt7eY
01_apoio/cap|||REG-CAP-005_Sessao-Treinamento-Mai2026.docx|||1wGWK2W15Bws7fpOpta5AaqqvTpBMe7s5
01_apoio/cap|||AVA-CAP-005_Avaliacao-GPC-MED-CAP.docx|||1KMJLMsB9KciEhNQxSNieI3A9O1d7wTsL
01_apoio/cap|||REL-CAP-001_Relatorio-de-Eficacia-2025.docx|||1gXdIOCwtTvOW-QrBf8UYFEv2YEH8q6A3
01_apoio/cap|||AVA-CAP-001_Avaliacao-Processo-Padrao-Geral.docx|||1L0MK80X6mMOf0oDMYQtBVmYKD-LLuB6O
01_apoio/cap|||AVA-CAP-003_Avaliacao-Tecnico-REQ-PCP-VV.docx|||1ihIG6DY8eq0B3qpLdXJMixozPhWv-bwT
01_apoio/cap|||GUIA-CAP-008_MiniManual-MED.docx|||15dXPTmal-yqg9B2vQyoSZEUX8OxZksFr
01_apoio/cap|||GUIA-CAP-005_MiniManual-GCO.docx|||1Ehp57xo1dNee43TBPc6l8McdEHqBIusA
01_apoio/cap|||AVA-CAP-004_Avaliacao-GCO-ITP.docx|||1HR8kPCFtn1YeCpdGSKCsvjEVsTpKdvoZ
01_apoio/cap|||MAT-CAP-021_Trilha-GCO-Baseline.docx|||1xG7FbLTcLVNY9Tf75MM3Ttu_t3ZRjTix
01_apoio/cap|||GUIA-CAP-001_MiniManual-GPR.docx|||1rS4OTxRrRrbua89Qg2Br9jrmOrjabfEu
01_apoio/cap|||REG-CAP-001_Sessao-Treinamento-Dez2024.docx|||1nO1WhH6T77KWemD0dxO2ZTXuzXbJU8at
01_apoio/cap|||REG-CAP-008_Sessao-Tecnico-Fev2026.docx|||1UYtCRfbMeXCdL_aXzAz-wpCs8bTC-sR1
01_apoio/cap|||MAT-CAP-020_Trilha-QA.docx|||1KUq-32kGvzsKicpUN_Kxy0aRMPu0Y_oi
01_apoio/cap|||REG-CAP-003_Sessao-Treinamento-Ago2025.docx|||1x2iX2AevFRS44IkePAvaC9BF1t8i5mup
01_apoio/cap|||MAT-CAP-019_Trilha-DevOps.docx|||1om6pDV7QThxnwkx52889J2_3pOrWACKm
01_apoio/cap|||GUIA-CAP-011_MiniManual-CAP.docx|||1TMwHMbbq0D8I17CWr-cPGP7TzW-GJms0
01_apoio/cap|||MAT-CAP-018_Trilha-Devs.docx|||1cYBe6kG7LK67kpPVPQj-jfolwxk57Z-S
01_apoio/cap|||GUIA-CAP-012_MiniManual-AQU.docx|||1xT56t0Yfh7YnSZ1TPx8TYla_9D9w7Xc4
01_apoio/cap|||GUIA-CAP-010_MiniManual-OSW.docx|||12S8LyYhsEzQv4A0D6qDZRLgC30S0nqmK
01_apoio/cap|||REG-CAP-002_Sessao-Treinamento-Mar2025.docx|||1S4KO93SuNshpOxu3g41TjnZW3HajFBNw
01_apoio/cap|||REG-CAP-009_Reciclagem-Mar2026.docx|||1xgHZsTCrfuBCgwvVfWaSTZGsS3GZ7xiR
01_apoio/cap|||GUIA-CAP-006_MiniManual-ITP.docx|||1dbKffWaDaaHkSpQ6wAuqyJujuyQ7Dkyy
01_apoio/cap|||GUIA-CAP-009_MiniManual-GPC.docx|||1kNivoZ1Wr4QXbjReNplUIfqigeOtJ8_o
01_apoio/cap|||MAT-CAP-013_Trilha-COO-Portfolio.docx|||13YO3MTQBznbYFOc_akFM-UwWdsobodLj
01_apoio/cap|||TPL-CAP-001_Registro-de-Sessao-de-Treinamento.docx|||1CVkEt9LrB9ClXXPqYteGC9NnEgYKoXFe
01_apoio/cap|||REG-CAP-006_Sessao-Gestao-Out2025.docx|||11Nd6v2QxAipLc6gR1WDvH81DS2FfMKox
01_apoio/cap|||MAT-CAP-022_Trilha-Responsavel-Medicao.docx|||1VRdJxBk4wlBQ_-jq7Ue_4DhHQ3PbKjsC
01_apoio/cap|||MAT-CAP-015_Trilha-RH-Pessoas.docx|||1apnEAcH2MS8RsyDsvl5Hqfnz5xkrCXpe
01_apoio/cap|||AVA-CAP-002_Avaliacao-GPR.docx|||13zYWvkkv4II08CrmYt3n0cmDwTCC3AeP
01_apoio/cap|||MAT-CAP-016_Trilha-Tech-Lead-Arquiteto.docx|||1JS4_FKAPYHzz1B65YTGL8uVkSAo0-ad-
01_apoio/cap|||GUIA-CAP-002_MiniManual-REQ.docx|||1wy0aD3f_ffoR5L742FgEMWqlKSj1gt1_
01_apoio/cap|||REG-CAP-004_Sessao-Treinamento-Jan2026.docx|||1jJ7Gjeu_ds4huXMAF7e564NeJBgICJDz
01_apoio/cap|||REG-CAP-002B_Sessao-Reforco-Set2025.docx|||1lOL9e-11IVGVyS4TvsF21Ht325Nl0NAS
01_apoio/cap|||MAT-CAP-014_Trilha-Time-Melhoria-SEPG.docx|||1RkTsNavdx3osAAgqlgFzkTLFIGwkMTBi
01_apoio/cap|||REG-CAP-001B_Sessao-Reforco-Jan2025.docx|||1O-P9xpYwaW_vd1xmsRiwgyP9FQ3j7nCp
01_apoio/cap|||GUIA-CAP-004_MiniManual-VV.docx|||10OrGMaay8ZyWKQQtlPWAIStN2EArM2lX
01_apoio/cap|||GUIA-CAP-003_MiniManual-PCP.docx|||1DCGLP9f5Pho42AMAjWzZn4A73E45bHBH
01_apoio/cap|||MAT-CAP-017_Trilha-PO-PM.docx|||1Nk9RNKlXzfJwijqhfm-wJysHm8et6cBG
01_apoio/cap|||REG-CAP-009_Reciclagem-Mar2026.md|||1X5pxMU4f1oCgfCn65m8SE8bQkPUiYnl8
01_apoio/cap|||REG-CAP-008_Sessao-Tecnico-Fev2026.md|||1FCa5wLWvxiOHu1GJfKqXrdYfvC8mg7MG
01_apoio/cap|||REG-CAP-006_Sessao-Gestao-Out2025.md|||10jW0RgPOO_YOPYdh0MiDkP1r6oAkPiS1
01_apoio/cap|||REG-CAP-007_Sessao-Tecnico-Jan2026.md|||1SthU41muR1B9KQ-AjTzdPy7C7zjAx6St
01_apoio/cap|||REG-CAP-001B_Sessao-Reforco-Jan2025.md|||1ABAnRyZSxwoJObVCP84fEt-N4fXR1bxQ
01_apoio/cap|||REG-CAP-002B_Sessao-Reforco-Set2025.md|||1Ljd3g8eppyULGODYbJzt1962L0O-VoSp
01_apoio/cap|||AVA-CAP-005_Avaliacao-GPC-MED-CAP.md|||1f4ODSbjmha6LhJjT7d86A1HOEnf4Pq0T
01_apoio/cap|||GUIA-CAP-004_MiniManual-VV.md|||1l5pgpbqAvQlIEz6MGdE7qmLi8kJ15eVU
01_apoio/cap|||GUIA-CAP-008_MiniManual-MED.md|||1MJf9WWhQQUdXuXW8VKazxIUzmFVSButZ
01_apoio/cap|||REG-CAP-002_Sessao-Treinamento-Mar2025.md|||1NbodP8vj_SS999XcRiCu4aslfdXw9FAP
01_apoio/cap|||REG-CAP-005_Sessao-Treinamento-Mai2026.md|||11POQMlFp5psX9W4oAWk5J842VZvU83hY
01_apoio/cap|||MAT-CAP-021_Trilha-GCO-Baseline.md|||1dJ_MTeu8qbYjaw50Wbh0c8Eh-ZKGZ-48
01_apoio/cap|||MAT-CAP-018_Trilha-Devs.md|||1Agyekcmbs8jKVYHF930x3mGtdS1b-l0w
01_apoio/cap|||AVA-CAP-002_Avaliacao-GPR.md|||13DugViGDC7m2Xqk-fBxWN2IqvwpSwQnc
01_apoio/cap|||MAT-CAP-014_Trilha-Time-Melhoria-SEPG.md|||1TTaEJ-gZEKxjrSZ4XVrBQgqrRjnoTBeL
01_apoio/cap|||REG-CAP-003_Sessao-Treinamento-Ago2025.md|||1ZKJFrUa_v0JpLre9LLNPti6sLE-qt-sI
01_apoio/cap|||GUIA-CAP-002_MiniManual-REQ.md|||1oVcmJVt3NVuN5MfJL80bJfdXJA7FL_hc
01_apoio/cap|||GUIA-CAP-011_MiniManual-CAP.md|||17ZZI8mUkEkCoRTmXrJe_mY8Qj0kol-N1
01_apoio/cap|||GUIA-CAP-006_MiniManual-ITP.md|||1gAPICKSawMohY7R2radBCHl6OyRZ-oA8
01_apoio/cap|||GUIA-CAP-003_MiniManual-PCP.md|||1APDWRdjS_qW3Zq5bDTRFOVjC3h4DXSZ7
01_apoio/cap|||GUIA-CAP-009_MiniManual-GPC.md|||15s8hqDo_2kh_qrkEqvbBSzSXvOVJa-hI
01_apoio/cap|||MAT-CAP-015_Trilha-RH-Pessoas.md|||1SgEIYvz-cRVmg2aEiwKHdYPJixBAT5fk
01_apoio/cap|||AVA-CAP-004_Avaliacao-GCO-ITP.md|||1JbcegYCdahfdayymHIawCep5N8sEbCqF
01_apoio/cap|||MAT-CAP-016_Trilha-Tech-Lead-Arquiteto.md|||12tV94PVD8CSJO7GBtuiV_wkAX8uhxZQD
01_apoio/cap|||GUIA-CAP-010_MiniManual-OSW.md|||15XAGw1n2P_mXvbGIEvHRGmnJKgbNgKBR
01_apoio/cap|||AVA-CAP-003_Avaliacao-Tecnico-REQ-PCP-VV.md|||1nskpt_7NeBQU76v1SecFt3shK616OHdU
01_apoio/cap|||REG-CAP-004_Sessao-Treinamento-Jan2026.md|||15qmHgk5_9u0ep5Je0R1femPBgim9Wvsw
01_apoio/cap|||REL-CAP-001_Relatorio-de-Eficacia-2025.md|||1bEjNu5MAK6AZSURmLyDRxn2jegRay09J
01_apoio/cap|||MAT-CAP-020_Trilha-QA.md|||13k32H05H8n7d1ZA3BoOeoL1NyXsHKGva
01_apoio/cap|||MAT-CAP-022_Trilha-Responsavel-Medicao.md|||1vL14qqXbQD_Tse191WLvePN5uB2ewpcG
01_apoio/cap|||MAT-CAP-017_Trilha-PO-PM.md|||1a8ORfbTfL6Ic6l8ECE1SiYTM8YUwaszg
01_apoio/cap|||AVA-CAP-001_Avaliacao-Processo-Padrao-Geral.md|||11rB7oDMvWo0GvcL1GhUM824bC85cmAOj
01_apoio/cap|||TPL-CAP-001_Registro-de-Sessao-de-Treinamento.md|||1V6nwWP49ThNknbf0gvVkK19GFRQMZC4l
01_apoio/cap|||GUIA-CAP-005_MiniManual-GCO.md|||1amNy8d4c3vZV__wkBMaIzOeky16bLvcn
01_apoio/cap|||GUIA-CAP-012_MiniManual-AQU.md|||1aS7ue400NH7RXhsiAch-o_IBnooTKg6b
01_apoio/cap|||TPL-CAP-002_Relatorio-de-Eficacia-de-Treinamento.md|||1GHbjdOCqWlo0_K4rnKN-kgJDs-A9aNAI
01_apoio/cap|||GUIA-CAP-001_MiniManual-GPR.md|||1obKGUSvsgBmoAzGF1j5sAjUYz72erOCV
01_apoio/cap|||GUIA-CAP-007_MiniManual-GDE.md|||1csGF1cCc8vi1dA5OlfKCh9q-g3FoMRg5
01_apoio/cap|||REG-CAP-001_Sessao-Treinamento-Dez2024.md|||1enrf4ZAUhttkVPDlVmCyLdbwOwHgJXKy
01_apoio/cap|||MAT-CAP-019_Trilha-DevOps.md|||13xgrU-0Pthp_6P6woHdUfiDyHwpVmb_g
01_apoio/cap|||MAT-CAP-013_Trilha-COO-Portfolio.md|||1ifOoba9-maD6zF6_4fqVJBohKkJFBfIc
01_apoio/cap/curriculos|||CV-Flavio-Fernandes_GQA-Arquitetura.pdf|||1GSQQ2yS_E7-HnE2BFPsf1A-hkq2AVjPd
01_apoio/cap/curriculos|||CV-Karen-Wada_Consultora-Processos.pdf|||1jX6ax9IDMALDHpoTCrcMMerF_nGIGpCr
01_apoio/cap/curriculos|||CV-Silvio-Baroni_SEPG-GPC.pdf|||1rC4NvQveAUCAWQOkNiU8VvlVX2AkTN6i
01_apoio/cap/curriculos|||CV-Caroline-Jenifer_QA.pdf|||1C7vxxTRerQM1J7J344iub0tfSV86ozhc
01_apoio/cap/curriculos|||CV-Wilson-Yamada_Sponsor-Portfolio.pdf|||11gRQH_6m7Eq1ojWkfu6hRK_AqTqY65ak
01_apoio/cap/curriculos|||CV-Cezar-Velazquez_TechLead.pdf|||1Wj_kGQvhXViFApjmjJDfvzUvbSuyqqV3
02_projeto|||PRO-PCP-001_Processo-de-Projeto-e-Construcao-do-Produto.docx|||1PFGeQPHNKcUFMFNIO9lT1CkO9RyUe0CD
02_projeto|||GUIA-GPR-001_Roteiro-de-Kickoff.docx|||1icahhXdwUOXQA3txofLbVmOaFKnbaCxu
02_projeto|||PRO-VV-001_Processo-de-Verificacao-e-Validacao.docx|||1UloaOSeholVwPG1uQTnwaYMCDd_Eqgu7
02_projeto|||PRO-ITP-001_Processo-de-Integracao-do-Produto.docx|||1Ua11xIFEHx4QTKpoKXZd3pFLXrES7OXW
02_projeto|||PRO-GPR-001_Processo-de-Gerencia-de-Projetos.docx|||1k8QAAFCQmb8sJAMKlrR-Pnv6MZqD1Xcy
02_projeto|||PRO-REQ-001_Processo-de-Engenharia-de-Requisitos.docx|||1FE8Ytpu1fUrggTPn7A1hAI2rut4oeRV2
02_projeto|||PRO-GPR-001_Processo-de-Gerencia-de-Projetos.md|||1tuaDp9oFw0sAVv4qe0BgsSPNKD_JgoMn
02_projeto|||PRO-ITP-001_Processo-de-Integracao-do-Produto.md|||1QdieFmzpCLXLGRwy_9QwjFuzKPM_-_03
02_projeto|||PRO-VV-001_Processo-de-Verificacao-e-Validacao.md|||1QFnmCgrpXpIPNqirQS9EwAVR38zDCJE3
02_projeto|||PRO-PCP-001_Processo-de-Projeto-e-Construcao-do-Produto.md|||1D9wE8bol3nzsW802mrEujCEmqDJcaG3K
02_projeto|||PRO-REQ-001_Processo-de-Engenharia-de-Requisitos.md|||1mEmw_8na4H8-Wysz_K51-hNyfMGq7B25
02_projeto|||GUIA-GPR-001_Roteiro-de-Kickoff.md|||1N1YGy0ljWuoaq603HAmFjpJwrF1Yw-Ac
03_templates|||EXEMPLO-GPR-005_Status-Report-Exemplo-Preenchido.md|||1tk09ctAQgOW2xowJIjnVQX9lx_DFpMvi
03_templates|||TPL-GPR-005_Template-Relatorio-de-Acompanhamento.md|||1HUSg5x0hlen1UY4RjPAiWh1a_ETf1RCu
03_templates|||TPL-GPR-001_Template-Plano-de-Projeto.md|||1s74PRIyXyCSuRPi2_yCL3GsYk_N9pR0k
03_templates|||TPL-GPC-001_Template-Registro-de-Verificacao-de-GQA.md|||1TFVY8JIrsAd9K-a52ymx0PvhlA4yUgbE
03_templates|||TPL-GPR-001_Template-Plano-de-Projeto.docx|||1JG7_Er7Cq5FfiS44dfcZlg0dKUwzWetA
03_templates|||TPL-REQ-002_Template-Matriz-de-Rastreabilidade.docx|||1W_0c8aevifCLVgNw8ecK3Djf4ar3Oatj
03_templates|||TPL-VV-002_Template-Registro-de-Revisao-por-Pares.docx|||1dgiWFADcf1hSgfkggK742ZZe0eEzaIcW
03_templates|||TPL-GDE-001_Template-Registro-de-Analise-de-Decisao.docx|||1V2VwWHjezpUNsDIy0eNM31mo0ydqiHa8
03_templates|||TPL-GPR-002_Template-Termo-de-Abertura.docx|||1fw6vq92uHpUuJoVNuHbDPbVFC3gxVEm8
03_templates|||TPL-GPR-006_Template-Change-Request.docx|||1p400uzBBwZpSWLeGNzJlFy_so7UoDURu
03_templates|||TPL-GPR-004_Template-Termo-de-Encerramento.docx|||1LFj2UMUcCD7ewIGlkRdshUo-HmJUMmad
03_templates|||TPL-ITP-001_Template-Estrategia-de-Integracao.docx|||1n3gUvRn54vsEAgZWQeXLxfbAoDoQRzEO
03_templates|||TPL-ORG-001_Template-Ata-de-Reuniao.docx|||1bdb2aarUtu2uLyhgCFVtS3FiyiKb7CF5
03_templates|||TPL-GPC-001_Template-Registro-de-Verificacao-de-GQA.docx|||1vklwYMZeJFJ_hsULzyPPQfHSIBH2sPCG
03_templates|||TPL-VV-001_Template-Plano-de-Verificacao-e-Validacao.docx|||1s0sjWb1MolACQ-3-GQajFDpnilc7kILw
03_templates|||TPL-REQ-001_Template-Documento-de-Requisitos.docx|||1IGz8Jxln6UO_tCFNplT6fcHxq-5KEVB5
03_templates|||TPL-PCP-001_Template-Documento-de-Design.docx|||1MzCnCw8RflPBrznE_xSEWci1LAaCoVLl
03_templates|||TPL-GPR-003_Template-Registro-de-Adaptacao.docx|||17Q9cPXicAvMqAXYPz8ljpb5S2i0NePx_
03_templates|||TPL-GPR-005_Template-Relatorio-de-Acompanhamento.docx|||1U4pFEFtk7OwhzNix2RDuOcvWNT55XJQo
03_templates|||TPL-GPR-002_Template-Termo-de-Abertura.md|||1pvb4FoBeV8cBmdEE7OLmIntCAmxNMD4A
03_templates|||TPL-GPR-006_Template-Change-Request.md|||1HwSihP8liBxJcEfLsgiHgwJZFgulkd_y
03_templates|||TPL-GPR-004_Template-Termo-de-Encerramento.md|||133uiwTw2s2O63F5E-DBBeCh1MmFvOCS9
03_templates|||TPL-GPR-003_Template-Registro-de-Adaptacao.md|||131xkb1wj3ZoJbRgkuNefU8bmLwACM3VD
03_templates|||TPL-ORG-001_Template-Ata-de-Reuniao.md|||1Cufw51GxH3TRru8xL9vDGHiYi8Mmjk6D
03_templates|||TPL-GDE-001_Template-Registro-de-Analise-de-Decisao.md|||1xqVF8ueYmwaKzDsDypX6n0YLy7Qq-6jU
03_templates|||TPL-VV-001_Template-Plano-de-Verificacao-e-Validacao.md|||1QLlkyRwI39PE_ih1Vz-rXkSWnivf4fQb
03_templates|||TPL-ITP-001_Template-Estrategia-de-Integracao.md|||1gTeyMOv_qhfqWZf8J7Se4O9kxJiJDrZO
03_templates|||TPL-PCP-001_Template-Documento-de-Design.md|||1vGR1UiffaWOvicnoU8NpPHhO96NBwbhV
03_templates|||TPL-REQ-001_Template-Documento-de-Requisitos.md|||19Uus1IU9ab_z960ITUxm8xaNluk7_LGz
03_templates|||TPL-REQ-002_Template-Matriz-de-Rastreabilidade.md|||168VucASymzvMt5g-p_F1ZhfwocT5z7Ww
03_templates|||TPL-VV-002_Template-Registro-de-Revisao-por-Pares.md|||1DFf9iA8lOkL7694hyz2x_PV62A_itJoA
04_registros/AASP_CNJ|||RAC-AASPCNJ01-001_Relatorio-de-Acompanhamento.docx|||1G_0Odyq4HbI3nfCyDh7-zZoXDgu_BiON
04_registros/AASP_CNJ|||GCO-AASPCNJ01-001_Registro-de-Configuracao.docx|||1IJozbK4BobNpyION4zPWa_s2auynxhv9
04_registros/AASP_CNJ|||VV-AASPCNJ01-001_Plano-de-VV.md|||1svrQKE2lJHz91RMvgbx21RNEHw60XMoz
04_registros/AASP_CNJ|||GQA-AASPCNJ01-001_Registro-de-GQA.docx|||1AI6TXKQ5f6Oh5g6VmFgzTmXNQHEtLOlh
04_registros/AASP_CNJ|||RASTR-AASPCNJ01-001_Matriz-de-Rastreabilidade.docx|||1lfPyboZZ3hd-8g3IzjQRQciVYXCztgZw
04_registros/AASP_CNJ|||TAP-AASPCNJ01-001_Termo-de-Abertura.md|||1l6PmtiKd-wy4CyjEgbhN3gky-4NRb3lk
04_registros/AASP_CNJ|||PLA-AASPCNJ01-001_Plano-de-Projeto.md|||15UPh6z7b9ZUbUVUBpANR2ow4EsIDxn9Y
04_registros/AASP_CNJ|||PCP-AASPCNJ01-001_Documento-de-Design.md|||1Unza8xmgkJujBYgKw8pg35-61abEm6WL
04_registros/AASP_CNJ|||ATA-AASPCNJ01-001_Ata-Alinhamento-Fluxo-CNJ.md|||1MEhewPJ_pd35kgdky_xETqE3I6XR7zMC
04_registros/AASP_CNJ|||MED-AASPCNJ01-001_Registro-de-Medicao.md|||1uewnWBXzHNoc6W1skfMxGLgrWRS-lGh3
04_registros/AASP_CNJ|||REL-VV-AASPCNJ01-001_Relatorio-de-Execucao-de-Testes.docx|||1whC8gTS2Mz1CW7QajDlOMvfXNlxt5AP6
04_registros/AASP_CNJ|||GEST-AASPCNJ01_Planilha-de-Gestao-do-Projeto.xlsx|||1Vdng-5mBCjlXpajdZ6ScLD67c8e85qob
04_registros/AASP_CNJ|||GDE-AASPCNJ01-001_Registro-de-Analise-de-Decisao.md|||15uYGS_DNz4Dt1mxmx4-PkQB9MUGfjffr
04_registros/AASP_CNJ|||CR-AASPCNJ01-001_Change-Request.md|||1LC7TXf4KqwN2oIEgL4sq74Zhg_eCPYST
04_registros/AASP_CNJ|||00_INDICE-AASPCNJ01_Mapa-de-Registros.md|||1D36lT0gskRVQ2uCke-m0hlrWD_zs6lXk
04_registros/AASP_CNJ|||REV-AASPCNJ01-001_Registro-de-Revisao-por-Pares.md|||1YPUEV8VMC4rLiB6ie182lY_9nRz72wdA
04_registros/AASP_CNJ|||PLA-AASPCNJ01-001_Plano-de-Projeto.docx|||1y9zo8Fx1AewE2z9GVdmhsecKySyDoSf6
04_registros/AASP_CNJ|||RASTR-AASPCNJ01-001_Matriz-de-Rastreabilidade.md|||1iDvjlcbuCL2sr01UQ1vqRONHz0aST6x8
04_registros/AASP_CNJ|||VV-AASPCNJ01-001_Plano-de-VV.docx|||199h316ZoZ43k7W_rnPpNq6GTBr502zuu
04_registros/AASP_CNJ|||CR-AASPCNJ01-001_Change-Request.docx|||1J3XOn56R7ruWa8vhPAnVzI7r092DFLY-
04_registros/AASP_CNJ|||PCP-AASPCNJ01-001_Documento-de-Design.docx|||1ywDtDrM3zHptY2XfL6ut22ra3MEbuLTe
04_registros/AASP_CNJ|||ITP-AASPCNJ01-001_Estrategia-de-Integracao.docx|||1tobpnNoEQf5LarNnPEJAEJnt5BAZGrtQ
04_registros/AASP_CNJ|||REV-AASPCNJ01-001_Registro-de-Revisao-por-Pares.docx|||1PfM9kKAjFJofhtJn5xqgicqG-0-v3mA-
04_registros/AASP_CNJ|||GDE-AASPCNJ01-001_Registro-de-Analise-de-Decisao.docx|||1EpobYWmsjCftVdxosshioK0mCuXVFlEq
04_registros/AASP_CNJ|||ADAP-AASPCNJ01-001_Registro-de-Adaptacao.md|||1AQtE9Q0KvpKNIY8fWtCWUrUCzhlx9iTa
04_registros/AASP_CNJ|||CAP-AASPCNJ01-001_Registro-de-Capacitacao-da-Equipe.md|||1jba7CzH_o_sggKZ6Y8pjjfxXTPwIMjf4
04_registros/AASP_CNJ|||ADAP-AASPCNJ01-001_Registro-de-Adaptacao.docx|||14GFOTJj6jxDsV62h60zCqIgxnRW-DbWW
04_registros/AASP_CNJ|||CAP-AASPCNJ01-001_Registro-de-Capacitacao-da-Equipe.docx|||11db2exVuX-huVhgL8azaDzByfMFQv_pb
04_registros/AASP_CNJ|||MED-AASPCNJ01-001_Registro-de-Medicao.docx|||1ePiJ3ONIXZf2gN00FzXuyUCIXdrpezsx
04_registros/AASP_CNJ|||GCO-AASPCNJ01-001_Registro-de-Configuracao.md|||1Dolv6F6w1b-HrjYBemHVis-JZjL3-vJR
04_registros/AASP_CNJ|||ATA-AASPCNJ01-001_Ata-Alinhamento-Fluxo-CNJ.docx|||12sOcC6FDaP-3OdoM1_duAMNNcbgYsQvb
04_registros/AASP_CNJ|||TAP-AASPCNJ01-001_Termo-de-Abertura.docx|||1hKBUW2dTTfmd8PEs36tEuIQjsKjPAuRF
04_registros/AASP_CNJ|||REQ-AASPCNJ01-001_Documento-de-Requisitos.md|||1YFHxBJU-mxG2nTGtwGVL2EGqDw6MYkcV
04_registros/AASP_CNJ|||RAC-AASPCNJ01-001_Relatorio-de-Acompanhamento.md|||16scQtbSvdpQbF0OS7KCRBRDLBpLI6gt7
04_registros/AASP_CNJ|||REQ-AASPCNJ01-001_Documento-de-Requisitos.docx|||1GDwHhtK1Nc-2AptWo8HIryVHeOF8hzj5
04_registros/AASP_CNJ|||GQA-AASPCNJ01-001_Registro-de-GQA.md|||1aYLuwSN8gKUIFpg3W53cgZGHwjUDmpb7
04_registros/AASP_CNJ|||REL-VV-AASPCNJ01-001_Relatorio-de-Execucao-de-Testes.md|||1UECG0sMcEQrEyTkMtTW2vDyOGYuPYlov
04_registros/AASP_CNJ|||ITP-AASPCNJ01-001_Estrategia-de-Integracao.md|||1cnLnAHipePGdvP26u1bQqQNAGlLCQ_LC
04_registros/PROFARMA_Cadastro-de-Clientes|||ADAP-PROFARMA01-001_Registro-de-Adaptacao.docx|||1aRgkciq4Ed3iPJgEbe1jJnpkXKlF4Tma
04_registros/PROFARMA_Cadastro-de-Clientes|||ADAP-PROFARMA01-001_Registro-de-Adaptacao.md|||1qa1eP5ZefDj1uNO-X1akjz55I4ZqmCOn
04_registros/PROFARMA_Cadastro-de-Clientes|||PCP-PROFARMA01-001_Documento-de-Design.md|||1xz3lOI7tT1T9MaUytvzP3u2djp_-VSll
04_registros/PROFARMA_Cadastro-de-Clientes|||LI-PROFARMA01-001_Licoes-Aprendidas.md|||1iG2LYXClAx5nZ4zuk_S74DvZ1Q0LMHQ_
04_registros/PROFARMA_Cadastro-de-Clientes|||VV-PROFARMA01-001_Plano-de-VV.md|||1pFat-uajlAcSBqyMC8Xr5TIDMOz5Yqa1
04_registros/PROFARMA_Cadastro-de-Clientes|||PLA-PROFARMA01-001_Plano-de-Projeto.md|||1UiPpMmAewO-ZAlFVC7Wgy3mUVTqk8KTG
04_registros/PROFARMA_Cadastro-de-Clientes|||MED-PROFARMA01-001_Registro-de-Medicao.md|||1QDJ9-TSu_9GDbyhDRN6ywUgTeuAJ4QiH
04_registros/PROFARMA_Cadastro-de-Clientes|||GQA-PROFARMA01-001_Registro-de-GQA.md|||1ejtinVxoovxalMob3EU5LzijUCO0eo0V
04_registros/PROFARMA_Cadastro-de-Clientes|||PLA-PROFARMA01-001_Plano-de-Projeto.docx|||189Kp-xA8BJ3SsO9NhxDyDOUtX3dADifK
04_registros/PROFARMA_Cadastro-de-Clientes|||LI-PROFARMA01-001_Licoes-Aprendidas.docx|||1NMayhfr_e6Li-R0NEGoST5QATJgifMc7
04_registros/PROFARMA_Cadastro-de-Clientes|||REQ-PROFARMA01-001_Documento-de-Requisitos.md|||1T0waKCjFQoXryc5x292hRhOggesgV4Pt
04_registros/PROFARMA_Cadastro-de-Clientes|||REQ-PROFARMA01-001_Documento-de-Requisitos.docx|||17OE2PW4XkEy3OnJlSb6rtsHHh9ouTFJE
04_registros/PROFARMA_Cadastro-de-Clientes|||MED-PROFARMA01-001_Registro-de-Medicao.docx|||1nmbiWfvYMAAa7Y5pO14VxaZgxEPQuKOn
04_registros/PROFARMA_Cadastro-de-Clientes|||GEST-PROFARMA01_Planilha-de-Gestao-do-Projeto.xlsx|||12SEFOVCAA1jVQRgM1c1RDR_CL3KaW32_
04_registros/PROFARMA_Cadastro-de-Clientes|||CR-PROFARMA01-001_Registro-de-Change-Requests.docx|||1XWRRoeJ6NnvjCG3S0hlyPyxnMfkf9vM7
04_registros/PROFARMA_Cadastro-de-Clientes|||CR-PROFARMA01-001_Registro-de-Change-Requests.md|||1kgckhl0v57S7-e70hCKJB6Eo8eW2gT1y
04_registros/PROFARMA_Cadastro-de-Clientes|||ITP-PROFARMA01-001_Estrategia-de-Integracao.docx|||1DKKcqAZK78dkV2UIRRSXHtELjnxdw4aj
04_registros/PROFARMA_Cadastro-de-Clientes|||GCO-PROFARMA01-001_Registro-de-Gerencia-de-Configuracao.docx|||1ld1PXP0yafu0eW7nUNXN0iRCm1P7cskc
04_registros/PROFARMA_Cadastro-de-Clientes|||RASTR-PROFARMA01-001_Matriz-de-Rastreabilidade.docx|||1ep0JvVMNhdLVRwWXVMIyfLxurd7ReAyI
04_registros/PROFARMA_Cadastro-de-Clientes|||GQA-PROFARMA01-001_Registro-de-GQA.docx|||1hefq-kmdiYVOIvc0RoWHcSVQDBbL8Fq4
04_registros/PROFARMA_Cadastro-de-Clientes|||ATA-PROFARMA01-001_Ata-de-Kickoff.docx|||1uNkVDge5WAgwLTCcUFZmBLlqKog16nmG
04_registros/PROFARMA_Cadastro-de-Clientes|||RAC-PROFARMA01-001_Relatorio-de-Acompanhamento.docx|||1HjCxyFwvC7Fxp4OXwxjqqL7OyYlSfI9x
04_registros/PROFARMA_Cadastro-de-Clientes|||REV-PROFARMA01-001_Registro-de-Revisao-Tecnica.docx|||1dHd-EpgVX2Mg2Wo5Y_uxB8KFH4qphhxM
04_registros/PROFARMA_Cadastro-de-Clientes|||TAP-PROFARMA01-001_Termo-de-Abertura.docx|||13BKbRnLmlBDMBkioH54vOpmicKqlei8W
04_registros/PROFARMA_Cadastro-de-Clientes|||PCP-PROFARMA01-001_Documento-de-Design.docx|||1t0fD748MR_EBRMHsgQzVGLKRnJ4Zq7__
04_registros/PROFARMA_Cadastro-de-Clientes|||CTQ-PROFARMA01-001_Cenarios-de-Teste-Homologacao.docx|||1ts70FWbIasG3sf9qDBSw8cXldJfRJ7bY
04_registros/PROFARMA_Cadastro-de-Clientes|||VV-PROFARMA01-001_Plano-de-VV.docx|||15tRkpsMad47tD4gPdlLKImY5ipIadjxw
04_registros/PROFARMA_Cadastro-de-Clientes|||TAE-PROFARMA01-001_Termo-de-Encerramento.docx|||1k_UZ_jWRVmpHA1Iiysa7vKvUwQ1T8QED
04_registros/PROFARMA_Cadastro-de-Clientes|||REL-VV-PROFARMA01-001_Relatorio-de-Execucao-de-Testes.docx|||1KF8zj0lufb0VPg6riJwGhibojJJIopHM
04_registros/PROFARMA_Cadastro-de-Clientes|||ATA-PROFARMA01-002_Ata-de-Aceite-Final.docx|||1odIVE62I5L7iqqLFUCACbHt3w2HRB8yR
04_registros/PROFARMA_Cadastro-de-Clientes|||GDE-PROFARMA01-001_Registro-de-Analise-de-Decisao.docx|||1wU_hxVhwrX-XUT1OQmEKxw80Mz0T5Rat
04_registros/PROFARMA_Cadastro-de-Clientes|||CTQ-PROFARMA01-001_Cenarios-de-Teste-Homologacao.md|||16ZD1X77Pqc4pDhauwVkg0ioDD6nVFAmy
04_registros/PROFARMA_Cadastro-de-Clientes|||GCO-PROFARMA01-001_Registro-de-Gerencia-de-Configuracao.md|||1Sa_Vs1t1DTIcQX0MLGesk4T6YVBc-Rlk
04_registros/PROFARMA_Cadastro-de-Clientes|||ITP-PROFARMA01-001_Estrategia-de-Integracao.md|||1hbMF9jFqMlJF3soSLRNy6LTp11g408Pn
04_registros/PROFARMA_Cadastro-de-Clientes|||REL-VV-PROFARMA01-001_Relatorio-de-Execucao-de-Testes.md|||1-GrCtAPUfBcRFM4tMJfIEAO-o_cvFqOt
04_registros/PROFARMA_Cadastro-de-Clientes|||ATA-PROFARMA01-002_Ata-de-Aceite-Final.md|||1fb6iusuVg05dDsai8VJhfW4ZxA-qpnxZ
04_registros/PROFARMA_Cadastro-de-Clientes|||TAE-PROFARMA01-001_Termo-de-Encerramento.md|||1G8wrZkaa7n3kidURBXK6tUzzupMHpeyb
04_registros/PROFARMA_Cadastro-de-Clientes|||GDE-PROFARMA01-001_Registro-de-Analise-de-Decisao.md|||1Fn6AEOrG_9rfsHc5rb-55Ba6AJXD-oqJ
04_registros/PROFARMA_Cadastro-de-Clientes|||ATA-PROFARMA01-001_Ata-de-Kickoff.md|||1lUV0rrT2F--Db0coxhXjcOre7lWH4HOU
04_registros/PROFARMA_Cadastro-de-Clientes|||REV-PROFARMA01-001_Registro-de-Revisao-Tecnica.md|||1oPm581spQso7WLZsNUHItMYAVQGqD6Qq
04_registros/PROFARMA_Cadastro-de-Clientes|||TAP-PROFARMA01-001_Termo-de-Abertura.md|||1EViPFMzb6dgDVBr-wLeSrGXIJB25-2v2
04_registros/PROFARMA_Cadastro-de-Clientes|||RASTR-PROFARMA01-001_Matriz-de-Rastreabilidade.md|||1TChhbQ3yhiT2-Q5VN8cbxtuO2C65slPV
04_registros/PROFARMA_Cadastro-de-Clientes|||RAC-PROFARMA01-001_Relatorio-de-Acompanhamento.md|||1WKuyyC2s6ukY52aDxjmqfD6w2L5l_GRn
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ADAP-GASMIG02-002_Registro-de-Adaptacao-OS002.docx|||1oQshhvn5DIq1DoB3rybc8jEbP_OdEnfn
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ADAP-GASMIG02-001_Registro-de-Adaptacao.docx|||1uDnjyU3hDOdzbVZPUFA-1PGqXCsuDeS7
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ADAP-GASMIG02-002_Registro-de-Adaptacao-OS002.md|||1Yi_n_zxaS-YAOGbQ8gg16RdRtmvKn6CA
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ADAP-GASMIG02-001_Registro-de-Adaptacao.md|||1bejNoYCCCfk5qhr7XWZz2N5g8q3KPhCD
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||VV-GASMIG02-002_Plano-de-VV-OS002.md|||1hDwgWy26ua7WcoidKXwkRKdPA3f8SgHB
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||PLA-GASMIG02-001_Plano-de-Projeto.md|||1q5NeTQRiY7BnnB2UiWdcG_ggbMB_Oigy
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||CAP-GASMIG02-001_Registro-de-Capacitacao-da-Equipe.md|||1S5Rvx0kYOz7QPQDU_BA3SpNA1xdAk8Fa
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||GDE-GASMIG02-001_Registro-de-Analise-de-Decisao.md|||15jlfJFiL4Kw0-bg2ZZcKnt7eKmay43k5
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||GQA-GASMIG02-001_Registro-de-GQA.md|||1uDY2HGSwfZRlYwyZ5zGbGQ_290rYm_Xd
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||PLA-GASMIG02-002_Plano-de-Projeto-OS002.md|||1OQok5rhtLilsAl3lboUjxAeWoRCa6SXA
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||VV-GASMIG02-001_Plano-de-VV.md|||1u0GkYIZ3U_T3KbW9zDIyrX41XWlzafgu
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||MED-GASMIG02-001_Registro-de-Medicao.md|||1yRECVQiPUAD3E8A6sSqcIjuCWsGJFOnN
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||PLA-GASMIG02-002_Plano-de-Projeto-OS002.docx|||1jfUDk7bhCtOXUYDcBnpjOx8FARp2VqPH
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||LI-GASMIG02-001_Licoes-Aprendidas.docx|||1ra9yyJuVYa2tmQW0DKwbJgannxAI2W0E
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||PLA-GASMIG02-001_Plano-de-Projeto.docx|||1ZIwX-h0RDNJfhO5AXev2vqhYrGHOr2qf
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||LI-GASMIG02-001_Licoes-Aprendidas.md|||1jn56o4n7EISf_OPXoT7W91T_SeJSteQA
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ATA-GASMIG02-003_Apresentacao-Entrega-OS002.docx|||1YCW3PFHS2p1bh8O6VWyZ8y2NFoG6ZWFN
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||VV-GASMIG02-001_Plano-de-VV.docx|||15t1yh5oMbpFZ47rREDx9kJPgS8oXyRmy
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||MED-GASMIG02-001_Registro-de-Medicao.docx|||1LtjN_WSjn_g1wQ_RRLe4Z4KP6Cnu-Ohx
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||RAC-GASMIG02-001_Relatorio-de-Acompanhamento.docx|||1bAl8o8UPkTb1AHypGNvRxEJG8UYswpvS
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||GQA-GASMIG02-001_Registro-de-GQA.docx|||1V-T1g_9AKu9TLFPROMR0fA1gkyx180a-
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||VV-GASMIG02-002_Plano-de-VV-OS002.docx|||18GgauiJykVy8AASSKtJcqkt2FR-6AuRv
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||GEST-GASMIG02_Planilha-de-Gestao-do-Projeto.xlsx|||1r_dSFP9AmEnj79FkmqU80OkuYWnwzfZS
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||TAE-GASMIG02-002_Termo-de-Encerramento-OS002.docx|||1-zvT45vPsVTAwmcEzQVak8qKT4dnQWEr
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||RAC-GASMIG02-001_Relatorio-de-Acompanhamento.md|||18grlbdgF-XIQJtb8UNmCvJ25UOqHWb9b
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||TAE-GASMIG02-002_Termo-de-Encerramento-OS002.md|||1Gvd3sqaF500esvT_KQXRRYQOKtSLBa1f
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ATA-GASMIG02-003_Apresentacao-Entrega-OS002.md|||1Un3zSWdjWObqjJfrr8dwWvNnHDKNzuMk
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||GCO-GASMIG02-001_Gerencia-de-Configuracao.docx|||1qpIzDVbsmVYkiXW9NNdciOuv5iovMNu4
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||GCO-GASMIG02-001_Gerencia-de-Configuracao.md|||193BAen9QIQt12KAzqakGH_bNUvMEdxpj
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ITP-GASMIG02-002_Estrategia-de-Integracao-OS002.docx|||1JIAbQHVpTSO3V0AKGnWyVwEs6zuTWX7R
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ITP-GASMIG02-002_Estrategia-de-Integracao-OS002.md|||15xAI-a66USbhl_h-DlQ4iWYBif6a4NYy
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||RASTR-GASMIG02-001_Matriz-de-Rastreabilidade.docx|||1_delTbo-PEeRpuGGGagv5p2SOF-ZNRos
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||RASTR-GASMIG02-002_Matriz-de-Rastreabilidade-OS002.docx|||1tfy9oNEOsThCKNb1YrvQq8Ll1jX9kYJO
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||REQ-GASMIG02-001_Documento-de-Requisitos.docx|||13duq0igfGKvJAHKh_sD9TN7WqTpuOfdn
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||REV-GASMIG02-001_Registro-de-Verificacao-Tecnica.docx|||1biHfNjSf_g7hnUcjBATCG48aG7ARNvRL
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ATA-GASMIG02-001_Ata-de-Kickoff.docx|||1XcstqfQTQC0cm8wZgfc9oLgjSknU6Ueq
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ATA-GASMIG02-002_Ata-de-Aceite-OS001.docx|||1CcRbEbIcDWeHO7sOznH_FcuK-uVVusM0
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||PCP-GASMIG02-001_Documento-de-Design.docx|||1YI-40O6IWGMB0C_R6ytpbxc2w1E7W4fF
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||TAE-GASMIG02-001_Termo-de-Encerramento-OS001.docx|||1mw7eJBj6HANyIYJ1MgxEnO59ML9sl5aa
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||TAP-GASMIG02-002_Termo-de-Abertura-OS002.docx|||1cMUOhgzZzj6wwWIijFMDugRVZIl8aPvf
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||TAP-GASMIG02-001_Termo-de-Abertura.docx|||1WW3VNRafS44JkZiXK29Rm7bYI7NbP9rS
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||CAP-GASMIG02-001_Registro-de-Capacitacao-da-Equipe.docx|||1ibleg7tRQDHfYp3ahRpAlbYjKetFDzzT
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||REQ-GASMIG02-002_Documento-de-Requisitos-OS002.docx|||1_yN7yHPBc9iKilAlxd4pxj52G1_WoCHP
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||GDE-GASMIG02-001_Registro-de-Analise-de-Decisao.docx|||1sqAtX-R1-EjASMtMCnp_fjiessTaSaQU
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||PCP-GASMIG02-002_Documento-de-Design-OS002.docx|||1Q4M2R4uqiy81BP8L3HiQ_idRqmpMt8Cw
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||REQ-GASMIG02-001_Documento-de-Requisitos.md|||1qU0dScZMsyE9b5u1RENM0M85uevSdmrL
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||REV-GASMIG02-001_Registro-de-Verificacao-Tecnica.md|||1uDopfyiOr-PKrdBbesatAYkF1YOgH1g6
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||TAP-GASMIG02-001_Termo-de-Abertura.md|||1X37fcpWgIcSM5LirpbU23geQekmjCp_i
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||PCP-GASMIG02-001_Documento-de-Design.md|||1rRXvNXOxYx1RmwJPihw-IlOEnMHL3LPi
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ATA-GASMIG02-001_Ata-de-Kickoff.md|||173I8V-9u9y4GjYm6CqXrqhL5_XLf0-Tx
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||TAP-GASMIG02-002_Termo-de-Abertura-OS002.md|||1EDT02kT9MVQV0gWPgpmAcCbVHa8T5GH8
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||RASTR-GASMIG02-002_Matriz-de-Rastreabilidade-OS002.md|||1WiIbZeuVyYE2ZPrnLjkoiqVH3_8Y3Igz
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||REQ-GASMIG02-002_Documento-de-Requisitos-OS002.md|||1tyw98Wg84EnhfdKkHSJw6IoGaXSZ6JgK
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||ATA-GASMIG02-002_Ata-de-Aceite-OS001.md|||1SMbROaSFGiRfxwoXqmEw9SWLkqJ0nZYZ
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||RASTR-GASMIG02-001_Matriz-de-Rastreabilidade.md|||1s5eS3sxpXkZh0TY8Ws0nl6jo8CRWPWyi
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||PCP-GASMIG02-002_Documento-de-Design-OS002.md|||1jR60AUVUBrZqmoZx6a1AKAAmbEdEUR0V
04_registros/FTGASMIG_Governanca-APIs/GASMIG02_Fundacao-Tecnologica|||TAE-GASMIG02-001_Termo-de-Encerramento-OS001.md|||16Tvn5wYajcpGwNyPouZCvoJWXDedha5s
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ADAP-FRUKI01-002_Registro-de-Adaptacao-PacoteFinal24.docx|||1LNzyoQkTM7oLgWtSCPY6VxNqt4JS_MzM
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ADAP-FRUKI01-001_Registro-de-Adaptacao.docx|||1NaEJlUDHw0FE6fgH28gpifHft7ZLxUyL
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ADAP-FRUKI01-002_Registro-de-Adaptacao-PacoteFinal24.md|||1JDPNC85L1TdEuweMvEmJphAH00Y8VbT0
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ADAP-FRUKI01-001_Registro-de-Adaptacao.md|||1jd-ueS7tJ7ipM9MvSxY0E9QI04RMOAxj
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||GCO-FRUKI01-001_Registro-de-Configuracao.md|||19M3LWTGKSzJ_rDQJfGF5sSg2Stj4ooYw
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||GQA-FRUKI01-001_Registro-de-GQA.md|||1LQg4Ts7Gp-dH1rHTCtPzOWBXODTb-xB0
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||PLA-FRUKI01-002_Plano-de-Projeto-PacoteFinal24.md|||1s4eNRbcYfsKtdn4cleCJkIN9t2cJAjGI
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||RAC-FRUKI01-002_Relatorio-de-Acompanhamento-Pacote1.md|||1o6AlWFp1nR1m5JRHVda54B19LaoFoMPO
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-008_Ata-Kickoff-PacoteFinal24.md|||1RNsmRLVuhzH7B7xEow8TR1epFtoTJuTG
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||PLA-FRUKI01-001_Plano-de-Projeto.md|||1ak4cVI3YUmLkRgLKhcjIooEnGCJzS8J8
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||TAE-FRUKI01-002_Termo-de-Encerramento-PacoteFinal24.docx|||1D3T0RHrOPhOq08Edxc1fWW-cZ1uR-e2n
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||MED-FRUKI01-001_Registro-de-Medicao.docx|||1D6gCK_SBP31WdmYGToQH2iCZV1RdzhWI
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||RASTR-FRUKI01-002_Matriz-de-Rastreabilidade-PacoteFinal24.docx|||1S4nR_PkZnGQrm6ppWv47ftgH2ptyG9xJ
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||TAE-FRUKI01-001_Termo-de-Encerramento.docx|||1JNvLtWIaqno7WXqzPfQwcK1bRE3UjCRv
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-002_Ata-Levantamento-Metas.docx|||1cypxWHL-NU9CPnLV47N-bKnP0QrSIB17
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ITP-FRUKI01-001_Estrategia-de-Integracao.docx|||19YCw05XWIRh-NaI5GWf1c-MF6m5AhIra
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||PLA-FRUKI01-001_Plano-de-Projeto.docx|||1WEPaZNg7rxj29B48l_scz7x7CyLlvoSf
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||GCO-FRUKI01-001_Registro-de-Configuracao.docx|||1fMcui7ebx_4af41JtRltlCCJzDWkd1eA
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-005_Ata-Validacao-Sprint2-RegraDeOuro.docx|||1VmGwsZK4GLu_zpzmrHnD2XOChsiR1GZr
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||REQ-FRUKI01-002_Documento-de-Requisitos-PacoteFinal24.docx|||1GexOXykQE4rnKFPmeW1kVQac18vsnlnQ
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||VV-FRUKI01-001_Plano-VeV.docx|||1yCFY98oM8rlf44HUIeERib4_7jtYsKeU
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-001_Ata-de-Kickoff.docx|||1pjAXblbrxR8Y6p5eq2BDYRBpiYlK3Ag_
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||PLA-FRUKI01-002_Plano-de-Projeto-PacoteFinal24.docx|||1d0l6IhtfbI9hE0UYxQm6nVq9grpjKnpn
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ITP-FRUKI01-002_Estrategia-de-Integracao-PacoteFinal24.docx|||1A-6S0ZZmHteTzIjSNP46H2OJYgeI-Gc7
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||PCP-FRUKI01-001_Documento-de-Design.docx|||1ff6Ha1FH1T1XAJGnmdy2QvkrqXxCUg2s
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||CR-FRUKI01-001_Solicitacao-de-Mudanca-RegraDeOuro.docx|||1z2TIuyQQTiU7fOKmK0kQfziTtE8NqiLc
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||GQA-FRUKI01-001_Registro-de-GQA.docx|||1jmdev8ggRDsbM_CrkMQY_oKaImvKG4vM
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||TAP-FRUKI01-002_Termo-de-Abertura-PacoteFinal24.docx|||1UUmn_lYKBv8eG5UZBaLipFbSMdnYTxgU
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-003_Ata-de-Aceite-Final.docx|||1m0odZUeHy212r9AQwyZ_sfwXzznT4oqJ
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||REQ-FRUKI01-001_Documento-de-Requisitos.docx|||1mCQ9GroaEFEjulblg31P0Kdknw95w8LJ
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||LI-FRUKI01-001_Licoes-Aprendidas.docx|||1pXvWCErdbUdvvAcXV93935DeGW6bJ7xL
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||RAC-FRUKI01-001_Relatorio-de-Acompanhamento.docx|||1_C3hZUp-7-2ldAa2BmIfZ3tMfa9WX0bd
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-007_Ata-Piloto-Pacote1.docx|||1bNAl7ljD0PhTyZEb-2ngdIbBzCpvNY2q
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||VV-FRUKI01-002_Plano-VeV-PacoteFinal24.docx|||1d_okleyBKoPtPW2zEy7300KiXoWL62oj
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-004_Ata-Validacao-Sprint1-NaoAlocados.docx|||10Qo6yB8nqAQmzacMbuLZaVv1ZaX178Lt
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||PCP-FRUKI01-002_Documento-de-Design-PacoteFinal24.docx|||17KodAvypysQkbqocfQIrlE2q1dfRIUnY
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||RASTR-FRUKI01-001_Matriz-de-Rastreabilidade.docx|||1SokajsndvgCtPAX7FyUpNp9mIDxQrVQf
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||GDE-FRUKI01-001_Registro-de-Decisao.docx|||1h8FKsNP59PnO8tzm2WEJ_vgsZYRSmjwX
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||TAP-FRUKI01-001_Termo-de-Abertura.docx|||1ehO_9gQoPrLS-Ykhxfnnsrn9KZ9o8zdH
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-006_Ata-Validacao-Sprint3-PDV.docx|||1ujgsYTHnAVE_J60APn-OqGSRaCTbfPHf
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||RAC-FRUKI01-002_Planilha-de-Gestao-do-Projeto.xlsx|||1RsktvVNbrH1f-RmcV3_AmIu3uJt9Q7sH
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||CR-FRUKI01-001_Solicitacao-de-Mudanca-RegraDeOuro.md|||18ut_8KPcueRiLUgl0CPLPR-G2vvZPtx3
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||TAE-FRUKI01-002_Termo-de-Encerramento-PacoteFinal24.md|||1TJpNI9gAt8nH0qi87whhkajt8msTG1TO
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||TAP-FRUKI01-002_Termo-de-Abertura-PacoteFinal24.md|||1q0Jciu5Wzc6Zn7-k55piZ2OS7Ty4gw71
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-003_Ata-de-Aceite-Final.md|||1Qk8B-Ny6zACkDanQ0QBsqznIzvzIX3xd
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||REQ-FRUKI01-001_Documento-de-Requisitos.md|||1m-7E7kW4OvRkUWA6EpO3BFveXiLIVHOF
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||VV-FRUKI01-001_Plano-VeV.md|||1ZtSNIU4pURtj7fcqmo-Ze_PUgT8Xd8qS
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||REQ-FRUKI01-002_Documento-de-Requisitos-PacoteFinal24.md|||1QSxYq6k8W1KxoVcr90P_31Xzmbb5uN5x
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||PCP-FRUKI01-002_Documento-de-Design-PacoteFinal24.md|||1OSDTx1gAc6_yJw_cN8rhwy4doQynXsws
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||TAP-FRUKI01-001_Termo-de-Abertura.md|||14-7t7EZ-5YdrL7xVn6VgTR75jDcQ9EW_
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-007_Ata-Piloto-Pacote1.md|||1RmwGe1-htZ1eswLCBIdw6KiYYnUMyFz7
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||RASTR-FRUKI01-001_Matriz-de-Rastreabilidade.md|||1ezQXGXqPC-2UMfRdDvudgmasO6TMO5n8
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-005_Ata-Validacao-Sprint2-RegraDeOuro.md|||1fL2lzK5ltJRAvrvBkZRGzHxNEI9xu5Bw
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||LI-FRUKI01-001_Licoes-Aprendidas.md|||1-LL6sPo2lPFF-5U-rT-v0w15M_USlgul
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-006_Ata-Validacao-Sprint3-PDV.md|||18EWiPMrnjSsiQaE_8C28PSBqL_lgVLlm
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-002_Ata-Levantamento-Metas.md|||1ficMpIGp18dxZ3mASn0bnpOcFIF6IkM5
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ITP-FRUKI01-002_Estrategia-de-Integracao-PacoteFinal24.md|||1u4DcmW9hpA01pW7nlBsxOxkvs7OFFkAX
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-004_Ata-Validacao-Sprint1-NaoAlocados.md|||1rfeMludEbjF7UISCTitVTklQgOVogPet
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||PCP-FRUKI01-001_Documento-de-Design.md|||1ZdDvNKE7Q1pA5rx5QPnYLd9FQHaqq-W8
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATA-FRUKI01-001_Ata-de-Kickoff.md|||15oaq3TW916Xz4agaxLeZq1-WTml1R5YU
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||TAE-FRUKI01-001_Termo-de-Encerramento.md|||1CWoASfmkMEYq_njAEpXGu_vwEjx7pAEn
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ITP-FRUKI01-001_Estrategia-de-Integracao.md|||1V-b-qbGgRW_GmmllG836nIib4F-1bxmQ
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||RAC-FRUKI01-001_Relatorio-de-Acompanhamento.md|||13Yx9B8mhKozIn9UHPmgI25DWFBsOfqD8
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||RASTR-FRUKI01-002_Matriz-de-Rastreabilidade-PacoteFinal24.md|||1s3__jTdqb1JrJQw3l9DS-tzsy28cYC2k
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||MED-FRUKI01-001_Registro-de-Medicao.md|||1VXH2Vf2-E0ExrU0D-meV5m2J1TU5rnT3
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||GDE-FRUKI01-001_Registro-de-Decisao.md|||1y8vwxSDf1lQ_dMEoGp96MINftpHX1yzj
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||VV-FRUKI01-002_Plano-VeV-PacoteFinal24.md|||1ifZ0yJp1bIsYSQtVRi9gIzDztsm9Uj3c
05_capacidade|||MAPA-ORG-001_Matriz-de-Papeis-e-Responsabilidades.docx|||16fsO_4U6QBJxV0HSWpFJsHX-XQ4HhLhT
05_capacidade|||MAPA-ORG-001_Matriz-de-Papeis-e-Responsabilidades.xlsx|||14kYNYwEsp3nawnEA9t25kWyYey51aYlu
05_capacidade|||MAPA-ORG-001_Matriz-de-Papeis-e-Responsabilidades.md|||1NHV3d4WHuUhUcTOtjtGi-uB1yR3BC6mL
05_capacidade|||MAPA-CAP-001_Mapa-de-Capacidade-dos-Processos.docx|||1YaGYkBQnoCkiO6AygwtZCQKSxZkMIRNU
05_capacidade|||MAPA-CAP-001_Mapa-de-Capacidade-dos-Processos.md|||1Cf81NchDsh8A185sbhMAt1NJTCks3snY
01_apoio|||REGMED001_RepositorioOrganizacionaldeMedicao.docx|||1FOAiyoGlyqXioyDAXV4gCyqsJZvaJ1aB
04_registros/FTFRUKI_SuperApp-Forca-de-Vendas|||ATAFRUKI01008_AtaKickoffPacoteFinal24.docx|||11alVpwlnsPjgd1_PO4OzMBXeJLRz6PXi
03_templates|||EXEMPLOGPR005_StatusReportExemploPreenchido.docx|||1xdb1hYORBdN9jrAxuuqEunXIoDzptTBH
04_registros/AASP_CNJ|||00_INDICEAASPCNJ01_MapadeRegistros.docx|||1kf3EdS_AsVImdD6P_03zCt-OF7_UHj6N
"""

def main():
    out_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rows = []
    seen_ids = {}
    seen_pathname = {}
    dup_ids = []
    dup_names = []
    for raw in DATA.strip().splitlines():
        raw = raw.strip()
        if not raw:
            continue
        pasta, nome, fid = raw.split("|||")
        ext = nome.rsplit(".", 1)[-1].lower() if "." in nome else ""
        link = LINK_TPL.format(id=fid)
        rows.append((pasta, nome, ext, link, fid))
        if fid in seen_ids:
            dup_ids.append((fid, nome, seen_ids[fid]))
        else:
            seen_ids[fid] = nome
        key = (pasta, nome)
        if key in seen_pathname:
            dup_names.append(key)
        else:
            seen_pathname[key] = True

    # ordena por pasta e depois por nome do documento
    rows.sort(key=lambda r: (r[0], r[1]))

    csv_path = os.path.join(out_dir, "MAPA-DRIVE_Indice-de-Links.csv")
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Pasta", "Documento", "Tipo", "Link"])
        for pasta, nome, ext, link, fid in rows:
            w.writerow([pasta, nome, ext, link])

    # tenta gerar xlsx
    xlsx_ok = False
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font
        wb = Workbook()
        ws = wb.active
        ws.title = "Mapa de Links Drive"
        ws.append(["Pasta", "Documento", "Tipo", "Link"])
        for c in ws[1]:
            c.font = Font(bold=True)
        for pasta, nome, ext, link, fid in rows:
            ws.append([pasta, nome, ext, link])
            cell = ws.cell(row=ws.max_row, column=4)
            cell.hyperlink = link
            cell.font = Font(color="0563C1", underline="single")
        widths = {"A": 60, "B": 60, "C": 8, "D": 70}
        for col, wd in widths.items():
            ws.column_dimensions[col].width = wd
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = "A1:D%d" % (len(rows) + 1)
        xlsx_path = os.path.join(out_dir, "MAPA-DRIVE_Indice-de-Links.xlsx")
        wb.save(xlsx_path)
        xlsx_ok = True
    except Exception as e:
        xlsx_path = None
        print("[aviso] xlsx nao gerado (%s)" % e, file=sys.stderr)

    # resumo
    from collections import Counter, defaultdict
    by_ext = Counter(r[2] for r in rows)
    by_folder = Counter(r[0] for r in rows)
    by_folder_docx = defaultdict(int)
    for r in rows:
        if r[2] == "docx":
            by_folder_docx[r[0]] += 1

    print("=" * 72)
    print("MAPA DE LINKS — ACERVO OFICIAL TIMEWARE (Docs oficial Timeware)")
    print("=" * 72)
    print("Total de arquivos mapeados: %d" % len(rows))
    print("IDs unicos: %d" % len(seen_ids))
    print()
    print("Por tipo:")
    for ext, n in sorted(by_ext.items(), key=lambda x: (-x[1], x[0])):
        print("  %-6s %d" % (ext or "(sem)", n))
    print()
    print("Por pasta (total / docx):")
    for folder in sorted(by_folder):
        print("  %-70s %3d / %3d docx" % (folder, by_folder[folder], by_folder_docx.get(folder, 0)))
    print()
    if dup_ids:
        print("!! IDs DUPLICADOS:")
        for fid, nome, antes in dup_ids:
            print("   %s  %s (ja visto como %s)" % (fid, nome, antes))
    else:
        print("OK: nenhum ID duplicado.")
    if dup_names:
        print("!! (pasta,nome) DUPLICADOS:")
        for k in dup_names:
            print("   %s" % (k,))
    else:
        print("OK: nenhum (pasta,documento) duplicado.")
    print()
    print("CSV : %s" % csv_path)
    if xlsx_ok:
        print("XLSX: %s" % xlsx_path)

if __name__ == "__main__":
    main()
