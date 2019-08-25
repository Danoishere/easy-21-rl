from GameEnvironment import GameEnvironment

env = GameEnvironment()

i = ''

while i != 'quit':
    print('Next game!')
    while (not env.terminated) and i != 'quit':
        print('Dealer-sum:', env.dealer_sum)
        print('Player-sum', env.player_sum)
        print('h = hit / s = stick')
        i = input()

        if i == 'h':
            reward= env.step(1)
            print('Dealer-sum:', env.dealer_sum)
            print('Player-sum', env.player_sum)
            print('Hit! Reward:', reward)
        elif i == 's':
            reward = env.step(0)
            print('Dealer-sum:', env.dealer_sum)
            print('Player-sum', env.player_sum)
            print('Stick! Reward:', reward)
        

    env.reset()
    print('Game finished!')
