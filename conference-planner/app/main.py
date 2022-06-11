import json
from planner.model import Plan
from planner.generator import generate_plan


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

    final_plan: Plan = generate_plan(conference_data=conference_data)

    print(final_plan)
