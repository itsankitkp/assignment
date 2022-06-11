import pytest
from planner.generator import ConferencePlanner
from planner.model import ConferenceInfo


class TestConferencePlannerModel:
    def test_model_validator_missing_keys(self):
        conference_json_data = [
            {"Name": "Overdoing it in Python", "Duration1": 45, "isNetworking": False}
        ]
        with pytest.raises(Exception):
            _ = ConferenceInfo(conference_json_data)

    def test_model_validator_wrong_type(self):
        conference_json_data = [
            {"Name": "Overdoing it in Python", "Duration": "45", "isNetworking": False}
        ]
        with pytest.raises(TypeError):
            _ = ConferenceInfo(conference_json_data)

    def test_model_validator_wrong_object(self):
        conference_json_data = [object()]
        with pytest.raises(TypeError):
            _ = ConferenceInfo(conference_json_data)
