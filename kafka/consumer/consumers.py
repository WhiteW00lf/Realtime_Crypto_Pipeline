from kafka import KafkaConsumer
import streamlit as st
import json
import time
import altair as alt
import pandas as pd

KAFKA_SERVER = "15.206.178.27:9092"

consumer = KafkaConsumer(
    "cryptoprices",
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

# Start Streamlit app
st.title("Bitcoin price tracker - near real-time")
placeholder = st.empty()
prices = []

print("Consumer started, waiting for messages...")
for message in consumer:
    data = message.value
    prices.append({"last_update": data["last_update"], "price": data["price"]})

    df = pd.DataFrame(prices)
    df["last_update"] = pd.to_datetime(df["last_update"])
    df.sort_values(by="last_update", inplace=True)

    chart = (
        alt.Chart(df)
        .mark_line(point=True)
        .encode(
            x="last_update:T",
            y=alt.Y("price:Q", scale=alt.Scale(reverse=False)),
        )
        .properties(width=700, height=400)
    )

    text = (
        alt.Chart(df)
        .mark_text(
            align="left",
            dx=5,
            dy=-5,  # adjust so text doesn't overlap point
            fontSize=10,
            color="black",
        )
        .encode(x="last_update:T", y="price:Q", text=alt.Text("price:Q", format=".2f"))
    )

    full_chart = chart + text

    with placeholder.container():
        st.altair_chart(full_chart, use_container_width=True)

    time.sleep(5)  # To avoid overwhelming the Streamlit app with updates
