import matplotlib.pyplot as plt
import os
from datetime import datetime

def generate_daily_summary_plot(daily_summaries):
    if not os.path.exists('static/plots'):
        os.makedirs('static/plots')
    
    cities = [summary['city'] for summary in daily_summaries]
    avg_temps = [summary['avg_temp'] for summary in daily_summaries]

    plt.figure(figsize=(10, 5))
    plt.bar(cities, avg_temps, color='blue')
    plt.xlabel('Cities')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Daily Average Temperature by City')
    plt.xticks(rotation=45)
    
    plt.savefig('static/plots/daily_summary.png')
    plt.close()

def generate_historical_trend_plot(summaries):
    if not os.path.exists('static/plots'):
        os.makedirs('static/plots')

    city = summaries[0]['city']  # Assuming all summaries are for the same city for simplicity
    dates = [summary['date'] for summary in summaries]
    avg_temps = [summary['avg_temp'] for summary in summaries]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.title(f'Historical Average Temperature Trend for {city}')
    plt.xticks(rotation=45)
    
    plt.savefig('static/plots/historical_trend.png')
    plt.close()

def generate_alerts_plot(alerts):
    if not os.path.exists('static/plots'):
        os.makedirs('static/plots')

    alert_counts = {}
    for alert in alerts:
        city = alert.split()[2]  # Assuming "Alert: {city} ..."
        alert_counts[city] = alert_counts.get(city, 0) + 1

    cities = list(alert_counts.keys())
    counts = list(alert_counts.values())

    plt.figure(figsize=(10, 5))
    plt.bar(cities, counts, color='red')
    plt.xlabel('Cities')
    plt.ylabel('Number of Alerts')
    plt.title('Alert Frequency by City')
    plt.xticks(rotation=45)

    plt.savefig('static/plots/alerts_frequency.png')
    plt.close()






