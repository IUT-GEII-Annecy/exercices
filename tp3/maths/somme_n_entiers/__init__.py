import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "2_maths"
MAIN = "somme_n_entiers.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def somme_exists():
    """somme_n_entiers.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(somme_exists)
def somme_compiles():
    """somme_n_entiers.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(somme_compiles)
def somme_de_5():
    """Somme des 5 premiers entiers"""
    check(5)


@check50.check(somme_compiles)
def somme_de_1():
    """Somme des 1 premiers entiers"""
    check(1)


# Helpers
def check(n: int):
    somme = n * (n + 1) // 2
    attendu = " + ".join(str(i) for i in range(1, n + 1)) + f" = {somme}\n"
    with exercise_cwd():
        check50.run("./somme_n_entiers").stdin(str(n)).stdout(attendu, regex=False).exit(0)
