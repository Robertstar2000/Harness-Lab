# HTML sources are committed directly because the hosting layer injects HTML runtime markup.
"""Mirror the verified public Harness Lab publication into this repository."""
from pathlib import Path, PurePosixPath
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen, Request
from urllib.parse import quote, urlparse
import hashlib,json,os,subprocess

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'publication-manifest.json').read_text())
origin=manifest['origin']
if origin!='https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site':
 raise SystemExit('Unexpected publication origin')
def download(item):
 path=PurePosixPath(item['path'])
 if path.is_absolute() or '..' in path.parts or path.parts[0]!='dist':
  raise ValueError('Invalid publication path')
 target=root/str(path)
 if target.is_file() and target.stat().st_size==item['bytes'] and hashlib.sha256(target.read_bytes()).hexdigest()==item['sha256']:return
 if path.suffix.lower() in ('.html','.htm'):
  raise ValueError('Canonical HTML source mismatch: '+str(path)+'; commit the Site source HTML and matching manifest together. The hosted response includes injected markup and cannot verify the source checksum.')
 request=Request(origin+'/'+quote('/'.join(path.parts[1:]),safe='/'),headers={'User-Agent':'MIFECO-Harness-Lab-Sync/1.0'})
 with urlopen(request,timeout=120) as response: data=response.read()
 if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256']:
  raise ValueError('Publication content mismatch: '+str(path))
 target.parent.mkdir(parents=True,exist_ok=True)
 target.write_bytes(data)
with ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(download,manifest['files']))
expected={item['path'] for item in manifest['files']}
for stale in (root/'dist').rglob('*'):
 if stale.is_file() and stale.relative_to(root).as_posix() not in expected:stale.unlink()
print('Verified',len(manifest['files']),'publication files against source commit',manifest['site_source_commit'])
if os.getenv('GITHUB_ACTIONS')=='true':
 subprocess.run(['git','config','user.name','github-actions[bot]'],check=True)
 subprocess.run(['git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com'],check=True)
 subprocess.run(['git','add','--','dist'],check=True)
 if subprocess.run(['git','diff','--cached','--quiet']).returncode:
  subprocess.run(['git','commit','-m','Sync verified Harness Lab publication v'+str(manifest['site_version'])],check=True)
  subprocess.run(['git','push'],check=True)
