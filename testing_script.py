from collections import Counter
from src.fixture_loader import load_golden_fixtures


fixtures = load_golden_fixtures("fixtures/golden_v1.json")
print(f"Loaded {len(fixtures)} fixtures successfully")

categories = [fixture.expected.category for fixture in fixtures]
category_counts = Counter(categories)
print("Category Counts:")
for category, count in category_counts.items():
    print(f"- {category}: {count}")
    
urgencies = [fixture.expected.urgency for fixture in fixtures]
urgency_counts = Counter(urgencies)
print("Urgency counts:")
for urgency, count in urgency_counts.items():
    print(f"- {urgency}: {count}")


fixture_ids = [fixture.id for fixture in fixtures]
fixture_counts = Counter(fixture_ids)
duplicate_ids = [fixture_id for fixture_id, count in fixture_counts.items() if count > 1]
if duplicate_ids:
    print("Duplicate fixture ids:")
    for fixture_id in duplicate_ids:
        print(f"- duplicate id: {fixture_id}")
else:
    print("There are no duplicate fixture ids")

empty_missing_info_ids = [] 
for fixture in fixtures:
    if len(fixture.expected.missing_information) == 0:
        empty_missing_info_ids.append(fixture.id)
if empty_missing_info_ids:
    for empty_fixture_id in empty_missing_info_ids:
        print(f"Fixture id of fixture with no missing_information: {empty_fixture_id}")
else:
    print("All fixtures include at least one missing_information item.")


long_action_threshold = 18
for fixture in fixtures:
    action = fixture.expected.suggested_next_action
    word_count = len(action.split())
    
    if word_count > long_action_threshold:
        print("Long suggested next action details:")
        print(f"ID: {fixture.id}")
        print(f"Word Count: {word_count}")
        print(f"Action: {action}")
        print(" ")


short_message_threshold = 10

for fixture in fixtures:
    message = fixture.message
    message_word_count = len(message.split())
    
    if message_word_count < short_message_threshold:
        print("Short messages details: ")
        print(f"ID: {fixture.id}")
        print(f"Message_length {message_word_count}")
        print(f"Category: {fixture.expected.category}")
        print(f"Urgency: {fixture.expected.urgency}")
        print(f"Message: {fixture.message}")
        print(f"Missing Information: {fixture.expected.missing_information}")
        print()
        
for fixture in fixtures:
    if not fixture.id.startswith("fixture_"):
        print(f"Fixture {fixture.id} does not follow standard naming convention")
        print()       
        


