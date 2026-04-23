import pytest

from src.fixture_loader import load_golden_fixtures
from src.schemas import GoldenFixture


def test_load_valid_fixtures():
    fixtures = load_golden_fixtures("fixtures/test_valid.json")

    assert len(fixtures) == 2
    assert isinstance(fixtures[0], GoldenFixture)
    assert fixtures[0].id == "FP-001"
    assert fixtures[1].expected.category == "how_to"


def test_reject_invalid_urgency():
    with pytest.raises(ValueError) as exc_info:
        load_golden_fixtures("fixtures/test_invalid_urgency.json")

    assert "FP-003" in str(exc_info.value)
    assert "expected.urgency" in str(exc_info.value)


def test_reject_bad_top_level_shape():
    with pytest.raises(ValueError) as exc_info:
        load_golden_fixtures("fixtures/test_bad_shape.json")

    assert "top-level JSON array" in str(exc_info.value)