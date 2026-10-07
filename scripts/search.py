"""Literal multi-term Markdown retrieval; full-text snippets aren't evidence."""
import argparse,re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('query');parser.add_argument('--limit',type=int,default=8)
args=parser.parse_args();terms=args.query.lower().split();results=[]
for path in sorted((root/'knowledge').rglob('*.md')):
    text=path.read_text();lower=text.lower();score=sum(lower.count(t) for t in terms)
    if score and all(t in lower for t in terms):
        lines=text.splitlines();snippet=next((x for x in lines if all(t in x.lower() for t in terms)),text[:180])
        results.append((score,str(path.relative_to(root)),snippet[:240]))
for score,path,snippet in sorted(results,key=lambda x:(-x[0],x[1]))[:args.limit]:
    print(f'{path}\n  {snippet}\n')
