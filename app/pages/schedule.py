import reflex as rx
from app.components.layout import app_layout
from app.states.schedule import ScheduleState


def schedule_page() -> rx.Component:
    return app_layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        f"Schedule - {ScheduleState.current_month}",
                        class_name="text-2xl font-bold mb-6",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Calendar View Simulated: Select Oct 15 to see sessions.",
                            class_name="text-gray-500 p-8 border-2 border-dashed border-gray-200 rounded-xl text-center",
                        )
                    ),
                    class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200 h-full",
                ),
                class_name="w-full md:w-3/5",
            ),
            rx.el.div(
                rx.el.h3(
                    f"Sessions on {ScheduleState.selected_date}",
                    class_name="text-xl font-bold mb-4",
                ),
                rx.cond(
                    ScheduleState.sessions_for_selected_date.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            ScheduleState.sessions_for_selected_date,
                            lambda s: rx.el.div(
                                rx.el.div(
                                    rx.el.h4(
                                        s["title"],
                                        class_name="font-bold text-gray-900",
                                    ),
                                    rx.el.span(
                                        s["time"],
                                        class_name="text-indigo-600 font-semibold text-sm",
                                    ),
                                    class_name="flex justify-between items-center mb-2",
                                ),
                                rx.el.p(
                                    f"{s['mentor']} & {s['student']}",
                                    class_name="text-sm text-gray-600 mb-2",
                                ),
                                rx.el.div(
                                    rx.el.span(
                                        s["topic"],
                                        class_name="text-xs bg-indigo-50 text-indigo-700 px-2 py-1 rounded-md",
                                    ),
                                    rx.el.span(
                                        s["status"],
                                        class_name="text-xs uppercase font-medium text-emerald-600",
                                    ),
                                    class_name="flex justify-between items-center",
                                ),
                                class_name="bg-white border border-gray-200 rounded-xl p-4 mb-4 shadow-sm",
                            ),
                        )
                    ),
                    rx.el.p(
                        "No sessions scheduled.",
                        class_name="text-gray-500 italic",
                    ),
                ),
                class_name="w-full md:w-2/5",
            ),
            class_name="flex flex-col md:flex-row gap-8",
        ),
        title="Schedule",
    )