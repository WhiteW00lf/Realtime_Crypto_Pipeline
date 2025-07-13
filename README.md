Crypto Price Tracker (Real-time) 🚀
A simple, real-time Bitcoin price tracker built from scratch using:

🐍 Python

🧩 Apache Kafka

🖼 Streamlit dashboard

☁ Runs on EC2

🔌 FreeCryptoAPI 

Project Overview
This project:
✅ Connects to a crypto API using HTTP
✅ Streams live Bitcoin prices into Kafka
✅ Stores the prices
✅ Displays them in near real-time on an interactive dashboard with Streamlit

📡 Data flow:
API → Kafka Producer → Kafka Topic → Kafka Consumer → Streamlit → Dashboard


| Tool      |            Purpose |
| --------- | -----------------: |
| Python    |      Main language |
| Kafka     | Streaming platform |
| Streamlit |          Dashboard |
| EC2       |         Deployment |
| Altair    |   Beautiful charts |


⚙️ How it works

Producer (producer.py): connects to the FreeCrypto API (using your API key) and sends price data to Kafka.

Kafka: brokers and stores messages in topic cryptoprices.

Consumer + Streamlit (consumer.py): reads data and displays a live updating chart with point values


🚀 Quick Start 

```bash
git clone https://github.com/WhiteW00lf/Realtime_Crypto_Pipeline.git

cd Realtime_Crypto_Pipeline

pip install -r requirements.txt

**Set up Kafka on your EC2 machine (e.g., with Docker or directly).
Make sure it’s running and accessible**

python3 producer.py

streamlit run consumer.py

Open the dashboard

http://<your-ec2-ip>:8501




```
