import reflex as rx
from app.components.layout import app_layout
from app.states.matching import MatchingState


def match_card(match: dict, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(match["mentor_name"], class_name="font-semibold"),
            rx.icon("arrow-left-right", class_name="h-4 w-4"),
            rx.el.div(match["student_name"], class_name="font-semibold"),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            f"Score: {match['compatibility_score']}%",
            class_name="mt-2 text-sm text-indigo-600",
        ),
        on_click=lambda: MatchingState.select_match(index),
        class_name=rx.cond(
            MatchingState.selected_match_index == index,
            "p-4 bg-indigo-50 border-l-4 border-indigo-600 cursor-pointer shadow-sm",
            "p-4 bg-white border border-gray-100 cursor-pointer hover:bg-slate-50",
        ),
    )


def matches_page() -> rx.Component:
    return app_layout(
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    MatchingState.filtered_matches,
                    lambda m, i: match_card(m, i),
                ),
                class_name="w-1/3 border-r border-gray-200 bg-white min-h-[600px]",
            ),
            rx.el.div(
                rx.cond(
                    MatchingState.selected_match_index >= 0,
                    rx.el.div(
                        rx.el.h2(
                            "Match Details",
                            class_name="text-2xl font-bold mb-4",
                        ),
                        rx.el.p(
                            f"Mentor: {MatchingState.selected_match_mentor_name}"
                        ),
                        rx.el.p(
                            f"Student: {MatchingState.selected_match_student_name}"
                        ),
                        rx.el.button(
                            "Accept Match",
                            on_click=lambda: MatchingState.accept_match(
                                MatchingState.selected_match_index
                            ),
                            class_name="mt-4 bg-indigo-600 text-white px-4 py-2 rounded-lg",
                        ),
                        class_name="p-8",
                    ),
                    rx.el.div(
                        "Select a match to view details",
                        class_name="p-8 text-gray-500",
                    ),
                ),
                class_name="w-2/3 bg-slate-50",
            ),
            class_name="flex rounded-2xl border border-gray-200 overflow-hidden shadow-sm",
        ),
        title="AI Matching Engine",
    )