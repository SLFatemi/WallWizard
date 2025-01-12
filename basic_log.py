import json
import random

class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.logs = []

    def log_move(self, player, move):
        self.logs.append({"player": player, "move": move})

    def log_winner(self, winner):
        self.logs.append({"winner": winner})

    def save_logs(self):
        with open(self.filename, 'w') as f:
            json.dump(self.logs, f, indent=4)

class Game:
    def __init__(self, logger):
        self.logger = logger
        self.players = ['Player 1', 'Player 2']
        self.moves = []
        self.winner = None

    def play(self):
        for i in range(10):
            player = self.players[i % 2]
            move = random.choice(['move_left', 'move_right', 'move_up', 'move_down'])
            print(f"{player} makes a move: {move}")
            self.logger.log_move(player, move)
            self.moves.append((player, move))

        self.winner = random.choice(self.players)
        print(f"The winner is {self.winner}")
        self.logger.log_winner(self.winner)

if __name__ == "__main__":
    logger = Logger('game_logs.json')
    game = Game(logger)
    game.play()
    logger.save_logs()