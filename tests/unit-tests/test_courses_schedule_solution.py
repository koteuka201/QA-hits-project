from unittest import TestCase
from courses_schedule_solution import Solution

class TestSolution(TestCase):
    def setUp(self) -> None:
        self.sut = Solution()

    def test_can_finish_exemple_1(self):
        numCourses = 2
        prerequisites = [[0, 1]]
        self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_exemple_2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        self.assertFalse(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_numCourses_count_valid(self):
        data=[
            (1, []),
            (2, [[1, 0]]),
            (1999, [[i, i - 1] for i in range(1, 1999)]),
            (2000, [[i, i - 1] for i in range(1, 2000)]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_numCourses_count_invalid(self):
        data=[
            (0, []),
            (2001, [[i, i - 1] for i in range(1, 2001)]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(ValueError):
                    self.sut.canFinish(numCourses, prerequisites)
    def test_can_finish_numCourses_isNumber(self):
        data = [
            ('0', []),
            ([], []),
            (None, []),
            (0.5, []),
            (True, []),
            ((1,), []),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(TypeError):
                    self.sut.canFinish(numCourses, prerequisites)

    def test_can_finish_prerequisites_length_valid(self):
        data=[
            (1, []),
            (2, [[1, 0]]),
            (2000, [[i % 2000, (i - 1) % 2000] for i in range(1, 2000)]),
            # ошибка maximum recursion depth exceeded in comparison при длине больше num (баг репорт мб сделать хз)
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites_length=len(prerequisites)):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_prerequisites_i_length_valid(self):
        data=[
            (2, [[1, 0]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_prerequisites_i_length_inValid(self):
        data=[
            (2, [[1]]),
            (3, [[1,2,3]])
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(ValueError):
                    self.sut.canFinish(numCourses, prerequisites)

    def test_can_finish_prerequisites_i_isArrayOfNumbers(self):
        data = [
            (2, [['0','0']]),
            (2, [[[],[]]]),
            (2, [[None, None]]),
            (2, [[0.5, 0.5]]),
            (2, [[True, True]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(TypeError):
                    self.sut.canFinish(numCourses, prerequisites)

    def test_can_finish_prerequisites_i_ai_bi_valid(self):
        data = [
            (2, [[1, 0]]),
            (5, [[4, 0]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_prerequisites_i_ai_bi_inValid(self):
        data = [
            (2, [[-1,0]]),
            (2, [[2, 0]]),
            (2, [[3, 0]]),

        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(ValueError):
                    self.sut.canFinish(numCourses, prerequisites)

    def test_can_finish_all_pairs_prerequisites_i_unique(self):
        data = [
            (3, [[1, 0], [2, 1]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_all_pairs_prerequisites_i_UnUnique(self):
        data = [
            (2, [[1, 0], [1, 0]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(ValueError):
                    self.sut.canFinish(numCourses, prerequisites)
    '''
        1 <= numCourses <= 2000
            1, 2, 0
            2000, 2001, 1999 !!!
        0 <= prerequisites.length <= 5000
            0, 1
            5000, 5001, 4999 !!!
        prerequisites[i].length == 2
            1, 2, 3 !!!
        0 <= ai, bi < numCourses
            ai, bi = -1, ai, b1 = 0, ai, bi = 1
            ai, bi = numCourses-1, ai, b1 = numCourses, ai, bi = numCourses-1 !!!
        All the pairs prerequisites[i] are unique.
            [0,1]-true, [0,0]-false

    '''