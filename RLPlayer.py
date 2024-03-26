class RLPlayer(Player):
    def __init__(self, letter, alpha, gamma):
        super().__init__(letter, PlayerType.RL_AGENT)
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount rate
        self.valueFunction = {}  # Dictionary to store state values

    def makeMove(self, board):
        if self.mode == TRAINING_MODE:
            n = random.random()
            if n < self.epsilon:
                any_move = random.choice(board.remaining_moves)
                move_legal = board.makeMove(any_move, self.letter)
                if not move_legal:
                    print('*** WARNING ILLEGAL MOVE BY RL ***')
                else:
                    self.rewardState(board)
                    self.previousBoard = copy.deepcopy(board)
            else:
                self.getRLMove(board)
        else:
            self.getRLMove(board)

    def rewardState(self, board):
        key = board.getKey(self.letter)  # Current board state key
        reward = self.getReward(board)  # Get reward for current board state

        if self.previousBoard is not None:
            prevKey = self.previousBoard.getKey(self.letter)  # Previous board state key
            valuePrev = self.valueOfState(prevKey)  # Value of previous state
            valueCurrent = self.valueOfState(key)  # Value of current state
            self.valueFunction[prevKey] = valuePrev + self.alpha * (
                        reward + (self.gamma * valueCurrent) - valuePrev)
        else:
            self.valueFunction[key] = self.valueFunction.get(key, 0) + self.alpha * reward

    def getReward(self, board):
        if board.isGameWon(self.letter):
            return 1
        elif board.isGameDraw():
            return 0
        else:
            return 0  # No reward for ongoing game

    def valueOfState(self, key):
        return self.valueFunction.get(key, 0)  # Default value is 0 if state not found
elf, board):
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
