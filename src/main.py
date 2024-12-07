from flask import Flask, render_template
from weather_data import fetch_weather_data, fetch_daily_summaries
from alerts import check_alerts
from visualizations import generate_daily_summary_plot, generate_historical_trend_plot, generate_alerts_plot
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    try:
        daily_summaries = fetch_daily_summaries()  # Fetch summaries
        alerts = check_alerts(daily_summaries)      # Fetch alerts

        if daily_summaries:
            generate_daily_summary_plot(daily_summaries)  # Generate daily summary plot
            generate_historical_trend_plot(daily_summaries)  # Generate historical trend plot
            generate_alerts_plot(alerts)  # Generate alerts plot

        return render_template('index.html', daily_summaries=daily_summaries, alerts=alerts)
    except Exception as e:
        logging.error(f"Error fetching weather data: {e}")
        return render_template('index.html', daily_summaries=[], alerts=["Failed to retrieve data. Please try again later."])

if __name__ == '__main__':
    app.run(debug=True)














