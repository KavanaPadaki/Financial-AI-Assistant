# Financial AI Assistant

A backend system that simulates an AI-powered financial assistant capable of analyzing transaction data, detecting anomalies, and generating spending insights.

---

## 🚀 Features

- Natural language-style query handling  
- Total and category-wise spend analysis  
- Anomaly detection for unusual transactions  
- Automated financial insights generation  
- Modular architecture for extensibility  

---

## 🧠 System Design

User Query  
→ Router (query → tool mapping)  
→ Tools Layer (data processing functions)  
→ FastAPI Response (structured JSON)  

### Tools Implemented

- total_spend()  
- total_income()  
- category_breakdown()  
- detect_anomaly()  
- generate_insights()  

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- Pandas  
- Uvicorn  

---

## 📂 Project Structure

```
project/
├── app.py
├── router.py
├── tools.py
├── data/
│   └── transactions.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

```bash
git clone https://github.com/your-username/financial-ai-assistant.git
cd financial-ai-assistant
pip install -r requirements.txt
```

---

## ▶️ Run the Server

```bash
uvicorn app:app --host=0.0.0.0 --port=8000
```

---

## 📌 API Usage

GET /ask?query=your_query

---

## 💬 Example Queries

- /ask?query=total spend  
- /ask?query=food spend  
- /ask?query=category breakdown  
- /ask?query=any unusual transactions  
- /ask?query=give insights  

---

## 📊 Sample Response

```json
{
  "tool_used": "total_spend",
  "query": "total spend",
  "total_spend": 12400,
  "total_income": 50000,
  "message": "You spent ₹12400 out of ₹50000 income"
}
```

---

## 🔍 Key Engineering Decisions

- Modular separation of routing, logic, and API  
- Tool-based execution design  
- Explicit conversion of NumPy outputs to native Python types  
- Structured API responses  

---

## ⚠️ Challenges & Fixes

Serialization Issue:
Pandas returns NumPy types not JSON serializable  
Fix: Convert to Python native types  

Anomaly Detection Issue:
Income skewed results  
Fix: Filter only expenses  

---

## 🔮 Future Improvements

- LLM-based routing  
- Memory support  
- UI dashboard  
- Real datasets  

---

## 👤 Author

Kavana Padaki
