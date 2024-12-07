def check_alerts(daily_summaries):
    alerts = []
    for summary in daily_summaries:
        # Example alert condition: temperature exceeds 35 degrees Celsius
        if summary['avg_temp'] > 35:
            alerts.append(f"Alert: {summary['city']} has exceeded the temperature threshold! Current: {summary['avg_temp']}°C")
    return alerts







