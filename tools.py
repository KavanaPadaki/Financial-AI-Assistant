import pandas as pd

# Load data once
df = pd.read_csv("data/transactions.csv")


# =========================
# TOTAL SPEND
# =========================
def total_spend(category=None):
    data = df[df["amount"] < 0]

    if category:
        data = data[data["category"] == category]

    return int(abs(data["amount"].sum()))


# =========================
# TOTAL INCOME
# =========================
def total_income():
    return int(df[df["amount"] > 0]["amount"].sum())


# =========================
# CATEGORY BREAKDOWN
# =========================
def category_breakdown():
    result = df.groupby("category")["amount"].sum().to_dict()

    # convert numpy types → python int
    return {k: int(v) for k, v in result.items()}


# =========================
# ANOMALY DETECTION
# =========================
def detect_anomaly():
    expenses = df[df["amount"] < 0].copy()

    # absolute spend for comparison
    expenses["abs_amount"] = expenses["amount"].abs()

    # threshold (simple heuristic)
    threshold = expenses["abs_amount"].mean() * 2

    anomalies = expenses[expenses["abs_amount"] > threshold]

    if anomalies.empty:
        return []

    # convert numpy types → python native
    anomalies = anomalies.astype(object)

    return anomalies.to_dict(orient="records")


# =========================
# INSIGHTS
# =========================
def generate_insights():
    total = total_spend()
    food = total_spend("food")

    insights = []

    # Food spending insight
    if total > 0 and food > 0.3 * total:
        insights.append("High spending on food (>30% of total spend)")

    # Anomaly insight
    if len(detect_anomaly()) > 0:
        insights.append("Unusual high-value transactions detected")

    # Top category insight
    expenses = df[df["amount"] < 0]
    if not expenses.empty:
        top_category = (
            expenses.groupby("category")["amount"]
            .sum()
            .abs()
            .idxmax()
        )
        insights.append(f"Highest spending category: {top_category}")

    return insights