Speech Recognition with Gradio

This project is a simple voice transcription app built using Python, Gradio, and the `SpeechRecognition` library.
It records audio using a microphone or accepts uploaded audio files and then transcribes the speech into text using Google’s Speech-to-Text API (via the `recognize_google()` function).


## Features

-  Record audio using microphone (browser-based via Gradio UI)
-  Accept uploaded audio files (.wav)
-  Transcribes speech to text using Google Web Speech API
-  Saves all recordings in a `recordings/` directory
-  Clean and simple web interface built with Gradio


## Requirements

Make sure you have  latest vesion of Python installed ( I have installed python 3.12).

Install dependencies using:

pip install -r requirements.txt



## Future steps
Next steps: give this transcribed text as input to pretrained open source  LLM  and get the generated output text(professionl summary  in my case).


Convert this text to speech as output.
