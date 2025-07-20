import os
from dotenv import load_dotenv
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    mood_agent = Agent(
        name= "Mood Analyzer",
        instructions= """
You are a mood detection assistant. Given a user’s message, identify their mood in one word (e.g., happy, sad, stressed, excited).
Only reply with the mood — no explanation.""",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )


    activity_agent = Agent(
        name= "Activity Suggester",
        instructions= """
You are a helpful assistant that suggests uplifting activities for someone who is sad or stressed.
Be gentle, encouraging, and specific. Suggest only 1 activity with a short explanation.""",
        model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )

    user_input = "today i won the match"

    mood_result = await Runner.run(mood_agent, user_input)
    mood = mood_result.final_output.strip().lower()

    print(f"Detected Mood: {mood}")

    if mood in ["sad", "stressed"]:
        activity_result = await Runner.run(activity_agent, mood)
        print(f"Suggested Activity: {activity_result.final_output}")

    else:
        print("you are doing great! Keep it up. 😊")

if __name__ == "__main__":
    asyncio.run(main())