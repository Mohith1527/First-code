import random
import time
import pygame


u_w = 0
c_w = 0
opt = ['rock', 'paper', 'scissors']
unwanted = ['rock', 'paper', 'scissors', 'q']
comments_p = ['Nice', 'Great', 'GoooOOOooody']
comments_n = ["That's Unfortunate", 'Better luck next time', 'You lose dude!']
com_P = random.randint(0, 2)
com_N = random.randint(0, 2)
Com_P = comments_p[com_P]
Com_N = comments_n[com_N]

while True:
    u_i = input('Type Rock/paper/scissors or q to quit:')
    if u_i.lower() == 'q':
        break
    if u_i.lower() == opt:
        continue

    ran_num = random.randint(0, 2)
    c_p = opt[ran_num]
    print('THE COMPUTER PICKED ' + str(c_p) + '.')

    if u_i.lower() == 'scissor' and c_p.lower() == 'paper':
        print(Com_P)
        u_w += 1

    elif u_i.lower() == 'rock' and c_p.lower() == 'scissor':
        print(Com_P)
        u_w += 1

    elif u_i.lower() == 'paper' and c_p.lower() == 'rock':
        print(Com_P)
        u_w += 1

    elif u_i.lower() == c_p.lower():
        print("That's a new one"
              or 'What a wavelength')

    elif u_i.lower() not in unwanted:
        print("[_'-'_'-'_I.N.V.A.L.I.D_'-'_'-'_]")

    else:
        print(Com_N)
        c_w += 1

print('The user gets ' + str(u_w) + ' points')
print('The program gets ' + str(c_w) + ' points')
time.sleep(0.5)
print('You are welcome again')