from flask import Flask, jsonify, render_template
import pandas as pd
import joblib
from pathlib import Path

# Create Flask app
app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load trained model
model = joblib.load(BASE_DIR / "models" / "sales_forecast_model.pkl")

# Load forecast data
future_df = pd.read_csv(BASE_DIR / "data" / "future_sales_forecast.csv")


# Home page route
@app.route('/')
def home():
    return render_template('index.html')


# Forecast API route
@app.route('/forecast')
def forecast():
    data = future_df.to_dict(orient='records')
    return jsonify(data)


# Summary API route
@app.route('/summary')
def summary():
    summary_data = {
        "total_predicted_sales": round(future_df['Predicted Sales'].sum(), 2),
        "average_monthly_sales": round(future_df['Predicted Sales'].mean(), 2),
        "highest_monthly_sales": round(future_df['Predicted Sales'].max(), 2),
        "lowest_monthly_sales": round(future_df['Predicted Sales'].min(), 2)
    }
    return jsonify(summary_data)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)