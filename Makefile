run:
	bash -c "python3 conference-planner/generate_plan.py conference-planner/sample_data/sample1.json"

test:
	bash -c "python3 -m venv test_venv && test_venv/bin/python3 -m pip install -r requirement.txt && test_venv/bin/pytest && rm -r test_venv";

cov:
	bash -c "python3 -m venv cov_venv && cov_venv/bin/python3 -m pip install -r requirement.txt && cov_venv/bin/pytest --cov=conference-planner && rm -r cov_venv";


