import check50
import check50.c

MAIN = "diviseur_tension.c"


@check50.check()
def exists():
    """diviseur_tension.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """diviseur_tension.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def pont_diviseur_egal():
    """Vin=10, R1=R2=1000 -> Vout=5.00 V"""
    check50.run("./diviseur_tension").stdin("10\n1000\n1000\n").stdout(
        "Tension de sortie : 5.00 V", regex=False
    ).exit(0)


@check50.check(compiles)
def pont_diviseur_inegal():
    """Vin=12, R1=1000, R2=2000 -> Vout=8.00 V"""
    check50.run("./diviseur_tension").stdin("12\n1000\n2000\n").stdout(
        "Tension de sortie : 8.00 V", regex=False
    ).exit(0)
