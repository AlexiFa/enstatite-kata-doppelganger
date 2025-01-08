import pytest
from mail_sender import MailSender, SendMailRequest, SendMailResponse
from http_client import Http_client
from user import User

@pytest.fixture
def user():
    return User("Bob", "bob@bob.fr")

def test_send_v1(user):
    # TODO: write a test that fails due to the bug in MailSender.send_v1

    http_client = Http_client()
    sender = MailSender(http_client)
    sender.send_v1(user, "message")
    assert http_client.requests_history[-1].recipient == user.email
    assert http_client.requests_history[-1].subject == "New notification"
    assert http_client.requests_history[-1].body == "message"


def test_send_v2(user):
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    http_client = Http_client()
    sender = MailSender(http_client)
    response = sender.send_v2(user, "message")
    assert isinstance(http_client.requests_history[-1], SendMailRequest)
    pass
