"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below. # noqa: E501

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'. # noqa: E501

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


print(bake_time_remaining(30))

# TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant. # noqa: E501
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers added to the lasagna.
    :return: int - total preparation time (in minutes) derived from 'PREPARATION_TIME' per layer. # noqa: E501

    Function that takes the number of layers added to the lasagna as
    an argument and returns how many minutes it will take to prepare
    the lasagna based on the `PREPARATION_TIME` per layer.
    """
    return PREPARATION_TIME * number_of_layers


print(preparation_time_in_minutes(3))

# TODO: define the 'elapsed_time_in_minutes()' function below.


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes) derived from preparation and baking times. # noqa: E501

    Function that takes the number of layers added to the lasagna and the
    actual minutes the lasagna has been in the oven as arguments and returns
    the total elapsed time spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


print(elapsed_time_in_minutes(3, 20))

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
