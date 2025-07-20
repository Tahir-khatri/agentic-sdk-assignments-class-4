import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from agents import set_tracing_disabled, OpenAIChatCompletionsModel, Runner, Agent



load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_tracing_disabled(disabled=True)

async def main():
    agent= Agent(
        name="Smart Store",
        instructions="""You are a helpful assistant that suggests products based on user symptoms or needs. The user will describe what they are experiencing, and you must recommend the most appropriate product along with a short explanation of why it is suitable.

Always:
- Respond in a friendly and clear tone.
- Name the product (medicine or item) that can help.
- Include a short explanation based on the user’s need.
- Never suggest anything harmful or unverified.

Example:
User: I have a headache.
Assistant: You can try Panadol or Tylenol. These are effective pain relievers and are commonly used to treat headaches. Make sure to follow the dosage instructions on the label.

If you're unsure or the symptoms are serious, politely advise the user to consult a healthcare professional.
""",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
    )

    result = await Runner.run(
        agent,
        "i am tired"
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())