#!/usr/bin/env python3
"""Build a local runtime with reviewed English lesson copy layered over the original."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / 'assets/index-BeXJu_A0.js'
RUNTIME = ROOT / 'assets/index-local.js'
INVENTORY = ROOT / 'content-original-en.json'
REWRITES = ROOT / 'content-rewrites'
VARS = {
    'request-lifecycle':'ce','latency-throughput':'he','napkin-math':'Ne',
    'vertical-horizontal':'He','load-balancing':'Ze','stateless':'ct','caching':'_t',
    'cdn':'kt','sql-nosql':'zt','indexes':'en','storage-engines':'An','replication':'Vn',
    'sharding':'$n','consistent-hashing':'Xi','unique-ids':'ua','cap':'Oa',
    'consensus':'Ua','transactions':'$a','files':'mo','apis':'wo','queues':'zo',
    'pubsub':'$o','realtime':'fs','redundancy':'js','rate-limiting':'Ks',
    'timeouts-retries':'tc','observability':'dc','microservices':'Oc',
    'service-discovery':'Uc','sagas':'$c','batch-stream':'ul','authentication':'xl',
    'authorization':'jl','encryption':'Yl','testing':'su','cicd':'Cu','hld-lld':'Ku',
    'design-url-shortener':'ld','design-news-feed':'Pd','design-chat':'tf'
}

def main():
    inventory = json.loads(INVENTORY.read_text())['lessons']
    patches = {}
    for lesson in inventory:
        path = REWRITES / f"{lesson['id']}.json"
        if path.exists():
            patches[lesson['id']] = json.loads(path.read_text())
    (ROOT / 'lesson-content-en.js').write_text(
        'window.__SYSTEM_DESIGN_ENGLISH__=' + json.dumps(patches, ensure_ascii=False, separators=(',', ':')) + ';\n'
    )
    source = ORIGINAL.read_text()
    assignments = ','.join(f'{json.dumps(k)}:{v}' for k,v in VARS.items())
    injection = ''';(()=>{const originals={'''+assignments+'''},patches=window.__SYSTEM_DESIGN_ENGLISH__||{};for(const [id,p] of Object.entries(patches)){const lesson=originals[id];if(!lesson)continue;if(typeof p.summary==='string')lesson.summary=p.summary;if(Array.isArray(p.goals))for(let i=0;i<p.goals.length;i++)if(lesson.goals[i]&&typeof p.goals[i]==='string')lesson.goals[i].text=p.goals[i];if(Array.isArray(p.steps))for(let i=0;i<p.steps.length;i++){const step=lesson.steps[i],q=p.steps[i];if(!step||!q)continue;if(typeof q.title==='string')step.title=q.title;if(Array.isArray(q.body))step.body=q.body;if(typeof q.callout==='string'&&step.callout)step.callout.text=q.callout;if(Array.isArray(q.changes))step.changes=q.changes;}}})();\n'''
    marker = 'document.querySelector(`#app`).innerHTML='
    if marker not in source:
        raise SystemExit('Could not find runtime initialization marker')
    source = source.replace(marker, injection + marker, 1)
    # Route the renderer's material gradients through the shared theme-token map.
    palette_start = source.find('vr={orange:')
    palette_end = source.find(',A=e=>', palette_start)
    if palette_start < 0 or palette_end < 0:
        raise SystemExit('Could not find diagram material palette')
    palette = '''vr=new Proxy({},{ownKeys:()=>["orange","green","blue","yellow","purple","slab","store"],get:(_,k)=>{const css=getComputedStyle(document.documentElement),prefix="--diagram-"+k+"-";return{top:[css.getPropertyValue(prefix+"top-start").trim(),css.getPropertyValue(prefix+"top-end").trim()],side:[css.getPropertyValue(prefix+"side-start").trim(),css.getPropertyValue(prefix+"side-end").trim()]};},getOwnPropertyDescriptor:()=>({enumerable:!0,configurable:!0})})'''
    source = source[:palette_start] + palette + source[palette_end:]
    source = source.replace('stop-color="#E3D6F3"', 'stop-color="${getComputedStyle(document.documentElement).getPropertyValue(\'--diagram-screen-start\').trim()}"', 1)
    source = source.replace('stop-color="#C9B5E6"', 'stop-color="${getComputedStyle(document.documentElement).getPropertyValue(\'--diagram-screen-end\').trim()}"', 1)
    source = source.replace('stop-color="#4b2f6b"', 'stop-color="${getComputedStyle(document.documentElement).getPropertyValue(\'--diagram-sheen\').trim()}"', 1)
    source = source.replace('fill="#a59c90" stroke="#a59c90"', 'fill="${getComputedStyle(document.documentElement).getPropertyValue(\'--diagram-arrow-muted\').trim()}" stroke="${getComputedStyle(document.documentElement).getPropertyValue(\'--diagram-arrow-muted\').trim()}"', 1)
    source = source.replace('stroke="#a8916f"', 'stroke="${getComputedStyle(document.documentElement).getPropertyValue(\'--diagram-grid\').trim()}"', 1)
    RUNTIME.write_text(source)
    print(f'Built {RUNTIME.name}; {len(patches)} lesson patches loaded; original runtime data retained.')

if __name__ == '__main__': main()
