import unittest
import tests_12_1
import tests_12_2

task_test = unittest.TestSuite()

task_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
task_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(task_test)
