# Unittest Monte Carlo Module
# Pranav Thiriveedhi
# DS 5100 Final Project

# Import Statements
import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer


class TestDie(unittest.TestCase):
    def setUp(self):
        self.faces = np.array([1, 2, 3, 4, 5, 6])
        self.die = Die(self.faces)

    def test_initializer(self):
        self.assertTrue(isinstance(self.die.show(), pd.DataFrame))
        self.assertEqual(self.die.show().shape[0], len(self.faces))

    def test_change_weight(self):
        self.die.change_weight(1, 3)
        df = self.die.show()
        self.assertEqual(df.at[1, 'Weight'], 3)

    def test_roll(self):
        rolls = self.die.roll(10)
        self.assertEqual(len(rolls), 10)
        self.assertTrue(all(face in self.faces for face in rolls))

    def test_show(self):
        df = self.die.show()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue('Weight' in df.columns)


class TestGame(unittest.TestCase):
    def setUp(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        d1 = Die(faces)
        d2 = Die(faces)
        self.game = Game([d1, d2])

    def test_initializer(self):
        self.assertTrue(isinstance(self.game, Game))

    def test_play(self):
        self.game.play(3)
        results = self.game.show()
        self.assertTrue(isinstance(results, pd.DataFrame))
        self.assertEqual(results.shape[0], 3)

    def test_show(self):
        self.game.play(3)
        wide_results = self.game.show(form='wide')
        self.assertTrue(isinstance(wide_results, pd.DataFrame))

        narrow_results = self.game.show(form='narrow')
        self.assertTrue(isinstance(narrow_results, pd.DataFrame))
        #self.assertTrue('Roll' in narrow_results.columns)
        self.assertTrue('Die' in narrow_results.columns)
        self.assertTrue('Face' in narrow_results.columns)


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        faces = np.array(['1', '2', '3'])
        d1 = Die(faces)
        d2 = Die(faces)
        self.game = Game([d1, d2])
        self.game.play(5)
        self.analyzer = Analyzer(self.game)

    def test_initializer(self):
        self.assertTrue(isinstance(self.analyzer, Analyzer))

    def test_jackpot(self):
        result = self.analyzer.jackpot()
        #self.assertTrue(isinstance(result, int))

    def test_face_counts(self):
        df = self.analyzer.face_counts()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(df.shape[0], 5)  # Matches number of rolls

    def test_combo_counts(self):
        df = self.analyzer.combo_counts()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue('Combination' in df.columns or df.index.name == 'Combination')
        self.assertTrue('Count' in df.columns)

    def test_permutation_counts(self):
        df = self.analyzer.permutation_counts()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue('Permutation' in df.columns or df.index.name == 'Permutation')
        self.assertTrue('Count' in df.columns)


if __name__ == '__main__':
    unittest.main()