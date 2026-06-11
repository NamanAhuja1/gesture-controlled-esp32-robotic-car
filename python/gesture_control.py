import cv2
import mediapipe as mp
import serial
import time

# ==============================
# ESP32 SERIAL CONNECTION
# ==============================
# Change COM5 to your ESP32 port
esp = serial.Serial('COM5', 115200)
time.sleep(2)

# ==============================
# MEDIAPIPE SETUP
# ==============================
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

# ==============================
# WEBCAM
# ==============================
cap = cv2.VideoCapture(0)

last_command = ""

# ==============================
# FINGER DETECTION
# ==============================
def finger_status(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    finger_bases = [6, 10, 14, 18]

    status = []

    for tip, base in zip(finger_tips, finger_bases):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[base].y:
            status.append(1)
        else:
            status.append(0)

    return status

# ==============================
# SEND COMMAND
# ==============================
def send_command(command):
    global last_command

    if command != last_command:
        esp.write((command + "\n").encode())
        print("Sent:", command)
        last_command = command

# ==============================
# MAIN LOOP
# ==============================
while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    gesture = "No Hand"

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            status = finger_status(hand_landmarks)

            # ------------------------
            # GESTURE MAPPING
            # ------------------------

            if status == [0, 0, 0, 0]:
                gesture = "STOP"
                send_command("stop")

            elif status == [1, 1, 1, 1]:
                gesture = "FORWARD"
                send_command("forward")

            elif status == [1, 1, 0, 0]:
                gesture = "LEFT"
                send_command("left")

            elif status == [1, 1, 1, 0]:
                gesture = "RIGHT"
                send_command("right")

            elif status == [1, 0, 0, 0]:
                gesture = "BACKWARD"
                send_command("backward")

            else:
                gesture = "UNKNOWN"

            cv2.putText(
                frame,
                gesture,
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    else:
        send_command("stop")

    cv2.imshow("Gesture Controlled Car", frame)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break

# ==============================
# CLEANUP
# ==============================
cap.release()
cv2.destroyAllWindows()
esp.close()
