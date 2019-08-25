import numpy as np
import copy


class Stats:
    def __init__(self, q):
        self.q = q

class QTable:
    def __init__(self, actions):
        actions_dict = {}
        for action in actions:
            actions_dict[action] = Stats(0)

        self.actions = actions_dict
        self.states = {}

    def assure_state_exists(self, state):
        if state not in self.states:
            self.states[state] = {}
            self.states[state]['actions'] = dict(copy.deepcopy(self.actions))
            self.states[state]['n'] = 1

    def get_action_stats(self, state, action):
        actions = self.states[state]['actions']
        stats = actions[action]
        return stats

    def get_q_value(self, state, action):
        self.assure_state_exists(state)
        stats = self.get_action_stats(state, action)
        return stats.q

    def set_q_value(self, state, action, q):
        self.assure_state_exists(state)        
        stats = self.get_action_stats(state, action)
        stats.q = q

    def get_n_value(self, state):
        self.assure_state_exists(state)
        state = self.states[state]
        return state['n']

    def increse_n_value(self, state):
        self.assure_state_exists(state)        
        self.states[state]['n'] += 1
    

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
                q_vals[idx] = self.get_q_value(state, a)
                idx += 1

            return self.randargmax(q_vals)

            

