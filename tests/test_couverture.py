import pytest
from app.livraison import frais_livraison


def test_livraison_montant_negatif_declenche_value_error():
    with pytest.raises(ValueError):
        frais_livraison(-1)