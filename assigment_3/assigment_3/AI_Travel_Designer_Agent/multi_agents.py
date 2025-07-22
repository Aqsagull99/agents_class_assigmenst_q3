from agents import Agent
# from agents.tools import Tool # with gemini api not supported 
from tools import get_flights, suggest_hotels, recommend_exploration

#not supported with gemini api
# Convert to tool objects 
# flights_tool = Tool.from_function(get_flights)
# hotels_tool = Tool.from_function(suggest_hotels)
# explore_tool = Tool.from_function(recommend_exploration)

# Destination Agent
destination_agent = Agent(
    name="DestinationAgent",
    instructions="Suggest destinations based on user's mood or interests.",
)

# Booking Agent
booking_agent = Agent(
    name="BookingAgent",
    instructions="Use tools to simulate booking flights and suggesting hotels.",
    # tools=[flights_tool, hotels_tool]  #not supported with gemini api
)

# Explore Agent
explore_agent = Agent(
    name="ExploreAgent",
    instructions="Give travel tips, attractions, and food ideas.",
    # tools=[explore_tool] #not supported with gemini api
)

# Main Controller Agent
main_agent = Agent(
    name="TravelMainAgent",
    instructions="Coordinate travel planning using other agents.",
    handoffs=[destination_agent, booking_agent, explore_agent] #not supported with gemini api
)
