"""
This module runs the Red/Green Game.
"""

import redgreen_game.redgreen_data as redgreen_data

def main():
    """
    This is the main function that runs the game
    :return: None
    """

    # Initializations

    game_instance = redgreen_data.GameStyle()

    print("Welcome to the Red/Green Game!")

    teams = int(input('How many teams are playing? '))

    game_instance.number_teams = teams

    return


if __name__ == '__main__':
    main()
