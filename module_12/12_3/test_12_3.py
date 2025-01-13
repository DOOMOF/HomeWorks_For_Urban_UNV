import suit_12_3 as ST
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсы заморожены")
    def test_walk(self):
        runner = ST.Runner("Роман")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)


    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = ST.Runner("Игорь")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challange(self):
        runner1 = ST.Runner("Егор")
        runner2 = ST.Runner("Илья")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    all_result = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = ST.Runner("Усейн", speed=10)
        self.andrey = ST.Runner("Андрей", speed=9)
        self.nik = ST.Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for results in cls.all_result.values():
            print(results)
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_usein_and_nik(self):
        tournament = ST.Tournament(90, self.usein, self.nik)
        results = tournament.start()
        self.__class__.all_results['race_1'] = {place: str(runner) for place, runner in results.item()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_andrey_and_nik(self):
        tournament = ST.Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.__class__.all_results['race_2'] = {place: str(runner) for place, runner in results.item()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_usein_andrey_nik(self):
        tournament = ST.Tournament(90, self.andrey, self.usein, self.nik)
        results = tournament.start()
        self.__class__.all_results['race_3'] = {place: str(runner) for place, runner in results.item()}
        self.assertTrue(results[max(results.keys())] == "Ник")


Suite_ST = unittest.TestSuite()
Suite_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
Suite_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(Suite_ST)


