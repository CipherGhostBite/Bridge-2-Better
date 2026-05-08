import reflex as rx
from app.components.layout import app_layout
from app.states.dashboard import DashboardState


def stat_card(stat: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(stat["icon"], class_name="h-6 w-6 text-indigo-600"),
            class_name="w-12 h-12 rounded-full bg-indigo-50 flex items-center justify-center mb-4",
        ),
        rx.el.div(
            stat["value"], class_name="text-3xl font-bold text-gray-900 mb-1"
        ),
        rx.el.div(
            stat["label"], class_name="text-sm text-gray-500 font-medium"
        ),
        rx.el.div(
            stat["change"],
            class_name="text-xs text-emerald-600 mt-2 font-medium",
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm",
    )


def activity_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                item["avatar_initial"],
                class_name="text-sm font-bold text-indigo-600",
            ),
            class_name="w-10 h-10 rounded-full bg-indigo-50 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.p(
                rx.el.span(
                    item["user"], class_name="font-semibold text-gray-900"
                ),
                " ",
                item["action"],
                class_name="text-sm text-gray-600",
            ),
            rx.el.p(item["time"], class_name="text-xs text-gray-400 mt-1"),
            class_name="flex-1",
        ),
        class_name="flex items-start gap-4 p-4 border-b border-gray-50 last:border-0",
    )


def session_row(session: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            session["mentor"],
            class_name="py-4 px-6 text-sm font-medium text-gray-900",
        ),
        rx.el.td(
            session["student"], class_name="py-4 px-6 text-sm text-gray-500"
        ),
        rx.el.td(
            session["topic"], class_name="py-4 px-6 text-sm text-gray-500"
        ),
        rx.el.td(
            f"{session['date']} at {session['time']}",
            class_name="py-4 px-6 text-sm text-gray-500",
        ),
        rx.el.td(
            session["status"], class_name="py-4 px-6 text-sm text-gray-500"
        ),
        class_name="border-b border-gray-50 last:border-0",
    )


def dashboard_page() -> rx.Component:
    return app_layout(
        rx.el.div(
            rx.el.div(
                rx.foreach(DashboardState.stats, stat_card),
                class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Recent Activity",
                        class_name="text-lg font-semibold text-gray-900 mb-4 px-4 pt-4",
                    ),
                    rx.el.div(
                        rx.foreach(
                            DashboardState.recent_activity, activity_item
                        ),
                        class_name="overflow-y-auto max-h-[400px]",
                    ),
                    class_name="bg-white rounded-2xl border border-gray-100 shadow-sm col-span-2",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Learning Progress",
                        class_name="text-lg font-semibold text-gray-900 mb-4 px-4 pt-4",
                    ),
                    rx.el.div(
                        rx.foreach(
                            DashboardState.learning_progress,
                            lambda track: rx.el.div(
                                rx.el.div(
                                    track["track"],
                                    class_name="text-sm font-medium text-gray-700",
                                ),
                                rx.el.div(
                                    f"{track['progress']}%",
                                    class_name="text-sm text-gray-500",
                                ),
                                class_name="flex justify-between mb-2",
                            ),
                        ),
                        class_name="p-4",
                    ),
                    class_name="bg-white rounded-2xl border border-gray-100 shadow-sm",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
            ),
            rx.el.div(
                rx.el.h3(
                    "Upcoming Sessions",
                    class_name="text-lg font-semibold text-gray-900 mb-4 p-4",
                ),
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Mentor",
                                class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Student",
                                class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Topic",
                                class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Date/Time",
                                class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="text-left py-3 px-6 text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            class_name="bg-gray-50",
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(
                            DashboardState.upcoming_sessions, session_row
                        )
                    ),
                    class_name="w-full",
                ),
                class_name="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden",
            ),
            class_name="space-y-6",
        ),
        title="Dashboard",
    )