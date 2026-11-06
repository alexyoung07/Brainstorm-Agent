"""Read-only verification of the original Brainstorming package."""
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'integrity.json').read_text(encoding='utf-8'))
archive_path = root / manifest['archive']
if sha256(archive_path.read_bytes()).hexdigest() != manifest['archive_sha256']:
    raise SystemExit('FAIL: source ZIP checksum mismatch')
with ZipFile(archive_path) as archive:
    expected_members = {item['archive_member'] for item in manifest['files']}
    if {item.filename for item in archive.infolist() if not item.is_dir()} != expected_members:
        raise SystemExit('FAIL: ZIP member list mismatch')
    for item in manifest['files']:
        supplied = archive.read(item['archive_member'])
        installed = (root / item['installed_path']).read_bytes()
        if installed != supplied or sha256(installed).hexdigest() != item['sha256']:
            raise SystemExit('FAIL: original content mismatch: ' + item['installed_path'])
        print('UNCHANGED:', item['installed_path'])
installed_files = {p.relative_to(root).as_posix() for p in (root / '.agents/skills/brainstorming').rglob('*') if p.is_file()}
if installed_files != {item['installed_path'] for item in manifest['files']}:
    raise SystemExit('FAIL: unexpected files in preserved skill directory')
print('PASS: original ZIP and all eight skill files match.')
