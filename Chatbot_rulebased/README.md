# Chat Assistant

A modern, interactive chat application built with Python and Streamlit. This chatbot provides a clean, user-friendly interface with features like typing indicators, message bubbles, and natural conversation flow.

## Features

- 💬 Modern chat interface with message bubbles
- ⌨️ Real-time typing indicators
- 🕒 Date and time queries support
- 👤 User and bot avatars
- ⏰ Message timestamps
- 🎨 Clean, responsive design
- 🔄 Natural conversation flow
- 🎯 Smart response handling

## Requirements

- Python 3.8 or higher
- Streamlit
- Required Python packages (install using `pip install -r requirements.txt`):
  - streamlit
  - datetime

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd chatbotwithifelse
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run chatbot_streamlit.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Start chatting! You can try:
   - Saying "hello" or "hi"
   - Asking "what is your name?"
   - Asking "what can you do?"
   - Asking "what time is it?"
   - Asking "what is the date?"
   - Asking for a joke

## Project Structure

- `chatbot_streamlit.py` - Main Streamlit application with the chat interface
- `chatbot.py` - Core chatbot logic and response handling
- `README.md` - Project documentation

## Features in Detail

### Chat Interface
- Clean, modern design with message bubbles
- User messages appear on the right (blue)
- Bot messages appear on the left (white)
- Each message includes a timestamp
- Typing indicator shows when the bot is "thinking"

### Smart Responses
- Handles basic greetings and conversations
- Provides current date and time
- Responds to questions about capabilities
- Tells jokes
- Maintains conversation context

### User Experience
- Input field clears after sending messages
- Send button is disabled while processing
- Clear chat button to start fresh
- Responsive design works on all screen sizes
- Smooth animations for messages and typing indicator

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. 