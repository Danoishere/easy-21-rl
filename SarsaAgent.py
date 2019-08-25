from GameEnvironment import GameEnvironment
from QTable import QTable
from tqdm import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from putils import plot


#lambdas = [0.1,0.2,0.3,0.4,0.5,.6,.7,.8,.9]
lambdas = [.5]
for lambd in lambdas:
    NUM_EPISODES = 10000
    ALPHA = 0.5
    LAMBDA = lambd

    Q = QTable([0,1])
    N = QTable([0,1], 1)
    env = GameEnvironment()

    for e in tqdm(range(NUM_EPISODES)):

        env.reset()

        E = QTable([0,1]) # Eligebility trace
        state = env.get_state()
        action = Q.choose_action(state)

        while not env.terminated:

            N[state, action] += 1
            reward = env.step(action)

            if env.terminated:
                # delta = reward we got vs reward we expected
                delta = reward - Q[state, action]
            else:
                next_state = env.get_state()
                next_action = Q.choose_action(next_state)
                # delta = reward we got for this step plus,
                # next_reward - current reward = reward gain over next step
                # if the q value of the next state is smaller than the current q value,
                # that means that the current reward is worth less
                delta = reward + (Q[next_state, next_action] - Q[state, action])
            
            # Update eligebility information for recently visited states
            E[state, action] += 1

            # Flatten eligebility and update action values (Q-Values)
            for state in E.states:
                for action in E.states[state]:
                    alpha = 1.0/N[state, action]
                    Q[state, action] += alpha*delta*E[state, action]
                    E[state, action] *= LAMBDA # Fade eligebility trace

            if not env.terminated:
                state = next_state
                action = next_action



    plot(Q.as_matrix(),[0,1])

    num_won = 0
    num_lost = 0

    env = GameEnvironment()

    # EVALUATION
    for i in range(100):
        while not env.terminated:
            state = env.get_state()
            action = Q.choose_action(state)
            reward = env.step(action)

        if reward == 1:
            num_won +=1
        else:
            num_lost+=1

        env.reset()

    print('Lambda:',lambd)
    print('Won:', num_won)
    print('Lost:',num_lost)

    # 39 - 61
