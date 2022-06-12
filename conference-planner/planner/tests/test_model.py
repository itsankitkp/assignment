import pytest
from planner.model import ConferenceInfo


class TestConferencePlannerModel:
    def test_model_validator_missing_keys(self):
        conference_json_data = [
            {"Name": "Overdoing it in Python", "Duration1": 45, "isNetworking": False}
        ]
        with pytest.raises(Exception):
            _ = ConferenceInfo(conference_json_data)

    def test_model_validator_less_duration(self):
        conference_json_data = [
            {"Name": "Overdoing it in Python", "Duration": 4, "isNetworking": False}
        ]
        with pytest.raises(Exception):
            _ = ConferenceInfo(conference_json_data)

    def test_model_validator_wrong_type(self):
        conference_json_data = [
            {"Name": "Overdoing it in Python", "Duration": "45", "isNetworking": False}
        ]
        with pytest.raises(TypeError):
            _ = ConferenceInfo(conference_json_data)

    def test_model_title_having_numbers(self):
        conference_json_data = [
            {"Name": "Overdoing it in Python 1", "Duration": 45, "isNetworking": False}
        ]
        with pytest.raises(ValueError):
            _ = ConferenceInfo(conference_json_data)

    def test_model_validator_wrong_object(self):
        conference_json_data = [object()]
        with pytest.raises(TypeError):
            _ = ConferenceInfo(conference_json_data)
