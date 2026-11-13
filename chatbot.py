def chatbot():
    print("hi! welcome to my chatbot")
    print("Type 'bye' to exit from the chatbot")
    
    while True:
        user = input("Ask chatbot:").lower()
        
        if user == "hello":
            print("Hi !")
        elif user == "how are you":
            print("I'm fine, thanks !")
        elif user == "bye":
            print("Goodbye !")
            break
        else:
            print("sorry , can you please try again.")
chatbot()