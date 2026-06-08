import streamlit as st
from openai import OpenAI

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI English Tutor Pro", page_icon="📘", layout="centered")

st.title("📘 Real AI English Tutor (ChatGPT Style)")
st.write("Speak, write, and learn English with real AI feedback.")

# ---------------- API KEY ----------------
api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    # ---------------- MODE SELECT ----------------
    mode = st.selectbox("Choose learning mode", [
        "🧪 Diagnose My English",
        "📚 Vocabulary Teacher",
        "✍️ Grammar Correction",
        "🗣️ Speaking Practice",
        "🔥 Free Chat Tutor"
    ])

    user_input = st.text_area("Write your English here:")

    # ---------------- PROMPTS ----------------
    def get_prompt(mode, text):
        if mode == "🧪 Diagnose My English":
            return f"""
            Analyze this English level:
            - Level (Beginner/Intermediate/Advanced)
            - Mistakes
            - How to improve

            Text: {text}
            """

        elif mode == "📚 Vocabulary Teacher":
            return f"""
            Improve vocabulary in this sentence.
            Give:
            - Better word choices
            - Synonyms
            - Corrected sentence

            Text: {text}
            """

        elif mode == "✍️ Grammar Correction":
            return f"""
            Correct grammar mistakes.
            Explain simply.

            Text: {text}
            """

        elif mode == "🗣️ Speaking Practice":
            return f"""
            Improve spoken English.
            Make it natural and fluent.
            Add better expressions.

            Text: {text}
            """

        else:
            return f"""
            You are a friendly English tutor.
            Have a natural conversation and correct mistakes.

            User: {text}
            """

    # ---------------- BUTTON ----------------
    if st.button("Ask AI Tutor 🤖"):

        if not user_input:
            st.warning("Please write something first.")
        else:
            with st.spinner("AI is thinking..."):

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a professional English tutor."},
                        {"role": "user", "content": get_prompt(mode, user_input)}
                    ]
                )

                result = response.choices[0].message.content
                st.success("AI Response:")
                st.write(result)

else:
    st.info("Enter your OpenAI API key to activate AI tutor.")
