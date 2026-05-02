# Financial AI Assistant

A backend system that simulates an AI-powered financial assistant capable of analyzing transaction data, detecting anomalies, and generating spending insights.

The system is designed using a modular, tool-based architecture to mimic how modern AI systems (including LLM agents) route user queries to specialized functions.

---

## 🚀 Features

- Natural language-style query handling  
- Total and category-wise spend analysis  
- Anomaly detection for unusual transactions  
- Automated financial insights generation  
- Modular architecture for easy extension to LLM-based agents  

---

## 🧠 System Design

The system follows a tool-based architecture:

User Query  
→ Router (maps query → tool)  
→ Tools Layer (data processing functions)  
→ FastAPI Response (structured JSON)  

### Tools Implemented:

- `total_spend()` — calculates overall or category-specific spending  
- `total_income()` — computes total income  
- `category_breakdown()` — aggregates spend by category  
- `detect_anomaly()` — flags unusually high transactions  
- `generate_insights()` — produces high-level financial insights  

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- Pandas  
- Uvicorn  

---

## 📂 Project Structure


project/
├── app.py # FastAPI application
├── router.py # Query routing logic
├── tools.py # Core data processing functions
├── data/
│ └── transactions.csv
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/your-username/financial-ai-assistant.git
cd financial-ai-assistant

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app:app --host=0.0.0.0 --port=8000
📌 API Usage
Base URL

http://127.0.0.1:8000

Endpoint

GET /ask?query=your_query

💬 Example Queries

/ask?query=total spend  
/ask?query=food spend  
/ask?query=category breakdown  
/ask?query=any unusual transactions  
/ask?query=give insights  

📊 Sample Response
{
  "tool_used": "total_spend",
  "query": "total spend",
  "total_spend": 12400,
  "total_income": 50000,
  "message": "You spent ₹12400 out of ₹50000 income"
}
---
🔍 Key Engineering Decisions
Modular architecture: separated routing, logic, and API layers
Tool-based execution: simulates agent-style workflows
Data handling: used Pandas for efficient aggregation and filtering
Serialization fixes: converted NumPy outputs to native Python types for API compatibility
Extensibility: designed to support future LLM-based routing and tool-calling
⚠️ Challenges & Solutions
1. Data Serialization Issue

Pandas returns NumPy types (numpy.int64) which are not JSON serializable.

Solution: Explicit conversion to Python native types (int, dict) before returning API responses.

2. Incorrect Anomaly Detection

Initial implementation included income values, skewing thresholds.

Solution: Isolated expense data and used absolute value-based thresholding.

3. Query Routing

Initial system used basic keyword matching.

Solution: Refactored into a modular router that can be replaced with LLM-based decision making.

---
🔮 Future Improvements
Replace rule-based router with LLM-based tool selection
Add conversational memory and multi-step reasoning
Integrate real-world financial datasets
Add frontend dashboard for visualization
Introduce evaluation metrics for response quality
📈 What This Project Demonstrates
Backend system design for AI-driven applications
Handling real-world data issues (serialization, anomalies)
Building interpretable, modular ML/AI systems
Designing APIs for production-style use cases

---
👤 Author

Kavana Padaki
Machine Learning Engineer