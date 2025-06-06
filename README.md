# Self-Driving Car Simulation Using NEAT and Pygame

## Author
**Saad Shabbir**  
**Developed at HeadQuarters at S.T.A.G LLC**

## Overview
This project is a self-driving car simulation developed using **Python**, **Pygame**, and **NEAT (NeuroEvolution of Augmenting Topologies)**. The simulation demonstrates how an AI-controlled car learns to navigate a track, avoid obstacles, and optimize its performance through evolutionary algorithms.

## Features
- **Neural Network:** Uses NEAT to evolve neural networks that control the car's movements.
- **Real-time Simulation:** Visualizes car behavior in a dynamic environment.
- **Sensor (Radar) Integration:** The car uses virtual sensors to detect distances to obstacles.
- **Collision Detection:** Crashes are detected when the car touches the track borders.
- **Adjustable Parameters:** Easy to modify the car's speed, radar angles, and track design.

## Technologies Used
- **Python**
- **Pygame**
- **NEAT-Python**

## Installation
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies:**
   ```bash
   pip install pygame neat-python
   ```

3. **Add Required Assets:**
   - `car.png` - Sprite image for the car.
   - `map.png` - The track layout for the simulation.

## How to Run
```bash
python <filename>.py
```

The simulation will start in full-screen mode. Press `Esc` or close the window to exit.

## Controls
The car is controlled automatically by the neural network. However, you can observe:
- **Generation Count:** Displays the current generation of the evolving AI.
- **Cars Alive:** Shows the number of cars still active in the simulation.

## Configuration
You can modify the following constants in the script to adjust the simulation:
```python
WIDTH = 1280
HEIGHT = 1024
CAR_SIZE_X = 60
CAR_SIZE_Y = 60
BORDER_COLOR = (255, 255, 255, 255)
```

## Project Structure
```
├── car.png         # Car sprite image
├── map.png         # Track map image
├── newcar.py         # Main simulation script
├── config-feedforward.txt # NEAT configuration file
└── README.md       # Project documentation
```

## NEAT Configuration
Make sure to adjust the `config-feedforward.txt` file to fine-tune the neural network parameters:
- **Population Size**
- **Number of Inputs/Outputs**
- **Mutation Rates**

## Troubleshooting
- **Pygame Full-Screen Issues:** Modify `pygame.display.set_mode()` if the screen doesn't fit your display.
- **Performance Lag:** Reduce the car speed or decrease the simulation resolution.
- **Collision Detection Issues:** Ensure `BORDER_COLOR` matches the track border color in `map.png`.

## Future Improvements
- Adding complex tracks with dynamic obstacles.
- Implementing multi-car racing scenarios.
- Enhancing the neural network with recurrent connections.

## License
This project is licensed under **MIT License**.

## Acknowledgments
- Inspired by projects from **Cheesy AI**.
- This README file was written using a GPT (Generative Pre-trained Transformer) tool.
- Created at  **S.T.A.G LLC** HeadQuarters.

---
**"Precision in Every Byte."**

