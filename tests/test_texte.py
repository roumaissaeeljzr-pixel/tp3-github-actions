import pytest
from app.texte import nettoyer_texte


@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    ("  déjà   propre  ", "déjà propre"),
    ("", ""),
    ("    ", ""),
    ("BONJOUR", "bonjour"),
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


@pytest.mark.parametrize("entree", [123, None])
def test_texte_non_textuel_declenche_type_error(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)


def test_nettoyer_deux_fois_ne_change_pas_le_resultat():
    texte = "  BONJOUR   monde  "
    resultat = nettoyer_texte(texte)

    assert nettoyer_texte(resultat) == resultat