import reflex as rx
from typing import Any


class DashboardState(rx.State):
    stats: list[dict[str, str]] = [
        {
            "label": "Sessions Completed",
            "value": "47",
            "change": "+12%",
            "icon": "video",
            "color": "indigo",
        },
        {
            "label": "Skills Learned",
            "value": "23",
            "change": "+5",
            "icon": "lightbulb",
            "color": "emerald",
        },
        {
            "label": "Match Score",
            "value": "94%",
            "change": "+3%",
            "icon": "target",
            "color": "violet",
        },
        {
            "label": "Upcoming Sessions",
            "value": "5",
            "change": "This week",
            "icon": "calendar",
            "color": "amber",
        },
    ]
    recent_activity: list[dict[str, str]] = [
        {
            "user": "Dr. Sarah Chen",
            "action": "completed a session on Quantum Computing",
            "time": "2h ago",
            "avatar_initial": "S",
            "color": "indigo",
        },
        {
            "user": "Alex Rivera",
            "action": "shared Digital Marketing resources",
            "time": "4h ago",
            "avatar_initial": "A",
            "color": "emerald",
        },
        {
            "user": "James Wilson",
            "action": "scheduled a new session",
            "time": "1d ago",
            "avatar_initial": "J",
            "color": "amber",
        },
        {
            "user": "Jordan Lee",
            "action": "earned 'Fast Learner' badge",
            "time": "2d ago",
            "avatar_initial": "J",
            "color": "violet",
        },
    ]
    upcoming_sessions: list[dict[str, str]] = [
        {
            "mentor": "Dr. Sarah Chen",
            "student": "Alex Rivera",
            "topic": "AI Fundamentals",
            "date": "Oct 15",
            "time": "10:00 AM",
            "status": "Confirmed",
        },
        {
            "mentor": "James Wilson",
            "student": "Casey Smith",
            "topic": "Career Guidance",
            "date": "Oct 16",
            "time": "2:00 PM",
            "status": "Pending",
        },
    ]
    learning_progress: list[dict[str, str | int]] = [
        {
            "track": "Expert Track",
            "progress": 45,
            "modules_completed": 3,
            "total_modules": 7,
        },
        {
            "track": "Student Track",
            "progress": 80,
            "modules_completed": 8,
            "total_modules": 10,
        },
    ]