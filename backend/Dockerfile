FROM python:3.7.3-alpine3.9

WORKDIR /app

ADD . .

RUN python -m pip install --upgrade pip  # Upgrade pip first
RUN python -m pip install -r requirement.txt  # Then install dependencies

CMD ["python", "app.py"]
