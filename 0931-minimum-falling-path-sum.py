class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        memory = [0] * length
        for i in range(N-1,-1,-1):
            next = [0] * length
            for j in range(length):
                Min = float('inf')
                if j - 1 > -1:
                    Min = min(memory[j - 1], Min)
                if j + 1 < N:
                    Min = min(memory[j + 1], Min)
                Min = min(memory[j], Min)
                next[j] = Min + matrix[i][j]
            memory = next
        return min(memory)
