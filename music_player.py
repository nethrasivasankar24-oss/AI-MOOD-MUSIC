import cv2
from fer import FER
import webbrowser
import time
from emotion_music import get_playlist

print("Enter your preferred language (ISO code):")
print("Options: 'en' = English, 'hi' = Hindi, 'ko' = Korean, 'ta' = Tamil")
user_language = input().strip().lower()

cap = cv2.VideoCapture(0)
detector = FER(mtcnn=True)

allowed_emotions = ["happy", "sad", "angry", "neutral"]

last_emotion = None
last_open_time = 0

cooldown = 30   # << 1 minute cooldown

emotion_history = []
history_limit = 15   # more stable detection

print("Starting Emotion-Based Music Player! Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detector.detect_emotions(frame)

    for face in faces:
        (x, y, w, h) = face["box"]
        emotions = {k: v for k, v in face["emotions"].items() if k in allowed_emotions}

        # Find dominant emotion
        if emotions:
            dominant_emotion = max(emotions, key=emotions.get)
        else:
            dominant_emotion = "neutral"

        # Draw Rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, dominant_emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Add to history
        emotion_history.append(dominant_emotion)
        if len(emotion_history) > history_limit:
            emotion_history.pop(0)

        # Stable emotion (most common)
        stable_emotion = max(set(emotion_history), key=emotion_history.count)

        current_time = time.time()

        # ⬇⬇ DETECT & PLAY SONG ONLY EVERY 60 SECONDS ⬇⬇
        if (stable_emotion != last_emotion) and ((current_time - last_open_time) > cooldown):
            playlist_url = get_playlist(stable_emotion, user_language)
            webbrowser.open(playlist_url)

            print(f"Stable Emotion: {stable_emotion} → Playing playlist...")

            last_emotion = stable_emotion
            last_open_time = current_time

    cv2.imshow("Emotion Music Player", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()