import pytest
from src.providers.base import BaseTriageProvider
from src.schemas import TicketRoute

def test_base_provider_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseTriageProvider()
        

class FakeTriageProvider(BaseTriageProvider):
    def route_ticket(self, message: str) -> TicketRoute:
        return TicketRoute(
    category="how_to",
    urgency="low",
    missing_information=[],
    suggested_next_action="Send guidance for using the feature.",
    confidence=0.9,
)
        

def test_fake_provider_returns_ticket_route():
    provider = FakeTriageProvider()

    route = provider.route_ticket("How do I export a report?")

    assert isinstance(route, TicketRoute)
    assert route.category == "how_to"
    assert route.urgency == "low"
    assert route.confidence == 0.9
