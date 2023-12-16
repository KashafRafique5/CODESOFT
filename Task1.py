import re

def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define rules and responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you': 'I am a chatbot. I don\'t have feelings, but thanks for asking!',
        r'wassup': 'I am good! Thanks for asking',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'your name': 'I\'m a botchat, you can call me ChatKASH.',
        r'age': 'I don\'t have an age. I\'m just a computer program.',
        r'help': 'I can provide information or answer questions. Just ask me anything!',

        # Add more rules as needed
    }

    # Check user input against rules
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response

    # If no match is found, provide a default response
    return "I'm sorry, I don't understand that. Can you please ask another question?"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
