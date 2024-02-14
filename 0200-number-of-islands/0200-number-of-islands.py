class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

       
        #상하좌우
        rows, cols = len(grid), len(grid[0])
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0": continue
                
                grid[row][col] = "0"

                ans+=1

                stack = [[row,col]]
                while stack:
                    y, x = stack.pop()

                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if ny >= 0 and ny < rows and nx >= 0 and nx < cols:
                            if grid[ny][nx] == "0": continue
                            grid[ny][nx] = "0"
                            stack.append([ny,nx])
        return ans