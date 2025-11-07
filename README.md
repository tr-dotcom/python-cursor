# 🎯 Number Guessing Game

A simple interactive number guessing game built with Python (Flask) backend and HTML/JavaScript frontend.

## Features

- 🎲 Random number generation between 1 and 100
- 💡 Real-time hints ("Too high", "Too low", "Correct!")
- ✅ Input validation (numbers only, range 1-100)
- 📊 Attempt counter
- 🔄 Restart functionality after winning
- 🎨 Beautiful, responsive UI with gradient background
- ⚡ RESTful API architecture

## Project Structure

```
.
├── app.py                 # Flask backend with game logic
├── requirements.txt       # Python dependencies
├── static/
│   └── index.html        # Frontend interface
└── README.md             # This file
```

## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setup

1. **Install pip** (if not already installed):
   ```bash
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python3 get-pip.py
   ```

2. **Install dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

## Running the Game

1. **Start the Flask server**:
   ```bash
   python3 app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Play the game**:
   - Click "New Game" to start
   - Enter a number between 1 and 100
   - Click "Submit Guess" or press Enter
   - Follow the hints to find the correct number
   - Try to guess in as few attempts as possible!

## API Endpoints

The backend provides the following REST API endpoints:

### `POST /api/new-game`
Starts a new game with a random number between 1 and 100.

**Response:**
```json
{
  "message": "New game started! Guess a number between 1 and 100.",
  "attempts": 0,
  "game_over": false
}
```

### `POST /api/guess`
Submits a guess and receives feedback.

**Request Body:**
```json
{
  "guess": 50
}
```

**Response:**
```json
{
  "hint": "Too high! Try a lower number.",
  "attempts": 1,
  "game_over": false,
  "guess": 50
}
```

### `GET /api/status`
Gets the current game status.

**Response:**
```json
{
  "active_game": true,
  "attempts": 3,
  "game_over": false
}
```

## Game Logic

1. **Random Number Generation**: When a new game starts, the server generates a random number between 1 and 100
2. **Input Validation**: 
   - Only accepts numbers
   - Must be between 1 and 100
   - Provides clear error messages for invalid input
3. **Comparison Logic**:
   - If guess < target: "Too low! Try a higher number."
   - If guess > target: "Too high! Try a lower number."
   - If guess == target: "Correct! You guessed the number in X attempts!"
4. **Session Management**: Uses Flask sessions to maintain game state across requests
5. **Attempt Tracking**: Counts and displays the number of guesses made

## Technologies Used

### Backend
- **Flask**: Lightweight Python web framework
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **Python Random**: Random number generation

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with gradients and animations
- **JavaScript (Vanilla)**: Game logic and API communication
- **Fetch API**: Asynchronous HTTP requests

## Features Demonstrated

✅ Random number generation (1-100)  
✅ User input validation (numbers only)  
✅ Real-time feedback (Too high/Too low/Correct)  
✅ Attempt counter  
✅ Restart functionality  
✅ Session-based state management  
✅ RESTful API design  
✅ Responsive UI design  
✅ Error handling  
✅ Clean, beginner-friendly code  

## Development Notes

- The Flask server runs in debug mode for development
- Sessions are used to maintain game state
- CORS is enabled for local development
- The frontend uses inline CSS and JavaScript for simplicity
- All validation happens on both client and server side

## Future Enhancements

- Add difficulty levels (different number ranges)
- Implement a leaderboard
- Add sound effects
- Create a multiplayer mode
- Add hints after certain number of attempts
- Implement a timer for speed challenges

## License

This project is open source and available for educational purposes.

---

**Enjoy the game! 🎮**
