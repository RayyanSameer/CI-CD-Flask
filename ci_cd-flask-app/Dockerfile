FROM python:3.11-slim
WORKDIR /app

# Copy only what you need
COPY ci_cd-flask-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the app code only
COPY ci_cd-flask-app/app.py .
COPY ci_cd-flask-app/test.py .

CMD ["python", "app.py"]
