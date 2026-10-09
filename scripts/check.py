from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
root=Path(__file__).resolve().parents[1]
class Check(HTMLParser):
 def __init__(self):super().__init__();self.cards=0;self.errors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='article':
   self.cards+=1
  if tag=='img' and not a.get('alt'):self.errors.append('Missing image alternative')
  for key in ['src','href']:
   value=a.get(key,'');url=urlsplit(value)
   if value and not url.scheme and url.path and not (root/unquote(url.path)).is_file():self.errors.append('Missing local asset: '+value)
for name in ['index.html','Guarder.html']:
 parser=Check();parser.feed((root/name).read_text(encoding='utf-8'));assert not parser.errors,parser.errors
assert (root/'index.html').read_bytes()==(root/'Guarder.html').read_bytes()
import re
for asset in re.findall(r'url\(([^)]+)\)',(root/'Guarder.css').read_text(encoding='utf-8')):assert (root/asset).is_file(),asset
text=(root/'index.html').read_text(encoding='utf-8')
ids=re.findall(r'\bid="([^"]+)"',text);assert len(ids)==len(set(ids)), 'Duplicate IDs'
for target in re.findall(r'href="#([^"]+)"',text):assert target in ids,target
print('Entry pages, image/CSS assets, unique IDs and navigation targets checked.')
