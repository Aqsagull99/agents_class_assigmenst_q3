import random
from agents import function_tool

@function_tool
def roll_dice() -> str:
    return f"You rolled a {random.randint(1, 6)}!"

@function_tool
def generate_event(choice: str) -> str:
    events = {
        "forest": "You encounter a wild beast!",
        "cave": "You find a treasure chest!",
        "village": "You meet a mysterious old man.",
    }
    return events.get(choice.lower(), "Nothing happens...")
