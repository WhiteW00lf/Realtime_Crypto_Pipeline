from kafka import KafkaConsumer
import sqlite3

KAFKA_SERVER = '15.206.178.27:9092'

consumer = KafkaConsumer(
    'cryptoprices',
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset='earliest'
)

print("Consumer started, waiting for messages...")
for message in consumer:
    data = message.value.decode('utf-8')
    print(f"Received message: {data}")


