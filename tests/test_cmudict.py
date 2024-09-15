# imports
from pathlib import Path

# project
from alea_data_resources.caching import delete_resource
from alea_data_resources.sources.cmudict import download


def test_cmudict():
    status = download()
    assert status
    assert (Path.home() / ".alea" / "data" / "cmudict-default").exists()


def test_cmudict_delete():
    delete_resource("cmudict")
    assert not (Path.home() / ".alea" / "data" / "cmudict-default").exists()
