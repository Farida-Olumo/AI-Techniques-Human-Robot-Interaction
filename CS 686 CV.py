import os
import cv2
import time
import threading
from deepface import DeepFace
#from furhat_remote_api import FurhatRemoteAPI

# --- SPEED FIXES ---
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# furhat_remote_api HERE 
furhat.attend(user="CLOSEST")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

latest_params = {}
running = True
last_gesture_time = 0
GESTURE_INTERVAL = 0.35   # send gesture max 3 times per second
ANALYZE_INTERVAL = 0.45   # analyze emotion twice per second

def cv_brain():
    """Runs DeepFace at a safe interval (fast + stable)."""
    global latest_params, running
    last_analyze = 0

    while running:
        ret, frame = cap.read()
        if not ret:
            continue

        now = time.time()
        if now - last_analyze < ANALYZE_INTERVAL:
            continue

        last_analyze = now

        try:
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False,
                detector_backend='opencv',
                silent=True
            )

            emotion = result[0]['dominant_emotion']
            score = min(result[0]['emotion'][emotion] / 100.0, 1.0)

            # --- MAPPING ---
            if emotion == "happy":
                latest_params = {"SMILE_OPEN": score}
            elif emotion == "surprise":
                latest_params = {"EYE_WIDE_LEFT": score, "EYE_WIDE_RIGHT": score}
            elif emotion in ["sad", "fear"]:
                latest_params = {"BROW_INNER_UP": score}
            elif emotion == "angry":
                latest_params = {"BROW_DOWN_LEFT": score, "BROW_DOWN_RIGHT": score}
            else:
                latest_params = {}

        except Exception:
            latest_params = {}

def mirror_loop(duration=6):
    """Mirrors expressions smoothly without lag."""
    global last_gesture_time

    start = time.time()
    while time.time() - start < duration:
        ret, frame = cap.read()
        if not ret:
            break

        now = time.time()
        if latest_params and (now - last_gesture_time > GESTURE_INTERVAL):
            furhat.gesture(body={
                "class": "furhatos.gestures.Gesture",
                "frames": [{"time": [0.3], "params": latest_params}]
            })
            last_gesture_time = now

        cv2.imshow("Mirror", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def smooth_mirror_and_listen(prompt, duration=6):
    furhat.say(text=prompt, blocking=True)
    furhat.listen()
    mirror_loop(duration)
    return "placeholder"

def start_session():
    threading.Thread(target=cv_brain, daemon=True).start()

    smooth_mirror_and_listen("Hello! To start, what is your name?")
    smooth_mirror_and_listen("Nice to meet you. Which department are you in?")
    smooth_mirror_and_listen("Tell me about your research projects for caregivers.")
    smooth_mirror_and_listen("What do you do to relax in your spare time?")
    smooth_mirror_and_listen("Finally, could you tell me a bit about your academic field?")

    furhat.say(text="Thank you for your time today!", blocking=True)

    global running
    running = False
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_session()
