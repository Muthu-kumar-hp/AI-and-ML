import streamlit as st
import speech_recognition as sr
import pyttsx3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ----------- Model Training (same data) -----------
texts = [
    'Win money now',
    'Limited offer just for you',
    'Hi, how are you?',
    'Call me tomorrow',
    'Free tickets available',
    'Congratulations, you won!',
    'Are you coming to the party?',
    "Let's grab lunch today",
    'Earn extra cash fast',
    'Meeting at 10 am'
]
labels = [1, 1, 0, 0, 1, 1, 0, 0, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# ----------- Voice Input Function -----------
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Speech recognition service is unavailable."

# ----------- Text-to-Speech (Female Voice) -----------
def speak_text(message):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(message)
    engine.runAndWait()

# ----------- Streamlit UI -----------
st.set_page_config(page_title="Voice Spam Detector", page_icon="🗣️")
st.title("🗣️ Voice-Based Spam Detector")

if st.button("🎙️ Speak and Classify"):
    with st.spinner("Listening..."):
        spoken_text = get_voice_input()

    st.write("**You said:**", spoken_text)

    if "sorry" in spoken_text.lower():
        st.error(spoken_text)
        speak_text(spoken_text)
    else:
        X_new = vectorizer.transform([spoken_text])
        prediction = model.predict(X_new)[0]
        result = "This sounds like Spam." if prediction == 1 else "This is Not Spam."
        st.success(result)
        speak_text(result)
        st.balloons() 