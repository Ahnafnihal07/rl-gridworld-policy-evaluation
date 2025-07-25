"""
Gridworld Environment for both deterministic and episodic versions.
"""
import numpy as np

class Gridworld:
    def __init__(self, stochastic=False, terminal_states=None, penalty_step=-0.2, penalty_offgrid=-0.5):
        self.grid_size = 5
        self.actions = ['up', 'down', 'left', 'right']
        self.state_space = list(range(self.grid_size ** 2))
        self.stochastic = stochastic
        self.terminal_states = terminal_states or []
        self.penalty_step = penalty_step
        self.penalty_offgrid = penalty_offgrid
        self.action_map = {
            'up': -self.grid_size,
            'down': self.grid_size,
            'left': -1,
            'right': 1
        }

    def step(self, state, action):
        if state in self.terminal_states:
            return state, 0

        move = self.action_map[action]
        new_state = state + move

        if action == 'up' and state < self.grid_size:
            return state, self.penalty_offgrid
        elif action == 'down' and state >= self.grid_size * (self.grid_size - 1):
            return state, self.penalty_offgrid
        elif action == 'left' and state % self.grid_size == 0:
            return state, self.penalty_offgrid
        elif action == 'right' and (state + 1) % self.grid_size == 0:
            return state, self.penalty_offgrid

        if new_state in self.terminal_states:
            return new_state, 0

        return new_state, self.penalty_step
