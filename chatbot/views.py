from django.shortcuts import render
from .natural_lang_model.pulga import chatbot_init


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

    context = {
      'pulga_response': response,
      'user': user_input
    }
  return render(request, 'chatbot/home.html', context)