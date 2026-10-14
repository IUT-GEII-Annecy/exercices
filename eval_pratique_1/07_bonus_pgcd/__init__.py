import shutil
from pathlib import Path

import check50
import check50.c

MAIN = "07_pgcd.c"
HARNESS = Path(__file__).parent / "_harness.c"


@check50.check()
def exists():
    """07_pgcd.c existe"""
    check50.exists(MAIN)


@check50.check(exists)
def compiles():
    """07_pgcd.c compile sans erreur"""
    check50.c.compile(MAIN, lcs50=True)


@check50.check(compiles)
def pgcd_48_18():
    """PGCD(48, 18) = 6"""
    check50.run("./07_pgcd").stdin("48\n18\n").stdout("PGCD : 6", regex=False).exit(0)


@check50.check(compiles)
def pgcd_premiers_entre_eux():
    """PGCD(17, 5) = 1"""
    check50.run("./07_pgcd").stdin("17\n5\n").stdout("PGCD : 1", regex=False).exit(0)


@check50.check(exists)
def fonction_pgcd_recursive():
    """la fonction pgcd existe, est bien definie et calcule le bon resultat"""
    shutil.copy(HARNESS, ".")
    check50.c.compile(MAIN, exe_name="_student.o", c=True, Dmain="studentmain")
    check50.c.compile("_harness.c", "_student.o", exe_name="_test_pgcd", lcs50=True)
    check50.run("./_test_pgcd").stdout("6\n1\n7\n", regex=False).exit(0)
