# Créez une fonction simple à tester.
def addition(a,b):
     return a+b
 
# TDD : développement dirigé par les tests (Test Driven Developement)
    # Écrivez une méthode de test pour la fonction addition.
def test_addition():
    #appeler la fonction à tester
    result = addition(3,5)
    #Assertion pour vérifier si résultat est conforme au résultat attendu
    assert result == 8 ,f"Le résultat attendu est 8, mais le résultat obtenu est {result}"
 
    result = addition(3,5)
    assert result == 8 ,f"Le résultat attendu est 9, mais le résultat obtenu est {result}"
# Créez une suite de tests et exécutez-les. 
test_addition()
print("test terminé")