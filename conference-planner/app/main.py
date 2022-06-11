import json
from planner.model import Plan, ConferenceInfo
from planner.generator import ConferencePlanner


def entrypoint(file_path: str) -> None:
    """
    Extract json information from given file,
    pass it to conference planner and displays result.
    Args:
        file_path: location of json file containing conference data
    Returns:
        None
    """
    try:
        file_object = open(file_path)
    except IOError as e:
        print(f"Unable to read file due to {e}")

    conference_json_data = json.loads(file_object.read())
    conference_information = ConferenceInfo(conference_json_data)
    data = conference_information.data
    track=1
    while len(data) != 0:
        print(f'Track {track}')
        print('-------------------------------------')
        planner = ConferencePlanner(conference_information=data)
        planned_events = planner.get_plan()
        for event in planned_events:
            print(event)
        data = planner.get_conference_data()
        track+=1
    # final_plan: Plan =

    # print(final_plan)
