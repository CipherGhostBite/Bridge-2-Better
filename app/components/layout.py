import reflex as rx
from app.states.auth import AuthState
from app.states.navigation import NavigationState


def nav_item(label: str, icon: str, route: str) -> rx.Component:
    is_active = NavigationState.active_page == label
    return rx.el.a(
        rx.icon(
            icon,
            class_name=rx.cond(
                is_active, "text-white h-5 w-5", "text-gray-500 h-5 w-5"
            ),
        ),
        rx.el.span(label, class_name="font-medium"),
        href=route,
        on_click=lambda: NavigationState.set_active_page(label),
        class_name=rx.cond(
            is_active,
            "flex items-center gap-3 px-4 py-2.5 rounded-lg bg-indigo-600 text-white transition-all",
            "flex items-center gap-3 px-4 py-2.5 rounded-lg text-gray-600 hover:bg-slate-100 transition-all",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("brain", class_name="h-8 w-8 text-indigo-600"),
                rx.el.span(
                    "SynapseBridge",
                    class_name="text-xl font-bold text-gray-900",
                ),
                class_name="flex items-center gap-2 px-6 h-16 border-b border-gray-100",
            ),
            rx.el.nav(
                rx.el.div(
                    nav_item("Dashboard", "layout-dashboard", "/dashboard"),
                    nav_item("Matches", "users", "/matches"),
                    nav_item("Sessions", "video", "/sessions"),
                    nav_item("Knowledge Base", "book-open", "/knowledge-base"),
                    nav_item("Schedule", "calendar", "/schedule"),
                    nav_item("Admin", "shield", "/admin"),
                    class_name="flex flex-col gap-1",
                ),
                class_name="flex-1 px-4 py-6 overflow-y-auto",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            AuthState.user_initial,
                            class_name="text-sm font-bold text-indigo-600",
                        ),
                        class_name="w-10 h-10 rounded-full bg-indigo-50 flex items-center justify-center shrink-0",
                    ),
                    rx.el.div(
                        rx.el.p(
                            AuthState.user_name,
                            class_name="text-sm font-semibold text-gray-900 truncate",
                        ),
                        rx.el.p(
                            AuthState.user_role,
                            class_name="text-xs text-gray-500 truncate",
                        ),
                        class_name="flex-1 min-w-0",
                    ),
                    rx.icon(
                        "log-out",
                        class_name="h-5 w-5 text-gray-400 hover:text-red-500 cursor-pointer shrink-0",
                        on_click=AuthState.logout,
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="p-4 border-t border-gray-100",
            ),
            class_name="flex flex-col h-full bg-white border-r border-gray-200 w-64 shrink-0",
        ),
        class_name="hidden md:block h-screen sticky top-0",
    )


def header(title: str) -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.h1(title, class_name="text-xl font-semibold text-gray-800"),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                    ),
                    rx.el.input(
                        placeholder="Search...",
                        class_name="pl-10 pr-4 py-2 w-64 rounded-full border border-gray-200 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all outline-none text-sm",
                    ),
                    class_name="relative hidden sm:block",
                ),
                rx.el.button(
                    rx.icon("bell", class_name="h-5 w-5 text-gray-500"),
                    class_name="p-2 hover:bg-gray-100 rounded-full transition-colors relative",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="flex items-center justify-between h-16 px-8 max-w-7xl mx-auto",
        ),
        class_name="bg-white border-b border-gray-200 sticky top-0 z-10",
    )


def app_layout(content: rx.Component, title: str = "Dashboard") -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(title),
            rx.el.main(
                rx.el.div(content, class_name="max-w-7xl mx-auto"),
                class_name="flex-1 p-8 overflow-y-auto",
            ),
            class_name="flex flex-col flex-1 min-w-0",
        ),
        class_name="flex min-h-screen bg-slate-50 font-['Inter']",
    )


def public_layout(content: rx.Component) -> rx.Component:
    return rx.el.div(content, class_name="min-h-screen font-['Inter']")