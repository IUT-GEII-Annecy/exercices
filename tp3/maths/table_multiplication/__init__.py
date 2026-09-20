import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "2_maths"
MAIN = "table_multiplication.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def table_exists():
    """table_multiplication.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(table_exists)
def table_compiles():
    """table_multiplication.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(table_compiles)
def table_de_5():
    """Table de multiplication de 5"""
    check(5)


@check50.check(table_compiles)
def table_de_1():
    """Table de multiplication de 1"""
    check(1)


# Helpers
def check(n: int):
    attendu = "".join(f"{n} x {i} = {n*i}\n" for i in range(1, 11))
    with exercise_cwd():
        check50.run("./table_multiplication").stdin(str(n)).stdout(attendu, regex=False).exit(0)
