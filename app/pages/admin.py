import reflex as rx
from app.components.layout import app_layout
from app.states.admin import AdminState


def stat_box(label: str, value: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(label, class_name="text-sm text-gray-500 font-medium mb-1"),
        rx.el.p(value, class_name="text-3xl font-bold text-gray-900"),
        class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm",
    )


def user_row(user: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            user["name"], class_name="py-4 px-6 text-sm font-bold text-gray-900"
        ),
        rx.el.td(user["email"], class_name="py-4 px-6 text-sm text-gray-500"),
        rx.el.td(user["role"], class_name="py-4 px-6 text-sm font-medium"),
        rx.el.td(
            user["status"],
            class_name="py-4 px-6 text-sm uppercase text-gray-500",
        ),
        rx.el.td(
            user["sessions_count"], class_name="py-4 px-6 text-sm text-gray-500"
        ),
        class_name="border-b border-gray-50",
    )


def admin_page() -> rx.Component:
    return app_layout(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Admin Dashboard",
                    class_name="text-2xl font-bold text-gray-900",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    stat_box(
                        "Total Users",
                        AdminState.platform_stats["total_users"].to(str),
                    ),
                    stat_box(
                        "Active Mentors",
                        AdminState.platform_stats["active_mentors"].to(str),
                    ),
                    stat_box(
                        "Active Students",
                        AdminState.platform_stats["active_students"].to(str),
                    ),
                    stat_box(
                        "Total Sessions",
                        AdminState.platform_stats["total_sessions"].to(str),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12",
                ),
                rx.el.div(
                    rx.el.h2(
                        "User Management", class_name="text-xl font-bold mb-4"
                    ),
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Name",
                                    class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase",
                                ),
                                rx.el.th(
                                    "Email",
                                    class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase",
                                ),
                                rx.el.th(
                                    "Role",
                                    class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase",
                                ),
                                rx.el.th(
                                    "Status",
                                    class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase",
                                ),
                                rx.el.th(
                                    "Sessions",
                                    class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase",
                                ),
                                class_name="bg-gray-50 rounded-t-xl",
                            )
                        ),
                        rx.el.tbody(
                            rx.foreach(AdminState.filtered_users, user_row)
                        ),
                        class_name="w-full bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden",
                    ),
                ),
            ),
        ),
        title="Admin Dashboard",
    )