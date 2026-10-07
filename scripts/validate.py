"""Validate schema, coverage, graph endpoints and LOCAL Markdown links only."""
import json,re,sys,hashlib
from pathlib import Path

root=Path(__file__).resolve().parents[1];errors=[]
def require(condition,message):
    if not condition:errors.append(message)
domains=json.loads((root/'architecture/domains.json').read_text())
sources=json.loads((root/'references/sources.json').read_text())
coverage=json.loads((root/'governance/coverage.json').read_text())
graph=json.loads((root/'architecture/graph.json').read_text())
ids={d['id'] for d in domains};sids={s['id'] for s in sources}
require(ids=={f'D{i:02}' for i in range(1,41)},'40 stable domain IDs required')
require(len(domains)==len(ids),'duplicate domain ID')
require(len(sources)==len(sids),'duplicate source ID')
require(len(coverage)==280,'280 topic records required')
require(len({c['id'] for c in coverage})==len(coverage),'duplicate topic ID')
for d in domains:
    require(len(d['topics'])==7,f"{d['id']} needs seven core subdomains")
    require(all(p in ids for p in d['prereqs']),f"invalid prerequisite {d['id']}")
    require(all(s in sids for s in d['sources']),f"missing source {d['id']}")
    p=root/'knowledge/domains'/f"{d['slug']}.md"
    require(p.exists(),f'missing {p}')
    if p.exists():
        text=p.read_text()
        for i,t in enumerate(d['topics'],1):
            require(f"{d['id']}.{i:02d}" in text,f'missing topic {d["id"]}.{i:02d}')
            require(len(t)==5 and all(t),f'empty topic {d["id"]}.{i:02d}')
        require(text.count('**Kegagalan.**')==7,f'missing failures {d["id"]}')
        require(text.count('**Verifikasi.**')==7,f'missing verifiers {d["id"]}')
for e in graph['edges']:require(e['source'] in ids and e['target'] in ids,'invalid graph endpoint')
require({n['id'] for n in graph['nodes']}==ids,'graph node mismatch')
for c in coverage:require((root/c['path']).exists(),f'missing coverage path {c["id"]}')
def anchors(path):
    result=set()
    for line in path.read_text().splitlines():
        if re.match(r'^#{1,6} ',line):
            heading=re.sub(r'^#+ ','',line).lower()
            heading=re.sub(r'[^\w\- ]','',heading)
            result.add(heading.replace(' ','-'))
    return result
links=0
for p in root.rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)',text):
        if target.startswith(('http:','https:','mailto:')):continue
        file,_,anchor=target.partition('#')
        resolved=(p.parent/file).resolve() if file else p
        require(resolved.is_relative_to(root),f'link escapes repo {p}:{target}')
        require(resolved.exists(),f'broken local link {p.relative_to(root)}:{target}')
        if anchor and resolved.exists() and resolved.suffix=='.md':
            require(anchor in anchors(resolved),f'missing anchor {p.relative_to(root)}:{target}')
        links+=1
for p in root.rglob('*.json'):
    try:json.loads(p.read_text())
    except Exception as ex:errors.append(f'invalid JSON {p}:{ex}')
report=dict(domains=len(domains),topics=len(coverage),source_entries=len(sources),graph_nodes=len(graph['nodes']),graph_edges=len(graph['edges']),local_links_checked=links,errors=errors,status='PASS' if not errors else 'FAIL',scope='Structure/schema/local links only; no scientific completeness or external URL verification.')
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
