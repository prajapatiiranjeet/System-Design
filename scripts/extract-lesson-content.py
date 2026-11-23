import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'assets/index-BeXJu_A0.js'
OUT=ROOT/'content-original-en.json'
source=SOURCE.read_text(encoding='utf-8')

class Token:
    __slots__=('kind','value','start','end')
    def __init__(self,kind,value,start,end): self.kind,self.value,self.start,self.end=kind,value,start,end

def scan_string(s,i):
    q=s[i]; j=i+1; raw=[]
    while j<len(s):
        c=s[j]
        if c=='\\':
            if j+1<len(s): raw.append(s[j:j+2]); j+=2; continue
        if c==q: return ''.join(raw),j+1
        raw.append(c); j+=1
    raise ValueError('unterminated string at %d'%i)

def decode_string(raw):
    # Decode ordinary JS escapes used in course copy while leaving unknown escapes intact.
    out=[]; i=0
    mapping={'n':'\n','r':'\r','t':'\t','b':'\b','f':'\f','v':'\v','0':'\0','`':'`','$':'$','\\':'\\','"':'"',"'":"'"}
    while i<len(raw):
        if raw[i]=='\\' and i+1<len(raw):
            c=raw[i+1]
            if c=='u' and i+5<len(raw) and re.fullmatch(r'[0-9a-fA-F]{4}',raw[i+2:i+6]):
                out.append(chr(int(raw[i+2:i+6],16))); i+=6; continue
            if c=='x' and i+3<len(raw) and re.fullmatch(r'[0-9a-fA-F]{2}',raw[i+2:i+4]):
                out.append(chr(int(raw[i+2:i+4],16))); i+=4; continue
            out.append(mapping.get(c,c)); i+=2
        else: out.append(raw[i]); i+=1
    return ''.join(out)

def tokenize(s):
    out=[]; i=0
    while i<len(s):
        c=s[i]
        if c.isspace(): i+=1; continue
        if s.startswith('//',i):
            j=s.find('\n',i+2); i=len(s) if j<0 else j+1; continue
        if s.startswith('/*',i):
            j=s.find('*/',i+2); i=len(s) if j<0 else j+2; continue
        if c in "'\"`":
            raw,end=scan_string(s,i); out.append(Token('string',decode_string(raw),i,end)); i=end; continue
        if c.isalpha() or c in '_$':
            j=i+1
            while j<len(s) and (s[j].isalnum() or s[j] in '_$'): j+=1
            out.append(Token('id',s[i:j],i,j)); i=j; continue
        if c.isdigit():
            j=i+1
            while j<len(s) and (s[j].isalnum() or s[j] in '._'): j+=1
            out.append(Token('number',s[i:j],i,j)); i=j; continue
        # Multi-character punctuation remains opaque but is harmless to the delimiter parser.
        out.append(Token('punc',c,i,i+1)); i+=1
    return out

class Parser:
    def __init__(self,tokens): self.t=tokens; self.i=0
    def peek(self,v=None):
        if self.i>=len(self.t): return False
        return self.t[self.i].value==v if v is not None else self.t[self.i]
    def take(self):
        x=self.t[self.i]; self.i+=1; return x
    def skip_expr(self,stops):
        stack=[]
        while self.i<len(self.t):
            v=self.t[self.i].value
            if not stack and v in stops: break
            if v in ('(','[','{'): stack.append({'(':')','[':']','{':'}'}[v])
            elif v in (')',']','}'):
                if stack and v==stack[-1]: stack.pop()
                elif not stack: break
            self.i+=1
        return None
    def value(self):
        if self.i>=len(self.t): return None
        tok=self.t[self.i]
        if tok.kind=='string': self.i+=1; return tok.value
        if tok.kind=='number':
            self.i+=1
            try: return int(tok.value,0) if tok.value.startswith('0x') else float(tok.value) if '.' in tok.value else int(tok.value)
            except: return tok.value
        if tok.value=='[':
            self.i+=1; arr=[]
            while self.i<len(self.t) and not self.peek(']'):
                if self.peek(','): self.i+=1; continue
                before=self.i; arr.append(self.value())
                if self.i==before: self.skip_expr({',',']'})
                if self.peek(','): self.i+=1
                elif not self.peek(']') and self.i<len(self.t): self.skip_expr({',',']'}); self.i+=1 if self.peek(',') else 0
            if self.peek(']'): self.i+=1
            return arr
        if tok.value=='{':
            self.i+=1; obj={}
            while self.i<len(self.t) and not self.peek('}'):
                if self.peek(','): self.i+=1; continue
                keytok=self.take(); key=keytok.value
                if self.peek(':'):
                    self.i+=1
                    if key=='scene': self.skip_expr({',','}'}) ; val=None
                    else: val=self.value()
                    obj[key]=val
                else:
                    # Shorthand/spread methods are irrelevant to copy inventory.
                    self.skip_expr({',','}'})
                if self.peek(','): self.i+=1
                elif not self.peek('}') and self.i<len(self.t): self.skip_expr({',','}'}); self.i+=1 if self.peek(',') else 0
            if self.peek('}'): self.i+=1
            return obj
        if tok.kind=='id' and tok.value in ('true','false','null'):
            self.i+=1; return {'true':True,'false':False,'null':None}[tok.value]
        self.skip_expr({',',']','}'})
        return None

def match_brace(s,start):
    depth=0; i=start
    while i<len(s):
        c=s[i]
        if c in "'\"`":
            _,i=scan_string(s,i); continue
        if s.startswith('//',i):
            j=s.find('\n',i+2); i=len(s) if j<0 else j+1; continue
        if s.startswith('/*',i):
            j=s.find('*/',i+2); i=len(s) if j<0 else j+2; continue
        if c=='{': depth+=1
        elif c=='}':
            depth-=1
            if depth==0: return i+1
        i+=1
    raise ValueError('unclosed object')

found=[]
for m in re.finditer(r'([A-Za-z_$][\w$]*)=\{id:`([^`]+)`,title:`([^`]*)`',source):
    var,id_,title=m.group(1),m.group(2),m.group(3)
    start=m.start()+len(var)+1
    end=match_brace(source,start)
    tokens=tokenize(source[start:end])
    obj=Parser(tokens).value()
    if not isinstance(obj,dict) or obj.get('id')!=id_: raise ValueError('failed parsing '+id_)
    goals=obj.get('goals') or []
    steps=[]
    for i,step in enumerate(obj.get('steps') or []):
        if not isinstance(step,dict): continue
        callout=step.get('callout') if isinstance(step.get('callout'),dict) else {}
        steps.append({
            'index':i,'short':step.get('short',''),'chapter':step.get('chapter',''),
            'title':step.get('title',''),'body':step.get('body') or [],
            'calloutKind':callout.get('kind',''),'callout':callout.get('text',''),
            'changes':step.get('changes') or []
        })
    found.append({'id':id_,'variable':var,'title':title,'summary':obj.get('summary',''),'goals':goals,'steps':steps})
if len(found)!=40: raise SystemExit(f'expected 40 lesson objects, found {len(found)}')
OUT.write_text(json.dumps({'source':'assets/index-BeXJu_A0.js','lessonCount':len(found),'stageCount':sum(len(x['steps']) for x in found),'lessons':found},ensure_ascii=False,indent=2))
print('Extracted',len(found),'lessons and',sum(len(x['steps']) for x in found),'stages to',OUT)
print('Body/callout missing:',[(l['id'],s['index']) for l in found for s in l['steps'] if not s['body'] and not s['callout']])
