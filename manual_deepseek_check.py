from src.providers.deepseek import DeepSeekProvider

provider = DeepSeekProvider()
deepseek_reply = provider.route_ticket("I cannot log in and the reset email never arrives.")
print(deepseek_reply)


