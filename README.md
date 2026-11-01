# Weather Data Pipeline

A small Python project that pulls daily weather data for a given location from the [Open-Meteo API](https://open-meteo.com/), checks that the response is usable, and handles failures along the way.

I built it to learn how to work with a real API: sending requests, dealing with failing responses, splitting code into modules, and writing tests for it.

## What it does

- Requests daily maximum and minimum temperatures for a given location
- Handles timeouts, HTTP errors, connection failures, and invalid JSON responses
- Validates the response by checking required fields, data types, and matching array lengths
- Keeps extraction, validation, and the pipeline flow in separate modules
- Includes pytest tests that use mocking, so they run without calling the real API

## Project layout

```
weather-data-pipeline/
├── data/
│   └── kathmandu_weather_data.csv
├── images/
├── notebooks/
│   ├── weather_data_extraction.ipynb
│   └── executing_pipeline.ipynb
├── src/
│   ├── extract.py
│   ├── validate.py
│   └── pipeline.py
├── tests/
│   ├── test_extract.py
│   ├── test_validate.py
│   └── test_pipeline.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Running it

Clone the repository and set up a virtual environment:

```
git clone <your-repository-url>
cd weather-data-pipeline
python -m venv .venv
```

Activate it (Windows):

```
.venv\Scripts\activate
```

Or on Mac/Linux:

```
source .venv/bin/activate
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the pipeline:

```python
from src.pipeline import run_weather_pipeline

weather_data = run_weather_pipeline(27.7172, 85.3240, "Asia/Kathmandu")
print(weather_data)
```

The three arguments are latitude, longitude, and timezone, so you can use coordinates for any other location. The `executing_pipeline.ipynb` notebook walks through the same run step by step.

Run the tests:

```
pytest -v
```

## How the pieces fit

`extract.py` makes the API request and handles request and JSON errors. `validate.py` checks that the returned data has the structure the rest of the code expects. `pipeline.py` calls the two in order and returns the validated data.

## Built with

Python, Requests, Pytest, and Jupyter Notebook.

Data source: [Open-Meteo](https://open-meteo.com/). This is a personal learning project.