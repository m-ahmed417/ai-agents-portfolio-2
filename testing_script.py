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
