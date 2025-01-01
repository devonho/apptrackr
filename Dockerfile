FROM bitnami/python:3.12

WORKDIR /app

COPY ./apptrackr /app/apptrackr
COPY ./pyproject.toml /app/pyproject.toml
COPY ./README.md /app/README.md
COPY ./entrypoint.sh /app/entrypoint.sh

RUN pip install poetry
RUN poetry install
RUN pip install .

ENTRYPOINT [ "/bin/bash" ]
CMD [ "/app/entrypoint.sh" ]