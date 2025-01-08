import pytest
from unittest.mock import Mock
from safe_calculator import SafeCalculator
from authorizer import Authorizer


def test_divide_should_not_raise_any_error_when_authorized():
    # Mock the Authorizer to always return True
    mock_authorizer = Mock(spec=Authorizer)
    mock_authorizer.authorize.return_value = True

    safe_calculator = SafeCalculator(mock_authorizer)

    # Test that the add method works without raising an exception
    try:
        assert safe_calculator.add(1, 2) == 3
    except Exception as e:
        pytest.fail(f"Exception raised unexpectedly: {e}")

    # Verify that the authorize method was called
    mock_authorizer.authorize.assert_called_once()
