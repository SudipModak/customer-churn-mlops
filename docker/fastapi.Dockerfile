FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

COPY . .

RUN pip install -e .

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn","src.churn.serving.app:app","--host","0.0.0.0","--port","8000"]