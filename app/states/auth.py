import reflex as rx
from typing import Any


class AuthState(rx.State):
    users: dict[str, dict[str, str]] = {
        "mentor1@example.com": {
            "email": "mentor1@example.com",
            "password": "password",
            "name": "Dr. Sarah Chen",
            "role": "Mentor",
        },
        "mentor2@example.com": {
            "email": "mentor2@example.com",
            "password": "password",
            "name": "James Wilson",
            "role": "Mentor",
        },
        "mentor3@example.com": {
            "email": "mentor3@example.com",
            "password": "password",
            "name": "Prof. Alan Turing",
            "role": "Mentor",
        },
        "student1@example.com": {
            "email": "student1@example.com",
            "password": "password",
            "name": "Alex Rivera",
            "role": "Student",
        },
        "student2@example.com": {
            "email": "student2@example.com",
            "password": "password",
            "name": "Jordan Lee",
            "role": "Student",
        },
        "student3@example.com": {
            "email": "student3@example.com",
            "password": "password",
            "name": "Casey Smith",
            "role": "Student",
        },
        "admin@example.com": {
            "email": "admin@example.com",
            "password": "password",
            "name": "System Admin",
            "role": "Admin",
        },
    }
    email: str = ""
    password: str = ""
    confirm_password: str = ""
    name: str = ""
    role: str = "Student"
    is_authenticated: bool = False
    current_user: dict[str, str] = {}

    @rx.var
    def user_name(self) -> str:
        return self.current_user.get("name", "User")

    @rx.var
    def user_role(self) -> str:
        return self.current_user.get("role", "Student")

    @rx.var
    def user_initial(self) -> str:
        name = self.current_user.get("name", "User")
        return name[:1].upper() if name else "U"

    @rx.event
    def login(self):
        user = self.users.get(self.email)
        if user and user.get("password") == self.password:
            self.is_authenticated = True
            self.current_user = user
            self.password = ""
            return rx.redirect("/dashboard")
        else:
            return rx.toast.error("Invalid email or password")

    @rx.event
    def register(self):
        if not self.email or not self.password or (not self.name):
            return rx.toast.error("Please fill in all fields")
        if self.password != self.confirm_password:
            return rx.toast.error("Passwords do not match")
        if self.email in self.users:
            return rx.toast.error("Email already exists")
        new_user = {
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "role": self.role,
        }
        self.users[self.email] = new_user
        self.is_authenticated = True
        self.current_user = new_user
        self.password = ""
        self.confirm_password = ""
        return rx.redirect("/profile/setup")

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.current_user = {}
        self.email = ""
        return rx.redirect("/")