import cv2
import mediapipe as mp

from google.protobuf.json_format import MessageToDict
mphands = mp.solutions.hands
hands = mphands.Hands(
    static_image_mode=False,
    model_complexity=1,
    max_num_hands=2,
    min_tracking_confidence=0.75,
    min_detection_confidence=0.75)
cap = cv2.VideoCapture(0)
while True :
    success, image = cap.read()
    img = cv2.flip(image, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if len(results.multi_handedness) == 2:
        cv2.putText(img, "Both Hands", (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    else:
        for i in results.multi_handedness:
            label = MessageToDict(i)['classification'][0]['label']
            if label == 'Right':
                cv2.putText(img, label+"Hand", (460, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv2.putText(img, label+"Hand", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
