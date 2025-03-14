from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()

        def bfs(row: int, col: int) -> None:
            q = deque([(row, col)])

            while q:
                row, col = q.popleft()
                if ((row, col) in visit or row not in range(m) 
                    or col not in range(n) or grid[row][col] != "1"):
                    continue
                visit.add((row, col))
                q.append((row+1, col))
                q.append((row-1, col))
                q.append((row, col+1))
                q.append((row, col-1))
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    res += 1
        
        return res

# Time: O(m*n)
# Space: O(m*n)