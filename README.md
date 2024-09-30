# PulgaB0T - A Chatbot Built with Django

- PulgaB0T is a simple chatbot application built using Django. The chatbot receives user input, processes it using a natural language model, and provides an appropriate response. Additionally, it has a feature to store and display all the user messages.
---

https://github.com/user-attachments/assets/5d7f3f16-b4ee-4061-bc4e-063866fa1b63

---
## Features

  1. **User Interaction:** Accepts user inputs and generates responses.
  2. **Message Logging:** Stores each user message along with the response and time sent in the database.
  3. **Message History:** Displays the history of messages exchanged with PulgaB0T.
  4. **API Endpoint:** Exposes an API to retrieve the messages in JSON format.

## File Structure
Main Files:

    views.py:
        Defines the main logic of the chatbot, including user interaction and response handling.

    natural_lang_model/pulga.py:
        Contains the function chatbot_init() that initializes the chatbot, which processes the user input and provides a response.

    models.py:
        Defines the Message model, which is used to store user inputs, responses, and the timestamp.

    serializers.py:
        Contains the MessageSerializer class, which is used for converting the Message model to JSON format for the API endpoint.

Key Functions:

    home(request):
        Handles the main logic of the chatbot interaction.
        Accepts user input from the form, processes it, and stores the messages.
        Renders the home.html template with the response from PulgaB0T and the user's message.

    messages(request):
        Displays all the messages exchanged with the chatbot.
        Renders the messages.html template.

    messages_api(request):
        Provides a REST API endpoint to get all the messages in JSON format.
        Uses MessageSerializer to serialize the data.
