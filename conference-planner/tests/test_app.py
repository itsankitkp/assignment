import json
import os
from planner.generator import ConferencePlanner
from planner.model import ConferenceInfo
from planner.const import PlannerConst


class TestApp:
    def setup(self):

        file_object = open(f"{os.path.dirname(__file__)}/test_data.json")

        conference_json_data = json.loads(file_object.read())
        conference_information = ConferenceInfo(conference_json_data)
        self.data = conference_information.data
        planner = ConferencePlanner(self.data)
        self.plan = planner.get_plan().plan

    def test_plan_generation(self):
        assert self.plan is not None

    def test_plan_ordering(self):
        prev = self.plan[0].start_time

        for index in range(1, len(self.plan)):
            assert self.plan[index].start_time > prev
            prev = self.plan[index].start_time

    def test_invalid_entries(self):

        for plan in self.plan:
            assert plan.start_time >= PlannerConst.MORNING_SESSION
            assert plan.end_time <= PlannerConst.SESSION_END
            # no task is scheduled in noon break
            assert not (
                plan.start_time > PlannerConst.NOON_BREAK
                and plan.start_time < PlannerConst.AFTERNOON_SESSION
            )
            assert not plan.start_time > PlannerConst.SESSION_END
