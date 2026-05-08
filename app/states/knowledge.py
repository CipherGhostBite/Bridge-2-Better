import reflex as rx


class KnowledgeState(rx.State):
    search_query: str = ""
    selected_filter: str = "all"
    selected_topic_filter: str = "all"
    knowledge_items: list[dict[str, str | int | bool | list[str]]] = [
        {
            "id": "1",
            "title": "Advanced Prompt Engineering",
            "type": "article",
            "topic": "AI",
            "author": "Dr. Sarah Chen",
            "date": "Oct 10, 2024",
            "summary": "Techniques to optimize your prompts for better LLM outputs.",
            "tags": ["AI", "Prompting"],
            "views": 120,
            "bookmarked": False,
        },
        {
            "id": "2",
            "title": "Session: Cloud Architecture",
            "type": "session_transcript",
            "topic": "STEM",
            "author": "James Wilson",
            "date": "Oct 12, 2024",
            "summary": "A review of modern cloud architecture patterns.",
            "tags": ["Cloud", "AWS"],
            "views": 45,
            "bookmarked": True,
        },
    ]

    @rx.var
    def filtered_items(self) -> list[dict[str, str | int | bool | list[str]]]:
        result = self.knowledge_items
        if self.search_query:
            result = [
                i
                for i in result
                if self.search_query.lower() in str(i["title"]).lower()
            ]
        if self.selected_filter != "all":
            result = [i for i in result if i["type"] == self.selected_filter]
        if self.selected_topic_filter != "all":
            result = [
                i for i in result if i["topic"] == self.selected_topic_filter
            ]
        return result

    @rx.event
    def set_search_query(self, value: str):
        self.search_query = value

    @rx.event
    def toggle_bookmark(self, id: str):
        for item in self.knowledge_items:
            if item["id"] == id:
                item["bookmarked"] = not item["bookmarked"]
                break

    @rx.event
    def set_filter(self, filter_type: str):
        self.selected_filter = filter_type

    @rx.event
    def set_topic_filter(self, topic: str):
        self.selected_topic_filter = topic