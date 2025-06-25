Smart Face & Smile Detection System

Developed by: Rupinder Kaur(102316129)
Tool Used: Python 3.x, OpenCV

Overview:

This project performs real-time face detection using OpenCV and captures images automatically when a user smiles. It also provides a face count, manual image saving via key press, and logs smile events to a CSV file.

Files Included:

1. smart_face_detection.py  - Main Python script
2. smile_log.csv            - Logs of smile detections with timestamps
3. smile_*.jpg              - Auto-captured images on smile detection
4. manual_*.jpg             - Manually captured images (via 's' key)
5. readme.txt               - This file

How to Run the Code:

1. Make sure Python 3.x is installed.
2. Install OpenCV using pip if not installed:
   pip install opencv-python

3. Run the script:
   python smart_face_detection.py

4. Controls while running:
   - Show face to webcam: A blue rectangle appears.
   - Smile: A green rectangle appears and image is auto-saved.
   - Press 's': Manually save the current frame.
   - Press 'q': Quit the webcam and close the program.

Features Summary:

- Real-time face detection (blue box)
- Smile detection with auto-screenshot (green box)
- Manual save with 's' key
- Smile log stored in smile_log.csv
- Face count displayed on screen

Notes:

- Haarcascade XML models used for face and smile detection.
- Images saved with timestamp in file name for uniqueness.
- Make sure your camera permissions are enabled for Python.

