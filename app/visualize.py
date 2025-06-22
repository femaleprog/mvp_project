import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np

def plot_metric_realtime(metric, df, placeholder):
    # Thème esthétique
    sns.set_style("whitegrid")

    # Seuils définis
    thresholds = {
        "cpu_usage": 85,
        "memory_usage": 80,
        "latency_ms": 300,
        "error_rate": 0.1,
        "temperature_celsius": 75,
    }
    
    threshold = thresholds.get(metric, None)

    # Données normales et anomalies
    normal_points = df[df[metric] <= threshold]
    anomaly_points = df[df[metric] > threshold]

    fig, ax = plt.subplots(figsize=(6, 3))  # Taille plus compacte

    # Courbe des points normaux
    ax.plot(normal_points["timestamp"], normal_points[metric],
            label=metric.replace("_", " ").title(),
            color="blue", marker="o", markersize=4, linestyle="-")

    # Points d’anomalie
    ax.plot(anomaly_points["timestamp"], anomaly_points[metric],
            'ro', label="Anomaly", markersize=5)

    # Ligne du seuil

    if threshold is not None:
        ax.axhline(y=threshold, color="red", linestyle="--", linewidth=1, label="Threshold")
        

    # Formatage des dates pour lisibilité
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    #ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    plt.xticks(rotation=45, ha="right")

    # Titre et légende
    ax.set_title(metric.replace("_", " ").title(), fontsize=12, pad=10)
    ax.legend(fontsize="small", bbox_to_anchor=(1.01, 1), loc="upper left", frameon=False)


    # Meilleur agencement
    fig.tight_layout()

    placeholder.pyplot(fig)
