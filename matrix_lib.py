import math
import random

class MatrixGame:
    def __init__(self):
        self.levels = self._init_levels()
    
    def _init_levels(self):
        """
        DESIGN GAME LEVELS with increasing difficulty
        """
        return [
            {   # Level 1: Identity matrix (A × I = A)
                "name": "Level 1: No Transformation",
                "input": [[1, 2], [3, 4]],
                "target": [[1, 2], [3, 4]],
                "hint": "What matrix when multiplied gives you the same matrix back?",
                "solution": [[1, 0], [0, 1]]
            },
            {   # Level 2: Scale by 2
                "name": "Level 2: Double Trouble", 
                "input": [[1, 2], [3, 4]],
                "target": [[2, 4], [6, 8]],
                "hint": "Try multiplying each element by 2",
                "solution": [[2, 0], [0, 2]]
            },
            {   # Level 3: Tripler (Scaling by 3)
                "name": "Level 3: Trifector", 
                "input": [[1, 2], [3, 4]],
                "target": [[3, 6], [9, 12]],
                "hint": "Like the last level, but matching the name of this level.",
                "solution": [[3, 0], [0, 3]]
            },
            {   # Level 4: 90 Degree Rotation (Complex 2x2)
                "name": "Level 4: Quad to Victory", 
                "input": [[1, 2], [3, 4]],
                "target": [[-2, 1], [-4, 3]],
                "hint": "Think in four quadrants. How do you rotate a matrix by 90 degrees?",
                "solution": [[0, 1], [-1, 0]]
            },
            {   # Level 5: 3x3 Introduction (Scale by 5)
                "name": "Level 5: PenTester", 
                "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                "target": [[5, 10, 15], [20, 25, 30], [35, 40, 45]],
                "hint": "Welcome to 3x3 matrices! Can you penetrate the system by scaling everything by 5?",
                "solution": [[5, 0, 0], [0, 5, 0], [0, 0, 5]]
            },
            {   # Level 6: 3x3 Reflection (Swap left and right columns)
                "name": "Level 6: The Witches Hex", 
                "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                "target": [[3, 2, 1], [6, 5, 4], [9, 8, 7]],
                "hint": "The witch cast a reflection spell! Swap the left and right columns.",
                "solution": [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
            },
            {   # Level 7: 2x2 Multiple Transformations (Scale Y, Invert X)
                "name": "Level 7: HeptaZone", 
                "input": [[1, 2], [3, 4]],
                "target": [[-1, 4], [-3, 8]],
                "hint": "Combine operations: Make the first column negative, and double the second column.",
                "solution": [[-1, 0], [0, 2]]
            },
            {   # Level 8: 3x3 Destructive Transformation (Zero out a column, scale rest)
                "name": "Level 8: OctaZone", 
                "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                "target": [[2, 0, 6], [8, 0, 12], [14, 0, 18]],
                "hint": "Eradicate the middle column completely, and double the outer edges.",
                "solution": [[2, 0, 0], [0, 0, 0], [0, 0, 2]]
            }
        ]
    
    def multiply_matrices(self, A, B):
        """
        IMPLEMENT MATRIX MULTIPLICATION ALGORITHM
        
        Matrix Multiplication Formula:
        If A is m×n and B is n×p, then result C is m×p where:
        C[i][j] = sum of (A[i][k] * B[k][j]) for k = 0 to n-1
        
        Step-by-step for 2x2 matrices:
        A = [[a, b],    B = [[e, f],    Result = [[ae+bg, af+bh],
             [c, d]]         [g, h]]             [ce+dg, cf+dh]]
        
        Algorithm:
        1. Check if multiplication is valid: cols_A must equal rows_B
        2. Create empty result matrix with dimensions: rows_A × cols_B
        3. For each row i in A:
           For each column j in B:
               sum = 0
               For each element k in row i of A (and column k of B):
                   sum += A[i][k] * B[k][j]
               Result[i][j] = sum
        
        Example:
        A = [[1, 2],   B = [[5, 6],
             [3, 4]]        [7, 8]]
             
        Result[0][0] = (1×5) + (2×7) = 5 + 14 = 19
        Result[0][1] = (1×6) + (2×8) = 6 + 16 = 22
        Result[1][0] = (3×5) + (4×7) = 15 + 28 = 43  
        Result[1][1] = (3×6) + (4×8) = 18 + 32 = 50
        
        Final result: [[19, 22],
                      [43, 50]]
        
        Parameters:
        A: First matrix (list of lists)
        B: Second matrix (list of lists)
        
        Returns:
        Result matrix if valid, None if dimensions incompatible
        """
        # TODO: Implement following the algorithm above
        rows_a = len(A)
        cols_a = len(A[0])
        rows_b = len(B)
        cols_b = len(B[0])

        if cols_a != rows_b:
            return None

        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += A[i][k] * B[k][j]

        return result
    
    def generate_random_matrix(self, rows, cols, min_val=-5, max_val=5):
        """
        GENERATE RANDOM MATRICES for the game palette
        
        This function creates random matrices that players can use to solve puzzles.
        
        Algorithm:
        1. Create an empty list for the matrix
        2. For each row from 0 to rows-1:
           - Create an empty list for the current row
           - For each column from 0 to cols-1:
               - Generate random integer between min_val and max_val
               - Add to current row
           - Add completed row to matrix
        
        Example:
        generate_random_matrix(2, 3, -2, 2) might return:
        [[1, -2, 0],
         [2, 1, -1]]
        
        Parameters:
        rows: Number of rows in the matrix
        cols: Number of columns in the matrix  
        min_val: Minimum value for matrix elements
        max_val: Maximum value for matrix elements
        
        Returns:
        Random matrix with specified dimensions and value range
        """
        # TODO: Implement following the algorithm above
        matrix = []

        for row in range(rows):
            row_list = []
            for col in range(cols):
                rand_int = random.randint(min_val, max_val)
                row_list.append(rand_int)
            matrix.append(row_list)

        return matrix
    
    def is_matrix_equal(self, A, B, tolerance=1e-6):
        """
        CHECK IF TWO MATRICES ARE EQUAL (within floating-point tolerance)
        
        Due to floating-point arithmetic, we need to check if matrices are 
        "close enough" rather than exactly equal.
        
        Algorithm:
        1. Check if both matrices have same number of rows
        2. Check if both matrices have same number of columns  
        3. For each position (i, j) in the matrices:
           - If |A[i][j] - B[i][j]| > tolerance, return False
        4. If all elements are within tolerance, return True
        
        Example:
        A = [[1.0, 2.0],   B = [[1.000001, 2.0],   → Equal (within 1e-6)
             [3.0, 4.0]]        [3.0, 4.0]]
             
        A = [[1.0, 2.0],   B = [[1.1, 2.0],        → Not equal
             [3.0, 4.0]]        [3.0, 4.0]]
        
        Parameters:
        A: First matrix to compare
        B: Second matrix to compare  
        tolerance: Maximum allowed difference between elements
        
        Returns:
        True if matrices are equal within tolerance, False otherwise
        """
        # TODO: Implement following the algorithm above
        if len(A) != len(B):
            return False
            
        if len(A) == 0:
            return True
            
        if len(A[0]) != len(B[0]):
            return False
            
        for i in range(len(A)):
            for j in range(len(A[0])):
                difference = abs(A[i][j] - B[i][j])
                
                if difference > tolerance:
                    return False

        return True
    
    def find_matrix_inverse(self, A):
        """
        BONUS CHALLENGE: FIND MATRIX INVERSE (for advanced levels)
        
        The inverse of matrix A (denoted A⁻¹) satisfies: A × A⁻¹ = I
        where I is the identity matrix.
        
        For 2x2 matrices, the inverse formula is:
        If A = [[a, b],
                [c, d]]
                
        Then A⁻¹ = (1/determinant) × [[d, -b],
                                     [-c, a]]
                                     
        Where determinant = (a×d - b×c)
        
        Algorithm for 2x2:
        1. Calculate determinant = a*d - b*c
        2. If determinant == 0, matrix has no inverse (return None)
        3. Return [[d/det, -b/det],
                  [-c/det, a/det]]
        
        Example:
        A = [[4, 7],
             [2, 6]]
             
        determinant = (4×6) - (7×2) = 24 - 14 = 10
        A⁻¹ = [[6/10, -7/10],
               [-2/10, 4/10]] = [[0.6, -0.7],
                                 [-0.2, 0.4]]
        
        Parameters:
        A: 2x2 matrix to invert
        
        Returns:
        Inverse matrix if it exists, None if matrix is not invertible
        """
        # TODO: Implement following the algorithm above (BONUS)
        if len(A) != 2 or len(A[0]) != 2:
            raise ValueError("This function only supports 2x2 matrices.")

        # Extract the values to perfectly match the formula's a, b, c, d
        a = A[0][0]
        b = A[0][1]
        c = A[1][0]
        d = A[1][1]

        # 1. Calculate determinant = a*d - b*c
        determinant = (a * d) - (b * c)

        # 2. If determinant == 0, matrix has no inverse (return None)
        # We use abs() < 1e-9 here just in case the inputs are floating-point 
        # numbers that get incredibly close to zero without technically being exactly 0.0
        if abs(determinant) < 1e-9:
            return None

        # 3. Return the calculated inverse matrix
        return [
            [d / determinant, -b / determinant],
            [-c / determinant, a / determinant]
        ]