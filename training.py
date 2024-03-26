from tic_tac_toe import TicTacToe, PlayerType, RLPlayer

class TrainRLAgent:
    def __init__(self, tic_tac_toe_instance, episodes=500, learning_rate=0.1, discount_rate=0.2, epsilon=0.3):
        """
        Initialize the TrainRLAgent.

        Args:
        - tic_tac_toe_instance: An instance of TicTacToe game.
        - episodes: Number of training episodes (default is 500).
        - learning_rate: The learning rate for the RL agent (default is 0.1).
        - discount_rate: The discount rate for future rewards (default is 0.2).
        - epsilon: The exploration rate for the RL agent (default is 0.3).
        """
        self.tic_tac_toe_instance = tic_tac_toe_instance
        self.episodes = episodes
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.epsilon = epsilon

    def train(self):
        """
        Train the RL agent for playing TicTacToe.
        """
        # Initialize RL player with 'X'
        rl_agent = RLPlayer('X')
        rl_agent.init_training(self.learning_rate, self.discount_rate, self.epsilon)

        # Create a random agent as a partner for training
        partner = self.tic_tac_toe_instance.create_player('O', PlayerType.RANDOM_AGENT)

        # Train the RL agent against the random agent
        self.tic_tac_toe_instance.train(rl_agent, partner, self.episodes)

        # Save the trained RL agent
        rl_agent.save()

# Example usage:
if __name__ == "__main__":
    # Create an instance of TicTacToe
    tic_tac_toe_instance = TicTacToe()

    # Train the RL agent
    trainer = TrainRLAgent(tic_tac_toe_instance)
    trainer.train()
