# -*- coding: utf-8 -*-
"""Preenche a PlanilhaIndicadores ASR (Nivel C) com Fonte da Evidencia (links Drive)
e autoavaliacao da empresa. Coluna 'Final' (auditor) fica vazia."""
import csv, re, openpyxl
from openpyxl.styles import Alignment, Font

SRC = '/root/.claude/uploads/5abbaf16-7c03-5c89-bd42-930844eb89cc/d820916e-PlanilhaIndicadores_SW_2024__NivelC.xlsx'
OUT = '/home/user/MPS-repository/mps-nivel-c/_interno/PlanilhaIndicadores_SW_2024_NivelC_PREENCHIDA.xlsx'
CSV = '/root/.claude/uploads/5abbaf16-7c03-5c89-bd42-930844eb89cc/c0987dec-MAPADRIVE_IndicedeLinks.csv'

FOLDER = {
 'cap':'1WaBDqw00DVFtkeCoCL3gJk59oO07kehU',
 'curriculos':'1voDfAAX8j0BR6ddM55izLF9pdQ2eclYi',
 'templates':'1ZYnsnMyNDpcBbyatEeB6yL5RKRhHAjuW',
}
def folder_url(k): return f"https://drive.google.com/drive/folders/{FOLDER[k]}"

# ---- link index ----
LINKS = {}
with open(CSV, encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        doc = row['Documento'].strip(); tipo = row['Tipo'].strip().lower(); link = row['Link'].strip()
        if tipo == 'md': continue
        LINKS.setdefault(doc.split('_',1)[0], {})[tipo] = (doc, link)

MISSING = set()
def L(code, sec=None, ext=None):
    """Return 'filename [§sec] — url' or record missing."""
    e = LINKS.get(code)
    if not e:
        MISSING.add(code); return None
    if ext and ext in e: fn, url = e[ext]
    elif 'docx' in e: fn, url = e['docx']
    else: fn, url = list(e.values())[0]
    label = fn
    if sec: label = f"{fn} {sec}"
    return f"{label} — {url}"

def block(items):
    """items: list of (code, sec, ext) or string. Returns multiline text, dropping missing."""
    out = []
    for it in items:
        if isinstance(it, str):
            out.append(it); continue
        code, sec, ext = (it + (None,None,None))[:3]
        s = L(code, sec, ext)
        if s: out.append(s)
    return "\n".join(out)

# ============ PROJECT ROLE MAPS ============
PROF = {
 'TAP':['TAP-PROFARMA01-001'],'PLA':['PLA-PROFARMA01-001'],'ADAP':['ADAP-PROFARMA01-001'],
 'REQ':['REQ-PROFARMA01-001'],'RASTR':['RASTR-PROFARMA01-001'],'PCP':['PCP-PROFARMA01-001'],
 'REV':['REV-PROFARMA01-001'],'VV':['VV-PROFARMA01-001'],'CTQ':['CTQ-PROFARMA01-001'],
 'RELVV':['REL-VV-PROFARMA01-001'],'GCO':['GCO-PROFARMA01-001'],'GDE':['GDE-PROFARMA01-001'],
 'MED':['MED-PROFARMA01-001'],'GQA':['GQA-PROFARMA01-001'],'RAC':['RAC-PROFARMA01-001'],
 'ATAK':['ATA-PROFARMA01-001'],'ATAA':['ATA-PROFARMA01-002'],'CR':['CR-PROFARMA01-001'],
 'LI':['LI-PROFARMA01-001'],'TAE':['TAE-PROFARMA01-001'],'GEST':['GEST-PROFARMA01'],
 'ITP':[],'ATA_METAS':[],'ATA_VAL':[],'CAP':[],
}
GAS = {
 'TAP':['TAP-GASMIG02-001','TAP-GASMIG02-002'],'PLA':['PLA-GASMIG02-001','PLA-GASMIG02-002'],
 'ADAP':['ADAP-GASMIG02-001','ADAP-GASMIG02-002'],'REQ':['REQ-GASMIG02-001','REQ-GASMIG02-002'],
 'RASTR':['RASTR-GASMIG02-001','RASTR-GASMIG02-002'],'PCP':['PCP-GASMIG02-001','PCP-GASMIG02-002'],
 'VV':['VV-GASMIG02-001','VV-GASMIG02-002'],'ITP':['ITP-GASMIG02-002'],'REV':['REV-GASMIG02-001'],
 'GDE':['GDE-GASMIG02-001'],'GCO':['GCO-GASMIG02-001'],'MED':['MED-GASMIG02-001'],
 'GQA':['GQA-GASMIG02-001'],'RAC':['RAC-GASMIG02-001'],'ATAK':['ATA-GASMIG02-001'],
 'ATAA':['ATA-GASMIG02-002','ATA-GASMIG02-003'],'CAP':['CAP-GASMIG02-001'],
 'LI':['LI-GASMIG02-001'],'TAE':['TAE-GASMIG02-001','TAE-GASMIG02-002'],'GEST':['GEST-GASMIG02'],
 'CR':[],'CTQ':[],'RELVV':[],'ATA_METAS':[],'ATA_VAL':[],
}
FRU = {
 'TAP':['TAP-FRUKI01-001','TAP-FRUKI01-002'],'PLA':['PLA-FRUKI01-001','PLA-FRUKI01-002'],
 'ADAP':['ADAP-FRUKI01-001','ADAP-FRUKI01-002'],'REQ':['REQ-FRUKI01-001','REQ-FRUKI01-002'],
 'RASTR':['RASTR-FRUKI01-001','RASTR-FRUKI01-002'],'PCP':['PCP-FRUKI01-001','PCP-FRUKI01-002'],
 'VV':['VV-FRUKI01-001','VV-FRUKI01-002'],'ITP':['ITP-FRUKI01-001','ITP-FRUKI01-002'],
 'GDE':['GDE-FRUKI01-001'],'GCO':['GCO-FRUKI01-001'],'MED':['MED-FRUKI01-001'],
 'GQA':['GQA-FRUKI01-001'],'RAC':['RAC-FRUKI01-001','RAC-FRUKI01-002'],'CR':['CR-FRUKI01-001'],
 'LI':['LI-FRUKI01-001'],'ATAK':['ATA-FRUKI01-001'],'ATA_METAS':['ATA-FRUKI01-002'],
 'ATAA':['ATA-FRUKI01-003'],'ATA_VAL':['ATA-FRUKI01-004','ATA-FRUKI01-005','ATA-FRUKI01-006','ATA-FRUKI01-007'],
 'TAE':['TAE-FRUKI01-001','TAE-FRUKI01-002'],'REV':[],'CTQ':[],'RELVV':[],'CAP':[],
}
PROJECTS = [('PROFARMA',PROF),('GASMIG',GAS),('FRUKI',FRU)]
PCOL = {'PROFARMA':3,'GASMIG':4,'FRUKI':5}  # C,D,E

# indicator -> role list (applied to all 3 projects)
IND_ROLES = {
 'GPR 1':['TAP','PLA'],'GPR 2+':['ADAP'],'GPR 3+':['PLA'],'GPR 4+':['PLA'],
 'GPR 5':['PLA','GEST'],'GPR 6':['PLA'],'GPR 7+':['PLA'],'GPR 8':['PLA'],'GPR 9':['PLA'],
 'GPR 10+':['PLA','GEST'],'GPR 11':['PLA'],'GPR 12+':['PLA'],'GPR 13+':['ATAK','PLA'],
 'GPR 14+':['RAC','GEST'],'GPR 15':['RAC'],'GPR 16':['RAC','TAE'],'GPR 17+':['RAC','GEST'],
 'GPR 18+':['RAC','CR'],'GPR 19+':['LI','RAC'],'GPR 20':['LI'],
 'REQ 1':['REQ','ATAK','ATA_METAS'],'REQ 2+':['REQ'],'REQ 3':['REQ','ATAK'],'REQ 4':['RASTR'],
 'REQ 5':['RASTR','GQA'],'REQ 6':['REQ'],'REQ 7':['REQ','ATAA','RELVV','CTQ'],
 'PCP 1+':['PCP'],'PCP 2':['REV','PCP'],'PCP 3+':['PCP'],
 'ITP 1+':['ITP'],'ITP 2':['ITP'],'ITP 3+':['ITP','REV'],'ITP 4':['ITP'],
 'ITP 5+':['ITP','VV','RELVV'],'ITP 6':['TAE','ATAA','ITP'],
 'VV 1':['VV'],'VV 2':['VV','REV'],'VV 3+':['VV','CTQ'],
 'VV 4':['RELVV','REV','GQA','ATA_VAL'],'VV 5':['RELVV','ATAA','ATA_VAL'],
}

def proj_evidence_and_ratings(sheet, ind):
    roles = IND_ROLES[ind]
    lines = []; ratings = {}
    for pname, pmap in PROJECTS:
        if sheet == 'ITP' and pname == 'PROFARMA':
            ratings[pname] = ''      # PROFARMA sem fase de integracao
            continue
        codes = []
        for r in roles:
            for c in pmap.get(r, []):
                if c not in codes: codes.append(c)
        if not codes:
            ratings[pname] = ''
            continue
        ev = block([(c,None,None) for c in codes])
        if ev:
            lines.append(f"[{pname}]\n{ev}")
            ratings[pname] = 'T'
        else:
            ratings[pname] = ''
    return "\n".join(lines), ratings

# ============ ORG SHEETS ============
GCO_REG=[('GCO-PROFARMA01-001',None,None),('GCO-GASMIG02-001',None,None),('GCO-FRUKI01-001',None,None)]
MED_REG=[('MED-PROFARMA01-001',None,None),('MED-GASMIG02-001',None,None),('MED-FRUKI01-001',None,None)]
GDE_REG=[('GDE-PROFARMA01-001',None,None),('GDE-GASMIG02-001',None,None),('GDE-FRUKI01-001',None,None)]
GQA_REG=[('GQA-PROFARMA01-001',None,None),('GQA-GASMIG02-001',None,None),('GQA-FRUKI01-001',None,None)]
LI_REG =[('LI-PROFARMA01-001',None,None),('LI-GASMIG02-001',None,None),('LI-FRUKI01-001',None,None)]
ADAP_REG=[('ADAP-PROFARMA01-001',None,None),('ADAP-GASMIG02-001',None,None),('ADAP-GASMIG02-002',None,None),('ADAP-FRUKI01-001',None,None),('ADAP-FRUKI01-002',None,None)]
REGCAP=[(f'REG-CAP-{n}',None,None) for n in ['001','001B','002','002B','003','004','005','006','007','008','009','010','011','012','013']]
AVACAP=[(f'AVA-CAP-{n}',None,None) for n in ['001','002','003','004','005']]

ORG_EV = {
 # AQU - candidato a NAO-APLICAVEL (sem aquisicao nos projetos). Evidencia: processo definido.
 'AQU 1':[('PRO-AQU-001','§3',None)],
 'AQU 2':[('PRO-AQU-001','§4',None)],
 'AQU 3+':[('PRO-AQU-001','§5',None)],
 'AQU 4+':[('PRO-AQU-001','§6',None)],
 'AQU 5':[],  # nivel B - fora do escopo do nivel C
 # GCO
 'GCO 1':[('PLA-GCO-001','§3',None),('CONV-ORG-001',None,None)],
 'GCO 2':[('PLA-GCO-001','§4',None),('GUIA-GCO-001',None,None)],
 'GCO 3':[('PLA-GCO-001','§5',None)]+GCO_REG,
 'GCO 4':[('PLA-GCO-001','§6',None),('CONV-ORG-001',None,None)]+GCO_REG,
 'GCO 5':[('PLA-GCO-001','§7',None),('EST-GPC-001',None,None)]+GQA_REG,
 # MED
 'MED 1':[('PLA-MED-001','§2',None)],
 'MED 2':[('PLA-MED-001','§3',None)],
 'MED 3+':[('PLA-MED-001','§4',None)]+MED_REG,
 'MED 4+':[('PLA-MED-001','§5',None)]+MED_REG,
 'MED 5':[('PLA-MED-001','§6',None)],
 'MED 6':[('PLA-MED-001','§7',None),('REG-OSW-001',None,None)],
 'MED 7':[('PLA-MED-001','§8',None)],
 # GDE
 'GDE 1':[('PRO-GDE-001','§3',None)],
 'GDE 2':[('PRO-GDE-001','§4',None)]+GDE_REG,
 'GDE 3':[('PRO-GDE-001','§4',None)]+GDE_REG,
 'GDE 4':[('PRO-GDE-001','§4',None),('TPL-GDE-001',None,None)]+GDE_REG,
 'GDE 5':[('PRO-GDE-001','§5',None)],
 'GDE 6':[('PRO-GDE-001','§5',None),('TPL-GDE-001',None,None)]+GDE_REG,
 # CAP
 'CAP 1+':[('PLA-CAP-001','§3',None)],
 'CAP 2':[('PLA-CAP-001','§4',None),('TPL-CAP-001',None,None),('CAP-GASMIG02-001',None,None),
          f"Mini-manuais por processo (GUIA-CAP-001 a 012) e trilhas por papel (MAT-CAP-013 a 022): {folder_url('cap')}"]+REGCAP,
 'CAP 3':[('PLA-CAP-001','§5',None),('REL-CAP-001',None,None)]+AVACAP,
 'CAP 4':[('PLA-CAP-001','§6',None),('REG-CAP-CV-001',None,None),
          f"Curriculos/certificados da equipe: {folder_url('curriculos')}"],
 # GPC
 'GPC 1':[('PLA-GPC-001','§2',None)],
 'GPC 2+':[('PRO-GPC-001',None,None),('GUIA-GPC-001',None,None)],
 'GPC 3':[('EST-GPC-001',None,None),('TPL-GPC-001',None,None)]+GQA_REG,
 'GPC 4+':[('PLA-GPC-001','§5.1',None),('REG-GPC-001',None,None)]+LI_REG,
 'GPC 5+':[('REG-GPC-002',None,None),('PLA-GPC-001','§5',None)],
 'GPC 6':[('PRO-GPC-002',None,None),('ATA-GPC-001',None,None)],
 'GPC 7':[('EST-GPC-002',None,None)],
 'GPC 8':[('PLA-GPC-001','§3',None),('GUIA-GCO-001',None,None)],
 'GPC 9':[('PLA-MED-001','§4 e §8',None)],
 'GPC 10':[('PLA-GPC-001','§4',None)]+ADAP_REG,
 'GPC 11':[('PLA-GPC-001','§6',None),('REG-GPC-002',None,None),('ATA-GPC-001',None,None)],
 # OSW
 'OSW 1':[('POL-ORG-001',None,None),('REG-OSW-002',None,None)],
 'OSW 2':[('PRO-OSW-001','§3',None),('PLA-CAP-001','§6.1',None)],
 'OSW 3':[('PRO-OSW-001','§6',None),('ATA-GPC-001',None,None),('REG-OSW-001',None,None)],
 'OSW 4+':[('PRO-OSW-001','§4',None),('MAPA-ORG-001',None,'docx')],
 'OSW 5+':[('PRO-OSW-001','§5',None),('EST-GPC-002',None,None)],
 'OSW 6':[('PRO-OSW-001','§6',None),('PLA-MED-001','§5',None)],
 'OSW 7':[('PRO-OSW-001','§7',None),('ATA-GPC-001',None,None),('REG-OSW-002',None,None)],
 'OSW 8':[('PRO-OSW-002','§3',None),('REG-OSW-001',None,None)],
 'OSW 9':[('PRO-OSW-002','§4',None),('REG-OSW-001',None,None)],
 'OSW 10':[('PRO-OSW-002','§5',None),('REG-OSW-001',None,None)],
}
ORG_NO_RATING = {'AQU 1','AQU 2','AQU 3+','AQU 4+','AQU 5'}  # AQU pendente decisao ASR

# ============ WRITE ============
wb = openpyxl.load_workbook(SRC)
WRAP = Alignment(wrap_text=True, vertical='top')

def find_blocks(ws):
    """Return list of (indicator_code, indicator_row, legend_row)."""
    blocks=[]; cur=None
    for r in range(4, ws.max_row+1):
        a = ws.cell(row=r, column=1).value
        b = ws.cell(row=r, column=2).value
        if a and isinstance(a,str):
            m = re.match(r'^([A-Z]{2,3}\s*\d+\+?)', a.strip())
            if m:
                code = re.sub(r'\s+',' ',m.group(1)).strip()
                cur = [code, r, None]; blocks.append(cur)
        if b == '(T,L,P,N,NA)' and cur and cur[2] is None:
            cur[2] = r
    return blocks

# project sheets
for sheet in ['GPR','REQ','PCP','ITP','VV']:
    ws = wb[sheet]
    for code, irow, lrow in find_blocks(ws):
        if code not in IND_ROLES: continue
        ev, ratings = proj_evidence_and_ratings(sheet, code)
        if ev:
            c = ws.cell(row=irow, column=2, value=ev); c.alignment=WRAP
        rr = lrow if lrow else irow
        for pname,col in PCOL.items():
            if ratings.get(pname):
                ws.cell(row=rr, column=col, value=ratings[pname]).alignment=Alignment(horizontal='center',vertical='top')

# org sheets
for sheet in ['AQU','GCO','MED','GDE','CAP','GPC','OSW']:
    ws = wb[sheet]
    for code, irow, lrow in find_blocks(ws):
        if code not in ORG_EV: continue
        ev = block(ORG_EV[code])
        if ev:
            ws.cell(row=irow, column=2, value=ev).alignment=WRAP
        rr = lrow if lrow else irow
        if code not in ORG_NO_RATING and ev:
            ws.cell(row=rr, column=3, value='T').alignment=Alignment(horizontal='center',vertical='top')

# ============ CP_Projeto (transversal aos processos de projeto) ============
PLA_ALL=[('PLA-PROFARMA01-001',None,None),('PLA-GASMIG02-001',None,None),('PLA-GASMIG02-002',None,None),('PLA-FRUKI01-001',None,None),('PLA-FRUKI01-002',None,None)]
VV_ALL =[('VV-PROFARMA01-001',None,None),('VV-GASMIG02-001',None,None),('VV-FRUKI01-001',None,None)]
REV_ALL=[('REV-PROFARMA01-001',None,None),('REV-GASMIG02-001',None,None)]
REGCAP5=[(f'REG-CAP-{n}',None,None) for n in ['001','002','003','004','005']]

CP_PROJ_ROWS = {4:'i',9:'ii',14:'iii',19:'iv',24:'v',29:'vi',33:'vii'}
CP_PROJ_EV = {
 'i':["Registros de execucao dos 3 projetos (evidencia detalhada nas abas GPR/REQ/PCP/ITP/VV). Ancoras:"]+PLA_ALL+VV_ALL,
 'ii':["Adaptacao do processo-padrao por projeto:"]+ADAP_REG+[('PRO-GPC-001',None,None),('GUIA-GPC-001',None,None)],
 'iii':[('PLA-CAP-001',None,None),('CAP-GASMIG02-001',None,None)]+REGCAP5,
 'iv':[('EST-GPC-001',None,None),('TPL-GPC-001',None,None)]+GQA_REG,
 'v':GQA_REG+REV_ALL+[('TPL-GPC-001',None,None)],
 'vi':LI_REG+[('REG-GPC-001',None,None)],
 'vii':[('PRO-GPC-001',None,None),('PLA-MED-001',None,None),('PLA-GPC-001',None,None)],
}
ws = wb['CP_Projeto']
for row,att in CP_PROJ_ROWS.items():
    ev = block(CP_PROJ_EV[att])
    if ev: ws.cell(row=row, column=2, value=ev).alignment=WRAP

# ============ CP_Organizacional (7 processos x 7 atributos) ============
CPO_PROC_COL = {'AQU':2,'GCO':4,'MED':6,'GDE':8,'CAP':10,'GPC':12,'OSW':14}
CPO_ROWS = {5:'i',10:'ii',15:'iii',20:'iv',25:'v',30:'vi',35:'vii'}
COM = {  # atributos comuns a todos os processos
 'ii':[('PRO-GPC-001',None,None),('GUIA-GPC-001',None,None)],
 'iv':[('EST-GPC-001',None,None),('GQA-ORG-001',None,None)],
 'v':[('GQA-ORG-001',None,None),('TPL-GPC-001',None,None)],
 'vi':[('REG-GPC-001',None,None),('PLA-GPC-001','§5.1',None)],
 'vii':[('PLA-GPC-001',None,None),('PLA-MED-001',None,None)],
}
CPO_I = {  # (i) doc principal por processo
 'AQU':[('PRO-AQU-001',None,None)],
 'GCO':[('PLA-GCO-001',None,None)]+GCO_REG,
 'MED':[('PLA-MED-001',None,None)]+MED_REG,
 'GDE':[('PRO-GDE-001',None,None)]+GDE_REG,
 'CAP':[('PLA-CAP-001',None,None)]+REGCAP5,
 'GPC':[('PLA-GPC-001',None,None),('PRO-GPC-001',None,None)],
 'OSW':[('PRO-OSW-001',None,None),('PRO-OSW-002',None,None)],
}
CPO_III = {  # (iii) capacitacao por processo
 'AQU':[('PLA-CAP-001',None,None),('GUIA-CAP-012',None,None)],
 'GCO':[('PLA-CAP-001',None,None),('GUIA-CAP-005',None,None),('MAT-CAP-021',None,None),('AVA-CAP-004',None,None)],
 'MED':[('PLA-CAP-001',None,None),('GUIA-CAP-008',None,None),('MAT-CAP-022',None,None),('AVA-CAP-005',None,None)],
 'GDE':[('PLA-CAP-001',None,None),('GUIA-CAP-007',None,None)],
 'CAP':[('PLA-CAP-001',None,None),('GUIA-CAP-011',None,None),('AVA-CAP-005',None,None)],
 'GPC':[('PLA-CAP-001',None,None),('GUIA-CAP-009',None,None),('MAT-CAP-014',None,None),('AVA-CAP-005',None,None)],
 'OSW':[('PLA-CAP-001',None,None),('GUIA-CAP-010',None,None),('MAT-CAP-013',None,None)],
}
ws = wb['CP_Organizacional']
for proc,col in CPO_PROC_COL.items():
    for row,att in CPO_ROWS.items():
        if att=='i': items=CPO_I[proc]
        elif att=='iii': items=CPO_III[proc]
        else: items=COM[att]
        ev = block(items)
        if ev: ws.cell(row=row, column=col, value=ev).alignment=WRAP

wb.save(OUT)
print("Saved:", OUT)
print("\nMISSING CODES (", len(MISSING), "):")
for m in sorted(MISSING): print("  -", m)
