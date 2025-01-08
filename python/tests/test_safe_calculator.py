import pytest
from safe_calculator import SafeCalculator
from authorizer import Authorizer

def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in
    # SafeCalculator.add

    authorizer = Authorizer(True)
    safeCalculator = SafeCalculator(authorizer)
    try:
        safeCalculator.add(1, 2) == 3
    except Exception as e:
        pytest.fail("Exception raised unexpectedly")
