from interaction.speech import *

help_message =  """
Para executar comandos, diga executar seguido do comando desejado.

Exemplo: Diga "executar eita" para mostrar uma mensagem de teste.

Comandos disponíveis:

"eita" ou "piano" para mensagens de teste

"""

def switch(value):
   if value is None:
      speak('Desculpe, não entendi... Pode repetir?')
      return 'comp_error'
   else:
      text = value.lower()
      
      if text == 'ajuda':
         speak(help_message)
         return 'pass'
      elif text == 'eita':
         speak('eita')
         return 'pass'
      elif text == 'piano':      
         speak('another one bites the dust')
         return 'pass'
      elif text == 'encerrar':
         speak('Certo, até mais!')
         return 'exit'
      else:
         return text