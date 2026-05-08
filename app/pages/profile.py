import reflex as rx
from app.components.layout import app_layout
from app.states.profile import ProfileState


def profile_setup_page() -> rx.Component:
    return app_layout(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Complete Your Profile",
                    class_name="text-2xl font-bold text-gray-900 mb-2",
                ),
                rx.el.p(
                    "Tell us more about yourself to help us find the perfect match.",
                    class_name="text-gray-500 mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Basic Information",
                            class_name="text-lg font-semibold text-gray-900 mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Bio",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.textarea(
                                    placeholder="Tell us about yourself...",
                                    on_change=ProfileState.set_bio,
                                    class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 h-32 resize-none",
                                ),
                                class_name="col-span-2 mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Institution / Company",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    placeholder="Where do you work/study?",
                                    on_change=ProfileState.set_institution,
                                    class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500",
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Years of Experience",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    type="number",
                                    placeholder="e.g. 5",
                                    on_change=ProfileState.set_years_experience,
                                    class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500",
                                ),
                                class_name="mb-4",
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                        ),
                        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm mb-6",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Skills & Expertise",
                            class_name="text-lg font-semibold text-gray-900 mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Add Skills",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.div(
                                rx.el.input(
                                    on_change=ProfileState.set_current_skill_input,
                                    placeholder="e.g. Python, AI, Leadership...",
                                    class_name="flex-1 px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500",
                                    default_value=ProfileState.current_skill_input,
                                ),
                                rx.el.button(
                                    "Add",
                                    on_click=ProfileState.add_skill,
                                    class_name="bg-indigo-100 text-indigo-700 px-4 py-2 rounded-lg font-medium hover:bg-indigo-200 transition-colors",
                                ),
                                class_name="flex gap-2 mb-4",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    ProfileState.skills,
                                    lambda skill: rx.el.span(
                                        skill,
                                        rx.icon(
                                            "x",
                                            class_name="h-3 w-3 ml-1 cursor-pointer",
                                            on_click=lambda: (
                                                ProfileState.remove_skill(skill)
                                            ),
                                        ),
                                        class_name="inline-flex items-center px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 text-sm font-medium",
                                    ),
                                ),
                                class_name="flex flex-wrap gap-2",
                            ),
                        ),
                        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm mb-8",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Save Profile",
                            on_click=ProfileState.save_profile,
                            class_name="bg-indigo-600 text-white px-8 py-3 rounded-lg font-medium hover:bg-indigo-700 transition-colors",
                        ),
                        class_name="flex justify-end",
                    ),
                ),
                class_name="max-w-3xl mx-auto",
            )
        ),
        title="Profile Setup",
    )