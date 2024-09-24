class Game:
    def __init__(self):
        self.player = {
            "thirst": 0,
            "miles": 0,
            "tired": 0,
        }
        
        self.natives = -20
        self.dist = 20
        self.canteen = 3
        self.oasis = None
        

    def actual_d(self):
        self.dist = self.player['miles'] - self.natives


    def oasis_r(self, r0):

        # print(r0)

        if r0 == 20:
            self.canteen = 3   
            for i in self.player:
                if i != "miles":
                    self.player[i] = 0

            print('You found an oasis!')


    def check(self, txt):
        if self.dist <= 0 or self.player['thirst'] > 6 or self.player['miles'] >= 200 or self.player['tired'] > 8:
            if self.player['miles'] >= 200:  
                print(txt['win'])

            elif self.dist <= 0:
                print(txt['dist'][1])

            elif self.player['tired'] > 8:
                print(txt['tired'][1])

            elif self.player['thirst'] > 6:
                print(txt['thirst'][1])

            input(txt['screen'][1])
            return True
        
        else:
            if self.player['thirst'] > 4:
                print(txt['thirst'][0])

            if self.player['tired'] > 5:
                print(txt['tired'][0])

            if self.dist < 15:
                print(txt['dist'][0])

            self.oasis = None
            input(txt['screen'][0])
            return False


    def a(self):
        if self.canteen > 0:
            self.canteen -= 1
            self.player['thirst'] = 0

            print(f'drinks left: {self.canteen}')
        else:
            print('no drinks left')


    def b(self, r0, r1):
        self.player['miles'] += r0
        self.player['thirst'] += 1
        self.player['tired'] += 1
        self.natives += r1
        self.oasis = True

        print(f'you traveled {r0} miles.')
        
    
    def c(self, r0, r1, r2):
        self.player['miles'] += r0
        self.player['thirst'] += 1
        self.player['tired'] += r2
        self.natives += r1
        self.oasis = True

        print(f'you traveled {r0} miles.')  
    

    def d(self, r0):
        self.player['tired'] = 0
        self.natives += r0

        print('The camel is happy (rest)')


    def e(self):

        # print(f'{self.player}\n {self.natives}\n {self.dist}')
        
        print(f'Miles traveled:  {self.player['miles']}\nDrinks in canteen:  {self.canteen}\nThe natives are {self.dist} miles behind you.')
    
