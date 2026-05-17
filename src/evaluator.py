from src.schemas import GoldenFixture
from src.providers.base import BaseTriageProvider



def evaluate_single_fixture(fixture: GoldenFixture, provider: BaseTriageProvider) -> dict:
    actual_route = provider.route_ticket(fixture.message)
    category_match = actual_route.category == fixture.expected.category
    urgency_match = actual_route.urgency == fixture.expected.urgency
    return {
        "fixture_id": fixture.id,
        "expected_category": fixture.expected.category,
        "actual_category": actual_route.category,
        "category_match": category_match,
        "expected_urgency": fixture.expected.urgency,
        "actual_urgency": actual_route.urgency,
        "urgency_match": urgency_match
    }