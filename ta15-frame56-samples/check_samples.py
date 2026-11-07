"""Summarize published TA15 CSVs. This does not run Unreal or compare PNGs."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read(name):
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


samples = read("reverse-samples.csv")
pairs = read("reverse-image-pairs.csv")
groups = ("C0", "C1", "C1Live")
frames = tuple(str(n) for n in range(54, 58))
subsamples = ("0/2", "1/2")
actors = ("NiagaraActor_0", "NiagaraActor_1")
sample_keys = {(r["condition"], r["source"], r["temporal"], r["actor"]) for r in samples}
pair_keys = {(r["condition"], r["source_frame"]) for r in pairs}
assert len(samples) == len(sample_keys) == 48
assert sample_keys == {(g, f, s, a) for g in groups for f in frames for s in subsamples for a in actors}
assert len(pairs) == len(pair_keys) == 12 and pair_keys == {(g, f) for g in groups for f in frames}

labels = {"0": "Active", "3": "Complete"}
for sub in subsamples:
    for group in groups:
        rows = [r for r in samples if (r["condition"], r["source"], r["temporal"]) == (group, "56", sub)]
        states = {(r["cache"] != "None", r["actual_state"], r["age"]) for r in rows}
        assert len(states) == 1
        bound, state, age = states.pop()
        print(f"56 {sub} {group:7} {'bound' if bound else 'unbound':7} {labels[state]:8} age={float(age):.5f}s")

print(f"Zero mask XOR: {sum(int(r['mask_xor']) == 0 for r in pairs)}/{len(pairs)}")
print(f"Exact RGB: {sum(r['rgb_exact'] == 'True' for r in pairs)}/{len(pairs)}")
