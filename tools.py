import pandas as pd

# Load data once
df = pd.read_csv("data/transactions.csv")


# =========================
# TOTAL SPEND
# =========================
def total_spend(category=None):

    data = df[df["amount"] < 0]

    if category:
        data = data[
            data["category"].str.lower()
            == category.lower()
        ]

    return int(abs(data["amount"].sum()))


# =========================
# TOTAL INCOME
# =========================
def total_income():

    return int(
        df[df["amount"] > 0]["amount"].sum()
    )


# =========================
# CATEGORY BREAKDOWN
# =========================
def category_breakdown():

    expenses = df[df["amount"] < 0]

    result = (
        expenses
        .groupby("category")["amount"]
        .sum()
        .abs()
        .to_dict()
    )

    return {
        k: int(v)
        for k, v in result.items()
    }


# =========================
# ANOMALY DETECTION
# =========================
def detect_anomaly():

    expenses = df[df["amount"] < 0].copy()

    expenses["abs_amount"] = (
        expenses["amount"].abs()
    )

    threshold = (
        expenses["abs_amount"].mean() * 2
    )

    anomalies = expenses[
        expenses["abs_amount"] > threshold
    ]

    if anomalies.empty:
        return []

    records = anomalies.to_dict(
        orient="records"
    )

    cleaned = []

    for row in records:

        clean_row = {}

        for key, value in row.items():

            if pd.isna(value):
                clean_row[key] = None

            elif isinstance(
                value,
                (str, int, float, bool)
            ):
                clean_row[key] = value

            else:
                clean_row[key] = str(value)

        cleaned.append(clean_row)

    return cleaned


# =========================
# INSIGHTS
# =========================
def generate_insights():

    insights = []

    total = total_spend()
    food = total_spend("food")

    if total > 0 and food > 0.3 * total:
        insights.append(
            "High spending on food (>30% of total spend)"
        )

    if len(detect_anomaly()) > 0:
        insights.append(
            "Unusual high-value transactions detected"
        )

    top_category = top_spending_category()

    if top_category:
        insights.append(
            f"Highest spending category: {top_category}"
        )

    return insights


# =========================
# SAVINGS RATE
# =========================
def savings_rate():

    income = total_income()
    spend = total_spend()

    if income == 0:
        return 0

    rate = (
        (income - spend) / income
    ) * 100

    return round(rate, 2)


# =========================
# BUDGET HEALTH
# =========================
def budget_health():

    income = total_income()
    spend = total_spend()

    if income == 0:
        return "No income data"

    ratio = spend / income

    if ratio < 0.5:
        return "Healthy"

    elif ratio < 0.8:
        return "Moderate"

    else:
        return "High Spending Risk"


# =========================
# TOP SPENDING CATEGORY
# =========================
def top_spending_category():

    expenses = df[df["amount"] < 0]

    if expenses.empty:
        return None

    return (
        expenses
        .groupby("category")["amount"]
        .sum()
        .abs()
        .idxmax()
    )


# =========================
# LARGEST EXPENSE
# =========================
def largest_expense():

    expenses = df[df["amount"] < 0]

    if expenses.empty:
        return {}

    row = expenses.loc[
        expenses["amount"].abs().idxmax()
    ]

    return {
        "category": str(row["category"]),
        "amount": abs(int(row["amount"]))
    }


# =========================
# EXPENSE VS INCOME
# =========================
def expense_income_summary():

    income = total_income()
    spend = total_spend()

    return {
        "income": income,
        "spend": spend,
        "remaining": income - spend
    }


# =========================
# CATEGORY DISTRIBUTION
# =========================
def category_distribution():

    expenses = df[df["amount"] < 0]

    total = (
        expenses["amount"]
        .abs()
        .sum()
    )

    if total == 0:
        return {}

    result = {}

    grouped = (
        expenses
        .groupby("category")["amount"]
        .sum()
        .abs()
    )

    for category, amount in grouped.items():

        result[category] = round(
            amount * 100 / total,
            2
        )

    return result


# =========================
# MONTHLY BURN RATE
# =========================
def monthly_burn_rate():

    if "date" not in df.columns:
        return {
            "error":
            "date column missing"
        }

    expenses = df[df["amount"] < 0]

    monthly = (
        expenses
        .groupby(
            pd.to_datetime(
                expenses["date"]
            ).dt.to_period("M")
        )["amount"]
        .sum()
        .abs()
    )

    return {
        str(k): int(v)
        for k, v in monthly.items()
    }


# =========================
# SPENDING FORECAST
# =========================
def forecast_next_month_spend():

    if "date" not in df.columns:
        return 0

    expenses = df[df["amount"] < 0]

    monthly = (
        expenses
        .groupby(
            pd.to_datetime(
                expenses["date"]
            ).dt.to_period("M")
        )["amount"]
        .sum()
        .abs()
    )

    if len(monthly) == 0:
        return 0

    return round(
        float(monthly.mean()),
        2
    )