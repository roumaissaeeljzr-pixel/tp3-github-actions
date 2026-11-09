import pytest
from unittest.mock import patch
from app.surveillance import surveiller


def test_taux_superieur_declenche_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:

        assert surveiller(0.15) == "alerte"

        notifier.assert_called_once_with("Taux eleve")


def test_taux_inferieur_pas_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:

        assert surveiller(0.05) == "ok"

        notifier.assert_not_called()


def test_taux_egal_seuil_pas_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:

        assert surveiller(0.10) == "ok"

        notifier.assert_not_called()


def test_erreur_notification_est_propagee():
    with patch("app.surveillance.envoyer_notification") as notifier:

        notifier.side_effect = RuntimeError(
            "Service indisponible"
        )

        with pytest.raises(RuntimeError):
            surveiller(0.15)