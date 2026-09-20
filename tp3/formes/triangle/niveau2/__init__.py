import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "3_formes"
MAIN = "triangle2.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def triangle2_exists():
    """triangle2.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(triangle2_exists)
def triangle2_compiles():
    """triangle2.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(triangle2_compiles)
def triangle_hauteur_4():
    """Triangle isocèle de hauteur 4"""
    check(4)


@check50.check(triangle2_compiles)
def triangle_hauteur_1():
    """Triangle isocèle de hauteur 1"""
    check(1)


# Helpers
def check(n: int):
    lignes = []
    for ligne in range(1, n + 1):
        lignes.append(" " * (n - ligne) + "*" * (2 * ligne - 1) + "\n")
    attendu = "".join(lignes)
    with exercise_cwd():
        check50.run("./triangle2").stdin(str(n)).stdout(attendu, regex=False).exit(0)
