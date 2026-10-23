import check50
import check50.c

MAIN = "03_compte_a_rebours.c"


@check50.check()
def exists():
    """03_compte_a_rebours.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """03_compte_a_rebours.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def n_5():
    """n=5 : compte à rebours puis Décollage !"""
    check50.run("./03_compte_a_rebours").stdin("5\n").stdout(
        "5\n4\n3\n2\n1\nDécollage !\n", regex=False
    ).exit(0)


@check50.check(compiles)
def n_0():
    """n=0 : seul Décollage ! est affiché"""
    check50.run("./03_compte_a_rebours").stdin("0\n").stdout(
        "Décollage !\n", regex=False
    ).exit(0)


@check50.check(compiles)
def n_1():
    """n=1 (borne basse du compte à rebours) : 1 puis Décollage !"""
    check50.run("./03_compte_a_rebours").stdin("1\n").stdout(
        "1\nDécollage !\n", regex=False
    ).exit(0)
