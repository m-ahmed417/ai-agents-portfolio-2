from src.prompt_loader import load_prompt

prompt = load_prompt("prompts/route_ticket_system.md")

def test_load_route_ticket_system_prompt():
    assert isinstance(prompt, str)
    assert "FlowPilot" in prompt
    assert "Return only valid JSON" in prompt
    assert "account_access" in prompt
    

