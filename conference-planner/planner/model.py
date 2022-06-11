from dataclasses import dataclass
from datetime import datetime
from typing import List
from planner.const import KEYWORD


class Specs:
    def __init__(self, conf_data: dict):
        self.name = conf_data[KEYWORD.NAME]
        self.duration = conf_data[KEYWORD.DURATION]
        self.is_networking = conf_data[KEYWORD.IS_NETWORKING]

    def is_networking_track(self) -> bool:
        return self.is_networking

    def __repr__(self) -> str:
        return f"{self.name} {self.duration}"


class ConferenceInfo:
    def __init__(self, json_data: dict):
        self.data: List[Specs] = []
        for conf_data in json_data:
            self.data.append(Specs(conf_data))


@dataclass
class Track:
    name: str
    start_time: datetime
    end_time: datetime

    def __str__(self) -> str:
        return f'{self.start_time.strftime("%H:%M%p")} {self.name}'


@dataclass
class Plan:
    plan: List[Track]
