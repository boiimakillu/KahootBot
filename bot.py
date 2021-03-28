#imports
from kahoot import client
import itertools
import random

#labeling bot as client
bot = client()

#asks for pin
print("What is pin?")
pin = input()
#asks for bot amount
print("enter bot amount")
N = input()
N = int(N)
#testing name inputs

print("enter bot name")
usrname = input() 

#ForLoop for entered information
for _ in itertools.repeat(None, N):
    n = random.randint(0, 1000000000000)
    bot.join(pin, '{} {}'.format(usrname, n))
    def joinHandle():
     pass
    bot.on("joined",joinHandle,print("Bot connected"))