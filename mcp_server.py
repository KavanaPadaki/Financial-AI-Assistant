from mcp.server.fastmcp import FastMCP

from tools import (
    total_spend,
    total_income,
    category_breakdown,
    detect_anomaly,
    generate_insights,
    savings_rate,
    budget_health,
    top_spending_category,
    largest_expense,
    expense_income_summary,
    category_distribution,
    monthly_burn_rate,
    forecast_next_month_spend
)

mcp = FastMCP("Financial Assistant")


@mcp.tool()
def get_total_spend():
    """Get total spending."""
    return total_spend()


@mcp.tool()
def get_food_spend():
    """Get total food spending."""
    return total_spend("food")


@mcp.tool()
def get_total_income():
    """Get total income."""
    return total_income()


@mcp.tool()
def get_category_breakdown():
    """Get spending by category."""
    return category_breakdown()


@mcp.tool()
def get_anomalies():
    """Detect unusual transactions."""
    return detect_anomaly()


@mcp.tool()
def get_insights():
    """Generate financial insights."""
    return generate_insights()


@mcp.tool()
def get_savings_rate():
    """Calculate savings rate."""
    return savings_rate()


@mcp.tool()
def get_budget_health():
    """Evaluate financial health."""
    return budget_health()


@mcp.tool()
def get_top_spending_category():
    """Find highest spending category."""
    return top_spending_category()


@mcp.tool()
def get_largest_expense():
    """Find largest expense."""
    return largest_expense()


@mcp.tool()
def get_expense_income_summary():
    """Compare income and expenses."""
    return expense_income_summary()


@mcp.tool()
def get_category_distribution():
    """Category spending percentages."""
    return category_distribution()


@mcp.tool()
def get_monthly_burn_rate():
    """Monthly spending trend."""
    return monthly_burn_rate()


@mcp.tool()
def get_expense_forecast():
    """Forecast next month's spending."""
    return forecast_next_month_spend()


if __name__ == "__main__":
    mcp.run()