import time
import keyboard
import winsound

def check_head_position():
    # Simulate head movements (left and right arrow keys)
    while True:
        if keyboard.is_pressed('left') or keyboard.is_pressed('right'):
            print("Driver is awake!")
        else:
            print("Driver might be dozing off! Beeping...")
            # Beep sound to alert the driver
            winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms
        
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    print("Starting Anti-Sleep Alarm System...")
    print("Press 'left' or 'right' arrow keys to simulate head movements.")
    check_head_position()
