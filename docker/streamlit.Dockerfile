FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --default-timeout=1000 -r requirements.txt


COPY . .


RUN pip install -e .

ENV PYTHONPATH=/app

EXPOSE 8501

CMD ["streamlit", "run", "src/churn/frontend/app.py", "--server.address=0.0.0.0", "--server.port=8501"]