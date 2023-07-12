from unittest.mock import patch
import pytest
from services.speaker import register_service, get_all_speakers
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



# def test_get_all_speakers():
#     with patch('models.speaker.Speaker.get_by') as mock_get_all:
#         mock_speaker_list = [Speaker(fullname='John Doe'), Speaker(fullname='Jane Doe')]
#         mock_get_all.return_value = mock_speaker_list
#         speaker_list = get_all_speakers()
#         assert speaker_list == (mock_speaker_list, 200)

