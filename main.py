from data import teams


# lambda team: team['score']

def parse_result(team):
    # win_msg = f"win: {team['result'].count('w')}".ljust(20)
    # lose_msg = f"lose: {team['result'].count('l')}".ljust(20)
    # draw_msg = f"draw: {team['result'].count('d')}".ljust(20)
    # team_name = f'name:{team["name"]}'.ljust(20)
    #
    # print(team_name + win_msg + draw_msg + lose_msg)
    return {
        'name': team['name'],
        'win': team['result'].count('w'),
        'draw': team['result'].count('d'),
        'lose': team['result'].count('l'),

    }


def calculate_score(team):
    score = (team['win'] * 3) + team['draw']
    team['score'] = score
    return team


def check_score(team):
    return team['score'] >= 13


# tmp_score_board = list()
# for team in teams:
#     tmp_score_board.append(parse_result(team))

tmp_score_board = list(map(parse_result, teams))

# score_board = list()
# for team in tmp_score_board:
#     score_board.append(calculate_score(team))

score_board = list(map(calculate_score, tmp_score_board))

# for team in score_board:
#     print(team)

# passed_teams = list()
# for team in score_board:
#     if check_score(team):
#         passed_teams.append(team)

# passed_teams = filter(check_score, score_board)
passed_teams = filter(lambda t: t['score'] >= 13, score_board)

for team in passed_teams:
    print(team)
