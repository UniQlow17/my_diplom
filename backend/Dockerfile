FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN sed -i 's/\r$//' /app/wait_db_connections.sh && \
    chmod +x /app/wait_db_connections.sh

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["/bin/bash", "/app/wait_db_connections.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "diplom.wsgi"]
