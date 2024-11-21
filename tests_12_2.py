import task2
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = task2.Runner('Усэйн', 10)
        self.run2 = task2.Runner('Андрей', 9)
        self.run3 = task2.Runner('Ник', 3)

    def test_start1(self):
        self.start1 = task2.Tournament(90, self.run1, self.run3)
        self.all_results.update(self.start1.start())
        print (self.all_results)
        a = max(self.all_results.keys())
        b = self.all_results.get(a)
        self.assertTrue(b, self.run3)

    def test_start2(self):
        self.start2 = task2.Tournament(90, self.run2, self.run3)
        self.all_results.update(self.start2.start())
        print(self.all_results)
        a = max(self.all_results.keys())
        b = self.all_results.get(a)
        self.assertTrue(b, self.run3)

    def test_start3(self):
        self.start3 = task2.Tournament(90, self.run1, self.run2, self.run3)
        self.all_results.update(self.start3.start())
        print(self.all_results)
        c = max(self.all_results.keys())
        d = self.all_results.get(c)
        self.assertTrue(d, self.run3)
