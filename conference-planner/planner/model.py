from dataclasses import dataclass
import json
from typing import List
from planner.const import KEYWORD


@dataclass
class Plan:
    plan: str


class Track:
    def __init__(self, conf_data: dict):
        self.name = conf_data[KEYWORD.NAME]
        self.duration = conf_data[KEYWORD.DURATION]
        self.is_networking = conf_data[KEYWORD.IS_NETWORKING]

    def is_networkin(self) -> bool:
        return self.is_networking


class ConferenceInfo:
    def __init__(self, json_data: dict):
        self.data: List[Track] = []
        for conf_data in json_data:
            self.data.append(Track(conf_data))
