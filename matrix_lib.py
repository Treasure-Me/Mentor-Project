class MatrixGame:
    def __init__(self):
        self.levels = self._init_levels()
    
    def _init_levels(self):
        """YOU COMPLETE: Define game levels with increasing difficulty"""
        return [
            {   # Level 1: 2x2 * 2x2 = 2x2
                "input": [[1, 2], [3, 4]],
                "target": [[7, 10], [15, 22]],
                "hint": "Find B such that A × B = C"
            }
            # MORE LEVELS - THEY DESIGN 8-10 PROGRESSIVELY HARDER ONES
        ]
    
    def multiply_matrices(self, A, B):
        """
        CHALLENGE 1: Implement matrix multiplication
        Rules: 
        - If cols_A != rows_B, return None (invalid)
        - Result[i][j] = sum(A[i][k] * B[k][j]) for k in range(cols_A)
        """
        # TODO: Implement this
        pass
    
    def generate_random_matrix(self, rows, cols, min_val=-5, max_val=5):
        """
        CHALLENGE 2: Generate random matrices for the game
        """
        # TODO: Implement
        pass
    
    def is_matrix_equal(self, A, B, tolerance=1e-6):
        """
        CHALLENGE 3: Check if two matrices are equal (within tolerance)
        """
        # TODO: Implement
        pass
    
    def find_matrix_inverse(self, A):
        """
        BONUS CHALLENGE: Implement matrix inverse for advanced levels
        """
        # TODO: Stretch goal
        pass
