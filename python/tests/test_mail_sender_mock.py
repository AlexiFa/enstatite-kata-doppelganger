import pytest
from unittest.mock import Mock
from mail_sender import MailSender, SendMailRequest, SendMailResponse
from http_client import Http_client
from user import User

@pytest.fixture
def user():
    return User("Bob", "bob@bob.fr")

def test_send_v1(user):
    mock_http_client = Mock(spec=Http_client)
    sender = MailSender(mock_http_client)

    sender.send_v1(user, "message")

    # Verify that the last request sent matches the expected values
    last_request = mock_http_client.requests_history[-1]
    assert last_request.recipient == user.email
    assert last_request.subject == "New notification"
    assert last_request.body == "message"

def test_send_v2(user):
    mock_http_client = Mock(spec=Http_client)
    sender = MailSender(mock_http_client)

    response = sender.send_v2(user, "message")

    # Verify that the last request is an instance of SendMailRequest
    last_request = mock_http_client.requests_history[-1]
    assert isinstance(last_request, SendMailRequest)

    # Verify that the response is an instance of SendMailResponse
    assert isinstance(response, SendMailResponse)
