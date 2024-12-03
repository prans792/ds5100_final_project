# Monte Carlo Final Project

## Metadata
- **Project Name:** Monte Carlo Simulator
- **Author:** Pranav Thiriveedhi 

---

## Synopsis

The Monte Carlo Simulator allows users to play games with dice and analyze outcomes using statistics. 

### Installation
To install the required libraries, run:
```bash
pip install numpy pandas

```
### Create a die
```
import numpy as np
from montecarlo import Die

# Create a 6-sided die 
faces = np.array([1, 2, 3, 4, 5, 6])
die = Die(faces)

# Change the weight of face 1 to 3
die.change_weight(1, 3)

# Roll the die 5 times
rolls = die.roll(5)
print("Rolls:", rolls)

# Show the current state of the die
print(die.show())

```
### Play game
```
from montecarlo import Game

# Create multiple dice
d1 = Die(np.array([1, 2, 3, 4, 5, 6]))
d2 = Die(np.array([1, 2, 3, 4, 5, 6]))
game = Game([d1, d2])

# Play the game with 5 rolls
game.play(5)

# Show the results of the game
print(game.show())

```
### Analyze Game
```
from montecarlo import Analyzer

# Analyze the results of the game
analyzer = Analyzer(game)

# Compute the number of jackpots
jackpots = analyzer.jackpot()
print("Number of jackpots:", jackpots)

# Get face counts per roll
face_counts = analyzer.face_counts_per_roll()
print("Face counts per roll:")
print(face_counts)

# Get combo counts
combo_counts = analyzer.combo_counts()
print("Combo counts:")
print(combo_counts)

# Get permutation counts
permutation_counts = analyzer.permutation_counts()
print("Permutation counts:")
print(permutation_counts)

```
### API Description

Class: Die
Methods
__init__(faces: np.ndarray) -> None
  Parameters:
        - faces: Array of number of faces.
  Raises:
        - TypeError: Number of faces is not a NumPy array.
        - ValueError: Number of faces is not distinct.

change_weight(face: Any, new_weight: float) -> None
  Parameters:
        - face_value: The face value to change the weight for.
        - new_weight (int or float): The new weight value for the face specified.
  Raises:
        - IndexError: The face is not in the die array.
        - TypeError: The weight is not numeric (int or float).

roll(times: int = 1) -> list
  Parameters:
        - num_rolls (int): Number of die rolls. Defaults to 1.
  Returns:
        - list: List of rolled faces.

show() -> pd.DataFrame
  Returns:
    A Pandas DataFrame with faces and their weights.

Class: Game
Methods
__init__(dice: list) -> None
  Parameters:
        - dice (list of Die): List of Die objects.

play(rolls: int) -> None
  Parameters:
        - num_rolls (int): Number of rolls to play.
  Updates:
        - _results_df (pd.DataFrame): Results of the game in wide format.

show(form: str = 'wide') -> pd.DataFrame
  Parameters:
        - form (str): wide or narrow format. Defaults to wide.
  Returns:
        - pd.DataFrame: Dataframe in wide or narrow format.
  Raises:
        - ValueError: If an invalid format is given.

Class: Analyzer
Methods
__init__(game: Game) -> None
  Parameters:
        - game (Game): Game object.
  Raises:
        - ValueError: If the value is not a Game object.

jackpot() -> int
  Returns:
        - int: How many times the game resulted in jackpots.

face_counts() -> pd.DataFrame
  Returns:
        - pd.DataFrame: Data frame of results.

combo_counts() -> pd.DataFrame
  Returns:
        - pd.DataFrame: Data frame with combinations and counts.
        
permutation_counts() -> pd.DataFrame
  Returns:
        - pd.DataFrame: Data frame with permutations and counts.



