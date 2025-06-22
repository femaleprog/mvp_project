import streamlit as st
import json
import time
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

from app.ingestion import load_data
from app.detection import detect_anomalies
from app.recommendation import generate_recommendations
from app.visualize import plot_metric_realtime
import pdb

st.set_page_config(page_title="Infra Watch", layout="centered")
st.title("🧠 Smart Infra Monitor")

uploaded_file = st.file_uploader("Drop your json file here", type="json")

if uploaded_file:
    
    if st.button("🔍 Analysis"):
        data = load_data(uploaded_file)
        
        st.subheader(" Real time simulation")
        metrics = ["cpu_usage", "memory_usage", "latency_ms", "error_rate", "temperature_celsius"]
        chart_placeholders = {metric : st.empty() for metric in metrics}

        recommendations_container = st.container()

        df_live = pd.DataFrame(columns=["timestamp"]+ metrics)

        recommendations_df = pd.DataFrame(columns=["🕒 Timestamp", "⚠️ Anomaly", "✅ Recommended Action"])
        recommendations_placeholder = recommendations_container.empty()

        for row in data:
            
            new_row = {
                "timestamp" : pd.to_datetime(row["timestamp"]),
                **{metric: row[metric] for metric in metrics}
            }

            df_live = pd.concat([df_live, pd.DataFrame([new_row])], ignore_index=True)

            for metric in metrics:
                plot_metric_realtime(metric, df_live, chart_placeholders[metric])

            anomalies = detect_anomalies([row])

            if anomalies :
                
                recos = generate_recommendations(anomalies)

                new_reco_df = pd.DataFrame(recos)

                new_reco_df = new_reco_df.rename(columns = {
                    "timestamp" : "🕒 Timestamp",
                    "anomaly"  : "⚠️ Anomaly",
                    "recommendation" : "✅ Recommended Action"
                })
            
                # Add to the top of the main dataframe
                recommendations_df = pd.concat([new_reco_df, recommendations_df], ignore_index=True)
                recommendations_df["🕒 Timestamp"] = pd.to_datetime(recommendations_df["🕒 Timestamp"])
                recommendations_df["🕒 Timestamp"] = pd.to_datetime(recommendations_df["🕒 Timestamp"])
                
                #Display updated recommendations_container
                recommendations_placeholder.markdown("### 💡 Recommandations en Temps Réel")
                recommendations_placeholder.dataframe(recommendations_df, use_container_width=True, hide_index=True)
                
            time.sleep(0.3)
        