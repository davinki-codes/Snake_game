# HUNGWY HUNGWY SNAKE 🐍

A classic Snake game built with Python's Turtle graphics library. Guide your snake to eat food, grow longer, and beat your high score!

## Features

- **Classic Snake Gameplay**: Control the snake using arrow keys to collect food
- **High Score Tracking**: Your best score is automatically saved and persists between game sessions
- **Auto-Reset**: Game automatically restarts when you hit a wall or bite your tail
- **Visual Feedback**: "nom nom" appears when you eat food
- **Growing Snake**: Snake grows longer with each piece of food eaten

## Requirements

- Python 3.x
- Turtle graphics library (comes pre-installed with Python)

## Files

- `main.py` - Main game loop and collision detection
- `snake_functioning.py` - Snake class with movement and growth logic
- `food.py` - Food class for random food placement
- `scoreboard_snake.py` - Score display and high score management
- `snake_spies.py` - Visual text elements (title and "nom nom" effects)
- `data.txt` - Stores the high score (created automatically)

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. **Controls**:
   - **Up Arrow** - Move up
   - **Down Arrow** - Move down
   - **Left Arrow** - Move left
   - **Right Arrow** - Move right

3. **Objective**: Eat the green turtle-shaped food to grow your snake and increase your score

4. **Game Over Conditions**:
   - Hitting the boundary walls
   - Colliding with your own tail

5. The game automatically restarts after a collision, and your high score is saved

## Game Settings

- **Screen Size**: 600x600 pixels
- **Background**: Black
- **Snake Color**: White
- **Food Color**: Green
- **Starting Snake Length**: 3 segments
- **Movement Speed**: 0.1 second delay between moves

## High Score

Your high score is automatically saved to `data.txt` and will be displayed the next time you play. The current high score is **17**!

## Click Escape to Exit

Clicking Escape will automatically close the window. But your high score will be saved in the data.txt


Enjoy playing HUNGWY HUNGWY SNAKE! 🐍🎮
