import reflex as rx


class ProfileState(rx.State):
    expertise_areas: list[str] = []
    goals: list[str] = []
    skills: list[str] = []
    languages: list[str] = []
    bio: str = ""
    years_experience: str = ""
    institution: str = ""
    current_skill_input: str = ""

    @rx.event
    def add_skill(self):
        if (
            self.current_skill_input
            and self.current_skill_input not in self.skills
        ):
            self.skills.append(self.current_skill_input)
            self.current_skill_input = ""

    @rx.event
    def remove_skill(self, skill: str):
        if skill in self.skills:
            self.skills.remove(skill)

    @rx.event
    def save_profile(self):
        return rx.redirect("/dashboard")