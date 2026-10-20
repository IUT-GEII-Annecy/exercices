import check50
import check50.c

MAIN = "02_condition.c"


@check50.check()
def exists():
    """02_condition.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """02_condition.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def surtension():
    """Surtension si U > 230"""
    check50.run("./02_condition").stdin("235\n").stdout("Surtension", regex=False).exit(0)


@check50.check(compiles)
def sous_tension():
    """Sous-tension si U < 220"""
    check50.run("./02_condition").stdin("215\n").stdout("Sous-tension", regex=False).exit(0)


@check50.check(compiles)
def nominale():
    """Tension nominale si 220 <= U <= 230"""
    check50.run("./02_condition").stdin("225\n").stdout("Tension nominale", regex=False).exit(0)
