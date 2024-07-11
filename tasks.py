from celery.app import Celery
import requests
import os
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()
redis_url = os.getenv("REDIS_URL")

app = Celery(__name__, broker=redis_url, backend=redis_url)

@app.task
def fetch_books():
    url='http://fastapi:8000/books'
    response = requests.get(url)
    if response.status_code == 200:
        producer = KafkaProducer(bootstrap_servers='kafka:9093')
        producer.send('my-topic', value=response.content)
        producer.close()
    return 