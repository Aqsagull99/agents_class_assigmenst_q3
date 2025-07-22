import os
from dotenv import load_dotenv
from agents import  AsyncOpenAI, OpenAIChatCompletionsModel,Runner
from agents.run import RunConfig
from multi_agents import main_agent, booking_agent, destination_agent, explore_agent

load_dotenv()

gemini_api_key = os.getenv("GEMIMI_API_KEY")

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
        tracing_disabled=True
    )

result = Runner.run_sync(
    booking_agent,
    input="I want a relaxing trip suggestion with hotels and things to do.",
    run_config=config
)

print(result.final_output)
