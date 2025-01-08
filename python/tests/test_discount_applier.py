import pytest
from discount_applier import DiscountApplier
from notifier import Notifier

@pytest.fixture
def setup():
    notifier = Notifier()
    discount_applier = DiscountApplier(notifier)
    
    yield notifier, discount_applier

    del notifier, discount_applier

def test_apply_v1(setup):
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v1

    notifier, discount_applier = setup

    discount_applier.apply_v1(10, ["Alice", "Bob", "Charlie"])

    # assert notifier.notifs == [
    #     ("Alice", "You've got a new discount of 10%"),
    #     ("Bob", "You've got a new discount of 10%"),
    #     ("Charlie", "You've got a new discount of 10%")
    # ]

    assert len(notifier.notifs) == 3


def test_apply_v2(setup):
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2

    notifier, discount_applier = setup

    discount_applier.apply_v1(10, ["Alice", "Bob", "Charlie"])

    assert notifier.notifs == [
        ("Alice", "You've got a new discount of 10%"),
        ("Bob", "You've got a new discount of 10%"),
        ("Charlie", "You've got a new discount of 10%")
    ]
