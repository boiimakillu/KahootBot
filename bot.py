from kahoot import client
import itertools
import random

bot = client()
print("What is pin?")
pin = input()
print("enter bot amount")
N = input()
N = int(N)

print('random bot name? y/n')
rng_usr = input()
if rng_usr == 'y':
    usrname = 'shit'
elif rng_usr == 'n':
    print("Enter bot name")
    usrname = input()
elif rng_usr == 'N':
    print('Enter bot name')
    usrname = input()
elif rng_usr == 'Y':
    usrname = 'shit'

for _ in itertools.repeat(None, N):
    n = random.randint(0, 10000)
    bot.join(pin, '{} {}'.format(usrname, n))
    def joinHandle():
     pass
    bot.on("joined",joinHandle,print("Bot connected"))
