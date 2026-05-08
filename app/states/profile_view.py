import reflex as rx
from typing import Any


class ProfileViewState(rx.State):
    viewed_profiles: list[dict[str, str | list[str] | list[dict[str, str]]]] = [
        {
            "name": "Dr. Sarah Chen",
            "role": "Mentor",
            "email": "mentor1@example.com",
            "bio": "AI Researcher",
            "institution": "Tech Univ",
            "years_experience": "15",
            "skills": ["AI", "Python"],
            "expertise_areas": ["Machine Learning"],
            "learning_goals": ["Cloud Architecture"],
            "badges": [{"name": "Top Mentor", "icon": "star"}],
            "session_history": [],
            "languages": ["English", "Mandarin"],
            "availability": "Weekends",
        }
    ]
    selected_profile_index: int = 0

    @rx.event
    def view_profile(self, index: int):
        self.selected_profile_index = index

    @rx.var
    def current_profile(
        self,
    ) -> dict[str, str | list[str] | list[dict[str, str]]]:
        if 0 <= self.selected_profile_index < len(self.viewed_profiles):
            return self.viewed_profiles[self.selected_profile_index]
        return {}