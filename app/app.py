import reflex as rx
from app.pages.landing import landing_page
from app.pages.auth import login_page, register_page
from app.pages.profile import profile_setup_page
from app.pages.dashboard import dashboard_page
from app.pages.matches import matches_page
from app.pages.sessions import sessions_page
from app.pages.knowledge import knowledge_base_page
from app.pages.schedule import schedule_page
from app.pages.admin import admin_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    ],
)
app.add_page(landing_page, route="/")
app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register")
app.add_page(profile_setup_page, route="/profile/setup")
app.add_page(dashboard_page, route="/dashboard")
app.add_page(matches_page, route="/matches")
app.add_page(sessions_page, route="/sessions")
app.add_page(knowledge_base_page, route="/knowledge-base")
app.add_page(schedule_page, route="/schedule")
app.add_page(admin_page, route="/admin")