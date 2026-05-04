import cv2
from preprocessing import preprocess_frame
from feature_extraction import get_center
from evaluation import evaluate_tracking

cap = cv2.VideoCapture("car-detection.mp4")
cap.set(cv2.CAP_PROP_POS_FRAMES, 60)

tracker = cv2.TrackerCSRT_create()

ret, frame = cap.read()

bbox = (260, 230, 160, 120)
tracker.init(frame, bbox)

trajectory = []
success_count = 0
total_frames = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    total_frames += 1

    processed = preprocess_frame(frame)

    success, bbox = tracker.update(frame)

    if success:
        success_count += 1
        x, y, w, h = map(int, bbox)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        cx, cy = get_center(x, y, w, h)
        trajectory.append((cx, cy))

        if len(trajectory) > 50:
            trajectory.pop(0)

        for i in range(1, len(trajectory)):
            cv2.line(frame, trajectory[i-1], trajectory[i], (0,0,255), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

evaluate_tracking(success_count, total_frames)