import pytest

from app.main import entrypoint
class TestConferenceMain:


    def test_wrong_file_path(self):
        with pytest.raises(IOError):
            entrypoint('/dev/random')

            
    # def test_model_validator_wrong_type(self):
    #     conference_json_data =     [{
    #     "Name": "Overdoing it in Python",
    #     "Duration": '45',
    #     "isNetworking": False
    #     }]
    #     with pytest.raises(TypeError):
    #         _ = ConferenceInfo(conference_json_data)
            
    # def test_model_validator_wrong_object(self):
    #     conference_json_data =     [object()]
    #     with pytest.raises(TypeError):
    #         _ = ConferenceInfo(conference_json_data)

        
