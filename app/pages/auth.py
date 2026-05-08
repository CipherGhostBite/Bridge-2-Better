import reflex as rx
from app.components.layout import public_layout
from app.states.auth import AuthState


def login_page() -> rx.Component:
    return public_layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "brain",
                        class_name="h-10 w-10 text-indigo-600 mx-auto mb-4",
                    ),
                    rx.el.h2(
                        "Welcome back",
                        class_name="text-2xl font-bold text-gray-900 text-center mb-2",
                    ),
                    rx.el.p(
                        "Sign in to your account",
                        class_name="text-gray-500 text-center mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Email address",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.input(
                                type="email",
                                on_change=AuthState.set_email,
                                class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Password",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.input(
                                type="password",
                                on_change=AuthState.set_password,
                                class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.button(
                            "Sign In",
                            on_click=AuthState.login,
                            class_name="w-full bg-indigo-600 text-white py-2.5 rounded-lg font-medium hover:bg-indigo-700 transition-colors",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.p(
                        "Don't have an account? ",
                        rx.el.a(
                            "Sign up",
                            href="/register",
                            class_name="text-indigo-600 font-medium hover:underline",
                        ),
                        class_name="text-center text-sm text-gray-600",
                    ),
                ),
                class_name="bg-white p-10 rounded-2xl shadow-xl w-full max-w-md border border-gray-100",
            ),
            class_name="min-h-screen bg-gradient-to-br from-indigo-900 via-indigo-800 to-violet-900 flex items-center justify-center p-4",
        )
    )


def register_page() -> rx.Component:
    return public_layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "brain",
                        class_name="h-10 w-10 text-indigo-600 mx-auto mb-4",
                    ),
                    rx.el.h2(
                        "Create an account",
                        class_name="text-2xl font-bold text-gray-900 text-center mb-2",
                    ),
                    rx.el.p(
                        "Join SynapseBridge today",
                        class_name="text-gray-500 text-center mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Full Name",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.input(
                                on_change=AuthState.set_name,
                                class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Email address",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.input(
                                type="email",
                                on_change=AuthState.set_email,
                                class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Role",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.div(
                                rx.el.select(
                                    rx.el.option(
                                        "Student (Digital Native)",
                                        value="Student",
                                    ),
                                    rx.el.option(
                                        "Mentor (Industry Expert)",
                                        value="Mentor",
                                    ),
                                    rx.el.option("Admin", value="Admin"),
                                    on_change=AuthState.set_role,
                                    class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none appearance-none bg-white",
                                ),
                                rx.icon(
                                    "chevron-down",
                                    class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-500 pointer-events-none",
                                ),
                                class_name="relative",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Password",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.input(
                                type="password",
                                on_change=AuthState.set_password,
                                class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Confirm Password",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.input(
                                type="password",
                                on_change=AuthState.set_confirm_password,
                                class_name="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none",
                            ),
                            class_name="mb-8",
                        ),
                        rx.el.button(
                            "Create Account",
                            on_click=AuthState.register,
                            class_name="w-full bg-indigo-600 text-white py-2.5 rounded-lg font-medium hover:bg-indigo-700 transition-colors",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.p(
                        "Already have an account? ",
                        rx.el.a(
                            "Sign in",
                            href="/login",
                            class_name="text-indigo-600 font-medium hover:underline",
                        ),
                        class_name="text-center text-sm text-gray-600",
                    ),
                ),
                class_name="bg-white p-10 rounded-2xl shadow-xl w-full max-w-md border border-gray-100",
            ),
            class_name="min-h-screen bg-gradient-to-br from-indigo-900 via-indigo-800 to-violet-900 flex items-center justify-center p-4 py-12",
        )
    )