# Application Tracker

Features

* Keep a record of job application (CV submitted, JD, cover letter, date of submission, status)
* Generate cover letter based on JD and CV


## Configuration

| Variable | Description | Example |
|-|-|-|
| GOOGLE_APPLICATION_CREDENTIALS | Path to Service Account certificate (PEM) |  -  |
| ANTHROPIC_API_KEY | Anthropic API key | - |

## GCP Services needed

* Cloud Run
* Datastore
* Anthropic

## Running

### Docker

```
docker compose up
```

### Python

```
git clone https://github.com/devonho/apptrackr.git
virtualenv apptrackr
source ./apptrackr/bin/activate
pip install poetry
poetry install
streamlit run ./apptrackr/main.py
```
