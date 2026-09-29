import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "0_plan_salle"
MAIN = "liste_rangees.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def liste_rangees_exists():
    """liste_rangees.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(liste_rangees_exists)
def liste_rangees_compiles():
    """liste_rangees.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(liste_rangees_compiles)
def liste_rangees_n3():
    """3 rangees : affiche les 3 lignes attendues (toutes libres, ou impaires occupees si bonus fait)"""
    check(3)


@check50.check(liste_rangees_compiles)
def liste_rangees_n1():
    """1 seule rangee"""
    check(1)


@check50.check(liste_rangees_compiles)
def liste_rangees_n0():
    """0 rangee : n'affiche aucune ligne"""
    check(0)


@check50.check(liste_rangees_compiles)
def liste_rangees_bonus_impaires_occupees():
    """Bonus : les rangees de numero impair sont marquees occupees"""
    check_bonus(4)


# Helpers
def rangees_libres(n: int) -> str:
    """Sortie attendue de la version de base : toutes les rangees libres."""
    return "".join(f"Rangee {i} : libre\n" for i in range(1, n + 1))


def rangees_avec_bonus(n: int) -> str:
    """Sortie attendue de la version bonus : rangees impaires occupees."""
    return "".join(
        f"Rangee {i} : {'occupee' if i % 2 == 1 else 'libre'}\n"
        for i in range(1, n + 1)
    )


def check(n: int):
    """Accepte indifferemment la version de base (toutes libres) ou la
    version bonus (impaires occupees) : le sujet demande de modifier le
    MEME fichier pour le bonus, les deux comportements sont donc valides
    pour ce meme exercice. Le check dedie liste_rangees_bonus_impaires_occupees
    ci-dessus verifie specifiquement, lui, que le bonus a bien ete fait."""
    attendu_base = rangees_libres(n)
    with exercise_cwd():
        try:
            (check50.run("./liste_rangees")
                .stdin(str(n))
                .stdout(attendu_base, regex=False)
                .exit(0))
            return
        except check50.Failure:
            pass
    attendu_bonus = rangees_avec_bonus(n)
    with exercise_cwd():
        (check50.run("./liste_rangees")
            .stdin(str(n))
            .stdout(attendu_bonus, regex=False)
            .exit(0))


def check_bonus(n: int):
    attendu = rangees_avec_bonus(n)
    with exercise_cwd():
        (check50.run("./liste_rangees")
            .stdin(str(n))
            .stdout(attendu, regex=False)
            .exit(0))
