# Code-demo
# Enhancing security through computer vision

## Project Overview
This project uses the YOLO model from Ultralytics to detect violent activities in video streams. The detected instances are cropped and saved as separate images.
For full overview you can check the project file "integerated.pdf"

## Installation Instructions
To set up this project locally:

1. **Clone the repository**:
   ```sh
   https://github.com/Benjamin4103/Code-demo.git
   cd violence_detection

2. **Create a virtual environment**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**:
```sh
pip install 
```
4. **Download the YOLO model file**:

Place the ViolenceDetection.pt model file in the project directory.

5. **To run this project**:

Ensure you have a webcam connected or adjust the video source in main.py.
Run the script
```
python main.py
```
6. **Dependencies**
The project relies on the following dependencies:
ultralytics
opencv-python-headless

Contact
For any questions or feedback, feel free to contact me at Kareernirmit@gmail.com
