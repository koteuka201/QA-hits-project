from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not isinstance(numCourses, int) or isinstance(numCourses, bool):
            raise TypeError('numCourses должно иметь тип int')

        if not isinstance(prerequisites, List) or not all(isinstance(course, list) and all(isinstance(item, int) and not isinstance(item, bool) for item in course) for course in prerequisites):
            raise TypeError('курсы в условия должны иметь тип int')

        seen_pairs = set()

        for course in prerequisites:
            ai, bi = course
            if not (0 <= ai < numCourses and 0 <= bi < numCourses):
                raise ValueError('0 <=ai, bi < numCourses')

            if tuple(course) in seen_pairs:
                raise ValueError('Пары курсов в массиве пар должны быть уникальны')
            else:
                seen_pairs.add(tuple(course))

        if len(prerequisites)>5000:
            raise ValueError(' len(prerequisites) <= 5000')

        if len(prerequisites):
            if len(prerequisites[0]) != 2:
                raise ValueError('Элемент массива условия должен иметь 2 курса')

        if numCourses < 1 or numCourses > 2000:
            raise ValueError('1<=numCourses <2000')

        if not prerequisites:
            return True

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
