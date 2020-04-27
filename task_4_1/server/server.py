import grpc
import threading
import random
import datetime
import sys
import os
import pathlib
import time

from concurrent import futures

sys.path.append(os.path.join(pathlib.Path().absolute(), 'gen'))
import match_pb2 as Match
import match_pb2_grpc as Match_grpc


tournaments = ["DreamHack", "ESLOne", "IntelExtremeMasters"]

teams = ["Astralis", "NiP", "FaZe", "G2", "fnatic", "mousesports", "AGO", "Natus Vincere"]

players = {
    "Astralis" : ["Xyp9x", "dupreeh", "gla1ve", "device", "Magisk"],
    "NiP" : ["twist", "Lekr0", "REZ", "nawwk", "Plopski"],
    "FaZe" : ["olofmeister", "NiKo", "rain", "coldzera", "broky"],
    "G2" : ["JaCkz", "huNter-", "kennyS", "AmaNEk", "nexa"],
    "fnatic" : ["flusha", "JW", "KRIMZ", "Golden", "Brollan"],
    "mousesports" : ["karrigan", "chrisJ", "woxic", "frozen", "ropz"],
    "AGO" : ["oskarish", "Furlan", "GruBy", "mhL", "F1KU"],
    "Natus Vincere" : ["flamie", "s1mple", "electronic", "Boombl4", "Perfecto"]
}

class Game():
    global players

    def __init__(self, tournament, teams):
        self.tournament = tournament
        self.first_team = teams[0]
        self.second_team = teams[1]
        self.score = str(self.first_team.score) + ":" + str(self.second_team.score)
        self.round = self.first_team.score + self.second_team.score
        self.last_win_cond = Match.WinConditions.Name(random.randrange(3))

    def getScore(self):
        return Match.ScoreReply(
            first_team=self.first_team,
            second_team=self.second_team,
            score=self.score,
            win_condition=self.last_win_cond,
            datetime=str(datetime.datetime.now()).split('.')[0]
        )

    def changeTeams(self, teams):
        self.first_team = teams[0]
        self.second_team = teams[1]
        self.score = str(self.first_team.score) + ":" + str(self.second_team.score)
        self.last_win_cond = Match.WinConditions.Name(random.randrange(3))

    def getCtWinCond(self):
        return Match.WinConditions.Name(random.randrange(3))

    def getTTWinCond(self):
        win_id = random.randrange(1)
        if win_id == 1:
            win_id = 3
        return Match.WinConditions.Name(win_id)

    def getAlivePlayers(self, team, amount):
        players_ids = random.sample(range(0, 4), amount)
        return list(players[team.name][i] for i in players_ids)

    def updateWinningScore(self, team):
        team.score = team.score + 1
        team.alive_members[:] = self.getAlivePlayers(team, random.randrange(1, 5))
        if team.is_ct:
            self.last_win_cond = self.getCtWinCond()
        else:
            self.last_win_cond = self.getTTWinCond()

    def updateLosingScore(self, team):
        if self.last_win_cond == "KILLED_ALL":
            team.alive_members[:] = []
        else:
            team.alive_members[:] = self.getAlivePlayers(team, random.randrange(0, 5))

    def updateSites(self):
        if self.round == 15:
            self.first_team.is_ct = not self.first_team.is_ct
            self.second_team.is_ct = not self.second_team.is_ct

    def updateStats(self):
        self.score = str(self.first_team.score) + ":" + str(self.second_team.score)
        self.round = self.first_team.score + self.second_team.score
        self.updateSites()

    def getWinner(self):
        winner_id = random.randrange(100)
        if winner_id < 50:
            self.updateWinningScore(self.first_team)
            self.updateLosingScore(self.second_team)
        else:
            self.updateWinningScore(self.second_team)
            self.updateLosingScore(self.first_team)
        self.updateStats()

    def checkEndGame(self):
        if self.first_team.score == 15 and self.second_team.score == 15:
            return True
        elif self.first_team.score == 16:
            return True
        elif self.second_team.score == 16:
            return True
        else:
            return False


class Listener(Match_grpc.ScoreNotificationsServicer):
    def __init__(self, server, games):
        self.server = server
        self.games = games

    def SubscribeToTournament(self, request, context):
        if not (request.tournament in self.games):
            print("There is no tournament " + request.tournament)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Wrong tournament name")
            yield Match_grpc.ScoreDetails()
            return

        self.addListener(request.tournament)
        while True:
            yield self.games[request.tournament].getScore()
            time.sleep(request.frequency)

    def addListener(self, tournament):
        print("\nNew subscriber for " + tournament + "\n")
        Match_grpc.add_ScoreNotificationsServicer_to_server(Listener(self.server, self.games), self.server)

def genTeams(is_beginning=False):
    global teams
    global players
    team_id = random.sample(range(0, 7), 2)

    first_team = Match.Team(
        name=teams[team_id[0]],
        score=0 if is_beginning else random.randrange(14),
        is_ct=True,
        alive_members=players[teams[team_id[0]]]
    )

    second_team = Match.Team(
        name=teams[team_id[1]],
        score=0 if is_beginning else random.randrange(14),
        is_ct=False,
        alive_members=players[teams[team_id[1]]]
    )

    return [first_team, second_team]

def genGames():
    global tournaments
    games = {}
    for tournament in tournaments:
        games[tournament] = Game(tournament, genTeams())
    return games

def updateScore(games):
    global tournaments
    while True:
        print()
        for tournament in tournaments:
            print("Updating score for " + tournament)
            games[tournament].getWinner()
            if games[tournament].checkEndGame():
                games[tournament].changeTeams(genTeams(True))
            else:
                pass
        time.sleep(random.randrange(10))

def serve(games):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Match_grpc.add_ScoreNotificationsServicer_to_server(Listener(server, games), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    try:
        while True:
            print("Server is still working")
            time.sleep(30)
    except KeyboardInterrupt:
        server.stop(0)
    server.wait_for_termination()

def main():
    games = genGames()
    threading.Thread(target=serve, args=(games, )).start()
    threading.Thread(target=updateScore, args=(games, )).start()

if __name__ == "__main__":
    main()