from your_rl_module import RLPlayer  # Import RLPlayer class from your RL module
from your_ttt_module import TicTacToe  # Import TicTacToe class from your TicTacToe module

class TrainRLAgent:
    """Class for training a reinforcement learning agent to play Tic-Tac-Toe.

    Attributes:
        rl_agent (RLPlayer): The reinforcement learning agent being trained.
        ttt (module): The Tic-Tac-Toe module.
        partner (Player): The opponent player for training the RL agent.
    """

    def __init__(self, ttt_module):
        """Initializes the TrainRLAgent with the specified Tic-Tac-Toe module.

        Args:
            ttt_module (module): The Tic-Tac-Toe module.
        """
        self.rl_agent = RLPlayer('X')
        self.ttt = ttt_module
        self.partner = self.ttt.create_player('O', self.ttt.RANDOM_AGENT)
        self.rl_agent.init_training(learning=0.1, discount=0.2, epsilon=0.3)

    def train(self, episodes=500):
        """Trains the reinforcement learning agent.

        Args:
            episodes (int, optional): The number of training episodes. Defaults to 500.
        """
        for _ in range(episodes):
            self.ttt.train(self.rl_agent, self.partner)

        self.rl_agent.save()

# Usage:
# ttt_module = YourTicTacToeModule()
# trainer = TrainRLAgent(ttt_module)
# trainer.train()
