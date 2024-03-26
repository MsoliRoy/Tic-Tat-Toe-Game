def evaluate_rl_agent():
    rl_agent = RLPlayer('X')
    rl_agent.load_policy('cse_policy_hw2.txt')  # Assuming you have a method to load the policy
    partner = ttt.create_player('O', ttt.RANDOM_AGENT)
    rl_agent.set_mode(ttt.PLAYING_MODE)
    tournament = ttt.Tournament()
    tournament.start(rl_agent, partner, games=5)
    tournament.start(partner, rl_agent, games=5)
    tournament.print_stats([rl_agent, partner])
  
