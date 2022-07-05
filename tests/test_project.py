

import json
import pytest
from typer.testing import CliRunner

import project

runner = CliRunner()


@pytest.fixture
def mock_json_file(tmp_path):
    data = [{}]
    db_file = tmp_path / "compound.json"
    with db_file.open("w") as db:
        json.dump(data, db, indent=4)
    return db_file

