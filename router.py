def route_query(query: str) -> str:
    """
    Routes user query to appropriate tool.
    
    Returns one of:
    - food_spend
    - total_spend
    - breakdown
    - anomaly
    - insights
    """

    query = query.lower()

    # FOOD SPENDING
    food_keywords = ["food", "swiggy", "zomato", "eat", "restaurant"]
    if any(word in query for word in food_keywords):
        return "food_spend"

    # TOTAL SPENDING
    total_keywords = ["total", "overall", "all spend", "expenses", "spent"]
    if any(word in query for word in total_keywords):
        return "total_spend"

    # CATEGORY BREAKDOWN
    breakdown_keywords = ["category", "breakdown", "distribution", "split"]
    if any(word in query for word in breakdown_keywords):
        return "breakdown"

    # ANOMALY DETECTION
    anomaly_keywords = ["anomaly", "unusual", "suspicious", "weird", "high spend"]
    if any(word in query for word in anomaly_keywords):
        return "anomaly"

    # DEFAULT → INSIGHTS
    return "insights"