"""Verify and unpack this bounded text bundle. Never executes decoded code."""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import lzma
from pathlib import Path

LIMIT = 1_048_576

def check(data: bytes, entry: dict) -> None:
    if len(data) != entry['bytes'] or hashlib.sha256(data).hexdigest() != entry['sha256']:
        raise ValueError('content size or SHA-256 mismatch')

def flat(name: str) -> str:
    if not name or Path(name).name != name or '/' in name or '\\' in name or name in ('.', '..'):
        raise ValueError('non-flat member name')
    return name

def load_unique(pairs: list[tuple[str, object]]) -> dict:
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError('duplicate JSON key')
        out[key] = value
    return out

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    manifest = json.loads((source/'bundle-manifest.json').read_text(encoding='utf-8'), object_pairs_hook=load_unique)
    pieces = []
    for item in manifest['parts']:
        path = source/flat(item['path'])
        if path.is_symlink() or path.stat().st_size > LIMIT:
            raise ValueError('invalid input part')
        raw = path.read_bytes()
        check(raw, item)
        pieces.append(raw)
    payload = b''.join(pieces)
    if len(payload) > LIMIT or hashlib.sha256(payload).hexdigest() != manifest['payload_sha256']:
        raise ValueError('payload mismatch')
    compressed = base64.b64decode(b''.join(payload.split()), validate=True)
    if hashlib.sha256(compressed).hexdigest() != manifest['xz_sha256']:
        raise ValueError('XZ mismatch')
    decoder = lzma.LZMADecompressor(memlimit=134_217_728)
    raw = decoder.decompress(compressed, max_length=LIMIT+1)
    if len(raw) > LIMIT or not decoder.eof or decoder.unused_data:
        raise ValueError('invalid or oversized compressed stream')
    check(raw, {'bytes':manifest['decoded_json_bytes'], 'sha256':manifest['decoded_json_sha256']})
    members = json.loads(raw.decode('utf-8'), object_pairs_hook=load_unique)
    if set(members) != set(manifest['members']):
        raise ValueError('member set mismatch')
    verified = {}
    for name, text in members.items():
        flat(name)
        if not isinstance(text, str):
            raise ValueError('non-text member')
        data = text.encode('utf-8')
        check(data, manifest['members'][name])
        verified[name] = data
    # Verify everything before writing; refuse an existing output directory.
    args.out.mkdir(parents=True, exist_ok=False)
    for name, data in verified.items():
        with (args.out/name).open('xb') as handle:
            handle.write(data)
    print(json.dumps({'verdict':'candidate_only', 'decoded_members':len(verified),
                      'decoded_json_sha256':manifest['decoded_json_sha256'],
                      'mathematical_code_executed':False}, sort_keys=True))

if __name__ == '__main__':
    main()
