class UI:
    def __init__(self):
        pass

    def display_game_rules(self):
        print("\nGame Rules\n__________\n"
              "Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to 'hold':" +
              "\nIf the player rolls a 1, they score nothing and it becomes the next player's turn.\n"
              "If the player rolls any other number, it is added to their turn total and the player's turn continues.\n"
              "If a player chooses to 'hold', their turn total is added to their score, and it becomes the next player's turn. "
              "\n\nThe first player to score the threshold or more points wins.")
