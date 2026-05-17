# Sales Forecasting and Business Insights Using Data Analytics and Machine Learning with Python

## 📌 Project Overview

This project predicts future sales using historical sales data and provides business insights through an interactive dashboard.

The system performs:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering
* Machine learning model training
* 12-month sales forecasting
* Flask API development
* Interactive dashboard visualization using Plotly

---

## 🚀 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Flask
* HTML
* CSS
* JavaScript
* Plotly
* Jupyter Notebook

---

## 📁 Project Structure

```text
sales_forecasting_project/
├── backend/
│   └── app.py
├── data/
│   ├── sales.csv
│   ├── cleaned_sales.csv
│   ├── monthly_sales_features.csv
│   └── future_sales_forecast.csv
├── models/
│   └── sales_forecast_model.pkl
├── static/
│   └── script.js
├── templates/
│   └── index.html
├── analysis.ipynb
├── monthly_sales_trend.png
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sales-forecasting-project.git
cd sales-forecasting-project
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask Application

```bash
python backend/app.py
```

### 6. Open the Dashboard

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 📊 Dashboard Features

* Total predicted sales
* Average monthly sales
* Highest and lowest monthly sales
* Interactive 12-month forecast chart

---

## 🤖 Machine Learning Workflow

1. Load historical sales data
2. Clean and preprocess the dataset
3. Aggregate monthly sales
4. Create lag-based features
5. Train a Random Forest Regressor
6. Predict future sales
7. Save model and forecast results

---

## 📈 Model Used

**Random Forest Regressor**

Why this model?

* Handles non-linear patterns
* Robust to noise
* Good baseline performance for forecasting

---

## 📌 API Endpoints

| Endpoint    | Description                   |
| ----------- | ----------------------------- |
| `/`         | Dashboard homepage            |
| `/forecast` | Returns forecast data in JSON |
| `/summary`  | Returns KPI summary values    |

---

## 🖼️ Sample Output

* KPI cards with summary metrics
* Interactive line chart of predicted sales

---

## 🎯 Business Insights

The dashboard helps businesses:

* Predict future demand
* Identify growth trends
* Plan inventory
* Optimize marketing strategies
* Improve decision-making

---

## 🔮 Future Enhancements

* Deploy to cloud platforms
* Add user authentication
* Support CSV upload from UI
* Compare multiple forecasting models
* Export reports as PDF

---

## 👩‍💻 Author

**Mounashree MR**

MCA Student | Aspiring Data Analyst | Machine Learning Enthusiast

---

## 📜 License

This project is for educational and academic purposes.
