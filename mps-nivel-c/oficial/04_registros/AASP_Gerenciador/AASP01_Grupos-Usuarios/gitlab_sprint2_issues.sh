#!/bin/bash
# GitLab API: mover AG-23 e AG-24 para Sprint 2 + status::homologado
# Executar com: GITLAB_TOKEN=<token> bash gitlab_sprint2_issues.sh
# Projeto: aasp/ms.auxo.usuarios (project_id=5)
# GitLab: http://191.234.192.153

set -e
BASE="http://191.234.192.153/api/v4"
PROJ=5
TOKEN="${GITLAB_TOKEN:?Defina GITLAB_TOKEN=<seu-token>}"
HDR="PRIVATE-TOKEN: $TOKEN"

# Descobrir IDs das milestones Sprint 2 e Sprint 3
echo "--- Buscando milestones..."
MILESTONES=$(curl -sf "$BASE/projects/$PROJ/milestones" -H "$HDR")
SPRINT2_ID=$(echo "$MILESTONES" | python3 -c "import sys,json; ms=json.load(sys.stdin); print(next(m['id'] for m in ms if 'sprint 2' in m['title'].lower() or 'sprint-2' in m['title'].lower()))")
SPRINT3_ID=$(echo "$MILESTONES" | python3 -c "import sys,json; ms=json.load(sys.stdin); print(next(m['id'] for m in ms if 'sprint 3' in m['title'].lower() or 'sprint-3' in m['title'].lower()))")
echo "Sprint 2 milestone_id=$SPRINT2_ID  |  Sprint 3 milestone_id=$SPRINT3_ID"

# Descobrir IDs das issues AG-23 e AG-24
echo "--- Buscando issues AG-23 e AG-24..."
ISSUES=$(curl -sf "$BASE/projects/$PROJ/issues?per_page=50" -H "$HDR")
AG23_ID=$(echo "$ISSUES" | python3 -c "import sys,json; issues=json.load(sys.stdin); print(next(i['iid'] for i in issues if 'AG-23' in i.get('title','') or 'ag-23' in i.get('title','').lower()))")
AG24_ID=$(echo "$ISSUES" | python3 -c "import sys,json; issues=json.load(sys.stdin); print(next(i['iid'] for i in issues if 'AG-24' in i.get('title','') or 'ag-24' in i.get('title','').lower()))")
echo "AG-23 iid=$AG23_ID  |  AG-24 iid=$AG24_ID"

# Mover AG-23: Sprint 2 + remover status::em-andamento + adicionar status::homologado
echo "--- Atualizando AG-23..."
curl -sf -X PUT "$BASE/projects/$PROJ/issues/$AG23_ID" \
  -H "$HDR" -H "Content-Type: application/json" \
  -d "{\"milestone_id\": $SPRINT2_ID, \"add_labels\": \"status::homologado\", \"remove_labels\": \"status::em-andamento\", \"state_event\": \"close\"}" \
  | python3 -c "import sys,json; i=json.load(sys.stdin); print(f'AG-23 -> milestone={i[\"milestone\"][\"title\"]}, state={i[\"state\"]}, labels={i[\"labels\"]}')"

# Mover AG-24: Sprint 2 + remover status::em-andamento + adicionar status::homologado
echo "--- Atualizando AG-24..."
curl -sf -X PUT "$BASE/projects/$PROJ/issues/$AG24_ID" \
  -H "$HDR" -H "Content-Type: application/json" \
  -d "{\"milestone_id\": $SPRINT2_ID, \"add_labels\": \"status::homologado\", \"remove_labels\": \"status::em-andamento\", \"state_event\": \"close\"}" \
  | python3 -c "import sys,json; i=json.load(sys.stdin); print(f'AG-24 -> milestone={i[\"milestone\"][\"title\"]}, state={i[\"state\"]}, labels={i[\"labels\"]}')"

echo "=== Concluído: AG-23 e AG-24 movidas para Sprint 2 + status::homologado ==="
