import check50
import check50.c

MAIN = "accumulateur.c"


@check50.check()
def exists():
    """accumulateur.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """accumulateur.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def moyenne_3_mesures():
    """Moyenne de 3 mesures (10, 20, 30)"""
    check50.run("./accumulateur").stdin("3\n10\n20\n30\n").stdout(
        "Moyenne : 20.00 V", regex=False
    ).exit(0)


@check50.check(compiles)
def moyenne_1_mesure():
    """Moyenne d'une seule mesure"""
    check50.run("./accumulateur").stdin("1\n42\n").stdout(
        "Moyenne : 42.00 V", regex=False
    ).exit(0)
