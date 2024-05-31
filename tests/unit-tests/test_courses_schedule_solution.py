from unittest import TestCase
from courses_schedule_solution import Solution

class TestSolution(TestCase):
    def setUp(self) -> None:
        self.sut = Solution()

    def test_can_finish_exemple_1(self):

        '''
            Тест проверяет, что курсы могут быть завершены при валидных входных данных
        '''

        numCourses = 2
        prerequisites = [[0, 1]]
        self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_exemple_2(self):

        '''
            Тест проверяет, что курсы не могут быть завершены при входных данных
        '''

        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        self.assertFalse(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_numCourses_count_valid(self):

        '''
            тест проверяет валидные значения курсов
        '''

        data=[
            (1, []),
            (2, [[1, 0]]),
            (1999, [[1,0]]),
            (2000, [[1,0]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_numCourses_count_invalid(self):

        '''
            Тест проверяет, что при невалидных значениях курса выдаст ValueError
        '''

        data=[
            (0, []),
            (2001, [[1,0]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(ValueError):
                    self.sut.canFinish(numCourses, prerequisites)
    def test_can_finish_numCourses_isNumber(self):

        '''
            Тест проверяет, что если число курсов имеет тип не Int то выведет ошибку TypeError
        '''

        data = [
            ('0', []),
            ([], []),
            (None, []),
            (0.5, []),
            (True, []),
            ({'numCourses': 1}, []),
            (b'1', []),
            ((1,), []),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(TypeError):
                    self.sut.canFinish(numCourses, prerequisites)

    def test_can_finish_prerequisites_length_valid(self):

        '''
            Тест проверяет валидность длины массива условий прохождения курсов
        '''

        data=[
            (1, []),
            (2, [[1, 0]]),
            # (2000, [[i % 5000, (i - 1) % 5000] for i in range(1, 5000)]),
            # (2000, [[i % 5001, (i - 1) % 5001] for i in range(1, 5001)]),
            # ошибка maximum recursion depth exceeded in comparison при длине больше num, поэтому проверить пограничные значения 4999 и 5000 невозможно BugReport!
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites_length=len(prerequisites)):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_prerequisites_length_invalid(self):

        '''
            Тест проверяет, что при невалидной длине массива условий прохождения курсов выведет ValueError
        '''

        data=[
            (2000, [[i % 2000, (i - 1) % 2000] for i in range(0, 5001)]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites_length=len(prerequisites)):
                with self.assertRaises(ValueError):
                    self.sut.canFinish(numCourses, prerequisites)
    def test_can_finish_prerequisites_i_length_valid(self):

        '''
            Тест проверяет, что элемент массива условий имеет только 2 курса
        '''


        data=[
            (2, [[1, 0]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_prerequisites_i_length_inValid(self):

        '''
            Тест проверяет, что при невалидных длинах элемента массива условий выведет ValueError
        '''

        data=[
            (2, [[1]]),
            (3, [[1,2,3]])
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(ValueError):
                    self.sut.canFinish(numCourses, prerequisites)

    def test_can_finish_prerequisites_i_isArrayOfNumbers(self):

        '''
            Тест проверяет, что если элементы массива условий не являются числами [[int,int]],
            то выведется ошибка TypeError
        '''

        data = [
            (2, [['0','0']]),
            (2, [[[],[]]]),
            (2, [[None, None]]),
            (2, [[0.5, 0.3]]),
            (2, [[True, True]]),
            (2, [[b'1', b'1']]),
            (2, [[{'numCourses': 1}, {'numCourses': 1}]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(TypeError):
                    self.sut.canFinish(numCourses, prerequisites)

    def test_can_finish_prerequisites_i_ai_bi_valid(self):

        '''
            Тест проверяет, что элементы элемента массива условий соотвествуют требованию  0 <=ai, bi<numCourses
        '''

        data = [
            (2, [[1, 0]]),
            (5, [[4, 0]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_prerequisites_i_ai_bi_inValid(self):

        '''
            Тест проверяет, что если элементы элемента массива не соотвествуют требованию  0 <=ai, bi<numCourses,
             то выведется ValueError
        '''

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

        '''
            Тест проверяет, все пары в элементах массива условий уникальны
        '''

        data = [
            (3, [[1, 0], [2, 1]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                self.assertTrue(self.sut.canFinish(numCourses, prerequisites))

    def test_can_finish_all_pairs_prerequisites_i_UnUnique(self):

        '''
            Тест проверяет, что если  есть неуникальная пара в элементах массива условий,
            то выведется ошибка ValueError
        '''

        data = [
            (2, [[1, 0], [1, 0]]),
        ]
        for numCourses, prerequisites in data:
            with self.subTest(numCourses=numCourses, prerequisites=prerequisites):
                with self.assertRaises(ValueError):
                    self.sut.canFinish(numCourses, prerequisites)