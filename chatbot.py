import random

#predefined rule
rules = {
    "who are you": "I am a rule-based chatbot.",
    "hello": "Hello! How can I assist you today?",
    "how are you":"Iam excited to help you",
    "goodbye": "Goodbye! Have a great day.",
    "default": "I'm sorry, I don't understand that."
}
def get_response(user_input):
    #conversion of user input to lowercase
    user_input = user_input.lower()
    for rule, response in rules.items():
        if rule in user_input:
            return response
    #default response
    return rules["default"]
#main
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)
