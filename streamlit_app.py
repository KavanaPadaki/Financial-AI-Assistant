import asyncio
import streamlit as st

from agent import ask

st.set_page_config(
    page_title="Financial AI Assistant",
    page_icon="💰",
)

st.title("💰 Financial AI Assistant")

st.write("Ask questions about your spending, income, savings, anomalies and financial insights.")

query = st.text_input(
    "Ask a question",
    placeholder="Example: What was my total spending this month?",
)

if st.button("Submit"):

    if not query.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            try:

                answer = asyncio.run(ask(query))

                st.success("Answer")

                st.write(answer)

            except Exception as e:

                st.error(str(e))
