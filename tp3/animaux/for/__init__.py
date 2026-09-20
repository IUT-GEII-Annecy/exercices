import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "0_animaux"
MAIN = "aboyer.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def aboyer_exists():
    """aboyer.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(aboyer_exists)
def aboyer_compiles():
    """aboyer.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(aboyer_compiles)
def aboie_cinq_fois():
    """Aboie 5 fois quand on demande 5"""
    check_n(5)


@check50.check(aboyer_compiles)
def aboie_zero_fois():
    """N'aboie pas quand on demande 0"""
    check_n(0)


# Helpers
def check_n(n: int):
    with exercise_cwd():
        run = check50.run("./aboyer").stdin(str(n))
        run.exit(0)
        output = run.process.before.replace("\r\n", "\n")
        attendu = "Ouaf !\n" * n
        if output.count("Ouaf !") != n:
            raise check50.Mismatch(attendu, output)
