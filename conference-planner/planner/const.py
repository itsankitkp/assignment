from datetime import datetime


class KEYWORD:
    NAME = "Name"
    DURATION = "Duration"
    IS_NETWORKING = "isNetworking"


SUPPORTED_KEYS = [
    (KEYWORD.NAME, str),
    (KEYWORD.DURATION, int),
    (KEYWORD.IS_NETWORKING, bool),
]


class PlannerConst:
    NOW = datetime.now()  # Not tz aware

    MORNING_SESSION = datetime(
        year=NOW.year, month=NOW.month, day=NOW.day, hour=9, minute=0
    )

    # 12:00 PM Noon today
    NOON_BREAK = datetime(
        year=NOW.year, month=NOW.month, day=NOW.day, hour=12, minute=0
    )

    AFTERNOON_SESSION = datetime(
        year=NOW.year, month=NOW.month, day=NOW.day, hour=13, minute=0
    )

    NETWORKING_SESSION = datetime(
        year=NOW.year, month=NOW.month, day=NOW.day, hour=16, minute=0
    )

    SESSION_END = datetime(
        year=NOW.year, month=NOW.month, day=NOW.day, hour=17, minute=0
    )
