from flask import Flask, jsonify, request, session
from flask_cors import CORS
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, supports_credentials=True)

@app.route('/api/new-game', methods=['POST'])
def new_game():
    """Start a new game with a random number between 1 and 100"""
    session['target_number'] = random.randint(1, 100)
    session['attempts'] = 0
    session['game_over'] = False
    return jsonify({
        'message': 'New game started! Guess a number between 1 and 100.',
        'attempts': 0,
        'game_over': False
    })

@app.route('/api/guess', methods=['POST'])
def make_guess():
    """Process a user's guess"""
    if 'target_number' not in session:
        return jsonify({'error': 'No active game. Start a new game first.'}), 400
    
    if session.get('game_over', False):
        return jsonify({'error': 'Game is over. Start a new game.'}), 400
    
    data = request.get_json()
    
    if not data or 'guess' not in data:
        return jsonify({'error': 'No guess provided'}), 400
    
    try:
        guess = int(data['guess'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input. Please enter a number.'}), 400
    
    if guess < 1 or guess > 100:
        return jsonify({'error': 'Please enter a number between 1 and 100.'}), 400
    
    session['attempts'] = session.get('attempts', 0) + 1
    target = session['target_number']
    
    if guess < target:
        hint = 'Too low! Try a higher number.'
        game_over = False
    elif guess > target:
        hint = 'Too high! Try a lower number.'
        game_over = False
    else:
        hint = f'Correct! You guessed the number in {session["attempts"]} attempts!'
        game_over = True
        session['game_over'] = True
    
    return jsonify({
        'hint': hint,
        'attempts': session['attempts'],
        'game_over': game_over,
        'guess': guess
    })

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get current game status"""
    if 'target_number' not in session:
        return jsonify({
            'active_game': False,
            'message': 'No active game'
        })
    
    return jsonify({
        'active_game': True,
        'attempts': session.get('attempts', 0),
        'game_over': session.get('game_over', False)
    })

@app.route('/')
def index():
    """Serve the main page"""
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
