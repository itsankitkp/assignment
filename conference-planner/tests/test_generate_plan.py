import sys
import os

import pytest
from generate_plan import main


class TestGeneratePlan:
    def test_no_param_gen_file(self):
        with pytest.raises(Exception):
            main()

    def test_with_param_file(self):
        sys.argv = [
            "generate_plan.py",
            f"{os.path.dirname(__file__)}/../sample_data/sample1.json",
        ]
        try:
            main()
        except:
            pytest.fail("Unexpected Error while running sample file")
