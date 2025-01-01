# Application Tracker

Features

* Keep a record of job application (CV submitted, JD, cover letter, date of submission, status)
* Generate cover letter based on JD and CV
* Chat with JD and CV


## Configuration

| Variable | Description | Example |
|-|-|-|
| GOOGLE_APPLICATION_CREDENTIALS | Path to Service Account certificate (PEM) |  -  |
| ANTHROPIC_API_KEY | Anthropic API key | - |
| OAUTH2_PROVIDER | OAuth2 provider | google |
| OAUTH2_CLIENT_ID | Service principal ID | - | 
| OAUTH2_CLIENT_SECRET | Service principal secret | - | 
| OAUTH2_REDIRECT_URL | Redirect URL after return from IdP | http://localhost:8080  | 

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
