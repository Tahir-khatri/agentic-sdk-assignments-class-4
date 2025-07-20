from agents import Agent, set_tracing_disabled, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

# Tools
async def get_capital(country: str) -> str:
    capitals = {
        "pakistan": "Islamabad",
        "india": "New Delhi",
        "france": "Paris",
        "japan": "Tokyo",
        "usa": "Washington, D.C."
    }
    return capitals.get(country.lower(), "Capital not found")

async def get_language(country: str) -> str:
    languages = {
        "pakistan": "Urdu",
        "india": "Hindi, English",
        "france": "French",
        "japan": "Japanese",
        "usa": "English"
    }
    return languages.get(country.lower(), "Language not found")

async def get_population(country: str) -> str:
    populations = {
        "pakistan": "240 million",
        "india": "1.4 billion",
        "france": "67 million",
        "japan": "125 million",
        "usa": "331 million",
    }
    return populations.get(country.lower(), "Population not found")

# Main Agent Logic
class CountryInfoAgent(Agent):
    async def ahandle(self, input: str) -> str:
        country = input.strip()
        capital = await get_capital(country)
        language = await get_language(country)
        population = await get_population(country)

        return f"{country.title()}: Capital is {capital}, Language is {language}, Population is {population}."

orchestrator = CountryInfoAgent(
    name="Country Info Orchestrator",
    instructions="Return capital, language, and population of a country.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)

async def main():
    country = input("Enter country name: ")
    result = await Runner.run(orchestrator, country)
    print(result.final_output)

asyncio.run(main())
