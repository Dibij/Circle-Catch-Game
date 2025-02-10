# Hand Tracking Game  

## Overview  
Hand Tracking Game is an interactive computer vision-based game that uses OpenCV and a Haar Cascade classifier to detect hands. The goal is to "catch" a randomly appearing circle by placing your hand over it. The game also includes a scoring system and a game timer.  

## Features  
- **Hand Detection**: Uses Haar Cascades to detect hands in real-time.  
- **Interactive Gameplay**: A circle appears at random positions, and players must cover it with their hand to score points.  
- **Score Tracking**: Keeps track of the player's score.  
- **Game Timer**: The game runs for a fixed duration before displaying the final score.  
- **Video Recording (Commented Out)**: The script originally included a video recording feature, but it has been commented out. If needed, you can uncomment the relevant sections in `src/main.py`.  
- **Automatic File Management**: If enabled, recorded videos are saved sequentially in `data/videos`.  

## Installation  

### Prerequisites  
- Python 3.x  

### Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/Hand-Tracking-Game.git
   cd Hand-Tracking-Game
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Ensure that the Haar Cascade file (`hand.xml`) is in the correct directory.  

## Usage  

Navigate to the `src` directory and run the game:  
```bash
cd src  
python main.py  
```  

### Controls  
- **Hand Movement**: Move your hand over the circle to score points.  
- **Quit**: Close the window to exit.  

### Optional (If You Uncomment Video Recording)  
- **Start/Stop Recording**: Press `V`  
- **Pause/Resume Recording**: Press `P`  

## File Structure  
```
Hand-Tracking-Game/
│── data/
│   ├── videos/        # Directory for saved videos (if enabled)
│   ├── scores.txt     # Stores final scores of each session
│── src/
│   ├── main.py        # Main game script
│── hand.xml           # Haar Cascade file for hand detection
│── requirements.txt   # Required dependencies
│── README.md          # Documentation
```

## Notes  
- The video recording feature has been **commented out** in `src/main.py`. If you want to enable it, remove the comments from the relevant sections.  
- The game uses OpenCV’s Haar Cascade method for hand detection, which may need adjustments for better accuracy.  

## License  
This project is open-source. Feel free to modify and improve it!  