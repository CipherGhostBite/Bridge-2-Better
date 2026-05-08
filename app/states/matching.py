import reflex as rx
from typing import Any


class MatchingState(rx.State):
    matches: list[dict[str, str | int | list[str]]] = [
        {
            "id": "1",
            "mentor_name": "Dr. Sarah Chen",
            "mentor_role": "Mentor",
            "mentor_skills": ["AI", "Research"],
            "mentor_avatar_initial": "S",
            "student_name": "Alex Rivera",
            "student_role": "Student",
            "student_skills": ["Python", "Data"],
            "student_avatar_initial": "A",
            "compatibility_score": 95,
            "mutual_learning_score": 88,
            "skill_overlap": ["Python"],
            "mentor_teaches": ["Machine Learning"],
            "student_teaches": ["Digital Marketing"],
            "status": "suggested",
        },
        {
            "id": "2",
            "mentor_name": "James Wilson",
            "mentor_role": "Mentor",
            "mentor_skills": ["Leadership"],
            "mentor_avatar_initial": "J",
            "student_name": "Jordan Lee",
            "student_role": "Student",
            "student_skills": ["Design"],
            "student_avatar_initial": "J",
            "compatibility_score": 82,
            "mutual_learning_score": 75,
            "skill_overlap": ["Communication"],
            "mentor_teaches": ["Management"],
            "student_teaches": ["Figma"],
            "status": "accepted",
        },
    ]
    selected_match_index: int = -1
    filter_status: str = "all"

    @rx.event
    def select_match(self, index: int):
        self.selected_match_index = index

    @rx.event
    def accept_match(self, index: int):
        if 0 <= index < len(self.matches):
            self.matches[index]["status"] = "accepted"
            return rx.toast.success("Match Accepted!")

    @rx.event
    def filter_matches(self, status: str):
        self.filter_status = status
        self.selected_match_index = -1

    @rx.var
    def filtered_matches(self) -> list[dict[str, str | int | list[str]]]:
        if self.filter_status == "all":
            return self.matches
        return [m for m in self.matches if m["status"] == self.filter_status]

    @rx.var
    def selected_match(self) -> dict[str, str | int | list[str]]:
        if 0 <= self.selected_match_index < len(self.filtered_matches):
            return self.filtered_matches[self.selected_match_index]
        return {}

    @rx.var
    def selected_match_mentor_name(self) -> str:
        match = self.selected_match
        return str(match.get("mentor_name", "")) if match else ""

    @rx.var
    def selected_match_student_name(self) -> str:
        match = self.selected_match
        return str(match.get("student_name", "")) if match else ""