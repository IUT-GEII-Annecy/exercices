import check50
import check50.c

MAIN = "pgcd.c"


@check50.check()
def exists():
    """pgcd.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """pgcd.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def pgcd_48_18():
    """PGCD(48, 18) = 6"""
    check50.run("./pgcd").stdin("48\n18\n").stdout("PGCD : 6", regex=False).exit(0)


@check50.check(compiles)
def pgcd_premiers_entre_eux():
    """PGCD(17, 5) = 1"""
    check50.run("./pgcd").stdin("17\n5\n").stdout("PGCD : 1", regex=False).exit(0)
