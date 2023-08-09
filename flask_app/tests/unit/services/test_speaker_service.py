from unittest.mock import patch
import pytest
from services.speaker import register_service, get_all_speakers, get_speaker_by_id
from models.speaker import Speaker


@pytest.fixture
def speaker():
    return Speaker(
        fullname="Christina",
        biography="",
        last_update=1689087134,
        publishable=0,
        speaker_parent=None,
        language_id=None
    )


def test_register_service(speaker):
    data = {'fullname': 'Christina'}

    # Test creation of a new speaker
    with patch('models.speaker.Speaker.get_by', return_value=False):
        with patch('models.speaker.Speaker.create', return_value=True):
            response = register_service(data)
            assert response == ({'message': 'Speaker well created'}, 201)

    # Test creation of an existing speaker
    with patch('models.speaker.Speaker.get_by', return_value=speaker):
        response = register_service(data)
        assert response == ({'message': 'Speaker already exists'}, 409)


def test_get_speaker_by_id():
    # Test with an existing speaker
    with patch('models.speaker.Speaker.get_by') as mock_get_by_id:
        speaker_1 = Speaker(fullname='John Doe')
        mock_get_by_id.return_value = speaker_1
        speaker = get_speaker_by_id(1)
        assert speaker == (speaker_1, 200)

    # Test with an existing speaker
    with patch('models.speaker.Speaker.get_by') as mock_get_by_id:
        mock_get_by_id.return_value = None
        speaker = get_speaker_by_id(1000)
        assert speaker == ({'message': 'Speaker not found'}, 404)


def test_get_all_speakers():
    #    Test with a list of speakers
    with patch('models.speaker.Speaker.get_all') as mock_get_all:
        mock_speaker_list = [Speaker(fullname='John Doe'), Speaker(fullname='Jane Doe')]
        mock_get_all.return_value = mock_speaker_list
        speaker_list = get_all_speakers()
        assert speaker_list == ({'speakers': mock_speaker_list}, 200)

    #    Test with an empty list of speakers
    with patch('models.speaker.Speaker.get_all') as mock_get_all:
        mock_speaker_list = []
        mock_get_all.return_value = mock_speaker_list
        speaker_list = get_all_speakers()
        assert speaker_list == ({'speakers': []}, 200)
