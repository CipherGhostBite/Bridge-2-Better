import reflex as rx
from app.components.layout import public_layout


def feature_card(title: str, desc: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-indigo-600"),
            class_name="w-12 h-12 rounded-xl bg-indigo-50 flex items-center justify-center mb-6",
        ),
        rx.el.h3(title, class_name="text-xl font-semibold text-gray-900 mb-3"),
        rx.el.p(desc, class_name="text-gray-600 leading-relaxed"),
        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-all",
    )


def stat_card(value: str, label: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(value, class_name="text-4xl font-bold text-white mb-2"),
        rx.el.div(label, class_name="text-indigo-100 font-medium"),
        class_name="text-center",
    )


def landing_page() -> rx.Component:
    return public_layout(
        rx.el.div(
            rx.el.header(
                rx.el.div(
                    rx.el.div(
                        rx.icon("brain", class_name="h-8 w-8 text-indigo-600"),
                        rx.el.span(
                            "SynapseBridge",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Login",
                            href="/login",
                            class_name="text-gray-600 font-medium hover:text-gray-900",
                        ),
                        rx.el.a(
                            "Get Started",
                            href="/register",
                            class_name="bg-indigo-600 text-white px-5 py-2 rounded-full font-medium hover:bg-indigo-700 transition-colors",
                        ),
                        class_name="flex items-center gap-6",
                    ),
                    class_name="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between",
                ),
                class_name="bg-white border-b border-gray-100 sticky top-0 z-50",
            ),
            rx.el.section(
                rx.el.div(
                    rx.el.h1(
                        "Bridge Generations. Share Knowledge. Transform Lives.",
                        class_name="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight",
                    ),
                    rx.el.p(
                        "A revolutionary reverse mentorship platform connecting seasoned professionals with digital natives for bidirectional learning.",
                        class_name="text-xl text-indigo-100 mb-10 max-w-2xl mx-auto leading-relaxed",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Join as Mentor",
                            href="/register",
                            class_name="bg-white text-indigo-600 px-8 py-4 rounded-full font-bold text-lg hover:bg-gray-50 transition-colors shadow-lg",
                        ),
                        rx.el.a(
                            "Join as Student",
                            href="/register",
                            class_name="bg-indigo-500 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-indigo-400 transition-colors border border-indigo-400 shadow-lg",
                        ),
                        class_name="flex flex-col sm:flex-row items-center justify-center gap-4",
                    ),
                    class_name="max-w-4xl mx-auto text-center",
                ),
                class_name="bg-gradient-to-br from-indigo-900 via-indigo-800 to-violet-900 py-32 px-6",
            ),
            rx.el.section(
                rx.el.div(
                    stat_card("500+", "Active Mentors"),
                    stat_card("1,200+", "Eager Students"),
                    stat_card("10,000+", "Sessions Completed"),
                    class_name="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8",
                ),
                class_name="bg-indigo-950 py-16 px-6",
            ),
            rx.el.section(
                rx.el.div(
                    rx.el.h2(
                        "Why SynapseBridge?",
                        class_name="text-3xl font-bold text-center text-gray-900 mb-16",
                    ),
                    rx.el.div(
                        feature_card(
                            "AI-Powered Matching",
                            "Our intelligent engine pairs mentors and students based on complementary skills, goals, and working styles.",
                            "sparkles",
                        ),
                        feature_card(
                            "Bidirectional Learning",
                            "Everyone teaches, everyone learns. Share industry experience while mastering new digital tools.",
                            "refresh-cw",
                        ),
                        feature_card(
                            "Knowledge Preservation",
                            "Automatically capture, transcribe, and summarize sessions to build an enduring library of insights.",
                            "database",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
                    ),
                    class_name="max-w-7xl mx-auto",
                ),
                class_name="py-24 px-6 bg-slate-50",
            ),
        )
    )