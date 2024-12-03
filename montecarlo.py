# Monte Carlo Module
# Pranav Thiriveedhi
# DS 5100 Final Project

# Import Statements
import numpy as np
import pandas as pd


# Die Class
class Die:
    """
    Die has N sides and W weights, can be rolled to select a face.
    If N = 2, it is a coin, if N = 6, it is a standard die.
    """
    def __init__(self, faces):
        """
        Die with number of faces as an argument.
        Parameters:
        - faces: Array of number of faces.
        Raises:
        - TypeError: Number of faces is not a NumPy array.
        - ValueError: Number of faces is not distinct.
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Number of faces must be a NumPy array.")
        if len(faces) != len(set(faces)):
            raise ValueError("Each face should have a distinct value.")
        
        self._faces = faces
        self._weights = np.ones(len(faces), dtype=float)
        self._die_df = pd.DataFrame({'Face': faces, 'Weight': self._weights}).set_index('Face')

    def change_weight(self, face_value, new_weight):
        """
        Changes the weight of a face's value to a new weight.
        Parameters:
        - face_value: The face value to change the weight for.
        - new_weight (int or float): The new weight value for the face specified.
        Raises:
        - IndexError: The face is not in the die array.
        - TypeError: The weight is not numeric (int or float).
        """
        if face_value not in self._die_df.index:
            raise IndexError("Face is not in die array.")
        try:
            new_weight = float(new_weight)
        except ValueError:
            raise TypeError("Weight is not a numeric value.")
        self._die_df.at[face_value, 'Weight'] = new_weight

    def roll(self, num_rolls=1):
        """
        How many times a die is rolled.
        Parameters:
        - num_rolls (int): Number of die rolls. Defaults to 1.
        Returns:
        - list: List of rolled faces.
        """
        return list(self._die_df.sample(n=num_rolls, weights='Weight', replace=True).index)

    def show(self):
        """
        Returns a copy of the private dataframe of the die's current status
        Returns:
        - pd.DataFrame: Data frame of current state of die.
        """
        return self._die_df.copy()

    
# Game Class
class Game:
    """
    Game involving rolling one or more die objects, one or more times.
    """
    def __init__(self, dice):
        """
        List of similar dice.
        Parameters:
        - dice (list of Die): List of Die objects.
        """
        self._dice = dice
        self._results_df = None

    def play(self, num_rolls):
        """
        Rolls dice a specified number of times.
        Parameters:
        - num_rolls (int): Number of rolls to play.
        Updates:
        - _results_df (pd.DataFrame): Results of the game in wide format.
        """
        rolls = {f'Die_{i}': die.roll(num_rolls) for i, die in enumerate(self._dice)}
        self._results_df = pd.DataFrame(rolls)

    def show(self, form='wide'):
        """
        Shows the results of the most recent play.
        Parameters:
        - form (str): wide or narrow format. Defaults to wide.
        Returns:
        - pd.DataFrame: Dataframe in wide or narrow format.
        Raises:
        - ValueError: If an invalid format is given.
        """
        if self._results_df is None:
            return None
        
        if form == 'wide':
            return self._results_df.copy()
        elif form == 'narrow':
            return self._results_df.stack().reset_index(name='Face').rename(columns={'level_0': 'Roll', 'level_1': 'Die'})
        else:
            raise ValueError("Needs to be a narrow or wide option.")


# Analyzer Class
class Analyzer:
    """
    A class to analyze the results of a game and computer varius statistics about it.
    """
    def __init__(self, game):
        """
        Initializes the Analyzer with a Game object.
        Parameters:
        - game (Game): Game object.
        Raises:
        - ValueError: If the value is not a Game object.
        """
        if not isinstance(game, Game):
            raise ValueError("Passed value must be a Game object.")
        self._game = game
        self._results = game.show()

    def jackpot(self):
        """
        Number of jackpots (all faces are the same in a roll).
        Returns:
        - int: How many times the game resulted in jackpots.
        """
        return (self._results.nunique(axis=1) == 1).sum()

    def face_counts(self):
        """
        Counts of each face value for each roll.
        Returns:
        - pd.DataFrame: Data frame of results.
        """
        return self._results.apply(pd.Series.value_counts, axis=1).fillna(0)

    def combo_counts(self):
        """
        Distinct combinations of rolled faces with counts.
        Returns:
        - pd.DataFrame: Data frame with combinations and counts.
        """
        combination = self._results.apply(lambda row: tuple(sorted(row)), axis=1)
        return combination.value_counts().rename_axis('Combination').reset_index(name='Count')

    def permutation_counts(self):
        """
        Distinct permutations of rolled faces with counts.
        Returns:
        - pd.DataFrame: Data frame with permutations and counts.
        """
        permutations = self._results.apply(tuple, axis=1)
        return permutations.value_counts().rename_axis('Permutation').reset_index(name='Count')