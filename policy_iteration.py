"""
Value Iteration and Policy Iteration for Gridworld
"""
import numpy as np

def value_iteration(env, gamma=0.95, theta=1e-4):
    V = np.zeros(len(env.state_space))
    policy = np.zeros((len(env.state_space), len(env.actions)))
    while True:
        delta = 0
        for s in env.state_space:
            v = V[s]
            q_sa = []
            for i, a in enumerate(env.actions):
                next_state, r = env.step(s, a)
                q_sa.append(r + gamma * V[next_state])
            V[s] = max(q_sa)
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    for s in env.state_space:
        q_sa = []
        for i, a in enumerate(env.actions):
            next_state, r = env.step(s, a)
            q_sa.append(r + gamma * V[next_state])
        best_a = np.argmax(q_sa)
        policy[s] = np.eye(len(env.actions))[best_a]
    return V, policy
