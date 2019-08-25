import numpy as np

class GameEnvironment:
    def __init__(self):
        # Player draws cards
        self.player_sum = self.draw_black_card()

        # Dealer draws card
        self.dealer_sum = self.draw_black_card()
        self.terminated = False
    
    def reset(self):
        self.__init__()

    def get_state(self):
        return (self.dealer_sum, self.player_sum)

    def step(self, action):
        """ 0 = stick, 1 == hit """
        if action == 0:
            return self.stick()
        if action == 1:
            return self.hit()

    def is_bust(self, points):
       return points > 21 or points < 1

    def hit(self):
        card = self.draw_card()
        self.player_sum += card
        if self.is_bust(self.player_sum):
            # Player busts and loses
            self.terminated = True
            return  -1
        else:
            return 0


    def stick(self):
        while self.dealer_sum < 17:
            self.dealer_sum += self.draw_card()
            if self.is_bust(self.dealer_sum):
                # Dealer busts, player gets reward
                self.terminated = True
                return 1
        
        if self.player_sum > self.dealer_sum:
            self.terminated = True
            return 1
        if self.dealer_sum > self.player_sum:
            self.terminated = True
            return -1
        else: # draw
            self.terminated = True
            return 0 


    def draw_black_card(self):
        card = int(np.random.uniform(1,11))
        return card

    def draw_card(self):
        is_black = np.random.choice([-1,1], p=[1/3, 2/3])
        card = int(np.random.uniform(1,11))
        return is_black*card