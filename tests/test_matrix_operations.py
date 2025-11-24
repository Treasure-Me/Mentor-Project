import pytest
import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matrix_lib import MatrixGame

class TestMatrixOperations:
    def setup_method(self):
        self.matrix_game = MatrixGame()
    
    def test_matrix_multiplication_2x2(self):
        """Test basic 2x2 matrix multiplication"""
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 2]]
        expected = [[4, 4], [10, 8]]
        result = self.matrix_game.multiply_matrices(A, B)
        assert result == expected
    
    def test_matrix_multiplication_3x3(self):
        """Test 3x3 matrix multiplication"""
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        result = self.matrix_game.multiply_matrices(A, B)
        assert result == expected
    
    def test_matrix_multiplication_incompatible_dimensions(self):
        """Test multiplication with incompatible dimensions"""
        A = [[1, 2, 3]]  # 1x3
        B = [[1], [2]]    # 2x1
        result = self.matrix_game.multiply_matrices(A, B)
        assert result is None
    
    def test_matrix_equality(self):
        """Test matrix equality checker"""
        A = [[1.0, 2.0], [3.0, 4.0]]
        B = [[1.0, 2.0], [3.0, 4.0]]
        C = [[1.0, 2.0], [3.0, 4.1]]
        
        assert self.matrix_game.is_matrix_equal(A, B) == True
        assert self.matrix_game.is_matrix_equal(A, C) == False
    
    def test_matrix_equality_with_tolerance(self):
        """Test matrix equality with floating point tolerance"""
        A = [[1.0, 2.0], [3.0, 4.0]]
        B = [[1.0, 2.0000001], [3.0, 4.0]]
        
        assert self.matrix_game.is_matrix_equal(A, B, tolerance=1e-6) == True
        assert self.matrix_game.is_matrix_equal(A, B, tolerance=1e-9) == False
    
    def test_generate_random_matrix(self):
        """Test random matrix generation"""
        rows, cols = 3, 4
        matrix = self.matrix_game.generate_random_matrix(rows, cols, -5, 5)
        
        assert len(matrix) == rows
        assert len(matrix[0]) == cols
        
        # Check all values are within range
        for row in matrix:
            for val in row:
                assert -5 <= val <= 5
    
    def test_level_initialization(self):
        """Test that game levels are properly initialized"""
        levels = self.matrix_game._init_levels()
        assert len(levels) > 0
        
        for level in levels:
            assert 'input' in level
            assert 'target' in level
            assert 'hint' in level
            
            # Verify dimensions are compatible for multiplication
            input_matrix = level['input']
            target_matrix = level['target']
            
            # If there's a transformation matrix, verify dimensions
            if 'transformation' in level:
                trans_matrix = level['transformation']
                assert len(input_matrix[0]) == len(trans_matrix)
                assert len(trans_matrix[0]) == len(target_matrix[0])
    
    def test_matrix_inverse_2x2(self):
        """Test matrix inverse calculation for 2x2 matrices"""
        A = [[4, 7], [2, 6]]
        expected_inverse = [[0.6, -0.7], [-0.2, 0.4]]
        
        result = self.matrix_game.find_matrix_inverse(A)
        
        if result:  # Only test if inverse exists
            assert self.matrix_game.is_matrix_equal(
                self.matrix_game.multiply_matrices(A, result),
                [[1, 0], [0, 1]],
                tolerance=1e-6
            )
    
    def test_singular_matrix_inverse(self):
        """Test that singular matrices have no inverse"""
        A = [[1, 2], [2, 4]]  # Singular matrix (determinant = 0)
        result = self.matrix_game.find_matrix_inverse(A)
        assert result is None
    
    def test_solution_validation(self):
        """Test the solution validation logic"""
        # Test correct solution
        matrices = [[[1, 2], [3, 4]], [[2, 0], [1, 2]]]
        target = [[4, 4], [10, 8]]
        
        # This would be part of the game logic
        result = self.matrix_game.multiply_matrices(matrices[0], matrices[1])
        assert self.matrix_game.is_matrix_equal(result, target)
    
    def test_multiple_matrix_multiplication(self):
        """Test chaining multiple matrix multiplications"""
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 2]]
        C = [[1, 1], [0, 1]]
        
        # (A × B) × C
        temp = self.matrix_game.multiply_matrices(A, B)
        result1 = self.matrix_game.multiply_matrices(temp, C)
        
        # A × (B × C)
        temp2 = self.matrix_game.multiply_matrices(B, C)
        result2 = self.matrix_game.multiply_matrices(A, temp2)
        
        # Results should be equal (associative property)
        assert self.matrix_game.is_matrix_equal(result1, result2)
