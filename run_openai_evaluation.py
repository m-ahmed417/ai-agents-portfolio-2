from src.fixture_loader import load_golden_fixtures
from src.providers.openai_provider import OpenAIProvider
from src.evaluator import evaluate_single_fixture

fixtures = load_golden_fixtures("fixtures/golden_v1.json")
sample_fixtures = fixtures
provider = OpenAIProvider()

category_match_count = 0
urgency_match_count = 0
failed_results = []

for fixture in sample_fixtures:
    single_evaluation = evaluate_single_fixture(fixture=fixture, provider=provider)

    if single_evaluation["category_match"]:
        category_match_count += 1

    if single_evaluation["urgency_match"]:
        urgency_match_count += 1
    
    if not single_evaluation["category_match"] or not single_evaluation["urgency_match"]:
        failed_results.append(single_evaluation)

total_fixtures = len(sample_fixtures)
category_accuracy = category_match_count / total_fixtures * 100
urgency_accuracy = urgency_match_count / total_fixtures * 100

print("OpenAI evaluation summary")
print(f"Total fixtures: {total_fixtures}")
print(f"Category accuracy: {category_match_count}/{total_fixtures} ({category_accuracy:.1f}%)")
print(f"Urgency accuracy: {urgency_match_count}/{total_fixtures} ({urgency_accuracy:.1f}%)")

if failed_results:
    print()
    print("Failed fixtures:")
    for result in failed_results:
        failures = []

        if not result["category_match"]:
            failures.append(
                f"category expected {result['expected_category']}, got {result['actual_category']}"
            )

        if not result["urgency_match"]:
            failures.append(
                f"urgency expected {result['expected_urgency']}, got {result['actual_urgency']}"
            )

        print(f"- {result['fixture_id']}: {'; '.join(failures)}")
else:
    print()
    print("No failed fixtures.")
