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
        self.end = False
        self.status = False
        

    def update(self):
        self.dist = self.player['miles'] - self.natives

        if self.dist <= 0 or self.player['thirst'] > 6 or self.player['miles'] >= 200 or self.player['tired'] > 8:
            self.end = True

        if self.player['thirst'] > 4 or self.player['tired'] > 5 or self.dist <= 15:
            self.status = True
        else:
            self.status = False


    def oasis_r(self, r0):
        if r0 == 20:
            self.canteen = 3   
            self.status = False
            
            for i in self.player:
                if i != "miles":
                    self.player[i] = 0

            return True


    def cont(self, txt, over):
        if over:
            return f'{txt['screen'][1]}' 
        else:
            return f'{txt['screen'][0]}' 


    def check(self, txt):
        if self.end:
            if self.player['miles'] >= 200:  
                print(txt['win'])

            elif self.dist <= 0:
                print(txt['dist'][1])

            elif self.player['tired'] > 8:
                print(txt['tired'][1])

            elif self.player['thirst'] > 6:
                print(txt['thirst'][1])

            return True
        
        else:
            if self.player['thirst'] > 4:
                print(txt['thirst'][0])

            if self.player['tired'] > 5:
                print(txt['tired'][0])

            if self.dist <= 15:
                print(txt['dist'][0])

            return False


    def a(self):
        if self.canteen > 0:
            self.canteen -= 1
            self.player['thirst'] = 0

            return f'drinks left: {self.canteen}'
        else:
            return 'no drinks left'


    def b(self, r0, r1, oasis):
        self.player['miles'] += r0
        self.player['thirst'] += 1
        self.player['tired'] += 1
        self.natives += r1
        o = self.oasis_r(oasis)
        if o:
            return f'you traveled {r0} miles. \nYou found an oasis!'
        else:
            return f'you traveled {r0} miles.'
        
    
    def c(self, r0, r1, r2, oasis):
        self.player['miles'] += r0
        self.player['thirst'] += 1
        self.player['tired'] += r2
        self.natives += r1
        o = self.oasis_r(oasis)
        if o:
            return f'you traveled {r0} miles. \nYou found an oasis!'
        else:
            return f'you traveled {r0} miles.'
    

    def d(self, r0):
        self.player['tired'] = 0
        self.natives += r0

        return 'The camel is happy (rest)'


    def e(self):

        # return f'{self.player}\n {self.natives}\n {self.dist}\nMiles traveled:  {self.player['miles']}\nDrinks in canteen:  {self.canteen}\nThe natives are {self.dist} miles behind you.'

        return f'Miles traveled:  {self.player['miles']}\nDrinks in canteen:  {self.canteen}\nThe natives are {self.dist} miles behind you.'
    
