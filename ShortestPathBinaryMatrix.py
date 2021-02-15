
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] == 1:
            return -1
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        queue = [(0, 0, 1)]
        while queue:
            size = len(queue)
            x, y, steps = queue.pop(0)
            if x == y == n - 1:
                return steps
            for dx, dy in direction:
                if 0 <= x + dx < n and 0 <= y + dy < n and grid[x + dx][y + dy] == 0:
                    grid[x + dx][y + dy] = 1
                    queue.append((x + dx, y + dy, steps + 1))
        return steps








