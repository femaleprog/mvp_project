import json
from app.llm import call_mistral_model

def generate_prompt(anomaly):
    return f"""
You are an expert monitoring assistant.
Your role is to return one very short, actionable recommendation for a given anomaly.
Here are examples:
- Anomaly: High error rate, Value: 0.12 -> Action: Check service status and restart failing services.
- Anomaly: High latency, Value: 334 -> Action: Scale resources or review database indexes.
- Anomaly: High CPU usage, Value: 93 -> Action: Check running processes and optimize workloads.

Given this anomaly:
- Type: {anomaly['anomaly']}
- Value: {anomaly['value']}

Return one short actionable action (one sentence).
"""


def generate_recommendations(anomalies):
    recommendations = []
    for anomaly in anomalies:
        prompt = generate_prompt(anomaly)
        response = call_mistral_model(prompt)

        recommendations.append({
            "timestamp": anomaly["timestamp"],
            "anomaly": anomaly["anomaly"],
            "value": anomaly["value"],
            "recommendation": response
        })
    return recommendations
