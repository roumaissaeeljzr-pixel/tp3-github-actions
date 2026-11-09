import pytest
from app.reservation import Stock, Reservation


@pytest.fixture
def stock():
    return Stock(5)


def test_reservation_deux_unites(stock):
    reservation = Reservation(stock)

    assert reservation.reserver(2) == "confirmee"
    assert stock.quantite == 3


def test_reservation_refusee(stock):
    reservation = Reservation(stock)

    assert reservation.reserver(6) == "refusee"
    assert stock.quantite == 5


def test_reservation_tout_le_stock(stock):
    reservation = Reservation(stock)

    assert reservation.reserver(5) == "confirmee"
    assert stock.quantite == 0


def test_reservation_quantite_nulle(stock):
    reservation = Reservation(stock)

    with pytest.raises(ValueError):
        reservation.reserver(0)

    assert stock.quantite == 5