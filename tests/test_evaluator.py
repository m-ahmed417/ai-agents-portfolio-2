from src.evaluator import evaluate_single_fixture
from src.schemas import TicketRoute, GoldenFixture
from src.providers.base import BaseTriageProvider


class FakeProvider(BaseTriageProvider):
    def route_ticket(self, message: str) -> TicketRoute:
        return TicketRoute(
            category='how_to',
            urgency='low',
            suggested_next_action='provide guidance on the feature',
            confidence=0.7,
            missing_information=[]
        )
    
class MismatchFakeProvider(BaseTriageProvider):
    def route_ticket(self, message: str) -> TicketRoute:
        return TicketRoute(
            category='billing',
            urgency='critical',
            suggested_next_action='provide a refund',
            confidence=0.8,
            missing_information=[]
        )


def test_evaluate_single_fixture_detects_match():
    fixture = GoldenFixture(
        id="test_01",
        message="How do I export a report?",
        expected={
            "category": "how_to",
            "urgency": "low",
            "missing_information": [],
            "suggested_next_action": "Provide guidance on exporting reports.",
        },
        notes="Simple how-to ticket.",
    )

    provider = FakeProvider()
    
    result = evaluate_single_fixture(fixture, provider)
       
    assert result["fixture_id"] == "test_01"
    assert result["expected_category"] == "how_to"
    assert result["actual_category"] == "how_to"
    assert result["category_match"] is True
    assert result["expected_urgency"] == "low"
    assert result["actual_urgency"] == "low"
    assert result["urgency_match"] is True
     
     
def test_evaluate_single_fixture_detects_mismatch():
    fixture = GoldenFixture(
        id="test_02",
        message="How do I export a report?",
        expected={
            "category": "how_to",
            "urgency": "low",
            "missing_information": [],
            "suggested_next_action": "Provide guidance on exporting reports.",
        },
        notes="Simple how-to ticket.",
    )

    provider = MismatchFakeProvider()
    
    result = evaluate_single_fixture(fixture, provider)
       
    assert result["actual_category"] == "billing"
    assert result["category_match"] is False
    assert result["actual_urgency"] == "critical"
    assert result["urgency_match"] is False
    assert result["fixture_id"] == "test_02"
    assert result["expected_category"] == "how_to"
    assert result["expected_urgency"] == "low"