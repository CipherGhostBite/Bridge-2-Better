import reflex as rx


class NavigationState(rx.State):
    active_page: str = "Dashboard"

    @rx.event
    def set_active_page(self, page: str):
        self.active_page = page