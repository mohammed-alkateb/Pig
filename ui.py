"""
import Theme, Console, track, time
"""
from rich.theme import Theme
from rich.console import Console


class UI:
    """
    User interface class
    """
    def __init__(self) -> None:
        """
        constructor with color setup
        :return: None
        """
        self.custom_theme = Theme({"success": "green", "error": "bold red"})
        self.console = Console(theme=self.custom_theme, force_terminal=True)

    def display_game_rules(self) -> None:
        """
        display game rules
        :return: None
        """
        self.console.print("\n\nGame Rules\n__________", style="dark_orange3")
        self.console.print("Each turn, a player repeatedly rolls a die until "
                           "either a 1 is rolled or the player decides to "
                           "'hold':\nIf the player rolls a 1, they score "
                           "nothing and it becomes the next player's turn."
                           "\n If the player rolls any other number, it is"
                           " added to their turn total and the player's turn"
                           " continues.\n If a player chooses to 'hold', "
                           "their turn total is added to their score, and it"
                           " becomes the next player's turn. \n\nThe first "
                           "player to score the threshold or more points wins."
                           "\n", style="gold3")

    def display_info(self) -> None:
        """
        display player info
        :return: None
        """
        self.console.print("Player name, Played Matches, Total wins,"
                           " Total losses, High score", style="deep_pink1")

    def only_alphabet_exception(self) -> None:
        """
        display alphabet exception
        :return: None
        """
        self.console.print("The name should contain only alphabet!\n", style="error")

    def only_digits_exception(self) -> None:
        """
        display digits exception
        :return: None
        """
        self.console.print("It should contain only digits\n", style="error")

    def out_of_range_exception(self) -> None:
        """
        Display out of range exception
        :return: None
        """
        self.console.print("Out of range\n", style="error")

    def player_registered(self, name) -> None:
        """
        display registered msg to player
        :param name: registered player name
        :return: None
        """
        self.console.print(f"New player with the name '{name}' registered", style="success")

    def player_confirmed(self, name) -> None:
        """
        confirm msg player exists
        :param name: player name
        :return: None
        """
        self.console.print(f"{name} has been confirmed!", style="success")

    def invalid_input_exception(self) -> None:
        """
        display invalid input exception
        :return: None
        """
        self.console.print("Invalid input", style="error")

    def one_was_rolled(self) -> None:
        """
        one was rolled msg
        :return: None
        """
        self.console.print("A 1 was rolled\n", style="purple")

    def display_dice_cast(self, name, cast) -> None:
        """
        Display dice cast value
        :param name: player name
        :param cast: cast value
        :return: None
        """
        self.console.print(f"{name} have got {cast}", style="green3")
