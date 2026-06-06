import sys

def get_bot_response(user_input):
    """
    Analyzes user input and returns a predefined response.
    Converts input to lowercase for case-insensitive matching.
    """
    # Clean the input by removing extra spaces and converting to lowercase
    cleaned_input = user_input.strip().lower()
    
    # Check for greeting patterns
    if cleaned_input in ["hello", "hi", "hey"]:
        return "Hi!"
    
    # Check for well-being inquiry patterns
    elif cleaned_input in ["how are you", "how are you?", "how's it going"]:
        return "I'm fine, thanks!"
    
    # Check for goodbye patterns
    elif cleaned_input in ["bye", "goodbye", "exit"]:
        return "Goodbye!"
    
    # Fallback response for unhandled inputs
    else:
        return "I am a simple rule-based chatbot. Try saying 'hello', 'how are you', or 'bye'."

def start_chatbot():
    """
    Main loop to run the chatbot console interface.
    """
    print("--- Rule-Based Chatbot Activated ---")
    print("Type your message below (or type 'bye' to exit):")
    print("-" * 36)
    
    while True:
        try:
            # Capture user input from the console
            user_msg = input("You: ")
            
            # Get the appropriate response from the helper function
            bot_reply = get_bot_response(user_msg)
            
            # Display the chatbot's response
            print(f"Bot: {bot_reply}")
            
            # Terminate the program execution if the user says goodbye
            if bot_reply == "Goodbye!":
                break
                
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            sys.exit(0)

# Entry point execution guard
if __name__ == "__main__":
    start_chatbot()
