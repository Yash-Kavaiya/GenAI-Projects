import gradio as gr
from transformers import pipeline
import numpy as np
import google.generativeai as genai
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY="API"
# Used to securely store your API key
genai.configure(api_key=GOOGLE_API_KEY)
print(transcriber)
model = genai.GenerativeModel('gemini-pro')
def transcribe(audio):
    sr, y = audio
    print(sr)
    print(y)
    print(type(sr))
    print(type(y))
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))
    res = transcriber({"sampling_rate": sr, "raw": y})["text"]
    response = model.generate_content(res)
    return response.text

demo = gr.Interface(
    transcribe,
    gr.Audio(sources=["microphone"]),
    "text",title="Conversation AI Bot Using Gradio",
     description="This is a Conversation AI Bot that transcribes audio input using Whisper and generates responses using Google's Generative AI. Speak into the microphone, and the bot will respond."
)

demo.launch()
