# -*- coding: utf-8 -*-
import streamlit as st
import time
from chatbot import SimpleChatbot
import random
from datetime import datetime

# Page config
st.set_page_config(
    page_title=" Chat Assistant",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern chat interface
st.markdown("""
    <style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Chat container */
    .chat-container {
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        max-height: 600px;
        overflow-y: auto;
    }
    
    /* Message bubbles */
    .message {
        display: flex;
        margin-bottom: 1rem;
        align-items: flex-start;
        animation: fadeIn 0.3s ease-in-out;
    }
    
    .message.user {
        flex-direction: row-reverse;
    }
    
    .message-content {
        max-width: 70%;
        padding: 0.8rem 1rem;
        border-radius: 15px;
        margin: 0 0.5rem;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    .user .message-content {
        background-color: #007AFF;
        color: white;
        border-bottom-right-radius: 5px;
    }
    
    .bot .message-content {
        background-color: white;
        color: #1f1f1f;
        border-bottom-left-radius: 5px;
    }
    
    /* Avatar */
    .avatar {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.2rem;
        flex-shrink: 0;
    }
    
    .user .avatar {
        background-color: #007AFF;
        color: white;
    }
    
    .bot .avatar {
        background-color: #10B981;
        color: white;
    }
    
    /* Timestamp */
    .timestamp {
        font-size: 0.7rem;
        color: #666;
        margin-top: 0.2rem;
        text-align: right;
    }
    
    /* Typing indicator */
    .typing-indicator {
        display: flex;
        align-items: center;
        margin: 1rem 0;
        animation: fadeIn 0.3s ease-in-out;
    }
    
    .typing-indicator .avatar {
        margin-right: 0.5rem;
    }
    
    .typing-dots {
        display: flex;
        align-items: center;
        background-color: white;
        padding: 0.8rem 1rem;
        border-radius: 15px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    .typing-dots span {
        width: 8px;
        height: 8px;
        margin: 0 2px;
        background-color: #666;
        border-radius: 50%;
        animation: typing 1s infinite ease-in-out;
    }
    
    .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
    .typing-dots span:nth-child(3) { animation-delay: 0.4s; }
    
    @keyframes typing {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Input area */
    .stTextInput>div>div>input {
        border-radius: 20px;
        padding: 0.5rem 1rem;
        border: 1px solid #ddd;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    .stButton>button {
        border-radius: 20px;
        padding: 0.5rem 1.5rem;
        background-color: #007AFF;
        color: white;
        border: none;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }
    
    .stButton>button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    .sidebar-content {
        padding: 1rem;
    }
    
    .sidebar-title {
        color: #007bff;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .sidebar-text {
        color: #6c757d;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Welcome message specific styling */
    .welcome-message {
        text-align: center;
        padding: 1rem;
        margin-bottom: 1rem;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    .welcome-message .message-content {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        color: #495057;
        font-size: 1.1rem;
        line-height: 1.5;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chatbot" not in st.session_state:
    st.session_state.chatbot = SimpleChatbot()
if "show_typing" not in st.session_state:
    st.session_state.show_typing = False
if "last_input" not in st.session_state:
    st.session_state.last_input = None
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

def add_message(role, content):
    """Add a message to the chat history"""
    timestamp = time.strftime("%H:%M")
    st.session_state.messages.append({
        "role": role,
        "content": content,
        "timestamp": timestamp
    })

def display_message(role, content, timestamp):
    """Display a single message with proper styling"""
    if role == "user":
        st.markdown(f"""
            <div class="message user">
                <div class="avatar">U</div>
                <div class="message-content">
                    {content}
                    <div class="timestamp">{timestamp}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="message bot">
                <div class="avatar">AI</div>
                <div class="message-content">
                    {content}
                    <div class="timestamp">{timestamp}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

def display_messages():
    """Display all messages in the chat"""
    with st.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        # Display welcome message if no messages
        if not st.session_state.messages:
            st.markdown("""
            <div class="welcome-message">
                <div class="message-content">
                    👋 Hi! I'm your AI assistant. I'm here to chat, answer questions, and maybe tell a joke or two! How can I help you today?
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Display chat messages
        for message in st.session_state.messages:
            display_message(message["role"], message["content"], message["timestamp"])
        
        # Show typing indicator if active
        if st.session_state.show_typing:
            st.markdown("""
            <div class="typing-indicator">
                <div class="avatar">AI</div>
                <div class="typing-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">💬 Chat Assistant</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="sidebar-text">
        I'm your friendly chat assistant! I can:
        <br><br>
        • Chat and have conversations<br>
        • Answer your questions<br>
        • Tell you jokes<br>
        • Share the current time<br>
        • Tell you the date<br>
        • And more!<br>
        <br>
        Try saying:<br>
        • "Hello" or "Hi"<br>
        • "What's your name?"<br>
        • "What can you do?"<br>
        • "Tell me a joke"<br>
        • "What time is it?"<br>
        • "What's today's date?"
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Main chat interface
st.markdown('<div style="text-align: center; margin-bottom: 2rem;"><h1>💬 Chat with Assistant</h1></div>', unsafe_allow_html=True)

# Display chat messages
display_messages()

# Input area
col1, col2 = st.columns([6, 1])

with col1:
    user_input = st.text_input(
        "Type your message here...",
        key=f"user_input_{st.session_state.input_key}",
        disabled=st.session_state.show_typing,
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send", disabled=st.session_state.show_typing or not user_input.strip())

# Clear chat button
if st.button("Clear Chat", type="secondary", disabled=st.session_state.show_typing):
    st.session_state.messages = []
    st.session_state.last_input = None
    st.rerun()

# Handle user input
if (send_button or (user_input and user_input.strip())) and not st.session_state.show_typing:
    current_input = user_input.strip()
    
    # Only process if this is a new input
    if current_input != st.session_state.last_input:
        st.session_state.last_input = current_input
        
        # Add user message
        add_message("user", current_input)
        
        # Show typing indicator
        st.session_state.show_typing = True
        
        # Increment input key to clear the input
        st.session_state.input_key += 1
        
        st.rerun()

def get_bot_response(user_input):
    """Get bot response with enhanced date/time handling"""
    # Convert input to lowercase for easier matching
    input_lower = user_input.lower()
    
    # Handle date/time queries
    if any(phrase in input_lower for phrase in ["what's the date", "what is the date", "today's date", "current date"]):
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}"
    
    elif any(phrase in input_lower for phrase in ["what time", "current time", "time now"]):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    
    # Get response from the chatbot for other queries
    return st.session_state.chatbot.get_response(user_input)

# Process bot response if we're in typing state
if st.session_state.show_typing:
    # Simulate typing delay
    time.sleep(random.uniform(0.5, 1.5))
    
    # Get bot response with enhanced handling
    response = get_bot_response(st.session_state.last_input)
    
    # Add bot response
    add_message("bot", response)
    
    # Reset typing state
    st.session_state.show_typing = False
    st.rerun() 