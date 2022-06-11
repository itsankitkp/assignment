# Assignment Project for allocating Conference tracks

This repo contains a python script for solution of problem #3.<br>
The following conditions are followed:
<ul>
  <li>The conference has multiple tracks each of which has a morning and afternoon
session.</li>
  <li>Each session contains multiple talks</li>
  <li>Morning sessions begin at 9am and must finish by 12 noon, for lunch</li>
  <li>Afternoon sessions begin at 1pm and must finish in time for the networking
event.</li>
  <li>The networking event can start no earlier than 4:00 and no later than 5:00.</li>
  <li>No talk title has numbers in it.</li>
  <li>All talk lengths are either in minutes (not hours) or lightning (5 minutes).</li>
  <li>Presenters will be very punctual; there needs to be no gap between sessions.</li>
</ul>

<p>
Note: Sample out in the given in the pdf didn't align with all given condition, namely
networking event were scheduled post closing time (5PM). Such diversion from given condition is not
implemented and condition (as mentioned) is strictly followed.
</p>
<details><summary>Installing dependencies (Debian/Ubuntu or equivalent)</summary>
<p>

1. Download and install python3 from <https://www.python.org/downloads/> .
2. Create a virtual environment.

```
python3 -m venv venv
```

Note: You may need to install `python3-venv` in some distros

3. Activate virtual environment.

```
source venv/bin/activate
````

4. Install Python dependencies.

```
pip install -r requirement.txt
```

</p>
</details>

<details><summary>Running script</summary>
<p>
1. Ensure that you are in virtualenv
2. Run following command:

```
python3 generate_plan.py <path_to_json_data>
```

</p>
</details>

<details><summary>Running sample data</summary>
<p>
1. Ensure that you are in virtualenv
2. Run following command:

```
python3 generate_plan.py sample_data/sample1.json
```

Choose different sample files: sample1.jsom, sample2.json, sample3.json
or create your own using these files.

</p>
</details>

<details><summary>Running tests</summary>
<p>

1. Ensure that you are in virtual environment
2. Run all tests

```
pytest
```

3. Get coverage report

```
pytest --cov=conference-planner
```

</p>
</details>
