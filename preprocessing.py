import cv2

def preprocess_frame(frame):
    # Resize
    frame = cv2.resize(frame, (640, 480))

    # Denoise
    blur = cv2.GaussianBlur(frame, (5,5), 0)

    # Enhance
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    enhanced = cv2.equalizeHist(gray)

    return enhanced