import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "3_formes"
MAIN = "damier.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def damier_exists():
    """damier.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(damier_exists)
def damier_compiles():
    """damier.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(damier_compiles)
def damier_4x6():
    """Damier 4 lignes x 6 colonnes"""
    check(4, 6)


@check50.check(damier_compiles)
def damier_2x2():
    """Damier 2 lignes x 2 colonnes"""
    check(2, 2)


# Helpers
def check(lignes: int, colonnes: int):
    grille = []
    for i in range(lignes):
        ligne = "".join("#" if (i + j) % 2 == 0 else "." for j in range(colonnes))
        grille.append(ligne + "\n")
    attendu = "".join(grille)
    with exercise_cwd():
        (check50.run("./damier")
            .stdin(str(lignes))
            .stdin(str(colonnes))
            .stdout(attendu, regex=False)
            .exit(0))
