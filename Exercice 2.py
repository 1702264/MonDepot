import unittest

# Code de la fonction à tester
def puissance(a, b):
    return a ** b

# Classe de test
class TestPuissance(unittest.TestCase):    # Héritage de la classe TestCase de unittest
    # Définition de la méthode de test
    def test_puissance(self):
        # Assertions pour vérifier si le résultat est conforme à ce qui est attendu
        self.assertEqual(puissance(2, 3), 8)
        self.assertEqual(puissance(5, 0), 1)
        self.assertEqual(puissance(4, 2), 16)
        self.assertEqual(puissance(10, 1), 10)
        self.assertEqual(puissance(3, 4), 81)
        self.assertEqual(puissance(0, 5), 0)
        self.assertEqual(puissance(-2, 2), 4)
        self.assertEqual(puissance(-2, 3), -8)

# Définition d'un objet de test
test_puissance = unittest.TestLoader().loadTestsFromTestCase(TestPuissance)

# Exécution du test
unittest.TextTestRunner().run(test_puissance)
