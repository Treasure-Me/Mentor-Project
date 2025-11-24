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
        # THEY COMPLETE: Prepare level data for the template
        return render_template('game_board.html', level=level_data)
    return "Level not found!"

@app.route('/check_solution', methods=['POST'])
def check_solution():
    """
    CHALLENGE 4: Validate player's matrix multiplication
    Expected JSON: {'matrices': [A, B, C, ...]} 
    """
    data = request.json
    matrices = data.get('matrices', [])
    current_level = session.get('current_level', 0)
    target = game.levels[current_level]['target']
    
    # TODO: Implement solution checking logic
    # Multiply all matrices in order and compare with target
    
    return jsonify({'correct': False, 'message': 'Implement this!'})

@app.route('/hint')
def get_hint():
    """Provide algorithmic hints"""
    level = session.get('current_level', 0)
    # TODO: Generate helpful hints based on level difficulty
    return jsonify({'hint': 'Think about matrix dimensions first!'})

if __name__ == '__main__':
    # app.run() = app.start()
    app.run(debug=True, host='0.0.0.0', port=5000)