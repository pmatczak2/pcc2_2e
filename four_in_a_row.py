"""A title-dropping game to ger four-in-a-row, similar to Connect Four."""

import sys
# Constant used for displaying the board:
EMPTY_SPACE = "."  # A period is easier to count than a space.
PLAYER_X = "X"
PLAYER_O = "O"

# Note: Update BOARD_TEMPLATE & COLUMN_LABLES if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# The template string for display the board:
BOARD_TEMPLATE = """
        1234567
        +-------+
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        +-------+"""

    def main():
        """Runs a single game of Four-in-a-row."""
        print(
            """Four-in-a-Row Two players take turns dropping tiles into one of seven clumns, trying
               to make Four-in-a-Row horizontally, vertically, or diagonally. 
               """
        )

        # Set up a new game:
