"""Recompute the TA05 window means and sampled maxima from the public CSVs."""

import csv
import hashlib
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


DATA = Path(__file__).resolve().parent / "data"
METRICS = (("GPUTime", "gpu"), ("GPU/Translucency", "translucency"))


def read_rows(filename, provenance):
    path = DATA / filename
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual_hash != provenance["source_sha256"][filename]:
        raise ValueError(f"{filename}: SHA-256 mismatch")
    with path.open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def window_key(row):
    return int(row["run"]), row["condition"]


def main():
    provenance = json.loads((DATA / "provenance.json").read_text(encoding="utf-8"))
    summaries = read_rows("逐轮统计.csv", provenance)
    samples = read_rows("逐帧关键列.csv", provenance)

    frames_by_window = defaultdict(list)
    for row in samples:
        frames_by_window[window_key(row)].append(row)

    summary_keys = {window_key(row) for row in summaries}
    if (
        len(summaries) != len(summary_keys)
        or len(summaries) != provenance["runs"]
        or summary_keys != frames_by_window.keys()
        or len(samples) != provenance["numeric_frames"]
    ):
        raise ValueError("Window keys or sample totals do not match")

    results = []
    for row in summaries:
        run, condition = window_key(row)
        frames = frames_by_window[run, condition]
        indices = [int(frame["frame"]) for frame in frames]
        if len(frames) != int(row["frames"]) or indices != list(range(len(frames))):
            raise ValueError(f"Run {run:02d}: frame count or sequence mismatch")

        readings = []
        for column, prefix in METRICS:
            values = [float(frame[column]) for frame in frames]
            if not all(map(math.isfinite, values)):
                raise ValueError(f"Run {run:02d}: non-finite {column} sample")
            mean = statistics.fmean(values)
            peak = max(values)
            for suffix, value in (("mean", mean), ("sample_max", peak)):
                field = f"{prefix}_{suffix}_ms"
                if not math.isclose(value, float(row[field]), rel_tol=0, abs_tol=1e-9):
                    raise ValueError(f"Run {run:02d}: {field} differs from summary")
            first_peak = indices[values.index(peak)]
            readings.append(f"{column} mean={mean:.6f} max={peak:.6f} (frame {first_peak})")
        results.append(f"{run:02d} {condition:<18} n={len(frames)} | " + " | ".join(readings))

    print("All timings in ms. Frame indices start at zero.")
    print("\n".join(results))
    print(f"PASS: {len(summaries)} windows, {len(samples)} sampled frames")


if __name__ == "__main__":
    try:
        main()
    except (OSError, KeyError, ValueError) as error:
        raise SystemExit(f"FAIL: {error}") from None
