from flask import Flask
import pandas as pd

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

if __name__ == "__main__":
    app.run(debug=True)