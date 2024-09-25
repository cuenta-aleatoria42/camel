import random
import os
from camel_c import Game
from text import intro, menu, choice, txt


def main():
    done = False
    print(intro)


    while not done:
        r = random.randint
        oasis = (r(1, 20))
        ans = None

        while True:
            print(f'{menu}\n')
            ask = input(choice)
                
            if ask.upper() == "Q":
                break

            elif ask.upper() == "A":
                ans = game.a()

            elif ask.upper() == "B":
                ans = game.b(r(5, 12), r(7, 14), oasis)

            elif ask.upper() == "C":
                ans = game.c(r(10, 20), r(7, 14), r(1, 3), oasis)

            elif ask.upper() == "D":
                ans = game.d(r(7, 14))
                
            elif ask.upper() == "E":
                ans = game.e()

            else:
                os.system('clear')
                continue

            if ans:
                break


        game.update()

        os.system('clear')

        if ans:
            print(ans)
            input(game.cont(txt, False))
        else:
            break
    

        os.system('clear')

        done = game.check(txt)
        if game.status:
            input(game.cont(txt, done))
            
        os.system('clear')
        

game = Game()
main()

