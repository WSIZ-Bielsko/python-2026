from pathlib import Path

from pydantic import BaseModel
from datetime import date, time


class Message(BaseModel):
    date: date
    time: time
    nickname: str
    message: str


def save_messages_to_jsonl(messages: list[Message], filepath: str | Path) -> None:
    """Saves a list of Message models to a .jsonl file."""
    with open(filepath, "w", encoding="utf-8") as f:
        for msg in messages:
            # .model_dump_json() returns a string for Pydantic models
            f.write(msg.model_dump_json() + "\n")


def load_messages_from_jsonl(filepath: str | Path) -> list[Message]:
    """Loads a list of Message models from a .jsonl file."""
    messages = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            # Skip empty lines to prevent errors
            if line.strip():
                # model_validate_json is the standard Pydantic 2 way to load JSON strings
                messages.append(Message.model_validate_json(line))
    return messages


if __name__ == '__main__':
    messages: list[Message] = [
        Message(
            date=date(2026, 1, 24),
            time=time(9, 15),
            nickname="alice",
            message="Morning standup done, notes are in the doc."
        ),
        Message(
            date=date(2026, 1, 24),
            time=time(12, 30),
            nickname="bob",
            message="Lunch break, will be back in 30 minutes."
        ),
        Message(
            date=date(2026, 1, 24),
            time=time(18, 5),
            nickname="charlie",
            message="Pushed the latest changes to the main branch."
        ),
    ]

    save_messages_to_jsonl(messages, "messages.jsonl")

    gg = load_messages_from_jsonl("messages.jsonl")
    for g in gg:
        print(g)

    # write converter

    # repo to sqlite3
