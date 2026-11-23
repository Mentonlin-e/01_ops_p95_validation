"""Готовая оболочка. Проверяемая функция находится в starter/p95_candidate.py."""
import argparse
import csv
import json
import math
import sys
from pathlib import Path
from starter.p95_candidate import p95

def read_samples(path):
    values, timeouts, ids = [], 0, set()
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["request_id", "status", "elapsed_ms"]:
            raise ValueError("HEADER: нужны request_id,status,elapsed_ms")
        for line, row in enumerate(reader, 2):
            rid, status, raw = row.get("request_id"), row.get("status"), row.get("elapsed_ms")
            if None in row or not rid or rid in ids or status not in ("ok", "timeout") or raw is None:
                raise ValueError(f"ROW {line}: неверная структура, ID или статус")
            ids.add(rid)
            if status == "timeout":
                if raw.strip():
                    raise ValueError(f"ROW {line}: точное время timeout должно быть пустым")
                timeouts += 1
            else:
                try:
                    value = float(raw)
                except ValueError:
                    raise ValueError(f"ROW {line}: elapsed_ms не является числом") from None
                if not math.isfinite(value) or value < 0:
                    raise ValueError(f"ROW {line}: требуется конечное время >= 0")
                values.append(value)
    if not ids:
        raise ValueError("EMPTY: набор не содержит попыток")
    return values, timeouts

def main():
    parser = argparse.ArgumentParser(description="Проверяемый кандидат p95, правило в SPEC.md")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        values, timeouts = read_samples(args.input)
        total = len(values) + timeouts
        print(json.dumps({"algorithm": "student_candidate", "n_total": total,
            "n_success": len(values), "n_timeout": timeouts,
            "timeout_fraction": timeouts / total,
            "p95_success_ms": p95(values) if values else None,
            "scope": "successful_observations_only",
            "censored": bool(timeouts)}, ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
