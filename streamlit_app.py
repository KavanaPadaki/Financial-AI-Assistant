import streamlit as st
import requests

st.title("💰 Financial AI Assistant")

query = st.text_input("Ask a question about your spending:")

if st.button("Submit") and query:
    try:
        response = requests.get(f"http://localhost:8000/ask?query={query}")
        data = response.json()

        st.subheader("Response")

        if "answer" in data:
            st.write(data["answer"])

        if "message" in data:
            st.write(data["message"])

        if "data" in data:
            st.json(data["data"])

        if "anomalies" in data:
            st.json(data["anomalies"])

        if "insights" in data:
            st.write(data["insights"])

        st.caption(f"Tool used: {data.get('tool_used')}")

    except Exception as e:
        st.error(f"Error: {e}")