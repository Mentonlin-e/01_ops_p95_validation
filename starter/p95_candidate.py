"""Кандидат на проверку. Его результат нужно подтвердить контрактом и тестами."""
import math

def p95(values):
    if not isinstance(values, list) or not values:
        raise ValueError("Нужен непустой список")
    if any(isinstance(x, bool) or not isinstance(x, (int, float))
           or (isinstance(x, float) and not math.isfinite(x)) or x < 0 for x in values):
        raise ValueError("Нужны конечные неотрицательные числа")
    ordered = sorted(values)
    rank = max(1, math.ceil(0.95 * len(ordered)))
    return ordered[rank - 1]
