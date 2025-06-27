import unittest

# Fonction à tester
def multiplication(a, b):
    return a * b

# Classe de test
class TestMultiplication(unittest.TestCase):    # Héritage de la classe TestCase de unittest
    # Méthode de test
    def test_multiplication(self):
        # Assertions pour vérifier si le résultat est correct
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(4, 5), 20)
        self.assertEqual(multiplication(7, 0), 0)
        self.assertEqual(multiplication(-2, 3), -6)
        self.assertEqual(multiplication(-2, -3), 6)

# Définition d'un objet de test
test_multiplication = unittest.TestLoader().loadTestsFromTestCase(TestMultiplication)

# Exécution du test
unittest.TextTestRunner().run(test_multiplication)