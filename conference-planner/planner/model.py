from dataclasses import dataclass
from datetime import datetime
from typing import List

from planner.const import KEYWORD
from planner.const import SUPPORTED_KEYS


class Specs:
    def __init__(self, conf_data: dict):
        # validate data
        if not isinstance(conf_data, dict):
            raise TypeError("Conference data should be dict")
        for key, key_type in SUPPORTED_KEYS:
            if key not in conf_data.keys():
                raise Exception(
                    f" Required key {key} is missing"
                )  # This should be custom business exeception
            if not isinstance(conf_data[key], key_type):
                raise TypeError(
                    f"Type of {key} should be {key_type} not {type(conf_data[key])}"
                )

        self.name = conf_data[KEYWORD.NAME]
        self.duration = conf_data[KEYWORD.DURATION]

        if self.duration < 5:
            # Talk duration should not be less than 5
            raise ValueError("Duration less than 5 is not supported")
        # Do we have upper limit on duration ?

        # Validate no number in track name
        if any(char.isdigit() for char in self.name):
            raise ValueError("Talk title can not contain number!")

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
