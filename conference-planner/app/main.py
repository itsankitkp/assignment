import json
from os import path

from planner.generator import ConferencePlanner
from planner.model import ConferenceInfo


def entrypoint(file_path: str) -> None:
    """
    Extract json information from given file,
    pass it to conference planner and displays result.
    Args:
        file_path: location of json file containing conference data
    Returns:
        None
    """
    if not path.isfile(file_path):
        raise Exception("Given file path is not valid")

    file_object = open(file_path)  # this will raise IO error if file is not found

    conference_json_data: dict = json.loads(file_object.read())
    conference_information = ConferenceInfo(conference_json_data)
    # extract parsed information
    data = conference_information.data
    track = 1

    # This loop runs till all tracks are allocated.
    # Each time planner is run, it can allocated from 9-5 only
    # Hence, multiple passes are needed
    while len(data) != 0:
        print(f"Track {track}")
        print("-------------------------------------")
        planner = ConferencePlanner(conference_information=data)
        planned_events = planner.get_plan()
        for event in planned_events.plan:
            print(event)
        data = planner.get_conference_data()
        track += 1
        print()
