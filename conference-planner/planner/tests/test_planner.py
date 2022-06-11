import json
from planner.generator import ConferencePlanner
from planner.model import ConferenceInfo


class TestConferencePlanner:
    def setup(self):
        try:
            file_object = open("test_data.json")
        except IOError as e:
            print(f"Unable to read file due to {e}")

        conference_json_data = json.loads(file_object.read())
        conference_information = ConferenceInfo(conference_json_data)
        self.data = conference_information.data

    def test_conference_planner(self):

        planner = ConferencePlanner(self.data)
