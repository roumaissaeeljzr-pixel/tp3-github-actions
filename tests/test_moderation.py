import pytest
from unittest.mock import Mock
from app.moderation import decider


def test_message_spam_est_bloque():
    modele = Mock()
    modele.predict.return_value = "spam"

    assert decider(modele, "Offre miracle") == "bloquer"

    modele.predict.assert_called_once_with(
        "Offre miracle"
    )


def test_message_normal_est_autorise():
    modele = Mock()
    modele.predict.return_value = "normal"

    assert decider(modele, "Bonjour") == "autoriser"

    modele.predict.assert_called_once_with("Bonjour")


def test_erreur_modele_est_propagee():
    modele = Mock()

    modele.predict.side_effect = RuntimeError(
        "Modele indisponible"
    )

    with pytest.raises(RuntimeError):
        decider(modele, "Un message")