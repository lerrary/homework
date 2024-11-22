import logging
import rt_with_exceptions as re
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            self.walk1 = re.Runner('1', -2)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                self.walk1.walk()
            self.assertEqual(self.walk1.distance, 50)

        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            self.run2 = re.Runner(2, 5)
            for i in range(10):
                self.run2.run()
            self.assertEqual(self.run2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
