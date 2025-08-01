import gradio as gr
import speech_recognition as sr
from datetime import datetime
import os
import shutil
import requests
from dotenv import load_dotenv

load_dotenv()

# Create recordings folder if not exists
os.makedirs("recordings", exist_ok=True)

def transcribe_audio(audio_path):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recordings/audio_{timestamp}.wav"
        textfile = f"transcripts/transcript_{timestamp}.txt"

        shutil.copy(audio_path, filename)

        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)

        # Save transcription to a file
        os.makedirs("transcripts", exist_ok=True)
        with open(textfile, "w", encoding="utf-8") as f:
            f.write(text)

        return text
    except Exception as e:
        return f"Speech recognition failed: {e}"
# Gradio UI
demo = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Voice Assistant",
    description="Speak or upload audio, and get transcription."
)

if __name__ == "__main__":
    demo.launch()
