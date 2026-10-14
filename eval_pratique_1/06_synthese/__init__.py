import check50
import check50.c

MAIN = "synthese.c"


@check50.check()
def exists():
    """synthese.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """synthese.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def deux_hors_tolerance():
    """min=0, max=10, mesures 4,5,15,8,-2 -> 2 hors tolérance"""
    check50.run("./synthese").stdin("0\n10\n4\n5\n15\n8\n-2\n").stdout(
        "Mesures hors tolérance : 2", regex=False
    ).exit(0)


@check50.check(compiles)
def zero_hors_tolerance():
    """min=0, max=10, mesures 1,2,3 -> 0 hors tolérance"""
    check50.run("./synthese").stdin("0\n10\n3\n1\n2\n3\n").stdout(
        "Mesures hors tolérance : 0", regex=False
    ).exit(0)
