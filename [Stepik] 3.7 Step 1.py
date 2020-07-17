# coding=utf-8
class footbal(object):
    team = str
    gameCount = 0
    wins = 0
    standoff = 0
    loses = 0
    score = 0

    def __init__(self, team, gameCount, wins, standoff, loses, score):
        self.team = team
        self.gameCount = gameCount
        self.wins = wins
        self.standoff = standoff
        self.loses = loses
        self.score = score


def teamInFootball(team, footballScore):
    for i in footballScore:
        if i.team == team:
            return False
    return True


gameCount = int(input())
userData = []
for i in range(gameCount):
    userData.append(input())
footballScore = []


def indexSearch(_team, _footballScore):
    for i in range(len(_footballScore)):
        if _footballScore[i].team == _team:
            return i


# Спартак;8;Локомотив;15
for game in userData:
    if teamInFootball(game.split(';')[0], footballScore):
        footballScore.append(object.__new__(footbal))
        footballScore[len(footballScore) - 1].team = game.split(';')[0]
    if teamInFootball(game.split(';')[2], footballScore):
        footballScore.append(object.__new__(footbal))
        footballScore[len(footballScore) - 1].team = game.split(';')[2]
    if int(game.split(';')[1]) > int(game.split(';')[3]):
        footballScore[indexSearch(game.split(';')[0], footballScore)].wins += 1
        footballScore[indexSearch(game.split(';')[2], footballScore)].loses += 1
    elif int(game.split(';')[1]) == int(game.split(';')[3]):
        footballScore[indexSearch(game.split(';')[0], footballScore)].standoff += 1
        footballScore[indexSearch(game.split(';')[2], footballScore)].standoff += 1
    else:
        footballScore[indexSearch(game.split(';')[0], footballScore)].loses += 1
        footballScore[indexSearch(game.split(';')[2], footballScore)].wins += 1
def countGameOfTeam(_team, _userData):
    counter = 0
    for i in _userData:
        if _team == i.split(';')[0]:
            counter += 1
        if _team == i.split(';')[2]:
            counter += 1
    return counter


for i in footballScore:
    score = i.wins * 3 + i.standoff
    print(i.team + ':' + str(countGameOfTeam(i.team, userData)), i.wins, i.standoff, i.loses, score)