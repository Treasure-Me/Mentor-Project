# Project: Matrix Multiplier Mayhem - A Puzzle Game
**Core Concept**: Players must arrange and multiply matrices to transform "data streams" into desired outputs. It's like a circuit/pipeline puzzle but with matrix operations.


# Warning
- Do not under any circumstances touch the javascript file (game.js) and if ever you feel you should use AI to help you, be mindful of the changes you make to the html templates and consider both your CSS and Javascript, since your javascript remains the same every change you make should conform to it. Do not worry, you dont need to know any javascript. This just serves as a warning.

## Game Design
### The "Story"
- They are "Data Flow Engineers" who need to process raw data streams through transformation matrices to achieve target outputs.

## Game Mechanics
### Level 1-3: Learn the basics

- Given input matrix A and target output C

- Must find the correct transformation matrix B such that A × B = C

### Level 4-6: Multiple transformations

- Input A must go through TWO transformations: A × B × C = Target

- Players place matrices in the correct order

### Level 7+: The Inverse Challenge

- Given output C and transformation B, find the original input A (introducing matrix inverses)

## Test Setup

### 1. Install Test Dependencies
```bash
pip install -r requirements-test.txt
```
### 2. Run Test Commands

#### Run All Tests with Coverage
```bash
pytest --cov=matrix_game --cov-report=html
```
#### Run Specific Test Categories:

#### Backend Algorithm Tests

```bash
pytest test_matrix_operations.py -v
```

#### Flask Application Tests:

```bash
pytest test_flask_app.py -v
```

#### Frontend UI Tests (requires ChromeDriver)

```bash
pytest test_frontend_ui.py -v --selenium
```

#### Integration Tests

```bash
pytest test_integration.py -v --integration
```

#### Run with Coverage Report

```bash
pytest --cov=matrix_game --cov-report=term-missing
```

## Prerequisites

- Python 3.8+
- Chrome browser (for Selenium tests)
- ChromeDriver installed and in PATH
