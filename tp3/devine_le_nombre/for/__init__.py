import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "1_devine_le_nombre"
MAIN = "devine_for.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def devine_exists():
    """devine_for.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(devine_exists)
def devine_compiles():
    """devine_for.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(devine_compiles)
def niveau_invalide():
    """Refuse un niveau invalide (5)"""
    with exercise_cwd():
        check50.run("./devine_for").stdin("5").stdout("[Nn]iveau invalide", regex=True).exit(1)


@check50.check(devine_compiles)
def perd_niveau_facile():
    """Niveau facile (10 vies) : perd si on ne trouve jamais (10 essais hors plage)"""
    with exercise_cwd():
        run = check50.run("./devine_for").stdin("1")
        for _ in range(10):
            run = run.stdin("1000").stdout("plus petit", regex=True)
        run.stdout(r"Perdu.*\d+", regex=True).exit(0)


@check50.check(devine_compiles)
def niveau_impossible_perd_sans_essai():
    """Niveau impossible (0 vie) : perd immédiatement, sans demander de proposition"""
    with exercise_cwd():
        check50.run("./devine_for").stdin("4").stdout(r"Perdu.*\d+", regex=True).exit(0)
