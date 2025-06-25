# Smart Face Detection with Smile Logging
import cv2
import datetime
import csv
import os

# Loading  Haarcascade models

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Initialize webcam

cap = cv2.VideoCapture(0)

# Create log file if not exists

log_file = 'smile_log.csv'
if not os.path.exists(log_file):
    with open(log_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Faces Detected', 'Smile'])

print("[INFO] Press 'q' to quit | Press 's' to manually save frame")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Display face count
    cv2.putText(frame, f'Faces detected: {len(faces)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Detect smiles inside face region

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"smile_{timestamp}.jpg"
            cv2.imwrite(filename, frame)

            # Log to CSV
            
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, len(faces), 'Smile Detected'])

            print(f"[INFO] Smile detected! Saved: {filename}")
            break  # Save only once per smile

    cv2.imshow('Smart Face Detection - Press q to quit', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"manual_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"[INFO] Manual save: {filename}")

cap.release()
cv2.destroyAllWindows()
