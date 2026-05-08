import reflex as rx
from app.components.layout import app_layout
from app.states.session import SessionState


def ai_chat_message(msg: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            msg["content"],
            class_name=rx.cond(
                msg["role"] == "user",
                "bg-indigo-600 text-white p-3 rounded-2xl rounded-tr-sm ml-auto max-w-[85%] text-sm",
                "bg-gray-100 text-gray-800 p-3 rounded-2xl rounded-tl-sm mr-auto max-w-[85%] text-sm",
            ),
        ),
        class_name="flex w-full mb-4",
    )


def live_session_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                f"Session: {SessionState.current_session['topic']}",
                class_name="text-xl font-bold",
            ),
            rx.el.div(
                rx.el.button(
                    rx.cond(
                        SessionState.is_session_active,
                        "End Session",
                        "Start Session",
                    ),
                    on_click=SessionState.toggle_session,
                    class_name="bg-indigo-600 text-white px-4 py-2 rounded-full font-medium hover:bg-indigo-700",
                )
            ),
            class_name="flex justify-between items-center bg-white p-4 rounded-xl border border-gray-200 mb-6 shadow-sm",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3("Live Transcript", class_name="font-semibold mb-4"),
                rx.el.div(
                    rx.foreach(
                        SessionState.transcript_entries,
                        lambda entry: rx.el.div(
                            rx.el.span(
                                entry["timestamp"],
                                class_name="text-xs text-gray-400 mr-2",
                            ),
                            rx.el.span(
                                entry["speaker"],
                                class_name="font-bold mr-2 text-indigo-700",
                            ),
                            rx.el.span(
                                entry["text"], class_name="text-gray-700"
                            ),
                            class_name="mb-3",
                        ),
                    ),
                    class_name="overflow-y-auto h-96 pr-2",
                ),
                class_name="w-full md:w-2/5 bg-white p-4 rounded-xl border border-gray-200 shadow-sm",
            ),
            rx.el.div(
                rx.el.h3(
                    "Engagement Analytics", class_name="font-semibold mb-4"
                ),
                rx.el.div(
                    rx.el.span(
                        f"{SessionState.engagement_level}%",
                        class_name="text-4xl font-bold text-indigo-600",
                    ),
                    class_name="w-32 h-32 rounded-full border-4 border-indigo-200 flex items-center justify-center mx-auto mb-6",
                ),
                class_name="w-full md:w-1/5 bg-white p-4 rounded-xl border border-gray-200 shadow-sm",
            ),
            rx.el.div(
                rx.el.h3("AI Assistant", class_name="font-semibold mb-4"),
                rx.el.div(
                    rx.foreach(SessionState.ai_chat_messages, ai_chat_message),
                    class_name="overflow-y-auto h-80 mb-4 pr-2",
                ),
                rx.el.div(
                    rx.el.input(
                        placeholder="Ask the AI assistant...",
                        on_change=SessionState.set_ai_chat_input,
                        class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none text-sm",
                        default_value=SessionState.ai_chat_input,
                    ),
                    rx.el.button(
                        "Send",
                        on_click=SessionState.send_ai_message,
                        class_name="mt-2 w-full bg-slate-800 text-white py-2 rounded-lg text-sm font-medium",
                    ),
                ),
                class_name="w-full md:w-2/5 bg-white p-4 rounded-xl border border-gray-200 shadow-sm flex flex-col",
            ),
            class_name="flex flex-col md:flex-row gap-6 mb-6",
        ),
        rx.el.button(
            "View Session Artifacts →",
            on_click=SessionState.toggle_artifacts,
            class_name="w-full py-3 bg-white border border-gray-200 rounded-xl font-medium text-indigo-600 hover:bg-slate-50",
        ),
    )


def artifacts_view() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            "← Back to Session",
            on_click=SessionState.toggle_artifacts,
            class_name="mb-6 text-gray-600 font-medium hover:text-gray-900",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Session Summary", class_name="text-xl font-bold mb-4"
                ),
                rx.el.p(
                    SessionState.session_artifacts["summary"].to(str),
                    class_name="text-gray-700 leading-relaxed mb-4",
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm col-span-2",
            ),
            rx.el.div(
                rx.el.h3(
                    "Knowledge Check", class_name="text-lg font-bold mb-4"
                ),
                rx.foreach(
                    SessionState.session_artifacts["quiz_questions"].to(
                        list[dict[str, str | list[str]]]
                    ),
                    lambda q: rx.el.div(
                        rx.el.p(
                            q["question"].to(str), class_name="font-medium mb-2"
                        )
                    ),
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm",
            ),
            rx.el.div(
                rx.el.h3("Action Items", class_name="text-lg font-bold mb-4"),
                rx.foreach(
                    SessionState.session_artifacts["action_items"].to(
                        list[str]
                    ),
                    lambda item: rx.el.div(
                        rx.el.span(item),
                        class_name="flex items-center gap-2 mb-2",
                    ),
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
        ),
    )


def sessions_page() -> rx.Component:
    return app_layout(
        rx.cond(
            SessionState.show_artifacts, artifacts_view(), live_session_view()
        ),
        title="Sessions",
    )