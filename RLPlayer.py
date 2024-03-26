class RLPlayer:
    def __init__(self, letter):
        self.letter = letter
        self.mode = TRAINING_MODE  # Assuming TRAINING_MODE is defined
        self.learning_rate = 0.1  # Initial values
        self.discount_rate = 0.2
        self.epsilon = 0.3
        self.previous_board = None
        self.value_function = {}

    def make_move(self, board):
        if self.mode == TRAINING_MODE:
            n = random.random()
            if n < self.epsilon:
                any_move = random.choice(board.remaining_moves)
                move_legal = board.make_move(any_move, self.letter)
                if not move_legal:
                    print('*** WARNING ILLEGAL MOVE BY RL ***')
                else:
                    self.reward_state(board)
                    self.previous_board = copy.deepcopy(board)
            else:
                self.get_rl_move(board)
        else:
            self.get_rl_move(board)

    def reward_state(self, board):
        if self.previous_board is None:
            reward = self.get_reward(board)
            key = board.get_key(self.letter)
            self.value_function[key] = self.value_function.get(key, 0) + self.learning_rate * reward
        else:
            reward = self.get_reward(board)
            key = board.get_key(self.letter)
            value_current = self.value_of_state(key)
            previous_key = self.previous_board.get_key(self.letter)
            value_previous = self.value_of_state(previous_key)
            self.value_function[previous_key] = value_previous + self.learning_rate * (
                        reward + (self.discount_rate * value_current) - value_previous)

    def get_reward(self, board):
        # Define your reward scheme here
        # For example:
        if board.is_game_won(self.letter):
            return 10
        elif board.is_game_draw():
            return 1
        else:
            return -1
