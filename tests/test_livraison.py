from app.livraison import frais_livraison


def test_livraison_panier_ordinaire():
    # Arrange : préparer les données
    montant = 120

    # Act : appeler la fonction
    resultat = frais_livraison(montant)

    # Assert : vérifier le résultat
    assert resultat == 25


def test_livraison_299():
    assert frais_livraison(299) == 25


def test_livraison_300():
    assert frais_livraison(300) == 0


def test_livraison_301():
    assert frais_livraison(301) == 0


def test_livraison_zero():
    assert frais_livraison(0) == 25
    