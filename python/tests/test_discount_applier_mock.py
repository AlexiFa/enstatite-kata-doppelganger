import pytest
from unittest.mock import Mock
from discount_applier import DiscountApplier
from notifier import Notifier


@pytest.fixture
def setup():
    mock_notifier = Mock(spec=Notifier)
    discount_applier = DiscountApplier(mock_notifier)

    yield mock_notifier, discount_applier


def test_apply_v1(setup):
    mock_notifier, discount_applier = setup

    discount_applier.apply_v1(10, ["Alice", "Bob", "Charlie"])

    # Verify that the notifier was called 3 times
    assert mock_notifier.notify.call_count == 3

    # Verify the content of the notifications
    expected_calls = [
        (("Alice", "You've got a new discount of 10%"),),
        (("Bob", "You've got a new discount of 10%"),),
        (("Charlie", "You've got a new discount of 10%"),)
    ]
    mock_notifier.notify.assert_has_calls(expected_calls, any_order=True)


def test_apply_v2(setup):
    mock_notifier, discount_applier = setup

    discount_applier.apply_v2(10, ["Alice", "Bob", "Charlie"])

    # Verify that the notifier was called 3 times
    assert mock_notifier.notify.call_count == 3

    # Verify the content of the notifications
    expected_calls = [
        (("Alice", "You've got a new discount of 10%"),),
        (("Bob", "You've got a new discount of 10%"),),
        (("Charlie", "You've got a new discount of 10%"),)
    ]
    mock_notifier.notify.assert_has_calls(expected_calls, any_order=True)
