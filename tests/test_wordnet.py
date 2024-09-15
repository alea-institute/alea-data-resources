# imports
from pathlib import Path

# project
from alea_data_resources.caching import delete_resource
from alea_data_resources.sources.wordnet import download


def test_wordnet():
    status = download()
    assert status
    assert (Path.home() / ".alea" / "data" / "wordnet-default").exists()


def test_wordnet_delete():
    delete_resource("wordnet")
    assert not (Path.home() / ".alea" / "data" / "wordnet-default").exists()
