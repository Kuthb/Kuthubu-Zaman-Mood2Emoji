🧠 Mood2Emoji — Kid-Safe Text Mood Detector

Mood2Emoji is a fun, kid-friendly web app built with Streamlit and TextBlob that detects the mood of a sentence and expresses it using emojis (😀 😐 😞).
It’s designed for students aged 12–16 to learn how machines understand human language and emotions.

🚀 Features

📝 Takes a short sentence as input.

😀 Returns an emoji + short explanation (e.g., “Sounds happy!”).

🚫 Filters inappropriate or unknown text (safe for kids).

👩‍🏫 Optional “Teacher Mode” explains how the app works using a simple diagram.

💡 Built using Streamlit and TextBlob — no heavy models.

⚙️ Setup & Run Instructions
1️⃣ Clone the repository
git clone https://github.com/Kuthb/kuthubu-zaman-mood2emoji.git
cd kuthubu-zaman-mood2emoji

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py

📘 How Kids Learn from It

Students understand how text sentiment can be analyzed using simple Natural Language Processing (NLP) tools.
They learn:

How computers interpret text as “positive”, “negative”, or “neutral”.

How to connect logic with visuals (text → emoji).

Safe and responsible AI design for age-appropriate apps.

🧑‍🏫 60-Minute Teaching Plan
Time	Activity
0–10 mins	Introduction to text moods & NLP
10–25 mins	Code walkthrough of app.py
25–40 mins	Students test the app with different inputs
40–55 mins	Add a custom emoji or new rule
55–60 mins	Recap & Q&A session
⚠️ Known Limitations

TextBlob works best with short, simple sentences.

Doesn’t detect sarcasm or complex emotions.

Limited vocabulary for bad-word filtering.

📂 Repository Structure
repo/
 ├─ app.py
 ├─ requirements.txt
 ├─ README.md
 └─ lesson_plan.pdf

🧩 Tech Stack

Python 3.9+

Streamlit — UI framework

TextBlob — sentiment detection
