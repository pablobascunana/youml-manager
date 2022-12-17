from datetime import datetime, timedelta, timezone


def date_now_plus_delta_in_minutes(time: int) -> datetime:
    return datetime.now(tz=timezone.utc) + timedelta(minutes=time)
