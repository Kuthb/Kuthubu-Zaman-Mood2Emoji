import streamlit as st
from textblob import TextBlob

# --- App setup ---
st.set_page_config(page_title="Mood2Emoji", page_icon="😀")

st.title("🎭 Mood2Emoji — Kid-Safe Text Mood Detector")
st.write("Type a short sentence, and I’ll show you the mood as an emoji!")

# --- Core logic ---
BAD_WORDS = ["stupid", "hate", "kill", "dumb"]

def detect_mood(text):
    text_lower = text.lower()
    if any(bad in text_lower for bad in BAD_WORDS):
        return "😐", "Let's keep our language kind and respectful!"

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "😀", "Sounds happy!"
    elif polarity < -0.2:
        return "😞", "Seems a bit sad."
    else:
        return "😐", "That's quite neutral."

# --- Input + Output ---
user_input = st.text_input("Enter your sentence:")

if st.button("Detect Mood"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence!")
    else:
        emoji, explanation = detect_mood(user_input)
        st.markdown(f"### {emoji} {explanation}")

# --- Teacher Mode ---
if st.checkbox("👩‍🏫 Show Teacher Mode"):
    st.subheader("📘 How This App Works")
    st.markdown("""
    **Step 1:** You type a sentence.  
    **Step 2:** The app checks for any bad or unsafe words.  
    **Step 3:** It measures positivity or negativity using *TextBlob*.  
    **Step 4:** It shows an emoji and message.  
    """)
