from src.fixture_loader import load_golden_fixtures
from src.providers.deepseek import DeepSeekProvider


provider = DeepSeekProvider()
deespseek_reply = provider.route_ticket("I cannot log in and the reset email never arrives.")
print(deespseek_reply)