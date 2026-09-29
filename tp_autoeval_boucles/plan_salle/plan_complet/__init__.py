import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "0_plan_salle"
MAIN = "plan_complet.c"


def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def plan_complet_exists():
    """plan_complet.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(plan_complet_exists)
def plan_complet_compiles():
    """plan_complet.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(plan_complet_compiles)
def plan_complet_3x4():
    """Plan 3 rangees x 4 places (grille de 'o', ou 'x'/'o' par parite si bonus fait)"""
    check(3, 4)


@check50.check(plan_complet_compiles)
def plan_complet_2x2():
    """Plan 2 rangees x 2 places"""
    check(2, 2)


@check50.check(plan_complet_compiles)
def plan_complet_1x1():
    """Plan 1 rangee x 1 place"""
    check(1, 1)


@check50.check(plan_complet_compiles)
def plan_complet_bonus_impaires_occupees():
    """Bonus : les rangees de numero impair sont affichees avec 'x'"""
    check_bonus(3, 4)


# Helpers
def grille_libre(n: int, m: int) -> str:
    """Sortie attendue de la version de base : grille entierement en 'o'."""
    ligne = " ".join(["o"] * m) + "\n"
    return ligne * n


def grille_avec_bonus(n: int, m: int) -> str:
    """Sortie attendue de la version bonus : 'x' sur les rangees impaires."""
    lignes = []
    for i in range(1, n + 1):
        symbole = "x" if i % 2 == 1 else "o"
        lignes.append(" ".join([symbole] * m) + "\n")
    return "".join(lignes)


def check(n: int, m: int):
    """Accepte indifferemment la version de base (grille en 'o') ou la
    version bonus ('x' sur les rangees impaires) : le sujet demande de
    modifier le MEME fichier pour le bonus, les deux comportements sont
    donc valides pour ce meme exercice. Le check dedie
    plan_complet_bonus_impaires_occupees verifie specifiquement, lui,
    que le bonus a bien ete fait."""
    attendu_base = grille_libre(n, m)
    with exercise_cwd():
        try:
            # .stdout(check50.EOF) est indispensable : .stdout(attendu) seul
            # ne verifie qu'un PREFIXE du flux (pexpect.expect), donc un
            # programme qui affiche la bonne grille PUIS continue (ex. des
            # dimensions figees et plus grandes que n/m demandes) passerait
            # quand meme sans cette verification supplementaire.
            (check50.run("./plan_complet")
                .stdin(str(n))
                .stdin(str(m))
                .stdout(attendu_base, regex=False)
                .stdout(check50.EOF)
                .exit(0))
            return
        except check50.Failure:
            pass
    attendu_bonus = grille_avec_bonus(n, m)
    with exercise_cwd():
        (check50.run("./plan_complet")
            .stdin(str(n))
            .stdin(str(m))
            .stdout(attendu_bonus, regex=False)
            .stdout(check50.EOF)
            .exit(0))


def check_bonus(n: int, m: int):
    attendu = grille_avec_bonus(n, m)
    with exercise_cwd():
        (check50.run("./plan_complet")
            .stdin(str(n))
            .stdin(str(m))
            .stdout(attendu, regex=False)
            .stdout(check50.EOF)
            .exit(0))
