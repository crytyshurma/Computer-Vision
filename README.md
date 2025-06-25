# Smart Face Detection System

A Python-based computer vision project that detects faces and smiles in real-time using OpenCV. It automatically captures images on smile detection, logs events, and supports manual captures.

## Project Details
- Name: Smart Face Detection System  
- Technology Stack: Python 3.x, OpenCV, Haarcascade pre-trained models  
- Tools: Webcam, CSV logging, OBS Studio / Clipchamp for demo recording  

## Features
- Real-time face detection using Haarcascade  
- Smile detection with automatic image capture  
- Live face count overlay on video feed  
- Manual image capture using the `s` key  
- Smile events logged in `smile_log.csv` with timestamps and face count  
- Images saved with timestamp-based filenames  

## Setup & Usage
1. Install dependencies:
pip install opencv-python

markdown
Copy
Edit
2. Run the script:
python face_detection.py

markdown
Copy
Edit
3. Controls:
- Press `q` to quit  
- Press `s` to manually save the current frame  
4. Outputs:
- Auto-saved smile images appear in `captured_images/`  
- `smile_log.csv` is updated with each smile event  

## How It Works
- Captures video frames from the webcam  
- Converts frames to grayscale for detection  
- Detects faces and draws bounding boxes  
- Detects smiles within each face region  
- On smile detection:
- Saves image as `smile_<timestamp>.jpg`  
- Logs the event in `smile_log.csv`  
- Displays live face count overlay  
- Supports manual capture via the `s` key  

## Challenges & Solutions
- Prevented repeated saves during continuous smiles using a break condition  
- Tuned detection parameters to handle varying lighting conditions  
- Optimized detection loops for smooth real-time performance  

## Applications
- Contactless photo booths  
- Basic emotion recognition  
- Real-time monitoring in public or office spaces  

## Demo
Check the folder and the presentation for output screenshots and demo images.

## Author
Kriti Sharma (Roll No. 102316019)  
Developed complete system: coding, testing, and demo recording  
