import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = Runner("Усейн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_result.items():
            formatted_result = {place: str(runner) for place, runner in result.items()}
            print(formatted_result)

    def test_usein_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_result["Усейн и Ник"] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")

    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_result["Андрей и Ник"] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")

    def test_usein_andrey_nik(self):
        tournament =  Tournament(90, self.runner2, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_result["Усейн, Андрей и Ник"] = results
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == "Ник")


if __name__ == "__main__":
    unittest.main()






