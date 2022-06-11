from datetime import date, datetime, timedelta
from typing import List

from planner.const import PlannerConst
from planner.model import Plan
from planner.model import Track


class ConferencePlanner:
    def __init__(self, conference_information: dict) -> None:
        # Store networking track
        self.networking_tracks = [
            conf_info
            for conf_info in conference_information
            if conf_info.is_networking_track()
        ]
        # track not networking track is general track
        self.general_tracks = list(
            set(conference_information) - set(self.networking_tracks)
        )
        self.planned_track: Plan = Plan(plan=[])

    def get_conference_data(self) -> List:
        return self.general_tracks + self.networking_tracks

    def get_plan(self) -> Plan:
        """
        Allocate and generate plan for all sessions

        Returns:
            Plan: resultant plan
        """

        # If there is no networking track, general tracks gets
        # allocated during 4-5 pm
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

    def allocate_track(
        self, session_start: datetime, session_end: datetime, tracks: List[Track]
    ):
        """
        Allocates track to conference Plan.
        Allocation is done without any preference.
        Once allocation is done, track is removed from general tracks

        Args:
            session_start (datetime): start time
            session_end (datetime): end time of session
            tracks (List[Track]): list of tracks
        """
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
            # Need to remove either general track or network track
            # depending on what track we are allocating
            # If there is no networking track, general tracks gets
            # allocated during 4-5 pm
            if (
                session_start == PlannerConst.NETWORKING_SESSION
                and not self.is_networking_track_empty()
            ):
                self.networking_tracks.remove(completed_track)
            else:

                self.general_tracks.remove(completed_track)

    def is_networking_track_empty(self) -> bool:
        """
            Returns true if no networking tracks are left

        Returns:
            bool: tre/false depending on length of networking tracks
        """
        return len(self.networking_tracks) == 0
