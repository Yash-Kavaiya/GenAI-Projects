import discord
import os
import json
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models

intents = discord.Intents.default()
intents.message_content = True  # Important to receive message content 
# Initialize the Discord client
client = discord.Client(intents=intents) 

def generate(text):
  vertexai.init(project="ondc-project-cloud", location="asia-southeast1")
  model = GenerativeModel("gemini-1.0-pro-vision-001")
  responses = model.generate_content(
      [text],
      generation_config=generation_config,
      safety_settings=safety_settings,stream=True
  )
  print(model)
  for response in responses:
    print("res-------------",response)
    print(response.text, end="")
    import time
    time.sleep(100)
    return response.text


generation_config = {
    "max_output_tokens": 2048,
    "temperature": 1,
    "top_p": 1,
    "top_k": 32,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# Event triggered when a message is received
@client.event
async def on_message(message):
    print("on_message fn is working")
    # Ignore messages from the bot itself
    print("message",message)
    print("message",type(message))
    print("message.author",type(message.author))
    if message.author == client.user:
        return
    # Get the user's message
    print("message.content",message.content)
    user_message = message.content
    print("User Message-----------------",user_message)
    bot_reply = generate(user_message)
    print("Bot Reply AI:-------- ",bot_reply)
    await message.channel.send(f"{message.author.mention} {bot_reply}")

# Run the bot with your Discord token
client.run("API")
