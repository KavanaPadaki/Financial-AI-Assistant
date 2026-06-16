# Financial AI Assistant with MCP

An MCP-enabled AI-powered financial assistant that analyzes transaction data, generates spending insights, detects anomalies, forecasts expenses, and autonomously selects financial tools using a Large Language Model.

---

## Overview

This project demonstrates an Agentic AI architecture using:

* FastAPI
* Model Context Protocol (MCP)
* LangGraph / LangChain Agents
* Groq Llama 3.3 70B
* Pandas

Instead of relying on hardcoded routing logic, the AI agent dynamically discovers and invokes financial analysis tools exposed through an MCP server.

---

## Features

### Financial Analytics

* Total spend analysis
* Total income analysis
* Category-wise spending breakdown
* Spending distribution percentages
* Largest expense detection
* Top spending category identification
* Savings rate calculation
* Budget health assessment
* Expense vs income summary
* Monthly burn rate analysis
* Spending forecast generation
* Anomaly detection
* Automated financial insights

### AI Capabilities

* Natural language financial queries
* Autonomous tool selection
* MCP-based tool discovery
* Multi-tool reasoning and execution
* LLM-driven financial assistance

---

## Architecture

User Query

↓
AI Agent (Groq Llama 3.3)

↓
MCP Client

↓
Financial MCP Server

↓
Financial Analytics Tools

↓
Structured Financial Response

---

## MCP Tools Exposed

### Core Analytics

* get_total_spend
* get_food_spend
* get_total_income
* get_category_breakdown

### Intelligence Tools

* get_savings_rate
* get_budget_health
* get_top_spending_category
* get_largest_expense
* get_expense_income_summary
* get_category_distribution
* get_monthly_burn_rate
* get_expense_forecast

### Insights

* get_anomalies
* get_insights

---

## Project Structure

```text
project/
│
├── app.py
├── agent.py
├── client.py
├── mcp_server.py
├── tools.py
│
├── data/
│   └── transactions.csv
│
├── requirements.txt
└── README.md
```

---

## Tech Stack

* Python
* FastAPI
* Pandas
* MCP (Model Context Protocol)
* LangGraph
* LangChain MCP Adapters
* Groq API
* Llama 3.3 70B
* Uvicorn

---

## Setup

### Clone Repository

```bash
git clone https://github.com/your-username/financial-ai-assistant.git

cd financial-ai-assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Groq API Key

```bash
export GROQ_API_KEY="your_api_key"
```

### Start MCP Server

```bash
python mcp_server.py
```

### Run AI Agent

```bash
python agent.py
```

### Run FastAPI

```bash
uvicorn app:app --reload
```

---

## Example Queries

* What is my savings rate?
* What category do I spend the most on?
* What is my largest expense?
* Forecast my next month's spending.
* Give me financial insights.
* Am I overspending?
* What percentage of my expenses are food-related?
* Show unusual transactions.

---

## Sample Interaction

User:

```text
What is my savings rate?
```

Agent:

```text
Your savings rate is 87.3%.
```

The LLM automatically selects and invokes the appropriate MCP tool without relying on hardcoded query routing.

---

## Key Engineering Decisions

* Replaced rule-based query routing with agent-driven tool selection.
* Exposed financial analytics capabilities through an MCP server.
* Enabled dynamic tool discovery using MCP clients.
* Implemented modular tool architecture for extensibility.
* Added financial intelligence features such as forecasting and budget health assessment.

---

## Future Improvements

* Memory-enabled financial conversations
* Real bank transaction integrations
* Personalized budgeting recommendations
* Vector database for financial history retrieval
* Multi-user support
* Dashboard UI
* Advanced forecasting models

---

## Resume Highlights

* Built an MCP-enabled Financial AI Assistant using FastAPI, LangGraph, Groq Llama 3.3, and Model Context Protocol.
* Developed and exposed 14 financial intelligence tools through a custom MCP server.
* Implemented autonomous tool discovery and execution using agentic AI workflows.
* Replaced rule-based query routing with LLM-driven reasoning and tool orchestration.

---

## Author

Kavana Padaki
