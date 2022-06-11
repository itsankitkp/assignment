# assignment

This repo contains a python script for solution of problem #3.
Following conditions are followed:
• The conference has multiple tracks each of which has a morning and afternoon
session.
• Each session contains multiple talks.
• Morning sessions begin at 9am and must finish by 12 noon, for lunch.
• Afternoon sessions begin at 1pm and must finish in time for the networking
event.
• The networking event can start no earlier than 4:00 and no later than 5:00.
• No talk title has numbers in it.
• All talk lengths are either in minutes (not hours) or lightning (5 minutes).
• Presenters will be very punctual; there needs to be no gap between sessions.

Note: Sample out in the given in the pdf didn't align with all given condition, namely
networking event were scheduled post closing time (5PM). Such diversion from given condition is not 
implemented and condition (as mentioned) is strictly followed.

<details><summary>Installing dependencies (Debian/Ubuntu or equivalent)</summary>
<p>

1. Download and install python3 from https://www.python.org/downloads/ .
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

<details><summary>Set up development machine</summary>
<p>
1. Install dependencies as given above.
2.
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