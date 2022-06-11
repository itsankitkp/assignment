import json
from planner.model import Plan
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

    conference_data = json.loads(file_object.read())

    planner = ConferencePlanner(conference_data=conference_data)
    planner.allocate_morning_plan()
    # final_plan: Plan =

    # print(final_plan)
