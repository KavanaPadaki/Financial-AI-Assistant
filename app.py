from fastapi import FastAPI
from tools import total_spend, category_breakdown, detect_anomaly, generate_insights,total_income
from router import route_query

app = FastAPI(title="Financial AI Assistant")

@app.get("/")
def home():
    return {
        "message": "Financial AI Assistant is running",
        "endpoints": ["/ask?query=your_query_here"]
    }


@app.get("/ask")
def ask(query: str):
    """
    Main query endpoint.
    Routes query to appropriate tool and returns structured response.
    """

    action = route_query(query)

    try:
        # FOOD SPEND
        if action == "food_spend":
            result = total_spend("food")
            return {
                "tool_used": action,
                "query": query,
                "answer": f"Total food spend is ₹{result}"
            }

        # TOTAL SPEND
        elif action == "total_spend":
            result = total_spend()
            income = total_income()
            return {
                "tool_used": action,
                "query": query,
                "total_spend": result,
                "total_income": income,
                "message": f"You spent ₹{result} out of ₹{income} income"
            }

        # CATEGORY BREAKDOWN
        elif action == "breakdown":
            result = category_breakdown()
            return {
                "tool_used": action,
                "query": query,
                "data": result,
                "message": "Category-wise spending breakdown"
            }

        # ANOMALY DETECTION
        elif action == "anomaly":
            result = detect_anomaly()

            if not result:
                return {
                    "tool_used": action,
                    "query": query,
                    "message": "No anomalies detected"
                }

            return {
                "tool_used": action,
                "query": query,
                "anomalies": result,
                "message": "Unusual transactions detected"
            }

        # INSIGHTS
        else:
            result = generate_insights()

            if not result:
                return {
                    "tool_used": action,
                    "query": query,
                    "message": "No significant insights found"
                }

            return {
                "tool_used": action,
                "query": query,
                "insights": result
            }

    except Exception as e:
        return {
            "error": str(e),
            "message": "Something went wrong while processing the query"
        }