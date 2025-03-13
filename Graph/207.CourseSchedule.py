from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visited = set()

        def dfs(course: int) -> bool:
            if course in visited:
                return False
            
            if course not in graph:
                return True
            
            visited.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            del graph[course]
            visited.remove(course)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True

# Time: O(n+p)
# Space: O(n+p)