import sys
from pathlib import Path

import check50
from check50 import internal

# check50.import_checks() résout toujours les chemins relatifs depuis le
# dossier du slug de premier niveau (check50.internal.check_dir), pas
# depuis ce fichier. Ça marche quand niveau2 est le slug testé directement,
# mais casse dès qu'un autre slug (ex. rendu/) importe niveau2, car
# "../niveau1" est alors résolu depuis le dossier de ce slug-là et non
# depuis 4_distributeur/. On résout donc explicitement depuis __file__.
_niveau1_dir = (Path(__file__).parent / "../niveau1").resolve()
_niveau1_checks_file = internal.load_config(_niveau1_dir)["checks"]
niveau1 = internal.import_file("niveau1", _niveau1_dir / _niveau1_checks_file)
sys.modules["niveau1"] = niveau1
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
