import random

class Score:
    '''Constructor for points class has many attributes
    Points for the score total of the player
    Multiplier for the score multiplier of earning score
    There is a non-specified attribute called upgrades specifying amount of upgrades gaint
    Price for upgrading pickaxe
    Completed indicates if the player has completed the game or not, the player
    will get the completed status if they choose to continue when they reach 1000000 ores
    Double is one of the bonuses the players can get for beating the game
    Double will give a 50% chance to get double the ore when you gain ore
    Lottery is another bonus, it will select 2 random numbers from 1-100
    Every 30 seconds it will occur example if the 2 numbers equal eachother the 
    player will gain 10000 * multiplier payout win is amount required to win
    '''

    def __init__(self, points=0, multiplier=1, price=100, completed=False, double=False, lottery=False, win=1000000):
        self.points = max(points, 0) # max checks to make sure integers being passed are at not negative
        self.multiplier = max(multiplier, 1) # checks to make sure it is at minimum one
        self.upgrades = 1
        self.price = max(price ** multiplier, 1)
        self.completed = completed
        self.double = double
        self.lottery = lottery
        self.win = max(win, 0)
    
    def add_score(self, scores=None):
        '''Adds the total score to score total'''
        # If a score is specified add the score instead
        if scores:
            self.points += scores
            self.points = round(self.points, 1)
        elif scores == 0:
            self.points += 0
        else:        
            calculate = 1 * self.multiplier
            if self.double:
                random_number = random.randint(1, 2)
                if random_number == 2:
                    calculate *= 2
            self.points += calculate

    def subtract_score(self, amount):
        '''Takes an amount and subtracts the score from it'''
        if self.points > amount:
            self.points -= amount
    
    def increase_values(self):
        '''Increases the price, based on formula'''
        increase_multiplier = 1.5 # 50% more increase for price/formula
        self.price = round(self.price * (increase_multiplier ** self.upgrades))
        self.upgrades += 1
    
    def increase_multiplier(self):
        '''Increases score multiplier, through the shop'''
        # if the player has enough points, upgrade the multiplier
        if self.points >= self.price:
            self.subtract_score(self.price)
            self.multiplier *= 2
            self.increase_values()
        else:
            print('Not enough points')
    
    def pull_lottery(self):
        '''This will draw the lottery if the player has a lottery bonus
            The lottery is technically free (only takes your time) and 
            if you lose you don't gain anything
            the lottery occurs every 30 seconds
            there are many payout bonuses to the lottery
            if the two numbers equal eachother get a 10000 * multiplier payout
            if the two numbers are both multiple of 10 get a 1000 * multiplier payout
            if the two numbers are both multiple of 5 get a 100 * multiplier payout
            if the two numbers are both multiple of 3 get a 10 * multiplier payout
            if the two numbers are both mutiipler of 2 gt a 1 * mutiplier payout
            if both payout both'''
        lot_one = random.randint(1,100)
        lot_two = random.randint(1,100)
        payout = 0
        if (lot_one == lot_two):
            payout += 10000 * self.multiplier
        if (lot_one % 10 == 0 and lot_two % 10 == 0):
            payout += 1000 * self.multiplier
        if (lot_one % 5 == 0 and lot_two % 5 == 0):
            payout += 100 * self.multiplier
        if (lot_one % 3 == 0 and lot_two % 3 ==0):
            payout += 10 * self.multiplier
        if (lot_one % 2 == 0 and lot_two % 2 == 0):
            payout += 1 * self.multiplier
        if payout == 0:
            self.add_score(0)
        else:
            self.add_score(payout)

        # Print a custom message for lottery
        print(f'Welcome to the Ore Lottery! \nLot One Pulled: {lot_one} \nLot Two Pulled: {lot_two} \nYour Total Payout is:{payout} ')
