import check50
import check50.c

FILES = [
    "variables.c",
    "condition.c",
    "compte_a_rebours.c",
    "accumulateur.c",
    "diviseur_tension.c",
    "synthese.c",
    "pgcd.c",
]


@check50.check()
def exists():
    """tous les fichiers .c sont presents"""
    for f in FILES:
        check50.exists(f)


@check50.check(exists)
def compiles_variables():
    """variables.c compile sans erreur"""
    check50.c.compile("variables.c", lcs50=True)


@check50.check(exists)
def compiles_condition():
    """condition.c compile sans erreur"""
    check50.c.compile("condition.c", lcs50=True)


@check50.check(exists)
def compiles_compte_a_rebours():
    """compte_a_rebours.c compile sans erreur"""
    check50.c.compile("compte_a_rebours.c", lcs50=True)


@check50.check(exists)
def compiles_accumulateur():
    """accumulateur.c compile sans erreur"""
    check50.c.compile("accumulateur.c", lcs50=True)


@check50.check(exists)
def compiles_diviseur_tension():
    """diviseur_tension.c compile sans erreur"""
    check50.c.compile("diviseur_tension.c", lcs50=True)


@check50.check(exists)
def compiles_synthese():
    """synthese.c compile sans erreur"""
    check50.c.compile("synthese.c", lcs50=True)


@check50.check(exists)
def compiles_pgcd():
    """pgcd.c compile sans erreur"""
    check50.c.compile("pgcd.c", lcs50=True)
