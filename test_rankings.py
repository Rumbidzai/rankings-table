import unittest
import rankings


class RankingsTestCase(unittest.TestCase):
    """ Tests for rankings.py. """

    def test_split_game_with_newlines(self):
        """ Test that multi-line game input is split correctly.
        """
        game_list = [
            "Lions 3, Snakes 3\n",
            "Tarantulas 1, FC Awesome 0\n",
            "Lions 1, FC Awesome 1\n",
            "Tarantulas 3, Snakes 1\n",
            "Lions 4, Grouches 0\n"
        ]
        expected = [
            ['Lions 3', 'Snakes 3'],
            ['Tarantulas 1', 'FC Awesome 0'],
            ['Lions 1', 'FC Awesome 1'],
            ['Tarantulas 3', 'Snakes 1'],
            ['Lions 4', 'Grouches 0']
        ]

        split_list = rankings.split_games(game_list)
        self.assertEqual(split_list, expected)

    def test_compare_scores(self):
        """ Test that game results are correctly translated into rankings:
            win = 3 points
            loss = 0 points
            draw = 1 point for each team
        """
        games = [
            ['Lions 3', 'Snakes 3'],
            ['Tarantulas 1', 'FC Awesome 0'],
            ['Lions 1', 'FC Awesome 1'],
            ['Tarantulas 3', 'Snakes 1'],
            ['Lions 4', 'Grouches 0']
        ]
        expected = {
            'Tarantulas': 6,
            'FC Awesome': 1,
            'Snakes': 1,
            'Lions': 5,
            'Grouches': 0
        }

        score_results = rankings.compare_scores(games)
        self.assertEqual(score_results, expected)

    def test_sort_order(self):
        """ Test that teams in rankings table are correctly sorted in
            descending order by score.
        """
        input = {
            'Tarantulas': 2,
            'FC Awesome': 4,
            'Snakes': 3,
            'Lions': 0,
            'Grouches': 1
        }
        expected = [
            ('FC Awesome', 4),
            ('Snakes', 3),
            ('Tarantulas', 2),
            ('Grouches', 1),
            ('Lions', 0)
        ]

        results = rankings.sort_results(input)
        self.assertEqual(results, expected)

    def test_same_score_names_alphabetized(self):
        """ Test that teams with same score will be sorted alphabetically
            by name.
        """
        input = {
            'Zeppelins': 1,
            'FC Awesome': 1,
            'Snakes': 1,
        }
        expected = [
            ('FC Awesome', 1),
            ('Snakes', 1),
            ('Zeppelins', 1)
        ]

        results = rankings.sort_results(input)
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
