from agents import Agent
# from agents.tools import Tool
from tools import roll_dice, generate_event

# Tools
# dice_tool = Tool.from_function(roll_dice)
# event_tool = Tool.from_function(generate_event)

# Agents
narrator_agent = Agent(
    name="NarratorAgent",
    instructions="You guide the player through the story and offer choices.",
    tools=[generate_event]
)

monster_agent = Agent(
    name="MonsterAgent",
    instructions="You simulate combat with monsters using rool dice tools and generate events.",
    tools=[roll_dice]
)

item_agent = Agent(
    name="ItemAgent",
    instructions="You handle inventory and give rewards after events.",
)

main_agent = Agent(
    name="GameMasterAgent",
    instructions="You are the main game master. Coordinate game flow using other agents.",
    handoffs=[narrator_agent, monster_agent, item_agent]
)
