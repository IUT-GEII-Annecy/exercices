import check50
import check50.c

PRIX = {
    1: ("cafe", 0.80),
    2: ("the", 0.70),
    3: ("chocolat", 1.00),
    4: ("eau", 0.50),
}


@check50.check()
def exists():
    """distributeur.c existe"""
    check50.exists("distributeur.c")


@check50.check(exists)
def compiles():
    """distributeur.c compile sans erreur"""
    check50.c.compile("distributeur.c", lcs50=True)


@check50.check(compiles)
def achat_cafe_avec_monnaie():
    """Achat d'un café avec monnaie à rendre"""
    achat("Alex", 1, 1.00)


@check50.check(compiles)
def achat_eau_montant_juste():
    """Achat d'une eau avec le montant exact"""
    achat("Sam", 4, 0.50)


# Helpers
def achat(nom: str, numero: int, montant: float):
    boisson, prix = PRIX[numero]
    rendu = montant - prix

    actual = check50.run("./distributeur")
    actual = actual.stdin(nom).stdout(f"Bonjour, {nom} !")
    actual = actual.stdin(str(numero)).stdin(str(montant))
    actual = actual.stdout(f"Voici votre {boisson}.")
    actual.stdout(f"Monnaie rendue : {rendu:.2f} euros")
