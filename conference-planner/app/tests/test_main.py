import os

import pytest
from app.main import entrypoint


class TestConferenceMain:
    def test_wrong_file_path(self):
        with pytest.raises(IOError):
            entrypoint("/")

    def test_wrong_file_path(self):
        with pytest.raises(Exception):
            entrypoint(1)

    def test_read_sample_file(self):
        entrypoint(f"{os.path.dirname(__file__)}/test_data.json")
