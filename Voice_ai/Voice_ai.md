

# Conversation AI Bot Using Gradio

## Overview
This project is a Conversation AI Bot that leverages the power of Gradio, the Hugging Face Transformers library, and Google's Generative AI to transcribe audio input and generate responses. It uses OpenAI's Whisper model for automatic speech recognition and Google's Generative AI for content generation.

## Features
- **Automatic Speech Recognition**: Utilizes the Whisper model to accurately transcribe spoken words into text.
- **Generative AI Responses**: Leverages Google's Generative AI to generate meaningful responses based on the transcribed text.
- **Gradio Interface**: Provides an easy-to-use web interface for real-time interaction with the AI bot.

## Installation

To run this project, you will need Python 3.6 or later. It's recommended to use a virtual environment.

1. Clone the repository:
   ```
   git clone <repository-url>
   
```
2. Navigate to the project directory:
   ```
   cd conversation-ai-bot-gradio
   
```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the Conversation AI Bot, run the following command in your terminal:

```
python app.py
```

After launching, the Gradio interface will be accessible via a URL displayed in your terminal. Speak into your microphone, and the bot will respond with generated text.

## Configuration

Before running the project, ensure you have set your Google API key in the `.env` file:

```python
GOOGLE_API_KEY = "your_google_api_key_here"
```

You can set the `GOOGLE_API_KEY` as an environment variable.

## Contributing

Contributions to the Conversation AI Bot are welcome! Please feel free to submit pull requests or open issues to suggest improvements or add new features.

## License

This project is licensed under the MIT License - see the file for details.

## Acknowledgments

- OpenAI's Whisper model for automatic speech recognition.
- Google's Generative AI for content generation capabilities.
- Gradio for providing an easy way to create web interfaces for Python applications.
