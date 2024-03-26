def train_rl_agent():
    rl_agent = RLPlayer('X')
    partner = ttt.create_player('O', ttt.RANDOM_AGENT)
    rl_agent.init_training(learning=0.1, discount=0.2, epsilon=0.3)
    ttt.train(rl_agent, partner, episodes=500)
    rl_agent.save()
