#A function that prints a list containig a series of short text messages
def show_messages(text_messages):
    """Prints each message in a list"""
    for text_message in text_messages:
        print(text_message)

message = ['Hello', 'Hi', 'Thank you']
show_messages(message)