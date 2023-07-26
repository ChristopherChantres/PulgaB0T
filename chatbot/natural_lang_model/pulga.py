from dataset import pairs as dataset
import nltk
from nltk.chat.util import Chat, reflections
import os
import time

def chatbot_init():
  chatbot = Chat(dataset, reflections)
  return chatbot

def main():
  chatbot = chatbot_init()
  os.system('clear')
  print("""
  --- Hello this is PulgaB0T! I am a basic ChatBot ---
  
            To exit type: "bye"

            Development in process...
            All rights reserved to PulgaInc
            If you need help type: "--help"

        """)
  
  while True:
    user_input = str(input('You: '))

    if user_input.lower() == 'bye':
      print('PulgaB0T: Goodbye!')
      time.sleep(1)
      break
    elif user_input.lower() == '--help':
      print("""
- PulgaB0T is a chatbot that uses nltk in the background
  - Type for example "Tell me a joke"
  - Ask for advices "Give me an advice"

Remember that PulgaB0T is still in development, go easy with it! ;)
            
      """)
    time.sleep(3)
    response = chatbot.respond(user_input)

    if response == None:
      response = ''

    print(f'PulgaB0T: {response}')
  

if __name__ == '__main__':
  main()
  