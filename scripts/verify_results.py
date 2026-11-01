"""Smoke-check the generated experiment artifacts, not real-world model quality."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / 'results'
m = json.loads((root / 'metrics.json').read_text())
assert m['samples'] == 178
assert 2 <= m['selected_k'] <= 6
assert all(-1 <= score <= 1 for score in m['silhouette_by_k'].values())
assert -1 <= m['adjusted_rand_vs_reference'] <= 1
plots = ['clusters.png']
for name in plots:
    data = (root / name).read_bytes()
    assert data.startswith(b'\x89PNG\r\n\x1a\n') and len(data) > 100
print('Experiment metrics and plots passed sanity checks.')
