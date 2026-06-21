FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501
EXPOSE 8000

CMD ["streamlit","run","src/churn/frontend/app.py","--server.address=0.0.0.0"]