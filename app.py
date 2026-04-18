from flask import Flask, render_template, request, session, jsonify
from matrix_lib import MatrixGame
import json

app = Flask(__name__)
app.secret_key = 'matrix_secret'
game = MatrixGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/levels')
def level_select():
    """Level selection page"""
    return render_template('level_select.html')

@app.route('/level/<int:level_id>')
def load_level(level_id):
    """Load a specific game level"""
    if level_id < len(game.levels):
        session['current_level'] = level_id
        level_data = game.levels[level_id]
        return render_template('game_board.html', level=level_data)
    return "Level not found!", 404

@app.route('/check_solution', methods=['POST'])
def check_solution():
    """
    Validate player's matrix multiplication
    Expected JSON: {'matrices': [A, B, C, ...]} 
    """
    data = request.json
    user_matrices = data.get('matrices', [])
    
    if not user_matrices:
        return jsonify({'correct': False, 'message': 'No matrices provided.'})
        
    current_level = session.get('current_level', 0)
    
    # Safety check to ensure level exists
    if current_level >= len(game.levels):
        return jsonify({'correct': False, 'message': 'Invalid level.'})
        
    level_data = game.levels[current_level]
    input_matrix = level_data['input']
    target_matrix = level_data['target']
    
    # Start with the original input matrix
    current_result = input_matrix
    
    # Multiply all matrices in order
    for matrix in user_matrices:
        current_result = game.multiply_matrices(current_result, matrix)
        
        # multiply_matrices returns None if dimensions are incompatible
        if current_result is None:
            return jsonify({
                'correct': False, 
                'message': 'Dimension mismatch! Check your rows and columns.'
            })
    
    # Compare final result with target using the tolerance check method
    if game.is_matrix_equal(current_result, target_matrix):
        return jsonify({'correct': True, 'message': 'Matrix Matched! Excellent work.'})
    else:
        return jsonify({'correct': False, 'message': 'Transformation incorrect. Try again!'})

@app.route('/hint')
def get_hint():
    """Provide algorithmic hints based on the current level"""
    current_level = session.get('current_level', 0)
    
    if current_level < len(game.levels):
        # Fetch the specific hint defined in the _init_levels dictionary
        level_hint = game.levels[current_level].get('hint', 'Think about matrix dimensions first!')
        return jsonify({'hint': level_hint})
        
    return jsonify({'hint': 'No hint available for this level.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)