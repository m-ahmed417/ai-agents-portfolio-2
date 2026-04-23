from pathlib import Path
import json
from pydantic import ValidationError
from src.schemas import GoldenFixture

def load_golden_fixtures(path: str | Path) -> list[GoldenFixture]:
        path = Path(path)
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Fixture file must contain a top-level JSON array.")
        
        fixtures: list[GoldenFixture] = []
        for index, item in enumerate(data):
            try:
                fixture = GoldenFixture.model_validate(item)
                fixtures.append(fixture)
            except ValidationError as e:
                fixture_id = item.get("id", "<missing id>") if isinstance(item, dict) else "<not an object>"
                raise ValueError(
                f"Invalid fixture at index {index} with id {fixture_id}: {e}"
                ) from e
        return fixtures
    
