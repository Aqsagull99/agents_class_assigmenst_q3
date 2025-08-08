import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from multi_agents import career_agent, job_agent, skills_agent, main_agent

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMIMI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
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

# result = Runner.run_sync(main_agent, input="Get career roadmap for Web Developer?"  , run_config=config)
#result = Runner.run_sync(main_agent, input="I’m looking for an internship. What should I do?"  , run_config=config)
result = Runner.run_sync(main_agent, input="I want to become a UI/UX designer, what skills should I learn?"  , run_config=config)

print(result.final_output)
print(result._last_agent.name)





