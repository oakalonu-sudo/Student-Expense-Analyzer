from flask import Flask
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route("/expenses")
def expenses():
    df = pd.read_csv("expense.csv")
    return df.to_json(orient="records")

@app.route("/expenses/total")
def total_expenses():
    df = pd.read_csv("expense.csv")
    total = df["Amount"].sum()
    return {"total": total}

@app.route("/expenses/monthly")
def monthly_expenses():
    df = pd.read_csv("expense.csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%m-%d-%Y")
    monthly_totals = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()
    return monthly_totals.to_json()

def predict_next_month():
    df = pd.read_csv("expense.csv")

    df["Date"] = pd.to_datetime(df["Date"], format="%m-%d-%Y")
    df["Month"] = df["Date"].dt.month

    month_order = [8,9,10,11,12,1,2,3,4,5,6]

    monthly_data = df.groupby('Month')['Amount'].sum().reset_index()

    monthly_data = monthly_data.set_index('Month').loc[month_order].reset_index()

    monthly_data['Previous_Month'] = monthly_data['Amount'].shift(1)

    monthly_data = monthly_data.dropna()

    x = monthly_data[['Previous_Month']]
    y = monthly_data['Amount']

    model = LinearRegression()
    model.fit(x, y)

    latest_amount = monthly_data['Amount'].iloc[-1]

    prediction = model.predict([[latest_amount]])

    return prediction[0]

@app.route("/expenses/predict")
def predict():
    prediction = predict_next_month()
    return {"predicted_expenses": prediction}

if __name__ == "__main__":
    app.run(debug=True)