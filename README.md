# Space Invaders Game - README

## Description
This project is a simple 2D Space Invaders game built using the Python `pygame` library. In this game, the player controls a spaceship and has to shoot down enemies while avoiding being hit. The game features background music, sound effects, and multiple levels of difficulty.

### Key Features:
- **Player Movement**: The player controls a spaceship that can move left and right using the arrow keys.
- **Shooting Mechanism**: The player can shoot bullets upwards to destroy enemy spaceships.
- **Enemies**: The game contains multiple enemies that move across the screen. When an enemy is hit by a bullet, it is respawned at a random position, and the player scores points.
- **Collision Detection**: The game checks for collisions between bullets and enemies and updates the score.
- **Sound Effects**: The game includes background music and sound effects for shooting and hitting enemies.
- **Score**: The score increases each time the player hits an enemy.

## Prerequisites
Before running the game, ensure that the following are installed on your system:
- Python (version 3.x)
- `pygame` library

### Installing Pygame:
To install `pygame`, run the following command:
```bash
pip install pygame
```

## File Structure
- **main.py**: The main game logic, where all the functionality is implemented.
- **images/**: Folder containing image assets:
  - `background.png`: The background image for the game.
  - `icon.png`: The icon displayed in the game window.
  - `player.png`: The image of the player's spaceship.
  - `enemy.png`: The image of the enemy spaceship.
  - `bullet.png`: The image of the bullet shot by the player.
- **sounds/**: Folder containing sound files:
  - `Pixel Love.mp3`: Background music that plays throughout the game.
  - `shoot.wav`: Sound effect when the player shoots a bullet.
  - `hit.mp3`: Sound effect when a bullet hits an enemy.
  
## How to Play
1. **Run the Game**:
   To start the game, simply run the `main.py` script using the command:
   ```bash
   python main.py
   ```

2. **Control the Player**:
   - **Move Left**: Press the **Left Arrow** key.
   - **Move Right**: Press the **Right Arrow** key.
   - **Shoot**: Press the **Up Arrow** key to shoot a bullet.

3. **Objective**:
   The goal is to destroy as many enemies as possible while avoiding collisions with them. Each time you destroy an enemy, your score increases.

4. **Collision Detection**:
   - When a bullet collides with an enemy spaceship, the enemy is destroyed, and a sound effect plays. The player earns one point for each enemy hit.
   - If the bullet moves out of the screen without hitting anything, it is reset to its original position.

5. **Background Music & Sound Effects**:
   - The game includes background music that plays continuously.
   - Sound effects play when the player shoots and when an enemy is hit.

## Game Logic
- **Player Movement**: The player's spaceship can be moved left or right, and its movement is bounded within the screen limits.
- **Enemy Movement**: Enemies move across the screen from left to right, and when they reach the edge, they change direction and move downward.
- **Bullet Movement**: The bullet moves upwards from the player's spaceship when the **Up Arrow** key is pressed.
- **Collision Detection**: The distance between the bullet and enemy is calculated, and if it is small enough, a collision is detected, and the enemy is reset.

## Future Improvements
- **Levels and Difficulty**: Implementing multiple levels with increasing difficulty, more enemies, and faster movements.
- **Lives**: Adding a life system where the player can lose lives upon being hit by an enemy.
- **Game Over Screen**: Displaying a game over screen with the final score when the player loses all their lives.

## License
This project is open-source and is available under the MIT License.

## Acknowledgements
- **pygame**: Used to create the graphical elements and handle the game logic.
- **Images and Sounds**: All images and sound files used in this project are created for this game.

Enjoy playing and have fun!
