from flask import Flask, render_template, request
import os
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_cover_letter', methods=['POST'])

def generate_cover_letter():
    job_description = request.form['job_description']
    resume_text = request.form['resume_text']
    vertexai.init(project="ondc-project-cloud", location="us-central1")
    model = GenerativeModel("gemini-1.0-pro-001")
    prompt_new= "You Are Expert In Writing IT Professional Cover Letter Above is Job Describation "+job_description + "And Above is My Resume Text "+resume_text +"Write Very Personized Cover Letter Give Output like a I want to show In Website" 
    responses = model.generate_content(prompt_new,generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1},safety_settings={
          generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,},stream=True,)
    print("-------------------------")
    cover_letter=""
    for response in responses:
      print(response.text, end="")
      print("-------------------------")
      cover_letter+=response.text

    return render_template('result.html', cover_letter=cover_letter)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
