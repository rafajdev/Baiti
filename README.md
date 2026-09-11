# Bot Algorithm for Intelligent Tasks and Interactions

A voice-controlled robotic arm built with Python, Arduino and the Gemini API.

The project was developed for a school project and combines voice commands, computer vision and an Arduino-controlled robotic arm. It can execute predefined movements, control an LED and use a camera to identify colored blocks and interact with them.

## Features

* Voice commands
* Robotic arm and gripper control
* Gemini API integration for command interpretation
* Speech recognition
* Camera input and image recognition with OpenCV
* RGB LED control
* Automatic block identification and sorting by color
* Custom commands

## Hardware

The project uses:

* Arduino
* 2 breadboards
* RGB LED
* 3 LED resistors
* Jumper wires
* Voltage regulator
* Acrylic robotic arm kit
* 4 servo motors

## Requirements

* Python 3.8+
* Arduino
* A configured Gemini API key
* Python packages listed in `requirements.txt`

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Bot-Algorithm-for-Intelligent-Tasks-and-Interactions.git
cd Bot-Algorithm-for-Intelligent-Tasks-and-Interactions
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Create an `.env` file inside the `src` directory and add your Gemini API key:

```env
GOOGLE_API_KEY=your_api_key
```

Run the project:

```bash
python main.py
```

## Commands

The voice commands are currently in Portuguese.

* `Ligar LED` - Turns the LED on
* `Desligar LED` - Turns the LED off
* `Frente` - Moves the robot forward
* `Atrás` - Moves the robot backward
* `Esquerda` - Moves the robot to the left
* `Direita` - Moves the robot to the right
* `Diagonal esquerda` - Moves diagonally to the left
* `Diagonal direita` - Moves diagonally to the right
* `Cima` - Moves the arm up
* `Baixo` - Moves the arm down
* `Abrir garra` - Opens the gripper
* `Fechar garra` - Closes the gripper
* `Teste` - Runs the arm test routine
* `Ajuda` - Displays the command list (outdated)
* `Modo bloco` - Starts block mode, which identifies and sorts blocks according to their color
* `Modo camera` - Starts camera mode for capturing and analyzing images

## Troubleshooting

If the project is not working as expected:

* Check that the Arduino and robotic arm are connected correctly.
* Check that the Gemini API key is configured in the `.env` file.
* Make sure the required Python packages are installed.
* Check that speech recognition and the camera are working correctly.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
