import task
import unittest

class RunnerTest(unittest.TestCase):
    iz_frozen = False

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.walk1 = task.Runner('1')
        for i in range(10):
            self.walk1.walk()
        self.assertEqual(self.walk1.distance, 50)

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.run2 = task.Runner('2')
        for i in range(10):
            self.run2.run()
        self.assertEqual(self.run2.distance, 100)

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.chal3 = task.Runner('3')
        self.chal4 = task.Runner('4')
        for i in range(10):
            self.chal3.run()
            self.chal4.walk()
        self.assertNotEqual(self.chal3.distance, self.chal4.distance)

if __name__ == '__main__':
    unittest.main()
