**Driver Drowsiness Detection System**
  This Python-based system provides real-time monitoring of driver drowsiness using computer vision techniques. Leveraging OpenCV and dlib, the system analyzes       video   feed to assess eye movements and detect potential drowsiness through the Eye Aspect Ratio (EAR). When drowsiness is detected, an alarm is triggered to      alert the      driver.

**Key Features:**

  **Real-Time Monitoring:** Utilizes a webcam to continuously monitor and analyze the driver's eye aspect ratio.
  **Drowsiness Detection:** Computes EAR from eye landmarks to determine if the driver is potentially drowsy.
  **Alarm Activation:** Plays an alarm sound if drowsiness is detected for a sustained period.
  **Multithreaded Alarm Handling:** Ensures non-blocking operation by playing the alarm sound on a separate thread.

**Dependencies:
**
  - opencv-python
  - dlib
  - numpy
  - playsound

**Setup Instructions:**

  1.Install the required Python packages.
  2. Ensure an appropriate alarm sound file (alarm.mp3) is available in the project directory or update the path in the ALARM_FILE variable.
  3.Execute the script using python <script_name>.py to start the drowsiness monitoring system.

**Usage:**
  Upon running the script, a video window will display the real-time feed. The system will automatically detect potential drowsiness and play an alert sound if       necessary.

**Note:** This script requires access to a webcam and may require adjustments to thresholds and parameters depending on specific use cases and environments.
