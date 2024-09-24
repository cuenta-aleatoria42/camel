import random
import os
from camel_c import Game
from text import intro, menu, choice, txt


def main():
    done = False
    print(intro)
    
    while not done:
        r = random.randint
        print(f'{menu}\n')
        ask = input(choice)
        
        if ask.upper() == "Q":
            break

        elif ask.upper() == "A":
            game.a()

        elif ask.upper() == "B":
            game.b(r(5, 12), r(7, 14))

        elif ask.upper() == "C":
            game.c(r(10, 20), r(7, 14), r(1, 3))

        elif ask.upper() == "D":
            game.d(r(7, 14))
        
        elif ask.upper() == "E":
            game.e()

        else:
            print('Error')


        game.actual_d()

        if game.oasis:
            game.oasis_r(r(1, 20))

        done = game.check(txt)
        os.system('clear')
        
        
game = Game()
main()

