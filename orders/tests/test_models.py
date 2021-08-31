from decimal import Decimal

import pytest

from ..models import Item, Order

pytestmark = pytest.mark.django_db


def test__str__(product):
    order = Order.objects.create(
        cpf="111.142.222-10",
        name="Ademar",
        email="test@ademar.com",
        postal_code="89226-270",
        address="Rua Habib Farah",
        number="123",
        district="Centro",
        state="SC",
        city="Joinville",
    )

    assert order.__str__() == f"Pedido {order.id}"
    assert str(order) == f"Pedido {order.id}"

    item = Item.objects.create(
        order=order,
        product=product,
        price=Decimal(10),
        quantity=1,
    )

    assert item.__str__() == str(item.id)
    assert str(item) == str(item.id)
