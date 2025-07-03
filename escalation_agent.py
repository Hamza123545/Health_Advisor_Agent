from agents import Agent

def create_escalation_agent():
    return Agent(
        name="EscalationAgent",
        instructions="You are an escalation agent. When a user requests to speak to a human coach, take over and provide guidance or escalate as needed.",
        tools=[],
    ) 