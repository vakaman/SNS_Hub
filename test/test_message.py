

import json
import uuid
import pytest
from src.models.message import Message

@pytest.fixture
def valid_content():
    return {'text': 'Hello, World!'}


@pytest.fixture
def invalid_content():
    return {'correlation_id': 'invalid-uuid'}


def test_get_content(valid_content):
    message = Message(valid_content)
    assert message.get_content() == json.dumps(valid_content)


def test_generate_correlation_id(valid_content):
    message = Message(valid_content)
    assert 'correlation_id' in message.content
    assert uuid.UUID(message.content['correlation_id'])


def test_invalid_correlation_id(invalid_content):
    with pytest.raises(ValueError) as excinfo:
        Message(invalid_content)
    assert "Invalid correlation_id" in str(excinfo.value)


def test_valid_correlation_id(valid_content):
    valid_content_with_id = valid_content.copy()
    valid_content_with_id['correlation_id'] = str(uuid.uuid4())
    message = Message(valid_content_with_id)
    assert 'correlation_id' in message.content
    assert uuid.UUID(message.content['correlation_id'])
