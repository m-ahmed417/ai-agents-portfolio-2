from src.providers.openai_provider import OpenAIProvider

provider = OpenAIProvider()
openai_reply = provider.route_ticket("I cannot log in and the reset email never arrives.")
print(openai_reply)
