import check50

check50.import_checks("../niveau1")
from niveau1 import *


@check50.check(compiles)
def montant_insuffisant():
    """Montant inséré insuffisant"""
    nom = "Sam"
    actual = check50.run("./distributeur")
    actual = actual.stdin(nom).stdout(f"Bonjour, {nom} !")
    actual = actual.stdin("2").stdin("0.50")
    actual.stdout("ERREUR : Montant insuffisant")


@check50.check(compiles)
def boisson_invalide():
    """Numéro de boisson invalide"""
    nom = "Sam"
    actual = check50.run("./distributeur")
    actual = actual.stdin(nom).stdout(f"Bonjour, {nom} !")
    actual = actual.stdin("9").stdin("5.00")
    actual.stdout("ERREUR : Boisson invalide")
