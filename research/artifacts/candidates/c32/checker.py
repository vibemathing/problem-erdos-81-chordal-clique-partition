"""C32 exact checker wrapper. Concatenates the two plain-text audited source fragments."""
from pathlib import Path
import hashlib
_here=Path(__file__).resolve().parent
_parts=[_here/"checker-core-a.pyfrag",_here/"checker-core-b.pyfrag"]
_src="".join(p.read_text(encoding="utf-8") for p in _parts)
SOURCE_SHA256=hashlib.sha256(_src.encode("utf-8")).hexdigest()
exec(compile(_src,str(_here/"checker-concatenated.py"),"exec"),globals(),globals())
