import reflex as rx


class SessionState(rx.State):
    is_session_active: bool = False
    session_timer: int = 0
    current_session: dict[str, str] = {
        "mentor": "Dr. Sarah Chen",
        "student": "Alex Rivera",
        "topic": "AI Fundamentals",
        "start_time": "10:00 AM",
    }
    transcript_entries: list[dict[str, str | int]] = [
        {
            "speaker": "Dr. Sarah Chen",
            "text": "Welcome to our session, Alex!",
            "timestamp": "00:00:10",
            "sentiment": "positive",
            "engagement_score": 90,
        },
        {
            "speaker": "Alex Rivera",
            "text": "Thanks! I'm excited to learn about neural networks.",
            "timestamp": "00:00:25",
            "sentiment": "positive",
            "engagement_score": 85,
        },
    ]
    engagement_level: int = 78
    sentiment_distribution: dict[str, int] = {
        "positive": 45,
        "neutral": 35,
        "negative": 5,
        "curious": 15,
    }
    ai_chat_messages: list[dict[str, str]] = [
        {
            "role": "user",
            "content": "What's a good way to explain backpropagation?",
        },
        {
            "role": "assistant",
            "content": "Think of it as adjusting the knobs on a machine until the output is just right, working backwards from the error.",
        },
    ]
    ai_chat_input: str = ""
    session_artifacts: dict[
        str, str | list[str] | list[dict[str, str | list[str]]]
    ] = {
        "summary": "The session covered the basics of neural networks, focusing on the concepts of forward and backpropagation.",
        "key_topics": ["Neural Networks", "Backpropagation", "Loss Functions"],
        "quiz_questions": [
            {
                "question": "What is backpropagation?",
                "options": [
                    "A network",
                    "An error adjusting algorithm",
                    "A loss function",
                    "None of the above",
                ],
                "correct_answer": "An error adjusting algorithm",
            }
        ],
        "flashcards": [
            {
                "front": "Backpropagation",
                "back": "Algorithm to calculate gradient of the loss function.",
            }
        ],
        "action_items": [
            "Review loss functions",
            "Practice basic neural net implementation",
        ],
    }
    memory_timeline: list[dict[str, str]] = [
        {
            "date": "Oct 15",
            "milestone": "First AI Session",
            "description": "Introduced basic concepts.",
            "type": "session",
            "icon": "video",
        }
    ]
    show_artifacts: bool = False

    @rx.event
    def toggle_session(self):
        self.is_session_active = not self.is_session_active

    @rx.event
    def send_ai_message(self):
        if self.ai_chat_input:
            self.ai_chat_messages.append(
                {"role": "user", "content": self.ai_chat_input}
            )
            self.ai_chat_messages.append(
                {
                    "role": "assistant",
                    "content": f"Simulated response about {self.current_session['topic']}.",
                }
            )
            self.ai_chat_input = ""

    @rx.event
    def set_ai_chat_input(self, value: str):
        self.ai_chat_input = value

    @rx.event
    def toggle_artifacts(self):
        self.show_artifacts = not self.show_artifacts