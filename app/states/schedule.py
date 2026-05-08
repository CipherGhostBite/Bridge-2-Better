import reflex as rx


class ScheduleState(rx.State):
    current_month: str = "October 2024"
    selected_date: str = "Oct 15"
    upcoming_sessions: list[dict[str, str | int]] = [
        {
            "id": "1",
            "title": "AI Fundamentals",
            "mentor": "Dr. Sarah Chen",
            "student": "Alex Rivera",
            "date": "Oct 15",
            "time": "10:00 AM",
            "duration": "60 min",
            "topic": "AI",
            "status": "confirmed",
            "type": "mentoring",
        }
    ]
    reminders: list[dict[str, str | bool]] = [
        {
            "id": "1",
            "text": "Review neural net notes",
            "date": "Oct 14",
            "time": "Evening",
            "is_active": True,
        }
    ]

    @rx.var
    def sessions_for_selected_date(self) -> list[dict[str, str | int]]:
        return [
            s for s in self.upcoming_sessions if s["date"] == self.selected_date
        ]

    @rx.event
    def select_date(self, date: str):
        self.selected_date = date

    @rx.event
    def toggle_reminder(self, id: str):
        for r in self.reminders:
            if r["id"] == id:
                r["is_active"] = not r["is_active"]
                break