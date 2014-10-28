import fileinput
import sys
from collections import defaultdict
from operator import itemgetter


def split_games(game_list):
    """ Split an input text file with one game per line into a list
        of games.

        Sample input:
        Lions 3, Snakes 3
        Tarantulas 1, FC Awesome 0
        Lions 1, FC Awesome 1
        Tarantulas 3, Snakes 1
        Lions 4, Grouches 0

        Output:
        [
            ['Lions 3', 'Snakes 3'],
            ['Tarantulas 1', 'FC Awesome 0'],
            ['Lions 1', 'FC Awesome 1'],
            ['Tarantulas 3', 'Snakes 1'],
            ['Lions 4', 'Grouches 0']
        ]
    """
    games = []
    for line in game_list:
        game = line.rstrip().split(', ')
        games.append(game)

    return games


def compare_scores(games):
    """ Assign rankings points to teams based on game outcome.
        Win => 3 points
        Loss => 0 points
        Draw => 1 point per team
    """
    results = defaultdict(int)
    for game in games:
        result1 = game[0].rsplit(',', 1)
        team1 = result1[0].rsplit(' ', 1)
        team1_name = team1[0]
        team1_score = team1[1]

        result2 = game[1].rsplit(',', 1)
        team2 = result2[0].rsplit(' ', 1)
        team2_name = team2[0]
        team2_score = team2[1]

        if team1_score > team2_score:
            team1_increment = 3
            team2_increment = 0
        elif team1_score < team2_score:
            team1_increment = 0
            team2_increment = 3
        elif team1_score == team2_score:
            team1_increment = 1
            team2_increment = 1

        results[team1_name] += team1_increment
        results[team2_name] += team2_increment

    return results


def sort_results(results):
    """ Sort results first by score (descending), then by team name
        (ascending), if multiple teams have the same score.

        Sorting twice is specifically condoned by the Python documentation as a
        performant solution for complex sorts, since sorts are guaranteed to be
        stable.  See:
        http://wiki.python.org/moin/HowTo/Sorting#Sort_Stability_and_Complex_Sorts
    """
    s = sorted(results.items(), key=itemgetter(0))
    rankings = sorted(s, key=itemgetter(1), reverse=True)

    return rankings


def generate_rankings():
    """ Generate rankings table.  """
    games = split_games(fileinput.input())
    results = compare_scores(games)
    rankings = sort_results(results)

    prev_score = rankings[0][1]
    current_rank = 1
    teams_with_current_rank = 0

    for r in rankings:
        team = r[0]
        score = r[1]

        if score == prev_score:
            # Teams have same rank
            rank = current_rank
            teams_with_current_rank += 1
        elif score < prev_score:
            # Team rank increases by number of teams w/previous rank
            prev_score = score
            current_rank += teams_with_current_rank
            rank = current_rank
            teams_with_current_rank = 1

        output = "%s. %s: %s \n" % (rank, team, score)
        sys.stdout.write(output)


if __name__ == '__main__':
    generate_rankings()
