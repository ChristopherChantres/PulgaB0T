from django.shortcuts import render
from .natural_lang_model.pulga import chatbot_init
from .models import Message
from django.utils import timezone


def home(request):
  context = dict()

  if request.method == 'POST':
    # ------------ NLTK Model ------------#
    chatbot = chatbot_init()
    user_input = request.POST['user_field_input']
    response = chatbot.respond(user_input)

    if response == None:
      response = ''
    #--------------------------------#

    # Calling the Model
    time_sent = timezone.now()
    message = Message(message=user_input, sent_at=time_sent)
    message.save()

    all_messages = Message.objects.all()

    context = {
      'pulga_response': response,
      'user': user_input,
      'all_messages': all_messages,
    }
  return render(request, 'chatbot/home.html', context)