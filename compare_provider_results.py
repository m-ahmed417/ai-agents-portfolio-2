from src.providers.deepseek import DeepSeekProvider
from src.providers.openai_provider import OpenAIProvider
from src.fixture_loader import load_golden_fixtures
from src.evaluator import evaluate_single_fixture


fixtures = load_golden_fixtures("fixtures/golden_v1.json")

deepseek_provider = DeepSeekProvider()
openai_provider = OpenAIProvider()

deepseek_results = []
openai_results = []
deepseek_category_match_count = 0
openai_category_match_count = 0
openai_urgency_match_count = 0
deepseek_urgency_match_count = 0
failed_deepseek_results = []
failed_openai_results = []


for fixture in fixtures:
    deepseek_evaluation = evaluate_single_fixture(fixture=fixture, provider=deepseek_provider)
    deepseek_results.append(deepseek_evaluation)
    
    openai_evaluation = evaluate_single_fixture(fixture=fixture, provider=openai_provider)
    openai_results.append(openai_evaluation)
    
    if deepseek_evaluation["category_match"]:
        deepseek_category_match_count += 1
    
    if deepseek_evaluation["urgency_match"]:
        deepseek_urgency_match_count += 1
        
    if openai_evaluation["category_match"]:
        openai_category_match_count += 1
    
    if openai_evaluation["urgency_match"]:
        openai_urgency_match_count += 1
        
    if not deepseek_evaluation["category_match"] or not deepseek_evaluation["urgency_match"]:
        failed_deepseek_results.append(deepseek_evaluation)

    if not openai_evaluation["category_match"] or not openai_evaluation["urgency_match"]:
        failed_openai_results.append(openai_evaluation)
        
    
    
    
total_fixtures = len(fixtures)

deepseek_category_accuracy = deepseek_category_match_count / total_fixtures * 100
deepseek_urgency_accuracy = deepseek_urgency_match_count / total_fixtures * 100

openai_category_accuracy = openai_category_match_count / total_fixtures * 100
openai_urgency_accuracy = openai_urgency_match_count / total_fixtures * 100

print("Provider comparison summary")
print(f"Total fixtures: {total_fixtures}")

print()
print("DeepSeek")
print(
    f"Category accuracy: {deepseek_category_match_count}/{total_fixtures} "
    f"({deepseek_category_accuracy:.1f}%)"
)
print(
    f"Urgency accuracy: {deepseek_urgency_match_count}/{total_fixtures} "
    f"({deepseek_urgency_accuracy:.1f}%)"
)

print()
print("OpenAI")
print(
    f"Category accuracy: {openai_category_match_count}/{total_fixtures} "
    f"({openai_category_accuracy:.1f}%)"
)
print(
    f"Urgency accuracy: {openai_urgency_match_count}/{total_fixtures} "
    f"({openai_urgency_accuracy:.1f}%)"
)

deepseek_failed_ids = set()

for failed_result in failed_deepseek_results:
    deepseek_failed_ids.add(failed_result["fixture_id"])
    
openai_failed_ids = set()

for failed_result in failed_openai_results:
    openai_failed_ids.add(failed_result["fixture_id"])
    

both_failed_ids = deepseek_failed_ids & openai_failed_ids
only_deepseek_failed_ids = deepseek_failed_ids - openai_failed_ids
only_openai_failed_ids = openai_failed_ids - deepseek_failed_ids

print()
print("Failure overlap")
print(f"Both providers failed: {sorted(both_failed_ids)}")
print(f"Only DeepSeek failed: {sorted(only_deepseek_failed_ids)}")
print(f"Only OpenAI failed: {sorted(only_openai_failed_ids)}")