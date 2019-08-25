import numpy as np
import copy


class QTable:
    def __init__(self, actions, init = 0):
        actions_dict = {}
        for action in actions:
            actions_dict[action] = init

        self.actions = actions_dict
        self.states = {}
        self.init = init

    def assure_state_exists(self, state):
        if state not in self.states:
            actions = dict(copy.deepcopy(self.actions))
            self.states[state] = actions

    def get_value(self, state, action):
        self.assure_state_exists(state)
        actions = self.states[state]
        return actions[action]

    def set_value(self, state, action, val):
        self.assure_state_exists(state)   
        self.states[state][action] = val

    def __setitem__(self, index, value):
        self.set_value(index[0],index[1],value)

    def __getitem__(self, index):
        return self.get_value(index[0],index[1])

    def randargmax(self, b,**kw):
        """ a random tie-breaking argmax"""
        return np.argmax(np.random.random(b.shape) * (b==b.max()), **kw)

    def choose_action(self, state):
        epsilon = 0.1
        should_choose_random = np.random.choice([False, True], p=[(1-epsilon), epsilon])

        if should_choose_random:
            # Choose random/epsilon action
            return np.random.choice(list(self.actions.keys()))
        else:
            # Choose greedy action
            largest_q_value = -np.inf
            action = -1

            q_vals = np.zeros(len(self.actions))
            idx = 0
            for a in self.actions:
                q_vals[idx] = self.get_value(state, a)
                idx += 1

            return self.randargmax(q_vals)

    def as_matrix(self):
        M = np.zeros((22,22,2))
        for d in range(1,22):
            for p in range(1,22):
                M[d,p,0] = self.get_value((d,p),0)
                M[d,p,1] = self.get_value((d,p),1)
        return M


        


            

