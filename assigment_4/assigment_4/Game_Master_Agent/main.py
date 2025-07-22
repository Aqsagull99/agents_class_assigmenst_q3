
import os
from dotenv import load_dotenv
from agents import  AsyncOpenAI, OpenAIChatCompletionsModel,Runner
from agents.run import RunConfig
from multi_agents import main_agent ,monster_agent, item_agent, narrator_agent

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMIMI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")



external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True)


result = Runner.run_sync(
    main_agent,
    input="I challenge the monster! Roll a 6-sided dice to attack. Narrate the battle and give me a reward if I win.",
    run_config=config
)

print(result.final_output)