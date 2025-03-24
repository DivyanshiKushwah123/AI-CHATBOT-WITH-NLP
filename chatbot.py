import nltk
from nltk.chat.util import Chat, reflections

# Download necessary resources
nltk.download('punkt')

# Define pairs of patterns and responses for rule-based conversations
patterns_responses = [
    (r"hi|hello|hey", ["Hello! How can I help you today?", "Hi! How can I assist you?"]),
    (r"how are you?", ["I'm good, thank you! How about you?", "I'm doing well, thanks for asking!"]),
    (r"what is your name?", ["I am a chatbot created to assist you.", "You can call me ChatBot."]),
    (r"quit", ["Goodbye! Take care.", "Bye! Have a great day."]),
    (r"my name is (.*)", ["Hello, %1! Nice to meet you."]),
    (r"what can you do?", ["I can help you with information, answer questions, and assist you in various tasks."]),
]

# Create the chatbot with patterns and reflections (this helps with basic conversation flow)
def chatbot():
    print("Hello, I am your friendly chatbot! Type 'quit' to end the conversation.")
    
    chatbot = Chat(patterns_responses, reflections)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        
        # Get the chatbot's response based on the user's input
        response = chatbot.respond(user_input)
        
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you try again?")
            
# Start the chatbot
if __name__ == "__main__":
    chatbot()
