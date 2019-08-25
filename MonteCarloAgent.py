from GameEnvironment import GameEnvironment
from QTable import QTable
from tqdm import tqdm
from putils import plot

NUM_EPISODES = 100000

Q = QTable([0,1])
N = QTable([0,1],1)
env = GameEnvironment()

for e in tqdm(range(NUM_EPISODES)):

    env.reset()

    state = env.get_state()
    state_hist = []
    G = 0

    while not env.terminated:
        action = Q.choose_action(state)
        reward = env.step(action)

        N[state, action] += 1

        G += reward
        state_hist.append((state,action))
        state = env.get_state()

    for (state,action) in state_hist:
        alpha = 1/N[state, action]
        q = Q[state, action]
        q += alpha*(G-q)
        Q[state, action] = q

    

plot(Q.as_matrix(),[0,1])