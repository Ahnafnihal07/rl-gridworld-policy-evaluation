"""
Monte Carlo Control Methods: Exploring Starts, ε-Soft, Off-Policy
"""
import numpy as np
import random

def mc_control_es(env, gamma=0.95, episodes=5000):
    Q = {s: {a: 0 for a in env.actions} for s in env.state_space}
    returns = {s: {a: [] for a in env.actions} for s in env.state_space}
    policy = {s: random.choice(env.actions) for s in env.state_space}

    for _ in range(episodes):
        s = random.choice(env.state_space)
        a = random.choice(env.actions)
        episode = []
        while s not in env.terminal_states:
            next_s, r = env.step(s, a)
            episode.append((s, a, r))
            s = next_s
            a = policy[s] if s in policy else random.choice(env.actions)

        G = 0
        for s, a, r in reversed(episode):
            G = gamma * G + r
            if (s, a) not in [(x[0], x[1]) for x in episode[:-1]]:
                returns[s][a].append(G)
                Q[s][a] = np.mean(returns[s][a])
                policy[s] = max(Q[s], key=Q[s].get)

    return policy

def mc_control_eps(env, gamma=0.95, episodes=5000, epsilon=0.1):
    Q = {s: {a: 0 for a in env.actions} for s in env.state_space}
    returns = {s: {a: [] for a in env.actions} for s in env.state_space}
    policy = {s: random.choice(env.actions) for s in env.state_space}

    for _ in range(episodes):
        s = random.choice(env.state_space)
        episode = []
        while s not in env.terminal_states:
            if random.random() < epsilon:
                a = random.choice(env.actions)
            else:
                a = policy[s]
            next_s, r = env.step(s, a)
            episode.append((s, a, r))
            s = next_s

        G = 0
        for s, a, r in reversed(episode):
            G = gamma * G + r
            if (s, a) not in [(x[0], x[1]) for x in episode[:-1]]:
                returns[s][a].append(G)
                Q[s][a] = np.mean(returns[s][a])
                policy[s] = max(Q[s], key=Q[s].get)

    return policy
