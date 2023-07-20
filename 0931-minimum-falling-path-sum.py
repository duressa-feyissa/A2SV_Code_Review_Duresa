class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        memory = matrix[-1]
        for i in range(length - 2, -1, -1):
            for j in range(length):
                Min = float('inf')
                if j - 1 > -1:
                    Min = min(memory[j - 1], Min)
                if j + 1 < length:
                    Min = min(memory[j + 1], Min)
                Min = min(memory[j], Min)
                memory[j] = Min + matrix[i][j]
        return min(memory)
