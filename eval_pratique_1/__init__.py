import check50
import check50.c

FILES = [
    "01_variables.c",
    "02_condition.c",
    "03_compte_a_rebours.c",
    "04_accumulateur.c",
    "05_diviseur_tension.c",
    "06_synthese.c",
    "07_pgcd.c",
]


@check50.check()
def exists():
    """tous les fichiers .c sont presents"""
    for f in FILES:
        check50.exists(f)


@check50.check(exists)
def compiles_variables():
    """01_variables.c compile sans erreur"""
    check50.c.compile("01_variables.c", lcs50=True)


@check50.check(exists)
def compiles_condition():
    """02_condition.c compile sans erreur"""
    check50.c.compile("02_condition.c", lcs50=True)


@check50.check(exists)
def compiles_compte_a_rebours():
    """03_compte_a_rebours.c compile sans erreur"""
    check50.c.compile("03_compte_a_rebours.c", lcs50=True)


@check50.check(exists)
def compiles_accumulateur():
    """04_accumulateur.c compile sans erreur"""
    check50.c.compile("04_accumulateur.c", lcs50=True)


@check50.check(exists)
def compiles_diviseur_tension():
    """05_diviseur_tension.c compile sans erreur"""
    check50.c.compile("05_diviseur_tension.c", lcs50=True)


@check50.check(exists)
def compiles_synthese():
    """06_synthese.c compile sans erreur"""
    check50.c.compile("06_synthese.c", lcs50=True)


@check50.check(exists)
def compiles_pgcd():
    """07_pgcd.c compile sans erreur"""
    check50.c.compile("07_pgcd.c", lcs50=True)
