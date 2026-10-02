import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import daire


class DaireTest(unittest.TestCase):
    def test_ikinci_basis_raporu_kisaltir_gercegi_degil(self):
        g1, r1, _ = daire.bekleme_saniye(5, 1, "sakin")
        g2, r2, hukum = daire.bekleme_saniye(5, 2, "sakin")
        self.assertGreater(g2, 0)
        self.assertLess(r2, g2)
        self.assertIn("dilekçe", hukum)

    def test_gizli_not_bos_degil(self):
        notu = daire.gizli_not()
        self.assertIn("asansör", notu)
        self.assertGreater(len(notu), 20)


if __name__ == "__main__":
    unittest.main()
