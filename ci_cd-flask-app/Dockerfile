FROM python:3.11-slim
WORKDIR /app
COPY ci_cd-flask-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
