FROM bitnami/python:3.12

WORKDIR /app

COPY ./apptrackr /app/apptrackr
COPY ./pyproject.toml /app/pyproject.toml
COPY ./README.md /app/README.md

RUN pip install poetry
RUN poetry install
RUN pip install .

CMD streamlit run /app/apptrackr/main.py