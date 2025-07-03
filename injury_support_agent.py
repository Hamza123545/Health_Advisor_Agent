from agents import Agent

def create_injury_support_agent():
    return Agent(
        name="InjurySupportAgent",
        instructions="You are an injury support agent. Assist users with physical limitations or injury-specific workout plans and advice.",
        tools=[],
    ) 