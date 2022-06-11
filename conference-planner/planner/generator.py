from datetime import timedelta
from planner.model import Plan, ConferenceInfo, Track
from planner.const import PlannerConst


class ConferencePlanner:
    def __init__(self, conference_data: dict) -> None:
        self.conference_information = ConferenceInfo(conference_data)
        # Stack to store networking track
        self.networking_tracks = [
            conf_info
            for conf_info in self.conference_information.data
            if conf_info.is_networking_track()
        ]
        self.general_tracks = list(
            set(self.conference_information.data) - set(self.networking_tracks)
        )
        self.planned_track: Plan = Plan(plan=[])

    def generate_plan(conference_data: dict):

        allocated_time = PlannerConst.MORNING_SESSION

    def allocate_morning_plan(self):

        curr_time = PlannerConst.MORNING_SESSION
        for conf_info in self.general_tracks:

            end_time = curr_time + timedelta(minutes=conf_info.duration)

            if end_time > PlannerConst.NOON_BREAK or (
                end_time == (PlannerConst.NOON_BREAK - timedelta(minutes=15))
            ):
                # skip, don't have enough time to allocate
                continue

            # allocate track
            current_track = Track(
                name=conf_info.name, start_time=curr_time, end_time=end_time
            )
            self.planned_track.plan.append(current_track)
            self.general_tracks.remove(conf_info)
            curr_time = end_time

    def allocate_afternoon_plan(self):
        curr_time = PlannerConst.AFTERNOON_SESSION
        for conf_info in self.general_tracks:

            end_time = curr_time + timedelta(minutes=conf_info.duration)

            if end_time > PlannerConst.NETWORKING_SESSION or (
                end_time == (PlannerConst.NETWORKING_SESSION - timedelta(minutes=15))
            ):
                # skip, don't have enough time to allocate
                continue

            # allocate track
            current_track = Track(
                name=conf_info.name, start_time=curr_time, end_time=end_time
            )
            self.planned_track.plan.append(current_track)
            self.general_tracks.remove(conf_info)
            curr_time = end_time

    def allocate_networking_plan(self):
        init_time = PlannerConst.NETWORKING_SESSION
        pass
