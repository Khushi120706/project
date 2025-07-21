def chatbot():
    responses = {
        "hello": "hi!",
        "how are you": "i am fine, thanks!",
        "bye": "Goodby!"
    }
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()