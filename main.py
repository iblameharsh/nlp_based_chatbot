import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db
st.title("E-commerce chatbot 📩")
btn = st.button("Create knowledge")
if btn:
    create_vector_db()
question =st.text_input("Question:")
if question:
    chain = get_qa_chain()
    answer = chain(question)

    st.header("Answer")
    st.write(answer["result"])