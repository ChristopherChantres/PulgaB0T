from django.shortcuts import render
from .natural_lang_model.pulga import chatbot_init
from .models import Message
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MessageSerializer

"""
Home function that holds the user input and outputs
PulgaB0T response
"""
def home(request):
  context = dict()

  if request.method == 'POST':
    chatbot = chatbot_init()
    user_input = request.POST['user_field_input']
    user_input = user_input.lower()
    response = chatbot.respond(user_input)

    # Setting response a default value if == none
    if response == None:
      response = 'Remember I am still learning :)'

    # Getting the time of the message
    time_sent = timezone.now()

    # Calling the Model
    message = Message(message=user_input, sent_at=time_sent)
    message.save()

    all_messages = Message.objects.all()

    context = {
      'pulga_response': response,
      'user': user_input,
      'all_messages': all_messages,
    }
  return render(request, 'chatbot/home.html', context)


# Function that passes all the messages to be displayed
def messages(request):
  context = dict()

  if request.method == 'GET':
    all_messages = Message.objects.all()
    context = {
      'all_messages': all_messages,
    }
  return render(request, 'chatbot/messages.html', context)


# Functions that serializes the messages to stisfy the API
@api_view(['GET'])
def messages_api(request):
  if request.method == 'GET':
    all_messages = Message.objects.all()
    serializer = MessageSerializer(all_messages, many=True)
  return Response(serializer.data)