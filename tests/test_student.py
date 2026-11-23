"""Добавьте собственные тесты. Ожидания получите независимо от кандидата."""
import unittest
from starter.p95_candidate import p95

class StudentChecks(unittest.TestCase):
    def test_your_case(self):
        self.assertEqual(p95([1, 2, 3, 4, 6]), 6)
        self.assertEqual(p95([7]), 7)
        with self.assertRaisesRegex(ValueError, "Нужен непустой список"):
            p95([])
        self.assertEqual(p95([4, 2, 1, 3]), 4)
        with self.assertRaisesRegex(ValueError, "Нужны конечные неотрицательные числа"):
            p95(["1, 2, 3"])

if __name__ == "__main__":
    unittest.main()
