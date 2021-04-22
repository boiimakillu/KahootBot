from kahoot import client as kahootapi
# import itertools
# import random

# bot = client()
# print("What is pin?")
# pin = input()
# print("enter bot amount")
# N = input()
# N = int(N)
def settings():
    print("\nPlease enter the pin followed by the amount of bots you would like:")
    pin = input('Pin:    ')
    amount = input('Amount:    ')
    print("\nWould you like random bot names, or to choose your own? (defaults to random)")
    botnametype = input('Y/n\n')
    if (botnametype == 'n' or botnametype == 'N' or botnametype == 'no' or botnametype == 'No' or botnametype == 'NO'):
        # Do our own random names,
    else:
        # Ask for name(s)
# print('random bot name? y/n')
# rng_usr = input()
# if rng_usr == 'y':
#     usrname = 'shit'
# elif rng_usr == 'n':
#     print("Enter bot name")
#     usrname = input()
# elif rng_usr == 'N':
#     print('Enter bot name')
#     usrname = input()
# elif rng_usr == 'Y':
#     usrname = 'shit'

for _ in itertools.repeat(None, N):
    n = random.randint(0, 10000)
    bot.join(pin, '{} {}'.format(usrname, n))
    def joinHandle():
     pass
    bot.on("joined",joinHandle,print("Bot connected"))