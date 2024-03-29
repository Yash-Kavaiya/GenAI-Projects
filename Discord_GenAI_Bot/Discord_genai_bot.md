# GenAI Discord Bot

Your Discord Bot leverages the power of Vertex AI's generative models to interact with users in Discord servers. It listens to messages and responds with AI-generated content based on the input it receives.

## Features

- Responds to user messages with AI-generated content.
- Customizable AI response settings for content safety and creativity.
- Easy to deploy and run on any server.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Discord account and have created a Discord bot.
- You have a Google Cloud account and have access to Vertex AI services.
- You have Python 3.6+ installed on your machine.

## Installation

To install the necessary dependencies for this bot, follow these steps:

1. Clone the repository to your local machine:


```bash
git clone https://github.com/Yash-Kavaiya/GenAI-Projects
cd GenAI-Projects/Discord_GenAI_Bot
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Set up your Google Cloud project and authenticate with Vertex AI as per the [official documentation](https://cloud.google.com/vertex-ai/docs/start/client-libraries).

2. Create a `.env` file in the root directory of your project and add your Discord bot token and Google Cloud project details:

```plaintext
DISCORD_TOKEN=your_discord_bot_token
GOOGLE_PROJECT_ID=your_google_cloud_project_id
GOOGLE_PROJECT_LOCATION=your_project_location
```

3. Update the `main.py` file with your specific model details if different from the defaults.

## Usage

To start the bot, run the following command in your terminal:

```bash
python main.py
```

The bot will log in to Discord and start listening for messages. When a message is received, it will generate a response using Vertex AI and reply in the same channel.

## Contributing

Contributions to this project are welcome! Here are a few ways you can help:

- Report bugs and request features by creating issues.
- Improve documentation.
- Submit pull requests with bug fixes or new features.


## License

Distribute under the MIT License. See `LICENSE` for more information.
