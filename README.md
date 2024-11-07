# AI-Based Arm Control and Face Recognition System

This project implements an AI-driven arm control system with face recognition capabilities, designed to interact with guests or manage items using the Dofbot robotic arm. It recognizes registered faces, performs actions such as placing and retrieving items based on detected individuals, and interacts via IPython widgets.

## Features

- **Face Recognition**: Identifies previously registered faces and associates them with specific actions.
- **Dofbot Arm Control**: Controls the robotic arm for placing and retrieving items based on recognized faces.
- **Interactive UI**: IPython widgets for controlling arm actions, such as "Place", "Retrieve", and "Exit".
- **Real-time Video Feed**: Displays live video feed with face detection.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-arm-control-face-recognition.git
   cd ai-arm-control-face-recognition
Install dependencies:

```bash
pip install -r requirements.txt
```
Set up known faces:

New faces will be registered to the known_faces directory. These will be used for face recognition.
Run the code in a Jupyter Notebook or Jupyter Lab environment.
