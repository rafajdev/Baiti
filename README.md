# Bot Algorihm for Inteligent Tasks and Interactions 

## Description

This project implements a voice-controlled robot arm using the Gemini API. The robot is capable of performing various programmed actions in response to voice commands. Developed as part of a school project.

## Features

* Voice control of the robotic arm.
* Interaction with the Gemini API to interpret and respond to commands.
* Speech recognition system for processing verbal commands.
* LED light control, its possible to turn a LED light on and off.
* Pre-programmed commands to control the robot.
* Image recognition using OpenCV.
* Pre-programmed command to identify the color of a block, pick it up and place it in a specific location according to the color.
* Support for custom commands.
* Personalizable.

## Technologies Used

* Python: Main programming language of the project.
* SpeechRecognition: Library for speech recognition.
* Gemini API: Used to interpret the commands.
* Other features that are listed in `requirements.txt`.

## Electronic Equipment Used

* 1 Arduino: Used as a microcontroller.
* 2 breadboards: Used to connect the components.
* 1 RGB LED: Used to indicate the status of the robot.
* Jumper cables: Used to connect the components.
* 3 resistors for the LED: Used to limit the electric current.
* 1 voltage regulator: Used to stabilize the voltage.
* 1 acrylic robotic arm kit: Used as the structure of the robot.
* 4 servo motors: Used to move the robotic arm.

## Dependencies
To run the project, the following dependencies need to be installed:
* Python 3.8+.
* The libraries on: `requirements.txt`.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git`
```

2. Install the dependencies: 

```bash
`pip install -r requirements.txt`
```

3. Configure the Gemini API: obtain the API key and put it in an `.env` file on the `src` folder with the variable name `GOOGLE_API_KEY`.

4. Run the project: 

```bash
`python main.py`
```

## Commands

* "Ligar LED" - Turns on the robot's LED.
* "Desligar LED" - Turns off the robot's LED.
* "Frente" - Moves the robot forward.
* "Atrás" - Moves the robot backward.
* "Esquerda" - Turns the robot left.
* "Diagonal esquerda" - Moves the robot diagonally to the left.
* "Diagonal direita" - Moves the robot diagonally to the right.
* "Direita" - Turns the robot right.
* "Cima" - Moves the robot's arm up.
* "Baixo" - Moves the robot's arm down.
* "Abrir garra" - Opens the robot's gripper.
* "Fechar garra" - Closes the robot's gripper.
* "Teste" - Runs a test routine on the robot's arm.
* "Ajuda" - Prints the list of commands. (Outdated)
* "Modo bloco" - Enters block mode to pick according to the color of the block.
* "Modo camera" - Enters camera mode to take pictures and analyze them.

## Troubleshooting

* Check if the Gemini API is configured correctly.
* Check if the robot is connected to the Wi-Fi network.
* Check if the speech recognition system is working correctly.

## Contributions

Contributions are welcome! If you have any ideas or suggestions to improve the project, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to modify it as needed!
