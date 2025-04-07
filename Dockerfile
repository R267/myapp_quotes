FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN apk add --no-cache gcc musl-dev postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DB_HOST=db
ENV DB_NAME=quotes_db
ENV DB_USER=postgres
ENV DB_PASS=postgres
CMD ["python", "app.py"]