from agents import Agent

def create_nutrition_expert_agent():
    return Agent(
        name="NutritionExpertAgent",
        instructions="You are a nutrition expert. Help users with complex dietary needs such as diabetes or allergies, and provide specialized meal plans and advice.",
        tools=[],
    ) 