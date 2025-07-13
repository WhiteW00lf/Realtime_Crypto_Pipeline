import json
from kafka import KafkaProducer
import requests
from dotenv import load_dotenv
import os
import time

KAFKA_SERVER = '3.110.156.76:9092'

producer = KafkaProducer( bootstrap_servers=KAFKA_SERVER)

URL = 'https://api.freecryptoapi.com/v1/getData?symbol=BTC '

load_dotenv()



HEADERS = {
    'Authorization': f"Bearer {os.getenv('API_KEY')}"
}


    

def make_request(url):
    data = requests.get(url, headers=HEADERS)
    default_dict = data.json()
    crypto_name = default_dict['symbols'][0]['symbol']
    price = default_dict['symbols'][0]['last']
    last_update = default_dict['symbols'][0]['date']
    data_in_json = json.dumps({
        'crypto_name': crypto_name,
        'price': price,
        'last_update': last_update
    })

    print(f"Sending data to Kafka")

    producer.send('cryptoprices', value=data_in_json.encode('utf-8'))
    producer.flush()




while True:

    make_request(URL)
    time.sleep(5)



