from agents import Agent

from tools import get_study_tips



math_agent = Agent(
    name="MathAgent",
    instructions="You are a math assistant. Answer math-related queries.",
    # tools=[get_study_tips]  with free gemini API, tools are not supported
)


science_agent = Agent(
    name="ScienceAgent",
    instructions="You are a science assistant. Help students understand scientific topics.",
    # tools=[get_study_tips] with free gemini API, tools are not supported
)

general_agent = Agent(
    name="GeneralAgent",
    instructions="You give general study advice.",
    tools=[get_study_tips] # with free gemini API, tools are not supported
)

main_agent = Agent(
    name="MainAgent",
    instructions="You are a smart student assistant. Based on the subject, hand off to relevant agent.",
    handoffs=[math_agent, science_agent, general_agent] # with free gemini API, handoffs are not supported
)
