import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "0_animaux"
MAIN = "miauler.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def miauler_exists():
    """miauler.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(miauler_exists)
def miauler_compiles():
    """miauler.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(miauler_compiles)
def miaule_cinq_fois():
    """Miaule 5 fois quand on demande 5"""
    check_n(5)


@check50.check(miauler_compiles)
def miaule_zero_fois():
    """Ne miaule pas quand on demande 0"""
    check_n(0)


# Helpers
def check_n(n: int):
    with exercise_cwd():
        run = check50.run("./miauler").stdin(str(n))
        run.exit(0)
        output = run.process.before.replace("\r\n", "\n")
        attendu = "Miaou !\n" * n
        if output.count("Miaou !") != n:
            raise check50.Mismatch(attendu, output)
