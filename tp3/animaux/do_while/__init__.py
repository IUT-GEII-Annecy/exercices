import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "0_animaux"
MAIN = "chanter.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def chanter_exists():
    """chanter.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(chanter_exists)
def chanter_compiles():
    """chanter.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(chanter_compiles)
def chante_cinq_fois():
    """Chante 5 fois quand on demande 5"""
    check_n(5)


@check50.check(chanter_compiles)
def chante_au_moins_une_fois_avec_zero():
    """Chante quand même une fois quand on demande 0 (do...while)"""
    with exercise_cwd():
        run = check50.run("./chanter").stdin("0")
        run.exit(0)
        output = run.process.before.replace("\r\n", "\n")
        if output.count("Cui-cui !") != 1:
            raise check50.Mismatch("Cui-cui !\n (exactement une fois)", output)


# Helpers
def check_n(n: int):
    with exercise_cwd():
        run = check50.run("./chanter").stdin(str(n))
        run.exit(0)
        output = run.process.before.replace("\r\n", "\n")
        attendu = "Cui-cui !\n" * n
        if output.count("Cui-cui !") != n:
            raise check50.Mismatch(attendu, output)
