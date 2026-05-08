import reflex as rx
from app.components.layout import app_layout
from app.states.knowledge import KnowledgeState


def knowledge_card(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                item["type"],
                class_name="text-xs font-medium px-2 py-1 rounded-full bg-blue-100 text-blue-700 uppercase tracking-wide",
            ),
            class_name="mb-3",
        ),
        rx.el.h3(
            item["title"], class_name="text-lg font-bold text-gray-900 mb-1"
        ),
        rx.el.p(
            f"{item['author']} • {item['date']}",
            class_name="text-xs text-gray-500 mb-3",
        ),
        rx.el.p(
            item["summary"],
            class_name="text-sm text-gray-700 mb-4 line-clamp-2",
        ),
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    item["tags"].to(list[str]),
                    lambda tag: rx.el.span(
                        tag,
                        class_name="text-xs bg-slate-100 text-slate-600 px-2 py-1 rounded-md mr-2",
                    ),
                )
            ),
            rx.el.div(
                rx.icon("eye", class_name="h-4 w-4 mr-1 text-gray-400"),
                rx.el.span(item["views"], class_name="text-xs text-gray-500"),
                class_name="flex items-center",
            ),
            class_name="flex items-center justify-between mt-auto",
        ),
        class_name="bg-white border border-gray-200 rounded-xl p-5 shadow-sm flex flex-col h-full hover:shadow-md transition-shadow cursor-pointer",
    )


def knowledge_base_page() -> rx.Component:
    return app_layout(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Knowledge Preservation Engine",
                    class_name="text-3xl font-bold text-gray-900 mb-2",
                ),
                rx.el.p(
                    "Semantic search across all session transcripts, insights, and resources.",
                    class_name="text-gray-500",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400",
                ),
                rx.el.input(
                    placeholder="Search transcripts, insights, resources...",
                    on_change=KnowledgeState.set_search_query,
                    class_name="w-full pl-12 pr-4 py-4 rounded-xl border border-gray-300 shadow-sm focus:ring-2 focus:ring-indigo-500 outline-none text-lg",
                    default_value=KnowledgeState.search_query,
                ),
                class_name="relative mb-8",
            ),
            rx.cond(
                KnowledgeState.filtered_items.length() > 0,
                rx.el.div(
                    rx.foreach(KnowledgeState.filtered_items, knowledge_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
                ),
                rx.el.div(
                    rx.icon(
                        "search-x",
                        class_name="h-12 w-12 text-gray-300 mx-auto mb-4",
                    ),
                    rx.el.p(
                        "No results found",
                        class_name="text-gray-500 font-medium",
                    ),
                    class_name="py-20 text-center",
                ),
            ),
        ),
        title="Knowledge Base",
    )