from datetime import timedelta
from planner.model import Plan, Track
from planner.const import PlannerConst


class ConferencePlanner:
    def __init__(self, conference_information: dict) -> None:
        # Stack to store networking track
        self.networking_tracks = [
            conf_info
            for conf_info in conference_information
            if conf_info.is_networking_track()
        ]
        self.general_tracks = list(
            set(conference_information) - set(self.networking_tracks)
        )
        self.planned_track: Plan = Plan(plan=[])

    def get_conference_data(self):
        return self.general_tracks + self.networking_tracks

    def get_plan(self) -> Plan:
        """
        Allocate and generate plan

        Returns:
            Plan: resultant plan
        """
        # List out all sessions
        # Note: if there is no networking event,
        # allocated general track in networking event time
        sessions = [
            (
                PlannerConst.MORNING_SESSION,
                PlannerConst.NOON_BREAK,
                self.general_tracks,
            ),
            (
                PlannerConst.AFTERNOON_SESSION,
                PlannerConst.NETWORKING_SESSION,
                self.general_tracks,
            ),
            (
                PlannerConst.NETWORKING_SESSION,
                PlannerConst.SESSION_END,
                self.networking_tracks
                if not self.is_networking_track_empty()
                else self.general_tracks,
            ),
        ]
        for start, end, track in sessions:
            self.allocate_track(start, end, track)
        return self.planned_track

    def allocate_track(self, session_start, session_end, tracks):
        curr_time = session_start

        completed_tracks = []
        for conf_info in tracks:

            end_time = curr_time + timedelta(minutes=conf_info.duration)

            if end_time > session_end or (
                end_time == (session_end - timedelta(minutes=15)) and len(tracks) != 1
            ):
                # skip, don't have enough leftover time to allocate
                continue

            # allocate track
            current_track = Track(
                name=conf_info.name, start_time=curr_time, end_time=end_time
            )
            self.planned_track.plan.append(current_track)
            completed_tracks.append(conf_info)
            curr_time = end_time
            if curr_time == PlannerConst.SESSION_END:
                break
        # remove completed track from pending tracks
        for completed_track in completed_tracks:
            if (
                session_start == PlannerConst.NETWORKING_SESSION
                and not self.is_networking_track_empty()
            ):
                self.networking_tracks.remove(completed_track)
            else:

                self.general_tracks.remove(completed_track)

    def is_networking_track_empty(self):
        return len(self.networking_tracks) == 0
