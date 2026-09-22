import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .answer-box {
        padding: 18px;
        border-radius: 10px;
        border: 1px solid #cccccc;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="main-title">🤖 AI FAQ Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask frequently asked questions and get instant answers.</div>',
    unsafe_allow_html=True
)

# FAQ database
faq_data = {
    "what is python":
        "Python is a popular programming language used for web development, data science, artificial intelligence, automation, and many other applications.",

    "what is artificial intelligence":
        "Artificial Intelligence (AI) is a technology that enables computers and machines to perform tasks that normally require human intelligence.",

    "what is machine learning":
        "Machine Learning is a branch of Artificial Intelligence that allows computers to learn patterns from data and make predictions or decisions.",

    "what is data science":
        "Data Science is the process of collecting, analyzing, and interpreting data to discover useful insights and support decision-making.",

    "what is streamlit":
        "Streamlit is a Python framework that allows developers to create interactive web applications quickly and easily.",

    "what is github":
        "GitHub is a platform used to store, manage, collaborate on, and share source code using Git.",

    "what is python used for":
        "Python is used for web development, data analysis, artificial intelligence, machine learning, automation, scientific computing, and software development.",

    "what is ai":
        "AI stands for Artificial Intelligence. It enables machines to perform tasks such as understanding language, recognizing images, and making decisions."
}

# Example questions
st.subheader("💡 Example Questions")

example_questions = [
    "What is Python?",
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Data Science?",
    "What is Streamlit?",
    "What is GitHub?"
]

selected_question = st.selectbox(
    "Choose an example question",
    ["Select a question"] + example_questions
)

# User input
question = st.text_input(
    "💬 Or type your own question",
    placeholder="Example: What is Python?"
)

# Get answer
if st.button("🔍 Get Answer", use_container_width=True):

    if selected_question != "Select a question":
        user_question = selected_question
    else:
        user_question = question

    if not user_question.strip():
        st.warning("⚠️ Please enter or select a question.")

    else:
        cleaned_question = (
            user_question.lower()
            .strip()
            .replace("?", "")
            .replace(".", "")
        )

        answer = None

        # Exact / keyword matching
        for faq_question, faq_answer in faq_data.items():
            if faq_question in cleaned_question:
                answer = faq_answer
                break

        # Additional keyword matching
        if answer is None:

            if "python" in cleaned_question:
                answer = faq_data["what is python"]

            elif "artificial intelligence" in cleaned_question or cleaned_question == "ai":
                answer = faq_data["what is artificial intelligence"]

            elif "machine learning" in cleaned_question:
                answer = faq_data["what is machine learning"]

            elif "data science" in cleaned_question:
                answer = faq_data["what is data science"]

            elif "streamlit" in cleaned_question:
                answer = faq_data["what is streamlit"]

            elif "github" in cleaned_question:
                answer = faq_data["what is github"]

        # Display result
        if answer:
            st.success("✅ Answer found!")

            st.subheader("💡 Answer")

            st.markdown(
                f'<div class="answer-box">{answer}</div>',
                unsafe_allow_html=True
            )

        else:
            st.info(
                "🤔 Sorry, I don't have an answer for that question. "
                "Please try one of the example questions."
            )

# Footer
st.divider()

st.caption(
    "🤖 CodeAlpha Artificial Intelligence Internship | FAQ Chatbot"
)