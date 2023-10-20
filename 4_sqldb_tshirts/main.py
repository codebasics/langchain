import streamlit as st
from langchain_helper import get_qa_chain

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)






