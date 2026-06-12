FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -e .

EXPOSE 7860

ENV FLASK_APP=app.py

CMD ["python", "app.py"]