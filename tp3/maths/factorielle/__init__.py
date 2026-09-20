import check50
import check50.c
import math
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "2_maths"
MAIN = "factorielle.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def factorielle_exists():
    """factorielle.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(factorielle_exists)
def factorielle_compiles():
    """factorielle.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(factorielle_compiles)
def factorielle_de_5():
    """Factorielle de 5"""
    check(5)


@check50.check(factorielle_compiles)
def factorielle_de_1():
    """Factorielle de 1"""
    check(1)


# Helpers
def check(n: int):
    attendu = f"{n}! = " + " x ".join(str(i) for i in range(1, n + 1)) + f" = {math.factorial(n)}\n"
    with exercise_cwd():
        check50.run("./factorielle").stdin(str(n)).stdout(attendu, regex=False).exit(0)
