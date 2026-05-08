import reflex as rx


class AdminState(rx.State):
    platform_stats: dict[str, int | float] = {
        "total_users": 1542,
        "active_mentors": 520,
        "active_students": 1022,
        "total_sessions": 12500,
        "avg_rating": 4.8,
        "knowledge_items": 3400,
    }
    engagement_data: list[dict[str, str | int]] = [
        {"month": "May", "sessions": 1200, "users": 800},
        {"month": "Jun", "sessions": 1500, "users": 950},
        {"month": "Jul", "sessions": 1800, "users": 1100},
    ]
    skill_adoption: list[dict[str, str | int]] = [
        {"skill": "Python", "count": 850, "growth_pct": 15},
        {"skill": "Machine Learning", "count": 620, "growth_pct": 25},
    ]
    user_management_data: list[dict[str, str | int]] = [
        {
            "name": "Dr. Sarah Chen",
            "email": "mentor1@example.com",
            "role": "Mentor",
            "status": "active",
            "join_date": "Jan 12, 2024",
            "sessions_count": 45,
            "last_active": "2 hours ago",
        },
        {
            "name": "Alex Rivera",
            "email": "student1@example.com",
            "role": "Student",
            "status": "active",
            "join_date": "Feb 05, 2024",
            "sessions_count": 12,
            "last_active": "1 day ago",
        },
    ]
    selected_admin_tab: str = "overview"
    search_users_query: str = ""

    @rx.var
    def filtered_users(self) -> list[dict[str, str | int]]:
        if not self.search_users_query:
            return self.user_management_data
        return [
            u
            for u in self.user_management_data
            if self.search_users_query.lower() in str(u["name"]).lower()
        ]

    @rx.event
    def set_admin_tab(self, tab: str):
        self.selected_admin_tab = tab

    @rx.event
    def set_search_users_query(self, value: str):
        self.search_users_query = value

    @rx.event
    def toggle_user_status(self, email: str):
        for u in self.user_management_data:
            if u["email"] == email:
                u["status"] = (
                    "inactive" if u["status"] == "active" else "active"
                )
                break