"""Shared timetable choices and display helpers for attendance sessions."""

from datetime import datetime


TIME_SLOTS = (
    ("09:00", "9:00–10:00"),
    ("10:00", "10:00–11:00"),
    ("11:00", "11:00–11:30 (Break)"),
    ("11:30", "11:30–12:30"),
    ("12:30", "12:30–1:30"),
    ("13:30", "1:30–2:30 (Lunch)"),
    ("14:30", "2:30–3:30"),
    ("15:30", "3:30–4:30"),
)

SLOT_LABELS = {start: label for start, label in TIME_SLOTS}


def timestamp_for_slot(slot_start: str, date=None) -> str:
    """Return a consistent session timestamp for the selected timetable period."""
    session_date = date or datetime.now().date()
    return f"{session_date.isoformat()}T{slot_start}:00"


def format_attendance_session(timestamp: str) -> str:
    """Show a saved timestamp as a date plus its timetable period when known."""
    try:
        value = datetime.fromisoformat(timestamp)
    except (TypeError, ValueError):
        return timestamp or "N/A"

    slot_label = SLOT_LABELS.get(value.strftime("%H:%M"))
    if slot_label:
        return f"{value.strftime('%Y-%m-%d')} · {slot_label}"
    return value.strftime("%Y-%m-%d %I:%M %p")
