class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        memory = matrix[-1] 
        # Start with the last row of the matrix
        for outer in range(length - 2, -1, -1):
            for inner in range(length):
                Min = float('inf')
                if inner - 1 > -1:
                    Min = min(memory[inner - 1], Min)
                if inner + 1 < length:
                    Min = min(memory[inner + 1], Min)
                Min = min(memory[inner], Min)
                memory[inner] = Min + matrix[outer][inner]
        return min(memory)
