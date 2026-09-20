import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "3_formes"
MAIN = "diagonale.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def diagonale_exists():
    """diagonale.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(diagonale_exists)
def diagonale_compiles():
    """diagonale.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(diagonale_compiles)
def diagonale_5():
    """Diagonale de taille 5"""
    check(5)


@check50.check(diagonale_compiles)
def diagonale_1():
    """Diagonale de taille 1"""
    check(1)


# Helpers
def check(n: int):
    grille = []
    for i in range(n):
        ligne = "".join("*" if i == j else "." for j in range(n))
        grille.append(ligne + "\n")
    attendu = "".join(grille)
    with exercise_cwd():
        check50.run("./diagonale").stdin(str(n)).stdout(attendu, regex=False).exit(0)
