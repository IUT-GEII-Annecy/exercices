import check50
import check50.c

MAIN = "variables.c"


@check50.check()
def exists():
    """variables.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """variables.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def puissance_4_230():
    """Puissance avec I=4, U=230"""
    check50.run("./variables").stdin("4\n230\n").stdout("Puissance : 920.00 W\n", regex=False).exit(0)


@check50.check(compiles)
def puissance_2_100():
    """Puissance avec I=2, U=100"""
    check50.run("./variables").stdin("2\n100\n").stdout("Puissance : 200.00 W\n", regex=False).exit(0)
