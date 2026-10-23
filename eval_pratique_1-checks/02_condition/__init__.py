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


@check50.check(compiles)
def limite_basse_incluse():
    """U=220 (borne basse incluse) -> Tension nominale"""
    check50.run("./02_condition").stdin("220\n").stdout("Tension nominale", regex=False).exit(0)


@check50.check(compiles)
def limite_haute_incluse():
    """U=230 (borne haute incluse) -> Tension nominale"""
    check50.run("./02_condition").stdin("230\n").stdout("Tension nominale", regex=False).exit(0)


@check50.check(compiles)
def juste_sous_la_limite_basse():
    """U=219 (juste sous 220) -> Sous-tension"""
    check50.run("./02_condition").stdin("219\n").stdout("Sous-tension", regex=False).exit(0)


@check50.check(compiles)
def juste_au_dessus_de_la_limite_haute():
    """U=231 (juste au-dessus de 230) -> Surtension"""
    check50.run("./02_condition").stdin("231\n").stdout("Surtension", regex=False).exit(0)
