# Smart Study AI Tool

Welcome to my submission for Task 1! I built a personalized AI study assistant using Python, Streamlit, and the Google Gemini 2.5 Flash API. It handles everyday student struggles, like understanding topics at 2 AM or creating quick practice quizzes.

## Features Included...
- **Explain a Concept:** Breaks down complex terms into plain English using funny analogies (ELI5 mode).
- **Summarize Text:** Condenses long, painful readings into bite-sized bullet points.
- **Generate Quiz Questions:** Instantly creates a 3-question MCQ checkpoint to test yourself.
- **Generate Flashcards:** Builds clean study flashcards with distinct Front and Back terms.
- **Chat History:** Uses Streamlit session state so your old messages don't disappear into the void every time the app reruns.
- **Web Interface:** Built a clean, dark-mode-compatible web dashboard using Streamlit's structural layout elements.
- **Markdown Rendering:** Formats the AI responses cleanly with bold text, headers, and bullet points.
- **Loading Animation:** Displays a live `"AI is cooking..."` status spinner while waiting for the API to respond.

---

## How to Get it Running Local?
Make sure you have Python installed, then run this command in your terminal to install the dependencies:
```bash
pip install streamlit google-generativeai
