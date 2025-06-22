def detect_anomalies(data):
    anomalies = []
    for entry in data:
        if entry['cpu_usage'] > 90 :
            anomalies.append(
                {
                    "timestamp" : entry['timestamp'],
                     "anomaly" : "High CPU usage",
                     "value" : entry['cpu_usage']
                    }
            )
        if entry['latency_ms'] > 300:
            anomalies.append(
                {
                    "timestamp" : entry['timestamp'],
                    "anomaly" : " High latency",
                    "value" : entry['latency_ms']
                }
            ) 
        if entry['memory_usage'] > 85 :
            anomalies.append(
                {
                    "timestamp" : entry['timestamp'],
                    "anomaly" : " High memory usage ",
                    "value" : entry['memory_usage']
                }
            )
        if entry['temperature_celsius'] > 80 :
            anomalies.append({
                "timestamp" : entry['timestamp'],
                "anomaly" : "High temperature",
                "value" : entry["temperature_celsius"]
            }) 
        if entry['error_rate'] > 0.05 :
            anomalies.append({
                "timestamp" : entry['timestamp'],
                "anomaly" : "High error rate",
                "value" : entry["error_rate"]
            })
    return anomalies