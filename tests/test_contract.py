"""Открытые контрольные проверки. Полную тестовую модель дополняет студент."""
import unittest
from pathlib import Path
from starter.p95_candidate import p95
from run import read_samples
ROOT = Path(__file__).resolve().parents[1]

class ContractChecks(unittest.TestCase):
    def test_single(self):
        self.assertEqual(p95([7]), 7)
    def test_twenty(self):
        self.assertEqual(p95(list(range(1, 21))), 19)
    def test_eleven(self):
        # Независимый контрольный пример; исходный кандидат может его не пройти.
        self.assertEqual(p95(list(range(10, 111, 10))), 110)
    def test_input_is_unchanged(self):
        data = [3, 1, 2]
        old = data.copy()
        p95(data)
        self.assertEqual(data, old)
    def test_duplicates(self):
        self.assertEqual(p95([5] * 25), 5)
    def test_invalid(self):
        for values in ([], [-1], [float("nan")], [float("inf")], [True], ["5"]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                p95(values)
    def test_timeout_separated(self):
        values, timeouts = read_samples(ROOT / "data" / "mixed.csv")
        self.assertEqual(len(values), 20)
        self.assertEqual(timeouts, 2)
    def test_bad_row_rejected(self):
        with self.assertRaises(ValueError):
            read_samples(ROOT / "data" / "invalid.csv")

if __name__ == "__main__":
    unittest.main()
