import tkinter as tk
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect, LangDetectException
import threading
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Mapping source and target languages to the correct Hugging Face model identifiers
LANGUAGE_PAIRS = {
    ("en", "ig"): "Helsinki-NLP/opus-mt-en-ig",
    ("ig", "en"): "Helsinki-NLP/opus-mt-ig-en",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
    ("de", "en"): "Helsinki-NLP/opus-mt-de-en",
    # Add more language pairs as needed
}

# Function to perform the translation
def perform_translation(text, src_lang, tgt_lang):
    model_name = LANGUAGE_PAIRS.get((src_lang, tgt_lang))
    if not model_name:
        return "Translation model not available for this language pair."
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translated_tokens = model.generate(**tokens)
    translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translation

# Function to handle the translation process
def translate_text():
    text = entry.get()  # Get input text from entry widget
    output_label.config(text="Processing...")  # Show "processing..." message

    try:
        src_lang = detect(text)  # Detect source language
    except LangDetectException:
        output_label.config(text="Could not detect language. Please enter more text.")
        return

    tgt_lang = tgt_lang_var.get()  # Get target language from dropdown menu

    # Run the translation in a separate thread to avoid blocking the UI
    def run_translation():
        translation = perform_translation(text, src_lang, tgt_lang)
        output_label.config(text=f"Translation: {translation}")
        # Speak the translation
        tts_engine.say(translation)
        tts_engine.runAndWait()

    threading.Thread(target=run_translation).start()

# Function to handle speech input
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_label.config(text="Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        entry.delete(0, tk.END)
        entry.insert(0, text)
    except sr.UnknownValueError:
        output_label.config(text="Sorry, I could not understand the audio.")
    except sr.RequestError:
        output_label.config(text="Could not request results; check your network connection.")

# Create Tkinter application window
root = tk.Tk()
root.title("Simple Translation System")
root.geometry("600x400")  # Set window size to 600x400 pixels

# Welcome message
welcome_label = tk.Label(root, text="Welcome to my Simple Translation System", font=("Helvetica", 16))
welcome_label.pack(pady=10)

# Input label and entry widget
input_label = tk.Label(root, text="Enter text to translate:")
input_label.pack()
entry = tk.Entry(root, width=60)
entry.pack()

# Target language dropdown menu
tgt_lang_label = tk.Label(root, text="Translate to:")
tgt_lang_label.pack()
tgt_lang_var = tk.StringVar(root)
tgt_lang_var.set("en")  # Default target language is English
# Adding more language options: Spanish (es), French (fr), German (de)
tgt_lang_menu = tk.OptionMenu(root, tgt_lang_var, "en", "ig", "es", "fr", "de")
tgt_lang_menu.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Feedback widget
feedback_label = tk.Label(root, text="Feedback:")
feedback_label.pack()
feedback_entry = tk.Entry(root, width=60)
feedback_entry.pack()

# Speech input button
speech_button = tk.Button(root, text="Speak", command=speech_to_text)
speech_button.pack(pady=10)

# Output label
output_label = tk.Label(root, text="", wraplength=500)
output_label.pack(pady=10)

# Run Tkinter event loop
root.mainloop()
