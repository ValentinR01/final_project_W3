from unittest.mock import patch
import pytest
from services.speaker import create_speaker, get_all_speakers, \
    get_speaker_by_id, update_speaker
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


@pytest.fixture
def data():
    return {'fullname': 'Christina'}


def test_create_speaker_empty_data():
    # Test with empty data
    response = create_speaker(data={})
    assert response == ({'message': 'Missing parameters'}, 400)


def test_create_speaker(data):
    # Test creation of a new speaker
    with patch('models.speaker.Speaker.get_by', return_value=False):
        with patch('models.speaker.Speaker.create', return_value=True):
            response = create_speaker(data)
            assert response == ({'message':
                                'The speaker has been successfully created'},
                                200)


def test_create_speaker_existing_speaker(speaker, data):
    # Test creation of an existing speaker
    with patch('models.speaker.Speaker.get_by', return_value=speaker):
        response = create_speaker(data)
        assert response == ({'message': 'speaker already exists'}, 409)


def test_get_speaker_by_id():
    # Test with an existing speaker
    with patch('models.speaker.Speaker.get_by') as mock_get_by_id:
        speaker_1 = Speaker(fullname='John Doe')
        mock_get_by_id.return_value = speaker_1
        speaker = get_speaker_by_id(1)
        assert speaker == (speaker_1, 200)


def test_get_speaker_by_id_not_existing():
    # Test with a non-existing speaker
    with patch('models.speaker.Speaker.get_by') as mock_get_by_id:
        mock_get_by_id.return_value = None
        speaker = get_speaker_by_id(1000)
        assert speaker == ({'message': 'Speaker not found'}, 404)


def test_get_all_speakers_empty():
    #    Test with an empty list of speakers
    with patch('models.speaker.Speaker.get_all') as mock_get_all:
        mock_speaker_list = []
        mock_get_all.return_value = mock_speaker_list
        speaker_list = get_all_speakers()
        assert speaker_list == ({'speakers': []}, 200)


def test_get_all_speakers():
    #    Test with a list of speakers
    with patch('models.speaker.Speaker.get_all') as mock_get_all:
        mock_speaker_list = [Speaker(fullname='John Doe'),
                             Speaker(fullname='Jane Doe')]
        mock_get_all.return_value = mock_speaker_list
        speaker_list = get_all_speakers()
        assert speaker_list == ({'speakers': mock_speaker_list}, 200)


def test_update_speaker_missing_data(speaker):
    # Test with empty data
    response = update_speaker(data={}, speaker_id=1)
    assert response == ({'message': 'Missing parameters'}, 400)


def test_update_speaker_without_existing_user(speaker, data):
    # Test with non-existing speaker
    with patch('models.speaker.Speaker.get_by', return_value=False):
        response = update_speaker(data=data, speaker_id=99999)
        assert response == ({'message': 'Entity not found'}, 404)


def test_update_speaker(speaker, data):
    # Test with an existing speaker
    with patch('models.speaker.Speaker.get_by', return_value=speaker):
        with patch('models.speaker.Speaker.update', return_value=True):
            response = update_speaker(data=data, speaker_id=1)
            assert response == ({'message':
                                'The speaker has been successfully updated'},
                                200)
