def get_response(user_input):
    # Convert the user input to lowercase and strip whitespace
    user_input = user_input.strip().lower()

    # Predefined rules and responses
    rules = {
        "who are you": "I am a rule-based chatbot.",
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm excited to help you.",
        "goodbye": "Goodbye! Have a great day.",
        "bye": "Goodbye! Have a great day.",
        "i want to speak to a human": "Sure, connecting you to a human representative. Please wait a moment.",
        "human": "Sure, connecting you to a human representative. Please wait a moment."
    }

    # Match user input with the predefined rules
    for rule, response in rules.items():
        if rule in user_input:
            return response

    # Default response for unrecognized queries
    return "I'm sorry, I don't understand that. Please contact 1800-180XX for further assistance."

# Main loop
def main():
    while True:
        user_input = input("You: ")

        # Exit condition: Stop the conversation if the user inputs 'goodbye' or 'bye'
        if user_input.strip().lower() in ["goodbye", "bye"]:
            print("Bot: Goodbye! Have a great day.")
            break

        response = get_response(user_input)
        print("Bot:", response)

# Start the chatbot
main()
