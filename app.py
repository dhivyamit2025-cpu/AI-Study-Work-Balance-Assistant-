
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="AI Study-Work Balance Assistant",
    page_icon="📚"
)

st.title("📚 AI Study-Work Balance Assistant")
st.write("Balance your studies, internships, projects and personal life.")

st.header("📝 Add Your Tasks")

task = st.text_input("Enter your task")
category = st.selectbox(
    "Category",
    ["Studies", "Internship", "Project", "Personal"]
)
deadline = st.date_input("Deadline", value=date.today())
priority = st.selectbox("Priority", ["High", "Medium", "Low"])

if st.button("Add Task"):
    if task.strip():
        st.success(f"Task added: {task}")
        st.write("Category:", category)
        st.write("Deadline:", deadline)
        st.write("Priority:", priority)
    else:
        st.warning("Please enter a task.")

st.header("💡 Daily Productivity")
rating = st.slider("Rate your productivity", 1, 10, 5)
st.write(f"Your productivity rating: {rating}/10")

st.header("📅 Weekly Planning")
st.write("Plan your tasks, set priorities, and manage your time wisely.")
