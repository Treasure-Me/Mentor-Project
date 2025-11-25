# 📚 Matrix Basics Crash Course

## What is a Matrix?
A matrix is a grid of numbers arranged in rows and columns. Example:

```text
[1, 2]
[3, 4]  ← This is a 2x2 matrix (2 rows, 2 columns)
```

## Matrix Dimensions
- 2x2 matrix: 2 rows, 2 columns → [[a, b], [c, d]]

- 2x3 matrix: 2 rows, 3 columns → [[a, b, c], [d, e, f]]

- 3x2 matrix: 3 rows, 2 columns → [[a, b], [c, d], [e, f]]

## Matrix Multiplication Rules
Two matrices can only be multiplied if:

```text
Columns of first matrix = Rows of second matrix
```

- 2x2 × 2x2 → ✅ Valid (2=2)

- 2x3 × 3x2 → ✅ Valid (3=3)

- 2x2 × 3x2 → ❌ Invalid (2≠3)

## 🎯 Implementation Guide
### Step 1: Understand the Math
- Watch this Matrix [Multiplication Visualization](https://www.youtube.com/watch?v=XkY2DOUCWMU)

- Practice with pen and paper first

- Start with 2x2 matrices, then generalize

## Step 2: Test Your Understanding

```python
# Test case 1: Identity matrix
A = [[1, 2], [3, 4]]
I = [[1, 0], [0, 1]]
# A × I should equal A

# Test case 2: Simple multiplication  
A = [[1, 2], [3, 4]]
B = [[2, 0], [0, 2]]
# A × B should equal [[2, 4], [6, 8]]
```

## Step 3: Implementation Order
1. multiply_matrices - Core algorithm

2. is_matrix_equal - Testing helper

3. generate_random_matrix - Game content

4. _init_levels - Game design

5. find_matrix_inverse - Bonus challenge

## Step 4: Debugging Tips

```python
# Add debug prints to see what's happening
print(f"Multiplying: {A} × {B}")
print(f"Dimensions: {len(A)}x{len(A[0])} × {len(B)}x{len(B[0])}")
print(f"Result: {result}")
```