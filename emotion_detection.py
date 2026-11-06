import cv2
from fer import FER

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize FER detector
detector = FER(mtcnn=True)

# List of emotions we care about
allowed_emotions = ["happy", "sad", "angry", "neutral"]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions
    result = detector.detect_emotions(frame)

    for face in result:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]

        # Filter only allowed emotions
        filtered_emotions = {k: v for k, v in emotions.items() if k in allowed_emotions}

        # Get dominant emotion among allowed ones
        if filtered_emotions:
            dominant_emotion = max(filtered_emotions, key=filtered_emotions.get)
        else:
            dominant_emotion = "neutral"

        # Draw rectangle and label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, dominant_emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Show video
    cv2.imshow("Emotion Detector", frame)

    # Quit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()