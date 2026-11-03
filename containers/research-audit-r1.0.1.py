from pathlib import Path
import hashlib, json, re, subprocess, sys
from urllib.parse import unquote, urlsplit
sys.dont_write_bytecode = True
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root.parent/'tools'))
from check_anchors import collect_headings, iter_unfenced_lines

platform=[
'Summary and fit','Verified product baseline','Architecture and workload support',
'Centralized and multi-host management','Provisioning and orchestration','Networking and multicast',
'Availability, failover, and maintenance','Backup, restore, and disaster recovery',
'Other capabilities and operations','Licensing, subscriptions, and support',
'Modules, add-ons, and integrations','Limitations, risks, and open questions','References']
comparison=[
'Executive summary','Compared stacks and assumptions','VM and container support','Centralized management',
'Provisioning and orchestration','Networking and multicast','Availability, failover, and maintenance',
'Backup and disaster recovery','Other capabilities and operations','Licensing, support, and required add-ons',
'Conditional recommendations','Migration and portability','Open questions and proposed validation','References']
REV='r1.0.1'
reports=[f'research-vmware-{REV}.md',f'research-proxmox-{REV}.md',f'research-rhel-{REV}.md',f'research-vm-comparison-{REV}.md']
print('audit targets:',', '.join(reports),'| cutoff 2026-10-30 | anchors via',root.parent/'tools'/'check_anchors.py',file=sys.stderr)
result={'revision':REV,'cutoff':'2026-10-30','reports':{},'pdfs':{},'web_snapshots':{},'issues':[]}
all_text=''
anchors_cache={}
def anchors_for(p):
 if p not in anchors_cache:
  lines=p.read_text().splitlines()
  anchors=set(collect_headings(lines))
  for _,line in iter_unfenced_lines(lines):
   anchors.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']',line,re.I))
  anchors_cache[p]=anchors
 return anchors_cache[p]
for name in reports:
 p=root/name
 if not p.exists():
  result['issues'].append(name+': missing'); continue
 s=p.read_text(); all_text+='\n'+s
 headings=re.findall(r'^## (.+)$',s,re.M)
 expected=comparison if name==reports[-1] else platform
 info={'bytes':p.stat().st_size,'words':len(s.split()),'headings':len(headings),'heading_order_ok':headings==expected,'cutoff_present':'2026-10-30' in s[:1200],'revision_header':('Document revision: **'+REV+'**') in s[:2500],'unresolved_heading':'### References - unresolved' in s,'tables':0,'external_urls':len(set(re.findall(r'https?://[^\s<>\)]+',s))),'internal_links':0,'local_links':0,'reference_links':0}
 if headings!=expected: result['issues'].append(name+': wrong section template/order')
 if not info['cutoff_present']:result['issues'].append(name+': cutoff missing near top')
 if not info['revision_header']:result['issues'].append(name+': revision header missing near top')
 if not info['unresolved_heading']:result['issues'].append(name+': missing unresolved subsection')
 if re.search(r'Research in progress\.|\bTODO\b|\bTBD\b|Working draft',s,re.I):result['issues'].append(name+': draft marker remains')
 fence=None; table_columns=None; previous=''; last_line=''
 for lineno,line in enumerate(s.splitlines(),1):
  if re.match(r'^\s*(```|~~~)',line): fence=None if fence else line[:3]; continue
  if fence:continue
  if line.startswith('|'):
   cells=re.split(r'(?<!\\)\|',line.strip())[1:-1]
   if not previous.startswith('|'):
    table_columns=len(cells);info['tables']+=1
   elif len(cells)!=table_columns:result['issues'].append(f'{name}:{lineno}: table cells {len(cells)} expected {table_columns}')
  if line.startswith('#') and last_line.strip():result['issues'].append(f'{name}:{lineno}: heading missing preceding blank line')
  previous=line;last_line=line
 if fence:result['issues'].append(name+': unclosed code fence')
 definitions=dict((label.lower(),url) for label,url in re.findall(r'^\[([^\]]+)\]:\s*(\S+)',s,re.M))
 for lineno,line in iter_unfenced_lines(s.splitlines()):
  targets=re.findall(r'\]\(([^\s\)]+)',line)
  for label in re.findall(r'(?<!!)\[([^\]]+)\](?!\(|:|\[)',line):
   if re.fullmatch(r'[A-Z]+\d+',label):
    if label.lower() in definitions:
     targets.append(definitions[label.lower()]);info['reference_links']+=1
    elif not re.search(r'(?:<a[^>]+id=["\']'+label.lower()+r'["\']|\*\*'+label+r'\b)',line,re.I):
     result['issues'].append(f'{name}:{lineno}: undefined source reference [{label}]')
  for target in targets:
   if re.match(r'^[a-z][a-z0-9+.-]*:',target,re.I):continue
   pathname,sep,fragment=target.partition('#')
   full=(p.parent/unquote(pathname)).resolve() if pathname else p
   if pathname:
    info['local_links']+=1
    if not full.exists():result['issues'].append(f'{name}:{lineno}: missing local target {target}');continue
   if sep:
    info['internal_links']+=1
    if full.suffix=='.md' and unquote(fragment) not in anchors_for(full):result['issues'].append(f'{name}:{lineno}: broken anchor {target}')
 result['reports'][name]=info
seen={}
for p in sorted((root/'reference').glob('*.pdf')):
 b=p.read_bytes();h=hashlib.sha256(b).hexdigest()
 r=subprocess.run(['pdfinfo',str(p)],capture_output=True,text=True)
 pages=re.search(r'^Pages:\s+(\d+)',r.stdout,re.M)
 valid=b.startswith(b'%PDF-') and r.returncode==0
 md=p.with_name(p.name+'.md')
 info={'bytes':len(b),'pages':int(pages[1]) if pages else None,'valid':valid,'sha256':h,'linked':('reference/'+p.name) in all_text,'markdown_extraction':md.exists() and md.stat().st_size>0}
 if not info['markdown_extraction']:result['issues'].append(p.name+': missing or empty .pdf.md extraction')
 if not valid:result['issues'].append(p.name+': invalid PDF')
 if h in seen:result['issues'].append(p.name+': duplicate of '+seen[h])
 if not info['linked']:result['issues'].append(p.name+': not linked from reports')
 seen[h]=p.name;result['pdfs'][p.name]=info
for p in sorted(q for q in (root/'reference'/'web').glob('*') if q.suffix in ('.html','.txt')):
 b=p.read_bytes();md=p.with_name(p.name+'.md')
 info={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'markdown_extraction':md.exists(),'linked':('reference/web/'+p.name) in all_text}
 if not info['linked']:result['issues'].append('web/'+p.name+': not linked from reports')
 result['web_snapshots'][p.name]=info
json.dump(result,sys.stdout,indent=2);print()
sys.exit(bool(result['issues']))
