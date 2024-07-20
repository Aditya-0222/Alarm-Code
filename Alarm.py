import cv2
import dlib
import numpy as np
from playsound import playsound
import threading

# Load pre-trained models
face_detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(dlib.data.shape_predictor_68_face_landmarks)

# EAR computation
def calculate_ear(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Parameters
EAR_THRESHOLD = 0.25
EAR_CONSECUTIVE_FRAMES = 15
ALARM_FILE = 'alarm.mp3'  # Path to your alarm sound file

# Initialize variables
frame_count = 0
alert_active = False

# Function to play alarm sound
def play_alarm():
    playsound(ALARM_FILE)

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])
        
        # Extract eye landmarks
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]
        
        # Compute EAR for both eyes
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        
        # Average EAR for both eyes
        ear = (left_ear + right_ear) / 2.0
        
        # Check if the EAR is below the threshold
        if ear < EAR_THRESHOLD:
            frame_count += 1
            if frame_count >= EAR_CONSECUTive_FRAMES:
                if not alert_active:
                    print("Alert: Driver may be drowsy!")
                    # Trigger the alarm in a separate thread
                    threading.Thread(target=play_alarm).start()
                    alert_active = True
        else:
            frame_count = 0
            if alert_active:
                print("Driver is awake.")
                # You can stop the alarm here if needed
                alert_active = False
        
        # Draw landmarks and EAR on the frame
        for (x, y) in landmarks:
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        
    cv2.imshow('Driver Monitoring System', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
