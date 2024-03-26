from your_rl_module import RLPlayer
from your_ttt_module import TicTacToe

class EvaluateRLAgent:
    """
    Class to evaluate the performance of an RL agent in playing TicTacToe.

    Attributes:
        rl_agent (RLPlayer): The RL player agent to be evaluated.
        ttt (module): The module containing the TicTacToe game implementation.
        partner (Player): The opponent player.
        tournament (Tournament): The tournament organizer for evaluating game performance.

    Methods:
        __init__(ttt_module): Initializes the evaluation process with the provided TicTacToe module.
        evaluate(): Initiates the evaluation process by running a series of games between the RL agent and the opponent.
    """

    def __init__(self, ttt_module):
        """
        Initializes the evaluation process with the provided TicTacToe module.

        Args:
            ttt_module (module): The module containing the TicTacToe game implementation.
        """
        self.rl_agent = RLPlayer('X')
        self.rl_agent.load_policy('cse_policy_hw2.txt')  # Assuming you have a method to load the policy
        self.ttt = ttt_module
        self.partner = self.ttt.create_player('O', self.ttt.PlayerType.RANDOM_AGENT)
        self.rl_agent.set_mode(self.ttt.PlayerType.PLAYING_MODE)
        self.tournament = self.ttt.Tournament()

    def evaluate(self):
        """
        Initiates the evaluation process by running a series of games between the RL agent and the opponent.
        """
        try:
            self.tournament.start(self.rl_agent, self.partner, games=5)
            self.tournament.start(self.partner, self.rl_agent, games=5)
            self.tournament.print_stats([self.rl_agent, self.partner])
        except Exception as e:
            print(f"An error occurred during evaluation: {e}")

# Usage:
# ttt_module = YourTicTacToeModule()
# evaluator = EvaluateRLAgent(ttt_module)
# evaluator.evaluate()
