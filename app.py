import os
import google.generativeai as genai
import streamlit as st

# Giving the app a normal title
st.title("📚 Smart Study AI Tool 📚")
st.write("Welcome to my first AI tool.")

# Setting up the API Key simply
# If it's missing, it just prints a normal message instead of throwing an enterprise error
my_key = os.environ.get("GEMINI_API_KEY")
if not my_key:
    st.warning("First set the GEMINI_API_KEY!")
    st.stop()

# Basic setup for Gemini
genai.configure(api_key=my_key)
ai_model = genai.GenerativeModel("gemini-2.5-flash")

# Sidebar for selecting options
st.sidebar.header("Pick Something 👇")
chosen_feature = st.sidebar.selectbox(
    "What do you want the AI to do?",
    ("Explain a Concept", "Summarize Text", "Generate Quiz Questions"),
)

# Basic chat history setup using session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show the old messages if they exist
for msg in st.session_state.chat_history:
    with st.chat_message(msg["user_or_bot"]):
        st.write(msg["text_content"])

# Chat input bar at the bottom
user_stuff = st.chat_input("Type something here...")

if user_stuff:
    # For empty prompt
    if user_stuff.strip() == "":
        st.error("Input is empty... Type something bro.")
    else:
        # Building the prompts
        if chosen_feature == "Explain a Concept":
            final_prompt = (
                f"Explain this like I'm 5 years old with funny analogies: {user_stuff}"
            )
        elif chosen_feature == "Summarize Text":
            final_prompt = f"Give me a short summary of this text with bullet points: {user_stuff}"
        elif chosen_feature == "Generate Quiz Questions":
            final_prompt = (
                f"Make a quick 3-question MCQ quiz about this: {user_stuff}"
            )

        # 1. Show what the user typed instantly
        with st.chat_message("user"):
            st.write(user_stuff)

        # Save user message to history
        st.session_state.chat_history.append(
            {"user_or_bot": "user", "text_content": user_stuff}
        )

        # 2. Call the AI with a normal loading text
        with st.chat_message("assistant"):
            with st.spinner("AI is cooking..."):
                try:
                    ai_response = ai_model.generate_content(final_prompt)
                    bot_text = ai_response.text

                    # 3. Print out the response
                    st.write(bot_text)

                    # Save bot response to history
                    st.session_state.chat_history.append(
                        {"user_or_bot": "assistant", "text_content": bot_text}
                    )

                except Exception as bug:
                    st.error(f"Something went wrong: {bug}")