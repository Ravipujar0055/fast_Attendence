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
# Store the selected period in the seconds field so the existing timestamp-only
# database schema can retain both the actual attendance time and its slot.
SLOT_SECONDS = {start: index + 10 for index, (start, _) in enumerate(TIME_SLOTS)}
SECONDS_SLOTS = {seconds: start for start, seconds in SLOT_SECONDS.items()}


def timestamp_for_attendance(slot_start: str, taken_at=None) -> str:
    """Save the real attendance time while retaining the selected timetable slot."""
    taken_at = taken_at or datetime.now()
    return taken_at.replace(
        second=SLOT_SECONDS[slot_start],
        microsecond=0,
    ).isoformat()


def format_attendance_session(timestamp: str) -> str:
    """Show a saved timestamp as a date plus its timetable period when known."""
    try:
        value = datetime.fromisoformat(timestamp)
    except (TypeError, ValueError):
        return timestamp or "N/A"

    # New entries encode the selected slot in their seconds value. For records
    # created before this change, fall back to the old period-start timestamp.
    slot_start = SECONDS_SLOTS.get(value.second) or value.strftime("%H:%M")
    slot_label = SLOT_LABELS.get(slot_start)
    if slot_label:
        return f"{value.strftime('%Y-%m-%d %I:%M %p')} · {slot_label}"
    return value.strftime("%Y-%m-%d %I:%M %p")
