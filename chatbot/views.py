from django.shortcuts import render
from .natural_lang_model.pulga import chatbot_init


def home(request):
  context = dict()

  if request.method == 'POST':
      # ------------ NLTK Model ------------#
    chatbot = chatbot_init()

    user_input = request.POST['user_field_input']

    #   if user_input.lower() == 'bye':
    #     print('PulgaB0T: Goodbye!')
    #     break
    #   elif user_input.lower() == '--help':
    #     print("""
    # - PulgaB0T is a chatbot that uses nltk in the background
    # - Type for example "Tell me a joke"
    # - Ask for advices "Give me an advice"

    # Remember that PulgaB0T is still in development, go easy with it! ;)
              
    #     """)
    response = chatbot.respond(user_input)

    if response == None:
      response = ''

    #--------------------------------#

    context = {
      'pulga_response': response
    }
  return render(request, 'chatbot/home.html', context)