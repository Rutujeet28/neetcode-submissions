class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col] == '1':
                    islands += 1
                    queue = deque()
                    queue.append((row, col))

                    grid[row][col] = '0'

                    while queue:
                        currRow, currCol = queue.popleft()

                        for dr, dc in dirs:
                            newRow = currRow + dr
                            newCol = currCol + dc

                            if (0 <= newRow < rows and
                                0 <= newCol < cols and grid[newRow][newCol] == '1'):

                                grid[newRow][newCol] = '0'
                                queue.append((newRow, newCol))

        return islands