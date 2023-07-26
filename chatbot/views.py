from django.shortcuts import render


def home(request):
  context = dict()
  
  if request.method == 'POST':
    user_input = request.POST['user_field_input']

    context = {
      'user_input': user_input
    }
  return render(request, 'chatbot/home.html', context)