import shutil
from pathlib import Path

import check50
import check50.c

MAIN = "05_diviseur_tension.c"
HARNESS = Path(__file__).parent / "_harness.c"


@check50.check()
def exists():
    """05_diviseur_tension.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """05_diviseur_tension.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def pont_diviseur_egal():
    """Vin=10, R1=R2=1000 -> Vout=5.00 V"""
    check50.run("./05_diviseur_tension").stdin("10\n1000\n1000\n").stdout(
        "Tension de sortie : 5.00 V", regex=False
    ).exit(0)


@check50.check(compiles)
def pont_diviseur_inegal():
    """Vin=12, R1=1000, R2=2000 -> Vout=8.00 V"""
    check50.run("./05_diviseur_tension").stdin("12\n1000\n2000\n").stdout(
        "Tension de sortie : 8.00 V", regex=False
    ).exit(0)


@check50.check(compiles)
def r1_nul():
    """R1=0 (borne) -> Vout=Vin (10.00 V)"""
    check50.run("./05_diviseur_tension").stdin("10\n0\n1000\n").stdout(
        "Tension de sortie : 10.00 V", regex=False
    ).exit(0)


@check50.check(compiles)
def r2_nul():
    """R2=0 (borne) -> Vout=0.00 V"""
    check50.run("./05_diviseur_tension").stdin("10\n1000\n0\n").stdout(
        "Tension de sortie : 0.00 V", regex=False
    ).exit(0)


@check50.check(exists)
def fonction_tension_sortie():
    """la fonction tension_sortie existe et calcule le bon resultat"""
    shutil.copy(HARNESS, ".")
    # Etape 1 : objet du fichier etudiant seul, avec son main() renomme
    # (-Dmain=studentmain) pour ne pas entrer en conflit avec celui du
    # harnais a l'edition de liens -- -Dmain appliquerait sinon aussi au
    # harnais si les deux fichiers etaient compiles ensemble en une seule
    # commande, cf. gotcha teste manuellement.
    check50.c.compile(MAIN, exe_name="_student.o", c=True, Dmain="studentmain")
    # Etape 2 : harnais (son vrai main) + objet etudiant. Si
    # tension_sortie n'existe pas (logique ecrite directement dans main),
    # l'edition de liens echoue avec "undefined reference" et ce check
    # echoue -- c'est le but : empecher de faire l'exercice sans fonction
    # dediee.
    check50.c.compile("_harness.c", "_student.o", exe_name="_test_tension_sortie", lcs50=True)
    # Harnais (_harness.c) : 8.00 (R1,R2 inegaux), 5.00 (R1=R2), 10.00
    # (R1=0, borne -- Vout=Vin), 0.00 (R2=0, borne -- Vout=0).
    check50.run("./_test_tension_sortie").stdout("8.00\n5.00\n10.00\n0.00\n", regex=False).exit(0)
