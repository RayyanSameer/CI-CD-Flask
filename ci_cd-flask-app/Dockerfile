FROM python:3.11-slim
WORKDIR /app

# Copy only what you need
COPY ci_cd-flask-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the app code only
COPY ci_cd-flask-app/app.py .
COPY ci_cd-flask-app/test.py .


ENV FLASK_ENV=production
ENV PORT=1000

EXPOSE 1000


CMD ["python", "app.py"]
