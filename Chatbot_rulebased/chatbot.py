import re
import random
from datetime import datetime

class SimpleChatbot:
    def __init__(self):
        # Predefined responses
        self.greetings = {
            'hi': ['Hello!', 'Hi there!', 'Hey! How can I help you?'],
            'hey': ['Hello!', 'Hi there!', 'Hey! How can I help you?'],
            'hello': ['Hello!', 'Hi there!', 'Hey! How can I help you?'],
            'how are you': ['I am doing well, thank you!', 'I am great! How about you?'],
            'bye': ['Goodbye!', 'See you later!', 'Take care!']
        }
        
        # List of jokes
        self.jokes = [
            "Why did the computer go to the doctor? Because it had a virus!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "What did the ocean say to the beach? Nothing, it just waved!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "How does a penguin build its house? Igloos it together!"
        ]
        self.current_joke_index = 0
        
        # Common questions and answers
        self.qa_pairs = {
            
            'what is your name': 'I am ChatBot, a rule-based chatbot!',
            'what can you do': 'I can chat with you, answer basic questions, tell jokes, and respond to greetings!',
            'who created you': 'I was created as a simple rule-based chatbot example!',
            'what time is it': lambda: f'The current time is {datetime.now().strftime("%H:%M:%S")}',
            'what is the date': lambda: f'Today is {datetime.now().strftime("%Y-%m-%d")}'
        }
        
        # Pattern matching for more complex responses
        self.patterns = [
            (r'weather', 'I am sorry, I cannot check the weather yet.'),
            (r'joke', self.get_next_joke),
            (r'another joke', self.get_next_joke),
            (r'more jokes', self.get_next_joke),
            (r'thank', 'You are welcome!'),
            (r'help', 'I can help you with basic conversation. Try asking me about my name, what I can do, or ask for a joke!')
        ]

    def get_next_joke(self):
        # Get the next joke and cycle through the list
        joke = self.jokes[self.current_joke_index]
        self.current_joke_index = (self.current_joke_index + 1) % len(self.jokes)
        return joke + "\n\nWant to hear another one? Just ask for 'another joke'!"

    def get_response(self, user_input):
        # Convert input to lowercase for easier matching
        user_input = user_input.lower().strip()
        
        # Check for greetings
        for greeting in self.greetings:
            if greeting in user_input:
                return random.choice(self.greetings[greeting])
        
        # Check for exact question matches
        for question, answer in self.qa_pairs.items():
            if question in user_input:
                if callable(answer):
                    return answer()
                return answer
        
        # Check for pattern matches
        for pattern, response in self.patterns:
            if re.search(pattern, user_input):
                if callable(response):
                    return response()
                return response
        
        # Default response if no matches found
        return "I'm not sure how to respond to that. Could you try asking something else?"

def main():
    chatbot = SimpleChatbot()
    print("ChatBot: Hello! I am ChatBot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot:", random.choice(chatbot.greetings['bye']))
            break
            
        response = chatbot.get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main() 