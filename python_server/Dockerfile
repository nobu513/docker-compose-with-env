FROM python:3.9

WORKDIR /app

COPY pyproject.toml . 

RUN pip install poetry && \
    poetry config virtualenvs.create

COPY . .

CMD ["poetry", "run", "python3", "main.py"]
