

import json
import pytest
from typer.testing import CliRunner

import project
from project import __app_name__, __version__, cli
from project import (
    DB_READ_ERROR,
    SUCCESS,
    __app_name__,
    __version__,
    cli,
    compound,
)

runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


@pytest.fixture
def mock_json_file(tmp_path):
    data = [{}]
    db_file = tmp_path / "compound.json"
    with db_file.open("w") as db:
        json.dump(data, db, indent=4)
    return db_file


def test_add(mock_json_file, description, priority, expected):
    inst = project.Compound(mock_json_file)
    assert compound.add(description, priority) == expected
    read = compound._db_handler.read_compound()
    assert len(read.todo_list) == 0
